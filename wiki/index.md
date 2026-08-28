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
| [[overview]] | overview | Brainpedia thesis + content bible vlog (Deadpan, 5 pilar, 4 formula) | 2026-04-04-llm-wiki, 2026-08-04-llm-wiki-concept, 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[conventions]] | concept | Aturan penulisan Brainpedia: naming, frontmatter, linking, epistemik, search, git | 2026-04-04-llm-wiki, 2026-08-04-llm-wiki-concept | 2026-08-28 |

## Sources

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| [[sources/2026-04-04-llm-wiki]] | source | Karpathy LLM Wiki pattern — persistent compounding wiki vs RAG | 2026-04-04-llm-wiki | 2026-08-28 |
| [[sources/2026-08-04-llm-wiki-concept]] | source | Brainpedia spec — tujuan, 3 lapis, 10-langkah ingest, aturan epistemik | 2026-08-04-llm-wiki-concept | 2026-08-28 |
| [[sources/2026-08-28-chatgpt-konten-vlog]] | source | Content bible vlog — Deadpan, 5 pilar, 4 formula, struktur 0-45d + random footage | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |

## Concepts

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| [[concepts/brainpedia]] | concept | Brainpedia: nama & tujuan vault ini — raw→LLM→wiki→query, LLM librarian | 2026-08-04-llm-wiki-concept, 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/content-bible]] | concept | Content bible v1.0 — identitas `Cerita kecil tentang keresahan hidup, ditertawakan secukupnya` | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/content-pillars]] | concept | 5 pilar: dewasa, uang/kerja, pertemanan, diri sendiri, hal receh yang dalam | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/tone-deadpan]] | concept | Tone Deadpan Self-Deprecating — natural, sinis, self-aware, dry humor | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/formula-konten]] | concept | 4 formula: Observation→Punchline, Complaint→Self-roast, Expectation→Reality, Serius→Bodoh | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/struktur-video]] | concept | Struktur 0-45d: Hook 0-3d → keresahan → perbesar → belokan → punchline | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/visual-random-footage]] | concept | Visual random footage 8d + VO observasional → vlog kehidupan bukan essay | 2026-08-28-chatgpt-konten-vlog | 2026-08-28 |
| [[concepts/persistent-wiki]] | concept | Wiki persisten & compounding: cross-ref & sintesis sudah siap sebelum ditanya | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/rag-vs-wiki]] | concept | RAG re-derive tiap query vs wiki compile-once, mahal di ingest murah di query | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/three-layer-architecture]] | concept | 3 lapis: raw immutable / wiki LLM-owned / schema (AGENTS.md) | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/epistemic-rules]] | concept | Aturan epistemik: pisah fakta/inference/spekulasi/opini, sitasi, flag contradiction | 2026-08-04-llm-wiki-concept | 2026-08-28 |
| [[concepts/obsidian-as-ide]] | concept | LLM programmer, Obsidian IDE, wiki codebase — Web Clipper, Graph, Dataview, Marp | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/ingest-operation]] | concept | Ingest: drop ke raw/sources/ → discuss → plan → generate 10-15 halaman → index+log | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/query-operation]] | concept | Query: index + BM25 union → top-k wiki → sintesis + sitasi → file balik ke questions/ | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/lint-operation]] | concept | Lint: cek kontradiksi, stale, orphan, stub, duplikat, copied-state drift | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/memex]] | concept | Memex Bush 1945 — private curated trails, LLM yang solve maintenance | 2026-04-04-llm-wiki | 2026-08-28 |
| [[concepts/index-vs-log]] | concept | index.md katalog isi vs log.md history kronologis parseable | 2026-04-04-llm-wiki | 2026-08-28 |

## Entities

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| [[entities/karpathy]] | entity | Andrej Karpathy — penulis gist llm-wiki 2026-04-04, pattern persistent wiki | 2026-04-04-llm-wiki | 2026-08-28 |
| [[entities/vannevar-bush]] | entity | Vannevar Bush — pencetus Memex 1945, spirit di balik LLM Wiki | 2026-04-04-llm-wiki | 2026-08-28 |

## Syntheses

| Page | Type | Summary | Sources | Updated |
|------|------|---------|---------|---------|
| *empty — will populate on synthesis/query filing* | | | | |

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
