# Ace Logic v7 Model Notes

This version is designed for prediction-market use, where selectivity and price discipline matter more than producing a large card.

## Hard lesson from prior tracking

- Broad full-slate leans underperformed when tracked as if they were official bets.
- NRFI/YRFI has been the strongest sleeve, but only when confidence is high and environment/starter filters agree.
- Props have been volatile; hitter total bases are useful only in the best environments or with clear platoon/order edges.
- Pitcher K props need stricter workload and line checks.

## v7 official-pick policy

### 1. Official picks are not the same as leans

Every future slate should separate:

- **Official picks**: actionable candidates that pass thresholds.
- **Watchlist**: model likes it, but price or confirmation is missing.
- **Informational leans**: full-slate opinions, not intended as bets unless upgraded.
- **Passes**: no bet.

### 2. Confidence thresholds

Minimum confidence for official consideration:

- NRFI/YRFI: **60%+ preferred**, never below 58% unless market price is extremely favorable.
- Hitter total bases: **60%+ preferred** and must have strong game environment or matchup edge.
- Pitcher props: **62%+ preferred** unless the line is clearly discounted.
- HR props: generally not official unless explicitly labeled longshot/value and priced with a major edge.
- Parlays: both legs should be **60%+**, independent, and price-positive.

### 3. Market-price edge requirement

A pick should only be recommended as official if:

```text
model confidence - market implied probability >= 5 percentage points
```

Examples:

- Model 62%, market price 55%: official candidate, +7 edge.
- Model 62%, market price 61%: pass/no edge.
- Model 59%, market price 48%: possible official only if qualitative edge is strong and risk is low.

If market price is not available, label the pick as **watchlist / price needed**, not official.

### 4. Volume limits

Default maximum official card:

- 1-3 official straight picks per slate.
- 0-1 parlay per slate.
- No forced pitcher props.
- No forced hitter props.
- No forced full-slate betting card.

### 5. Prediction-market discipline

- Do not chase action just because games are available.
- Avoid low-confidence full-slate leans as official bets.
- Prefer no pick over a marginal pick.
- Track closing price if available to measure whether the model beats the market over time.
- Do not promise profitability; the goal is disciplined positive expected value selection.

## Required output style going forward

When asked for picks:

1. State official picks first.
2. Include model confidence.
3. Include max buy price / fair price if market price is not provided.
4. Include watchlist separately.
5. Include full-slate leans only if requested, labeled informational.
6. Include a short reason for every pass on popular/high-risk spots.
