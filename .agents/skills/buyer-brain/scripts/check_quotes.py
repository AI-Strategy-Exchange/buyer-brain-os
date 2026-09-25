#!/usr/bin/env python3
"""Check quoted strings in clue or card Markdown against transcript files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def norm(text: str) -> str:
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", text).lower()


def files(path: Path) -> list[Path]:
    return sorted(item for item in path.rglob("*") if item.is_file())


def quotes(path: Path) -> list[tuple[Path, str]]:
    found = []
    for item in files(path):
        if item.suffix.lower() not in {".md", ".txt"}:
            continue
        text = item.read_text(errors="replace")
        pairs = re.findall(r'"([^"\n]*)"', text) + re.findall(r"\u201c([^\u201d\n]*)\u201d", text)
        found.extend((item, quote) for quote in pairs if len(quote.strip(" .,;:!?")) >= 12)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", type=Path)
    parser.add_argument("transcripts", type=Path)
    args = parser.parse_args()
    sources = [item for item in files(args.transcripts) if item.name.lower() != "readme.md"]
    found = quotes(args.records) if args.records.exists() else []
    if not sources or not found:
        print(f"NOTHING TO CHECK: {'no source files under ' + str(args.transcripts) if not sources else 'no quotes in ' + str(args.records)}")
        return 1
    summary = [item for item in sources if "summaries" in item.parts]
    verbatim = norm("\n".join(item.read_text(errors="replace") for item in sources if item not in summary))
    summarized = norm("\n".join(item.read_text(errors="replace") for item in summary))
    missing, from_summary = [], []
    for item, quote in found:
        key = norm(quote).strip(" .,;:!?")
        if key in verbatim:
            continue
        (from_summary if key in summarized else missing).append((item, quote))
    for item, quote in missing:
        print(f"MISSING {item}: {quote}")
    for item, quote in from_summary:
        print(f"SUMMARY ONLY {item}: {quote}")
    if missing:
        print(f"REVIEW: {len(missing)} quoted string(s) not found verbatim. Fix the wording from the source, or drop the quote marks and keep it as your paraphrase.")
    if from_summary:
        print(f"REVIEW: {len(from_summary)} quote(s) exist only in an AI summary. Present them as the summary's wording, not the buyer's.")
    if not missing and not from_summary:
        print(f"OK: all {len(found)} quoted strings appear verbatim in the sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
