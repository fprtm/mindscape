---
title: Mindscape
type: concept
status: active
sources: [2026-08-04-llm-wiki-concept, 2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [mindscape, overview]
aliases: [mindscape]
---

# Mindscape

## Summary

**Mindscape** adalah nama personal LLM wiki lu — implementasi pattern Karpathy di vault `mindscape`. Alurnya `raw sources → LLM processing → persistent wiki → future queries`, di mana LLM jadi librarian/maintainer dan Obsidian jadi interface baca/eksplorasi.

## Details

- **Bukan RAG sederhana**: tidak tiap query retrieval mentah dari `raw/`. Knowledge dikompilasi sekali ke `wiki/` lalu diperkaya tiap sumber baru.
- **3 lapis** (AGENTS.md): `raw/` immutable (lu kurasi), `wiki/` terstruktur interlinked (LLM yang kelola), `AGENTS.md`/`CLAUDE.md` + `[[conventions]]` sebagai schema.
- **Lokasi**: vault `mindscape/` ini adalah Mindscape itu sendiri (bukan folder terpisah `Mindscape/`). `raw/assets/`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md` adalah tulang punggungnya.
- **Workflow**: `ingest this` / `masukkan artikel ini` → 10 langkah ingest; query via `wiki/index.md` + union search; lint cek orphan/broken/duplicate/stale/contradiction; semua dicatat di `[[log]]`.
- **Aturan main**: lihat [[epistemic-rules]] — pisahkan fakta vs inference vs spekulasi vs opini, sitasi per klaim, jangan pilih diam-diam kalau sumber bertentangan (catat contradiction).

Mindscape didesain sederhana dulu: `index.md` + filesystem search, tanpa vector DB. Baru evaluasi `qmd` kalau sudah >100 sumber / >200 halaman. Git sudah init biar perubahan tertrack.

## Sources

- [[wiki/sources/2026-08-04-llm-wiki-concept]] — spec Mindscape (tujuan, nama, alur)
- [[wiki/sources/2026-04-04-llm-wiki]] — Karpathy gist sebagai design reference
- `raw/sources/2026-08-04-llm-wiki-concept.md`

## Related

- [[concepts/epistemic-rules]]
- [[concepts/three-layer-architecture]]
- [[concepts/persistent-wiki]]
- [[conventions]]
- [[overview]]
