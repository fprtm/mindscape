---
title: Wiki Log
type: log
status: active
updated: 2026-08-28
---

# Wiki Log

> Chronological, append-only. Prefix every entry `## [YYYY-MM-DD] <op> | <title>` for `grep "^## \["` parsing.

## [2026-08-28] setup | Initialize LLM Wiki vault

- Operation: setup
- Raw: `raw/sources/2026-04-04-llm-wiki.md` (Karpathy gist fetched and saved)
- Created: `AGENTS.md`, `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`, directory structure `raw/{sources,assets}`, `wiki/{concepts,entities,sources,syntheses,questions,inbox}`, `scripts/`
- Config: `.obsidian/app.json` attachment path → `raw/assets`, graph settings, helper scripts `scripts/search.py` + `scripts/lint.py`
- Notes: Vault initialized as 3-layer system (raw immutable / wiki LLM-owned / schema). Ready for first ingest. Next: `ingest raw/sources/2026-04-04-llm-wiki.md` or drop new source.

## [2026-08-28] ingest | raw/sources/* — batch ingest 2026-04-04-llm-wiki

- Raw: `raw/sources/2026-04-04-llm-wiki.md` (Karpathy gist 442a6bf555914893e9891c11519de94f)
- Created: `wiki/concepts/persistent-wiki.md`, `wiki/concepts/rag-vs-wiki.md`, `wiki/concepts/three-layer-architecture.md`, `wiki/concepts/obsidian-as-ide.md`, `wiki/concepts/ingest-operation.md`, `wiki/concepts/query-operation.md`, `wiki/concepts/lint-operation.md`, `wiki/concepts/memex.md`, `wiki/concepts/index-vs-log.md`, `wiki/entities/karpathy.md`, `wiki/entities/vannevar-bush.md`
- Updated: `wiki/overview.md` (thesis + key ideas), `wiki/index.md` (11 new rows), `wiki/sources/2026-04-04-llm-wiki.md` (already existed)
- Notes: Batch ingest requested as `ingest overall in raw/sources/*` (first pass). 1 source present, expanded to 9 concepts + 2 entities per AGENTS.md §3.1 (5-15 pages).

## [2026-08-28] ingest | raw/sources/2026-08-04-llm-wiki-concept.md — Brainpedia spec

- Raw: `raw/sources/2026-08-04-llm-wiki-concept.md` (Brainpedia task spec, 180 lines)
- Created: `wiki/sources/2026-08-04-llm-wiki-concept.md`, `wiki/concepts/brainpedia.md`, `wiki/concepts/epistemic-rules.md`, `wiki/conventions.md`, `wiki/analyses/` (folder, alias for syntheses)
- Updated: `wiki/overview.md` (rename to Brainpedia, thesis + epistemic link), `wiki/index.md` (+3 concepts +1 conventions +1 source), `wiki/sources/2026-04-04-llm-wiki.md` untouched
- Notes: Second source in batch `raw/sources/*`. Diterapkan mapping spec: `schema/` → `AGENTS.md`/`CLAUDE.md` + `conventions.md`, `wiki/analyses/` ditambah tanpa hapus `syntheses/`. Aturan epistemik dipisah jadi halaman tersendiri. Tidak ada destructive operation.

## [2026-08-28] ingest | raw/sources/2026-08-28-chatgpt-konten-vlog.md — Content Bible Vlog

- Raw: `raw/sources/2026-08-28-chatgpt-konten-vlog.md` (825 lines, ChatGPT c/6a911da..., via Web Clipper fallback manual)
- Created: `wiki/sources/2026-08-28-chatgpt-konten-vlog.md`, `wiki/concepts/content-bible.md`, `wiki/concepts/content-pillars.md`, `wiki/concepts/tone-deadpan.md`, `wiki/concepts/formula-konten.md`, `wiki/concepts/struktur-video.md`, `wiki/concepts/visual-random-footage.md`
- Updated: `wiki/overview.md` (thesis + content cluster 6 halaman, sources), `wiki/index.md` (+1 source +6 concepts, total 22 halaman)
- Notes: Ingest #3 triggered by `ingest again` after raw/sources/* now has 3 files. Previous watcher confusion (vault name mindscape vs mindspace) resolved. Content cluster jadi domain pertama yang compounding di Brainpedia. Next: lint + git commit.

## [2026-08-28] ingest | today batch 2026-08-28 — Malaka + Jagat Review + Dig Deeper

- Raw: `raw/sources/2026-08-28-anatomy-of-a-problem--the-trial 1.md` (91K, 1019 lines, Malaka), `raw/sources/2026-08-28-cara-manfaatin-teknologi-biar-10x-lebih-produktif-darinol-jagat-review.md` (58K, 1201 lines, Theo x Jagat), `raw/sources/2026-08-28-step-by-step-mulai-bisnis-dari-nol--dig-deeper.md` (14K, 94 lines, Theo), `raw/sources/2026-08-28-gua-kasih-solusi-kaya-tanpa-privilege‼️tanpa-nipu,-tanpa-koin😂--the-host---theo-derick.md` (739 bytes, stub 16 lines)
- Created: `wiki/sources/2026-08-28-anatomy-of-a-problem-the-trial-1.md`, `wiki/sources/2026-08-28-cara-manfaatin-teknologi-biar-10x-lebih-produktif-darinol-jagat-review.md`, `wiki/sources/2026-08-28-step-by-step-mulai-bisnis-dari-nol-dig-deeper.md`, `wiki/sources/2026-08-28-gua-kasih-solusi-kaya-tanpa-privilege.md` (stub), `wiki/concepts/definisi-masalah.md`, `wiki/concepts/gadget-sebagai-aset-produktif.md`, `wiki/concepts/framework-mulai-bisnis-dari-nol.md`, `wiki/entities/theo-derick.md`, `wiki/entities/malaka-project.md`, `wiki/entities/jagat-review.md`
- Updated: `wiki/overview.md` (thesis + problem/bisnis cluster), `wiki/index.md` (+4 sources +3 concepts +3 entities, total ~32 halaman)
- Notes: Trigger `ingest today` — 3 empty files from failed clip earlier auto-removed/replaced by 4 new clips after vault fix (mindscape s-c-a-p-e). Empty 0-byte files were skipped by watcher (wait_stable). Batch today = 4 raw, 1 stub flagged. Next: git push via post-commit hook.

## [2026-08-28] ingest | today batch 2026-08-28 — continued (Kuli + Akademi + Giorrando)

- Raw: `raw/sources/2026-08-28-dari-nol-belajar-hire-ai-assistant-cuma-1-jam-william-jakfar-kuli-eps.78.md` (49K, 1000 lines), `raw/sources/2026-08-28-malu-di-depan-kamera-pake-cara-ini-buat-hasilkan-870-juta.md` (52K, 1052 lines), `raw/sources/2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit.md` (49K, 1110 lines) — semua muncul setelah `ingest again` karena clip baru berhasil setelah vault fix
- Created: `wiki/sources/2026-08-28-dari-nol-belajar-hire-ai-assistant-william-jakfar.md`, `wiki/sources/2026-08-28-malu-di-depan-kamera-870-juta.md`, `wiki/sources/2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit.md`, `wiki/concepts/hire-ai-assistant.md`, `wiki/concepts/jualan-tanpa-personal-branding.md`, `wiki/entities/william-jakfar.md`, `wiki/entities/akademi-marketer.md`, `wiki/entities/giorrando.md`
- Updated: `wiki/overview.md` (thesis + AI & marketing cluster), `wiki/index.md` (+3 sources +2 concepts +3 entities, total ~40 halaman)
- Notes: Trigger second `ingest again` — watcher `queue` sempat bikin `wiki/inbox/` stubs untuk 2 file baru, di-clean ke `wiki/sources/` full. Slug mismatch ` 1.md` vs `-1.md` dan `--` vs `-` dibersihin.

## [2026-08-28] ingest | ingest lagi batch 2026-08-28 — Marketing & Bisnis

- Raw: `raw/sources/2026-08-28-15-menit-auto-paham-marketing-&-branding.md` (141 lines, Malaka/Pandji), `raw/sources/2026-08-28-engineering-thinking-untuk-menyelesaikan-masalah--the-trial.md` (671 lines, Sabda PS), `raw/sources/2026-08-28-belajar-hutang-ala-orang-kaya.md` (412 lines, Raymond Chin), `raw/sources/2026-08-28-branding-lo-jelek,-bisnis-lo-susah-sukses!-darinol-ft-stephanie-regina.md` (922 lines, Haloka), `raw/sources/2026-08-28-cara-riset-market---belajar-bisnis-online-untuk-pemula.md` (86 lines, Denny Santoso), `raw/sources/2026-08-28-cara-saya-memperoleh-keuntungan-besar-di-anomali-bursa-saham-indonesia.md` (133 lines, Ferry Irwandi), `raw/sources/2026-08-28-materi-strategi-digital-marketing-dari-harvard-business-school.md` (126 lines, Ferry Irwandi Harvard), `raw/sources/2026-08-28-trik-marketing-yang-semua-orang-wajib-tau-(gw-sendiri-pake).md` (256 lines, Raymond Chin), `raw/sources/2026-08-28-kuliah-publik-inovasi-&-produktivitas--universitas-trisakti.md` (1089 lines, Ferry Irwandi Trisakti)
- Created: `wiki/sources/2026-08-28-15-menit-auto-paham-marketing-branding.md`, `wiki/sources/2026-08-28-belajar-hutang-ala-orang-kaya.md`, `wiki/sources/2026-08-28-branding-lo-jelek-bisnis-lo-susah-sukses.md`, `wiki/sources/2026-08-28-cara-riset-market-belajar-bisnis-online.md`, `wiki/sources/2026-08-28-cara-saya-memperoleh-keuntungan-besar-di-anomali-bursa-saham-indonesia.md`, `wiki/sources/2026-08-28-engineering-thinking-untuk-menyelesaikan-masalah-the-trial.md`, `wiki/sources/2026-08-28-materi-strategi-digital-marketing-harvard.md`, `wiki/sources/2026-08-28-trik-marketing-yang-semua-orang-wajib-tau.md`, `wiki/sources/2026-08-28-kuliah-publik-inovasi-produktivitas-trisakti.md`, `wiki/concepts/marketing-vs-branding.md`, `wiki/concepts/klinik-branding.md`, `wiki/concepts/strategi-digital-marketing.md`, `wiki/concepts/marketing-funnel.md`, `wiki/concepts/hutang-sebagai-leverage.md`, `wiki/concepts/riset-market.md`, `wiki/concepts/anomali-bursa.md`, `wiki/entities/raymond-chin.md`
- Updated: `wiki/overview.md` (thesis + marketing cluster 7 concepts), `wiki/index.md` (+9 sources +7 concepts +1 entity, total ~53 halaman, 18 sources)
- Notes: Trigger `ingest lagi` — 9 new raw detected (raw 19 vs wiki 10), watcher queue 11 (incl dup slugs) cleaned. Batch 9 processed incremental, no re-read of 10 existing.

## [2026-08-28] ingest | ingest again — 2026-08-28-kenapa-berpikir-saja-tidak-cukup

- Raw: `raw/sources/2026-08-28-kenapa-berpikir-saja-tidak-cukup.md` (313 lines, Prof Iwan Pranoto, 2026-04-30) — muncul setelah batch sebelumnya, diff raw 20 vs wiki 19
- Created: `wiki/sources/2026-08-28-kenapa-berpikir-saja-tidak-cukup.md`, `wiki/concepts/berpikir-vs-bernalar.md`
- Updated: `wiki/overview.md` (thesis + logika cluster), `wiki/index.md` (+1 source +1 concept, total ~55 halaman, 20 sources)
- Notes: Trigger `ingest again` — hanya 1 baru, incremental check via `comm` (raw 20 vs wiki 19) jadi tidak boros token. Watcher queue sempat bikin 13 inbox dup karena slug `&` dan ` 1.md`, dibersihin.

## [2026-08-28] ingest | ingest batch 2026-08-28 — 6 baru (Fajrul + Creativera + Tina + Cuanomix + Malaka)

- Raw: `raw/sources/2026-08-28-aku-membuat-ai-dari-nol..md` (120 lines, Fajrul Fx), `raw/sources/2026-08-28-bisnis-itu-sulit-sebelum-tau-konsep-ini---insights-083-(ft.-augie-&-hansel).md` (487 lines, Creativera), `raw/sources/2026-08-28-cara-bikin-sistem-bisnis-biar-jalan-tanpa-lo---monologue-017-(ft.-augie-aditya).md` (117 lines, Creativera), `raw/sources/2026-08-28-how-to-learn-to-code-in-2026.md` (191 lines, Tina Huang), `raw/sources/2026-08-28-survival-mode-2026-bikin-diri-&-bisnis-tetap-laku-di-tengah-ekonomi-yang-tak-pasti--cuanomix.md` (989 lines, Malaka Cuanomix), `raw/sources/2026-08-28-training-cara-bikin-konten-viral-ke-30-orang-tim-saya.md` (430 lines, Malaka)
- Created: `wiki/sources/2026-08-28-aku-membuat-ai-dari-nol.md`, `wiki/sources/2026-08-28-bisnis-itu-sulit-sebelum-tau-konsep-ini.md`, `wiki/sources/2026-08-28-cara-bikin-sistem-bisnis-biar-jalan-tanpa-lo.md`, `wiki/sources/2026-08-28-how-to-learn-to-code-in-2026.md`, `wiki/sources/2026-08-28-survival-mode-2026-cuanomix.md`, `wiki/sources/2026-08-28-training-cara-bikin-konten-viral.md`, `wiki/concepts/ai-dari-nol.md`, `wiki/concepts/survival-mode-2026.md`, `wiki/concepts/sistem-bisnis-tanpa-owner.md`
- Updated: `wiki/overview.md` (thesis + survival & AI cluster), `wiki/index.md` (+6 sources +3 concepts, total ~64 halaman, 26 sources, raw 26 == wiki 26 sinkron)
- Notes: Trigger `ingest` — 6 baru terdeteksi via `comm` (raw 26 vs wiki 20), watcher queue 13 dup slug dibersihin, incremental terbukti untuk 100.

---

## [2026-08-28] ingest | ingest — 2026-08-28-bisnis-dengan-kondisi-dan-modal-ekstream

- Raw: `raw/sources/2026-08-28-bisnis-dengan-kondisi-dan-modal-ekstream.md` (4583 lines, ChatGPT, roadmap 500×)
- Created: `wiki/sources/2026-08-28-bisnis-dengan-kondisi-dan-modal-ekstream.md`, `wiki/concepts/roadmap-modal-ekstrem.md`
- Updated: `wiki/overview.md`, `wiki/index.md` (+1 source +1 concept, total ~74 halaman, 27 sources, raw 27 == wiki 27)
- Notes: Trigger `ingest lagi` — 1 baru terdeteksi (raw 27 vs wiki 26), incremental, watcher queue dup cleaned.

---

## [2026-08-28] ingest | ingest lagi — FPRTM Atlas

- Raw: `raw/sources/2026-08-28-fprtmatlas-blueprints.md` (57 lines), `raw/sources/2026-08-28-fprtmatlas-domain-knowledge-kamus-referensi-dunia-nyata-untuk-programmer,-product-builder,-dan-pebisnis.md` (4330 lines, v1.0)
- Created: `wiki/sources/2026-08-28-fprtm-atlas-blueprints.md`, `wiki/sources/2026-08-28-fprtm-atlas-domain-knowledge.md`, `wiki/concepts/atlas-blueprints.md`, `wiki/concepts/atlas-domain-knowledge.md`
- Updated: `wiki/index.md` (+2 sources +2 concepts, total ~77 halaman, 29 sources, raw 29 == wiki 29), `wiki/overview.md`
- Notes: Trigger `ingest lagi` — 2 baru terdeteksi (raw 29 vs wiki 27), watcher queue 18 dup cleaned, incremental.

---

## [2026-08-29] ingest | ingest — 2026-08-29-guides-pwas

- Raw: `raw/sources/2026-08-29-guides-pwas.md` (446 lines, Vercel Next.js PWA)
- Created: `wiki/sources/2026-08-29-guides-pwas.md`, `wiki/concepts/pwa-nextjs.md`
- Updated: `wiki/index.md` (+1 source +1 concept, total ~75 halaman, 30 sources, raw 30 == wiki 30), `wiki/overview.md`
- Notes: Trigger `ingest` — 1 baru terdeteksi (raw 30 vs wiki 29), incremental, watcher queue dup cleaned.

---
