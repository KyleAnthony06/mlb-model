# Ace Logic v5 Full Slate - 2026-06-08

## Model context

This slate uses the graded May 12-15 tracking results:

- Overall tracked record: 26-20-1, 56.5%
- NRFI/YRFI record: 14-8, 63.6%
- Props record: 12-12-1, 50.0%
- Hitter props first sample: 3-2

Model adjustment for today: first-inning picks remain the primary sleeve, hitter total bases are now a regular secondary sleeve, and pitcher K props are used more selectively.

## Full-slate first-inning leans

| Game | Lean | Confidence | Why |
|---|---|---:|---|
| SEA @ BAL | YRFI | 54% | Camden, 78°F, 13 mph wind, and multiple top-order OBP/power paths. |
| NYY @ CLE | NRFI | 53% | Gavin Williams anchors it and Yankees projected top lacks Judge; warm weather keeps this thin. |
| BOS @ TB | NRFI | 54% | Indoor run control and two left-handed starters; Tampa top three caps confidence. |
| PHI @ TOR | YRFI | 56% | Patrick Corbin vs PHI top and Toronto righties vs Sanchez create first-inning risk. |
| HOU @ LAA | YRFI | 55% | Yordan/Altuve/Pena and Neto/Trout give both sides scoring paths. |
| CIN @ SD | NRFI | 58% | Petco and Buehler/Abbott profiles give the cleanest late-game NRFI outside Oracle. |
| WSH @ SF | NRFI | 60% | Oracle, 62°F, Logan Webb anchor, and Washington contact without much early power. |
| MIL @ ATH | YRFI | 62% | Las Vegas Ballpark, 87°F, 24 mph wind, and strong top-order bats. |

## Pitcher props

| Rank | Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Gavin Williams O 6.5 K | 61% | Yankees projected lineup is lefty-heavy with K pockets and no projected Judge. |
| 2 | Grayson Rodriguez O 5.5 K | 60% | Normal workload path and enough Houston swing-and-miss behind the stars. |
| 3 | Logan Webb U 5.5 K | 60% | Excellent pitcher, but not a pure whiff arm; Washington contact profile can hold Ks down. |
| 4 | Emerson Hancock O 4.5 K | 58% | Low line vs Baltimore K pockets; Camden power risk caps confidence. |

## Hitter props

| Rank | Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Yordan Alvarez O 1.5 TB | 62% | Elite total-base profile and fair 1.5 line. |
| 2 | Jackson Chourio O 1.5 TB | 61% | Vegas/Las Vegas Ballpark heat and wind support extra-base upside. |
| 3 | Nick Kurtz O 1.5 TB | 60% | Same high-run environment; strong wOBA and top-order role. |
| 4 | Junior Caminero O 1.5 TB | 59% | Right-handed power vs lefty in a controlled dome. |
| 5 | Vladimir Guerrero Jr. O 1.5 TB | 58% | Right-handed middle-order bat vs lefty; capped by Sanchez quality. |

## Two-leg parlay

| Leg | Pick | Confidence | Reason |
|---:|---|---:|---|
| 1 | WSH @ SF NRFI | 60% | Best true NRFI setup: Oracle, cool weather, Webb anchor. |
| 2 | Yordan Alvarez O 1.5 TB | 62% | Best hitter total-base edge in a separate game. |

**Parlay logic:** independent games/markets, one from the strongest NRFI sleeve and one from the hitter-total-bases sleeve. Keep stake smaller than straight bets; parlays amplify variance.

## Tracking files

- Picks: `data/picks/2026-06-08_picks.csv`
- Results template: `data/results/2026-06-08_results.csv`

After games finish:

```bash
python3 scripts/grade_picks.py --date 2026-06-08
python3 scripts/summarize_performance.py
python3 scripts/make_prop_results_report.py --date 2026-06-08
python3 scripts/make_nrfi_results_report.py --date 2026-06-08
```
