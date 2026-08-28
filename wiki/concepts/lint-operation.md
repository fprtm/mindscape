---
title: Lint Operation
type: concept
status: active
sources: [2026-04-04-llm-wiki]
updated: 2026-08-28
tags: [workflow, lint, maintenance]
---

# Lint Operation

## Summary

Lint = health check periodik wiki. Cek kontradiksi, klaim basi, orphan, stub, konsep disebut tapi belum ada halaman, duplikat near-concept, missing cross-ref, copied-state drift, dan gap data. Output jadi `wiki/syntheses/lint-YYYY-MM-DD.md` + entry di `log.md`.

## Details

### Checklist (AGENTS.md §3.3)

- Kontradiksi antar halaman (klaim sama beda isi)
- Klaim basi yang sudah disupersede sumber lebih baru (cek `updated` vs tanggal sumber)
- Orphan — 0 inbound `[[links]]`, saranin `## Related`
- Stub — `status: stub` atau `planned` yang nggak pernah jadi
- Mentioned-but-missing — entitas disebut tapi belum ada halamannya
- Duplikat near-concept — `eori` vs `eori-number`
- Missing cross-ref, graph belum konek
- **Copied state drift** — nilai yang bergerak (SHA, count, tanggal) jangan dikutip literal; taro di frontmatter/repo dan baca live. Count tulis "these rules" bukan "these 5 rules". Literal di dalam code yang executable paling berbahaya (exit code 0 tapi ngitung salah)
- Gap data — saranin web search / sumber baru

### Cara jalanin

```
lint
# atau manual:
python scripts/lint.py
```

Di vault ini `scripts/lint.py` sudah ada — cek orphan, stub, broken link, near-duplicate stems. Untuk lint full (kontradiksi semantik), LLM baca isi halaman, bukan cuma struktur.

Hasil lint yang bagus tidak cuma ngeluh, tapi saranin pertanyaan baru untuk diselidiki dan sumber baru untuk dicari — biar wiki makin sehat seiring tumbuh.

## Sources

- [[wiki/sources/2026-04-04-llm-wiki]] — "Operations: Lint"
- `raw/sources/2026-04-04-llm-wiki.md`
- Komentar WadeGIMPBC tentang copied state drift di gist

## Related

- [[ingest-operation]]
- [[query-operation]]
- [[persistent-wiki]]
