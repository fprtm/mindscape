---
title: Conventions
type: concept
status: active
sources: [2026-08-04-llm-wiki-concept, 2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [conventions, schema]
---

# Conventions

## Summary

Aturan penulisan wiki Brainpedia biar konsisten, Obsidian-friendly, dan Graph View bermakna. Ringkasan dari `AGENTS.md` + spec `2026-08-04-llm-wiki-concept`.

## Details

### Naming & lokasi

- `kebab-case` semua file: `wiki/concepts/spaced-repetition.md`, `wiki/entities/karpathy.md`
- Source summary mirror raw: `raw/sources/2026-04-04-llm-wiki.md` → `wiki/sources/2026-04-04-llm-wiki.md`
- Jangan bikin folder kompleks tanpa alasan. Folder yang ada: `wiki/{concepts,entities,sources,analyses,syntheses,questions,inbox}`, `raw/{sources,assets}`. `analyses/` dan `syntheses/` diperlakukan setara — `analyses/` untuk jawaban/query yang di-file balik, `syntheses/` untuk deep dive/lint.
- No duplicate stem: `eori` vs `eori-number` → pilih satu.

### Frontmatter (YAML wajib)

```yaml
---
title: Spaced Repetition
type: concept  # concept | entity | source | synthesis | question | overview
status: active # active | planned | stub | deprecated
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [learning, memory]
aliases: [SRS]
---
```

### Struktur halaman (deterministik)

1. `# Title`
2. `## Summary` — 2-3 kalimat TL;DR
3. `## Details` — isi utama dengan `[[wikilinks]]`
4. `## Sources` — list `[[wiki/sources/...]]` + path `raw/...`
5. `## Related` — outgoing links (orphan tanpa inbound = bug)

### Linking & Graph

- Pakai `[[wiki/concepts/foo]]` atau `[[foo]]` kalau unik. Selalu isi `## Related`.
- Tiap ingest harus update `## Related` di halaman yang tersentuh.

### Epistemik

- Lihat [[concepts/epistemic-rules]]: pisahkan fakta vs inference vs spekulasi vs opini, sitasi per klaim, flag kontradiksi eksplisit.

### Obsidian

- Markdown standar, `[[wikilinks]]`, heading konsisten, tags secukupnya.
- Attachment path `raw/assets/`, hotkey `Ctrl+Shift+D`.
- Graph View dioptimasi biar bermakna, bukan noise (colorGroups per path sudah di `.obsidian/graph.json`).

### Search & Git

- Awal: `wiki/index.md` + `scripts/search.py` (BM25 union). Jangan vector DB dulu.
- Evaluasi `qmd` kalau >100 sumber / >200 halaman.
- Git: repo sudah init, jangan destructive tanpa konfirmasi.

## Sources

- [[wiki/sources/2026-08-04-llm-wiki-concept]] — "schema/instructions", "Obsidian", "Search", "Git"
- [[wiki/sources/2026-04-04-llm-wiki]]
- `AGENTS.md` §2

## Related

- [[concepts/brainpedia]]
- [[concepts/epistemic-rules]]
- [[concepts/three-layer-architecture]]
- [[overview]]
- [[index]]
