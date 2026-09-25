#!/usr/bin/env python3
"""Flag clue files that repeat the same sentences as other clue files."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

SKIP = re.compile(r"^(#|\*\*File|- In their words: Not in this call|Not in this call|- Not in this call)")


def lines(path: Path) -> set[str]:
    out = set()
    for raw in path.read_text(errors="replace").splitlines():
        line = raw.strip()
        value = re.sub(r"^-\s*[^:]{1,60}:\s*", "", line)
        if len(value) < 40 or SKIP.match(line) or '"' in line or "“" in line:
            continue
        out.add(re.sub(r"\s+", " ", line.lower()))
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("clues", type=Path)
    parser.add_argument("--min-files", type=int, default=3)
    args = parser.parse_args()
    clue_files = sorted(args.clues.glob("*.md")) if args.clues.exists() else []
    if len(clue_files) < args.min_files:
        print(f"NOTHING TO CHECK: {len(clue_files)} clue file(s) in {args.clues}; the check needs at least {args.min_files}. Read them yourself instead.")
        return 1
    seen: dict[str, set[Path]] = defaultdict(set)
    for path in clue_files:
        for line in lines(path):
            seen[line].add(path)
    flagged: dict[Path, int] = defaultdict(int)
    for line, paths in seen.items():
        if len(paths) >= args.min_files:
            for path in paths:
                flagged[path] += 1
    for path, count in sorted(flagged.items()):
        print(f"GENERIC {path}: {count} line(s) shared with {args.min_files}+ other clue files")
    if flagged:
        print(f"REVIEW: {len(flagged)} clue file(s) share sentences with other calls. Reread those calls; keep shared lines only if they are true of each call.")
    else:
        print("OK: no boilerplate shared across clue files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
