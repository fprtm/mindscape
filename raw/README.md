# raw/ — Immutable Sources (Layer 1)

**Do not edit files here.** This is the source of truth.

- `sources/` — drop new sources here: `.md` from Obsidian Web Clipper, PDFs, notes, transcripts.
  - Naming: `YYYY-MM-DD-<slug>.md` (e.g. `2026-04-04-llm-wiki.md`)
  - Content: keep original markdown + frontmatter if any. Human curates; LLM reads only.
- `assets/` — locally downloaded images (Obsidian attachmentFolderPath).
  - Set in Obsidian → Settings → Files & links → Attachment folder path = `raw/assets`
  - Hotkey `Ctrl+Shift+D` → Download attachments for current file (see `.obsidian/` config).

Flow: `raw/sources/<new-file.md>` → tell LLM `ingest raw/sources/<new-file.md>` → LLM writes to `wiki/` and updates `wiki/index.md` + `wiki/log.md`.

See `wiki/sources/2026-04-04-llm-wiki.md` for the pattern description and `AGENTS.md` §3.1 for ingest workflow.
