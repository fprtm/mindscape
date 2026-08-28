# Task: Build My Personal LLM Wiki

Saya ingin membangun personal knowledge base menggunakan pola **LLM Wiki dari Andrej Karpathy**.

Gunakan dokumen LLM Wiki dari Karpathy sebagai **design reference utama**, bukan sebagai aplikasi yang harus di-install. Implementasikan konsep tersebut ke dalam Obsidian vault saya.

## Tujuan

Nama knowledge base saya adalah **Brainpedia**.

Brainpedia harus menjadi persistent, compounding knowledge base yang dikelola oleh LLM. Saya ingin LLM bertindak sebagai librarian/maintainer, sementara Obsidian menjadi interface untuk membaca dan mengeksplorasi knowledge base.

Saya tidak ingin sistem RAG sederhana yang setiap kali menjawab pertanyaan hanya melakukan retrieval dari dokumen mentah.

Saya ingin:

raw sources → LLM processing → persistent wiki → future queries

Knowledge yang sudah diproses harus terus diperkaya dan diperbarui ketika saya menambahkan sumber baru.

## Prinsip utama

Implementasikan tiga layer:

1. `raw/`
    
    - Berisi sumber asli.
    - Markdown, PDF, artikel, catatan, gambar, dan materi lainnya.
    - Immutable.
    - LLM boleh membaca tetapi tidak boleh mengubah sumber asli.
2. `wiki/`
    
    - Berisi knowledge yang sudah dikompilasi oleh LLM.
    - LLM bertanggung jawab membuat dan memperbarui halaman.
    - Harus memiliki cross-reference antar halaman.
    - Harus mendeteksi dan mencatat contradiction ketika sumber baru bertentangan dengan pengetahuan sebelumnya.
3. `schema/instructions`
    
    - Berisi aturan bagaimana LLM harus mengelola wiki.
    - Jelaskan struktur halaman, naming convention, linking convention, metadata, workflow ingest/query/lint, dan aturan maintenance.

## Struktur awal

Gunakan struktur yang masuk akal seperti:

Brainpedia/  
├── raw/  
│ └── assets/  
├── wiki/  
│ ├── index.md  
│ ├── overview.md  
│ ├── log.md  
│ ├── conventions.md  
│ ├── sources/  
│ ├── entities/  
│ ├── concepts/  
│ └── analyses/  
└── schema/

Jangan membuat struktur yang kompleks tanpa alasan. Jika menurutmu struktur yang lebih baik diperlukan, jelaskan alasannya terlebih dahulu.

## Workflow yang harus tersedia

### Ingest

Ketika saya mengatakan:

- "ingest this"
- "masukkan artikel ini"
- "pelajari sumber ini"
- atau instruksi serupa

LLM harus:

1. membaca sumber dari `raw/`
2. memahami isi sumber
3. membuat source summary
4. menentukan entities dan concepts yang relevan
5. mencari halaman wiki yang sudah ada
6. memperbarui halaman yang relevan
7. membuat halaman baru jika memang diperlukan
8. menambahkan wikilinks
9. memperbarui `index.md`
10. mencatat perubahan di `log.md`

Jangan membuat halaman baru hanya karena satu keyword muncul. Hindari duplikasi dan prioritaskan halaman yang memiliki nilai jangka panjang.

### Query

Ketika saya bertanya tentang sesuatu:

1. baca `wiki/index.md` terlebih dahulu
2. identifikasi halaman yang relevan
3. baca halaman-halaman tersebut
4. lakukan synthesis
5. gunakan source pages untuk melakukan verification bila diperlukan
6. jawab dengan citation/link ke halaman wiki yang digunakan

Jika jawaban atau analisis memiliki nilai jangka panjang, tawarkan untuk menyimpannya sebagai halaman baru di `wiki/analyses/`.

### Lint

Buat workflow untuk memeriksa:

- orphan pages
- broken wikilinks
- duplicate concepts
- missing cross-references
- stale information
- contradictory claims
- concepts penting yang belum memiliki halaman
- entities yang belum memiliki halaman
- halaman yang tidak memiliki source/reference yang jelas
- inkonsistensi metadata

## Aturan epistemik

Ini penting.

Jangan mencampurkan:

- fakta dari source
- inference LLM
- speculation
- opinion saya

Jika sebuah claim berasal dari source tertentu, pertahankan hubungan ke source tersebut.

Jika dua sumber bertentangan, jangan diam-diam memilih salah satunya. Catat contradiction dan jelaskan sumber mana yang mengatakan apa.

Jangan mengarang fakta hanya untuk membuat wiki terlihat lengkap.

## Obsidian

Knowledge base harus menggunakan Markdown standar yang kompatibel dengan Obsidian.

Gunakan:

- `[[wikilinks]]`
- YAML frontmatter jika memang berguna
- heading yang konsisten
- source references
- tags secukupnya

Optimalkan struktur supaya Obsidian Graph View menghasilkan hubungan yang bermakna, bukan sekadar graph yang penuh noise.

## Search

Untuk tahap awal, jangan menambahkan vector database atau RAG infrastructure jika belum diperlukan.

Gunakan `index.md` dan filesystem search terlebih dahulu.

Jika jumlah halaman sudah cukup besar dan pencarian mulai menjadi bottleneck, baru evaluasi penggunaan local search engine seperti `qmd`.

## Git

Jika memungkinkan, jadikan Brainpedia sebagai git repository sehingga semua perubahan wiki dapat dilacak.

Jangan melakukan destructive operation tanpa konfirmasi.

## Prinsip implementasi

Jangan hanya membuat folder kosong.

Bangun workflow yang benar-benar bisa saya gunakan.

Sebelum mengubah file penting:

1. inspect environment saya
2. jelaskan apa yang akan dibuat
3. pilih struktur yang sederhana
4. implementasikan
5. test workflow ingest/query/lint
6. berikan contoh penggunaan

Jika ada keputusan desain yang belum jelas, pilih default yang sederhana dan dokumentasikan keputusan tersebut di `schema/` atau `conventions.md`.

Gunakan LLM Wiki Karpathy sebagai inspirasi arsitektur, tetapi jangan mengklaim bahwa implementasi ini adalah implementasi resmi Karpathy.

Mulai dengan melakukan audit terhadap environment dan menentukan apa saja yang sudah tersedia. Setelah itu buat implementation plan sebelum melakukan perubahan.