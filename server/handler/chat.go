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

type ChatRequest struct {
	Message string `json:"message"`
	ApiKey  string `json:"api_key"`
}

type ChatResponse struct {
	Answer string    `json:"answer"`
	Pages  []PageRef `json:"pages"`
}

type PageRef struct {
	Slug  string `json:"slug"`
	Title string `json:"title"`
	Score int    `json:"score"`
}

type ollamaReq struct {
	Model    string          `json:"model"`
	Messages []ollamaMsg     `json:"messages"`
	Stream   bool            `json:"stream"`
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

		pages := searchWiki(wikiDir, req.Message, 8)

		var sb strings.Builder
		for i, p := range pages {
			content := readPageContent(wikiDir, p.Slug)
			if content == "" {
				continue
			}
			sb.WriteString(fmt.Sprintf("--- Page %d: %s ---\n%s\n\n", i+1, p.Title, content))
		}

		system := "You are a battery technology expert with deep knowledge of LG Energy Solution's Korean blog. Answer the user's question in English. Use ONLY the context below. Internally reason using Korean battery terminology (리튬이온, 양극재, 음극재, 전해질, 배터리, 전기차, ESS, etc.) but write your answer in natural English. Always cite your sources using [[wikilinks]] like [[page-name]] at the end of relevant sentences. If the context doesn't contain enough information to answer, say so honestly."

		user := fmt.Sprintf("Context:\n%s\n\nQuestion: %s", sb.String(), req.Message)

		answer := callOllama(system, user, req.ApiKey)

		resp := ChatResponse{Answer: answer, Pages: pages}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(resp)
	}
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
	if len([]rune(body)) > 10000 {
		body = string([]rune(body)[:10000]) + "..."
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

func callOllama(system, user, apiKey string) string {
	ak := apiKey
	if ak == "" {
		ak = os.Getenv("OLLAMA_API_KEY")
	}
	if ak == "" {
		return "Error: OLLAMA_API_KEY not configured. Provide one in the chat input."
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
			{Role: "system", Content: system},
			{Role: "user", Content: user},
		},
		Stream: false,
	}
	payload, _ := json.Marshal(body)

	ctx, cancel := context.WithTimeout(context.Background(), 60*time.Second)
	defer cancel()

	req, err := http.NewRequestWithContext(ctx, "POST", baseURL+"/chat/completions", bytes.NewReader(payload))
	if err != nil {
		return fmt.Sprintf("Error: %v", err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+ak)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return fmt.Sprintf("Error calling Ollama: %v", err)
	}
	defer resp.Body.Close()

	b, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Sprintf("Error reading response: %v", err)
	}
	if resp.StatusCode != 200 {
		return fmt.Sprintf("Ollama API error (%d): %s", resp.StatusCode, string(b))
	}

	var or ollamaResp
	if err := json.Unmarshal(b, &or); err != nil {
		return fmt.Sprintf("Error parsing response: %v", err)
	}
	return or.Choices[0].Message.Content
}