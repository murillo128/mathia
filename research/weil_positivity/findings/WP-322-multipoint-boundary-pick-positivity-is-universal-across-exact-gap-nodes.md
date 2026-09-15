---
id: WP-322
title: Exact multipoint gap coupling is a universal Pick Gram and cannot supply arithmetic-selective positivity
branch: weil_positivity
status: supported
kind: exact-multipoint-pick-loewner-universality-obstruction
claim_strength: exact finite-section classification for scalar Herglotz sources at arbitrary regular real nodes; the full boundary Loewner matrix is an explicit Gram matrix of resolvent vectors, so every finite multipoint gap coupling, every principal minor, and every admissible Julia-Nevanlinna Schur-complement reduction is positive for every positive scalar Herglotz measure; consequently exact cross-gap Pick positivity is not arithmetic-selective even before the atomwise smoothing control of WP-321, although support-sensitive non-Pick invariants and genuinely matrix/operator-valued couplings remain open
created: 2026-09-15
related: [WP-304, WP-310, WP-312, WP-318, WP-319, WP-320, WP-321]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for boundary Pick matrices and the theorem that Julia-Nevanlinna reduction corresponds to Schur complementation of Pick matrices
---

# WP-322 — Exact multipoint gap coupling is a universal Pick Gram and cannot supply arithmetic-selective positivity

## Claim

`WP-321` closes the natural weak-topology escape from the scalar Julia route: one non-arithmetic positive Herglotz source can asymptotically match the full unthinned bounded-gap family of derivative-biased Mangoldt laws. It deliberately leaves open a sharper possibility: perhaps the **exact simultaneous values at several arithmetic gap nodes** satisfy a positive cross-gap constraint that atomwise smoothing cannot preserve.

The canonical scalar multipoint constraint does not provide that escape.

Let `f` be any scalar Pick/Herglotz function on the upper half-plane with representation

\[
f(z)=az+b+
\int_{\mathbb R}
\left(
\frac1{x-z}-\frac{x}{1+x^2}
\right)d\mu(x),
\qquad a\ge0,
\quad b\in\mathbb R,
\quad \mu\ge0.
\tag{1}
\]

Choose distinct real regular nodes

\[
t_1,\ldots,t_m\in\mathbb R\setminus\operatorname{supp}\mu
\tag{2}
\]

at which `f'(t_i)<infinity`. They may lie in arbitrary different support gaps; no sparsity or separation hypothesis is imposed. Define the boundary Loewner/Pick matrix

\[
L_f(T)=(L_{ij})_{1\le i,j\le m}
\tag{3}
\]

by

\[
L_{ii}=f'(t_i),
\qquad
L_{ij}=\frac{f(t_i)-f(t_j)}{t_i-t_j}
\quad(i\ne j).
\tag{4}
\]

Then exactly

\[
\boxed{
L_{ij}
=
a+
\int_{\mathbb R}
\frac{d\mu(x)}{(x-t_i)(x-t_j)}
}
\tag{5}
\]

for all `i,j`. Consequently, if

\[
u_i=
\left(
\sqrt a,
\frac1{x-t_i}
\right)
\in
\mathbb C\oplus L^2(\mu),
\tag{6}
\]

then

\[
\boxed{
L_{ij}=\langle u_i,u_j\rangle,
\qquad
L_f(T)\succeq0.
}
\tag{7}
\]

Thus the exact cross-gap Pick/Loewner positivity is not a special feature of the Mangoldt source. It is a universal Gram theorem for **every** positive scalar Herglotz source.

Applied to the reflected Mangoldt source of `WP-318`, every finite collection of exact prime-power gap nodes therefore lies in the same positive Pick cone as arbitrary non-arithmetic positive controls. The entries of the matrix can retain exact arithmetic information, but their nonnegativity cannot be the independent arithmetic sign mechanism sought by the `weil_positivity` mandate.

Moreover, Agler--Young's boundary Nevanlinna--Pick theory identifies Julia--Nevanlinna reduction with Schur complementation of the associated Pick matrix. Hence coupling finitely many exact gaps first and then performing any admissible sequence of scalar Julia reductions does not escape this universal cone: positivity of every resulting Schur complement is inherited from (7), not forced by Mangoldt arithmetic.

This is stronger in a different direction from `WP-321`. No smoothing, asymptotic matching, weak convergence, or replacement source is needed. The obstruction is **exact at the original arithmetic nodes**. What remains open is correspondingly narrower: an exact support-sensitive scalar invariant that is not merely a Pick-kernel positivity statement, or a genuinely matrix/operator-valued/global coupling whose sign is not inherited from scalar Herglotz positivity.

## Derivation

### 1. The boundary divided differences are resolvent inner products

For `i != j`, subtract (1) at `t_i` and `t_j`. The subtraction constant disappears and

\[
\frac{a(t_i-t_j)}{t_i-t_j}=a.
\tag{8}
\]

For the integral term,

\[
\frac{1}{t_i-t_j}
\left(
\frac1{x-t_i}-\frac1{x-t_j}
\right)
=
\frac1{(x-t_i)(x-t_j)}.
\tag{9}
\]

This gives (5) off the diagonal. On the diagonal,

\[
f'(t_i)
=
a+
\int_{\mathbb R}
\frac{d\mu(x)}{(x-t_i)^2},
\tag{10}
\]

so the same formula holds there as well.

The regularity assumption makes `(x-t_i)^(-1)` an `L^2(mu)` vector. Cross terms in (5) are therefore finite by Cauchy--Schwarz. Equations (6)--(7) follow immediately.

Equivalently, the usual Pick kernel has the explicit factorization

\[
\frac{f(z)-\overline{f(w)}}{z-\overline w}
=
a+
\int_{\mathbb R}
\frac{d\mu(x)}{(x-z)(x-\overline w)},
\tag{11}
\]

and (7) is its regular real-boundary restriction. The multipoint geometry is therefore already present before any Julia normalization: it is the Gram geometry of one family of source resolvents.

### 2. Arbitrarily many exact arithmetic gaps do not change the sign theorem

Let the reflected Mangoldt source be

\[
\mu_{\rm M}
=
\sum_{q=p^k}
\frac{\Lambda(q)}{q+1}\,\delta_{-\log q},
\tag{12}
\]

as in `WP-318`. Every midpoint of a consecutive support gap is a regular node, and one may select **any finite family** of such nodes

\[
T=\{t_{j_1},\ldots,t_{j_m}\}.
\tag{13}
\]

No matter how close the gaps are, whether they overlap after rescaling, or whether the family is sparse or dense along the support, (7) gives

\[
L_{\rm M}(T)\succeq0.
\tag{14}
\]

But (14) does not use that the support points are logarithms of prime powers or that the masses are Mangoldt masses. Replacing (12) by any positive measure for which the same nodes are regular gives the identical theorem.

The decisive distinction is therefore:

- the **matrix entries** may be arithmetic;
- the **reason the matrix is positive** is not arithmetic.

A Weil mechanism needs the second item. A positive form whose sign survives every replacement by an arbitrary positive Herglotz measure is a matched-control sign theorem, not an explanation of global Weil positivity.

### 3. Principal minors and finite exact coherence are equally universal

Any principal submatrix of (7) is again a Gram matrix, hence

\[
\det L_f(T')\ge0
\tag{15}
\]

for every finite subfamily `T' subseteq T`. Thus exact determinant inequalities linking several arithmetic gaps do not acquire arithmetic selectivity merely because they use several nodes simultaneously.

For the pure-measure case `a=0`, if `mu` has infinitely many distinct support points and the `t_i` are distinct regular nodes, the Gram is in fact strictly positive definite. Indeed,

\[
\sum_i c_i\frac1{x-t_i}=0
\quad \mu\text{-a.e.}
\tag{16}
\]

would imply that the rational function on the left vanishes at infinitely many support points. Multiplication by `prod_i(x-t_i)` gives a polynomial of degree at most `m-1` with infinitely many zeros, hence it is identically zero and all `c_i=0`. Therefore

\[
L_f(T)\succ0.
\tag{17}
\]

whenever the source has infinite support of this kind. Strict determinant positivity is thus also generic inside the scalar positive-measure class; it is not a prime-power signature.

This strictness statement is a useful adversarial control, not a new arithmetic theorem. It prevents a route that would try to interpret nonvanishing of exact multipoint Pick determinants as the missing arithmetic rigidity.

### 4. Julia reductions are Schur complements of the same universal Gram

Boundary Julia--Nevanlinna reduction does not manufacture a new sign principle. Agler and Young prove that, for boundary Pick interpolation, reduction corresponds to Schur complementation of the Pick matrix.

Write a positive block as

\[
L=
\begin{pmatrix}
\alpha & v^*\\
v & B
\end{pmatrix},
\qquad \alpha>0.
\tag{18}
\]

Its Schur complement

\[
B-\alpha^{-1}vv^*
\tag{19}
\]

is positive semidefinite. In the Gram realization (7), (19) is simply the Gram matrix of the residual resolvent vectors after orthogonal projection away from the first vector.

Hence a finite chain of exact gap-node Julia reductions is geometrically

\[
\text{resolvent Gram}
\;\longrightarrow\;
\text{orthogonal residual Gram}
\;\longrightarrow\;\cdots,
\tag{20}
\]

and positivity at every stage is inherited from Hilbert-space projection. This is the multipoint version of the universality already visible in the one-node Boolean self-energy form of `WP-318`.

### 5. Infinite-node caution

The result is deliberately a **finite-section** statement. If one lists infinitely many gap nodes, (7) proves that every finite submatrix is positive, so it defines a positive kernel in the usual finite-section sense. It does **not** by itself assert that the resulting infinite matrix is a bounded operator on `ell^2`, that a corresponding quadratic form is closable, or that arbitrary infinite Julia chains are stable.

Those operator-domain questions can still carry structure. They cannot, however, obtain arithmetic selectivity merely by invoking positivity of finite Pick sections, because that positivity has already been classified by (7).

## Adversarial checks

1. **Sign convention.** With the Herglotz convention of `WP-318`, differentiating `(x-z)^(-1)` in `z` gives `+(x-z)^(-2)`, so (10) has the required positive sign. Equation (9) likewise has positive sign.

2. **Cross-gap denominators can change sign pointwise.** This does not threaten positivity. Individual integrands in (5) need not be nonnegative when `i != j`; positivity is the Gram identity (7), not termwise positivity.

3. **No hidden compact-support assumption.** Only the ordinary Herglotz integrability plus finite boundary derivatives at the selected nodes is used. Cauchy--Schwarz controls each cross integral.

4. **Exactness versus `WP-321`.** `WP-321` gives one non-arithmetic source that asymptotically matches all bounded-gap Julia profiles after smoothing. The present finding does not use that control. It says that the canonical exact multipoint sign constraint itself is universal even on the unsmoothed Mangoldt source.

5. **Arithmetic data are not erased.** Equation (5) can distinguish two measures numerically. The no-go concerns the provenance of **nonnegativity**, not recoverability of source data from all matrix entries.

6. **No claim about arbitrary support-sensitive invariants.** An invariant using exact atomic locations or masses in a way not equivalent to scalar Pick positivity is not ruled out. Nor are matrix-valued Herglotz functions, non-Pick indefinite-to-positive quotients, global finite--archimedean couplings, or infinite-domain phenomena.

7. **Prior-art boundary.** The positivity of Pick matrices and their Schur-complement behavior are classical. The new content here is the Mathia-specific redirect: the exact all-gap scalar coherence left open after `WP-321` remains inside that classical universal cone and therefore fails the line's independent-sign requirement.

## Matched controls

The relevant control is now stronger than a specially engineered atomless approximation. Let `mu_ctrl` be **any** positive Herglotz measure with the chosen real nodes regular. Its exact multipoint matrix satisfies

\[
L_{\rm ctrl}(T)\succeq0.
\tag{21}
\]

Thus the arithmetic source and a broad non-arithmetic control class share the same multipoint sign theorem without matching the matrix entries. This is sufficient for the falsification question: positivity alone cannot identify the arithmetic source.

A second control is obtained by replacing prime-power support with arbitrary infinite discrete support and arbitrary positive masses. Under the same regular-node condition, (17) gives strict positivity of every finite multipoint matrix there as well.

## Consequence for the research line

The scalar Julia/Herglotz route is narrower again. `WP-318` showed that one-node Julia tangents are universal Boolean self-energies; `WP-319` and `WP-320` showed that individual and sparse same-source gap coherence are matched controls; `WP-321` extended this to the full bounded-gap family in the natural weak topology. The exact multipoint candidate that survives those approximation arguments is now classified too:

\[
\boxed{
\text{exact scalar cross-gap Pick positivity}
=
\text{resolvent Gram positivity},
}
\tag{22}
\]

and finite Julia reductions are only Schur complements of that same Gram geometry.

Therefore the next scalar test should **not** be another Pick determinant, principal minor, or finite Julia-reduction inequality at more arithmetic gap nodes. A viable continuation must exhibit a source-forced constraint whose sign is not automatic for arbitrary positive Herglotz measures. Otherwise the search should leave the scalar Pick category and investigate a genuinely matrix/operator-valued or global finite--archimedean structure with an independent positivity theorem.

This remains a negative result for the primary question. Mathia still does not yet contain a geometric structure whose own positivity yields the global Weil form. The value of `WP-322` is to remove the most canonical exact cross-gap scalar escape without confusing numerical arithmetic information with an arithmetic origin of positivity.

## References

- Jim Agler and N. J. Young, *Boundary Nevanlinna-Pick interpolation via reduction and augmentation*, Mathematische Zeitschrift 268 (2011), 791--817, DOI `10.1007/s00209-010-0696-3`, arXiv:`0905.4759`.
