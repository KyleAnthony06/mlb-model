# Ace Logic v3 Model Notes

This version incorporates the graded May 12 and May 13 slates.

## Performance baseline

- May 12: 9-6, 60.0%
- May 13: 6-4, 60.0%
- Aggregate: 15-10, 60.0%

## Updates from v2

### NRFI updates

1. Keep the two-sided starter requirement from v2.
2. Add a recent-lineup-warning penalty: if a lineup scored in the first inning yesterday and the same top-order profile is active today, downgrade the NRFI unless the pitching/environment edge is strong.
3. Do not force NRFI picks from high-total parks, warm run environments, or elite top-order matchups.
4. A low game total helps only if both starters pass the first-inning matchup screen.

### Pitcher prop updates

1. K overs require three checks: pitcher whiff skill, opponent K path, and workload path.
2. A discounted line is not enough by itself. Avoid overs when quick-contact risk or early removal risk is elevated.
3. K unders are allowed again against non-elite pitchers with high lines, contact-heavy opponents, or poor workload profiles.
4. Continue avoiding unders against elite whiff pitchers unless there is a clear pitch-count, injury, weather-delay, or full-lineup low-K edge.

## May 14 implementation note

The May 14 card excludes already-started games and intentionally stays selective. Several environments fail the v3 screen: Sutter Health Park has a high total, SF @ LAD has wind out and a dangerous Dodgers top order, and early games were already live.
