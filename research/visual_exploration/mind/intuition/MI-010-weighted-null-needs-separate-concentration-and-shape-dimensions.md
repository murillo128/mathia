# MI-010 — Weighted prime-phase nulls have separate concentration, shape, and support-transfer regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer theorems VIS-173--VIS-177.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

VIS-173 shows that `D_2` and `D_4` control different parts of the matched Haar null. `D_2` governs leading concentration/effective support, while `D_4` governs whether standardized shape Gaussianizes. The bulk can concentrate while heavy low-prime coordinates keep a non-Gaussian law.

VIS-174 transfers fixed moments of the matched Haar law to deterministic continuous prime-log averaging. VIS-177 sharpens its elementary character geometry: after balancing positive and negative multiplicities, every nonzero character in the `k`th moment has

\[
|\lambda|\ge\frac1{2y^{\lfloor k/2\rfloor}},
\]

so the deterministic/Haar moment discrepancy is bounded at scale

\[
\frac{y^{\lfloor k/2\rfloor}D_2(y)^{k/2}}{H}
\]

up to the explicit fixed-order constant. The improvement is purely representational—unique factorization plus near-resonant balance—not a new zeta signal.

VIS-175 and VIS-176 turn the weight geometry into full weak-law regimes. In the square-summable phase, the limit is the infinite weighted Haar convolution under its transfer gate. In the Lindeberg phase, vanishing maximal normalized weight plus transfer of every fixed moment gives `N(0,1/8)`.

For prime-power weights `w_p=p^{-\alpha}`, `0<=\alpha<=1/2`, VIS-177 extends that Gaussian conclusion from the original polylogarithmic examples to every growing cutoff

\[
y(H)=H^{o(1)}.
\]

Indeed for fixed `k`, `D_2(y)<=y` and subpolynomial support makes the strengthened moment-transfer cost `o(1)`. Thus **all subpolynomial support growth remains inside the representation-matched Gaussian null** in the Lindeberg prime-power phase.

A source-sensitive statistic must therefore leave more than the square-summability phase boundary or the polylogarithmic support example. It must change sampling, use a source-bearing hybrid/zero variable, enter a rare/shrinking or unbounded functional class, reach a genuinely polynomial-or-faster support regime requiring new transfer theory, or otherwise leave the normalized additive prime torus.

**Boundary.** The moment order is fixed before the limit. VIS-177 does not control `k->infinity`, moving extremes, Gram/discrete sampling, hybrid variables, or a fixed positive-power support law `y=H^delta`. Failure of the current all-moment argument there is not evidence that the matched null fails.