# WP-230 — Faithful metric reweighting cannot orient the Bost–Connes Weil defect; nonfaithful repair is support selection

**Status:** `EXACT-DERIVED + BOST-CONNES-CRITICAL-GRAM + FAITHFUL-POSITIVE-METRIC + UNBOUNDED-CONGRUENCE + DENSE-RANGE-INERTIA + MODULAR-WEIGHT-BOUNDARY + SUPPORT-COMPRESSION-CLASSIFICATION + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-229` closes scalar singular traces on the exact critical Bost--Connes carrier and leaves genuinely nontracial/operator-valued modular weighting as one possible category change. There is an immediate version of that escape which can now be closed exactly: **changing only the positive metric in which the already-formed finite Weil defect is tested cannot change its sign if the metric is faithful**, even when the metric is unbounded, non-diagonal, and need not commute with the Bost--Connes Hamiltonian.

Let `F` be any nonempty finite prime set and let `W_F` be the source-forced critical finite-place defect of `WP-216`/`WP-223` on

\[
\mathcal H_F=\ell^2(\mathbb N_0^F).
\]

Let `G\ge0` be an arbitrary positive self-adjoint operator and form the metric-weighted quadratic form

\[
q_G[x]
=
\langle G^{1/2}x,\,W_F G^{1/2}x\rangle,
\qquad
x\in\operatorname{Dom}G^{1/2}.
\tag{1}
\]

Write

\[
M_G=\overline{\operatorname{Ran}G^{1/2}}
=(\ker G)^{\perp}.
\tag{2}
\]

Then there is an exact classification:

\[
\boxed{
q_G\ge0
\quad\Longleftrightarrow\quad
P_{M_G}W_FP_{M_G}\succeq0
\text{ on }M_G.
}
\tag{3}
\]

In particular, if `G` is **faithful** (`ker G=0`), then `M_G=H_F`. Since `W_F` is indefinite,

\[
\boxed{
\ker G=0
\quad\Longrightarrow\quad
q_G\text{ takes both signs.}
}
\tag{4}
\]

Thus no faithful positive density, metric operator, Radon--Nikodym derivative, Gibbs-like weight, or unbounded modular reweighting can orient `W_F` merely by inserting the same positive metric on the two sides. The conclusion requires no bounded inverse, no spectral gap of `G`, no commutation with the Hamiltonian, and no time-covariance hypothesis.

If `G` is nonfaithful, equation (3) shows that **all sign-changing power comes from its support projection**, not from the positive weights inside that support. Such a repair is therefore a compression/subspace-selection mechanism in disguise. That returns directly to the source-selection problem isolated by `WP-222`: a support can be chosen to program sign unless its origin is forced independently by the arithmetic geometry.

This does not rule out a genuinely operator-valued modular correspondence, an asymmetric left/right spatial construction, a noncongruential completely positive operation, a finite--archimedean coupling formed before the defect, or the semilocal compression/quantized-calculus mechanisms of Connes--Consani. It closes the narrower but natural post-`WP-229` shortcut in which the missing sign is supposed to arise just by replacing the Hilbert metric or inserting a faithful positive modular density around the same Bost--Connes defect.

## 1. The finite critical defect has strict directions of both signs

From `WP-223`, in the canonical exponent basis `e_\alpha`, the finite critical defect has zero diagonal and prime-axis entries

\[
\langle e_\alpha,W_Fe_\beta\rangle
=
-(\log p)p^{-|\alpha_p-\beta_p|/2}
\tag{5}
\]

whenever `alpha` and `beta` differ only in the `p` coordinate. Choose such a pair and write

\[
c=(\log p)p^{-|\alpha_p-\beta_p|/2}>0.
\]

Then

\[
\langle e_\alpha+e_\beta,
W_F(e_\alpha+e_\beta)\rangle=-2c<0,
\tag{6}
\]

while

\[
\langle e_\alpha-e_\beta,
W_F(e_\alpha-e_\beta)\rangle=2c>0.
\tag{7}
\]

So the open cones

\[
\mathcal C_-=
\{y:\langle y,W_Fy\rangle<0\},
\qquad
\mathcal C_+=
\{y:\langle y,W_Fy\rangle>0\}
\tag{8}
\]

are both nonempty. They are norm-open because `W_F` is bounded.

The proof below uses only this strict indefiniteness and boundedness; the detailed Poisson kernel is needed only to establish that the exact Mathia source object satisfies those hypotheses.

## 2. Dense-range congruence cannot erase either sign

Let `G\ge0` be self-adjoint, possibly unbounded. The standard range identity gives

\[
\overline{\operatorname{Ran}G^{1/2}}
=(\ker G^{1/2})^\perp
=(\ker G)^\perp
=M_G.
\tag{9}
\]

Suppose first that `G` is faithful. Then `Ran G^{1/2}` is dense in `H_F`. Since both cones in (8) are nonempty and open, density gives vectors `x_\pm\in Dom G^{1/2}` such that

\[
G^{1/2}x_-\in\mathcal C_-,
\qquad
G^{1/2}x_+\in\mathcal C_+.
\tag{10}
\]

Therefore

\[
q_G[x_-]<0,
\qquad
q_G[x_+]>0.
\tag{11}
\]

This proves (4). Notice what is *not* used: `G` need not be bounded, invertible in the bounded sense, diagonal, a function of the Hamiltonian, or compatible with the Bost--Connes time action. Faithfulness alone gives dense range, and dense range is enough because the positive and negative cones are open.

Finite-dimensional Sylvester inertia is the familiar special case: an invertible congruence preserves the full inertia of a Hermitian form. Equation (11) is the exact infinite-dimensional statement needed here; it retains the two strict signs even when the positive congruence has unbounded condition number or spectrum accumulating at zero.

## 3. Nonfaithful metrics reduce exactly to support compression

The same argument gives more than the faithful no-go. Let `G` now have arbitrary kernel and let `M=M_G`.

If

\[
P_MW_FP_M\succeq0
\quad\text{on }M,
\tag{12}
\]

then `G^{1/2}x\in M` for every `x\in Dom G^{1/2}`, so immediately

\[
q_G[x]\ge0.
\tag{13}
\]

Conversely, suppose `q_G\ge0`. Then

\[
\langle y,W_Fy\rangle\ge0
\qquad
(y\in\operatorname{Ran}G^{1/2}).
\tag{14}
\]

The range is dense in `M` by definition, and the bounded quadratic form of `W_F` is norm-continuous. Taking limits in (14) gives

\[
\langle y,W_Fy\rangle\ge0
\qquad(y\in M),
\tag{15}
\]

which is exactly (12). Hence (3) follows.

This classification separates two mechanisms which can otherwise look similar:

1. changing the **metric values** on a fixed support cannot repair the sign;
2. changing the **support** can repair the sign, but only by selecting a subspace on which the original form was already nonnegative.

For the Bost--Connes direction this is important because `WP-222` already demonstrates that finite source quotients can be chosen with either sign. A nonfaithful metric therefore does not create a new positivity theorem by itself; its support projection becomes the entire unexplained datum.

## 4. Consequence for modular and semifinite weighting

The literature on metric operators and modular Radon--Nikodym theory makes positive self-adjoint densities a canonical way to change Hilbert geometry or weights. Jean-Pierre Antoine and Camillo Trapani, *Partial inner product spaces, metric operators and generalized hermiticity*, J. Phys. A 46 (2013), 025204, DOI `10.1088/1751-8113/46/2/025204`, develops bounded and unbounded metric operators and the Hilbert scales they generate. Stefaan Vaes, *A Radon-Nikodym theorem for von Neumann algebras*, J. Operator Theory 46 (2001), 477--489, arXiv `math/9811122`, constructs normal semifinite faithful weights by inserting a strictly positive affiliated operator `delta` in the form

\[
\phi_\delta(\,\cdot\,)
=
\phi(\delta^{1/2}(\,\cdot\,)\delta^{1/2})
\tag{16}
\]

under the corresponding modular hypotheses, extending the Pedersen--Takesaki framework.

The present result is not a new theorem about metric operators or Radon--Nikodym derivatives. Its Mathia-specific content is a **category boundary** for the exact critical Bost--Connes defect: whenever a proposed nontracial/modular completion acts on `W_F` only through a faithful positive density congruence, the strict negative directions survive by (11). If the density ceases to be faithful, the proposal has become support selection by (3), and that support needs an independent source law.

A bounded literature search around unbounded metric operators, indefinite forms, normal semifinite weights, Bost--Connes systems, and Weil positivity did not expose a published claim identifying this particular Bost--Connes critical defect with a metric-reweighting obstruction. The abstract mechanism is classical and is therefore **not** claimed as novel operator theory.

## 5. Matched controls and what remains open

The obstruction is arithmetic-independent once an indefinite bounded defect is present. Replacing the prime labels or Poisson radii by any matched hollow weighted graph with at least one surviving edge gives the same faithful-metric no-go. This is a useful control: positivity arising solely from a faithful reweighting could not distinguish the Riemann arithmetic from such a generic indefinite source.

The result also explains why the known semilocal Connes--Consani direction is not captured by this shortcut. Their archimedean positivity mechanism uses a **compression of the scaling action onto a source-defined orthogonal complement**, not a faithful metric congruence of an already-fixed finite defect. The broader Connes--Consani--Marcolli adelic/cohomological program likewise changes the global object and pairing before the desired sign statement. Those are genuine category changes and remain outside (3).

After `WP-229` and the present no-go, a surviving nontracial/operator-valued route must therefore do at least one of the following before final positivity is asserted: introduce a source-forced nontrivial support/correspondence, use asymmetric or genuinely modular left--right data rather than a single positive density, actively couple finite and archimedean sectors, or replace the finite defect by a new global operator whose positivity theorem is independent of the Weil target. Merely changing the faithful Hilbert metric around `W_F` cannot supply the missing sign.