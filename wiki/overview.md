---
title: Overview
type: overview
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [meta, wiki]
---

# Overview

## Summary

This vault implements Karpathy's LLM Wiki pattern: a persistent, compounding knowledge base where the LLM incrementally compiles raw sources into an interlinked wiki. Raw sources remain immutable; the wiki is LLM-maintained; the schema (`AGENTS.md`) is the discipline that makes it compound.

## Content

### Thesis / Working Synthesis

*Empty on initialization — this section will evolve as sources are ingested. It should hold the 3-5 sentence current synthesis of everything in the vault.*

> Placeholder: The wiki is young. Add sources via `raw/sources/` and run ingest to build the thesis here.

### Architecture (from [[sources/2026-04-04-llm-wiki]])

- **Layer 1 — Raw (`raw/sources/`, `raw/assets/`)**: curated immutable sources. Web clips, PDFs, notes. Downloaded images via `Ctrl+Shift+D`. Never edited by the LLM.
- **Layer 2 — Wiki (`wiki/`)**: LLM-owned persistent artifact. `index.md` (content catalog), `log.md` (chronology), topic/entity pages, syntheses. Updated on every ingest/query/lint.
- **Layer 3 — Schema (`AGENTS.md` / `CLAUDE.md`)**: the contract that makes the LLM a disciplined maintainer — naming, frontmatter, page structure, ingest/query/lint workflows, pin handling.

### Key Ideas to Track

- [[concepts/persistent-wiki]] (planned) — compounding artifact vs per-query RAG
- [[concepts/rag-vs-wiki]] (planned) — RAG re-derives; wiki compiles once
- [[concepts/obsidian-as-ide]] (planned) — "LLM is programmer, Obsidian is IDE, wiki is codebase"

### Graph Health

- No pages yet — graph view will populate after first ingest.
- Goal: zero orphans, every page reachable via `Related` links and `index.md`.

## Sources

- [[sources/2026-04-04-llm-wiki]] — Karpathy gist `442a6bf555914893e9891c11519de94f` (2026-04-04)
- `raw/sources/2026-04-04-llm-wiki.md` (local mirror)

## Related

- [[index]]
- [[log]]
- [[sources/2026-04-04-llm-wiki]]
