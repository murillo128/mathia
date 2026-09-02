# PF-165 — interval-filling compact-reference residuals kill analytic scalar normalization

**Status:** `EXACT-DERIVED + CROSS-LINE-EVIDENCE + DECISIVE-NEGATIVE/BOUNDARY`.

## Statement

Let

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
f(x):=V(x)-x,
\]

and let the standard all-composite shift reference for the exact prime flute be

\[
q_j=p_j+1.
\]

Write `C(Q)` for the PF-161 connected bottom-Ruelle logarithmic cusp coefficient computed against an ordered all-composite reference `Q=(q'_j)` that differs from the standard shift reference at only finitely many interior labels. PF-164 gives the exact finite-support law

\[
\boxed{
C(Q)-C(Q_0)
=2\sum_j\bigl(V(q'_j)-V(q_j)\bigr).
}
\tag{1}
\]

Splitting `V(x)=x+f(x)` gives

\[
C(Q)-C(Q_0)
=
2M(Q)+R(Q),
\tag{2}
\]

where

\[
M(Q):=\sum_j(q'_j-q_j)\in\mathbb Z,
\qquad
R(Q):=2\sum_j\bigl(f(q'_j)-f(q_j)\bigr).
\tag{3}
\]

Thus the obvious integer displacement disappears after passing to the natural reduced scalar

\[
[C(Q)]_2\in\mathbb R/2\mathbb Z.
\tag{4}
\]

VIS-002 supplies an exact legal subfamily of compact reference changes. At every eligible site with following prime gap greater than `2`, one may replace

\[
q_j=p_j+1
\longmapsto
q'_j=p_j+3.
\tag{5}
\]

If the corresponding eligible primes are `r_k`, put

\[
a_k
:=2\bigl(V(r_k+3)-V(r_k+1)-2\bigr)
=2\bigl(f(r_k+3)-f(r_k+1)\bigr)>0.
\tag{6}
\]

VIS-002 proves that `(a_k)` is summable and that for every sufficiently far tail its achievement set is an interval. Consequently there is a tail index `K`, which may also be chosen so that

\[
0<A_K:=\sum_{k\ge K}a_k<2,
\tag{7}
\]

such that the finite-support reduced coefficient shifts

\[
R(F):=\sum_{k\in F}a_k,
\qquad F\subset\{K,K+1,\ldots\}\text{ finite},
\tag{8}
\]

are dense in the full interval `[0,A_K]`. Equivalently,

\[
\boxed{
\overline{
\{[C(Q_F)]_2:F\text{ finite}\}
}
\supset
[C(Q_0),C(Q_0)+A_K]
\subset\mathbb R/2\mathbb Z.
}
\tag{9}
\]

The arc in (9) is nondegenerate and comes from exact ordered all-composite references that differ from the standard shift reference only at finitely many vertices.

It follows that **no nonconstant real-analytic scalar normalization of the reduced coefficient can be compact-reference invariant**. Precisely, let

\[
\Phi:\mathbb R/2\mathbb Z\longrightarrow\mathbb C
\]

be real analytic. If

\[
\Phi([C(Q)]_2)
\]

has the same value for every legal finite-support all-composite reference `Q`, then

\[
\boxed{\Phi\text{ is constant}.}
\tag{10}
\]

The same conclusion holds for a real-analytic scalar function of the explicitly integer-subtracted residual coordinate in (2)--(3).

Thus quotienting the obvious `2Z` displacement and then applying a determinant-like, exponential, analytic, or other real-analytic scalar reparameterization cannot rescue the PF-161 cusp coefficient as an intrinsic quantity. The full signed/multivalued achievement set need not be classified to obtain this obstruction.

## Derivation

For the `+2` move (5), equation (1) gives

\[
C(Q_F)-C(Q_0)
=
4|F|+\sum_{k\in F}a_k.
\tag{11}
\]

Modulo `2Z`, the term `4|F|` vanishes, so

\[
[C(Q_F)]_2
=
\left[C(Q_0)+\sum_{k\in F}a_k\right]_2.
\tag{12}
\]

VIS-002 reconstructs the legality and arithmetic of this subfamily. Simultaneous `+2` moves preserve order, and eligibility guarantees that a moved label remains below the next unmoved one. It also proves

\[
a_k
=
\frac{4\pi^2}{3r_k^2}+O(r_k^{-3}),
\tag{13}
\]

that eligible sites have bounded gaps in prime-index scale, and hence that if

\[
A_k^{\rm tail}=\sum_{\ell>k}a_\ell,
\]

then

\[
\frac{a_k}{A_k^{\rm tail}}\longrightarrow0.
\tag{14}
\]

The classical Kakeya achievement-set criterion therefore applies after some index: every term is no larger than the remaining tail, so the infinite subsum set of that tail is exactly an interval. Finite subsums are dense in it. Because the series is summable, the tail index can be increased until (7) also holds, avoiding any wraparound ambiguity on the circle `R/2Z`. This proves (9).

Now assume `Phi` satisfies the compact-reference invariance hypothesis. For every finite `F`, (12) gives

\[
\Phi\!\left([C(Q_0)+R(F)]_2\right)
=
\Phi([C(Q_0)]_2).
\tag{15}
\]

The set of `R(F)` is dense in `[0,A_K]`. Continuity of a real-analytic function extends (15) to the whole nondegenerate arc in (9). A real-analytic function on the connected real-analytic circle that is constant on a nonempty open arc is constant everywhere. This proves (10).

No information about negative moves, larger integer displacements, or the exact topology of the complete constrained residual family is used.

## Relevance to the prime-flute program

PF-164 already shows that the PF-161 connected Ruelle cusp coefficient is not intrinsic: one compact change of an exact all-composite comparison can move it, even though the comparison tail is unchanged. A natural possible escape was to regard the integer part of that change as a coarse gauge, quotient it out, and ask whether the nonlinear cotangent residue still supports a canonical analytic scalar.

Equation (10) closes that escape. The failure is stronger than isolated reference dependence: after removing the integer displacement, exact compact controls already fill an interval in closure. Any natural analytic scalar function that is required to forget the compact-reference choice must therefore forget the reduced coefficient altogether.

This does **not** rule out a genuinely intrinsic full-surface Selberg/Ruelle object, a canonical comparison selected by the prime-flute geometry itself, or an invariant depending on substantially more data than the single PF-161 coefficient. It only rules out repairing this selected relative coefficient by an analytic scalar quotient or reparameterization.

## Prior art and novelty assessment

The achievement-set input is classical in type and is already persisted, with its own literature audit, as VIS-002. Kakeya's criterion and the modern theory of interval/Cantor/Cantorval achievement sets are not new. The fact that a real-analytic function constant on a nondegenerate interval is constant on a connected one-dimensional analytic manifold is likewise elementary.

A directed literature check of achievement sets and multivalued/multigeometric subsum sets confirms that interval, Cantor, and Cantorval behavior is a classical subject; it does not supply a special spectral meaning to the present residual family. No general novelty is claimed. The durable contribution here is the **prime-flute-specific no-go consequence** obtained by combining PF-164's exact compact-reference coefficient law with VIS-002's interval-filling legal subfamily.

## Boundary conditions and falsification tests

The conclusion uses the closure of finite-support values, not an assertion that a countable finite-support family literally contains every point of an interval. Continuity is exactly what lets density suffice.

The conclusion is restricted to real-analytic scalar normalizations after the natural `2Z` reduction, or equivalently to real-analytic functions of the explicitly integer-subtracted scalar residual. An arbitrary discontinuous quotient can be constant on the compact-reference orbit and nonconstant elsewhere; PF-165 makes no claim about such constructions. Nor does it rule out a normalization that depends on the full reference sequence, a scattering matrix, a resonance divisor, or another operator-valued object rather than on this one coefficient.

A decisive falsification would require failure of either persisted input: the PF-164 finite-support law would have to fail for the simultaneous legal `+2` family, or VIS-002's interval-filling tail would have to be false. Both are independently checkable from the exact endpoint formula. The final analytic step is an identity principle and has no geometric hypothesis.

## Consequence

The exact topology of the complete signed/multivalued compact-reference residual achievement set may remain an interesting subsum-set problem, but it is no longer needed to decide whether the PF-161 scalar can be rescued by a natural analytic normalization. For the research mandate, further work on this selected cusp coefficient is warranted only if a new construction couples it to genuinely intrinsic full-surface data in a way that is not a scalar analytic function of `[C]_2`.
