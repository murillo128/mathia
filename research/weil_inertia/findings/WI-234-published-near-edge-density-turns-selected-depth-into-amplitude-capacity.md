# WI-234 — published near-edge density turns selected depth into an amplitude-capacity barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE`.

WI-232 combines density-matched local Riemann--von Mangoldt counting with a near-edge zero-density theorem to bound the total first-harmonic capacity of any same-interval complementary screen. WI-233 independently strengthens the required cancellation amplitude by retaining the selected bow's radial weight

\[
A_T:=\frac1m\sum_{j=1}^m \cosh a_j^{\rm sel}\ge 1.
\]

These two facts combine without a new analytic estimate. The resulting invariant is not the selected population `m` alone but its **effective first-harmonic amplitude mass** `m A_T`. In the density-matched same-interval model, Bellotti's near-edge zero-density theorem forces

\[
\boxed{
 mA_T
 =O_A\!\left(
 T^{1/4}\exp\!\left[-\left(\frac1{96.1436}+o(1)\right)
 \frac{(\log T)^{1/3}}{(\log\log T)^{1/3}}
 \right]
 \right).
}
\tag{1}
\]

for every fixed `A>A_0`, where

\[
A_0=\frac1{48.0718}.
\]

Consequently a density-matched same-interval screen is impossible whenever the left side exceeds the right side by an unbounded factor. If a fixed positive fraction of the selected bow is already a fixed physical distance `delta_0>0` from the critical line, (1) becomes

\[
\boxed{
 m
 =O_{A,q}\!\left(
 T^{1/4-\delta_0/2}
 \exp\!\left[-\left(\frac1{96.1436}+o(1)\right)
 \frac{(\log T)^{1/3}}{(\log\log T)^{1/3}}
 \right]
 \right).
}
\tag{2}
\]

This closes the fixed-power equality left open in WI-233: when `delta_0+2 vartheta=1/2`, a bow of size `m=T^{vartheta}` times any factor larger than the displayed negative subpower correction cannot be screened inside its own density-matched interval. The result remains a local screen obstruction, not an RH proof and not a global zero-density theorem.

## 1. Evidence promotion: Bellotti's near-edge theorem is now published

WI-232 recorded Chiara Bellotti's theorem from arXiv:2508.02041v1 (4 Aug 2025) as a recent unrefereed preprint. That bibliographic status is now stale. The work has appeared as:

Chiara Bellotti, **A new zero-density estimate for $\zeta(s)$ and the error term in the prime number theorem**, *Bulletin of the London Mathematical Society* **58** (2026), no. 7, Paper e70442, DOI `10.1112/blms.70442`.

The publication metadata is independently corroborated by Johnston--Trudgian, *A round of Pintz to celebrate oscillations in sums*, *Analysis Mathematica* (published 10 Aug 2026), whose bibliography cites Bellotti as *Bull. London Math. Soc.* 58 (2026), Paper e70442.

The theorem surface in the accessible arXiv text states: if `A_0` is the Korobov--Vinogradov zero-free-region constant, `A>A_0` is fixed, and `T` is sufficiently large, then for every

\[
\sigma\ge
1-A(\log T)^{-2/3}(\log\log T)^{-1/3}
\]

one has

\[
\boxed{N(\sigma,T)=O_A(1).}
\tag{3}
\]

The same text records the current value `A_0=1/48.0718`. Its proof controls zeros in small disks through `\zeta'/\zeta`, so the multiplicity-sensitive interface audited in WI-232 is retained: repeated roots are charged with their multiplicities rather than silently converted to distinct ordinates.

Thus WI-232 equations (39)--(42) no longer need the status `RECENT-PREPRINT` merely because the theorem was unrefereed. Their analytic input is now peer-reviewed literature. This finding does not claim that peer review substitutes for checking hypotheses: the exact theorem statement, fixed-`A` quantifier, near-edge scale, and multiplicity interface are the pieces consumed below.

## 2. Same-interval screen capacity from the published theorem

Use the density-matched normalization of WI-232. Let

\[
\ell_0:=\log\frac{T_0}{2\pi},
\qquad
\Delta:=\frac{4\pi}{\ell_0},
\qquad
I=(T_0,T_0+m\Delta],
\qquad T_0\asymp T,
\tag{4}
\]

and let the selected bow contain `m` distinct right-half-plane off-line labels in `I`, together with their compulsory same-ordinate functional-equation mirrors. For `m=T^{vartheta+o(1)}` with `vartheta<1/2`, WI-232 proves from the local Riemann--von Mangoldt formula that every remaining same-interval label, including multiplicity, fits into a budget

\[
R=O(\log T).
\tag{5}
\]

For a zero at physical horizontal displacement `beta-1/2`, the first reciprocal harmonic has normalized radial depth

\[
a=\frac{(\beta-1/2)\ell_0}{2}.
\tag{6}
\]

Put

\[
S(T):=\frac{(\log T)^{1/3}}{(\log\log T)^{1/3}}.
\tag{7}
\]

Bellotti's published 2024 zero-free region, with `A_0=1/48.0718`, implies that every screen zero has

\[
a\le \frac{\ell_0}{4}-\left(\frac{A_0}{2}+o(1)\right)S(T).
\tag{8}
\]

Now fix any `A>A_0` and split the screen at

\[
\beta=1-A(\log T)^{-2/3}(\log\log T)^{-1/3}.
\]

By (3), only `O_A(1)` zero labels can lie on the deeper side. Each contributes first-harmonic modulus at most

\[
O\!\left(
T^{1/4}\exp[-(A_0/2+o(1))S(T)]
\right).
\tag{9}
\]

All remaining same-interval labels number only `O(log T)` by (5), and each has the stronger radial suppression `exp[-(A/2+o(1))S(T)]`. Since

\[
\log T\,\exp\!\left[-\frac{A-A_0}{2}S(T)\right]=o(1),
\tag{10}
\]

the entire complementary first-harmonic vector satisfies

\[
\boxed{
|S_1^{\rm comp}|
=O_A\!\left(
T^{1/4}\exp\!\left[-\left(\frac{A_0}{2}+o(1)\right)S(T)\right]
\right).
}
\tag{11}
\]

This is the capacity estimate already implicit in WI-232 equation (41), now promoted to a literature-backed input because (3) is published.

## 3. Retaining selected radial weight changes the controlled quantity from m to m A_T

WI-233 keeps the selected bow's exact first-harmonic amplitude instead of replacing every radial factor by one. Define

\[
a_j^{\rm sel}:=\frac{(\beta_j-1/2)\ell_0}{2},
\qquad
A_T:=\frac1m\sum_{j=1}^m\cosh a_j^{\rm sel}.
\tag{12}
\]

After rotating away the common vertical phase at the first reciprocal harmonic, the selected labels and their compulsory mirrors contribute exactly

\[
B_1=2mA_T.
\tag{13}
\]

Suppose a same-interval complement cancels this harmonic to error at most `eta m` with `eta=o(1)`. Then

\[
|S_1^{\rm comp}|
\ge 2mA_T-\eta m
=m(2A_T-\eta).
\tag{14}
\]

Because `A_T>=1`, the right side is at least `mA_T` for all sufficiently large `T`. Comparing (14) with (11) proves (1):

\[
\boxed{
 mA_T
 =O_A\!\left(
 T^{1/4}\exp\!\left[-\left(\frac{A_0}{2}+o(1)\right)S(T)\right]
 \right).
}
\tag{15}
\]

Since `A_0/2=1/96.1436`, this is exactly the announced amplitude-capacity law. The step is algebraic: no new zero-density, pair-correlation, mollifier, or prime-side estimate has been inserted.

Equivalently, with WI-233's effective selected depth

\[
\delta_{\rm eff}(T):=\frac{2}{\ell_0}\log A_T,
\tag{16}
\]

one obtains the necessary condition

\[
\log m+\frac{\delta_{\rm eff}(T)\ell_0}{2}
\le
\frac14\log T
-\left(\frac1{96.1436}+o(1)\right)S(T)+O_A(1).
\tag{17}
\]

This form makes the ledger explicit: selected population and selected horizontal defect consume the same finite near-edge screening capacity.

## 4. Positive-density selected depth closes the equality endpoint

Assume fixed `q>0` and `delta_0>0` such that at least `qm` selected right-half-plane labels satisfy

\[
\beta_j-\frac12\ge\delta_0.
\tag{18}
\]

Then (12) gives

\[
A_T
\ge q\cosh\!\left(\frac{\delta_0\ell_0}{2}\right)
\ge\frac q2\exp\!\left(\frac{\delta_0\ell_0}{2}\right).
\tag{19}
\]

Since `ell_0=log T+O(1)`, insertion into (15) proves (2). Therefore same-interval screening is impossible whenever

\[
\boxed{
\frac{m}{
T^{1/4-\delta_0/2}
\exp[-S(T)/96.1436]}
\longrightarrow\infty.
}
\tag{20}
\]

For a pure fixed-power size `m=T^{vartheta+o(1)}`, WI-233 already excludes `delta_0+2 vartheta>1/2` from strip width alone. Equation (20) resolves the previously delicate equality scale: if

\[
\delta_0+2\vartheta=\frac12,
\tag{21}
\]

then a density-matched bow with no compensating negative subpower shrinkage still exceeds the published near-edge screen capacity by `exp(S(T)/96.1436+o(S(T)))`. More generally, (20) excludes a whole subpower wedge below the fixed-power boundary.

This is stronger than simply applying the zero-free edge to the single deepest screen zero. The `O_A(1)` near-edge theorem controls the *number* of zeros capable of carrying almost maximal radial amplitude, while the local `O(log T)` budget controls the rest. The resulting statement is therefore a population-weighted capacity constraint.

## 5. What remains open

The hypotheses are essential. The conclusion applies only to a complementary population drawn from the same density-matched interval `I`. It does not show that the explicit-formula cancellation relevant to an actual zeta configuration must be local. Vertically remote zeros, the distinguished prime/source side, or a genuine spacing surplus remain possible escapes. WI-232 quantifies the spacing-surplus reservoir separately.

Nor does (15) identify the global uncertified complement with off-line zeros. Multiple critical-line zeros consume the local label budget but contribute only unit radial modulus; repeated off-line zeros are included with multiplicity in both the local budget and Bellotti's zero count. Pure proof slack in the global simple-critical proportion remains a separate category.

Finally, (20) is not yet an iterable defect-to-zero theorem. It gives a stronger obstruction to screening a selected positive-density radial population, but it does not manufacture the reciprocal-phase coherence or density-matched geometry needed to feed the same argument a second time. The live bootstrap question is now sharper: any local screen surviving near the boundary must either lose the selected radial mass, become nonlocal/source-driven, or exploit a spacing reservoir.

## 6. Prior art and novelty audit

The external ingredients are:

- Chiara Bellotti, *A new zero-density estimate for $\zeta(s)$ and the error term in the prime number theorem*, *Bull. London Math. Soc.* 58 (2026), no. 7, Paper e70442, DOI `10.1112/blms.70442`; arXiv:2508.02041. Role: published near-edge estimate (3).
- Chiara Bellotti, *Explicit bounds for the Riemann zeta function and a new zero-free region*, *J. Math. Anal. Appl.* 536:2 (2024), 128249, DOI `10.1016/j.jmaa.2024.128249`, arXiv:2306.10680. Role: published asymptotic Korobov--Vinogradov constant `A_0=1/48.0718` used in (8).
- Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, *J. Number Theory* 235 (2022), 219--241. Role inherited from WI-232: the explicit Riemann--von Mangoldt error giving the local `O(log T)` residual budget.
- James Maynard and Kyle Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, *IMRN* 2024:19 (2024), 12978--13014. Role inherited from WI-183/WI-232: the slowly varying bow geometry being stress-tested, not the screen-capacity conclusion.

Within `weil_inertia`, WI-232 already derives the **unweighted** near-edge screen capacity and originally recorded Bellotti's theorem at preprint evidence level. WI-233 independently derives the exact **selected radial amplitude** `mA_T` and its fixed-power inherited-depth tariff. The durable delta here is their conjunction after the bibliographic promotion of Bellotti's theorem: the screen must pay against `mA_T`, yielding (15), and positive-density selected depth shifts the published near-edge threshold to (20), including the equality endpoint (21).

A bounded external search around Bellotti near-edge zero density, Maynard--Pratt bows, reciprocal-harmonic screening, and radial-weighted zero populations located the sources above but no published statement of the amplitude-capacity laws (15) or (20). Absence of a search hit is not evidence of priority, and no priority claim is made.

## 7. Audit test and research consequence

This finding can be falsified by checking four interfaces only:

1. Bellotti's published theorem must have the fixed-`A>A_0` quantifier and the cumulative multiplicity-sensitive bound `N(sigma,T)=O_A(1)` at the stated Korobov--Vinogradov scale.
2. WI-232's density-matched interval must leave only `O(log T)` complementary labels and its zero-free-edge normalization must give (8).
3. The shallow/deep split must give the total first-harmonic capacity (11); in particular the `log T` shallow count must be absorbed by the fixed exponential gap `A-A_0` as in (10).
4. WI-233's selected first-harmonic amplitude must be exactly `2mA_T`, so cancellation to `o(m)` error forces the lower bound (14).

If these interfaces hold, (15) and (20) are exact consequences. The research consequence is a stricter target for any surviving local exceptional configuration: **near the quarter-scale boundary it must defeat a published near-edge amplitude capacity, not merely provide enough labels.** That moves the remaining work toward the genuinely live escapes in the canonical mandate—nonlocal screening, source-side cancellation, spacing surplus, or a mechanism that prevents the selected radial population from forming in the first place.