\
#!/usr/bin/env python3
"""Summarize model performance across all graded MLB pick files."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List


def read_rows(paths: Iterable[Path]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for path in paths:
        with path.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["source_file"] = path.name
                rows.append(row)
    return rows


def confidence_bucket(value: str) -> str:
    try:
        confidence = float(value)
    except (TypeError, ValueError):
        return "unknown"
    lower = int(confidence // 5 * 5)
    upper = lower + 4
    return f"{lower}-{upper}"


def summarize(rows: List[Dict[str, str]], group_key: str) -> List[Dict[str, str]]:
    groups: Dict[str, Dict[str, int]] = defaultdict(lambda: {"WIN": 0, "LOSS": 0, "PUSH": 0, "PENDING": 0})
    for row in rows:
        key = row.get(group_key, "") or "unknown"
        result = (row.get("result") or "PENDING").upper()
        if result not in groups[key]:
            result = "PENDING"
        groups[key][result] += 1

    output = []
    for key, counts in sorted(groups.items()):
        graded = counts["WIN"] + counts["LOSS"]
        hit_rate = counts["WIN"] / graded if graded else 0
        output.append(
            {
                "group": group_key,
                "value": key,
                "wins": counts["WIN"],
                "losses": counts["LOSS"],
                "pushes": counts["PUSH"],
                "pending": counts["PENDING"],
                "graded_picks": graded,
                "hit_rate": f"{hit_rate:.3f}",
            }
        )
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root; defaults to current directory")
    parser.add_argument("--output", default="reports/model_performance_summary.csv", help="Output CSV path")
    args = parser.parse_args()

    root = Path(args.root)
    graded_paths = sorted((root / "data" / "graded").glob("*_graded.csv"))
    if not graded_paths:
        raise SystemExit("No graded files found. Run scripts/grade_picks.py first.")

    rows = read_rows(graded_paths)
    for row in rows:
        row["confidence_bucket"] = confidence_bucket(row.get("confidence", ""))

    summary_rows: List[Dict[str, str]] = []
    summary_rows.extend(summarize(rows, "overall")) if False else None

    total_counts = {"WIN": 0, "LOSS": 0, "PUSH": 0, "PENDING": 0}
    for row in rows:
        result = (row.get("result") or "PENDING").upper()
        if result not in total_counts:
            result = "PENDING"
        total_counts[result] += 1
    graded = total_counts["WIN"] + total_counts["LOSS"]
    summary_rows.append(
        {
            "group": "overall",
            "value": "all",
            "wins": total_counts["WIN"],
            "losses": total_counts["LOSS"],
            "pushes": total_counts["PUSH"],
            "pending": total_counts["PENDING"],
            "graded_picks": graded,
            "hit_rate": f"{(total_counts['WIN'] / graded if graded else 0):.3f}",
        }
    )
    for key in ["type", "market", "pick", "model_version", "confidence_bucket"]:
        summary_rows.extend(summarize(rows, key))

    out_path = root / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["group", "value", "wins", "losses", "pushes", "pending", "graded_picks", "hit_rate"]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"wrote: {out_path}")
    for row in summary_rows:
        if row["group"] in {"overall", "type"}:
            print(f"{row['group']}={row['value']}: {row['wins']}-{row['losses']}-{row['pushes']} pending={row['pending']} hit_rate={float(row['hit_rate']):.1%}")


if __name__ == "__main__":
    main()
