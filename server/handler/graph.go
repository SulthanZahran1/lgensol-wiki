package handler

import (
	"encoding/json"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

type GraphData struct {
	Nodes []map[string]any `json:"nodes"`
	Links []map[string]any `json:"links"`
}

var cachedGraph []byte

func LoadGraph(path string) error {
	data, err := os.ReadFile(path)
	if err != nil {
		return err
	}
	cachedGraph = data
	return nil
}

func GraphHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Cache-Control", "public, max-age=3600")
	w.Write(cachedGraph)
}

func PageHandler(wikiDir string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		slug := strings.TrimPrefix(r.URL.Path, "/api/page/")
		slug = strings.TrimSuffix(slug, ".md")
		if slug == "" || strings.Contains(slug, "/") {
			http.Error(w, `{"error":"invalid slug"}`, http.StatusBadRequest)
			return
		}

		// Search for the file in subdirectories
		var foundPath string
		filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
			if err != nil || info.IsDir() {
				return nil
			}
			if strings.EqualFold(strings.TrimSuffix(info.Name(), ".md"), slug) {
				foundPath = path
			}
			return nil
		})

		if foundPath == "" {
			http.Error(w, `{"error":"page not found"}`, http.StatusNotFound)
			return
		}

		content, err := os.ReadFile(foundPath)
		if err != nil {
			http.Error(w, `{"error":"read error"}`, http.StatusInternalServerError)
			return
		}

		// Return raw markdown — frontend renders it
		w.Header().Set("Content-Type", "text/markdown; charset=utf-8")
		w.Write(content)
	}
}

func ListPagesHandler(wikiDir string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var pages []map[string]string
		filepath.Walk(wikiDir, func(path string, info os.FileInfo, err error) error {
			if err != nil || info.IsDir() || !strings.HasSuffix(path, ".md") {
				return nil
			}
			rel, _ := filepath.Rel(wikiDir, path)
			if !strings.Contains(rel, string(filepath.Separator)) {
				return nil
			}
			pages = append(pages, map[string]string{
				"slug": strings.TrimSuffix(info.Name(), ".md"),
				"path": rel,
			})
			return nil
		})

		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(pages)
	}
}