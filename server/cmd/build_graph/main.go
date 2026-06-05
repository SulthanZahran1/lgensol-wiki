package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

type Node struct {
	Slug     string   `json:"slug"`
	Title    string   `json:"title"`
	Type     string   `json:"type"`
	Category string   `json:"category"`
	Tags     []string `json:"tags"`
	Summary  string   `json:"summary"`
}

type Link struct {
	Source string `json:"source"`
	Target string `json:"target"`
}

type Graph struct {
	Nodes []Node `json:"nodes"`
	Links []Link `json:"links"`
}

var wikilinkRe = regexp.MustCompile(`\[\[([^\]|]+)(?:\|[^\]]+)?\]\]`)

func parseFrontmatter(content string) map[string]any {
	fm := make(map[string]any)
	if !strings.HasPrefix(content, "---\n") {
		return fm
	}
	end := strings.Index(content[4:], "\n---")
	if end < 0 {
		return fm
	}
	block := content[4 : 4+end]
	lines := strings.Split(block, "\n")
	var currentKey string
	var currentList []string
	for _, line := range lines {
		if strings.HasPrefix(line, "  - ") {
			currentList = append(currentList, strings.TrimSpace(line[4:]))
			continue
		}
		if currentKey != "" && currentList != nil {
			fm[currentKey] = currentList
			currentList = nil
		}
		parts := strings.SplitN(line, ": ", 2)
		if len(parts) == 2 {
			currentKey = strings.TrimSpace(parts[0])
			val := strings.TrimSpace(parts[1])
			if val == "" {
				currentList = []string{}
			} else {
				fm[currentKey] = val
				currentKey = ""
			}
		}
	}
	if currentKey != "" && currentList != nil {
		fm[currentKey] = currentList
	}
	return fm
}

func getSlug(path string) string {
	base := filepath.Base(path)
	return strings.TrimSuffix(base, ".md")
}

func extractTitle(content string) string {
	fm := parseFrontmatter(content)
	if t, ok := fm["title"]; ok {
		if s, ok := t.(string); ok {
			return s
		}
	}
	return "Untitled"
}

func extractTags(content string) []string {
	fm := parseFrontmatter(content)
	if t, ok := fm["tags"]; ok {
		switch v := t.(type) {
		case []string:
			return v
		case []any:
			tags := make([]string, len(v))
			for i, a := range v {
				tags[i] = fmt.Sprint(a)
			}
			return tags
		}
	}
	return nil
}

func extractSummary(content string, maxLen int) string {
	body := content
	if strings.HasPrefix(body, "---\n") {
		end := strings.Index(body[4:], "\n---")
		if end >= 0 {
			body = body[4+end+5:]
		}
	}
	// Strip markdown headers and links
	body = regexp.MustCompile(`#{1,6}\s+`).ReplaceAllString(body, "")
	body = regexp.MustCompile(`\[([^\]]+)\]\([^)]+\)`).ReplaceAllString(body, "$1")
	body = strings.TrimSpace(body)
	if len([]rune(body)) > maxLen {
		return string([]rune(body)[:maxLen]) + "..."
	}
	return body
}

func determineType(path string, fm map[string]any) string {
	path = filepath.ToSlash(path)
	if strings.Contains(path, "/entities/") {
		return "entity"
	}
	if strings.Contains(path, "/concepts/") {
		return "concept"
	}
	if strings.Contains(path, "/comparisons/") {
		return "comparison"
	}
	if strings.Contains(path, "/glossary/") {
		return "glossary"
	}
	if t, ok := fm["type"]; ok {
		if s, ok := t.(string); ok {
			return s
		}
	}
	return "page"
}

func getCategory(path string) string {
	path = filepath.ToSlash(path)
	if strings.Contains(path, "/entities/") {
		return "entities"
	}
	if strings.Contains(path, "/concepts/") {
		return "concepts"
	}
	if strings.Contains(path, "/comparisons/") {
		return "comparisons"
	}
	if strings.Contains(path, "/glossary/") {
		return "glossary"
	}
	return "other"
}

func main() {
	wikiDir := "/home/dev/lgensol-wiki/wiki"
	if len(os.Args) > 1 {
		wikiDir = os.Args[1]
	}

	// Validate wiki directory exists
	indexPath := filepath.Join(wikiDir, "index.md")
	if _, err := os.Stat(indexPath); os.IsNotExist(err) {
		fmt.Fprintf(os.Stderr, "Wiki directory not found at %s (no index.md)\n", wikiDir)
		fmt.Fprintf(os.Stderr, "Usage: go run cmd/build_graph/main.go [path-to-wiki]\n")
		os.Exit(1)
	}

	graph := Graph{}
	slugMap := make(map[string]bool)

	// Walk all .md files
	err := filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() || !strings.HasSuffix(path, ".md") {
			return nil
		}
		// Skip root files (SCHEMA.md, index.md, log.md)
		rel, _ := filepath.Rel(wikiDir, path)
		if !strings.Contains(rel, string(filepath.Separator)) {
			return nil
		}

		content, err := os.ReadFile(path)
		if err != nil {
			return err
		}

		slug := getSlug(path)
		fm := parseFrontmatter(string(content))
		title := extractTitle(string(content))
		if t, ok := fm["title"]; ok {
			if s, ok := t.(string); ok {
				title = s
			}
		}
		slugMap[slug] = true

		node := Node{
			Slug:     slug,
			Title:    title,
			Type:     determineType(path, fm),
			Category: getCategory(path),
			Tags:     extractTags(string(content)),
			Summary:  extractSummary(string(content), 150),
		}
		graph.Nodes = append(graph.Nodes, node)

		return nil
	})
	if err != nil {
		fmt.Fprintf(os.Stderr, "Walk error: %v\n", err)
		os.Exit(1)
	}

	// Now parse wikilinks from each file
	err = filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() || !strings.HasSuffix(path, ".md") {
			return nil
		}
		rel, _ := filepath.Rel(wikiDir, path)
		if !strings.Contains(rel, string(filepath.Separator)) {
			return nil
		}

		content, err := os.ReadFile(path)
		if err != nil {
			return err
		}

		sourceSlug := getSlug(path)
		matches := wikilinkRe.FindAllStringSubmatch(string(content), -1)
		seen := make(map[string]bool)
		for _, m := range matches {
			target := strings.TrimSpace(m[1])
			if target == sourceSlug || seen[target] {
				continue
			}
			// Only include links to actual wiki pages
			if slugMap[target] {
				seen[target] = true
				graph.Links = append(graph.Links, Link{
					Source: sourceSlug,
					Target: target,
				})
			}
		}
		return nil
	})
	if err != nil {
		fmt.Fprintf(os.Stderr, "Link walk error: %v\n", err)
		os.Exit(1)
	}

	// Write output
	outPath := filepath.Join(wikiDir, "..", "server", "data", "graph.json")
	out, err := json.MarshalIndent(graph, "", "  ")
	if err != nil {
		fmt.Fprintf(os.Stderr, "JSON marshal error: %v\n", err)
		os.Exit(1)
	}
	if err := os.MkdirAll("data", 0755); err != nil {
		fmt.Fprintf(os.Stderr, "Mkdir error: %v\n", err)
		os.Exit(1)
	}
	if err := os.WriteFile(outPath, out, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "Write error: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Built graph: %d nodes, %d links → %s\n", len(graph.Nodes), len(graph.Links), outPath)
}