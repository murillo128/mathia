# MI-010 — Weighted prime-phase nulls have separate concentration, shape, and transfer dimensions

**Evidence level:** supported by the weighted-Haar calculation of VIS-173 and the deterministic prime-log moment transfer of VIS-174; no full-distribution or optimal discrepancy theorem is claimed.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

VIS-173 shows that these control different parts of the matched Haar null. `D_2` governs leading concentration/effective support, while `D_4` governs whether the first standardized correction Gaussianizes. One can have `D_2 -> infinity` while `D_4` stays finite, so the bulk concentrates but heavy low-prime coordinates leave a persistent non-Gaussian fingerprint.

VIS-174 now shows that this fingerprint can survive **deterministic prime-log averaging** without becoming source evidence. For the normalized weighted prime-phase observable over `p<=y`, every fixed moment order `k` satisfies

\[
\left|\operatorname{Av}_{[T,T+H]} S_y(t)^k
-\mathbb E(S_y^{\rm Haar})^k\right|
\le
2^{2-k}\frac{y^k D_2(y)^{k/2}}{H}.
\]

Thus fixed moments transfer whenever `y^kD_2(y)^{k/2}/H -> 0`. The estimate is uniform in the starting height and follows from exact prime-log character resonance plus the elementary gap `|log(a/b)| \gtrsim y^{-k}`.

The taper `w_p=1/p` is the decisive calibration. Here

\[
D_2(y)\asymp (\log\log y)^2,
\qquad
D_4(y)\to \frac{P(2)^2}{P(4)}<\infty.
\]

For any polylogarithmic cutoff `y=(\log H)^A`, every preassigned fixed moment transfers to the matched weighted Haar law, while the fourth cumulant stays nonzero. Persistent non-Gaussian low-prime shape in the actual continuous prime-log orbit is therefore a **representation-matched null effect** in this regime, not a discriminator.

A source-sensitive statistic must now beat three separate budgets: concentration through `D_2`, null-shape persistence through `D_4` or the exact weighted Haar law, and deterministic transfer through the observation condition `H \gg y^kD_2^{k/2}` at the declared moment order. Rare collisions and full-distribution approximation remain separate gates.

**Boundary.** VIS-174 treats continuous vertical averaging and fixed `k`. It does not cover Gram-point/discrete sampling, growing moment order, rare tails, total variation, or observables containing additional zero/hybrid factors.