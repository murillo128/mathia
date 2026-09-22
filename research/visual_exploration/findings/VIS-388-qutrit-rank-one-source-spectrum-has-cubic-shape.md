# VIS-388 — qutrit rank-one source spectrum has an intrinsic cubic shape parameter

## Claim

Let

`V = Herm_0(3)`

with the Hilbert-Schmidt inner product, and let `S subset V` be a one-dimensional source subspace. Choose either unit generator `E` of `S`, so `tr(E)=0` and `tr(E^2)=1`, and define

`Delta_S = ad_E^* ad_E`.

Let `lambda_1,lambda_2,lambda_3` be the eigenvalues of `E`, and put

`q_12=(lambda_1-lambda_2)^2`,
`q_13=(lambda_1-lambda_3)^2`,
`q_23=(lambda_2-lambda_3)^2`.

Then on `V`, `Delta_S` has a two-dimensional diagonal kernel and the three root-sector eigenvalues `q_12,q_13,q_23`, each with real multiplicity two; one of the `q_ij` may vanish only when `E` has a repeated eigenvalue.

Write

`t = tr(E^3)`.

The unordered triple `{q_12,q_13,q_23}` is determined exactly by the source-subspace invariant `t^2`: its elements are the three roots of

`z^3 - 3 z^2 + (9/4) z - (1/2 - 3 t^2) = 0`.

Equivalently,

`q_12+q_13+q_23 = 3`,

`q_12 q_13 + q_12 q_23 + q_13 q_23 = 9/4`,

and

`q_12 q_13 q_23 = 1/2 - 3 t^2`.

Because changing the unit generator from `E` to `-E` changes `t` to `-t` but leaves `S` and `Delta_S` unchanged, `t^2` is the intrinsic parameter. Its range is

`0 <= t^2 <= 1/6`.

Thus, unlike the qubit case of `VIS-387`, a rank-one qutrit source already has genuine operator spectral-shape freedom after source rank and total commutator mass are fixed.

Moreover, for generic `E` with three distinct root-sector values

`0 < q_1 < q_2 < q_3`,

the normalized positive spectral measure seen by a Gram tangent is **not determined by its scalar defect rate**. There exist unit vectors `g_A,g_B` in the positive spectral subspace such that

`<g_A,Delta_S g_A> = <g_B,Delta_S g_B> = q_2`,

while their spectral probability measures are different. Hence the scale-invariant spectral-shape channel left open by `VIS-386` is algebraically nonempty already at `d=3`, even though no source-specific or arithmetic anomaly has yet been established.

**Evidence/status:** `EXACT-DERIVED + MINIMAL-DIMENSION CAPACITY RESULT + CLASSICAL SU(3)/CUBIC INGREDIENTS + NO-NOVELTY-CLAIM FOR LIE-THEORETIC BACKGROUND`.

## 1. Adjoint spectrum of one qutrit source direction

Diagonalize `E`. For each unordered pair `i<j`, the two real Hermitian off-diagonal directions supported on entries `(i,j)` and `(j,i)` satisfy

`ad_E^* ad_E X = (lambda_i-lambda_j)^2 X`.

The traceless diagonal subspace has real dimension two and commutes with `E`, hence lies in the kernel. Therefore the spectrum of `Delta_S` on `V` is

`0,0,q_12,q_12,q_13,q_13,q_23,q_23`.

This is the ordinary `A_2` / `SU(3)` root-space picture specialized to the positive commutator Laplacian.

The rank-one trace identity from `VIS-385` gives

`Tr_V Delta_S = 2 d r = 6`,

so

`2(q_12+q_13+q_23)=6`,

which recovers the first symmetric relation.

## 2. Fixed quadratic scale leaves one cubic invariant

Since `tr(E)=0` and `tr(E^2)=1`, the eigenvalues obey

`lambda_1+lambda_2+lambda_3=0`,

`lambda_1^2+lambda_2^2+lambda_3^2=1`.

Hence

`lambda_1 lambda_2 + lambda_1 lambda_3 + lambda_2 lambda_3 = -1/2`.

The traceless cubic identity gives

`t = lambda_1^3+lambda_2^3+lambda_3^3 = 3 lambda_1 lambda_2 lambda_3`.

For three numbers with zero sum and unit sum of squares,

`lambda_1^4+lambda_2^4+lambda_3^4 = 1/2`.

Using the standard fourth-power gap identity,

`q_12^2+q_13^2+q_23^2`
` = 3 sum_i lambda_i^4 + 3 (sum_i lambda_i^2)^2`
` = 9/2`.

Therefore

`q_12 q_13 + q_12 q_23 + q_13 q_23`
` = ((q_12+q_13+q_23)^2 - (q_12^2+q_13^2+q_23^2))/2`
` = 9/4`.

The remaining symmetric invariant is the product. The eigenvalues of `E` are roots of

`x^3 - (1/2)x - t/3 = 0`.

Its cubic discriminant is

`prod_(i<j) (lambda_i-lambda_j)^2 = 1/2 - 3 t^2`.

Thus

`q_12 q_13 q_23 = 1/2 - 3t^2`,

which proves the cubic equation for the `q_ij`. Nonnegativity of the discriminant gives `t^2<=1/6`; equality is exactly the repeated-eigenvalue boundary.

Two useful endpoints are visible immediately. At `t=0`, the eigenvalue triple of `E` is unitarily equivalent, up to ordering, to

`(-1/sqrt(2),0,1/sqrt(2))`,

and the root-sector values are

`{1/2,1/2,2}`.

At `t^2=1/6`, two eigenvalues of `E` coincide and the root-sector values are

`{0,3/2,3/2}`.

Between these boundaries, the generic source has three distinct positive root-sector values. Fixed rank and fixed total spectral mass therefore do not determine the qutrit commutator spectrum.

## 3. Equal defect rate does not determine tangent spectral shape

Fix a generic source with

`0<q_1<q_2<q_3`.

Choose orthonormal positive-spectrum eigenvectors `H_1,H_2,H_3` of `Delta_S` with eigenvalues `q_1,q_2,q_3`, respectively. Set

`g_A = H_2`.

Its positive spectral probability measure is

`mu_A = delta_(q_2)`,

and its defect rate is `m_A=q_2`.

Now define

`alpha = (q_3-q_2)/(q_3-q_1)`,

so `0<alpha<1`, and set

`g_B = sqrt(alpha) H_1 + sqrt(1-alpha) H_3`.

Then `||g_B||_F=1` and

`mu_B = alpha delta_(q_1) + (1-alpha) delta_(q_3)`.

Its defect rate is

`m_B = alpha q_1 + (1-alpha) q_3 = q_2 = m_A`.

Thus `g_A` and `g_B` have the same scalar defect rate but different complete spectral measures. After normalizing spectral coordinates by their common mean, `mu_A` becomes the single atom `delta_1`, while `mu_B` remains a two-atom distribution. The distinction therefore survives the tangent-amplitude quotient of `VIS-386`.

This is an existence/capacity statement, not evidence that an admissible Wang Gram tangent actually realizes an anomalous shape. It proves only that the qubit collapse from `VIS-387` is genuinely dimension-specific rather than a universal consequence of first-moment normalization.

## 4. Consequence for the Wang packet clue

`VIS-387` showed that `d=2` is too small: once source rank and scalar defect rate are known, the complete tangent-weighted commutator spectrum carries no additional information.

The present result identifies `d=3`, already at source rank one, as the first matrix dimension where that obstruction disappears. There are two distinct layers of residual freedom:

1. the operator spectrum of `Delta_S` itself has one intrinsic source-shape parameter `t^2=tr(E^3)^2` beyond rank and total mass;
2. even at fixed `S`, the tangent-weighted spectral measure has degrees of freedom not recoverable from its first moment.

Therefore the accepted clue `research/visual_exploration/clues/CLUE-wang-fixed-source-packet-localization.md` now has a minimal nontrivial algebraic test bed: `d=3`, `r=1`. Any future positive experiment should first distinguish variation caused merely by the classical cubic source invariant from variation caused by arithmetic/source coupling, and should still compare the tangent-weighted normalized measure against matched nonarithmetic controls.

A source-specific Wang gain has not been shown. The result only proves that there is algebraic room for a genuinely independent shape statistic after the exact qubit no-go.

## Prior-art and novelty audit

The Lie-theoretic ingredients are classical. For a diagonal Cartan element of `su(3)`, the adjoint root values are the pairwise eigenvalue differences; squaring them gives the positive commutator-Laplacian root-sector eigenvalues used above.

The normalized traceless `3 x 3` Hermitian conjugacy class also classically has one residual cubic invariant. Thomas L. Curtright and Cosmas K. Zachos, **Elementary Results for the Fundamental Representation of SU(3)**, *Reports on Mathematical Physics* 76:3 (2015), 401–404, DOI `10.1016/S0034-4877(15)30040-9`, arXiv `1508.00868`, explicitly record the Cayley-Hamilton identity

`H^3 = I det(H) + (1/2) H tr(H^2)`

and `det(H)=tr(H^3)/3`, and note that after fixing the quadratic normalization the determinant is the sole remaining invariant of the normalized traceless Hermitian generator.

No novelty is claimed for `SU(3)` roots, the cubic discriminant, Cayley-Hamilton, or the one-parameter classification of normalized traceless qutrit generators. The Mathia-specific contribution is the exact reduction of the current intrinsic source-subspace commutator statistic to that classical cubic invariant and the explicit same-first-moment construction showing that the tangent-normalized spectral measure can carry information not contained in scalar defect energy.

## Boundaries

- The source rank is exactly one. Higher-rank qutrit subspaces may have additional invariants and are not classified here.
- The result shows **capacity**, not arithmetic/source specificity. A generic nonarithmetic source has the same algebraic freedom.
- The same-defect construction chooses abstract positive-spectrum tangents. It does not prove that the Gram tangent of an admissible Wang packet realizes those orientations.
- The result does not beat the isotropic null of `VIS-385`; it identifies what can remain after the scalar moment is calibrated.
- No retained visualization is needed because all claims are exact and representation-independent after unitary diagonalization.
- No Riemann-hypothesis implication or Wang destination gain is established.