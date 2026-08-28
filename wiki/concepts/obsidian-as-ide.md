---
title: Obsidian as IDE
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [obsidian, workflow, tooling]
---

# Obsidian as IDE

## Summary

"LLM adalah programmer, Obsidian adalah IDE, wiki adalah codebase." Lu buka LLM di satu sisi, Obsidian di sisi lain — LLM ngedit, lu browsing hasilnya real-time via Graph View dan links.

## Details

Praktik yang disarankan Karpathy dan yang sudah di-setup di vault ini:

- **Web Clipper** → `raw/sources/` (1 klik artikel jadi markdown)
- **Attachment path** `raw/assets/` + hotkey `Ctrl+Shift+D` (Download attachments for current file) — biar gambar lokal, URL nggak putus. LLM baca teks dulu, lalu lihat gambar terpisah kalau perlu.
- **Graph View** → lihat hub, orphan, cluster. Orphan (0 inbound link) adalah bug — harus ada `## Related`.
- **Dataview** → query frontmatter (`type`, `status`, `updated`, `tags`) jadi tabel dinamis. Frontmatter di vault ini sudah konsisten.
- **Marp** → `--- marp: true ---` di `wiki/syntheses/` buat deck slide dari konten wiki.
- **Git** → vault ini sudah `git init` (`8ed6c3d`). Version history, branching, kolaborasi gratis.

Workflow harian: lu kurasi sumber & nanya pertanyaan bagus (kerjaan manusia). LLM kerjain bookkeeping membosankan: update cross-reference, jaga ringkasan tetap current, catat kontradiksi, jaga 15 file tetap konsisten sekaligus (kerjaan LLM).

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "The core idea" (praktik LLM + Obsidian), "Tips and tricks"
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[three-layer-architecture]]
- [[persistent-wiki]]
- [[index-vs-log]]
