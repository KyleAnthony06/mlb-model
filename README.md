# mlb-model

A lightweight workspace for tracking MLB NRFI and pitcher-prop picks, grading them after games are final, and carrying lessons forward into the next slate.

## Files added for the Ace Logic workflow

```text
data/
  picks/                 # Daily pregame picks
  results/               # Manual actual results after games finish
  graded/                # Output from the grading script
  model_notes/           # Human-readable model review notes
reports/                 # Aggregate performance summaries
scripts/
  create_daily_template.py
  grade_picks.py
  make_nrfi_results_report.py
  make_prop_results_report.py
  summarize_performance.py
```

The May 12, 2026 Ace Logic slate has already been seeded here:

```text
data/picks/2026-05-12_picks.csv
data/results/2026-05-12_results.csv
```

## Daily workflow

### 1. Before games: save picks

Add each slate's picks to `data/picks/YYYY-MM-DD_picks.csv`.

Required columns:

```csv
date,pick_id,type,matchup,pick,player,market,line,confidence,reasoning,model_version
```

Use:

- `type=NRFI`, `pick=NRFI`, `market=FIRST_INNING_RUNS`, blank `line`
- `type=PROP`, `pick=OVER` or `UNDER`, `market=K` or another stat, numeric `line`
- Hitter props also use `type=PROP`; examples include `market=TB` for total bases and `market=HR` for home runs.

To create blank files for a new slate:

```bash
python3 scripts/create_daily_template.py --date 2026-05-13
```

### 2. After games: enter actuals

Fill `data/results/YYYY-MM-DD_results.csv`.

For NRFI picks:

```text
actual = total first-inning runs by both teams
0 means NRFI won
1+ means NRFI lost
```

For pitcher K props:

```text
actual = final pitcher strikeout total
```

For hitter props:

```text
TB actual = hitter total bases
HR actual = hitter home runs
```

Example:

```csv
date,pick_id,type,matchup,player,market,actual,notes
2026-05-12,2026-05-12-nrfi-01,NRFI,DET @ NYM,,FIRST_INNING_RUNS,0,No first-inning runs
2026-05-12,2026-05-12-prop-01,PROP,ARI @ TEX,MacKenzie Gore,K,6,Gore cleared 4.5 K
```

### 3. Grade the slate

```bash
python3 scripts/grade_picks.py --date 2026-05-12
```

This writes:

```text
data/graded/2026-05-12_graded.csv
```

### 4. Summarize model performance

```bash
python3 scripts/summarize_performance.py
```

This writes:

```text
reports/model_performance_summary.csv
```

The summary breaks performance down by:

- Overall record
- Pick type: NRFI vs PROP
- Market: FIRST_INNING_RUNS, K, etc.
- Side: NRFI, OVER, UNDER
- Model version
- Confidence bucket

### 5. Make a prop-only hit/miss report

If you only want to see which pitcher props hit or missed:

```bash
python3 scripts/make_prop_results_report.py --date 2026-05-12
```

This writes:

```text
reports/2026-05-12_prop_results.md
reports/2026-05-12_prop_results.csv
```

### 6. Make an NRFI-only hit/miss report

If you only want to see which NRFI picks hit or missed:

```bash
python3 scripts/make_nrfi_results_report.py --date 2026-05-12
```

This writes:

```text
reports/2026-05-12_nrfi_results.md
reports/2026-05-12_nrfi_results.csv
```

### 7. Learn from it before tomorrow's picks

Update `data/model_notes/ace_logic_v1.md` or create a new model note such as `ace_logic_v2.md`.

Only promote repeatable lessons into the model. Examples:

- Penalize NRFI confidence when pitcher BB% is high and the opposing leadoff hitter has strong plate discipline.
- Penalize NRFI confidence in high-carry weather: 90°F+, Coors, or strong wind out.
- For high K lines, require both pitcher whiff strength and opponent chase/swing-and-miss support.
- Track line sensitivity, e.g. a pick may be good at 5.5 but bad at 6.5.

Then ask for the next slate with context like:

> Use the graded results and model notes in this repo, update the Ace Logic model, and make tomorrow's MLB NRFI and pitcher-prop picks.
