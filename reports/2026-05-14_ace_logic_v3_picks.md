# Ace Logic v3 Picks - 2026-05-14

## Scope

These picks use only games that had not started when the May 14 card was built. Already-started early games were excluded. The model also passed on STL @ ATH and SF @ LAD NRFI because those spots failed the v3 environment/top-order filters.

## What changed after grading May 13

- Yesterday's card went 6-4 overall, with NRFI and props both 3-2.
- The model now penalizes teams/top orders that just created first-inning damage in the prior slate.
- K overs now require whiff skill, opponent K path, and workload path. A low line alone is not enough.
- K unders are back in play against non-elite pitchers when line/workload/opponent contact point that way.
- The card stays smaller when the remaining slate is thin.

## Today's NRFI card

| Rank | Matchup | Pitchers | Confidence | Why |
|---:|---|---|---:|---|
| 1 | PHI @ BOS | Jesus Luzardo vs Ranger Suarez | 57% | Cold Fenway, wind in, and 7.0-7.5 total help. Rain-delay risk and Phillies top-order power cap it. |
| 2 | CHC @ ATL | Ben Brown vs Chris Sale | 55% | Sale anchors one side and the total is 7.5. Braves top-three quality caps the score. |
| 3 | KC @ CWS | Kris Bubic vs Anthony Kay | 53% | Cool weather and wind in help, but Kay vs Garcia/Witt creates asymmetry. Small lean only. |

## Today's pitcher props

| Rank | Player & Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Chris Sale O 6.5 K | 63% | Best skill edge on remaining slate; elite whiff arm with normal workload path. |
| 2 | Kris Bubic O 5.5 K | 61% | White Sox K path plus starter workload support. |
| 3 | Anthony Kay U 3.5 K | 60% | Non-elite whiff arm vs Kansas City contact/righty-heavy profile. |
| 4 | Landen Roupp U 5.5 K | 59% | High line vs deep Dodgers contact/power lineup and workload volatility. |
| 5 | Ben Brown O 3.5 K | 58% | Low line creates a four-K path; capped because Atlanta can shorten counts. |

## Notable passes

- STL @ ATH NRFI: Sutter Health Park, 9.5-10.0 total, and Athletics top-order power fail the environment filter.
- SF @ LAD NRFI: Dodgers top order plus wind out is too much first-inning risk.
- Jesus Luzardo/Ranger Suarez K overs: weather/rain-delay risk makes workload too fragile.
- Emmet Sheehan K props: Giants' Lee/Arraez contact profile creates enough uncertainty to pass.

## Tracking files

- Picks: `data/picks/2026-05-14_picks.csv`
- Results template: `data/results/2026-05-14_results.csv`

After games finish:

```bash
python3 scripts/grade_picks.py --date 2026-05-14
python3 scripts/summarize_performance.py
python3 scripts/make_prop_results_report.py --date 2026-05-14
python3 scripts/make_nrfi_results_report.py --date 2026-05-14
```
