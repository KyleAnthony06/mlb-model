#!/usr/bin/env python3
"""Filter daily picks into official bets using confidence and market edge rules.

The optional market prices file should be CSV with:

    pick_id,market_price

`market_price` can be entered as 0.57, 57, or 57%.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Dict, List


def parse_percent(value: str) -> float | None:
    value = (value or "").strip().replace("%", "")
    if not value:
        return None
    parsed = float(value)
    if parsed <= 1:
        parsed *= 100
    return parsed


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_market_prices(path: Path | None) -> Dict[str, float]:
    if path is None:
        return {}
    rows = read_csv(path)
    prices: Dict[str, float] = {}
    for row in rows:
        pick_id = row.get("pick_id", "").strip()
        if not pick_id:
            continue
        prices[pick_id] = parse_percent(row.get("market_price", "")) or 0
    return prices


def classify_pick(confidence: float, market_price: float | None, min_confidence: float, min_edge: float) -> tuple[str, float | None]:
    if confidence < min_confidence:
        return "PASS_LOW_CONFIDENCE", None
    if market_price is None:
        return "WATCHLIST_NEEDS_PRICE", None
    edge = confidence - market_price
    if edge >= min_edge:
        return "OFFICIAL", edge
    return "PASS_NO_EDGE", edge


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="Slate date in YYYY-MM-DD format")
    parser.add_argument("--root", default=".", help="Repository root; defaults to current directory")
    parser.add_argument("--min-confidence", type=float, default=60.0, help="Minimum model confidence for official consideration")
    parser.add_argument("--min-edge", type=float, default=5.0, help="Minimum model edge over market price, in percentage points")
    parser.add_argument("--market-prices", help="Optional CSV path containing pick_id,market_price")
    args = parser.parse_args()

    root = Path(args.root)
    picks_path = root / "data" / "picks" / f"{args.date}_picks.csv"
    if not picks_path.exists():
        raise SystemExit(f"Missing picks file: {picks_path}")

    market_prices = load_market_prices(Path(args.market_prices) if args.market_prices else None)
    rows = read_csv(picks_path)

    output_rows = []
    for row in rows:
        confidence = parse_percent(row.get("confidence", "")) or 0
        market_price = market_prices.get(row["pick_id"])
        status, edge = classify_pick(confidence, market_price, args.min_confidence, args.min_edge)
        if status == "PASS_LOW_CONFIDENCE":
            continue
        output_rows.append(
            {
                "status": status,
                "pick_id": row["pick_id"],
                "type": row["type"],
                "matchup": row["matchup"],
                "pick": row["pick"],
                "player": row["player"],
                "market": row["market"],
                "line": row["line"],
                "confidence": f"{confidence:.1f}%",
                "market_price": "" if market_price is None else f"{market_price:.1f}%",
                "edge": "" if edge is None else f"{edge:.1f}%",
                "reasoning": row["reasoning"],
            }
        )

    reports_dir = root / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    csv_path = reports_dir / f"{args.date}_official_pick_filter.csv"
    md_path = reports_dir / f"{args.date}_official_pick_filter.md"

    fieldnames = [
        "status",
        "pick_id",
        "type",
        "matchup",
        "pick",
        "player",
        "market",
        "line",
        "confidence",
        "market_price",
        "edge",
        "reasoning",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    official = [row for row in output_rows if row["status"] == "OFFICIAL"]
    watchlist = [row for row in output_rows if row["status"] == "WATCHLIST_NEEDS_PRICE"]
    no_edge = [row for row in output_rows if row["status"] == "PASS_NO_EDGE"]

    lines = [
        f"# Official Pick Filter - {args.date}",
        "",
        f"Rules: minimum confidence **{args.min_confidence:.1f}%**, minimum edge **{args.min_edge:.1f}%** over market price.",
        "",
        f"- Official: **{len(official)}**",
        f"- Watchlist needing price: **{len(watchlist)}**",
        f"- Passed confidence but no edge: **{len(no_edge)}**",
        "",
        "| Status | Pick | Market | Confidence | Market Price | Edge | Matchup |",
        "|---|---|---|---:|---:|---:|---|",
    ]
    for row in output_rows:
        display = row["player"] if row["player"] else row["pick"]
        if row["line"]:
            display = f"{display} {row['pick'].title()} {row['line']}"
        lines.append(
            f"| {row['status']} | {display} | {row['market']} | {row['confidence']} | {row['market_price']} | {row['edge']} | {row['matchup']} |"
        )
    lines.append("")
    lines.append(f"CSV version: `{csv_path}`")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"wrote: {md_path}")
    print(f"wrote: {csv_path}")
    print(f"official={len(official)} watchlist={len(watchlist)} no_edge={len(no_edge)}")


if __name__ == "__main__":
    main()
