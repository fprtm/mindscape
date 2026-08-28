---
title: Overview — Brainpedia
type: overview
status: active
sources: [2026-04-04-llm-wiki, 2026-08-04-llm-wiki-concept, 2026-08-28-chatgpt-konten-vlog]
updated: 2026-08-28
tags: [meta, wiki, brainpedia, content]
---

# Overview

## Summary

**Brainpedia** — vault `mindscape` ini adalah persistent compounding wiki berbasis pattern Karpathy. LLM jadi librarian/maintainer, Obsidian jadi IDE. Alur `raw sources → LLM processing → persistent wiki → future queries`, bukan RAG re-derive tiap query. Aturan epistemik [[concepts/epistemic-rules]] dijaga. Domain pertama yang compounding: **content bible vlog kehidupan** — dari humor template → ke [[concepts/tone-deadpan|Deadpan Self-Deprecating Storytelling]] dengan 5 pilar, 4 formula, struktur 0-45d + visual random footage + VO.

## Content

### Thesis / Working Synthesis

> Vault ini mengimplementasikan **persistent compounding wiki** (Karpathy 2026-04-04): daripada RAG yang re-derive tiap query, pengetahuan dikompilasi sekali ke `wiki/` dan dijaga tetap current via ingest/query/lint. Satu ingest menyentuh 10-15 halaman; cross-reference, kontradiksi, dan sintesis sudah siap sebelum ditanya. Spirit-nya adalah [[concepts/memex]] Bush (1945).
> 
> **Update 2026-08-28**: domain pertama yang masuk adalah **content bible vlog kehidupan** (ChatGPT). Dari masalah `humor terlalu dibuat jokes` → ditemukan identitas `[[concepts/content-bible|Cerita kecil tentang keresahan hidup, ditertawakan secukupnya]]` dengan DNA `Keresahan → serius → belok → self-roast` (lihat [[concepts/content-bible]]). Ini jadi cluster compounding terbesar saat ini di wiki (6 halaman baru), di atas fondasi Brainpedia (Karpathy + spec).

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
- **Content cluster (baru)**: [[concepts/content-bible]] (identitas & DNA), [[concepts/content-pillars]] (5 pilar), [[concepts/tone-deadpan]] (Deadpan Self-Deprecating), [[concepts/formula-konten]] (4 formula), [[concepts/struktur-video]] (0-45d), [[concepts/visual-random-footage]] (random footage + VO)

### Graph Health

- Ingest #1 (2026-04-04-llm-wiki): 9 concepts + 2 entities + 1 source. Ingest #2 (2026-08-04-llm-wiki-concept): +1 source + 3 halaman (brainpedia, epistemic-rules, conventions). Ingest #3 (2026-08-28-chatgpt-konten-vlog): +1 source + 6 halaman content cluster. Total ~22 halaman wiki.
- Semua sudah cross-link via `## Related` dan terdaftar di `[[index]]`.
- Goal: zero orphans. Saat ini `python scripts/lint.py` orphan hanya `wiki/inbox/README.md` (staging, expected).

## Sources

- [[sources/2026-04-04-llm-wiki]] — Karpathy gist `442a6bf555914893e9891c11519de94f` (2026-04-04)
- [[sources/2026-08-04-llm-wiki-concept]] — Brainpedia spec (2026-08-04)
- [[sources/2026-08-28-chatgpt-konten-vlog]] — Content bible vlog (ChatGPT 2026-08-28)
- `raw/sources/2026-04-04-llm-wiki.md`, `raw/sources/2026-08-04-llm-wiki-concept.md`, `raw/sources/2026-08-28-chatgpt-konten-vlog.md`

## Related

- [[index]]
- [[log]]
- [[sources/2026-04-04-llm-wiki]]
- [[sources/2026-08-04-llm-wiki-concept]]
- [[sources/2026-08-28-chatgpt-konten-vlog]]
- [[concepts/brainpedia]]
- [[concepts/content-bible]]
- [[conventions]]
