---
title: Overview — Brainpedia
type: overview
status: active
sources: [2026-04-04-llm-wiki, 2026-08-04-llm-wiki-concept, 2026-08-28-chatgpt-konten-vlog, 2026-08-28-anatomy-of-a-problem-the-trial-1, 2026-08-28-cara-manfaatin-teknologi-biar-10x-lebih-produktif-darinol-jagat-review, 2026-08-28-step-by-step-mulai-bisnis-dari-nol-dig-deeper, 2026-08-28-dari-nol-belajar-hire-ai-assistant-william-jakfar, 2026-08-28-malu-di-depan-kamera-870-juta, 2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit]
updated: 2026-08-28
tags: [meta, wiki, brainpedia, content, bisnis, problem-solving, ai]
---

# Overview

## Summary

**Brainpedia** — vault `mindscape` ini adalah persistent compounding wiki berbasis pattern Karpathy. LLM jadi librarian/maintainer, Obsidian jadi IDE. Alur `raw sources → LLM processing → persistent wiki → future queries`, bukan RAG re-derive tiap query. Aturan epistemik [[concepts/epistemic-rules]] dijaga. Domain compounding: **content bible vlog** (Deadpan, 5 pilar, 4 formula) + **problem solving & bisnis** — definisi masalah sebagai gap tujuan, gadget sebagai aset produktif, framework mulai bisnis dari nol (resources→koneksi→opportunities→execution).

## Content

### Thesis / Working Synthesis

> Vault ini mengimplementasikan **persistent compounding wiki** (Karpathy 2026-04-04): daripada RAG yang re-derive tiap query, pengetahuan dikompilasi sekali ke `wiki/` dan dijaga tetap current via ingest/query/lint. Satu ingest menyentuh 10-15 halaman; cross-reference, kontradiksi, dan sintesis sudah siap sebelum ditanya. Spirit-nya adalah [[concepts/memex]] Bush (1945).
> 
> **Update 2026-08-28 #1**: domain pertama **content bible vlog kehidupan** (ChatGPT) — dari `humor terlalu dibuat jokes` → identitas `[[concepts/content-bible|Cerita kecil tentang keresahan hidup, ditertawakan secukupnya]]` dengan DNA `Keresahan → serius → belok → self-roast` (6 halaman baru).
> 
> **Update 2026-08-28 #2 — today batch 1**: 4 sumber (Malaka Trial, Jagat Review, Dig Deeper) menambah cluster **problem solving & bisnis** — [[concepts/definisi-masalah]] (gap tujuan), [[concepts/gadget-sebagai-aset-produktif]] (30-40% trap), [[concepts/framework-mulai-bisnis-dari-nol]] (resources→koneksi→opportunities→execution → Kota Tua Market 2015).
> 
> **Update 2026-08-28 #3 — today batch 2**: 3 sumber baru (Kuli Eps.78, Akademi Marketer, Giorrando) menambah **AI produktivitas & jualan tanpa branding** — [[concepts/hire-ai-assistant]] (1 jam hire AI dari chatbot → rekan kerja), [[concepts/jualan-tanpa-personal-branding]] (717jt via Meta Ads tanpa ngonten), plus nasehat ikan hias 110K subs sulit monetisasi karena audiens mismatch. Total wiki ~40 halaman.

### Architecture (from [[sources/2026-04-04-llm-wiki]])

- **Layer 1 — Raw (`raw/sources/`, `raw/assets/`)**: curated immutable sources. Web clips, PDFs, notes. Downloaded images via `Ctrl+Shift+D`. Never edited by the LLM.
- **Layer 2 — Wiki (`wiki/`)**: LLM-owned persistent artifact. `index.md` (content catalog), `log.md` (chronology), topic/entity pages, syntheses. Updated on every ingest/query/lint.
- **Layer 3 — Schema (`AGENTS.md` / `CLAUDE.md`)**: the contract that makes the LLM a disciplined maintainer — naming, frontmatter, page structure, ingest/query/lint workflows, pin handling.

### Key Ideas to Track

- [[concepts/brainpedia]] — Brainpedia itu sendiri (nama & tujuan vault ini)
- [[concepts/persistent-wiki]] — compounding artifact: compile once, keep current
- [[concepts/rag-vs-wiki]] — perbandingan RAG re-derive vs wiki persistent
- [[concepts/three-layer-architecture]] — raw / wiki / schema
- [[concepts/epistemic-rules]] — fakta vs inference vs spekulasi, flag contradiction
- [[conventions]] — naming, frontmatter, linking, Obsidian, search, git
- [[concepts/obsidian-as-ide]] — "LLM is programmer, Obsidian is IDE, wiki is codebase"
- [[concepts/index-vs-log]] — index (katalog) vs log (kronologi)
- [[concepts/ingest-operation]] / [[concepts/query-operation]] / [[concepts/lint-operation]] — tiga operasi utama
- [[concepts/memex]] — akar historis Bush 1945
- **Content cluster**: [[concepts/content-bible]] (identitas & DNA), [[concepts/content-pillars]] (5 pilar), [[concepts/tone-deadpan]] (Deadpan Self-Deprecating), [[concepts/formula-konten]] (4 formula), [[concepts/struktur-video]] (0-45d), [[concepts/visual-random-footage]] (random footage + VO)
- **Problem & Bisnis cluster (today)**: [[concepts/definisi-masalah]] (gap tujuan), [[concepts/gadget-sebagai-aset-produktif]] (30-40% → nice to have), [[concepts/framework-mulai-bisnis-dari-nol]] (resources→koneksi→opportunities→execution)
- **AI & Marketing cluster (today)**: [[concepts/hire-ai-assistant]] (1 jam hire AI), [[concepts/jualan-tanpa-personal-branding]] (717jt via Meta Ads), nasehat [[sources/2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit]] (110K subs ≠ bisnis)

### Graph Health

- Ingest #1 (2026-04-04-llm-wiki): 9 concepts + 2 entities + 1 source. Ingest #2 (2026-08-04-llm-wiki-concept): +1 source + 3 halaman. Ingest #3 (2026-08-28-chatgpt-konten-vlog): +1 source + 6 halaman content cluster. Ingest #4 today batch 1 (2026-08-28): +4 sources +3 concepts +3 entities. Ingest #5 today batch 2 (2026-08-28): +3 sources +2 concepts +3 entities. Total ~40 halaman wiki.
- Semua sudah cross-link via `## Related` dan terdaftar di `[[index]]`.
- Goal: zero orphans. Saat ini `python scripts/lint.py` orphan hanya `wiki/inbox/README.md` (staging, expected).

## Sources

- [[sources/2026-04-04-llm-wiki]] — Karpathy gist `442a6bf555914893e9891c11519de94f` (2026-04-04)
- [[sources/2026-08-04-llm-wiki-concept]] — Brainpedia spec (2026-08-04)
- [[sources/2026-08-28-chatgpt-konten-vlog]] — Content bible vlog (ChatGPT 2026-08-28)
- [[sources/2026-08-28-anatomy-of-a-problem-the-trial-1]] — Malaka Trial: definisi masalah (2026-02-13)
- [[sources/2026-08-28-cara-manfaatin-teknologi-biar-10x-lebih-produktif-darinol-jagat-review]] — Jagat Review x Theo (2026-07-23)
- [[sources/2026-08-28-step-by-step-mulai-bisnis-dari-nol-dig-deeper]] — Framework bisnis dari nol (2024-03-25)
- [[sources/2026-08-28-gua-kasih-solusi-kaya-tanpa-privilege]] — stub (transcript minim)
- [[sources/2026-08-28-dari-nol-belajar-hire-ai-assistant-william-jakfar]] — Kuli Eps.78: hire AI 1 jam (2026-08-21)
- [[sources/2026-08-28-malu-di-depan-kamera-870-juta]] — Akademi Marketer: 717jt tanpa branding (2026-04-18)
- [[sources/2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit]] — Giorrando: nasehat bisnis ikan hias (2026-08-24)
- `raw/sources/2026-04-04-llm-wiki.md`, `raw/sources/2026-08-04-llm-wiki-concept.md`, `raw/sources/2026-08-28-*.md` (10 total today)

## Related

- [[index]]
- [[log]]
- [[sources/2026-04-04-llm-wiki]]
- [[sources/2026-08-04-llm-wiki-concept]]
- [[sources/2026-08-28-chatgpt-konten-vlog]]
- [[sources/2026-08-28-anatomy-of-a-problem-the-trial-1]]
- [[sources/2026-08-28-cara-manfaatin-teknologi-biar-10x-lebih-produktif-darinol-jagat-review]]
- [[sources/2026-08-28-step-by-step-mulai-bisnis-dari-nol-dig-deeper]]
- [[sources/2026-08-28-dari-nol-belajar-hire-ai-assistant-william-jakfar]]
- [[sources/2026-08-28-malu-di-depan-kamera-870-juta]]
- [[sources/2026-08-28-11-tahun-nasehat-bisnis-dalam-45-menit]]
- [[concepts/brainpedia]]
- [[concepts/content-bible]]
- [[concepts/definisi-masalah]]
- [[concepts/hire-ai-assistant]]
- [[conventions]]
