# Hitter Props v1 Notes

Hitter props are added starting with the May 15 slate.

## Initial rules

1. Prefer total bases over home-run-only props because total bases have more paths to cash.
2. Use hitter-friendly environments that are bad for NRFI as positive inputs for hitter props: Coors, Sutter Health Park, heat, wind out, and high game totals.
3. Prioritize batting-order position. Leadoff/top-three hitters get more plate appearances and more reliable volume.
4. For total bases, look for contact plus power: strong AVG/SLG/ISO profile, platoon edge, and weak opposing starter contact quality.
5. Home-run props are value/lottery picks only. Keep confidence lower unless the implied probability is clearly below the projection.
6. Track hitter props under `type=PROP` with markets like `TB` for total bases and `HR` for home runs, so the existing grading scripts work.

## May 15 implementation

The first hitter card focuses on total bases in Coors/Sutter/high-run contexts and one small-stake HR value longshot. These are intentionally separate from NRFI logic: the same environment can be a pass for NRFI and a target for hitter props.
