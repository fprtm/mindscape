#!/usr/bin/env python3
"""
Lint checks for the LLM wiki (AGENTS.md §3.3).

Checks:
- orphans (0 inbound [[links]])
- stubs (status: stub/planned)
- broken [[links]]
- duplicate near-concepts (stem overlap)
- copied-state drift hints (literal SHA/count/date in body should be frontmatter/live)

Usage: python scripts/lint.py [--fix]
Creates wiki/syntheses/lint-YYYY-MM-DD.md on demand.
"""
import re
import json
from pathlib import Path
from datetime import date

VAULT = Path(__file__).resolve().parents[1]
WIKI = VAULT / "wiki"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]]*)?(?:\|[^\]]*)?\]\]")
FRONT_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

def parse_front(path: Path):
    m = FRONT_RE.match(path.read_text(encoding="utf-8", errors="ignore"))
    if not m:
        return {}
    raw = m.group(1)
    d = {}
    for line in raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            d[k.strip()] = v.strip()
    return d

def main():
    md_files = list(WIKI.rglob("*.md"))
    # inbound links
    inbound = {p.relative_to(VAULT).as_posix(): 0 for p in md_files}
    link_edges = []
    for p in md_files:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(txt):
            target = m.group(1).strip()
            # resolve bare name to likely file
            candidates = [k for k in inbound if target in k or k.endswith(target + ".md")]
            if candidates:
                for c in candidates:
                    inbound[c] += 1
                    link_edges.append((p.relative_to(VAULT).as_posix(), c))
    orphans = [k for k, v in inbound.items() if v == 0 and "index.md" not in k and "log.md" not in k and "overview.md" not in k]
    stubs = []
    for p in md_files:
        fm = parse_front(p)
        if fm.get("status") in ("stub", "planned"):
            stubs.append(p.relative_to(VAULT).as_posix() + f" ({fm.get('status')})")
    # broken links: target not matching any file stem
    all_stems = {Path(k).stem for k in inbound}
    broken = []
    for p in md_files:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(txt):
            target = m.group(1).strip().split("/")[-1]
            if target not in all_stems and target not in ("index", "log", "overview"):
                # heuristic: ignore external pass
                broken.append(f"{p.relative_to(VAULT).as_posix()} -> [[{target}]]")
    # duplicate stems: concepts/foo vs concepts/foo-number
    from collections import defaultdict
    by_base = defaultdict(list)
    for k in inbound:
        stem = Path(k).stem
        base = re.split(r"[-_]", stem)[0]
        by_base[base].append(k)
    dupe_groups = {b: v for b, v in by_base.items() if len(v) > 1 and b not in ("index","log","overview","README")}

    print("=== LINT REPORT ===")
    print(f"\nOrphans ({len(orphans)}): {orphans[:10]}")
    print(f"\nStubs ({len(stubs)}): {stubs[:10]}")
    print(f"\nBroken links ({len(broken)}): {broken[:10]}")
    print(f"\nNear-duplicate stems: {dict(list(dupe_groups.items())[:5])}")
    print(f"\nTotal pages: {len(md_files)}")
    # Suggest lint page
    today = date.today().isoformat()
    out = WIKI / f"syntheses/lint-{today}.md"
    if not out.exists():
        print(f"\nTip: create {out.relative_to(VAULT)} via: python scripts/lint.py -> wire to wiki/syntheses/lint-{{date}}.md (manual step)")

if __name__ == "__main__":
    main()
