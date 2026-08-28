---
title: RAG vs Wiki
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [rag, wiki, retrieval]
---

# RAG vs Wiki

## Summary

RAG re-derive jawaban tiap query dari chunk mentah; wiki mengkompilasi pengetahuan jadi wiki berstruktur yang sudah siap pakai. RAG murah di ingest, mahal di query. Wiki mahal di ingest (LLM nyentuh 10-15 halaman), murah dan akurat di query.

## Details

| Aspek | RAG | Wiki (Karpathy pattern) |
|-------|-----|--------------------------|
| **Waktu kerja** | Saat query: retrieve → generate | Saat ingest: compile → maintain |
| **Akumulasi** | Tidak ada. Tiap tanya mulai dari nol | Ada. Sintesis sudah terkompilasi |
| **Sintesis 5+ dokumen** | Harus nemu fragmen tiap kali, rawan miss | Sudah dirangkum di halaman konsep/sintesis |
| **Kontradiksi** | Ketahuan kalau kebetulan ke-retrieve bareng | Sudah di-flag `> [!WARNING] Contradicts ...` sejak ingest |
| **Cross-ref** | Implicit di vector space | Eksplisit `[[links]]` di markdown, terlihat di Graph View |
| **Biaya** | Query mahal kalau konteks panjang | Ingest mahal (nyentuh banyak halaman), query ringan (baca `index.md` + top-k) |

Shard penting dari gist: *"The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read."*

Di vault ini: RAG tidak dipakai sebagai default. Pencarian adalah `index.md` (katalog 1 baris per halaman) + `scripts/search.py` (BM25) dengan strategi **union** — biar recall tidak pernah lebih buruk dari index saja. `qmd` (https://github.com/tobi/qmd) baru dipasang kalau sudah >100 sumber / >200 halaman.

Kapan masih butuh RAG murni? Kalau sumber belum di-ingest sama sekali dan lu butuh jawab cepat tanpa mau ngerapihin wiki dulu. Tapi begitu jawaban itu bagus, file-kan balik ke `wiki/questions/` — biar compounding.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "The core idea", "Indexing and logging", "Optional: CLI tools"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[persistent-wiki]]
- [[three-layer-architecture]]
- [[index-vs-log]]
- [[query-operation]]
