package main

import (
	"embed"
	"io/fs"
	"log"
	"net/http"
	"os"
	"path/filepath"

	"wiki.zahranm.cloud/handler"
)

//go:embed static/*
var staticFiles embed.FS

//go:embed data/*
var dataFiles embed.FS

func main() {
	wikiDir := os.Getenv("WIKI_DIR")
	if wikiDir == "" {
		wikiDir = "wiki"
	}
	absWiki, err := filepath.Abs(wikiDir)
	if err == nil {
		wikiDir = absWiki
	}

	// Static files sub-fs (strip "static/" prefix)
	staticFS, _ := fs.Sub(staticFiles, "static")

	// Static file server with cache headers
	fileServer := http.FileServer(http.FS(staticFS))
	staticHandler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		ext := ""
		if len(r.URL.Path) >= 3 {
			ext = r.URL.Path[len(r.URL.Path)-3:]
		}
		if ext == ".js" || ext == "css" || ext == "svg" || ext == "png" || ext == "ico" || ext == "woff2" {
			w.Header().Set("Cache-Control", "public, max-age=31536000, immutable")
		} else {
			w.Header().Set("Cache-Control", "public, max-age=3600")
		}
		fileServer.ServeHTTP(w, r)
	})

	// Load graph data into cache
	graphPath := os.Getenv("GRAPH_PATH")
	if graphPath == "" {
		graphPath = "data/graph.json"
	}
	if err := handler.LoadGraph(graphPath); err != nil {
		log.Printf("Warning: could not load graph from %s: %v", graphPath, err)
	}

	mux := http.NewServeMux()

	// ── Public routes (no auth) ──
	mux.Handle("/", staticHandler)

	// ── Protected API routes (with auth) ──
	apiMux := http.NewServeMux()
	apiMux.HandleFunc("/api/graph", http.HandlerFunc(handler.GraphHandler))
	apiMux.HandleFunc("/api/page/", handler.PageHandler(wikiDir))
	apiMux.HandleFunc("/api/pages", handler.ListPagesHandler(wikiDir))
	apiMux.HandleFunc("/api/chat", handler.ChatHandler(wikiDir))
	apiMux.HandleFunc("/api/verify-token", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte(`{"ok":true}`))
	})

	mux.Handle("/api/", handler.ApiAuthMiddleware(apiMux))

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	log.Printf("Wiki server starting on :%s (wiki dir: %s)", port, wikiDir)
	log.Printf("Auth: %s", map[bool]string{true: "enabled", false: "disabled"}[handler.AccessToken() != ""])
	log.Fatal(http.ListenAndServe(":"+port, mux))
}