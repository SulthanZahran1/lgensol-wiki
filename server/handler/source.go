package handler

import (
	"encoding/json"
	"html"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

type RawSource struct {
	Path     string `json:"path"`
	Title    string `json:"title"`
	Date     string `json:"date,omitempty"`
	Category string `json:"category,omitempty"`
	URL      string `json:"url,omitempty"`
	Body     string `json:"body"`
}

func PageSourcesHandler(wikiDir, rawDir string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		slug := strings.TrimPrefix(r.URL.Path, "/api/page-sources/")
		slug = strings.TrimSuffix(slug, ".md")
		if slug == "" || strings.Contains(slug, "/") {
			http.Error(w, `{"error":"invalid slug"}`, http.StatusBadRequest)
			return
		}

		sources, err := loadPageSources(wikiDir, rawDir, slug)
		if err != nil {
			http.Error(w, `{"error":"page not found"}`, http.StatusNotFound)
			return
		}

		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Cache-Control", "private, max-age=3600")
		json.NewEncoder(w).Encode(map[string]any{
			"slug":    slug,
			"sources": sources,
		})
	}
}

func loadPageSources(wikiDir, rawDir, slug string) ([]RawSource, error) {
	pagePath := findWikiPage(wikiDir, slug)
	if pagePath == "" {
		return nil, os.ErrNotExist
	}

	content, err := os.ReadFile(pagePath)
	if err != nil {
		return nil, err
	}

	sourcePaths := frontmatterList(string(content), "sources")
	sources := make([]RawSource, 0, len(sourcePaths))
	for _, sourcePath := range sourcePaths {
		source, ok := loadRawSource(rawDir, sourcePath)
		if ok {
			sources = append(sources, source)
		}
	}
	return sources, nil
}

func loadRawSource(rawDir, sourcePath string) (RawSource, bool) {
	const prefix = "raw/ko/"
	relative := strings.TrimPrefix(strings.TrimSpace(sourcePath), prefix)
	relative = filepath.Clean(filepath.FromSlash(relative))
	if relative == "." || filepath.IsAbs(relative) || relative == ".." || strings.HasPrefix(relative, ".."+string(filepath.Separator)) {
		return RawSource{}, false
	}

	fullPath := filepath.Join(rawDir, relative)
	resolved, err := filepath.Rel(rawDir, fullPath)
	if err != nil || resolved == ".." || strings.HasPrefix(resolved, ".."+string(filepath.Separator)) {
		return RawSource{}, false
	}

	content, err := os.ReadFile(fullPath)
	if err != nil {
		return RawSource{}, false
	}

	meta, body := splitFrontmatter(string(content))
	title := html.UnescapeString(meta["title"])
	if title == "" {
		title = strings.TrimSuffix(filepath.Base(relative), filepath.Ext(relative))
	}

	return RawSource{
		Path:     sourcePath,
		Title:    title,
		Date:     meta["date"],
		Category: meta["category"],
		URL:      meta["source_url"],
		Body:     strings.TrimSpace(body),
	}, true
}

func findWikiPage(wikiDir, slug string) string {
	var found string
	filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil || info.IsDir() {
			return nil
		}
		if strings.EqualFold(strings.TrimSuffix(info.Name(), ".md"), slug) {
			found = path
		}
		return nil
	})
	return found
}

func frontmatterList(content, key string) []string {
	meta, _ := splitFrontmatter(content)
	block := meta["__frontmatter"]
	lines := strings.Split(block, "\n")
	values := []string{}
	inList := false
	for _, line := range lines {
		if strings.HasPrefix(line, key+":") {
			inList = true
			continue
		}
		if inList {
			if strings.HasPrefix(line, "  - ") {
				values = append(values, strings.TrimSpace(strings.TrimPrefix(line, "  - ")))
				continue
			}
			if strings.TrimSpace(line) != "" && !strings.HasPrefix(line, " ") {
				break
			}
		}
	}
	return values
}

func splitFrontmatter(content string) (map[string]string, string) {
	meta := map[string]string{}
	if !strings.HasPrefix(content, "---\n") {
		return meta, content
	}

	end := strings.Index(content[4:], "\n---")
	if end < 0 {
		return meta, content
	}
	block := content[4 : 4+end]
	meta["__frontmatter"] = block
	for _, line := range strings.Split(block, "\n") {
		if strings.HasPrefix(line, " ") {
			continue
		}
		key, value, ok := strings.Cut(line, ":")
		if !ok {
			continue
		}
		meta[strings.TrimSpace(key)] = strings.Trim(strings.TrimSpace(value), `"'`)
	}

	bodyStart := 4 + end + len("\n---")
	body := strings.TrimPrefix(content[bodyStart:], "\n")
	return meta, body
}
