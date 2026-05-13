#!/usr/bin/env python3
"""Create easy-to-read NRFI result reports from a graded picks file."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List


def read_rows(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def result_icon(result: str) -> str:
    result = result.upper()
    if result == "WIN":
        return "HIT"
    if result == "LOSS":
        return "MISS"
    if result == "PUSH":
        return "PUSH"
    return "PENDING"


def first_inning_note(row: Dict[str, str]) -> str:
    actual = (row.get("actual") or "").strip()
    if not actual:
        return "Missing first-inning run total"
    if actual == "0":
        return "0 total first-inning runs"
    return f"{actual} total first-inning run(s)"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Slate date in YYYY-MM-DD format")
    parser.add_argument("--root", default=".", help="Repository root; defaults to current directory")
    args = parser.parse_args()

    root = Path(args.root)
    graded_path = root / "data" / "graded" / f"{args.date}_graded.csv"
    if not graded_path.exists():
        raise SystemExit(f"Missing graded file: {graded_path}")

    rows = [row for row in read_rows(graded_path) if row["type"].upper() == "NRFI"]
    if not rows:
        raise SystemExit(f"No NRFI rows found in {graded_path}")

    wins = sum(1 for row in rows if row["result"].upper() == "WIN")
    losses = sum(1 for row in rows if row["result"].upper() == "LOSS")
    pushes = sum(1 for row in rows if row["result"].upper() == "PUSH")
    pending = sum(1 for row in rows if row["result"].upper() == "PENDING")
    graded = wins + losses
    hit_rate = wins / graded if graded else 0

    report_rows = []
    for row in rows:
        report_rows.append(
            {
                "result": result_icon(row["result"]),
                "matchup": row["matchup"],
                "pick": row["pick"],
                "first_inning_runs": row["actual"],
                "confidence": f"{row['confidence']}%",
                "quick_note": row["result_notes"] or row["grade_notes"] or first_inning_note(row),
            }
        )

    reports_dir = root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    csv_path = reports_dir / f"{args.date}_nrfi_results.csv"
    md_path = reports_dir / f"{args.date}_nrfi_results.md"

    fieldnames = ["result", "matchup", "pick", "first_inning_runs", "confidence", "quick_note"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)

    lines = [
        f"# NRFI Results - {args.date}",
        "",
        f"Record: **{wins}-{losses}-{pushes}** | Pending: **{pending}** | Hit Rate: **{hit_rate:.1%}**",
        "",
        "| Result | Matchup | Pick | 1st Inning Runs | Confidence | Note |",
        "|---|---|---|---:|---:|---|",
    ]
    for row in report_rows:
        note = row["quick_note"].replace("|", "\\|")
        lines.append(
            f"| {row['result']} | {row['matchup']} | {row['pick']} | {row['first_inning_runs']} | {row['confidence']} | {note} |"
        )
    lines.append("")
    lines.append(f"CSV version: `{csv_path}`")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"wrote: {md_path}")
    print(f"wrote: {csv_path}")
    print(f"NRFI record: {wins}-{losses}-{pushes}, pending={pending}, hit_rate={hit_rate:.1%}")


if __name__ == "__main__":
    main()
