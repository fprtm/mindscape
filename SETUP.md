# Mindscape — SETUP (agnostic bootstrap)

> Tutorial untuk nge-bootstrap Mindscape di **laptop baru** atau re-install. Agnostic: work untuk **OpenCode / Claude Code / Codex / Pi** — semua baca `AGENTS.md` yang sama.

Vault ini (`mindscape`) adalah implementasi **LLM Wiki pattern Karpathy (2026-04-04)** — persistent compounding wiki, bukan RAG re-derive tiap query. Alur `raw/sources → LLM processing → wiki → future queries`.

---

## 1. Prereq (sekali di laptop baru)

```bash
# wajib
sudo apt install git gh python3 python3-pip -y  # atau brew install ...
gh auth login                    # login github (ssh + repo scope)
git config --global user.name "Nama Lu"
git config --global user.email "email@example.com"

# obsidian
# download dari https://obsidian.md → open vault: /path/to/mindscape

# optional tapi direkomendasi
pip install watchdog            # buat scripts/watch.py mode watchdog (fallback polling tanpa ini juga jalan)
pip install qmd 2>/dev/null || echo "skip qmd sampai wiki >100 sumber"
```

## 2. Clone vault (laptop baru)

```bash
# ganti fprtm dengan username github lu kalau beda
gh repo clone fprtm/mindscape ~/projects/personal/mindscape
# atau via https:
git clone https://github.com/fprtm/mindscape.git ~/projects/personal/mindscape
cd ~/projects/personal/mindscape
git log --oneline -3   # cek commit terakhir
ls raw/sources/ wiki/  # pastikan ada
```

Kalau repo belum ada di GitHub (fresh laptop pertama kali):
```bash
cd /path/to/mindscape
gh repo create mindscape --public --source=. --remote=origin --push
# atau private: gh repo create mindscape --private --source=. --remote=origin --push
git branch -M main && git push -u origin main
```

## 3. Global pointer — biar start session dari manapun tetap ngeuh

Agent apapun cuma baca `AGENTS.md` di cwd. Biar agnostic, bikin pointer global di 4 tempat (sekali jalan, copy-paste aja):

```bash
# Claude Code
mkdir -p ~/.claude
cat >> ~/.claude/CLAUDE.md << 'MD'

---
# Mindscape — Global Pointer (agnostic, mindscape)
Vault utama: `/home/dsg-ferry/projects/personal/mindscape` (Mindscape).
Kalau user bilang ingest/query/lint/mindscape/mindscape — baca `/home/dsg-ferry/projects/personal/mindscape/AGENTS.md` dulu (bukan di cwd).
MD

# Codex
mkdir -p ~/.codex
cat > ~/.codex/AGENTS.md << 'MD'
# Mindscape — Global Pointer (agnostic, mindscape)
Vault utama: `/home/dsg-ferry/projects/personal/mindscape`.
Jika user menyebut ingest/query/lint/mindscape/mindscape — baca `/home/dsg-ferry/projects/personal/mindscape/AGENTS.md` dulu.
MD

# OpenCode
mkdir -p ~/.config/opencode
cat > ~/.config/opencode/AGENTS.md << 'MD'
# Mindscape — Global Pointer (agnostic, mindscape)
Vault utama: `/home/dsg-ferry/projects/personal/mindscape` (Mindscape).
Instruksi untuk OpenCode: jika user bilang ingest/query/lint/mindscape/mindscape, baca `/home/dsg-ferry/projects/personal/mindscape/AGENTS.md` dulu.
MD

# Pi / generic (walk-up dari ~)
cat > ~/AGENTS.md << 'MD'
# Global AGENTS — pointer to Mindscape
Vault: `/home/dsg-ferry/projects/personal/mindscape`. See that AGENTS.md for ingest/query/lint.
MD
```

## 4. Shell alias — biar nggak perlu inget path

```bash
cat >> ~/.zshrc << 'SH'

# Mindscape — agnostic shortcuts
alias brain='cd /home/dsg-ferry/projects/personal/mindscape && opencode'
alias mindscape='cd /home/dsg-ferry/projects/personal/mindscape'
alias brain-claude='cd /home/dsg-ferry/projects/personal/mindscape && claude'
alias brain-codex='cd /home/dsg-ferry/projects/personal/mindscape && codex'
brain-ingest() { cp "$1" /home/dsg-ferry/projects/personal/mindscape/raw/sources/ && echo "→ copied to raw/sources/$(basename $1)"; }
SH
source ~/.zshrc
# pakai:
# brain              → buka opencode di vault
# mindscape          → cd aja
# brain-ingest ~/Downloads/artikel.pdf
```

> Ganti `/home/dsg-ferry/projects/personal/mindscape` dengan path vault di laptop baru lu.

## 5. Obsidian — setting 2 menit (sekali per vault)

1. Open vault → pilih folder `mindscape`
2. Settings → Files and links → Attachment folder path = `raw/assets`
3. Settings → Hotkeys → cari `Download attachments for current file` → bind `Ctrl+Shift+D`
4. Install plugin (optional): Dataview, Marp
5. Buka Graph View → cek warna per `wiki/sources|concepts|entities|syntheses` sudah ada di `.obsidian/graph.json`

Web Clipper:
- Extension → Settings → Vault = `mindscape` (exact, case-sensitive, `scape` bukan `space`)
- File location = `raw/sources/`
- File name = `{{date}}-{{title}}`
- Kalau error `Vault not found` → pastikan Obsidian lagi kebuka + vault name bener + `xdg-mime default md.obsidian.Obsidian.desktop x-scheme-handler/obsidian`

## 6. Git remote & auto push tiap ingest

Vault ini sudah git repo. Setiap ingest **harus** commit + push biar sinkron ke GitHub:

```bash
cd ~/projects/personal/mindscape
git remote -v                    # cek
# kalau belum ada remote:
gh repo create mindscape --public --source=. --remote=origin --push
# atau manual:
git remote add origin git@github.com:fprtm/mindscape.git
git branch -M main
git push -u origin main

# auto push tiap ingest — watcher & manual ingest sudah di-setup untuk push:
git config alias.ingest '!git add -A && git commit -m "ingest: $(date +%F) — $*" && git push'
# pakai: git ingest "content bible vlog"
```

Watcher `scripts/watch.py` **nggak auto push** by default (biar aman). Kalau mau watcher auto push, jalanin:
```bash
python scripts/watch.py --mode queue --push   # TODO: flag push ada di versi berikutnya
# sementara: manual push setelah ingest:
# git add . && git commit -m "ingest: ..." && git push
```

Hook otomatis (opsional, bikin push tiap commit):
```bash
cat > .git/hooks/post-commit << 'HOOK'
#!/bin/sh
git push --quiet &
HOOK
chmod +x .git/hooks/post-commit
```

## 7. Verifikasi install

```bash
cd ~/projects/personal/mindscape
python scripts/search.py "mindscape" --top 3
python scripts/lint.py
python scripts/watch.py --once --dry-run --mode queue
cat wiki/index.md | head -n 20
cat wiki/log.md | tail -n 20
gh repo view fprtm/mindscape --web  # cek github
```

## 8. Cara pakai harian (ingat 3 perintah)

```bash
# ada hal baru → drop ke raw/sources/ lalu:
ingest raw/sources/2026-08-28-judul.md
# atau kalau watcher jalan: otomatis ke wiki/inbox/ → confirm ingest ...

# mau nanya:
# "bedanya RAG vs wiki apa?" → agent baca wiki/index.md + search, jawab pakai [[wiki/...]]

# beres-beres:
lint
# atau python scripts/lint.py
```

Jangan pernah hapus `raw/sources/` — immutable, append-only (lihat `AGENTS.md §1` + `wiki/concepts/epistemic-rules.md`).

---

**Source of truth untuk tutorial ini:** file ini (`SETUP.md`) + `AGENTS.md` + `wiki/conventions.md`. Kalau pindah laptop, cukup ikutin langkah 1-7 di atas, vault akan identik.
