---
title: Overview — Brainpedia
type: overview
status: active
sources: [2026-04-04-llm-wiki, 2026-08-04-llm-wiki-concept]
updated: 2026-08-28
tags: [meta, wiki, brainpedia]
---

# Overview

## Summary

**Brainpedia** — vault `mindscape` ini adalah persistent compounding wiki berbasis pattern Karpathy. LLM jadi librarian/maintainer, Obsidian jadi IDE. Alur `raw sources → LLM processing → persistent wiki → future queries`, bukan RAG re-derive tiap query. Aturan epistemik [[concepts/epistemic-rules]] dijaga: fakta vs inference vs spekulasi vs opini dipisah dan disitasi per klaim.

## Content

### Thesis / Working Synthesis

> Vault ini mengimplementasikan **persistent compounding wiki** (Karpathy 2026-04-04): daripada RAG yang re-derive tiap query, pengetahuan dikompilasi sekali ke `wiki/` dan dijaga tetap current via ingest/query/lint. Satu ingest menyentuh 10-15 halaman; cross-reference, kontradiksi, dan sintesis sudah siap sebelum ditanya. Spirit-nya adalah [[concepts/memex]] Bush (1945) — private curated store dengan associative trails — yang baru feasible karena LLM yang handle bookkeeping membosankan. Manusia kurasi sumber & tanya pertanyaan bagus; LLM jadi programmer, Obsidian jadi IDE, wiki jadi codebase.

### Architecture (from [[sources/2026-04-04-llm-wiki]])

- **Layer 1 — Raw (`raw/sources/`, `raw/assets/`)**: curated immutable sources. Web clips, PDFs, notes. Downloaded images via `Ctrl+Shift+D`. Never edited by the LLM.
- **Layer 2 — Wiki (`wiki/`)**: LLM-owned persistent artifact. `index.md` (content catalog), `log.md` (chronology), topic/entity pages, syntheses. Updated on every ingest/query/lint.
- **Layer 3 — Schema (`AGENTS.md` / `CLAUDE.md`)**: the contract that makes the LLM a disciplined maintainer — naming, frontmatter, page structure, ingest/query/lint workflows, pin handling.

### Key Ideas to Track

- [[concepts/brainpedia]] — Brainpedia itu sendiri (nama & tujuan vault ini)
- [[concepts/persistent-wiki]] — compounding artifact: compile once, keep current
- [[concepts/rag-vs-wiki]] — perbandingan RAG re-derive vs wiki persistent
- [[concepts/three-layer-architecture]] — raw / wiki / schema
- [[concepts/epistemic-rules]] — fakta vs inference vs spekulasi, flag contradiction
- [[conventions]] — naming, frontmatter, linking, Obsidian, search, git
- [[concepts/obsidian-as-ide]] — "LLM is programmer, Obsidian is IDE, wiki is codebase"
- [[concepts/index-vs-log]] — index (katalog) vs log (kronologi)
- [[concepts/ingest-operation]] / [[concepts/query-operation]] / [[concepts/lint-operation]] — tiga operasi utama
- [[concepts/memex]] — akar historis Bush 1945

### Graph Health

- Ingest #1 (2026-04-04-llm-wiki): 9 concepts + 2 entities + 1 source. Ingest #2 (2026-08-04-llm-wiki-concept): +1 source + 3 halaman (brainpedia, epistemic-rules, conventions) + folder `wiki/analyses/`. Total ~15 halaman wiki.
- Semua sudah cross-link via `## Related` dan terdaftar di `[[index]]`.
- Goal: zero orphans. Saat ini `python scripts/lint.py` orphan hanya `wiki/inbox/README.md` (staging, expected).

## Sources

- [[sources/2026-04-04-llm-wiki]] — Karpathy gist `442a6bf555914893e9891c11519de94f` (2026-04-04)
- [[sources/2026-08-04-llm-wiki-concept]] — Brainpedia spec (2026-08-04)
- `raw/sources/2026-04-04-llm-wiki.md`, `raw/sources/2026-08-04-llm-wiki-concept.md`

## Related

- [[index]]
- [[log]]
- [[sources/2026-04-04-llm-wiki]]
- [[sources/2026-08-04-llm-wiki-concept]]
- [[concepts/brainpedia]]
- [[conventions]]
