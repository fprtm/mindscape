---
title: Andrej Karpathy
type: entity
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [person, ai]
aliases: [karpathy]
---

# Andrej Karpathy

## Summary

Peneliti/engineer AI (ex-Tesla, OpenAI) yang menulis gist `llm-wiki.md` (2026-04-04) — pattern LLM Wiki: persistent compounding wiki sebagai alternatif RAG, dengan metafora "LLM is programmer, Obsidian is IDE, wiki is codebase."

## Details

Peran di vault ini:

- Penulis sumber `2026-04-04-llm-wiki.md` yang jadi fondasi `[[wiki/sources/2026-04-04-llm-wiki]]`
- Pengusul 3-layer architecture (`raw/` immutable, `wiki/` LLM-owned, `AGENTS.md` schema) dan operasi ingest/query/lint
- Preferensi workflow: ingest satu-per-satu dengan human in the loop, tapi batch juga didukung

Konteks tambahan dari gist: gist ini sengaja abstract — cuma ngasih pattern, implementasi spesifik diserahkan ke LLM + human buat co-evolve sesuai domain. Komentar-komentar di gist yang nambahin team-scale lessons (concurrent ingest, visibility labels, union search, pins) juga diadopsi di `AGENTS.md`.

Link: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]]
- `raw/sources/2026-04-04-llm-wiki.md`

## Related

- [[concepts/persistent-wiki]]
- [[concepts/three-layer-architecture]]
- [[entities/vannevar-bush]]
