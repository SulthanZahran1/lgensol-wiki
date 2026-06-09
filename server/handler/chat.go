package handler

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"math"
	"net/http"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"
	"time"
	"unicode"
)

var wikilinkRe = regexp.MustCompile(`\[\[([^\]|]+)(?:\|[^\]]+)?\]\]`)

type pageEntry struct {
	slug  string
	title string
	ctype string
}

type ChatRequest struct {
	Message string `json:"message"`
	History []struct {
		Role    string `json:"role"`
		Content string `json:"content"`
	} `json:"history"`
}

type ChatResponse struct {
	Answer    string        `json:"answer"`
	Pages     []PageRef     `json:"pages"`
	Citations []CitationRef `json:"citations,omitempty"`
	Steps     []Step        `json:"steps"`
}

type Step struct {
	Action   string `json:"action"`
	Page     string `json:"page,omitempty"`
	Parent   string `json:"parent,omitempty"`
	Title    string `json:"title,omitempty"`
	SourceID string `json:"source_id,omitempty"`
	Path     string `json:"path,omitempty"`
	URL      string `json:"url,omitempty"`
	Details  string `json:"details,omitempty"`
}

type PageRef struct {
	Slug     string `json:"slug"`
	Title    string `json:"title"`
	Relation string `json:"relation,omitempty"`
}

type wikiSearchResult struct {
	Pages   []PageRef
	Scores  map[string]int
	Details string
}

type CitationRef struct {
	ID       string    `json:"id"`
	Path     string    `json:"path"`
	Title    string    `json:"title"`
	Date     string    `json:"date,omitempty"`
	Category string    `json:"category,omitempty"`
	URL      string    `json:"url,omitempty"`
	Snippet  string    `json:"snippet,omitempty"`
	Pages    []PageRef `json:"pages,omitempty"`
}

type ollamaReq struct {
	Model    string      `json:"model"`
	Messages []ollamaMsg `json:"messages"`
	Stream   bool        `json:"stream"`
}

type ollamaMsg struct {
	Role    string `json:"role"`
	Content string `json:"content"`
}

type ollamaResp struct {
	Choices []struct {
		Message struct {
			Content string `json:"content"`
		} `json:"message"`
	} `json:"choices"`
}

// stepCallback is called by reactLoop to push intermediate SSE events
type stepCallback func(action string, details map[string]string)

func ChatHandler(wikiDir, rawDir string) http.HandlerFunc {
	type pageEntry struct {
		slug  string
		title string
		ctype string
	}
	pageIndex := buildPageIndex(wikiDir)

	return func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, `{"error":"method not allowed"}`, http.StatusMethodNotAllowed)
			return
		}

		var req ChatRequest
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil || req.Message == "" {
			http.Error(w, `{"error":"invalid request"}`, http.StatusBadRequest)
			return
		}

		// Detect if client wants SSE (Accept header or ?stream=true)
		useSSE := strings.Contains(r.Header.Get("Accept"), "text/event-stream") || r.URL.Query().Get("stream") == "true"

		if !useSSE {
			// Legacy non-streaming path
			seedPages := searchWikiDetailed(wikiDir, req.Message, 3).Pages
			if len(seedPages) == 0 {
				seedPages = []PageRef{{Slug: "lg-energy-solution", Title: "LG Energy Solution", Relation: "default"}}
			}
			answer, allPages, citations, steps := reactLoop(wikiDir, rawDir, req.Message, seedPages, pageIndex, nil)
			resp := ChatResponse{Answer: answer, Pages: allPages, Citations: citations, Steps: steps}
			w.Header().Set("Content-Type", "application/json")
			json.NewEncoder(w).Encode(resp)
			return
		}

		// ── SSE streaming path ──
		w.Header().Set("Content-Type", "text/event-stream")
		w.Header().Set("Cache-Control", "no-cache")
		w.Header().Set("Connection", "keep-alive")
		flusher, ok := w.(http.Flusher)
		if !ok {
			http.Error(w, "streaming not supported", http.StatusInternalServerError)
			return
		}

		// Helper to send a status event
		sendStatus := func(action string, details map[string]string) {
			data, _ := json.Marshal(details)
			fmt.Fprintf(w, "event: status\ndata: %s\n\n", data)
			flusher.Flush()
		}

		searchResult := searchWikiDetailed(wikiDir, req.Message, 3)
		seedPages := searchResult.Pages
		if len(seedPages) == 0 {
			seedPages = []PageRef{{Slug: "lg-energy-solution", Title: "LG Energy Solution", Relation: "default"}}
			searchResult.Details += "\nNo scored match was found; using the LG Energy Solution overview as baseline context."
		}
		sendStatus("search", map[string]string{"action": "search", "details": searchResult.Details})
		for _, sp := range seedPages {
			details := fmt.Sprintf("Selected %s as baseline context because the search returned no scored match.", sp.Title)
			if score, ok := searchResult.Scores[sp.Slug]; ok {
				details = fmt.Sprintf("Matched %s (%s) with retrieval score %d.", sp.Title, sp.Slug, score)
			}
			sendStatus("discover", map[string]string{
				"action":  "discover",
				"page":    sp.Slug,
				"parent":  "__search__",
				"title":   sp.Title,
				"details": details,
			})
		}

		// Run the ReAct loop with callback
		answer, allPages, citations, steps := reactLoop(wikiDir, rawDir, req.Message, seedPages, pageIndex, func(action string, details map[string]string) {
			sendStatus(action, details)
		})

		// Send final done event
		final := map[string]interface{}{
			"answer":    answer,
			"pages":     allPages,
			"citations": citations,
			"steps":     steps,
		}
		finalData, _ := json.Marshal(final)
		fmt.Fprintf(w, "event: done\ndata: %s\n\n", finalData)
		flusher.Flush()
	}
}

func buildPageIndex(wikiDir string) []pageEntry {
	var idx []pageEntry
	filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() || !strings.HasSuffix(path, ".md") {
			return nil
		}
		rel, _ := filepath.Rel(wikiDir, path)
		parts := strings.SplitN(rel, string(filepath.Separator), 2)
		if len(parts) < 2 {
			return nil
		}
		slug := strings.TrimSuffix(info.Name(), ".md")
		title := extractTitleFromFile(path)
		idx = append(idx, pageEntry{slug: slug, title: title, ctype: parts[0]})
		return nil
	})
	return idx
}

func extractTitleFromFile(path string) string {
	content, err := os.ReadFile(path)
	if err != nil {
		return "Untitled"
	}
	s := string(content)
	if strings.HasPrefix(s, "---\n") {
		if end := strings.Index(s[4:], "\n---"); end >= 0 {
			for _, line := range strings.Split(s[4:4+end], "\n") {
				if strings.HasPrefix(line, "title: ") {
					t := strings.TrimSpace(line[7:])
					t = strings.Trim(t, `"'`)
					return t
				}
			}
		}
	}
	return "Untitled"
}

func reactLoop(wikiDir, rawDir, userQuestion string, seedPages []PageRef, pageIndex []pageEntry, onStep stepCallback) (string, []PageRef, []CitationRef, []Step) {
	var steps []Step
	visited := make(map[string]bool)
	pages := make([]PageRef, 0, len(seedPages))
	maxTurns := reactTurnLimit(len(pageIndex))
	context := make([]string, 0, maxTurns+3)
	allSlugs := make(map[string]string)
	loadedLinks := make(map[string][]string)
	loadedOrder := make([]string, 0, maxTurns+3)

	for _, p := range pageIndex {
		allSlugs[p.slug] = p.title
	}

	pushStep := func(s Step) {
		steps = append(steps, s)
		if onStep != nil {
			d := map[string]string{
				"action":  s.Action,
				"details": s.Details,
			}
			if s.Page != "" {
				d["page"] = s.Page
			}
			if s.Parent != "" {
				d["parent"] = s.Parent
			}
			if s.Title != "" {
				d["title"] = s.Title
			}
			if s.SourceID != "" {
				d["source_id"] = s.SourceID
			}
			if s.Path != "" {
				d["path"] = s.Path
			}
			if s.URL != "" {
				d["url"] = s.URL
			}
			onStep(s.Action, d)
		}
	}

	// Load seed pages
	for _, sp := range seedPages {
		if visited[sp.Slug] {
			continue
		}
		visited[sp.Slug] = true
		content := readPageContent(wikiDir, sp.Slug)
		if content == "" {
			continue
		}
		title := sp.Title
		if t, ok := allSlugs[sp.Slug]; ok {
			title = t
		}
		relation := sp.Relation
		if relation == "" {
			relation = "search"
		}
		context = append(context, fmt.Sprintf("--- Page: %s (slug: %s) ---\n%s", title, sp.Slug, content))
		pages = append(pages, PageRef{Slug: sp.Slug, Title: title, Relation: relation})
		links := extractWikilinks(content)
		loadedLinks[sp.Slug] = links
		loadedOrder = append(loadedOrder, sp.Slug)
		linkDetails := "no outgoing wikilinks"
		if len(links) > 0 {
			linkDetails = fmt.Sprintf("%d outgoing wikilinks: %s", len(links), strings.Join(links, ", "))
		}
		pushStep(Step{
			Action:  "read",
			Page:    sp.Slug,
			Parent:  "__search__",
			Title:   title,
			Details: fmt.Sprintf("Read %d characters from %s; %s.", len([]rune(content)), sp.Slug, linkDetails),
		})
	}

	// Build a compact page index string for the LLM
	var indexSb strings.Builder
	indexSb.WriteString("Available pages (slug → title):\n")
	typeGroups := make(map[string][]string)
	for _, p := range pageIndex {
		typeGroups[p.ctype] = append(typeGroups[p.ctype], fmt.Sprintf("  - %s → %s", p.slug, p.title))
	}
	for _, ctype := range []string{"entities", "concepts", "comparisons", "glossary"} {
		if entries, ok := typeGroups[ctype]; ok {
			indexSb.WriteString(fmt.Sprintf("[%s]\n", ctype))
			for _, e := range entries {
				indexSb.WriteString(e + "\n")
			}
		}
	}
	pageIndexStr := indexSb.String()

	loop := 0
	for loop < maxTurns {
		loop++

		pushStep(Step{
			Action: "think",
			Details: fmt.Sprintf(
				"Reviewing %d loaded wiki pages to decide whether to fetch another linked page or begin the answer (turn %d of %d).",
				len(context),
				loop,
				maxTurns,
			),
		})

		// Build the prompt
		var sb strings.Builder
		sb.WriteString("You are a battery technology expert exploring LG Energy Solution's wiki.\n\n")
		sb.WriteString("## Page Directory\n")
		sb.WriteString(pageIndexStr)
		sb.WriteString("\n")
		sb.WriteString("## Pages Loaded So Far\n")
		for _, c := range context {
			sb.WriteString(c)
			sb.WriteString("\n\n")
		}
		sb.WriteString("## User Question\n")
		sb.WriteString(userQuestion)
		sb.WriteString("\n\n")
		sb.WriteString("## Instructions\n")
		sb.WriteString("You are exploring pages to answer the question. You can:\n\n")
		sb.WriteString("1. FETCH a page by its slug to learn more — respond with ONLY a JSON object:\n")
		sb.WriteString("   {\"action\": \"fetch\", \"slug\": \"page-slug\", \"from\": \"loaded-parent-slug\", \"reason\": \"one-sentence decision summary\"}\n")
		sb.WriteString("   The from field must identify the loaded page whose content or wikilink led you to the new page.\n\n")
		sb.WriteString("2. ANSWER the question when you have enough context — respond with:\n")
		sb.WriteString("   {\"action\": \"answer\", \"reason\": \"one-sentence decision summary\"}\n\n")
		sb.WriteString("Rules:\n")
		sb.WriteString("- FETCH a page when you need specific information from it\n")
		sb.WriteString("- Pay attention to wikilinks [[like-this]] mentioned in pages — they point to related pages\n")
		sb.WriteString("- You can fetch at most one page per turn\n")
		sb.WriteString("- Use Korean terminology internally for search (리튬이온, 양극재, 음극재, 전해질 etc.)\n")
		sb.WriteString("- Keep track of which pages you've already loaded — don't fetch them again\n")
		sb.WriteString("- You have limited turns. Make each fetch count. ANSWER when you're confident.\n")
		sb.WriteString("- The reason field must be a concise explanation of the decision, not private chain-of-thought or a hidden reasoning transcript.\n")

		llmResp := callOllamaRaw(sb.String(), maxTurns*2+5)

		var parsed struct {
			Action string `json:"action"`
			Slug   string `json:"slug"`
			From   string `json:"from"`
			Reason string `json:"reason"`
		}

		jsonStart := strings.Index(llmResp, "{")
		jsonEnd := strings.LastIndex(llmResp, "}")
		if jsonStart >= 0 && jsonEnd > jsonStart {
			jsonStr := llmResp[jsonStart : jsonEnd+1]
			if err := json.Unmarshal([]byte(jsonStr), &parsed); err != nil {
				parsed.Action = ""
			}
		}

		if parsed.Action == "fetch" && parsed.Slug != "" {
			slug := parsed.Slug
			actualSlug := fuzzyFindSlug(allSlugs, slug)
			if actualSlug == "" {
				pushStep(Step{
					Action:  "think",
					Details: fmt.Sprintf("The requested page %q was not present in the page index, so the explorer will choose again.", slug),
				})
				continue
			}
			if visited[actualSlug] {
				pushStep(Step{
					Action:  "think",
					Page:    actualSlug,
					Title:   allSlugs[actualSlug],
					Details: fmt.Sprintf("%s was already loaded, so the explorer will choose a different page.", actualSlug),
				})
				continue
			}

			visited[actualSlug] = true
			content := readPageContent(wikiDir, actualSlug)
			if content == "" {
				pushStep(Step{
					Action:  "think",
					Page:    actualSlug,
					Title:   allSlugs[actualSlug],
					Details: fmt.Sprintf("%s could not be read, so the explorer will continue with the available evidence.", actualSlug),
				})
				continue
			}
			title := allSlugs[actualSlug]
			if title == "" {
				title = actualSlug
			}

			parentSlug := fuzzyFindSlug(allSlugs, parsed.From)
			if parentSlug == actualSlug || !visited[parentSlug] {
				parentSlug = ""
			}
			if parentSlug == "" {
				for i := len(loadedOrder) - 1; i >= 0; i-- {
					candidate := loadedOrder[i]
					if containsSlug(loadedLinks[candidate], actualSlug) {
						parentSlug = candidate
						break
					}
				}
			}
			if parentSlug == "" && len(loadedOrder) > 0 {
				parentSlug = loadedOrder[len(loadedOrder)-1]
			}

			pushStep(Step{
				Action: "think",
				Page:   actualSlug,
				Parent: parentSlug,
				Title:  title,
				Details: decisionDetails(
					parsed.Reason,
					fmt.Sprintf("Fetch %s to add evidence connected from %s.", title, parentSlug),
				),
			})

			context = append(context, fmt.Sprintf("--- Page: %s (slug: %s) ---\n%s", title, actualSlug, content))
			pages = append(pages, PageRef{Slug: actualSlug, Title: title, Relation: "follow"})

			links := extractWikilinks(content)
			loadedLinks[actualSlug] = links
			loadedOrder = append(loadedOrder, actualSlug)
			linkStr := ""
			if len(links) > 0 {
				linkStr = fmt.Sprintf("; %d outgoing wikilinks: %s", len(links), strings.Join(links, ", "))
			} else {
				linkStr = "; no outgoing wikilinks"
			}
			pushStep(Step{
				Action:  "follow",
				Page:    actualSlug,
				Parent:  parentSlug,
				Title:   title,
				Details: fmt.Sprintf("Read %d characters from %s%s.", len([]rune(content)), actualSlug, linkStr),
			})

		} else if parsed.Action == "answer" {
			pushStep(Step{
				Action: "think",
				Details: decisionDetails(
					parsed.Reason,
					fmt.Sprintf("The %d loaded wiki pages provide enough direction to load their primary sources and compose the answer.", len(context)),
				),
			})
			uniquePages := uniquePageRefs(pages)
			answer, citations := answerFromPrimarySources(wikiDir, rawDir, userQuestion, context, uniquePages, pushStep)
			return answer, uniquePages, citations, steps

		} else {
			pushStep(Step{
				Action:  "think",
				Details: "The model response did not contain a valid fetch or answer action, so the same loaded evidence will be evaluated again.",
			})
			continue
		}
	}

	pushStep(Step{
		Action:  "think",
		Details: fmt.Sprintf("The %d-turn exploration limit was reached; loading primary sources for the pages already collected.", maxTurns),
	})
	uniquePages := uniquePageRefs(pages)
	answer, citations := answerFromPrimarySources(wikiDir, rawDir, userQuestion, context, uniquePages, pushStep)
	return answer, uniquePages, citations, steps
}

func reactTurnLimit(pageCount int) int {
	if pageCount <= 0 {
		return 1
	}
	return (pageCount + 4) / 5
}

func uniquePageRefs(pages []PageRef) []PageRef {
	unique := make([]PageRef, 0, len(pages))
	seen := make(map[string]bool)
	for _, page := range pages {
		if !seen[page.Slug] {
			seen[page.Slug] = true
			unique = append(unique, page)
		}
	}
	return unique
}

func answerFromPrimarySources(
	wikiDir string,
	rawDir string,
	userQuestion string,
	wikiContext []string,
	pages []PageRef,
	pushStep func(Step),
) (string, []CitationRef) {
	type sourceContext struct {
		source     RawSource
		pages      []PageRef
		citationID string
	}

	sourceOrder := []string{}
	sourcesByPath := make(map[string]*sourceContext)
	for _, page := range pages {
		sources, err := loadPageSources(wikiDir, rawDir, page.Slug)
		if err != nil {
			continue
		}
		for _, source := range sources {
			entry, exists := sourcesByPath[source.Path]
			if !exists {
				entry = &sourceContext{
					source:     source,
					citationID: fmt.Sprintf("S%d", len(sourceOrder)+1),
				}
				sourcesByPath[source.Path] = entry
				sourceOrder = append(sourceOrder, source.Path)
				pushStep(Step{
					Action:   "source",
					Page:     page.Slug,
					Parent:   page.Slug,
					Title:    source.Title,
					SourceID: entry.citationID,
					Path:     source.Path,
					URL:      source.URL,
					Details:  fmt.Sprintf("Read %s, the complete Korean primary source for %s (%d characters).", entry.citationID, page.Title, len([]rune(source.Body))),
				})
			}
			entry.pages = append(entry.pages, page)
		}
	}

	citations := make([]CitationRef, 0, len(sourceOrder))
	for _, path := range sourceOrder {
		entry := sourcesByPath[path]
		citations = append(citations, CitationRef{
			ID:       entry.citationID,
			Path:     entry.source.Path,
			Title:    entry.source.Title,
			Date:     entry.source.Date,
			Category: entry.source.Category,
			URL:      entry.source.URL,
			Snippet:  sourceSnippet(entry.source.Body, userQuestion),
			Pages:    uniquePageRefs(entry.pages),
		})
	}

	var prompt strings.Builder
	prompt.WriteString("You are a battery technology expert producing the final answer after completing wiki graph exploration.\n\n")
	prompt.WriteString("The compact English wiki pages below are retrieval guides only. You MUST ground and enrich the answer using the complete Korean primary-source blogs that follow. Their bodies are included in full and are not truncated.\n\n")
	prompt.WriteString("Rules:\n")
	prompt.WriteString("- Answer the user's question in natural English.\n")
	prompt.WriteString("- Use specific technical details, dates, quantities, distinctions, and caveats from the Korean primary sources when relevant.\n")
	prompt.WriteString("- Do not invent facts that are absent from the supplied sources.\n")
	prompt.WriteString("- Cite the associated wiki pages using [[slug|Title]] wikilinks.\n")
	prompt.WriteString("- Cite source-backed claims inline with the bracketed primary-source IDs, for example [S1] or [S1][S2].\n")
	prompt.WriteString("- Prefer source IDs near the exact sentence they support; do not add a bibliography because the app renders it separately.\n")
	prompt.WriteString("- Return the answer only, without JSON or a preamble about your process.\n\n")
	prompt.WriteString("## User Question\n")
	prompt.WriteString(userQuestion)
	prompt.WriteString("\n\n## Retrieved Wiki Pages\n")
	for _, page := range wikiContext {
		prompt.WriteString(page)
		prompt.WriteString("\n\n")
	}

	prompt.WriteString("## Complete Korean Primary Sources\n")
	for _, path := range sourceOrder {
		entry := sourcesByPath[path]
		prompt.WriteString("\n### ")
		prompt.WriteString("[")
		prompt.WriteString(entry.citationID)
		prompt.WriteString("] ")
		prompt.WriteString(entry.source.Title)
		prompt.WriteString("\nAssociated wiki pages: ")
		for i, page := range entry.pages {
			if i > 0 {
				prompt.WriteString(", ")
			}
			prompt.WriteString(fmt.Sprintf("[[%s|%s]]", page.Slug, page.Title))
		}
		if entry.source.Date != "" {
			prompt.WriteString("\nDate: ")
			prompt.WriteString(entry.source.Date)
		}
		if entry.source.URL != "" {
			prompt.WriteString("\nOriginal URL: ")
			prompt.WriteString(entry.source.URL)
		}
		prompt.WriteString("\n\n")
		prompt.WriteString(entry.source.Body)
		prompt.WriteString("\n")
	}

	pushStep(Step{
		Action:  "answer",
		Details: fmt.Sprintf("Composing the final answer from %d complete Korean primary sources and %d retrieved wiki pages.", len(sourceOrder), len(pages)),
	})
	return callOllamaRaw(prompt.String(), 120), citations
}

func sourceSnippet(body, query string) string {
	paragraphs := strings.Split(strings.ReplaceAll(body, "\r\n", "\n"), "\n\n")
	terms := expandedSearchTerms(query)
	best := ""
	bestScore := -1.0
	for _, paragraph := range paragraphs {
		cleaned := strings.Join(strings.Fields(paragraph), " ")
		if cleaned == "" {
			continue
		}
		tokens := tokenizeSearchText(cleaned)
		freq := termFrequency(tokens)
		score := 0.0
		for _, term := range terms {
			score += float64(freq[term.term]) * term.weight
		}
		if score > bestScore {
			bestScore = score
			best = cleaned
		}
	}
	if best == "" {
		best = strings.Join(strings.Fields(body), " ")
	}
	runes := []rune(best)
	if len(runes) > 320 {
		best = string(runes[:317]) + "..."
	}
	return best
}

func decisionDetails(reason, fallback string) string {
	summary := strings.Join(strings.Fields(reason), " ")
	if summary == "" {
		summary = fallback
	}
	runes := []rune(summary)
	if len(runes) > 360 {
		summary = string(runes[:357]) + "..."
	}
	return "Decision: " + summary
}

func fuzzyFindSlug(slugs map[string]string, query string) string {
	ql := strings.ToLower(strings.TrimSpace(query))
	if ql == "" {
		return ""
	}
	if _, ok := slugs[ql]; ok {
		return ql
	}
	for slug := range slugs {
		if strings.EqualFold(slug, ql) {
			return slug
		}
	}
	for slug := range slugs {
		if strings.HasPrefix(strings.ToLower(slug), ql) || strings.HasPrefix(ql, strings.ToLower(slug)) {
			return slug
		}
	}
	for slug := range slugs {
		if strings.Contains(strings.ToLower(slug), ql) || strings.Contains(ql, strings.ToLower(slug)) {
			return slug
		}
	}
	return ""
}

func extractWikilinks(content string) []string {
	matches := wikilinkRe.FindAllStringSubmatch(content, -1)
	var links []string
	seen := make(map[string]bool)
	for _, m := range matches {
		s := strings.TrimSpace(m[1])
		if s != "" && !seen[s] {
			seen[s] = true
			links = append(links, s)
		}
	}
	return links
}

func containsSlug(slugs []string, target string) bool {
	for _, slug := range slugs {
		clean := strings.TrimSpace(strings.SplitN(slug, "#", 2)[0])
		if strings.EqualFold(clean, target) {
			return true
		}
	}
	return false
}

func callOllamaRaw(prompt string, timeoutSec int) string {
	ak := os.Getenv("OLLAMA_API_KEY")
	if ak == "" {
		return `{"action": "answer", "text": "Error: OLLAMA_API_KEY not configured."}`
	}
	model := os.Getenv("OLLAMA_MODEL")
	if model == "" {
		model = "deepseek-v4-flash:cloud"
	}
	baseURL := os.Getenv("OLLAMA_BASE_URL")
	if baseURL == "" {
		baseURL = "https://ollama.com/v1"
	}

	body := ollamaReq{
		Model: model,
		Messages: []ollamaMsg{
			{Role: "user", Content: prompt},
		},
		Stream: false,
	}
	payload, _ := json.Marshal(body)

	ctx, cancel := context.WithTimeout(context.Background(), time.Duration(timeoutSec)*time.Second)
	defer cancel()

	req, err := http.NewRequestWithContext(ctx, "POST", baseURL+"/chat/completions", bytes.NewReader(payload))
	if err != nil {
		return fmt.Sprintf(`{"action": "answer", "text": "Error: %v"}`, err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+ak)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return fmt.Sprintf(`{"action": "answer", "text": "Error calling Ollama: %v"}`, err)
	}
	defer resp.Body.Close()

	b, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Sprintf(`{"action": "answer", "text": "Error reading response: %v"}`, err)
	}
	if resp.StatusCode != 200 {
		return fmt.Sprintf(`{"action": "answer", "text": "Ollama API error (%d): %s"}`, resp.StatusCode, string(b))
	}

	var or ollamaResp
	if err := json.Unmarshal(b, &or); err != nil {
		return fmt.Sprintf(`{"action": "answer", "text": "Error parsing response: %v"}`, err)
	}
	return or.Choices[0].Message.Content
}

func searchWiki(wikiDir, query string, limit int) []PageRef {
	return searchWikiDetailed(wikiDir, query, limit).Pages
}

type weightedTerm struct {
	term     string
	weight   float64
	original bool
}

var batterySearchSynonyms = map[string][]string{
	"46":                        {"46 series", "4680", "4695", "cylindrical"},
	"46-series":                 {"46 series", "4680", "4695", "cylindrical"},
	"anode":                     {"negative electrode", "음극", "음극재", "silicon anode"},
	"양극":                        {"cathode", "positive electrode", "양극재"},
	"양극재":                       {"cathode", "cathode material", "positive electrode"},
	"battery management":        {"bms", "bmts", "soc", "soh"},
	"battery management system": {"bms", "bmts", "soc", "soh"},
	"battery passport":          {"passport", "traceability", "esg"},
	"battery safety":            {"thermal runaway", "tp prevention", "srs", "venting"},
	"bms":                       {"battery management system", "bmts", "soc", "soh"},
	"bmts":                      {"battery management system", "bms", "thermal management"},
	"cathode":                   {"positive electrode", "양극", "양극재", "cathode material"},
	"cell to pack":              {"ctp", "pack process", "moduleless"},
	"conductive additive":       {"carbon black", "conductivity", "도전재"},
	"ctp":                       {"cell to pack", "moduleless", "pack process"},
	"dry electrode":             {"dry electrode process", "solvent free", "wet electrode"},
	"전해질":                       {"electrolyte", "liquid electrolyte", "solid electrolyte"},
	"electrolyte":               {"전해질", "liquid electrolyte", "solid electrolyte", "additive"},
	"ev":                        {"electric vehicle", "mobility"},
	"fast charging":             {"c-rate", "cc cv", "heat generation", "lithium plating"},
	"lfp":                       {"lithium iron phosphate", "iron phosphate", "리튬인산철"},
	"lithium iron phosphate":    {"lfp", "iron phosphate", "리튬인산철"},
	"negative electrode":        {"anode", "음극", "음극재"},
	"ncm":                       {"nickel cobalt manganese", "ternary", "high nickel"},
	"positive electrode":        {"cathode", "양극", "양극재"},
	"separator":                 {"분리막", "srs", "safety reinforced separator"},
	"solid state":               {"solid electrolyte", "all solid state", "solid-state battery"},
	"srs":                       {"separator", "safety reinforced separator", "분리막"},
	"swelling":                  {"gas", "gassing", "gas free", "electrolyte", "battery safety"},
	"thermal runaway":           {"battery safety", "tp prevention", "srs", "venting"},
	"wet electrode":             {"wet electrode process", "dry electrode", "solvent"},
}

func tokenizeSearchText(text string) []string {
	tokens := strings.FieldsFunc(strings.ToLower(text), func(r rune) bool {
		return !(unicode.IsLetter(r) || unicode.IsNumber(r))
	})
	out := make([]string, 0, len(tokens))
	for _, token := range tokens {
		token = strings.TrimSpace(token)
		if len([]rune(token)) < 2 {
			continue
		}
		out = append(out, token)
	}
	return out
}

func normalizeSearchPhrase(text string) string {
	return strings.Join(tokenizeSearchText(text), " ")
}

func addWeightedTerm(terms map[string]weightedTerm, term string, weight float64, original bool) {
	for _, token := range tokenizeSearchText(term) {
		existing, ok := terms[token]
		if !ok || weight > existing.weight || original {
			terms[token] = weightedTerm{term: token, weight: weight, original: original || existing.original}
		}
	}
}

func expandedSearchTerms(query string) []weightedTerm {
	terms := make(map[string]weightedTerm)
	originals := tokenizeSearchText(query)
	for _, token := range originals {
		addWeightedTerm(terms, token, 1.0, true)
		for _, synonym := range batterySearchSynonyms[token] {
			addWeightedTerm(terms, synonym, 0.65, false)
		}
	}

	normalizedQuery := " " + normalizeSearchPhrase(query) + " "
	for key, synonyms := range batterySearchSynonyms {
		normalizedKey := normalizeSearchPhrase(key)
		if normalizedKey == "" || !strings.Contains(normalizedQuery, " "+normalizedKey+" ") {
			continue
		}
		addWeightedTerm(terms, key, 0.75, false)
		for _, synonym := range synonyms {
			addWeightedTerm(terms, synonym, 0.65, false)
		}
	}

	out := make([]weightedTerm, 0, len(terms))
	for _, term := range terms {
		out = append(out, term)
	}
	sort.Slice(out, func(i, j int) bool {
		if out[i].original != out[j].original {
			return out[i].original
		}
		if out[i].weight != out[j].weight {
			return out[i].weight > out[j].weight
		}
		return out[i].term < out[j].term
	})
	return out
}

func termFrequency(tokens []string) map[string]int {
	freq := make(map[string]int, len(tokens))
	for _, token := range tokens {
		freq[token]++
	}
	return freq
}

func searchWikiDetailed(wikiDir, query string, limit int) wikiSearchResult {
	terms := expandedSearchTerms(query)
	originalWords := make([]string, 0, len(terms))
	seenOriginalWords := make(map[string]bool)
	for _, word := range tokenizeSearchText(query) {
		if !seenOriginalWords[word] {
			seenOriginalWords[word] = true
			originalWords = append(originalWords, word)
		}
	}
	expandedWords := make([]string, 0, len(terms))
	for _, term := range terms {
		if !term.original {
			expandedWords = append(expandedWords, term.term)
		}
	}

	type doc struct {
		slug      string
		title     string
		length    int
		freq      map[string]int
		titleFreq map[string]int
		slugFreq  map[string]int
		titleNorm string
		bodyNorm  string
		slugNorm  string
	}
	type s struct {
		slug  string
		title string
		score int
	}
	docs := []doc{}

	filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() || !strings.HasSuffix(path, ".md") {
			return nil
		}
		rel, _ := filepath.Rel(wikiDir, path)
		if !strings.Contains(rel, string(filepath.Separator)) {
			return nil
		}
		slug := strings.TrimSuffix(info.Name(), ".md")
		content, err := os.ReadFile(path)
		if err != nil {
			return nil
		}
		body := string(content)
		title := extractTitle(body)
		titleTokens := tokenizeSearchText(title)
		slugTokens := tokenizeSearchText(slug)
		bodyTokens := tokenizeSearchText(body)
		allTokens := make([]string, 0, len(titleTokens)*3+len(slugTokens)*2+len(bodyTokens))
		allTokens = append(allTokens, titleTokens...)
		allTokens = append(allTokens, titleTokens...)
		allTokens = append(allTokens, titleTokens...)
		allTokens = append(allTokens, slugTokens...)
		allTokens = append(allTokens, slugTokens...)
		allTokens = append(allTokens, bodyTokens...)
		docs = append(docs, doc{
			slug:      slug,
			title:     title,
			length:    len(allTokens),
			freq:      termFrequency(allTokens),
			titleFreq: termFrequency(titleTokens),
			slugFreq:  termFrequency(slugTokens),
			titleNorm: strings.Join(titleTokens, " "),
			bodyNorm:  strings.Join(bodyTokens, " "),
			slugNorm:  strings.Join(slugTokens, " "),
		})
		return nil
	})

	scanned := len(docs)
	df := make(map[string]int, len(terms))
	totalLength := 0
	for _, doc := range docs {
		totalLength += doc.length
		for _, term := range terms {
			if doc.freq[term.term] > 0 {
				df[term.term]++
			}
		}
	}
	avgLength := 1.0
	if len(docs) > 0 {
		avgLength = float64(totalLength) / float64(len(docs))
		if avgLength <= 0 {
			avgLength = 1
		}
	}

	normalizedQuery := normalizeSearchPhrase(query)
	res := make([]s, 0, len(docs))
	for _, doc := range docs {
		score := 0.0
		for _, term := range terms {
			tf := doc.freq[term.term]
			if tf <= 0 {
				continue
			}
			n := float64(len(docs))
			docFreq := float64(df[term.term])
			idf := math.Log(1 + (n-docFreq+0.5)/(docFreq+0.5))
			k1 := 1.35
			b := 0.72
			dl := math.Max(float64(doc.length), 1)
			bm25 := idf * (float64(tf) * (k1 + 1)) / (float64(tf) + k1*(1-b+b*dl/avgLength))
			score += bm25 * 12 * term.weight
			if doc.titleFreq[term.term] > 0 {
				score += 20 * term.weight
			}
			if doc.slugFreq[term.term] > 0 {
				score += 10 * term.weight
			}
		}
		if normalizedQuery != "" {
			if strings.Contains(doc.titleNorm, normalizedQuery) {
				score += 60
			}
			if strings.Contains(doc.slugNorm, normalizedQuery) {
				score += 32
			}
			if strings.Contains(doc.bodyNorm, normalizedQuery) {
				score += 18
			}
		}
		if score > 0 {
			rankedScore := int(math.Round(score * 10))
			if rankedScore <= 0 {
				rankedScore = 1
			}
			res = append(res, s{slug: doc.slug, title: doc.title, score: rankedScore})
		}
	}

	sort.Slice(res, func(i, j int) bool {
		if res[i].score != res[j].score {
			return res[i].score > res[j].score
		}
		return res[i].slug < res[j].slug
	})
	matched := len(res)
	if limit >= 0 && len(res) > limit {
		res = res[:limit]
	}
	pages := make([]PageRef, len(res))
	scores := make(map[string]int, len(res))
	for i, r := range res {
		pages[i] = PageRef{Slug: r.slug, Title: r.title, Relation: "search"}
		scores[r.slug] = r.score
	}

	var details strings.Builder
	fmt.Fprintf(&details, "Query: %q\n", query)
	if len(originalWords) > 0 {
		fmt.Fprintf(&details, "Terms: %s\n", strings.Join(originalWords, " | "))
	} else {
		details.WriteString("Terms: no searchable terms after normalization\n")
	}
	if len(expandedWords) > 0 {
		if len(expandedWords) > 16 {
			expandedWords = expandedWords[:16]
		}
		fmt.Fprintf(&details, "Expanded terms: %s\n", strings.Join(expandedWords, " | "))
	}
	details.WriteString("Matcher: BM25 lexical ranker with title/slug boosts and battery-domain synonym expansion\n")
	fmt.Fprintf(&details, "Scanned: %d pages; matched: %d\n", scanned, matched)
	if len(res) > 0 {
		details.WriteString("Top matches:\n")
		for i, result := range res {
			fmt.Fprintf(&details, "%d. %s (%s), score %d\n", i+1, result.title, result.slug, result.score)
		}
	}

	return wikiSearchResult{
		Pages:   pages,
		Scores:  scores,
		Details: strings.TrimSpace(details.String()),
	}
}

func readPageContent(wikiDir, slug string) string {
	var fp string
	filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() {
			return nil
		}
		if strings.EqualFold(strings.TrimSuffix(info.Name(), ".md"), slug) {
			fp = path
		}
		return nil
	})
	if fp == "" {
		return ""
	}
	content, err := os.ReadFile(fp)
	if err != nil {
		return ""
	}
	body := string(content)
	if strings.HasPrefix(body, "---\n") {
		if end := strings.Index(body[4:], "\n---"); end >= 0 {
			body = body[4+end+5:]
		}
	}
	if len([]rune(body)) > 12000 {
		body = string([]rune(body)[:12000]) + "..."
	}
	return strings.TrimSpace(body)
}

func extractTitle(content string) string {
	if strings.HasPrefix(content, "---\n") {
		if end := strings.Index(content[4:], "\n---"); end >= 0 {
			for _, line := range strings.Split(content[4:4+end], "\n") {
				if strings.HasPrefix(line, "title: ") {
					return strings.TrimSpace(line[7:])
				}
			}
		}
	}
	for _, line := range strings.Split(content, "\n") {
		t := strings.TrimSpace(line)
		if strings.HasPrefix(t, "# ") {
			return strings.TrimPrefix(t, "# ")
		}
	}
	return "Untitled"
}
