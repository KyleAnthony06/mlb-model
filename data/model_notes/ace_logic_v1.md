# Ace Logic v1 Model Notes

## Purpose
Track daily MLB NRFI and pitcher-prop picks, grade them after final scores, and use the results to update tomorrow's rules.

## Current scoring rules
- NRFI confidence starts with both starters' first-inning/run-prevention profile, then adjusts for opposing top-three OBP/power, park factor, and weather.
- Pitcher K props prioritize line value, pitcher whiff/CSW profile, opponent swing-and-miss tendency, expected leash, and weather/park context.
- Downgrade any big-name pitcher when the top-order matchup, park, or weather materially increases first-inning run or contact risk.

## Review process
After games are final:
1. Fill `data/results/YYYY-MM-DD_results.csv`.
2. Run `python3 scripts/grade_picks.py --date YYYY-MM-DD`.
3. Run `python3 scripts/summarize_performance.py`.
4. Add notes here about any repeatable model adjustment, not one-game noise.

## Candidate adjustments to test
- Penalize NRFI confidence when pitcher BB% is elevated and the opposing leadoff hitter has strong plate discipline.
- Penalize NRFI confidence for high-carry environments: Coors, 90°F+ heat, or strong wind out.
- For K props, require opponent chase/swinging-strike support before betting high lines like 7.5+.
- Track line sensitivity separately, e.g. Peralta over 5.5 vs over 6.5.
