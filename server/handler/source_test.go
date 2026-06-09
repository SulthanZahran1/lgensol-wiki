package handler

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestLoadPageSourcesPreservesCompleteBody(t *testing.T) {
	wikiDir := t.TempDir()
	rawDir := t.TempDir()

	pageDir := filepath.Join(wikiDir, "concepts")
	rawTechDir := filepath.Join(rawDir, "tech")
	if err := os.MkdirAll(pageDir, 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.MkdirAll(rawTechDir, 0o755); err != nil {
		t.Fatal(err)
	}

	longBody := strings.Repeat("전체 한국어 원문입니다. ", 1000)
	page := "---\ntitle: Test\nsources:\n  - raw/ko/tech/source.md\n---\n# Test\n"
	source := "---\nsource_url: https://inside.lgensol.com/test/\ntitle: 테스트 &#8211; 원문\ndate: 2026-06-06\ncategory: tech\n---\n" + longBody

	if err := os.WriteFile(filepath.Join(pageDir, "test.md"), []byte(page), 0o644); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(rawTechDir, "source.md"), []byte(source), 0o644); err != nil {
		t.Fatal(err)
	}

	sources, err := loadPageSources(wikiDir, rawDir, "test")
	if err != nil {
		t.Fatal(err)
	}
	if len(sources) != 1 {
		t.Fatalf("expected one source, got %d", len(sources))
	}
	if sources[0].Body != strings.TrimSpace(longBody) {
		t.Fatalf("source body was truncated: got %d chars, want %d", len(sources[0].Body), len(strings.TrimSpace(longBody)))
	}
	if sources[0].Title != "테스트 – 원문" {
		t.Fatalf("title was not decoded: %q", sources[0].Title)
	}
}

func TestLoadRawSourceRejectsTraversal(t *testing.T) {
	rawDir := t.TempDir()
	if _, ok := loadRawSource(rawDir, "raw/ko/../../secret.md"); ok {
		t.Fatal("expected path traversal to be rejected")
	}
}
