# XF-009 — fixed-radius gap averages lose mesoscopic phase at leading order

**Status:** `EXACT-DERIVED` + `CROSS-LINE-OBSTRUCTION` + `LITERATURE-CALIBRATED`. XF-008 identifies the fixed-heat-time perturbative coordinate `X=h^2 j` and its Cauchy generator. The new result is that any translation-averaged statistic built from a fixed number of consecutive normalized gaps freezes, to leading order as `h -> 0`, to a pointwise functional of the mesoscopic profile. It therefore retains the value distribution of that profile but loses its mesoscopic ordering/phase. Explicit equimeasurable cosine profiles have identical leading fixed-radius gap statistics while relaxing at different order-one Cauchy rates. Thus a fixed-radius asymptotic constant is not enough to constrain fixed-time Xi-flow dynamics; the missing information first appears at `O(h^2)`, i.e. `O(log^-2 T)` at Xi height `T`, unless the observed block grows to the mesoscopic `Theta(h^-2)` scale.

## 1. Claim

Work in the perturbative lattice regime of XF-007--XF-008. Let the local mean gap be `h`, and put

\[
X_j=h^2j.
\]

To make the averaging argument exact on a compact domain, take a subsequence with

\[
h^2=\frac{2\pi}{N},
\qquad j\in\mathbb Z/N\mathbb Z,
\]

so `X_j` samples the torus `\mathbb T=\mathbb R/(2\pi\mathbb Z)` uniformly. Let `U in C^1(\mathbb T)` and choose `epsilon>0` small enough that

\[
1+\epsilon U(X)>0
\]

for all `X`. Consider the slowly modulated normalized gaps

\[
\frac{g_j}{h}=1+\epsilon U(X_j).
\tag{1}
\]

Fix an integer radius `r>=1`. For any Lipschitz local functional `F` on the compact range of the `r` consecutive normalized gaps, define its translation average

\[
A_h[F,U]
:=\frac1N\sum_{j=0}^{N-1}
F\!\left(
\frac{g_j}{h},\ldots,\frac{g_{j+r-1}}{h}
\right).
\tag{2}
\]

Then, with `r`, `F`, `epsilon`, and `U` fixed,

\[
\boxed{
A_h[F,U]
=
\frac1{2\pi}\int_0^{2\pi}
F\bigl(1+\epsilon U(X),\ldots,1+\epsilon U(X)\bigr)\,dX
+O(h^2).
}
\tag{3}
\]

The implicit constant depends only on the fixed stencil and regularity data. In particular, the leading term depends on `U` only through its pushforward value distribution under uniform `X`; it does **not** retain the mesoscopic ordering of those values.

This creates an explicit fixed-time ambiguity. For any positive integers `k` and `ell`, let

\[
U_k(X)=a\cos(kX),
\qquad
U_\ell(X)=a\cos(\ell X),
\qquad 0<a<1/\epsilon.
\tag{4}
\]

Uniform `X` makes `cos(kX)` and `cos(ell X)` identically distributed. Hence every fixed-radius functional in (2) has the same leading limit for `U_k` and `U_ell`.

But XF-008 gives the mesoscopic linearized Xi-flow equation

\[
\partial_t U=-2\pi|D_X|U.
\tag{5}
\]

Therefore

\[
U_k(t,X)=a e^{-2\pi k t}\cos(kX),
\tag{6}
\]

so two profiles that are indistinguishable by **all leading fixed-radius translation averages** can have different order-one decay over any fixed positive heat time.

Consequently a fixed-radius local statistic can constrain this fixed-time flow only if it carries information beyond its leading asymptotic constant: either a phase-sensitive `O(h^2)` term (or better), a radius growing with `h^{-2}`, or some genuinely nonlocal observable.

## 2. Frozen-stencil derivation

For `0<=m<r`, the mean-value theorem gives

\[
|U(X_{j+m})-U(X_j)|
\le m h^2\|U'\|_\infty.
\tag{7}
\]

If `L_F` is a Lipschitz constant for `F` on the compact gap range, replacing every argument in the `j`th stencil by its first value changes the summand by at most

\[
L_F\,\epsilon h^2\|U'\|_\infty
\sum_{m=0}^{r-1}m
=O_{F,U,r,\epsilon}(h^2).
\tag{8}
\]

Thus

\[
A_h[F,U]
=
\frac1N\sum_j
F\bigl(1+\epsilon U(X_j),\ldots,1+\epsilon U(X_j)\bigr)
+O(h^2).
\tag{9}
\]

The remaining summand is a fixed `C^1` periodic function of `X_j`; its uniform Riemann sum differs from its torus integral by `O(h^2)`. This proves (3).

The obstruction is therefore not probabilistic and does not depend on a particular pair-correlation conjecture. It is a deterministic scale-separation statement: on the coordinate `X=h^2j`, a fixed index stencil has physical `X`-diameter only `O(h^2)` and collapses to one point in the fixed-time limit.

The cosine comparison then isolates exactly what is lost. The maps `X -> kX mod 2pi` preserve Haar measure, so all `U_k` have the same one-point value distribution. Equation (3) cannot distinguish their mesoscopic frequencies at leading order. Equation (5), by contrast, distinguishes them through the multiplier `|k|`.

## 3. The missing information is on the same `h^2` scale as the Xi equilibrium defect

XF-008 already showed that an order-one mesoscopic profile can evolve over order-one heat time while

\[
R_j-2=O(h^2).
\tag{10}
\]

The present calculation shows the same scale from the observation side. Fixed-radius local averages freeze to their diagonal value with error `O(h^2)`. Thus the first phase-sensitive information available from a smooth fixed stencil lives at exactly the order at which the normalized exterior-field defect becomes visible.

At Xi height `T`,

\[
h_T\sim\frac{4\pi}{\log T},
\qquad
h_T^2\asymp\frac1{(\log T)^2}.
\tag{11}
\]

Therefore an upstream local-gap theorem that supplies only a limiting constant with an unspecified `o(1)` error is too coarse for this perturbative fixed-time mechanism. The error can be much larger than the `log^{-2}T` signal that distinguishes mesoscopic phase.

This does **not** say that every useful theorem must literally prove an expansion in powers of `h^2`. A growing block or a nonlocal statistic can retain the phase at leading order. But a genuinely fixed-radius translation average must resolve its first non-frozen correction quantitatively if it is to control the Cauchy field.

## 4. Consequence for the current `analytic_frontier` bridge

ANF-006 establishes an important unconditional fact: finite ordered-gap/block processing can beat the Montgomery--Taylor global pair-moment ceiling. ANF-008 then shows that, for its frozen `n_point_bound` architecture, the improving block size is forced by a finite certificate; the currently verified examples use fixed `n` and fixed finite `m` independent of `T`.

That information is valuable for simple-zero counting, but it does not automatically match the Xi-flow scale. Any continuous statistic extracted from a fixed block of normalized gaps is subject to the frozen-stencil law (3) on a smooth mesoscopic modulation. The stored ANF theorem provides a limiting simple-zero proportion, not a phase-sensitive `O(log^{-2}T)` asymptotic for a mesoscopic ordered field.

Hence the current ANF gain should **not** be imported into `xi_flow` merely because it retains more local configuration information than pair correlation. To become a fixed-time dynamical input, that architecture would need at least one of the following upgrades:

- a block/stencil whose index width grows on the `h_T^{-2}=Theta(log^2 T)` scale;
- a uniform expansion or error bound sharp enough to resolve the `O(h_T^2)=O(log^{-2}T)` non-frozen term;
- a separate mesoscopic/nonlocal observable that retains ordering or low-frequency phase before global averaging.

This is a scale-matching obstruction, not a criticism of the ANF simple-zero theorem. A fixed finite block can improve a global counting constant while still discarding the spatial information needed to propagate a gap field for fixed heat time.

## 5. Prior art and novelty boundary

The mathematical ingredients behind (3) are elementary frozen-coefficient/Riemann-sum analysis, and the equimeasurability of `cos(kX)` under Haar measure is classical. The Cauchy semigroup in (5) is already established in XF-008 and belongs to the standard half-Laplacian universality class. No novelty is claimed for any of those facts in isolation.

There is also a substantial literature on **mesoscopic statistics of zeta zeros**, which is relevant mainly because it confirms that mesoscopic information is a distinct analytic regime rather than a synonym for microscopic pair correlation. Paul Bourgade, *Mesoscopic fluctuations of the zeta zeros* (2010), studies mesoscopic zero fluctuations. Paul Bourgade and Jeffrey Kuan, *Strong Szego Asymptotics and Zeros of the Zeta-Function* (2014), obtain under RH Gaussian linear-statistic limits with covariance governed by an `H^{1/2}` norm; the appearance of the Fourier weight `|frequency|` is structurally consonant with the half-Laplacian generator in XF-008. Kenneth Maples and Brad Rodgers (2015) prove an unconditional central limit theorem for zero linear statistics with diverging variance, keeping off-line zeros within the formalism.

These papers are **not** evidence that an existing theorem already supplies the Xi-flow input isolated here. Their test-function regimes, hypotheses, observables, and scaling are different, and an ordered real-gap field cannot be assumed when RH is precisely what the flow is meant to constrain. They serve only as prior-art calibration that a mesoscopic analytic layer exists and that `H^{1/2}`-type frequency weights are natural in zeta-zero fluctuation theory.

The Mathia-specific contribution is the exact scale bridge: combining XF-008's `X=h^2j` Cauchy limit with a frozen-stencil expansion proves that leading fixed-radius ordered-gap averages lose the phase that controls fixed-time relaxation, and that the information first re-enters at the same `h^2~log^{-2}T` scale as the exterior-field defect.

## 6. Falsification boundary

This finding is deliberately perturbative and does not claim that every Xi zero configuration is a smooth modulation of an arithmetic lattice. Large Lehmer defects, collision cascades, singular profiles, and strongly nonlinear regimes may carry information that is visible to a fixed local statistic without an `h^2` penalty.

The synthetic gap sequences (1) are also not asserted to be complete zero sets of admissible Xi-type entire functions. Their role is narrower: they are exact profiles for the lattice linearization that governs the candidate perturbative fixed-time mechanism. A future Xi-specific theorem could rule out one of the compared profiles by arithmetic structure; that would be precisely the missing source-specific law rather than a failure of the scale calculation.

Nor does the result apply when the observation radius grows with height. If `r h^2` stays of order one, the stencil spans a nontrivial interval in `X` and no longer freezes to a point. Likewise, a fixed-radius theorem with a proved `O(h^2)` expansion may recover derivative/phase information from its subleading coefficient. Statistics retaining absolute spatial location rather than translation averaging also fall outside the equimeasurability argument.

## 7. Consequence for `xi_flow`

XF-007 and XF-008 established that fixed heat time lives on `Theta(log^2 T)` gaps and is propagated by a nonlocal Cauchy field. XF-009 now identifies the complementary **observation barrier**: leading fixed-radius local statistics collapse before they can see that field's phase.

A credible statistical route to an upper bound on `Lambda` must therefore match both sides of the scale. It must provide unconditional information that is real-rootedness-safe and either remains coherent across `Theta(log^2 T)` ordered gaps, or resolves fixed-block observables to roughly `log^{-2}T` precision with a demonstrable link to the Cauchy mode structure. A stronger asymptotic constant for a fixed local block, without such a rate or mesoscopic organization, can improve zero counting while still being dynamically too coarse.