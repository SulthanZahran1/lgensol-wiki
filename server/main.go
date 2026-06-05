package main

import (
	"embed"
	"io/fs"
	"log"
	"net/http"
	"os"

	"wiki.zahranm.cloud/handler"
)

//go:embed static/*
var staticFiles embed.FS

func main() {
	wikiDir := os.Getenv("WIKI_DIR")
	if wikiDir == "" {
		wikiDir = "/home/dev/lgensol-wiki/wiki"
	}

	graphPath := os.Getenv("GRAPH_PATH")
	if graphPath == "" {
		graphPath = "/home/dev/lgensol-wiki/server/data/graph.json"
	}

	accessToken := os.Getenv("ACCESS_TOKEN")
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	// Load graph data
	if err := handler.LoadGraph(graphPath); err != nil {
		log.Printf("Warning: could not load graph from %s: %v", graphPath, err)
	}

	// Sub-filesystem for embedded static
	staticFS, err := fs.Sub(staticFiles, "static")
	if err != nil {
		log.Fatalf("Static files error: %v", err)
	}

	// Middleware
	auth := handler.AuthMiddleware(accessToken)

	// Routes
	mux := http.NewServeMux()

	// API routes
	mux.Handle("/api/graph", auth(http.HandlerFunc(handler.GraphHandler)))
	mux.Handle("/api/page/", auth(http.HandlerFunc(handler.PageHandler(wikiDir))))
	mux.Handle("/api/pages", auth(http.HandlerFunc(handler.ListPagesHandler(wikiDir))))
	mux.Handle("/api/chat", auth(http.HandlerFunc(handler.ChatHandler(wikiDir))))

	// Static frontend (catch-all)
	mux.Handle("/", auth(http.FileServer(http.FS(staticFS))))

	log.Printf("Server starting on :%s", port)
	log.Printf("Wiki: %s", wikiDir)
	log.Printf("Token: %s", map[bool]string{true: "set", false: "not set"}[accessToken != ""])

	if err := http.ListenAndServe(":"+port, mux); err != nil {
		log.Fatalf("Server error: %v", err)
	}
}