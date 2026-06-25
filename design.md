# LG-Family Agent Product Design Pattern

_Last updated: 2026-06-25_

This document defines the reusable design pattern for LG-related agent projects. It uses the current LG Energy Solution wiki as the reference implementation, but the pattern is meant to transfer to future battery, electronics, DevOps, research, security, factory, and operations agents.

The goal is not to force every project into the same set of tabs. The goal is to make every project feel like it belongs to the same LG-family product line: branded, domain-specific, evidence-first, and clear about what the agent is doing.

---

## 1. Core Principle: Workstation Clarity

Every LG-family agent project should make five things immediately clear:

1. **Where am I?**  
   The product identity, domain, and assistant role should be visible without reading documentation.

2. **What am I looking at?**  
   The current object, page, source, run, task, service, or dataset should have a stable canonical detail view.

3. **What is the agent doing?**  
   Agent activity should be visible through steps, status, tool history, retrieval paths, or run logs.

4. **Why should I trust the result?**  
   The interface should expose evidence: source documents, citations, retrieved objects, logs, checks, or state transitions.

5. **What visual family does this belong to?**  
   Every project must use the fixed LG red identity layer plus a disciplined semantic theme palette.

The product should feel like an expert workstation, not a generic chatbot and not a decorative dashboard.

---

## 2. Product Shape: Flexible Surface Archetypes

Do **not** force every project to have four views or four tabs. Instead, identify which parts of a project resemble these surface archetypes and apply the relevant guidance.

A single screen may contain multiple archetypes.

For example:

- A chat answer with citations is an **Ask Surface** plus evidence cards.
- A dependency graph is a **Map Surface**.
- A service health dashboard is an **Operate Surface**.
- A wiki page browser is an **Explore Surface**.

### 2.1 Explore Surface

Use when the UI lets users browse domain objects.

Examples:

- Wiki pages
- Documents
- Services
- Jobs
- Agents
- Datasets
- Tickets
- Models
- Experiments
- Battery chemistries, electronic components, factory systems, or infrastructure resources

Design guidance:

- Provide search and filtering near the object list.
- Each object row/card should include type, title, summary, and useful tags/status.
- Opening an object should show its canonical detail, not a transient generated answer.
- The selected object should be visually obvious using the LG red identity layer.
- Related objects should be visible as links, cards, breadcrumbs, or a compact map.

Reference in LGES wiki:

- Left page list + article reader.
- Page metadata chips: type, tags, confidence, updated date, source count.

### 2.2 Map Surface

Use when the UI shows relationships.

Examples:

- Knowledge graph
- Citation graph
- Service topology
- Agent routing map
- Workflow DAG
- Dependency graph
- Incident blast radius
- Manufacturing or process flow

Design guidance:

- The map must answer “how things connect,” not merely look interesting.
- Always provide a readable fallback: related cards, table, step list, breadcrumbs, or textual summary.
- Dense maps need focus mode, search mode, filters, or progressive disclosure.
- Clicking a node should open the canonical Explore detail.
- Avoid unlabeled decorative graph blobs. If labels are too dense, switch to compact pills or focus mode.

Reference in LGES wiki:

- Full knowledge graph.
- Related-page mini graph inside the reader.
- Chat tool-history tree.

### 2.3 Ask Surface

Use when the UI lets the user communicate with an agent.

Examples:

- Chat
- Command box
- Copilot panel
- Natural-language query
- Q&A over documents
- Analyst assistant
- Troubleshooting assistant

Design guidance:

- The assistant should not be a black box.
- Separate user message, agent activity, final answer, and evidence.
- Show retrieved objects, source documents, citations, tool calls, or reasoning path summaries.
- Suggested prompts should teach the user what the agent is good at.
- The assistant identity should use LG red, but long-form answers should remain readable on neutral surfaces.
- Do not make every assistant answer a solid red block; use LG red for identity, headers, accents, active states, and primary recommendations.

Reference in LGES wiki:

- Chat view with prompt chips.
- Agent activity: search → read → follow → source → answer.
- Primary evidence cards and source IDs.

### 2.4 Operate Surface

Use when the UI exposes actions, runs, diagnostics, or system state.

Examples:

- Deployment runs
- Cron jobs
- Test runs
- Scraper status
- Logs
- Diagnostics
- Health checks
- Agent task queues
- “Apply this fix” workflows
- Infrastructure and DevOps actions

Design guidance:

- Make state explicit: pending, running, succeeded, failed, stale, blocked.
- Show recent events and timestamps.
- Logs should be readable, filterable, and linked to affected objects.
- Dangerous actions need clear scope visibility.
- Completion should be grounded in real output, not just optimistic labels.

Reference in LGES wiki:

- Diagnostics surface with access state, page count, graph link count, and client event log.

---

## 3. Assistant Identity: Domain-Specific Branded Assistants

Every project should define its own domain-specific assistant identity under the LG visual family.

Use names like:

- **LG Battery Analyst** — battery technology, ESS, EV cells, manufacturing, LG Energy Solution sources.
- **LG Ops Agent** — DevOps, deployment, service health, logs, infrastructure actions.
- **LG Electronics Expert** — electronics, hardware debugging, components, signal/power/thermal analysis.
- **LG Security Analyst** — security review, SAST/DAST, vulnerabilities, threat modeling.
- **LG Factory Agent** — PLC, manufacturing automation, process troubleshooting.
- **LG Research Assistant** — papers, technical reports, market or patent intelligence.

Each project must declare:

```md
## Assistant Identity

- Assistant name:
- Domain:
- Primary user:
- Primary promise:
- Typical questions:
- Typical actions:
- Evidence sources:
- Domain colors:
```

Example for the current LGES wiki:

```md
## Assistant Identity

- Assistant name: LG Battery Analyst
- Domain: Battery technology, ESS, EV cells, manufacturing, LG Energy Solution sources
- Primary user: Engineer, analyst, researcher, product stakeholder
- Primary promise: Explain battery topics with source-grounded evidence and visible retrieval path
- Typical questions:
  - Compare LFP and NCM for ESS vs EV use
  - Explain thermal runaway prevention
  - Map LGES partnerships and battery chemistries
- Typical actions:
  - Search wiki pages
  - Follow related concepts
  - Read primary source blogs/documents
  - Produce cited answers
- Evidence sources:
  - Compiled wiki pages
  - Original LGES blogs
  - Corporate documents
  - Source citations
- Domain colors:
  - Teal for concepts / energy systems
  - Amber for comparisons / trade-offs
  - Purple for glossary / evidence
```

---

## 4. Theme System

### 4.1 Fixed LG Identity Tokens

LG red is absolute across LG-related projects.

```css
:root {
  --lg-red: #a50034;
  --lg-red-hover: #8d002d;
  --lg-red-soft: #fde8ef;

  --accent: var(--lg-red);
  --accent-hover: var(--lg-red-hover);
  --accent-soft: var(--lg-red-soft);
  --assistant-accent: var(--lg-red);
  --primary-action: var(--lg-red);
}
```

LG red represents the branded assistant/system layer:

- Assistant identity
- Primary recommendations
- Primary actions
- Active navigation
- Selected objects
- Focus rings
- Important links
- Premium product identity

LG red should not be treated as just another taxonomy color. It is the product family anchor.

### 4.2 Neutral Workstation Base

The neutral base should remain stable across projects unless there is a strong reason to change it.

```css
:root {
  --bg: #f5f7fb;
  --surface: #ffffff;
  --surface-muted: #eef2f7;
  --surface-strong: #e2e8f0;

  --text: #172033;
  --text-muted: #64748b;
  --text-soft: #94a3b8;
  --border: #d7dee8;

  --shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
  --radius: 8px;
}
```

This creates the default enterprise workstation feel: light, clean, dense enough for expert work, but not visually noisy.

### 4.3 Domain Palette Tokens

Each project may define domain colors, but only through semantic tokens.

Do not invent one-off raw colors inside components. Components should consume tokens such as `--domain-primary`, `--state-success`, or `--evidence-accent`.

Battery / energy default:

```css
:root {
  --domain-primary: #00766f;
  --domain-primary-soft: #e2f4f2;
  --domain-secondary: #b45309;
  --domain-secondary-soft: #fef3c7;
  --domain-tertiary: #7c3aed;
  --domain-tertiary-soft: #ede9fe;
}
```

DevOps / infrastructure example:

```css
:root {
  --domain-primary: #2563eb;
  --domain-primary-soft: #dbeafe;
  --domain-secondary: #0f766e;
  --domain-secondary-soft: #ccfbf1;
  --domain-tertiary: #9333ea;
  --domain-tertiary-soft: #f3e8ff;
}
```

Electronics / hardware example:

```css
:root {
  --domain-primary: #2563eb;
  --domain-primary-soft: #dbeafe;
  --domain-secondary: #16a34a;
  --domain-secondary-soft: #dcfce7;
  --domain-tertiary: #ea580c;
  --domain-tertiary-soft: #ffedd5;
}
```

### 4.4 State Tokens

Use consistent state colors across projects.

```css
:root {
  --state-success: #00766f;
  --state-success-soft: #e2f4f2;
  --state-warning: #b45309;
  --state-warning-soft: #fef3c7;
  --state-danger: #9f1239;
  --state-danger-soft: #fff1f2;
  --state-info: #2563eb;
  --state-info-soft: #dbeafe;
}
```

State colors should communicate operational meaning, not decoration.

### 4.5 Taxonomy Tokens

Projects should map object categories to taxonomy tokens.

LGES wiki example:

```css
:root {
  --taxonomy-entity: var(--lg-red);
  --taxonomy-concept: #00766f;
  --taxonomy-comparison: #b45309;
  --taxonomy-glossary: #7c3aed;
}
```

Guidance:

- Taxonomy colors are for classification.
- State colors are for operational status.
- LG red is for brand/system identity and selected/primary states.
- Avoid using color alone; pair colors with labels, icons, or text.

---

## 5. Component Rules

### 5.1 Topbar / Product Header

The header should answer “where am I?”

Required elements:

- LG-family brand marker or logo.
- Product name.
- Short domain subtitle.
- Search or command entry when relevant.
- Navigation only if it helps the current product.

The header should stay compact. Avoid marketing hero sections inside workstations.

### 5.2 Navigation

Navigation should adapt to the project. Do not force Browse / Graph / Chat / Diagnostics as mandatory tabs.

Allowed patterns:

- Tabs for major surfaces.
- Sidebar for object categories.
- Split panel for object list + detail.
- Command palette for power users.
- Contextual action bar for Operate surfaces.

Rules:

- Active nav uses LG red.
- Labels should be domain-specific when helpful.
- Navigation should describe user tasks, not internal implementation.

### 5.3 Cards and Panels

Cards should be information-dense but calm.

Use cards for:

- Domain objects.
- Evidence sources.
- Retrieved pages.
- Tool steps.
- Run summaries.
- Related objects.

Each card should usually include:

- Title
- Type/status chip
- Short summary
- Optional metadata row
- Optional action or link

### 5.4 Chat Messages

For sellable LG-facing products, LG red should brand the assistant/system, not merely the user.

Recommended pattern:

- User bubble: neutral dark or subtle surface.
- Assistant avatar/icon/header: LG red.
- Assistant answer body: neutral white surface for readability.
- Agent activity: LG red accent plus state labels.
- Evidence/citations: domain/evidence colors with clear labels.

Avoid making long assistant messages solid red.

### 5.5 Evidence Cards

Evidence cards should be first-class UI, not an afterthought.

Evidence cards may represent:

- Source documents
- Raw files
- Web pages
- Logs
- Test output
- Citations
- Retrieved wiki pages
- Tool results

Each evidence card should include:

- Stable ID or citation marker
- Source title
- Source type/path/date when available
- Snippet or summary
- Link to open full source or related object

### 5.6 Agent Activity / Tool History

Whenever an agent performs non-trivial work, expose a concise activity trail.

Good activity labels:

- Search
- Read
- Follow
- Fetch source
- Check status
- Run test
- Inspect log
- Compose answer
- Apply change
- Verify result

Do not expose private chain-of-thought. Show observable actions and concise decision summaries.

---

## 6. Evidence-First Behavior

All generated outputs should be grounded in visible support.

For knowledge products:

- Show retrieved pages.
- Show primary sources.
- Cite source IDs inline.
- Let users open the source without leaving the flow.

For operations products:

- Show command/test/deploy output.
- Show status transitions.
- Link logs to affected services or tasks.
- Distinguish queued, running, completed, failed, and blocked states.

For research products:

- Show source documents and dates.
- Mark confidence and contradictions.
- Keep source snippets near claims.

Trust comes from inspectability. The user should be able to answer: “What did the agent look at, and what did it do?”

---

## 7. Responsive Behavior

The desktop experience should feel like a workstation. The mobile experience should feel like a focused task flow, not a squeezed desktop.

Desktop guidance:

- Multi-panel layouts are acceptable.
- Use sidebars, readers, context panels, maps, and evidence drawers.
- Keep dense expert information visible.

Mobile guidance:

- Collapse to a single primary task at a time.
- Prefer bottom sheets, drawers, or stacked sections for secondary context.
- Keep primary action reachable.
- Do not require users to inspect dense graphs on mobile; provide lists and summaries.
- Evidence must remain accessible even if hidden behind a drawer.

---

## 8. Reusable Project Template

Copy this section into new LG-family agent projects and fill it in.

```md
# Design

## Product Identity

- Product name:
- Domain:
- Primary users:
- Product promise:
- LG-family positioning:

## Assistant Identity

- Assistant name:
- Domain:
- Primary user:
- Primary promise:
- Typical questions:
- Typical actions:
- Evidence sources:
- Domain colors:

## Workstation Clarity

This product must make clear:

1. Where the user is:
2. What object/task/source/run is active:
3. What the agent is doing:
4. What evidence/state supports the result:
5. How the visual theme belongs to the LG family:

## Surface Archetypes Used

Do not include every archetype by default. Include only those naturally present.

### Explore Surface

- Domain objects browsed:
- Search/filter behavior:
- Canonical detail view:
- Related object behavior:

### Map Surface

- Relationship type shown:
- Focus/search/filter behavior:
- Readable fallback:
- Node click behavior:

### Ask Surface

- Input style:
- Assistant activity visibility:
- Evidence display:
- Suggested prompts:
- Citation/source behavior:

### Operate Surface

- Actions/runs/statuses exposed:
- State model:
- Logs/events:
- Safety/scope visibility:
- Verification behavior:

## Theme Tokens

### Fixed LG Tokens

- `--lg-red: #a50034`
- `--lg-red-hover: #8d002d`
- `--lg-red-soft: #fde8ef`

### Neutral Base

- `--bg:`
- `--surface:`
- `--surface-muted:`
- `--text:`
- `--text-muted:`
- `--border:`

### Domain Tokens

- `--domain-primary:`
- `--domain-primary-soft:`
- `--domain-secondary:`
- `--domain-secondary-soft:`
- `--domain-tertiary:`
- `--domain-tertiary-soft:`

### Taxonomy Mapping

- Category A:
- Category B:
- Category C:
- Category D:

### State Mapping

- Success:
- Warning:
- Danger:
- Info:

## Component Notes

- Header:
- Navigation:
- Object cards:
- Detail view:
- Chat:
- Evidence cards:
- Agent activity:
- Diagnostics / operations:

## Responsive Rules

- Desktop layout:
- Tablet layout:
- Mobile layout:
- Evidence on mobile:
- Map/graph fallback on mobile:

## Non-Goals

- What this product should not try to be:
- Views/surfaces intentionally omitted:
- Interactions intentionally deferred:
```

---

## 9. Current LGES Wiki Mapping

The current LGES wiki should map to the pattern like this:

```md
## Product Identity

- Product name: LG Energy Solution Wiki
- Domain: Battery technology, ESS, EV batteries, LGES partnerships, manufacturing, source-grounded battery research
- Primary users: Engineers, analysts, researchers, technical stakeholders
- Product promise: Explore and ask questions over LGES battery knowledge with visible evidence and source grounding
- LG-family positioning: Evidence-first LG Battery Analyst workstation

## Assistant Identity

- Assistant name: LG Battery Analyst
- Domain: Battery technology and LG Energy Solution source corpus
- Primary user: Engineer, analyst, researcher, product stakeholder
- Primary promise: Explain battery topics with source-grounded evidence and visible retrieval path
- Typical questions:
  - Compare LFP and NCM for ESS and EV use
  - Explain why fast charging is difficult
  - Map battery safety, separator design, and thermal propagation prevention
- Typical actions:
  - Search compiled wiki pages
  - Read relevant pages
  - Follow wikilinks
  - Read primary source documents
  - Produce cited answer
- Evidence sources:
  - Wiki pages
  - Original LGES blog posts
  - Corporate documents
  - Regional/JV public sources
- Domain colors:
  - LG red: identity, assistant/system, selected state, primary action
  - Teal: concepts and energy systems
  - Amber: comparisons and trade-offs
  - Purple: glossary, citations, primary evidence
```

Surface mapping:

- Explore: Browse page list + article reader + source section.
- Map: Full graph + related-page mini graph + chat tool-history tree.
- Ask: Chat with prompt chips, activity trail, cited answers, evidence cards.
- Operate: Diagnostics page and client event log.

Known design debts to resolve later:

- `login.html` should use the same LGES logo treatment as the SPA, not the generic lightning emoji.
- UI labels such as “Korean source blogs” should generalize to “Primary sources” because the corpus now includes English, corporate, regional, and JV records.
- The source loader/deployment should align with the actual multi-source corpus, not only `raw/ko`.
- Mobile should be treated as a focused task flow with evidence drawers and graph fallbacks, not just a collapsed desktop.

---

## 10. Implementation Checklist

Before shipping a new LG-family agent project, verify:

- [ ] LG red is fixed at `#a50034` and used as the assistant/system brand anchor.
- [ ] Domain colors are defined through semantic tokens, not one-off component colors.
- [ ] The assistant has a domain-specific branded identity.
- [ ] The project declares which surface archetypes it uses.
- [ ] Explore-like surfaces have search/filter and canonical details.
- [ ] Map-like surfaces have readable fallbacks.
- [ ] Ask-like surfaces expose evidence and agent activity.
- [ ] Operate-like surfaces expose state, logs, and verification.
- [ ] Evidence is visible near generated outputs.
- [ ] Mobile behavior is designed explicitly.
- [ ] Component colors come from tokens.
- [ ] The UI answers: where am I, what am I viewing, what is the agent doing, and why should I trust it?
