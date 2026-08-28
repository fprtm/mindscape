---
title: Query Operation
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [workflow, query]
---

# Query Operation

## Summary

Query = tanya ke wiki, bukan ke raw. LLM baca `index.md` dulu, union dengan full-text search, baca top-k halaman wiki, sintesis plus sitasi, tawarkan format (markdown/tabel/Marp/chart), lalu tanya mau di-file balik ke `wiki/questions/` atau `wiki/syntheses/` biar compounding.

## Details

### Alur baku (AGENTS.md §3.2)

1. Baca `wiki/index.md` dulu (katalog 1 baris per halaman)
2. Full-text search (`scripts/search.py` atau `grep -r` atau `qmd search` kalau sudah >100 sumber) — ambil **union**, jangan cuma index. Index itu lossy, fakta terkubur di body (mis. angka fee spesifik) bisa kelewat kalau cuma index.
3. Baca top-k halaman wiki yang relevan (bukan raw langsung, kecuali wiki masih kosong)
4. Sintesis jawaban dengan sitasi `[[wiki/...]]`. Tawarkan format sesuai pertanyaan: markdown page, comparison table, slide deck Marp, matplotlib chart, canvas
5. Tanya: "File jawaban ini balik ke wiki?" → kalau ya, simpan ke `wiki/questions/<slug>.md` atau `wiki/syntheses/<slug>.md`, lalu update `wiki/index.md` + `wiki/log.md`

### Contoh format log

```
## [2026-08-28] query | "Bedanya wiki vs RAG?"
- Answer: wiki/questions/rag-vs-wiki.md
- Sources: wiki/concepts/rag.md, wiki/concepts/persistent-wiki.md
```

Insight penting: jawaban bagus yang hilang di chat history adalah kerugian. Makanya query yang compounding diubah jadi halaman wiki — sama berharganya dengan sumber ingest.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Operations: Query"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[ingest-operation]]
- [[lint-operation]]
- [[rag-vs-wiki]]
- [[index-vs-log]]
