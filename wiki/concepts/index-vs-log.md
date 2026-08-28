---
title: Index vs Log
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [index, log, navigation]
---

# Index vs Log

## Summary

`index.md` itu content-oriented (katalog apa yang ada di wiki), `log.md` itu chronological (apa yang terjadi kapan). Dua-duanya bikin wiki bisa dinavigasi tanpa embedding/RAG.

## Details

### index.md — katalog isi

- Satu baris per halaman: `| Page | Type | Summary | Sources | Updated |`, dikelompokin per kategori (Overview, Sources, Concepts, Entities, Syntheses, Questions)
- LLM update tiap ingest. Saat query, LLM baca index dulu baru drill ke halaman. Di skala moderat (~100 sumber, ratusan halaman) ini surprisingly cukup — nggak perlu infra embedding.
- Plus Dataview block di bawah buat auto-generate tabel dari frontmatter kalau sudah banyak halaman.
- Team-scale lesson: index itu **lossy bottleneck** — summary 1 baris nggak bisa surface fakta terkubur di body (mis. angka fee spesifik). Fix: ambil **union** index + full-text BM25 (`scripts/search.py` atau `qmd`), jangan ganti index dengan search.

### log.md — history kronologis

- Append-only, prefix konsisten `## [YYYY-MM-DD] <op> | <title>` biar bisa `grep "^## \[" log.md | tail -5` kasih 5 entry terakhir.
- Kasih timeline evolusi wiki, bantu LLM ngerti apa yang baru dikerjain.
- Contoh entry ingest dan query ada di AGENTS.md §3.1 dan §3.2.

Keduanya ada di `wiki/` dan di-commit ke git — jadi version history gratis.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Indexing and logging"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[persistent-wiki]]
- [[query-operation]]
- [[three-layer-architecture]]
