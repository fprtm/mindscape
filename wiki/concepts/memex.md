---
title: Memex
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [history, memex, bush]
---

# Memex

## Summary

Memex (Vannevar Bush, 1945) adalah visi toko pengetahuan pribadi dengan associative trails antar dokumen — privat, terkurasi, koneksi antar dokumen sama berharganya dengan dokumen itu sendiri. LLM Wiki adalah Memex yang akhirnya bisa jalan karena LLM yang ngerjain maintenance.

## Details

Karpathy nutup gist dengan referensi Bush:

- **Memex** = meja personal yang nyimpen koleksi dokumen terkurasi + trail asosiatif antar dokumen. Lebih dekat ke wiki privat yang aktif dikurasi, bukan web yang kita kenal sekarang.
- Masalah Bush yang nggak kesolve di 1945: **siapa yang ngerjain maintenance?** Bikin cross-reference, jaga ringkasan tetap current, catat kontradiksi — manusia nyerah karena beban maintenance naik lebih cepat dari value.
- **LLM Wiki jawab itu**: LLM nggak bosen, nggak lupa update cross-ref, bisa nyentuh 15 file dalam satu pass, biaya maintenance mendekati nol. Manusia tugasnya kurasi sumber, arahkan analisis, tanya pertanyaan bagus; LLM kerjain sisanya.

Implikasi: kalau lu ngerasa wiki ini "mahal di ingest" (LLM lama nyentuh banyak halaman), itu memang by design — bayar di ingest biar query murah dan graph sudah jadi.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Why this works"
- `raw/sources/2026-04-04-llm-wiki.md`
- Bush, Vannevar (1945) — "As We May Think" (implisit di gist)

## Related

- [[persistent-wiki]]
- [[three-layer-architecture]]
- [[entities/vannevar-bush]]
