---
title: Mindscape — Personal LLM Wiki Spec (2026-08-04)
type: source
status: active
sources: [2026-08-04-llm-wiki-concept]
updated: 2026-08-28
tags: [mindscape, spec, llm-wiki, requirements]
aliases: [mindscape-spec]
---

# Mindscape — Personal LLM Wiki Spec (2026-08-04)

## Summary

Spesifikasi user untuk **Mindscape**: personal persistent compounding wiki berbasis pattern Karpathy, di mana LLM jadi librarian/maintainer dan Obsidian jadi interface. Menolak RAG sederhana (retrieval mentah tiap query) — minta alur `raw sources → LLM processing → persistent wiki → future queries` dengan 3 lapis, workflow ingest/query/lint yang eksplisit, dan aturan epistemik ketat (jangan campur fakta vs inference).

## Details

### Tujuan — Mindscape

- Nama vault: **Mindscape**
- Sifat: persistent, compounding, dikelola LLM. LLM = librarian/maintainer, Obsidian = reader/explorer.
- Anti-pattern: RAG sederhana yang tiap jawab hanya retrieval dari dokumen mentah. Mau kompilasi yang terus diperkaya saat sumber baru masuk.

### Tiga Lapis (versi spec user, sedikit beda dari Karpathy gist)

1. `raw/` — sumber asli (markdown, PDF, artikel, catatan, gambar). Immutable. LLM boleh baca, tidak boleh ubah.
2. `wiki/` — knowledge terkompilasi LLM. LLM bikin & update, harus cross-reference, harus deteksi & catat contradiction.
3. `schema/instructions` — aturan kelola wiki: struktur halaman, naming, linking, metadata, workflow ingest/query/lint, maintenance. Di vault ini diimplementasikan sebagai `AGENTS.md` + `CLAUDE.md` di root (setara `schema/`) plus `wiki/conventions.md` untuk aturan halaman.

> [!NOTE] Mapping struktur
> Spec minta `wiki/conventions.md` dan `wiki/analyses/` (bukan `syntheses/`). Vault ini sebelumnya pakai `wiki/syntheses/` dari Karpathy. Keputusan: **pertahankan keduanya** — `syntheses/` tetap ada, `analyses/` ditambahkan sebagai alias untuk query filing yang bernilai jangka panjang. `conventions.md` dibuat sebagai ringkasan konvensi halaman. Tidak ada destruktif.

### Workflow Ingest (10 langkah eksplisit)

Trigger: "ingest this", "masukkan artikel ini", "pelajari sumber ini", dll. LLM harus:
1. baca sumber dari `raw/`
2. pahami isi
3. buat source summary
4. tentukan entities & concepts relevan
5. cari halaman wiki yang sudah ada
6. update halaman relevan
7. buat halaman baru jika perlu (jangan buat hanya karena keyword muncul — hindari duplikasi, prioritaskan nilai jangka panjang)
8. tambah wikilinks
9. update `index.md`
10. catat di `log.md`

### Workflow Query

1. baca `wiki/index.md` dulu
2. identifikasi halaman relevan
3. baca halaman tersebut
4. synthesis
5. verifikasi via source pages jika perlu
6. jawab dengan citation/link ke halaman wiki

Jika jawaban/analisis bernilai jangka panjang, tawarkan simpan sebagai halaman baru di `wiki/analyses/`.

### Workflow Lint

Periksa: orphan pages, broken wikilinks, duplicate concepts, missing cross-ref, stale info, contradictory claims, konsep penting belum punya halaman, entities belum punya halaman, halaman tanpa source/reference jelas, inkonsistensi metadata.

### Aturan Epistemik — Penting

- Jangan campur: fakta dari source vs inference LLM vs spekulasi vs opini user — harus dipisah.
- Klaim dari source tertentu harus pertahankan hubungan ke source tersebut.
- Jika dua sumber bertentangan, jangan diam-diam pilih satu. Catat contradiction, jelaskan sumber mana bilang apa.
- Jangan ngarang fakta biar wiki kelihatan lengkap.

### Obsidian

- Markdown standar kompatibel Obsidian: `[[wikilinks]]`, YAML frontmatter kalau berguna, heading konsisten, source references, tags secukupnya.
- Optimasi Graph View biar bermakna, bukan noise.

### Search & Git

- Awal: pakai `index.md` + filesystem search. Vector DB / RAG infra jangan dulu.
- Baru evaluasi `qmd` kalau halaman sudah besar dan search jadi bottleneck.
- Jadikan git repo biar perubahan tertrack. Jangan destructive operation tanpa konfirmasi.

### Prinsip Implementasi

Jangan cuma bikin folder kosong — bangun workflow yang beneran bisa dipakai. Inspect environment → jelaskan rencana → pilih struktur sederhana → implementasi → test ingest/query/lint → kasih contoh. Kalau desain belum jelas, pilih default sederhana dan dokumentasikan di `schema/` atau `conventions.md`. Pakai Karpathy sebagai inspirasi arsitektur, tapi jangan klaim ini implementasi resmi Karpathy.

## Sources

- `raw/sources/2026-08-04-llm-wiki-concept.md` (local, immutable)
- [[wiki/sources/2026-04-04-llm-wiki]] — Karpathy gist sebagai design reference

## Related

- [[concepts/mindscape]]
- [[concepts/epistemic-rules]]
- [[concepts/ingest-operation]]
- [[concepts/query-operation]]
- [[concepts/lint-operation]]
- [[conventions]]
- [[overview]]
