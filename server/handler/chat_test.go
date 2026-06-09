package handler

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestFuzzyFindSlugRejectsEmptyQuery(t *testing.T) {
	slugs := map[string]string{"fast-charging": "Fast Charging"}
	if got := fuzzyFindSlug(slugs, ""); got != "" {
		t.Fatalf("expected no match for an empty query, got %q", got)
	}
}

func TestContainsSlugHandlesAnchorsAndCase(t *testing.T) {
	slugs := []string{"Fast-Charging#overview", "battery-safety"}
	if !containsSlug(slugs, "fast-charging") {
		t.Fatal("expected anchored wikilink to match its page slug")
	}
	if containsSlug(slugs, "separator") {
		t.Fatal("did not expect an unrelated slug to match")
	}
}

func TestReactTurnLimitUsesOneFifthOfIndexedPages(t *testing.T) {
	tests := []struct {
		pages int
		want  int
	}{
		{pages: 0, want: 1},
		{pages: 1, want: 1},
		{pages: 5, want: 1},
		{pages: 6, want: 2},
		{pages: 24, want: 5},
		{pages: 96, want: 20},
	}

	for _, test := range tests {
		if got := reactTurnLimit(test.pages); got != test.want {
			t.Errorf("reactTurnLimit(%d) = %d, want %d", test.pages, got, test.want)
		}
	}
}

func TestSearchWikiDetailedReportsActualScan(t *testing.T) {
	wikiDir := t.TempDir()
	conceptsDir := filepath.Join(wikiDir, "concepts")
	if err := os.MkdirAll(conceptsDir, 0o755); err != nil {
		t.Fatal(err)
	}
	pages := map[string]string{
		"fast-charging.md": "---\ntitle: Fast Charging\n---\nFast charging raises battery temperature.",
		"separator.md":     "---\ntitle: Separator\n---\nA separator prevents electrical shorts.",
	}
	for name, body := range pages {
		if err := os.WriteFile(filepath.Join(conceptsDir, name), []byte(body), 0o644); err != nil {
			t.Fatal(err)
		}
	}

	result := searchWikiDetailed(wikiDir, "fast charging", 3)
	if len(result.Pages) != 1 || result.Pages[0].Slug != "fast-charging" {
		t.Fatalf("expected fast-charging as the only result, got %#v", result.Pages)
	}
	for _, expected := range []string{
		`Query: "fast charging"`,
		"Terms: fast | charging",
		"Scanned: 2 pages; matched: 1",
		"Fast Charging (fast-charging), score",
	} {
		if !strings.Contains(result.Details, expected) {
			t.Errorf("search details missing %q:\n%s", expected, result.Details)
		}
	}
}

func TestSearchWikiDetailedExpandsBatterySynonyms(t *testing.T) {
	wikiDir := t.TempDir()
	conceptsDir := filepath.Join(wikiDir, "concepts")
	if err := os.MkdirAll(conceptsDir, 0o755); err != nil {
		t.Fatal(err)
	}
	pages := map[string]string{
		"cathode-materials.md": "---\ntitle: Cathode Materials\n---\nLithium-ion cells use active material on this electrode.",
		"separator.md":         "---\ntitle: Separator\n---\nA separator prevents electrical shorts.",
	}
	for name, body := range pages {
		if err := os.WriteFile(filepath.Join(conceptsDir, name), []byte(body), 0o644); err != nil {
			t.Fatal(err)
		}
	}

	result := searchWikiDetailed(wikiDir, "양극재", 3)
	if len(result.Pages) == 0 || result.Pages[0].Slug != "cathode-materials" {
		t.Fatalf("expected Korean cathode synonym to find cathode-materials, got %#v", result.Pages)
	}
	if !strings.Contains(result.Details, "Expanded terms:") {
		t.Fatalf("expected expanded-term details, got:\n%s", result.Details)
	}
}

func TestSourceSnippetSelectsRelevantParagraph(t *testing.T) {
	body := strings.Join([]string{
		"첫 번째 문단은 회사 소개만 다룹니다.",
		"두 번째 문단은 전해질과 gas-free solvent가 배터리 swelling을 줄이는 방식에 대해 설명합니다.",
		"마지막 문단은 다른 소식을 다룹니다.",
	}, "\n\n")

	got := sourceSnippet(body, "battery swelling prevention")
	if !strings.Contains(got, "swelling") || !strings.Contains(got, "gas-free") {
		t.Fatalf("expected swelling paragraph snippet, got %q", got)
	}
}

func TestDecisionDetailsUsesSummaryAndLimitsLength(t *testing.T) {
	got := decisionDetails("  Need   the linked safety page. ", "fallback")
	if got != "Decision: Need the linked safety page." {
		t.Fatalf("unexpected normalized decision: %q", got)
	}

	long := decisionDetails(strings.Repeat("x", 400), "fallback")
	if len([]rune(long)) > len([]rune("Decision: "))+360 {
		t.Fatalf("decision was not limited: %d runes", len([]rune(long)))
	}
}
