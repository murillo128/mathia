# MI-025 — Regular sampling separates aliasing, coupling, degree, sample count, timing provenance, differential jitter, and target quotient

**Evidence level:** supported by exact phase-pushforward classifications AF-279--AF-281 and finite-prefix separation/stability/timing theorems AF-282--AF-289 on the stated ordinary-Dirichlet coefficient/source classes.

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

The common-offset subclass supplies the matching obstruction, so full known-prefix coefficient recovery has the sharp worst-case scale `T_coefficient(N)=Theta(1/log N)`.

AF-288 shows why that coefficient scale must not be charged blindly to every downstream target. The common-clock action is exactly vertical translation of the Dirichlet series,

\[
F_{D_\tau a}(s)=F(s+i\tau),
\]

which preserves every zero real part. Therefore the RH yes/no predicate is constant on the whole common-clock orbit. Source restrictions can instead pin the gauge: two known nonzero reference coefficients at multiplicatively independent indices determine `tau` exactly, although irrational torus recurrence prevents a source-independent global inverse modulus on an unbounded clock range.

AF-289 sharpens the quotient geometry for **arbitrary rowwise timing error**. Define

\[
r(\tau)
:=\inf_{\sigma\in\mathbb R}\max_j|\tau_j-\sigma|
=\frac{\operatorname{osc}(\tau)}2.
\]

For any chosen common mode `sigma`, writing `tau_j=sigma+epsilon_j` gives the exact factorization

\[
\widetilde A(\tau)=\widetilde A(\varepsilon)G_\sigma.
\]

If the nominal frame has condition number at most `K`, its decoder satisfies

\[
\inf_{\sigma\in\mathbb R}
\frac{\|\widehat b-G_\sigma b\|_2}{\|b\|_2}
\le
K\left(e^{r(\tau)\log N}-1\right).
\]

The same `r(tau)` controls singular-value stability. Hence a common-clock-invariant target pays **no cost for the absolute center of the timing cloud**; the intrinsic timing resource is the row-to-row diameter. Fixed quotient-relative distortion is ensured by `osc(tau)=O(1/log N)` even when every `tau_j` is translated by an arbitrarily large common amount.

This does not make residual jitter free. Exact target invariance removes only the common mode. To convert the coefficient-orbit estimate into a downstream theorem, the target needs a stability modulus on the quotient. Exact zero ordinates, fixed-height windows, canonical phase data, or another observable that retains absolute imaginary origin must keep the corresponding provenance instead.

The reusable separation is therefore: **phase-fiber aliasing, retention of joint coupling, finite-prefix label spacing, stable mixed degree, raw sample count, frame conditioning, common-clock gauge, exact source anchoring, global calibration stability, differential jitter diameter, coefficient-orbit stability, and downstream target quotient are distinct resources**. A nuisance parameter can be costly for coefficient reconstruction, exactly identifiable from source provenance, and simultaneously irrelevant to an invariant target; residual perturbations must then be priced in the quotient geometry rather than in ambient coordinates.

**Boundary.** AF-282--AF-289 are finite known-support coefficient/frame theorems except for the exact Dirichlet-series vertical-translation identity. AF-289 gives a sufficient orbit-relative perturbation bound, not a target-specific modulus and not a sharp lower bound for differential jitter. RH invariance concerns horizontal zero geometry only. None of these results supplies analytic continuation, a new zero-free region, or a proof of RH.