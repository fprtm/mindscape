---
title: Ingest Operation
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [workflow, ingest]
---

# Ingest Operation

## Summary

Ingest = lu drop sumber ke `raw/sources/` lalu bilang `ingest <path>`. LLM baca, diskusi takeaway, plan halaman target, generate ringkasan + update 10-15 halaman, lalu update `index.md` + `log.md` dan kasih diff.

## Details

### Alur baku (AGENTS.md §3.1)

1. **Read** — baca sumber full (teks dulu, baru gambar di `raw/assets/` terpisah)
2. **Discuss** — tanya lu mau emphasize apa
3. **Plan** — cek `wiki/index.md` dulu biar nggak duplikat `eori` vs `eori-number`. Untuk ingest paralel, reserve placeholder `status: planned` + `claimed_by` set via atomic conditional write *di luar* LLM call
4. **Generate** — `wiki/sources/<slug>.md` (ringkasan setia: klaim, evidence, gap) + 5-15 halaman di `concepts/`, `entities/`, `syntheses/`, `overview.md`. Tiap klaim harus sitasi slug sumber. Kontradiksi di-flag `> [!WARNING] Contradicts [[old-page]]: ...`
5. **Index** — update `wiki/index.md` (1 baris per halaman)
6. **Log** — append `wiki/log.md` dengan prefix `## [YYYY-MM-DD] ingest | ...` biar bisa `grep "^## \["`
7. **Show diff** — ringkas yang berubah, minta lu review di Obsidian

### Contoh perintah

```
ingest raw/sources/2026-04-04-llm-wiki.md
batch ingest raw/sources/
```

Satu sumber yang sama kalau di-ingest paralel tanpa placeholder pernah bikin 38% duplikat near-duplicate di tim yang coba pattern ini — makanya ada protokol `claimed_by` set (bukan scalar) biar kalau 1 ingest cancel, slot tetap hidup buat yang lain.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Operations: Ingest"
- `raw/sources/2026-04-04-llm-wiki.md`
- AGENTS.md §3.1

## Related

- [[query-operation]]
- [[lint-operation]]
- [[three-layer-architecture]]
- [[persistent-wiki]]
