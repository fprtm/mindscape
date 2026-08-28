---
title: Wiki Log
type: log
status: active
updated: 2026-08-28
---

# Wiki Log

> Chronological, append-only. Prefix every entry `## [YYYY-MM-DD] <op> | <title>` for `grep "^## \["` parsing.

## [2026-08-28] setup | Initialize LLM Wiki vault

- Operation: setup
- Raw: `raw/sources/2026-04-04-llm-wiki.md` (Karpathy gist fetched and saved)
- Created: `AGENTS.md`, `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`, directory structure `raw/{sources,assets}`, `wiki/{concepts,entities,sources,syntheses,questions,inbox}`, `scripts/`
- Config: `.obsidian/app.json` attachment path → `raw/assets`, graph settings, helper scripts `scripts/search.py` + `scripts/lint.py`
- Notes: Vault initialized as 3-layer system (raw immutable / wiki LLM-owned / schema). Ready for first ingest. Next: `ingest raw/sources/2026-04-04-llm-wiki.md` or drop new source.

## [2026-08-28] ingest | raw/sources/* — batch ingest 2026-04-04-llm-wiki

- Raw: `raw/sources/2026-04-04-llm-wiki.md` (Karpathy gist 442a6bf555914893e9891c11519de94f)
- Created: `wiki/concepts/persistent-wiki.md`, `wiki/concepts/rag-vs-wiki.md`, `wiki/concepts/three-layer-architecture.md`, `wiki/concepts/obsidian-as-ide.md`, `wiki/concepts/ingest-operation.md`, `wiki/concepts/query-operation.md`, `wiki/concepts/lint-operation.md`, `wiki/concepts/memex.md`, `wiki/concepts/index-vs-log.md`, `wiki/entities/karpathy.md`, `wiki/entities/vannevar-bush.md`
- Updated: `wiki/overview.md` (thesis + key ideas), `wiki/index.md` (11 new rows), `wiki/sources/2026-04-04-llm-wiki.md` (already existed)
- Notes: Batch ingest requested as `ingest overall in raw/sources/*` (first pass). 1 source present, expanded to 9 concepts + 2 entities per AGENTS.md §3.1 (5-15 pages).

## [2026-08-28] ingest | raw/sources/2026-08-04-llm-wiki-concept.md — Brainpedia spec

- Raw: `raw/sources/2026-08-04-llm-wiki-concept.md` (Brainpedia task spec, 180 lines)
- Created: `wiki/sources/2026-08-04-llm-wiki-concept.md`, `wiki/concepts/brainpedia.md`, `wiki/concepts/epistemic-rules.md`, `wiki/conventions.md`, `wiki/analyses/` (folder, alias for syntheses)
- Updated: `wiki/overview.md` (rename to Brainpedia, thesis + epistemic link), `wiki/index.md` (+3 concepts +1 conventions +1 source), `wiki/sources/2026-04-04-llm-wiki.md` untouched
- Notes: Second source in batch `raw/sources/*`. Diterapkan mapping spec: `schema/` → `AGENTS.md`/`CLAUDE.md` + `conventions.md`, `wiki/analyses/` ditambah tanpa hapus `syntheses/`. Aturan epistemik dipisah jadi halaman tersendiri. Tidak ada destructive operation.

---
