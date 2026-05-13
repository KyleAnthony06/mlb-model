# Ace Logic v2 Picks - 2026-05-13

## Model update used today

These picks use `ace_logic_v2`, built from the 2026-05-12 graded slate:

- Yesterday finished 9-6 overall, with NRFI and pitcher props both at 60%.
- The biggest NRFI lesson: do not let one elite starter carry the entire pick if the other starter has a dangerous first-inning matchup.
- The biggest prop lesson: prefer K overs at discounted lines; be very cautious with K unders against elite whiff pitchers.
- Closed roofs now count as weather-neutral, not pitcher-friendly by themselves.
- Fragile NRFIs with obvious YRFI paths were removed instead of forced into a Top 10.

## Today's graded-card picks

### NRFI card

| Rank | Matchup | Pitchers | Confidence | Why |
|---:|---|---|---:|---|
| 1 | SD @ MIL | Michael King vs Jacob Misiorowski | 62% | Best two-sided run-prevention setup. Dome, 7.0 total, and both starters have enough swing-and-miss to offset top-three traffic. |
| 2 | LAA @ CLE | Reid Detmers vs Parker Messick | 60% | Cold/crosswind conditions and 7.0 total. Messick is the stronger half; Detmers passes the two-sided check but keeps this below elite confidence. |
| 3 | DET @ NYM | Framber Valdez vs Christian Scott | 59% | Citi Field and Framber anchor the pick. Scott vs Detroit is acceptable, but Soto/Bichette on the Mets side cap the score. |
| 4 | TB @ TOR | Griffin Jax vs Dylan Cease | 55% | Dome and low total help. Cease is dominant, but Jax/role uncertainty triggers the v2 asymmetry cap. |
| 5 | KC @ CWS | Seth Lugo vs Noah Schultz | 54% | Cool Chicago weather helps. Top-order OBP/power risk on both sides keeps this as the final lean only. |

### Pitcher K props

| Rank | Player & Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Mitch Keller O 4.5 K | 63% | Discounted line vs Rockies swing-and-miss; stable workload. |
| 2 | Christian Scott O 4.5 K | 62% | Detroit offers full-lineup K paths and Citi supports leash/run prevention. |
| 3 | Dylan Cease O 6.5 K | 60% | Best whiff ceiling among the stronger lines; capped because Tampa can stack lefty contact. |
| 4 | Max Fried O 5.5 K | 60% | Camden wind hurts run prevention more than strikeouts; Baltimore lineup has enough K pockets. |
| 5 | Max Meyer O 4.5 K | 59% | Low line and plus stuff; moderate edge because Minnesota has contact threats. |

## Notable passes from v2 filter

- NYY @ BAL NRFI: Yankees top-order power plus Camden wind out creates too much first-inning damage risk.
- WSH @ CIN NRFI: Great American Ball Park with wind out and a 9+ total fails the environment filter.
- PHI @ BOS NRFI: Fenway with wind out and Painter's volatility creates a direct YRFI path.
- ARI @ TEX NRFI: Roof is neutral, but both starters and both top orders are too volatile.
- SEA @ HOU NRFI: McCullers' recent run prevention/leash risk fails the two-sided starter requirement.
- STL @ ATH NRFI: Sutter Health Park, 80+ degrees, and 10.0 total are a hard pass.
- SF @ LAD NRFI: Ohtani is strong, but Ray vs the Dodgers top with wind out is too asymmetric.

## Tracking files

- Pregame picks: `data/picks/2026-05-13_picks.csv`
- Postgame actuals template: `data/results/2026-05-13_results.csv`

After games finish, fill actuals or ask the agent to grade them, then run:

```bash
python3 scripts/grade_picks.py --date 2026-05-13
python3 scripts/summarize_performance.py
```
