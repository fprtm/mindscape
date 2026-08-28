#!/usr/bin/env python3
"""
Naive BM25-ish / full-text search over wiki/.
Fallback before installing qmd (https://github.com/tobi/qmd).

Usage:
  python scripts/search.py "persistent wiki vs RAG"
  python scripts/search.py --top 10 "karpathy"
  python scripts/search.py --json "query"

Takes union with index.md selection (AGENTS.md §3.2, §5).
"""
import argparse
import json
import math
import re
from pathlib import Path
from collections import Counter, defaultdict

VAULT = Path(__file__).resolve().parents[1]
WIKI = VAULT / "wiki"
TOKEN_RE = re.compile(r"[a-z0-9]+")

def tokenize(s: str):
    return TOKEN_RE.findall(s.lower())

def load_docs():
    docs = []
    for p in WIKI.rglob("*.md"):
        if ".obsidian" in p.parts:
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # strip frontmatter for scoring but keep it for display
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
        docs.append((p.relative_to(VAULT).as_posix(), text, body))
    return docs

def score_docs(query_tokens, docs):
    N = len(docs)
    doc_tokens = [tokenize(body) for _, _, body in docs]
    df = Counter()
    for toks in doc_tokens:
        df.update(set(toks))
    scores = []
    k1, b = 1.5, 0.75
    avgdl = sum(len(t) for t in doc_tokens) / max(1, N)
    for (path, _, _), toks in zip(docs, doc_tokens):
        tf = Counter(toks)
        dl = len(toks)
        s = 0.0
        for q in query_tokens:
            if q not in tf:
                continue
            idf = math.log((N - df[q] + 0.5) / (df[q] + 0.5) + 1)
            denom = tf[q] + k1 * (1 - b + b * dl / max(1, avgdl))
            s += idf * (tf[q] * (k1 + 1) / denom)
        # small filename bonus
        if any(q in path.lower() for q in query_tokens):
            s += 0.5
        scores.append((s, path))
    scores.sort(reverse=True)
    return scores

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="+", help="search query")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--json", action="store_true", help="json output")
    args = ap.parse_args()
    query = " ".join(args.query)
    docs = load_docs()
    if not docs:
        print("No wiki docs found.")
        return
    q_toks = tokenize(query)
    scored = score_docs(q_toks, docs)
    top = [(p, s) for s, p in scored if s > 0][: args.top]
    if args.json:
        print(json.dumps([{"path": p, "score": round(s, 3)} for p, s in top], indent=2))
    else:
        if not top:
            print(f"No hits for: {query!r}")
            print("Tip: check wiki/index.md — index recall misses buried facts; this search is the union fallback.")
            return
        w = max(len(p) for p, _ in top)
        print(f"Query: {query!r}  ({len(docs)} docs)")
        for p, s in top:
            print(f"  {s:5.2f}  {p:<{w}}")

if __name__ == "__main__":
    main()
