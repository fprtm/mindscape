---
title: Wiki Index
type: index
status: active
updated: 2026-08-28
---

# Wiki Index

> Content catalog — every page with 1-line summary. LLM reads this first for every query/ingest. Keep sorted by type.

## Overview

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| [[overview]] | overview | Synthesis / thesis of the whole wiki | — | 2026-08-28 |

## Sources

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| [[sources/2026-04-04-llm-wiki]] | source | Karpathy LLM Wiki pattern — persistent compounding wiki vs RAG | 2026-04-04-llm-wiki | 2026-08-28 |

## Concepts

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| *empty — will populate on ingest* | | | | |

## Entities

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| *empty — will populate on ingest* | | | | |

## Syntheses

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| *empty — will populate on ingest* | | | | |

## Questions

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| *empty — will populate on query filing* | | | | |

---

### Dataview catalog (auto-generates once pages have frontmatter)

```dataview
TABLE type, status, updated, tags
FROM "wiki"
WHERE type != "index"
SORT updated DESC
```

### Maintenance

- One row per `wiki/**/*.md` (except this file). Keep summaries to one line.
- `Sources` column lists raw slug(s) that support the page, e.g. `2026-04-04-llm-wiki`.
- On ingest: add/update rows immediately; don't let index drift.
- For concurrent ingests: reserve `status: planned` placeholder rows before generation (see AGENTS.md §3.1).

## Related
- [[overview]]
- [[log]]
