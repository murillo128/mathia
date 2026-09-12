---
id: WP-267
title: Linear-relation closure makes the critical Fock boundary coupling purely singular
branch: weil_positivity
status: supported
kind: negative
claim_strength: exact regular-singular classification of the source-native Fock boundary map at and below the Euler threshold
created: 2026-09-12
refined: 2026-09-12
related: [WP-033, WP-261, WP-262, WP-266]
prior_art:
  - Arens linear relations and closure of nonclosable operators
  - canonical regular/singular decomposition of Hilbert-space linear relations
  - graph contractions of closed linear relations
---

# WP-267 — Linear-relation closure makes the critical Fock boundary coupling purely singular

## Claim

`WP-261` left open a natural category change: the source-native symmetric-Fock boundary map is nonclosable as an ordinary Hilbert-space operator at Weil criticality, but perhaps its graph could be closed as a **linear relation** rather than discarded. That escape can be classified exactly.

For the `WP-261` boundary map

\[
C_\sigma e_{p^k}
=\sqrt{\log p}\,p^{-k\sigma/2}e_{p^{k-1}},
\qquad e_{p^0}=\Omega,
\tag{1}
\]

the only cross-prime coupling is the first-layer collapse

\[
L_\sigma e_p
=u_p^{(\sigma)}\Omega,
\qquad
u_p^{(\sigma)}:=\sqrt{\log p}\,p^{-\sigma/2},
\tag{2}
\]

because all primes share the same vacuum endpoint. For every `0<sigma<=1`,

\[
\sum_p |u_p^{(\sigma)}|^2
=\sum_p\frac{\log p}{p^\sigma}
=\infty.
\tag{3}
\]

Closing the graph of this nonclosable scalar row in the standard linear-relation category does **not** preserve it as a singular but still arithmetic boundary operator. Its graph closure is the whole product

\[
\boxed{
\overline{\operatorname{graph}L_\sigma}
=\ell^2(\mathbb P)\times\mathbb C\Omega,
\qquad 0<\sigma\le1.
}
\tag{4}
\]

Thus the first-layer boundary relation is maximally multivalued: every bulk prime vector is compatible with every vacuum amplitude. Its canonical regular operator part is zero.

For the full Fock map, the higher prime-power layers are bounded and prime-separable. Consequently the closed relation splits exactly into

\[
\boxed{
\overline{C_\sigma}
=
\bigl(\ell^2(\mathbb P)\times\mathbb C\Omega\bigr)
\oplus
\operatorname{graph}B_\sigma,
\qquad 0<\sigma\le1,
}
\tag{5}
\]

where `B_sigma` is the bounded weighted backward shift on the `k>=2` layers. The multivalued part is precisely `C Omega`, and the canonical regular part is precisely `B_sigma` with the entire first prime layer sent to zero.

Therefore the canonical regularization by linear relations deletes **exactly the piece that supplied both the critical prime-layer Mangoldt norm and the only mixed-prime Gram entries**. The surviving positive adjoint-square is bounded but prime-separable and has zero first-prime-layer diagonal.

At `sigma=1/2`, the same scalar row is the critical rank-one functional appearing after the source-canonical rescaling in `WP-266`. Hence allowing a multivalued closure does not rescue that rank-one positive direction either: the canonical relation closure classifies it as pure singular freedom rather than as a closed arithmetic coupling.

This is a decisive negative for the most direct “replace nonclosable operator by closed relation” escape. A successful boundary/cohomological completion must introduce additional source-derived structure **before** closure; the standard relation closure itself contains no rule that couples the bulk prime vector to the new boundary value.

## 1. Decompose the Fock boundary map into the coherent row and bounded tower shift

Let

\[
\mathcal H_{\rm ax}
=
\mathcal H_1\oplus\mathcal H_{\ge2},
\qquad
\mathcal H_1
=\overline{\operatorname{span}}\{e_p:p\in\mathbb P\},
\tag{6}
\]

and decompose the target as

\[
\mathcal K
=\mathbb C\Omega\oplus\mathcal K_{\ge1}.
\tag{7}
\]

On algebraic finite support, equation (1) becomes the orthogonal sum

\[
C_\sigma=L_\sigma\oplus B_\sigma,
\tag{8}
\]

with

\[
L_\sigma x
=
\left(\sum_p u_p^{(\sigma)}x_p\right)\Omega
\tag{9}
\]

and

\[
B_\sigma e_{p^k}
=\sqrt{\log p}\,p^{-k\sigma/2}e_{p^{k-1}},
\qquad k\ge2.
\tag{10}
\]

The higher-layer map is bounded for every `sigma>0`, because its images are orthogonal and

\[
\|B_\sigma\|^2
=
\sup_{p,\,k\ge2}
(\log p)p^{-k\sigma}
<\infty.
\tag{11}
\]

So every failure of closability in `WP-261` is concentrated in the single coherent vacuum row `L_sigma`. This also isolates the geometry: `L_sigma` is the only place where distinct primes acquire a nonzero Gram inner product.

Indeed, on the first layer

\[
\langle L_\sigma e_p,L_\sigma e_q\rangle
=
\sqrt{\log p\log q}\,(pq)^{-\sigma/2},
\tag{12}
\]

whereas the higher-layer images for different prime towers are orthogonal.

## 2. The scalar graph closure is the entire product

Write

\[
\ell_\sigma(x)
:=\sum_p u_p^{(\sigma)}x_p
\tag{13}
\]

on `c_00(P)`. For `0<sigma<=1`, the coefficient sequence is not in `ell^2` by (3).

Because the positive series in (3) diverges, choose pairwise disjoint finite prime blocks `F_j` with

\[
A_j
:=\sum_{p\in F_j}|u_p^{(\sigma)}|^2
\longrightarrow\infty.
\tag{14}
\]

Set

\[
v_j
:=\frac1{A_j}
\sum_{p\in F_j}u_p^{(\sigma)}e_p.
\tag{15}
\]

The coefficients are real and positive, so directly

\[
\ell_\sigma(v_j)=1,
\qquad
\|v_j\|^2=A_j^{-1}\longrightarrow0.
\tag{16}
\]

Therefore

\[
(0,1)
\in
\overline{\operatorname{graph}\ell_\sigma}.
\tag{17}
\]

Linearity gives the whole vertical fiber

\[
\{0\}\times\mathbb C
\subset
\overline{\operatorname{graph}\ell_\sigma}.
\tag{18}
\]

Now take any finitely supported `x`. Since `(x,ell_sigma(x))` lies in the original graph and `(0,-ell_sigma(x))` lies in its closure, their sum gives

\[
(x,0)
\in
\overline{\operatorname{graph}\ell_\sigma}.
\tag{19}
\]

Finite support is dense in `ell^2(P)`, hence

\[
\ell^2(\mathbb P)\times\{0\}
\subset
\overline{\operatorname{graph}\ell_\sigma}.
\tag{20}
\]

Combining (18) and (20) proves the exact identity

\[
\boxed{
\overline{\operatorname{graph}\ell_\sigma}
=
\ell^2(\mathbb P)\times\mathbb C.
}
\tag{21}
\]

An equivalent geometric statement is that the algebraic primitive kernel

\[
\ker\ell_\sigma\cap c_{00}(\mathbb P)
\tag{22}
\]

is dense in `ell^2(P)`. The would-be codimension-one boundary condition therefore ceases to be a closed hyperplane at the critical/global Hilbert scale.

## 3. Standard linear-relation theory identifies the row as purely singular

A linear relation from a Hilbert space `H` to a Hilbert space `K` is simply a linear subspace of `H x K`; a nonclosable operator acquires a nontrivial multivalued part when its graph is closed. For a closed relation `T`,

\[
\operatorname{mul}T
:=\{y:(0,y)\in T\}
\tag{23}
\]

measures exactly this failure of single-valuedness.

Equation (21) gives

\[
\operatorname{mul}\overline{\ell_\sigma}
=\mathbb C.
\tag{24}
\]

Since this is the entire target, the canonical regular part obtained by projecting away the multivalued target is zero:

\[
\boxed{
(\overline{\ell_\sigma})_{\rm reg}=0.
}
\tag{25}
\]

The same statement can be checked without importing any decomposition theorem. If

\[
R=\ell^2(\mathbb P)\times\mathbb C,
\tag{26}
\]

then its adjoint relation is only

\[
R^*=\{(0,0)\},
\tag{27}
\]

because the adjoint identity must hold independently for arbitrary bulk and boundary coordinates. Consequently

\[
\boxed{R^*R=0}
\tag{28}
\]

as the everywhere-defined zero operator on `ell^2(P)`. Thus the canonical positive adjoint-square of the closed relation does not retain a renormalized remnant of the critical Gram; it annihilates it.

This is exactly the classical “singular relation” situation: the closure is a Cartesian product rather than the graph of a regular operator.

## 4. The full Fock relation loses exactly its mixed-prime geometry

Because `B_sigma` in (10) is bounded, its graph is already closed. The domain and target splittings (6)--(7) are orthogonal, so equations (21) and (10) give

\[
\overline{\operatorname{graph}C_\sigma}
=
\left\{
\bigl((x_1,x_h),\,z\Omega+B_\sigma x_h\bigr):
 x_1\in\mathcal H_1,
 x_h\in\mathcal H_{\ge2},
 z\in\mathbb C
\right\}.
\tag{29}
\]

Hence

\[
\operatorname{mul}\overline C_\sigma
=\mathbb C\Omega.
\tag{30}
\]

Projecting the target orthogonally away from `Omega` gives the canonical regular part

\[
(\overline C_\sigma)_{\rm reg}(x_1,x_h)
=B_\sigma x_h.
\tag{31}
\]

It is a bounded operator on all of `H_ax`. Its Gram therefore satisfies

\[
(\overline C_\sigma)_{\rm reg}^*
(\overline C_\sigma)_{\rm reg}e_p=0
\tag{32}
\]

on the first prime layer, while for `k>=2`,

\[
(\overline C_\sigma)_{\rm reg}^*
(\overline C_\sigma)_{\rm reg}e_{p^k}
=(\log p)p^{-k\sigma}e_{p^k}.
\tag{33}
\]

All mixed-prime matrix entries vanish.

Thus relation closure has a sharp interpretation in the original Mathia construction:

\[
\boxed{
\text{singular part}
=
\text{common-vacuum prime coherence},
\qquad
\text{regular part}
=
\text{prime-separable tower shift}.
}
\tag{34}
\]

At `sigma=1/2`, equation (32) deletes the entire `log p/sqrt p` first-prime layer that `WP-261` was trying to preserve, while (33) retains only the already-separable higher prime powers. The category change therefore regularizes the operator only by throwing away the exact component that made the construction interesting for Weil positivity.

## 5. A single-valued selection is extra, programmable structure

One might refuse the canonical regular part and instead choose a single-valued section of the full relation (21). But once the closure is the entire product, it no longer selects any section at all.

Every linear functional

\[
s:\ell^2(\mathbb P)\supset\operatorname{dom}s\to\mathbb C
\tag{35}
\]

has its graph contained in `R=ell^2(P) x C`. If one demands an everywhere-defined closed selection, the closed graph theorem makes `s` bounded, hence

\[
s(x)=\langle x,h\rangle
\tag{36}
\]

for some `h in ell^2(P)`.

To recover the original critical amplitudes one would need

\[
s(e_p)=u_p^{(\sigma)}.
\tag{37}
\]

For `0<sigma<=1`, equation (3) says that no such `h` belongs to `ell^2`. Therefore no closed everywhere-defined selection preserves the original row.

Conversely, infinitely many bounded selections exist after changing the amplitudes to any square-summable sequence. The closed relation itself does not distinguish among them. Selecting one because its Gram has a desired sign, Gamma term, polar term, or Weil matrix would simply reinsert the target by hand.

This also blocks the tempting interpretation of the multivalued vacuum coordinate as an automatically generated archimedean boundary variable. The relation says precisely the opposite: the vacuum coordinate is **independent** of the finite bulk vector after closure. A source-derived law relating the two would have to be new structure not contained in the closed relation.

## 6. Sharp matched controls

### Off-critical control

For `sigma>1`,

\[
\sum_p\frac{\log p}{p^\sigma}<\infty,
\tag{38}
\]

so `u^(sigma) in ell^2(P)` and `L_sigma` is bounded. Its graph closure remains the graph of the unique bounded functional represented by `u^(sigma)`; there is no multivalued part. The mixed-prime Gram

\[
\langle L_\sigma e_p,L_\sigma e_q\rangle
=u_p^{(\sigma)}u_q^{(\sigma)}
\tag{39}
\]

survives intact.

Thus the regular/singular transition occurs at exactly the same `sigma=1` threshold as the `WP-261` closability theorem. Linear relations do not move that boundary.

### Generic divergent-sequence control

Nothing in the proof of (21) uses primes beyond divergence of

\[
\sum_j|u_j|^2.
\tag{40}
\]

For any countable label set and any coefficient sequence outside `ell^2`, the scalar functional on finite support has the same full-product graph closure. The singularization mechanism is therefore universal functional analysis, not a hidden arithmetic theorem.

### Orthogonal-boundary control

`WP-261` already showed that retaining an orthogonal prime boundary label makes the exact critical carrier bounded. In that control there is no common scalar row, hence no multivalued vacuum defect—but also no cross-prime coherence. Together with (34), this identifies the precise tradeoff:

\[
\boxed{
\text{common finite boundary}
\Rightarrow
\text{coherence becomes purely singular};
\qquad
\text{orthogonal labels}
\Rightarrow
\text{regular but separable}.
}
\tag{41}
\]

`WP-262` showed that infinite-dimensional incidence can evade this analytic dichotomy, but only with programmable correlation support. The present result therefore closes a different route: **linear-relation regularization of the original common-boundary map does not provide the missing non-programmable infinite-dimensional correspondence.**

## 7. Prior-art and novelty audit

No theorem-level novelty is claimed for the operator theory.

The language of multivalued linear relations goes back at least to R. Arens, *Operational calculus of linear relations*, Pacific Journal of Mathematics 11 (1961), 9--23. The regular/singular decomposition used to interpret (25) is classical; see S. Hassi, Z. Sebestyen, H. S. V. de Snoo, and F. H. Szafraniec, *A canonical decomposition for linear operators and linear relations*, Acta Mathematica Hungarica 115 (2007), 281--307, DOI `10.1007/s10474-007-5247-y`. That work characterizes singular relations by closures that are Cartesian products of closed subspaces. Z. Tarcsay and Z. Sebestyen, *Canonical Graph Contractions of Linear Relations on Hilbert Spaces*, Complex Analysis and Operator Theory 15 (2021), article 21, DOI `10.1007/s11785-020-01066-3`, gives a modern account of closed relation graphs, their multivalued parts, regular parts, and canonical graph contractions.

Those sources classicalize the category and terminology; equations (14)--(34) are the direct specialization to Mathia's `WP-261` Fock boundary coefficients. A targeted search did not reveal an independent Riemann/Weil mechanism based on treating this Mangoldt boundary row as a multivalued relation, and none is claimed.

The substantive Mathia-specific result is narrower and exact: the category change explicitly left open by the nonclosability result can be executed canonically, and its regular/singular decomposition shows that **the singular component is exactly the source-native cross-prime coherence**. Canonical regularization removes that coherence and the first-prime Mangoldt diagonal simultaneously.

This is not a new zeta representation, not a positivity criterion equivalent to RH, and not a spectrum built from zeros. It is a structural no-go about one candidate carrier before any zero data or archimedean completion is introduced.

## 8. Boundary of the result

`WP-267` does **not** rule out:

- an infinite-dimensional source-forced boundary correspondence whose critical map is already closed;
- a non-Hilbert topology in which the finite-place test space is changed for an independently justified arithmetic reason;
- a quotient/cohomological construction in which the common-vacuum row is not the primitive object being closed;
- an archimedean sector coupled to the finite source before the singular collapse occurs;
- a canonical non-Bessel or distributional state space whose pairing is not obtained by taking the graph closure of `L_sigma`;
- the locally finite infinite-dimensional Fock incidences of `WP-262`, although those still face the separate source-selection/programming obstruction.

What it does rule out is the simplest category-only repair:

\[
\text{nonclosable Mathia boundary operator}
\longrightarrow
\text{close its graph as a linear relation}
\longrightarrow
\text{extract a canonical positive regular part}.
\tag{42}
\]

For the actual critical boundary row, that pipeline produces zero on the mixed-prime component.

## 9. Consequence for the research line

After `WP-266`, the live problem was whether a new global carrier could retain the source-canonical critical half-density while escaping ordinary Hilbert-form nonclosability. Closed linear relations are a canonical first enlargement of the operator category, so they had to be tested before inventing a more exotic boundary space.

They do not solve the problem. At criticality the relation closure remembers the bad row only as a free multivalued boundary fiber, while its canonical regular operator forgets the row entirely. The missing geometry must therefore do more than tolerate nonclosability: it must **derive a nontrivial bulk-boundary law whose global closure remains single-valued or whose quotient/cohomology fixes the boundary value canonically**.

That surviving mechanism must still satisfy the original mandate: recover the finite prime terms with their Weil orientation, generate the Gamma and polar/global counterterms from the same structure, and obtain the final sign from an independent geometric theorem rather than from target-selected boundary data.
