# Ace Logic v7 Official Picks - 2026-06-15

## Prediction-market rules used

These are **official candidates**, not blind bets at any price. Only place if your market price is at or below the max buy.

- Target edge: model confidence - market price >= 5 percentage points
- No forced full-slate card
- No pick if price is too expensive
- Smaller card preferred

## Official candidates

| Rank | Pick | Model Confidence | Max Buy | Why |
|---:|---|---:|---:|---|
| 1 | PIT @ ATH YRFI | 64% | 59c | Sutter Health Park, 92F, 10.0-10.5 total, wind, and both top orders create the clearest first-inning scoring environment. |
| 2 | Pete Crow-Armstrong O 1.5 Total Bases | 63% | 58c | Leadoff at Wrigley with wind out against Michael Lorenzen/Colorado run-prevention profile. Multiple paths to 2+ TB. |
| 3 | Zack Wheeler O 6.5 K | 62% | 57c | Best pitcher-prop skill edge vs a Marlins lineup with K paths. Line is high, so pass above max buy. |

## Optional two-leg parlay

Only if both legs are individually available at or below max buy:

| Leg | Pick | Model Confidence |
|---:|---|---:|
| 1 | PIT @ ATH YRFI | 64% |
| 2 | Pete Crow-Armstrong O 1.5 TB | 63% |

Estimated parlay model probability: about **40%**. To keep edge, I would want an implied parlay price around **35c or better**.

## Watchlist / pass notes

- Nick Kurtz O 1.5 TB: strong environment, but correlated with PIT @ ATH YRFI. Prefer the YRFI as the official exposure unless Kurtz is clearly mispriced.
- CHC/COL YRFI: attractive environment, but Shota Imanaga can suppress Colorado early; prefer PCA total bases instead.
- Zack Wheeler O 6.5 K: included, but only with strict price discipline because pitcher props have been weaker than NRFI/hitter TB in tracking.
- NYM @ CIN YRFI: Great American Ball Park helps, but Chase Burns is strong enough to avoid official status.
- TB @ LAD YRFI: Dodgers lineup is dangerous, but not enough edge at likely market prices.
- PIT @ ATH hitter props: useful if the YRFI price is too high, but do not overstack the same game.

## Tracking files

- Picks: `data/picks/2026-06-15_picks.csv`
- Results template: `data/results/2026-06-15_results.csv`

After games finish:

```bash
python3 scripts/grade_picks.py --date 2026-06-15
python3 scripts/summarize_performance.py
python3 scripts/make_prop_results_report.py --date 2026-06-15
python3 scripts/make_nrfi_results_report.py --date 2026-06-15
```
