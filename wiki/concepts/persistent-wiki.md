---
title: Persistent Wiki
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [wiki, knowledge-management, llm]
aliases: [compounding wiki]
---

# Persistent Wiki

## Summary

Wiki yang persisten dan compounding: bukan ngitung ulang jawaban tiap query, tapi mengkompilasi pengetahuan sekali lalu dijaga tetap current. Cross-reference, kontradiksi, dan sintesis sudah ada sebelum ditanya.

## Details

Inti dari [[rag-vs-wiki]] adalah perbedaan **re-derive vs compile-once**.

- **RAG biasa** (NotebookLM, ChatGPT file upload): tiap pertanyaan, LLM cari chunk, rangkai jawaban dari nol. Kalau pertanyaan butuh sintesis 5 dokumen, harus nemu dan jahit fragmen tiap kali. Tidak ada akumulasi.
- **Persistent wiki**: LLM baca sumber baru sekali, lalu **integrasi** ke wiki yang ada — update halaman entitas, revisi ringkasan topik, catat kontradiksi, perkuat atau tantang sintesis di [[overview]]. Pengetahuan dikompilasi sekali lalu *dijaga*.

Gist Karpathy menekankan: wiki ini **semakin kaya tiap sumber dan tiap query yang di-file balik**. Query yang bagus (perbandingan, analisis) tidak hilang di chat history, tapi disimpan ke `wiki/questions/` atau `wiki/syntheses/` — jadi ikut compounding.

Analogi: RAG = kalkulator yang ngitung ulang tiap kali. Persistent wiki = buku catatan yang nambah halaman dan ngebenerin halaman lama.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — bagian "The core idea" dan "Why this works"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[rag-vs-wiki]]
- [[three-layer-architecture]]
- [[memex]]
- [[overview]]
- [[index-vs-log]]
