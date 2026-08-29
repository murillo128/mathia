# WI-012 — an exact global Fenchel dual removes the fixed-block boundary loss

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-IDENTITY`. The spectral Fenchel-conjugacy step is classical convex matrix analysis (A. S. Lewis, 1996). The specific connection-Laplacian witness and its proposed zeta/Bellman use already appear in `tawanerguo-cn/zeta-simple-zeros`, `archive/original/GLOBAL_SPECTRAL_DUAL.md`; no novelty claim is made for that mechanism. The new Mathia contribution here is the independent audit below and the exact identification of WI-011's pinched-block assembly as a restricted feasible class inside this global dual.

## 1. Precise claim

Let `M` be any finite positive-semidefinite Hermitian matrix with unit diagonal, and let

\[
\Psi(t)=
\begin{cases}
(t-1)^2,&0\le t\le2,\\
2t-3,&t\ge2.
\end{cases}
\]

The Gram defect used in WI-009--WI-011,

\[
\mathcal D(M)=\operatorname{tr}\Psi(M),
\]

has the exact global variational representation

\[
\boxed{
\mathcal D(M)
=
\sup_{H=H^*,\ H\preceq2I}
\left[
\operatorname{tr}H(M-I)-\frac14\operatorname{tr}H^2
\right].
}
\tag{1}
\]

Consequently, fixed-block pinching is not an intrinsic part of the stability method. It is exactly what results from restricting the admissible test matrix `H` in (1) to be block diagonal. Cross-block entries of `H` are therefore a mathematically legitimate source of support-one improvement that WI-011 necessarily discards.

A particularly useful globally coupled feasible family is obtained from a connection Laplacian. If `E` is a graph on the indices, `q_ij>=0`,

\[
a_{ij}=|M_{ij}|,
\qquad
\omega_{ij}=M_{ij}/|M_{ij}|
\]

for nonzero entries, and

\[
d_i=\sum_{j:\{i,j\}\in E}q_{ij},
\]

then, whenever `d_i<=2` for every vertex,

\[
\boxed{
\mathcal D(M)
\ge
\sum_{\{i,j\}\in E}
\left(2q_{ij}a_{ij}-\frac12q_{ij}^2\right).
}
\tag{2}
\]

For fixed `E`, maximizing the right side subject to the vertex capacities is a concave capacitated fractional-matching problem, with exact convex dual

\[
\boxed{
\min_{\lambda_i\ge0}
\left[
2\sum_i\lambda_i
+
\frac12\sum_{\{i,j\}\in E}
(2a_{ij}-\lambda_i-\lambda_j)_+^2
\right].
}
\tag{3}
\]

Equations (1)--(3) turn the next support-one problem from a vague "better global assembly" into a precise global optimization problem on the actual Montgomery--Taylor overlaps.

## 2. Independent derivation of the spectral dual

For every scalar `t>=0`,

\[
\Psi(t)=\sup_{h\le2}
\left(h(t-1)-\frac{h^2}{4}\right).
\tag{4}
\]

If `0<=t<=2`, the unconstrained maximizer is `h=2(t-1)<=2` and the value is `(t-1)^2`. If `t>=2`, the constraint is active at `h=2` and the value is `2t-3`.

Classical Fenchel conjugacy for spectral functions on Hermitian matrices then lifts (4) to (1). Here the lift can also be checked directly: diagonalize `M`; for fixed eigenvalues of `H`, von Neumann's trace inequality aligns an optimizer with the eigenbasis of `M`, and the scalar problem separates coordinatewise. Equivalently, the optimizer is the spectral clipping

\[
H_*=\min\bigl(2I,\,2(M-I)\bigr)
\]

in functional calculus.

This confirms that no hidden commutativity assumption is being introduced in (1).

## 3. Connection-Laplacian witness

For each edge define the rank-one positive-semidefinite Hermitian contribution whose diagonal entries at `i,j` are `q_ij` and whose off-diagonal entries are `-q_ij omega_ij` and its conjugate. Their sum is a connection Laplacian `L(q)>=0` with diagonal `d_i`.

Set

\[
S=\operatorname{diag}(\min(d_i,2)),
\qquad
H=S-L(q).
\]

Then

\[
2I-H=(2I-S)+L(q)\succeq0,
\]

so `H` is feasible in (1). Since `M-I` has zero diagonal, every edge contributes exactly `2q_ij a_ij` to `tr H(M-I)`. Also

\[
\operatorname{tr}H^2
=
2\sum_Eq_{ij}^2
+
\sum_i(d_i-2)_+^2.
\]

Substitution into (1) gives the more general exact lower witness

\[
\mathcal D(M)
\ge
2\sum_Eq_{ij}a_{ij}
-
\frac12\sum_Eq_{ij}^2
-
\frac14\sum_i(d_i-2)_+^2.
\tag{5}
\]

Under the hard capacities `d_i<=2`, the last term vanishes and (2) follows.

For (3), attach multipliers `lambda_i>=0` to `2-d_i`. The edgewise supremum over `q_ij>=0` is

\[
\sup_{q\ge0}
\left[(2a_{ij}-\lambda_i-\lambda_j)q-\frac12q^2\right]
=
\frac12(2a_{ij}-\lambda_i-\lambda_j)_+^2.
\]

Slater's condition is trivial (`q=0` is strictly feasible), so strong duality gives (3).

## 4. WI-011 pinching is exactly a restricted Fenchel witness

Let the indices be partitioned into blocks `B_r`. Restrict (1) to block-diagonal matrices

\[
H=\bigoplus_r H_r,
\qquad H_r\preceq2I_{B_r}.
\]

The objective then decomposes exactly:

\[
\operatorname{tr}H(M-I)-\frac14\operatorname{tr}H^2
=
\sum_r
\left[
\operatorname{tr}H_r(M_{B_r}-I)-\frac14\operatorname{tr}H_r^2
\right].
\]

Optimizing each block independently gives

\[
\boxed{
\mathcal D(M)\ge\sum_r\mathcal D(M_{B_r}).
}
\tag{6}
\]

This is exactly the pinching inequality used by WI-011. Thus its block-boundary loss has a precise variational meaning: all cross-boundary coordinates of the globally optimal `H_*` have been forbidden.

Averaging over shifts of a fixed block partition reduces the boundary loss but does not restore those cross-boundary couplings. Likewise, convexly mixing several fixed block sizes remains a convex mixture of restricted witnesses and does not reproduce the unrestricted supremum in (1).

## 5. Application to the ordered simple-zero Gram matrix

For the retained simple critical zeros, the limiting Montgomery--Taylor Gram matrix has

\[
M_{ij}\approx k_{\rm MT}(y_i-y_j),
\qquad
a_{ij}\approx|k_{\rm MT}(y_i-y_j)|,
\]

on bounded normalized spans. Choose a finite index range `R` and connect `i,j` when `|i-j|<=R`. Any local rule producing feasible capacities `q_ij` turns (2) into a translation-covariant finite-range potential in the consecutive gaps.

This means the asymptotic lower-bound problem can be posed as a one-dimensional ground-state problem rather than a sequence of disjoint finite blocks. If `V` is the resulting finite-range potential and `U` is a bounded function of the boundary state satisfying a Bellman/subaction inequality

\[
V(g_i,\ldots,g_{i+R-1})+\beta g_i
+U(g_{i+1},\ldots)-U(g_i,\ldots,g_{i+R-2})
\ge C,
\tag{7}
\]

then summing (7) telescopes `U` and leaves only `O(1)` endpoint loss. A directed interval certificate for (7), together with the already audited Montgomery--Taylor kernel passage and the appropriate pressure/tail ledger, would therefore give a genuinely global support-one improvement without introducing a new prime-side moment.

The public `tawanerguo-cn/zeta-simple-zeros` archive already proposes precisely this connection-Laplacian/Fenchel/Bellman route. Its later Bellman-coboundary certificate demonstrates that subaction certification is computationally viable, although its larger numerical bounds still sit below Mathia's established-evidence tier because their finite certificates and full analytic splice are not independently formalized here.

## 6. Why this materially changes the search space

WI-010 showed that the old `n_point_bound` bridge strangles the gain as the local point count grows. WI-011 showed that replacing that bridge by a better trace--energy block envelope recovers some slack. Equation (1) identifies the next loss exactly:

\[
\boxed{
\text{full spectral defect}
\;\supsetneq\;
\text{best block-diagonal Fenchel witness}
\;\supseteq\;
\text{WI-011 block certificate}.
}
\]

The next serious optimization target is therefore not merely a larger local point certificate or a different fixed block length. It is a globally feasible `H`, equivalently a cross-boundary capacitated edge witness, whose average reward can be certified by a Bellman subaction.

This route stays entirely inside the same bandwidth-one Gram geometry. It therefore does not pay the support-`>1` arithmetic cost identified by WI-007 and does not suffer the short-bandwidth rank loss of WI-008.

## 7. Prior art and novelty audit

The spectral-function conjugacy itself is classical. A. S. Lewis, *Convex Analysis on the Hermitian Matrices*, SIAM J. Optim. 6 (1996), 164--177, gives the general Fenchel-conjugacy framework for convex spectral functions on Hermitian matrices.

The specific formulas (1), (5), the hard-capacity form (2), its dual (3), and the suggested finite-range/Bellman application to the zeta Gram matrix are explicitly present in the public `tawanerguo-cn/zeta-simple-zeros` research archive. Therefore Mathia must treat the mechanism as prior art, not a new discovery.

The independent audit above matters because it verifies the algebraic bridge without relying on the repository's larger numerical headline. The exact mechanism survives even if every unreviewed finite certificate in that repository is discarded.

## 8. Boundaries and falsification tests

This finding does **not** prove a new numerical proportion. To produce one, a concrete finite-range witness must still be paired with a rigorously certified ground-state constant and with the finite-`T` kernel/tail bookkeeping.

It also does not distinguish multiple critical-line zeros from screened simple off-line pairs. The functional `D(M)` only strengthens the accounting of the simple critical-line Gram contribution, so the WI-005--WI-007 screening obstruction remains intact on the exceptional block.

The connection-Laplacian family is a lower-witness family inside the exact Fenchel dual, not a proof that every global optimizer has this form. Failure of a particular edge rule or Bellman ansatz therefore would not refute (1).

A decisive implementation/audit test is now finite and explicit: choose a small range `R`, construct a capacity-feasible local `q` rule, derive the exact potential `V`, and certify a Bellman inequality of the form (7) with directed intervals. If its resulting global defect coefficient cannot beat WI-011, that rules out that witness family without touching the exact global dual itself.

## 9. Consequence for the research line

The vague post-WI-011 goal of a "global variational formulation" already has an exact prior-art realization. The fixed-block boundary is not a fundamental property of the Montgomery--Taylor/inertia method; it is an artifact of restricting the Fenchel witness.

Accordingly, the highest-value support-one direction is now:

\[
\boxed{
\text{Montgomery--Taylor Gram}
\to
\text{exact Fenchel dual}
\to
\text{capacity-feasible cross-boundary edges}
\to
\text{Bellman ground-state certificate}.
}
\]

This is a materially different route from increasing the local point count, and it is precise enough to be attacked or falsified without new arithmetic input.
