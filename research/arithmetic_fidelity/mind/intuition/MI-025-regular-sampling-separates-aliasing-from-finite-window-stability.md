# MI-025 — Regular sampling separates aliasing, coupling, degree, sample count, timing provenance, and target quotient

**Evidence level:** supported by exact phase-pushforward classifications AF-279--AF-281 and finite-prefix separation/stability/timing theorems AF-282--AF-288 on the stated ordinary-Dirichlet coefficient/source classes.

For

\[
F(s)=\sum_n a_n n^{-s},\qquad \sum_n|a_n|n^{-c}<\infty,
\]

a single regular vertical lattice retains the phase `n -> e^{-ih log n}`, not `log n` itself. With

\[
R_h=\{r\in\mathbb Q_{>0}:h\log r\in2\pi\mathbb Z\},
\]

AF-279 gives exact coefficient fidelity for the complete bilateral lattice iff `R_h={1}`. AF-280 shows that finitely many **separate lattice marginals** cannot generally repair individually resonant quotients on the unrestricted weighted `ell^1` source class, even when their phase-label tuple is injective. AF-281 gives the complementary classification for genuinely **joint mixed samples**: exact fidelity is equivalent to joint phase injectivity, `cap_j R_(h_j)={1}`.

For the concrete two-prime repair

\[
h_2=2\pi/\log2,\qquad h_3=2\pi/\log3,
\]

AF-282 proves that the joint nodes of the known prefix `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 prices coefficient stability: if mixed indices range over `{0,...,L-1}^2`, a two-point test forces instability for `L=o(N)`, while `L=30N` admits a breadth-uniform stable inverse. AF-284--AF-285 separate degree from observation count: deterministic subset selection gives an unweighted linear-size family of raw complex mixed moments and rank forces at least `N` complex observations.

AF-286--AF-287 show that timing error itself splits into different information classes. A common offset `tau` factors exactly as

\[
\widetilde y=A D_\tau b,
\qquad
D_\tau=\operatorname{diag}(n^{-i\tau})_{n\le N},
\]

so an arbitrary complex source is identifiable only modulo the coefficient gauge. Independent rowwise jitter is not a gauge, but after selecting an unweighted `O(N)` raw subframe with bounded condition number its perturbation obeys

\[
\|\widetilde A-A\|\le\|A\|\bigl(e^{T\log N}-1\bigr).
\]

The common-offset subclass supplies the matching obstruction, so full known-prefix coefficient recovery has the sharp worst-case scale

\[
T_{\rm coefficient}(N)=\Theta(1/\log N)
\]

for both common-mode and arbitrary rowwise jitter.

AF-288 shows why that coefficient scale must not be charged blindly to every downstream target. The common-clock action is exactly vertical translation of the Dirichlet series:

\[
F_{D_\tau a}(s)=F(s+i\tau).
\]

It rigidly translates the zero/pole divisor in imaginary direction and preserves every zero real part. Therefore the RH yes/no predicate is constant on the whole common-clock orbit: **an exact vertically translated zeta carrier retains the RH discriminator without recovering the clock origin**.

Source restrictions can instead pin the gauge. If two known nonzero reference coefficients occur at multiplicatively independent indices `m,n`, equality of their phase ratios forces `tau` uniquely; the canonical zeta anchors `m=2,n=3` suffice. Exact identifiability is nevertheless not global robust calibration. Irrational torus recurrence gives `|tau_j|->infinity` with both anchor phases returning arbitrarily near their initial values, so no uniform inverse modulus exists on all of `R`. On a bounded clock interval, one anchor already gives a local inverse-Lipschitz chart.

The reusable separation is therefore: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw sample count, frame conditioning, common-clock gauge, exact source anchoring, global calibration stability, independent jitter, and downstream target quotient are distinct resources**. A nuisance parameter can be costly for coefficient reconstruction, exactly identifiable from source provenance, and simultaneously irrelevant to an invariant target.

**Boundary.** AF-282--AF-288 are finite known-support coefficient results except for the exact Dirichlet-series vertical-translation identity. The source-anchor statement assumes known nonzero phases at multiplicatively independent indices. RH invariance concerns horizontal zero geometry only; exact ordinates, fixed-height windows, canonical completed-zeta normalization, and independent rowwise perturbations are not gauge-invariant. None of these results supplies analytic continuation, a new zero-free region, or a proof of RH.