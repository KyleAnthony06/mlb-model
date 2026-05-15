# Ace Logic v4 Picks - 2026-05-15

## What changed after grading May 14

- May 14 went 4-4 overall, with NRFI stronger than props.
- NRFI remains selective and environment-driven.
- Props were tightened: no thin 3.5 K unders, fewer middle-tier overs, and more emphasis on elite whiff plus workload.
- K unders are mostly avoided today because May 14 showed poor margin for error without a real pitch-count cap.

## Today's NRFI card

| Rank | Matchup | Pitchers | Confidence | Why |
|---:|---|---|---:|---|
| 1 | SD @ SEA | Randy Vasquez vs Emerson Hancock | 62% | Dome, 7.0 total, and two viable run-prevention profiles. Best two-sided NRFI screen on the slate. |
| 2 | NYY @ NYM | Cam Schlittler vs Clay Holmes | 59% | Citi Field and 7.0 total help. Capped because Rice/Judge and Soto create first-inning damage paths. |
| 3 | PHI @ PIT | Aaron Nola vs Braxton Ashcraft | 56% | PNC helps run suppression. Phillies top-order power and Pirates lefty bats cap confidence. |
| 4 | MIA @ TB | Janson Junk vs Jesse Scholtens | 55% | Dome stability and no extreme park/weather risk. Contact-heavy Miami top keeps it modest. |

## Today's pitcher props

| Rank | Player & Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Blake Snell O 6.5 K | 64% | Elite whiff arm, normal workload path, and Angels swing-and-miss pockets. |
| 2 | Spencer Strider O 6.5 K | 63% | Premium strikeout skill with workload ceiling against Boston. |
| 3 | Edward Cabrera O 5.5 K | 60% | Real whiff stuff vs White Sox K pockets; capped for command/workload volatility. |
| 4 | Shane Baz O 4.5 K | 60% | Strong stuff at a discounted 4.5 line; avoid if only 5.5 is available. |
| 5 | Clay Holmes O 4.5 K | 58% | Low line and starter workload path; capped by Yankees power/traffic risk. |


## Today's hitter props

| Rank | Player & Prop | Confidence | Why |
|---:|---|---:|---|
| 1 | Nick Kurtz O 1.5 TB | 62% | Sutter Health Park, 91°F, 10.0 total, leadoff role, and strong FTA projection/value. |
| 2 | Mickey Moniak O 1.5 TB | 61% | Coors/high-total setup vs Merrill Kelly; FTA projected 2.8 TB and 72% cover. |
| 3 | Ketel Marte O 1.5 TB | 60% | Leadoff at Coors vs Kyle Freeland with elite PA/park setup; juiced line caps confidence. |
| 4 | Bryce Harper O 1.5 TB | 57% | Plus-money value vs Braxton Ashcraft; PNC caps HR carry but not all 2+ TB paths. |
| 5 | Liam Hicks O 0.5 HR | 52% | Longshot value only: projection around 17.2% vs roughly 10% implied at +825. |

## Notable passes

- ARI @ COL NRFI: Coors, 82 degrees, wind out, and 11.5 total are an automatic pass.
- SF @ ATH NRFI: 91 degrees and 10.0 total at Sutter Health Park are too hitter-friendly.
- MIL @ MIN NRFI: 86 degrees and wind out fail the v4 environment screen.
- BAL @ WSH NRFI: 9.5 total and weak run-prevention profiles fail the two-sided screen.
- TEX @ HOU NRFI: Dome helps, but Yordan/Altuve and Texas lefty top-order quality create too much first-inning damage risk.
- K unders: mostly passed because May 14 showed poor margin without clear pitch-count/opener edges.
- Hitter props are new today and are tracked separately by market (`TB`, `HR`) in the same picks CSV.

## Tracking files

- Picks: `data/picks/2026-05-15_picks.csv`
- Results template: `data/results/2026-05-15_results.csv`

After games finish:

```bash
python3 scripts/grade_picks.py --date 2026-05-15
python3 scripts/summarize_performance.py
python3 scripts/make_prop_results_report.py --date 2026-05-15
python3 scripts/make_nrfi_results_report.py --date 2026-05-15
```
