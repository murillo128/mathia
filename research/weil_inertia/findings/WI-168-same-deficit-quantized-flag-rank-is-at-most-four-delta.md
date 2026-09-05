# WI-168 — any same-deficit quantized flag extension has rank at most four times the Lamzouri deficit

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + BARRIER`. WI-167 shows that a nonzero extra integer-depth flag step cannot be charged on an arbitrarily shallow isolated off-line pair because its Hilbert--Schmidt norm has a fixed floor while Lamzouri's complete deficit tends to zero. The same obstruction has a global quantitative form that does not use confluence: **any refinement of the canonical Lamzouri target by nested projection levels, if it is controlled by the same finite deficit and no new source budget, has total added rank at most `4 Delta`.** More precisely, if the added depth operator is `J`, then

\[
\boxed{
\Delta\ge \frac14\|J\|_{\rm HS}^2
=\frac14\sum_{q\ge1}q^2\dim E_q
\ge\frac14\operatorname{rank}J.
}
\]

Here `E_q` is the graded subspace on which `J` has integer depth `q`. Thus a nonzero same-deficit flag refinement already requires `Delta >= 1/4`; an added depth `q` on one direction costs at least `q^2/4`; and along any family with `Delta=o(N)` the added quantized rank must be `o(N)`. A macroscopic interaction layer therefore cannot be created by merely repackaging WI-137's existing deficit. It needs a genuinely new source inequality or a different, non-quantized information carrier. No unconditional zero proportion changes in this finding.

## 1. Exact source interface

Use the notation of WI-137, reconstructed from Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1, Proposition 2.1. Let

\[
\mathcal D=P_U+P_V,
\qquad
X:=\mathcal A_F-\mathcal D.
\]

WI-137 proves the exact identity

\[
\boxed{
\Delta=\|X\|_{\rm HS}^2+L,
\qquad
L:=2B+4H_V\ge0.
}
\tag{1}
\]

This identity is stronger than the published scalar inequality because it keeps the full off-diagonal Bessel mass and completes all three Lamzouri spectral blocks around the canonical `2/1/0` target.

Now keep the original retained levels `U subset V` and add finitely many source-derived nested flag levels. Their natural depth correction has the form

\[
J=\sum_{a=1}^r P_a\succeq0,
\qquad
\mathcal D'=\mathcal D+J,
\tag{2}
\]

where the `P_a` are orthogonal projections onto nested subspaces. The decisive hypothesis in this finding is **same-deficit control**:

\[
\boxed{
\|\mathcal A_F-\mathcal D'\|_{\rm HS}^2
=\|X-J\|_{\rm HS}^2
\le\Delta.
}
\tag{3}
\]

Equation (3) is a necessary condition for any attempted WI-137-type refinement in which the new squared-distance term is paid entirely from the existing Lamzouri deficit, for example

\[
\Delta
=\|\mathcal A_F-\mathcal D'\|_{\rm HS}^2
+\text{other nonnegative terms}.
\]

No conclusion below is asserted when an independent source theorem supplies an additional budget not contained in `Delta`.

## 2. The midpoint identity gives an exact depth budget

The Hilbert--Schmidt space is itself a real Hilbert space on self-adjoint operators. Hence the parallelogram/midpoint identity gives

\[
\|X\|_{\rm HS}^2+\|X-J\|_{\rm HS}^2
=2\left\|X-\frac J2\right\|_{\rm HS}^2
 +\frac12\|J\|_{\rm HS}^2.
\tag{4}
\]

Using (1) for the first term and (3) for the second,

\[
\|X\|_{\rm HS}^2+\|X-J\|_{\rm HS}^2
\le (\Delta-L)+\Delta
=2\Delta-L.
\tag{5}
\]

Combining (4) and (5) yields the stronger exact constraint

\[
\boxed{
\Delta
\ge
\left\|\mathcal A_F-\mathcal D-\frac J2\right\|_{\rm HS}^2
+\frac14\|J\|_{\rm HS}^2
+\frac L2.
}
\tag{6}
\]

Thus even before using quantization, two targets that are both required to lie inside the same radius-`sqrt(Delta)` Hilbert--Schmidt ball cannot be far apart: their separation costs one quarter of its squared norm. The already present Lamzouri charge `L` and any failure of `A_F` to sit at the midpoint between the two targets only increase the required deficit.

## 3. Nested flags quantize the cost

Because the added projections come from a flag, they commute. Decompose their joint support into graded subspaces `E_q` on which exactly `q` added levels contain the vector. Then

\[
J|_{E_q}=qI,
\qquad q\in\{1,\ldots,r\},
\]

and therefore

\[
\boxed{
\|J\|_{\rm HS}^2
=\operatorname{tr}(J^2)
=\sum_{q=1}^r q^2\dim E_q.
}
\tag{7}
\]

In particular

\[
\|J\|_{\rm HS}^2
\ge\sum_{q=1}^r\dim E_q
=\operatorname{rank}J.
\tag{8}
\]

Equations (6)--(8) give

\[
\boxed{
\operatorname{rank}J\le4\Delta.
}
\tag{9}
\]

This is more informative than the unit norm floor used in WI-167. A depth-two direction costs at least `1` unit of deficit by itself, a depth-three direction at least `9/4`, and in general the cost grows quadratically with added flag depth. If `J != 0`, then (7) has at least one positive integer eigenvalue and (6) implies

\[
\boxed{\Delta\ge\frac14.}
\tag{10}
\]

For a sequence of finite configurations with `Delta=o(N)`, (9) immediately gives

\[
\boxed{\operatorname{rank}J=o(N).}
\tag{11}
\]

Thus no same-deficit quantized refinement can create a positive-density extra layer near saturation.

## 4. Equality and near-equality are rigid

The constant `1/4` in (6) is the sharp Hilbert-space midpoint constant. Equality in the coarse bound

\[
\Delta=\frac14\|J\|_{\rm HS}^2
\]

forces every discarded nonnegative term in (6) to vanish:

\[
L=0,
\qquad
\mathcal A_F-\mathcal D=\frac J2.
\tag{12}
\]

The canonical and refined targets must therefore lie symmetrically around `A_F`, with both squared distances exactly `||J||_HS^2/4`. Equality also in the rank relaxation (8) forces every nonzero eigenvalue of `J` to equal one, so `J` itself is a single-depth orthogonal projection on its support. Any genuine multi-depth overlap makes the rank bound strictly more expensive.

Near equality has the same interpretation quantitatively. Equation (6) explicitly records the three independent sources of extra cost: midpoint error, the existing source charge `L/2`, and the quantized depth energy `||J||_HS^2/4`. Hence a proposed large added layer cannot hide behind cancellation in the signed polarization term from WI-167; the midpoint identity has already optimized that cancellation exactly.

## 5. Relation to the confluence obstruction and the live clue

WI-167 proves the pointwise one-pair obstruction by combining the unit norm floor for a nonzero `J` with the explicit WI-140 confluence family. Equation (10) globalizes the same conclusion: for **any** finite Lamzouri configuration with `Delta<1/4`, every same-deficit quantized extension must have `J=0`, regardless of how the proposed added subspace is selected.

WI-140 additionally shows that for every fixed number of distinct simple off-line pairs the abstract finite class contains configurations with arbitrarily small `Delta`. Therefore no rule that turns on a nonzero same-deficit flag level merely from the presence of one, or any fixed finite number, of off-line pairs can be universal in Lamzouri's Proposition 2.1 class. A successful interaction-triggered flag must use a source condition absent from those controls.

This narrows `CLUE-lamzouri-flag-depth-operator` without fully resolving it. A new zeta-specific theorem could still force a finite- or sublinear-rank interaction layer, or could supply an independent quantitative budget that pays for a macroscopic layer. The present finding only closes the idea that the **existing** Lamzouri deficit can be repartitioned to fund a substantial extra integer-depth target.

## 6. Prior-art and novelty audit

The zeta-side primary source is Lamzouri, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1 and its nested spaces `U subset V subset W`. The preprint proves the finite Hilbert-space inequality by Bessel/Parseval and scalar square inequalities; it does not state a longer flag-depth target or a rank budget for such a target. WI-137 supplies the exact operator-distance normal form, while WI-140 and WI-167 supply the confluence and one-pair quantized controls used for comparison here.

The midpoint/parallelogram identity, `||P||_HS^2=rank(P)` for an orthogonal projection, simultaneous diagonalization of nested commuting projections, and the resulting Frobenius/Hilbert--Schmidt rank estimates are classical Hilbert-space and matrix-analysis facts. No novelty is claimed for any of them. A targeted search around the new Lamzouri preprint, projection-sum/flag operators, Hilbert--Schmidt nearness, and rank/Frobenius perturbation bounds found general matrix-nearness and projection-distance literature but no external zeta-specific formulation of (6)--(11). That absence is not used as a priority claim.

The durable Mathia deduction is the exact consequence of combining those classical facts with WI-137's recent source-specific normal form: **same-deficit quantized depth has a quadratic spectral cost, so its rank is bounded by four times the complete Lamzouri deficit.**

## 7. Research consequence

The accepted longer-flag clue should now be interpreted more narrowly. It is not enough to exhibit a multi-zero subspace `J` that vanishes on isolated confluence controls. If the proposed layer is integer-depth and its squared-distance term is still paid only from `Delta`, then (9) limits its dimension automatically, and near saturation makes that dimension negligible compared with the zero population.

For the RH-facing objective, the next viable flag mechanism must therefore identify the **new source theorem that funds the layer**, or abandon quantized projection depth in favor of an observable whose scale can shrink with the horizontal defect without becoming confluence-blind. This is an information requirement, not an optimization problem inside the existing WI-137 slack decomposition.