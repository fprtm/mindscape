---
title: Epistemic Rules
type: concept
status: active
sources: [2026-08-04-llm-wiki-concept]
updated: 2026-08-28
tags: [epistemic, rules, provenance]
---

# Epistemic Rules

## Summary

Aturan epistemik Mindscape: jangan campur fakta dari source, inference LLM, spekulasi, dan opini user. Tiap klaim harus nyantol ke source, kontradiksi harus dicatat eksplisit, jangan ngarang biar wiki keliatan lengkap.

## Details

Diambil verbatim dari `raw/sources/2026-08-04-llm-wiki-concept.md` bagian "Aturan epistemik":

1. **Pisahkan provenans**: fakta source vs inference LLM vs spekulasi vs opini lu. Jangan dicampur dalam satu kalimat seolah setara.
2. **Sitasi per klaim**: kalau klaim dari source tertentu, pertahankan hubungan ke source tersebut (`Sources:` di tiap halaman + slug di frontmatter `sources: [...]`).
3. **Kontradiksi eksplisit**: kalau dua sumber bertentangan, jangan diam-diam pilih satu. Tulis `> [!WARNING] Contradicts [[halaman-lain]]: sumber A bilang X, sumber B bilang Y` dan jelaskan keduanya.
4. **Jangan ngarang**: jangan fabricate fakta biar wiki keliatan lengkap. Kalau belum ada source, tulis gap-nya.

Implementasi di vault:

- Frontmatter `sources: [slug]` wajib di tiap halaman wiki
- Bagian `## Sources` di tiap halaman list `[[wiki/sources/...]]` + path `raw/sources/...`
- Saat ingest, LLM harus cek halaman existing dulu sebelum bikin baru — hindari halaman hanya karena keyword muncul
- Lint harus flag halaman tanpa source/reference jelas

> Ini yang bikin Mindscape beda dari RAG: RAG cuma retrieve, Mindscape jaga provenance.

## Sources

- [[wiki/sources/2026-08-04-llm-wiki-concept]] — "Aturan epistemik"
- `raw/sources/2026-08-04-llm-wiki-concept.md`

## Related

- [[concepts/mindscape]]
- [[concepts/ingest-operation]]
- [[concepts/lint-operation]]
- [[conventions]]
