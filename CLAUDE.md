# CLAUDE.md — LLM Wiki Schema for Mindscape

This is the **schema** for the LLM Wiki pattern (Karpathy `llm-wiki.md` 2026-04-04). It tells any LLM agent (OpenCode, Claude Code, Codex, Pi) how this vault is structured and what workflows to follow.

You are the **programmer**, Obsidian is the **IDE**, the wiki is the **codebase**. The human curates sources and asks questions — you do all the bookkeeping.

---

## 1. Architecture — Three Layers

```
mindscape/
├── raw/                  # Layer 1: IMMUTABLE sources (you READ only, never edit)
│   ├── sources/          # Drop new sources here (.md from Web Clipper, PDFs, notes)
│   └── assets/           # Locally downloaded images (attachmentFolderPath)
├── wiki/                 # Layer 2: LLM-OWNED persistent wiki (you WRITE here)
│   ├── index.md          # Content catalog — every page with 1-line summary
│   ├── log.md            # Chronological append-only history
│   ├── overview.md       # Synthesis / thesis of the whole wiki
│   ├── sources/          # One summary page per raw source
│   ├── concepts/         # Topic pages (ideas, theories, themes)
│   ├── entities/         # Entity pages (people, orgs, books, places, tools)
│   ├── syntheses/        # Comparisons, thesis evolutions, deep dives
│   ├── questions/        # Filed answers that compound (query -> wiki page)
│   └── inbox/            # Staging for drafts awaiting human review
├── scripts/              # Optional CLI helpers (search, lint)
├── .obsidian/            # Obsidian config (graph, attachment path)
├── AGENTS.md             # This file (schema for OpenCode/Codex)
└── CLAUDE.md             # Mirror schema for Claude Code
```

**Rule:** `raw/` is source of truth — never modify. `wiki/` is derived — you own it entirely. If a fact is only in chat history and not in `wiki/`, it does not exist.

---

## 2. Conventions

### 2.1 File naming
- `kebab-case` slugs, e.g. `wiki/concepts/spaced-repetition.md`, `wiki/entities/karpathy.md`
- Source summaries: mirror raw name `raw/sources/2026-04-04-llm-wiki.md` → `wiki/sources/2026-04-04-llm-wiki.md`
- No spaces, no caps, no duplicate names across folders (use `concepts/eori-number.md` not separate `eori.md` + `eori-number.md`).

### 2.2 Frontmatter (YAML) — required on every wiki page
```yaml
---
title: Spaced Repetition
type: concept          # concept | entity | source | synthesis | question | overview
status: active         # active | planned | stub | deprecated
sources: [2026-04-04-llm-wiki]  # slugs of raw sources that support this page
updated: 2026-04-04
tags: [learning, memory]
aliases: [SRS]
---
```

### 2.3 Page structure (deterministic headers)
Every page must have:
1. `# Title`
2. `## Summary` — 2-3 sentence TL;DR
3. `## Details` / `## Content` — main body with `[[wiki-links]]` to other pages
4. `## Sources` — bullet list of `[[wiki/sources/...]]` or `raw/sources/...` citations
5. `## Related` — outgoing `[[links]]` (keeps graph connected)

Cross-reference liberally. An orphan page (0 inbound links) is a bug.

### 2.4 Links & Graph
- Use `[[wiki/concepts/foo]]` or `[[foo]]` if unique. The graph view is your linter.
- Every ingest must create/update `Related` sections on touched pages.

### 2.5 Dataview & Obsidian
- Frontmatter fields are Dataview-queryable. Keep `type`, `status`, `updated`, `tags` consistent.
- Images: always reference `raw/assets/...` locally, never remote URLs.

---

## 3. Operations

### 3.1 INGEST — when human says `ingest <path>` or drops file in `raw/sources/`

Do this **one source at a time** with human in loop (unless they say `batch ingest`):

1. **Read** the raw source fully (text first, then images in `raw/assets/` separately if any).
2. **Discuss** key takeaways with human — ask what to emphasize before writing.
3. **Plan** target pages: which existing pages to update vs new pages to create.
   - Check `wiki/index.md` first to avoid duplicates.
   - Reserve new slugs as `status: planned` in index to avoid concurrent-ingest forks.
4. **Generate**:
   - `wiki/sources/<slug>.md` — faithful summary (claims, evidence, gaps)
   - Update/create 5-15 pages across `concepts/`, `entities/`, `syntheses/`, `overview.md`
   - Every claim that stays or changes must cite its source slug.
   - Flag contradictions explicitly: `> [!WARNING] Contradicts [[old-page]]: old says X, new source says Y`
5. **Index** — update `wiki/index.md` (add/update entries, keep 1-line summary).
6. **Log** — append to `wiki/log.md`:
   ```
   ## [2026-04-04] ingest | llm-wiki — Karpathy
   - Raw: raw/sources/2026-04-04-llm-wiki.md
   - Created: wiki/sources/llm-wiki.md, wiki/concepts/persistent-wiki.md
   - Updated: wiki/overview.md, wiki/concepts/rag-vs-wiki.md
   - Notes: flagged contradiction on RAG recall limits
   ```
7. **Show diff** — summarize what changed and ask human to review in Obsidian.

> Batch backfill: use atomic conditional writes for placeholders (`status: planned` with `claimed_by` set) so parallel ingests degrade create→update without duplicates.

### 3.2 QUERY — when human asks a question

1. Read `wiki/index.md` first, then full-text search (`scripts/search.py` or `grep -r`) and take **union** of both — never index-only.
2. Read top-k relevant wiki pages (not raw sources directly, unless wiki is empty).
3. Synthesize answer with citations `[[wiki/...]]`. Offer formats: markdown page, table, Marp slides, matplotlib chart.
4. **Ask:** "File this answer back into the wiki?" If yes, save to `wiki/questions/<slug>.md` or `wiki/syntheses/<slug>.md`, then update `index.md` + `log.md`:
   ```
   ## [2026-04-04] query | "How does wiki differ from RAG?"
   - Answer: wiki/questions/rag-vs-wiki.md
   - Sources: wiki/concepts/rag.md, wiki/concepts/persistent-wiki.md
   ```

### 3.3 LINT — when human says `lint` or periodically

Check and report (fix with approval):

- Contradictions between pages (same claim differs)
- Stale claims superseded by newer sources (check `updated` vs source date)
- Orphans (0 inbound links) — suggest `Related` links
- Stubs (`status: stub` or `planned` never landed)
- Mentioned-but-missing concepts (entity named but no page)
- Missing cross-refs, duplicate near-concepts (`eori` vs `eori-number`)
- Data gaps — suggest web searches / sources to fill
- **Copied state drift** — values that move (SHAs, counts, dates) must not be quoted literally; point to live home in frontmatter/repo instead. Counts: write "these rules" not "these 5 rules".

Output a lint report as `wiki/syntheses/lint-YYYY-MM-DD.md` and append to `log.md`.

### 3.4 Human corrections (pins) — must survive recompilation

If human edits a wiki page, record a pin:

```json
{ "page": "wiki/concepts/eori-number.md", "kind": "correction",
  "claim": "Threshold applies per shipment", "anchor": "## Registration thresholds",
  "provenance": "human", "status": "active" }
```

Store pins in `wiki/.pins.json` (or frontmatter `pins:`). On regeneration, re-check: satisfied→keep, contradicted by newer source→surface to human, section gone→orphaned.

---

## 4. Indexing & Logging

- **index.md** — content-oriented, one line per page: `| Page | Type | Summary | Sources | Updated |`
- **log.md** — chronological, append-only, prefix `## [YYYY-MM-DD] <op> | <title>` for `grep "^## \["` parsing.

LLM must read `index.md` at start of every query/ingest; update it at end of every ingest/query that creates a page.

---

## 5. Optional CLI Tools

- `scripts/search.py` — naive BM25/full-text over `wiki/` (fallback is `grep -r`). Use when index recall misses buried facts.
- `qmd` (https://github.com/tobi/qmd) — if installed, prefer `qmd search` (hybrid BM25/vector, on-device). Both CLI and MCP.
- `scripts/lint.py` — checks orphans, stubs, duplicate stems, broken links.

Install `qmd` when wiki >~100 sources or >200 pages. Before that, `index.md` + grep is enough.

---

## 6. Tips for Human

- Use **Obsidian Web Clipper** to drop articles → `raw/sources/` as markdown.
- In Obsidian Settings → Files and links → Attachment folder path = `raw/assets`. Hotkey `Ctrl+Shift+D` → Download attachments for current file.
- Browse wiki in Obsidian **Graph View** — hubs, orphans, clusters.
- Marp (slides) + Dataview (queries over frontmatter) plugins are pre-configured ideas — LLM can generate `--- marp: true ---` decks in `wiki/syntheses/`.
- Vault is a git repo — commit often, branch for experiments.

---

## 7. What NOT to do

- Never edit `raw/` — immutable.
- Never create visibility labels `audience: internal` to filter queries — compile a second wiki from safe sources instead. Labels leak via stale derivation.
- Never let source retirement delete human-added pins.
- Never summarize a long session in one giant prompt — partition source, coverage-plan, bounded spans.
- Review **artifacts not plans** — generate draft pages and diff them; don't ask human to approve "intent".

---

## 8. First-Run Checklist (for LLM)

When user says "setup wiki" or "ingest first source":

1. Ensure directories exist (`raw/assets`, `wiki/*`, `scripts`).
2. Create/update `wiki/index.md`, `wiki/log.md`, `wiki/overview.md` if missing.
3. Explain the three layers and ask: what domain will this wiki cover? (personal, research, book, team, hobby?)
4. Suggest first source to ingest (or ingest the Karpathy gist itself as `raw/sources/2026-04-04-llm-wiki.md`).

---

*Schema version: 1.0 (2026-04-04 gist + team-scale lessons). Evolve this file with the human as you learn what works — it's the discipline that makes the wiki compound.*
