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

---
