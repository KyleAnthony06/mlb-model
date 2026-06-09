# Prediction Market Selection Policy

This repo now uses a stricter policy for picks intended to be placed on prediction markets.

## Core rule

A pick is only an **official pick** when it has both:

1. Strong model confidence.
2. A market price that leaves enough edge.

The model should not recommend every lean as a bet.

## Price conversion

Prediction-market prices are implied probabilities:

- 57 cents = 57% implied probability
- 0.57 = 57% implied probability

For a YES-style pick:

```text
edge = model confidence - market price
```

For a pick to be official, target:

```text
edge >= 5 percentage points
```

## Max buy price

If the model says a pick is 62%, the fair price is 62 cents. To keep edge, the max buy price should be about:

```text
62 - 5 = 57 cents
```

So the report should say something like:

```text
Model: 62%
Max buy: 57c
Pass above: 57c
```

## Default volume

The default slate should usually produce:

- 1-3 official straight picks
- 0-1 two-leg parlay
- Watchlist if prices are not available

If nothing qualifies, the correct output is **no official picks**.

## Risk notes

This process can improve discipline but cannot guarantee profit. Prediction markets have variance, stale/inaccurate data risk, liquidity issues, fees/spreads, and late lineup changes. Only risk money you can afford to lose.
