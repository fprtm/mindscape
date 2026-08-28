---
title: Three-Layer Architecture
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [architecture, vault, schema]
---

# Three-Layer Architecture

## Summary

Vault dibagi 3 lapis: `raw/` (immutable source of truth, lu yang kurasi), `wiki/` (LLM-owned, terstruktur, interlinked), dan `AGENTS.md`/`CLAUDE.md` (schema yang bikin LLM disiplin, bukan chatbot ngarang).

## Details

### Lapis 1 — Raw (`raw/sources/`, `raw/assets/`)
- Isi: artikel, paper, gambar, PDF, catatan. Hasil Web Clipper masuk sini.
- Sifat: **immutable** — LLM cuma baca, nggak pernah edit. Kalau fakta cuma ada di chat history dan belum masuk `wiki/`, itu dianggap tidak ada.
- Penamaan: `YYYY-MM-DD-slug.md` (contoh `2026-04-04-llm-wiki.md`). Gambar di `raw/assets/` via `Ctrl+Shift+D`.

### Lapis 2 — Wiki (`wiki/`)
- Isi: ringkasan sumber (`wiki/sources/`), halaman konsep (`wiki/concepts/`), entitas (`wiki/entities/`), sintesis (`wiki/syntheses/`), pertanyaan yang di-file (`wiki/questions/`), inbox (`wiki/inbox/`), plus `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`.
- Sifat: **LLM owns entirely** — bikin, update, jaga cross-reference, jaga konsistensi. Lu baca di Obsidian; LLM yang nulis.
- Satu ingest bisa nyentuh 10-15 halaman wiki.

### Lapis 3 — Schema (`AGENTS.md` / `CLAUDE.md`)
- Isi: struktur folder, konvensi naming (`kebab-case`), frontmatter wajib, struktur header deterministik, workflow ingest/query/lint, aturan pin untuk koreksi human, aturan anti `audience: internal`.
- Sifat: co-evolve bareng lu. Tanpa schema, LLM jadi generic chatbot; dengan schema, jadi maintainer yang disiplin.

Hubungan: `raw/` → (via ingest) → `wiki/` → (via schema) → konsisten. `index.md` dan `log.md` adalah navigasi di atas `wiki/`.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Architecture"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[persistent-wiki]]
- [[obsidian-as-ide]]
- [[ingest-operation]]
- [[overview]]
