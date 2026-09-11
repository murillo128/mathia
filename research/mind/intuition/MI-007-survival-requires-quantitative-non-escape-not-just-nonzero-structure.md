# MI-007 — Weak disappearance can be drift, controlled escape, or canonical residual convergence

**Evidence level:** supported; the three mechanisms below are distinguished and no universal equivalence is claimed.

For fixed `N` and `q` in the invertible residue class `r`, choose `1<=a<N` with `ar=1 mod N` and put `k_q=(aq-1)/N`. The original refined Prime-Circle coordinate is exactly

\[
Z_q=R_1\otimes S_q^{-k_q},\qquad k_q/q\to a/N.
\]

A fixed degree not divisible by `N` moves a localized packet by order `q` and is weakly invisible in the old packet window. Its norm has not been lost. Following the moving window returns the channel to the already-classified CRT quotient algebra, so this is **ballistic drift plus recentering**, not decay ([PC-239](../../prime_circle/findings/PC-239-original-coordinate-bezout-winding-is-ballistic-and-collapses-to-shift-calculus.md)).

For the flute's fixed physical high-pass spaces, [PF-292](../../prime_flute/findings/PF-292-fixed-physical-high-pass-forces-diverging-local-frequency-floor.md) instead gives a quantitative high-pass inequality. Uniform positive-Sobolev control forces the high projection to vanish, and [PF-296](../../prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md) supplies that control for canonical source synthesis under a bounded weighted source moment. This is **escape exclusion by an explicit regularity budget**; growing row count alone is insufficient.

Nyman--Beurling supplies a third mechanism. For the canonical nested finite-section residuals, [NB-057](../../nyman_beurling/findings/NB-057-canonical-finite-residuals-cannot-sustain-large-shift-semigroup-leakage.md) gives

\[
h_N=h_*+a_N,\qquad \|a_N\|^2=\delta_N^2-\delta_*^2\to0.
\]

The limiting defect is exactly blind on the integer-log grid and vectorwise blind at late off-grid shifts; the strong convergence of the *canonical* residual sequence upgrades this to joint large-section/large-shift decay. Thus no choice `t_N->infinity` can preserve a positive single-shift projection merely by exploiting nonuniform continuity on the unit sphere. This is **canonical residual convergence**, not a uniform operator-norm theorem.

These mechanisms have different conclusions. In Prime Circle the mass survives but is located by recentering and then classicalized. In Prime Flute an explicit family bound excludes high-frequency escape. In Nyman--Beurling every late individual shifted block becomes invisible to the canonical moving residual, while the closed span of many individually weak late directions can still remain target-bearing.

The reusable rule is quantitative: a weak limit by itself says little. One must identify the permitted moving frame, the family norm/regularity budget, or the canonical convergence law of the actual target residual. Even then, one-column disappearance does not imply collective-span disappearance.
