# Ace Logic v2 Model Notes

This model version incorporates the graded 2026-05-12 slate.

## Baseline from v1

- 2026-05-12 overall: 9-6, 60.0%
- NRFI: 6-4, 60.0%
- Pitcher props: 3-2, 60.0%

## NRFI scoring updates

### 1. Two-sided pitcher requirement

An NRFI cannot receive a premium confidence score from one elite starter alone. Score both halves independently:

- Away starter vs home top three
- Home starter vs away top three

If one half is materially weak, cap the full-game NRFI confidence.

Suggested caps:

- One elite starter + one average/uncertain starter vs dangerous top three: max 58%
- One elite starter + one weak/low-sample starter vs dangerous top three: max 54%
- Both starters favorable and park/weather neutral or pitcher-friendly: eligible for 62%+

### 2. Top-three danger penalty

Apply a downgrade when the opposing top three has at least two of the following:

- Strong leadoff OBP/discipline profile
- Top-three wOBA or OPS strength
- Clear ISO/home-run threat
- Platoon advantage against the starter
- Low strikeout/contact-heavy profile against the starter's primary pitch type

This matters most in the first inning because the top three are guaranteed to bat.

### 3. Roof is not a run-suppression factor

A closed roof removes weather volatility, but it should not be treated as pitcher-friendly by itself. Continue to apply:

- Park run factor
- Park HR factor
- Top-order quality
- Starter walk/contact risk

### 4. Fragility filter

If the written explanation identifies a direct YRFI path, the pick should usually be excluded from the Top 10. If included because the slate is thin, cap it at 51-52%.

Examples of direct YRFI paths:

- Low-sample/opener/converted reliever vs multiple power bats
- Hitter-friendly park plus warm weather
- High BB% starter vs disciplined leadoff hitter
- One starter clearly overmatched even if the other starter is elite

## Pitcher prop updates

### 1. Prefer K overs at discounted lines

K overs performed better than the single K under on 2026-05-12. Keep prioritizing:

- Strong pitcher whiff/CSW profile
- Opponent swing-and-miss support
- Reasonable line relative to workload
- Stable pitch count/leash

### 2. Limited-sample leash penalty

For pitchers with limited MLB sample, international transition uncertainty, opener risk, or recent workload volatility, do not recommend K overs unless at least one condition is true:

- Line is meaningfully discounted
- Opponent is clearly high-K throughout the lineup
- Projected outs/innings strongly support the line
- Recent pitch counts show normal starter leash

### 3. K-under restraint on elite arms

Avoid under recommendations on elite whiff pitchers unless there is more than a contact-oriented top order. Require at least one additional edge:

- Pitch-count restriction
- Injury return or short rest
- Weather/delay risk
- Opponent low-K profile across the full lineup, not just top three
- Inflated line relative to recent workload

## Next-slate checklist

Before publishing picks:

1. Score both NRFI halves separately.
2. Apply asymmetry caps before ranking.
3. Separate roof/no-weather benefit from true pitcher-friendly park effects.
4. Reject fragile NRFIs with obvious YRFI paths.
5. For props, check projected workload before using pitch-quality arguments.
6. Record final picks under `data/picks/YYYY-MM-DD_picks.csv` with `model_version=ace_logic_v2`.
