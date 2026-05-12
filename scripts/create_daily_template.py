\
#!/usr/bin/env python3
"""Create blank daily pick/result templates for a new MLB slate."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

PICK_HEADERS = [
    "date",
    "pick_id",
    "type",
    "matchup",
    "pick",
    "player",
    "market",
    "line",
    "confidence",
    "reasoning",
    "model_version",
]

RESULT_HEADERS = [
    "date",
    "pick_id",
    "type",
    "matchup",
    "player",
    "market",
    "actual",
    "notes",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Slate date in YYYY-MM-DD format")
    parser.add_argument("--root", default=".", help="Repository root; defaults to current directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing templates")
    args = parser.parse_args()

    root = Path(args.root)
    picks_path = root / "data" / "picks" / f"{args.date}_picks.csv"
    results_path = root / "data" / "results" / f"{args.date}_results.csv"

    picks_path.parent.mkdir(parents=True, exist_ok=True)
    results_path.parent.mkdir(parents=True, exist_ok=True)

    for path, headers in [(picks_path, PICK_HEADERS), (results_path, RESULT_HEADERS)]:
        if path.exists() and not args.force:
            print(f"exists: {path}")
            continue
        with path.open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(headers)
        print(f"created: {path}")


if __name__ == "__main__":
    main()
