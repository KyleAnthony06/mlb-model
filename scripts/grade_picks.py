\
#!/usr/bin/env python3
"""Grade saved MLB picks against manually entered final results.

Results format:
- NRFI actual = total first-inning runs by both teams. 0 wins NRFI; 1+ loses NRFI.
- PROP actual = final stat for the listed market. For K props, enter pitcher strikeouts.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

REQUIRED_PICK_COLUMNS = {
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
}
REQUIRED_RESULT_COLUMNS = {"date", "pick_id", "type", "matchup", "player", "market", "actual", "notes"}


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: Iterable[Dict[str, str]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def require_columns(path: Path, rows: List[Dict[str, str]], required: set[str]) -> None:
    if not rows:
        return
    missing = required - set(rows[0])
    if missing:
        missing_text = ", ".join(sorted(missing))
        raise SystemExit(f"{path} is missing required columns: {missing_text}")


def parse_float(value: str) -> float | None:
    value = (value or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise SystemExit(f"Could not parse numeric value: {value!r}") from exc


def grade_pick(pick: Dict[str, str], result: Dict[str, str] | None) -> Tuple[str, str]:
    if result is None or not (result.get("actual") or "").strip():
        return "PENDING", "Missing actual result"

    actual_text = result["actual"].strip().upper()
    if actual_text in {"VOID", "DNP", "NA", "N/A"}:
        return "PUSH", "Void/no-action result"

    actual = parse_float(result["actual"])
    pick_type = pick["type"].upper().strip()
    side = pick["pick"].upper().strip()

    if pick_type == "NRFI":
        if actual == 0:
            return ("WIN", "NRFI hit: no first-inning runs") if side == "NRFI" else ("LOSS", "YRFI side lost")
        return ("LOSS", f"NRFI lost: {actual:g} first-inning runs") if side == "NRFI" else ("WIN", "YRFI side hit")

    if pick_type == "PROP":
        line = parse_float(pick.get("line", ""))
        if line is None:
            return "PENDING", "Missing prop line"
        if actual == line:
            return "PUSH", f"Actual {actual:g} landed exactly on line {line:g}"
        if side == "OVER":
            return ("WIN", f"Actual {actual:g} over line {line:g}") if actual > line else ("LOSS", f"Actual {actual:g} under line {line:g}")
        if side == "UNDER":
            return ("WIN", f"Actual {actual:g} under line {line:g}") if actual < line else ("LOSS", f"Actual {actual:g} over line {line:g}")
        return "PENDING", f"Unsupported prop side: {side}"

    return "PENDING", f"Unsupported pick type: {pick_type}"


def create_results_template(path: Path, picks: List[Dict[str, str]]) -> None:
    rows = [
        {
            "date": pick["date"],
            "pick_id": pick["pick_id"],
            "type": pick["type"],
            "matchup": pick["matchup"],
            "player": pick["player"],
            "market": pick["market"],
            "actual": "",
            "notes": "Fill after games are final. NRFI actual = total 1st inning runs; K actual = strikeouts.",
        }
        for pick in picks
    ]
    write_csv(path, rows, ["date", "pick_id", "type", "matchup", "player", "market", "actual", "notes"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Slate date in YYYY-MM-DD format")
    parser.add_argument("--root", default=".", help="Repository root; defaults to current directory")
    args = parser.parse_args()

    root = Path(args.root)
    picks_path = root / "data" / "picks" / f"{args.date}_picks.csv"
    results_path = root / "data" / "results" / f"{args.date}_results.csv"
    graded_path = root / "data" / "graded" / f"{args.date}_graded.csv"

    if not picks_path.exists():
        raise SystemExit(f"Missing picks file: {picks_path}")
    picks = read_csv(picks_path)
    require_columns(picks_path, picks, REQUIRED_PICK_COLUMNS)

    if not results_path.exists():
        create_results_template(results_path, picks)
        raise SystemExit(f"Created results template: {results_path}. Fill actuals, then rerun.")

    results = read_csv(results_path)
    require_columns(results_path, results, REQUIRED_RESULT_COLUMNS)
    results_by_id = {row["pick_id"]: row for row in results}

    graded_rows = []
    for pick in picks:
        result = results_by_id.get(pick["pick_id"])
        outcome, grade_notes = grade_pick(pick, result)
        graded_rows.append(
            {
                **pick,
                "actual": "" if result is None else result.get("actual", ""),
                "result": outcome,
                "grade_notes": grade_notes,
                "result_notes": "" if result is None else result.get("notes", ""),
            }
        )

    fieldnames = list(picks[0].keys()) + ["actual", "result", "grade_notes", "result_notes"]
    write_csv(graded_path, graded_rows, fieldnames)

    wins = sum(1 for row in graded_rows if row["result"] == "WIN")
    losses = sum(1 for row in graded_rows if row["result"] == "LOSS")
    pushes = sum(1 for row in graded_rows if row["result"] == "PUSH")
    pending = sum(1 for row in graded_rows if row["result"] == "PENDING")
    graded = wins + losses
    hit_rate = wins / graded if graded else 0
    print(f"wrote: {graded_path}")
    print(f"record: {wins}-{losses}-{pushes}, pending={pending}, hit_rate={hit_rate:.1%}")


if __name__ == "__main__":
    main()
