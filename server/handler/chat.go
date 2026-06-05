package handler

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"time"
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
	Answer string    `json:"answer"`
	Pages  []PageRef `json:"pages"`
	Steps  []Step    `json:"steps"`
}

type Step struct {
	Action  string `json:"action"`  // "read", "follow", "think", "answer"
	Page    string `json:"page,omitempty"`
	Title   string `json:"title,omitempty"`
	Details string `json:"details,omitempty"`
}

type PageRef struct {
	Slug  string `json:"slug"`
	Title string `json:"title"`
	Score int    `json:"score"`
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

func ChatHandler(wikiDir string) http.HandlerFunc {
	// Pre-build page index at startup
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

		// Seed: keyword search → top 3 pages
		seedPages := searchWiki(wikiDir, req.Message, 3)
		if len(seedPages) == 0 {
			// Pick some default seed if nothing matches
			seedPages = []PageRef{{Slug: "lg-energy-solution", Title: "LG Energy Solution"}}
		}

		// Run the ReAct loop
		answer, allPages, steps := reactLoop(wikiDir, req.Message, seedPages, pageIndex)

		resp := ChatResponse{Answer: answer, Pages: allPages, Steps: steps}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(resp)
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
					// Remove quotes if present
					t = strings.Trim(t, `"'`)
					return t
				}
			}
		}
	}
	return "Untitled"
}

const maxReActTurns = 6

func reactLoop(wikiDir, userQuestion string, seedPages []PageRef, pageIndex []pageEntry) (string, []PageRef, []Step) {
	var steps []Step
	visited := make(map[string]bool)          // slug → true
	pages := make([]PageRef, 0, len(seedPages))
	context := make([]string, 0, maxReActTurns+3)
	allSlugs := make(map[string]string) // slug → title

	for _, p := range pageIndex {
		allSlugs[p.slug] = p.title
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
		context = append(context, fmt.Sprintf("--- Page: %s (slug: %s) ---\n%s", title, sp.Slug, content))
		pages = append(pages, PageRef{Slug: sp.Slug, Title: title, Score: 10})
		steps = append(steps, Step{Action: "read", Page: sp.Slug, Title: title, Details: fmt.Sprintf("Loaded %d chars", len(content))})
	}

	// Build a compact page index string for the LLM
	var indexSb strings.Builder
	indexSb.WriteString("Available pages (slug → title):\n")
	// Group by type for readability
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
	for loop < maxReActTurns {
		loop++

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
		sb.WriteString("   {\"action\": \"fetch\", \"slug\": \"page-slug\"}\n\n")
		sb.WriteString("2. ANSWER the question when you have enough context — respond with:\n")
		sb.WriteString("   {\"action\": \"answer\", \"text\": \"your detailed answer...\"}\n\n")
		sb.WriteString("Rules:\n")
		sb.WriteString("- FETCH a page when you need specific information from it\n")
		sb.WriteString("- Pay attention to wikilinks [[like-this]] mentioned in pages — they point to related pages\n")
		sb.WriteString("- You can fetch at most one page per turn\n")
		sb.WriteString("- Use Korean terminology internally for search (리튬이온, 양극재, 음극재, 전해질 etc.)\n")
		sb.WriteString("- Keep track of which pages you've already loaded — don't fetch them again\n")
		sb.WriteString("- You have limited turns. Make each fetch count. ANSWER when you're confident.\n")
		sb.WriteString("- Cite sources in your answer using [[wikilinks]] format.\n")
		sb.WriteString("- Write your answer in natural English.\n")

		llmResp := callOllamaRaw(sb.String(), maxReActTurns*2+5)

		// Parse the response
		var parsed struct {
			Action string `json:"action"`
			Slug   string `json:"slug"`
			Text   string `json:"text"`
		}

		// Try to find JSON in the response
		jsonStart := strings.Index(llmResp, "{")
		jsonEnd := strings.LastIndex(llmResp, "}")
		if jsonStart >= 0 && jsonEnd > jsonStart {
			jsonStr := llmResp[jsonStart : jsonEnd+1]
			if err := json.Unmarshal([]byte(jsonStr), &parsed); err != nil {
				parsed.Action = "" // parse failed
			}
		}

		if parsed.Action == "fetch" && parsed.Slug != "" {
			slug := parsed.Slug
			// Fuzzy match: try exact, then case-insensitive, then prefix
			actualSlug := fuzzyFindSlug(allSlugs, slug)
			if actualSlug == "" || visited[actualSlug] {
				// Page not found or already loaded — ask LLM to try again
				continue
			}

			visited[actualSlug] = true
			content := readPageContent(wikiDir, actualSlug)
			if content == "" {
				continue
			}
			title := allSlugs[actualSlug]
			if title == "" {
				title = actualSlug
			}

			context = append(context, fmt.Sprintf("--- Page: %s (slug: %s) ---\n%s", title, actualSlug, content))
			pages = append(pages, PageRef{Slug: actualSlug, Title: title, Score: 5})

			// Extract wikilinks from content for the step details
			links := extractWikilinks(content)
			linkStr := ""
			if len(links) > 0 {
				linkStr = fmt.Sprintf(" — links to: %s", strings.Join(links, ", "))
			}
			steps = append(steps, Step{
				Action:  "follow",
				Page:    actualSlug,
				Title:   title,
				Details: fmt.Sprintf("Read %d chars%s", len(content), linkStr),
			})

		} else if parsed.Action == "answer" {
			steps = append(steps, Step{Action: "answer", Details: "Answered the question"})
			// Deduplicate pages for return
			uniquePages := make([]PageRef, 0, len(pages))
			seen := make(map[string]bool)
			for _, p := range pages {
				if !seen[p.Slug] {
					seen[p.Slug] = true
					uniquePages = append(uniquePages, p)
				}
			}
			return parsed.Text, uniquePages, steps

		} else {
			// LLM didn't follow format — give it a hint
			continue
		}
	}

	// Max turns reached — return whatever we have with a fallback answer
	steps = append(steps, Step{Action: "think", Details: "Max exploration turns reached"})

	// Build a summary from all context
	var finalSb strings.Builder
	finalSb.WriteString("You are a battery technology expert. Based on the following context, answer the user's question in English. Cite [[wikilinks]]. If you cannot fully answer, say what you know.\n\n")
	for _, c := range context {
		finalSb.WriteString(c)
		finalSb.WriteString("\n\n")
	}
	finalSb.WriteString("Question: " + userQuestion)

	answer := callOllamaRaw(finalSb.String(), 60)

	uniquePages := make([]PageRef, 0, len(pages))
	seen := make(map[string]bool)
	for _, p := range pages {
		if !seen[p.Slug] {
			seen[p.Slug] = true
			uniquePages = append(uniquePages, p)
		}
	}
	return answer, uniquePages, steps
}

func fuzzyFindSlug(slugs map[string]string, query string) string {
	ql := strings.ToLower(strings.TrimSpace(query))
	// Exact match first
	if _, ok := slugs[ql]; ok {
		return ql
	}
	// Case-insensitive exact
	for slug := range slugs {
		if strings.EqualFold(slug, ql) {
			return slug
		}
	}
	// Prefix match (handles partial slugs)
	for slug := range slugs {
		if strings.HasPrefix(strings.ToLower(slug), ql) || strings.HasPrefix(ql, strings.ToLower(slug)) {
			return slug
		}
	}
	// Contains match
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
	ql := strings.ToLower(query)
	words := strings.Fields(ql)
	type s struct {
		slug  string
		title string
		score int
	}
	var res []s

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
		bl := strings.ToLower(body)
		tl := strings.ToLower(title)

		score := 0
		for _, w := range words {
			if len(w) < 2 {
				continue
			}
			if strings.Contains(tl, w) {
				score += 10
			}
			if strings.Contains(bl, w) {
				score += 3
			}
		}
		if strings.Contains(tl, ql) {
			score += 50
		}
		if strings.Contains(bl, ql) {
			score += 15
		}
		if score > 0 {
			res = append(res, s{slug, title, score})
		}
		return nil
	})

	for i := 0; i < len(res); i++ {
		for j := i + 1; j < len(res); j++ {
			if res[j].score > res[i].score {
				res[i], res[j] = res[j], res[i]
			}
		}
	}
	if len(res) > limit {
		res = res[:limit]
	}
	pages := make([]PageRef, len(res))
	for i, r := range res {
		pages[i] = PageRef{Slug: r.slug, Title: r.title, Score: r.score}
	}
	return pages
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
	// Truncate to 12K chars
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