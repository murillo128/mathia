# AF-385 — Sampled solid-minor hierarchy certifies continuum fixed-order total nonnegativity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `POLYA-FREQUENCY` · `TOEPLITZ` · `CERTIFICATE-COMPRESSION` · `SAMPLED-STRICT-INTERIOR` · `NO-NOVELTY-CLAIM`

## Claim

AF-384 compresses the order-`k` placement problem to solid Toeplitz minors after assuming **continuum** strict total positivity through every lower order. The finite recognition theorem used there permits a sharper resource statement: the lower-order strictness itself need only be certified on the same sampled solid-minor family.

Let

\[
K_f(u,x)=f(u-x),\qquad f:\mathbb R\to\mathbb R
\]

with `f` continuous. Fix `k\ge2`, let `h_m>0` satisfy `h_m\to0`, and for every `1\le j\le k` and `d\in\mathbb Z` define

\[
C_{j,h_m}(d)
:=
\det\!\left(f\!\left((d+a-b)h_m\right)\right)_{a,b=0}^{j-1}.
\tag{1}
\]

Assume only the sampled lower-order strictness

\[
C_{j,h_m}(d)>0
\qquad
(1\le j<k,\;m\ge1,\;d\in\mathbb Z).
\tag{2}
\]

Then the following are equivalent:

1. `K_f` is totally nonnegative through order `k` on `\mathbb R\times\mathbb R`;
2. the sampled top-order solid minors satisfy
   \[
   C_{k,h_m}(d)\ge0
   \qquad
   (m\ge1,\;d\in\mathbb Z).
   \tag{3}
   \]

Thus the entire continuum placement certificate through fixed order `k` can be reduced, inside the sampled strict-interior class `(2)`, to a **triangular one-parameter hierarchy of solid Toeplitz determinants**: strict signs at orders below `k`, and a nonnegative sign at order `k`, on any one sequence of lattice meshes tending to zero.

This removes a stronger hypothesis from AF-384. One does not need an independent proof that every lower-order continuum translation minor is strictly positive before the solid order-`k` family becomes target-complete. It is enough to prove strict positivity of the lower-order **solid sampled generators themselves**.

## Fixed-mesh derivation

Fix one mesh `h=h_m` and form the bi-infinite Toeplitz array

\[
A^{(h)}_{rs}=f((r-s)h),\qquad r,s\in\mathbb Z.
\tag{4}
\]

Take an arbitrary finite rectangular consecutive-index block `X` of this array. Grussler and Damm's Proposition 2 states that a finite matrix is `k`-positive if

- every row-initial and column-initial minor of orders `1,\ldots,k-1` is strictly positive; and
- every consecutive order-`k` minor is nonnegative.

Every such initial minor of `X` is itself solid: its row indices and column indices are consecutive. By Toeplitz translation invariance, an order-`j` solid minor with row start `r_0` and column start `s_0` has determinant

\[
\det\!\left(f\!\left((r_0-s_0+a-b)h\right)\right)_{a,b=0}^{j-1}
=
C_{j,h}(r_0-s_0).
\tag{5}
\]

Therefore `(2)` supplies **all** lower-order row/column initial minors required by Proposition 2; no unsampled or non-solid lower-order determinant is needed as an input.

Likewise every consecutive order-`k` minor of `X` is `C_{k,h}(d)` for an integer relative offset `d`, so `(3)` supplies the top-order hypothesis. Proposition 2 therefore makes every such finite block `k`-positive. Since every finite lattice minor is contained in one of these blocks,

\[
\det\bigl(f((r_a-s_b)h)\bigr)_{a,b=1}^{j}\ge0
\tag{6}
\]

for every `1\le j\le k` and every increasing integer row and column tuples.

The reverse implication at the sampled level is immediate: if the continuum kernel is `TN_k`, then every sampled solid order-`k` minor is nonnegative.

## Vanishing meshes close the continuum

Now assume `(2)` and `(3)` on every mesh `h_m`. Fix arbitrary increasing real tuples

\[
u_1<\cdots<u_j,
\qquad
x_1<\cdots<x_j,
\qquad 1\le j\le k.
\tag{7}
\]

For sufficiently large `m`, choose increasing integer tuples `r^{(m)}` and `s^{(m)}` with

\[
r_a^{(m)}h_m\to u_a,
\qquad
s_b^{(m)}h_m\to x_b.
\tag{8}
\]

The corresponding sampled determinant is nonnegative by `(6)`. Continuity of `f` and of the determinant yields

\[
\det\bigl(f(u_a-x_b)\bigr)_{a,b=1}^{j}
=
\lim_{m\to\infty}
\det\!\left(
 f\!left((r_a^{(m)}-s_b^{(m)})h_m\right)
\right)_{a,b=1}^{j}
\ge0.
\tag{9}
\]

Hence `K_f\in TN_k`. No continuum strict-positivity conclusion is needed or obtained: lower-order sampled determinants may stay positive while a limiting continuum determinant tends to zero.

This distinction is precisely why `(2)` is a weaker **verification burden** than AF-384's continuum assumption. The finite matrix theorem consumes strictness only on its initial minors, and the shrinking-grid step needs only nonnegative limits.

## Certificate-complexity consequence

The sequence AF-383--AF-385 now separates three levels of spatial information at fixed determinant order.

AF-383 works on the unrestricted continuous class and keeps one consecutive row stencil plus arbitrary column tuples. AF-384 shows that continuum strict lower-order positivity removes the arbitrary-column family at order `k`. AF-385 localizes that side information further: **the lower-order strictness needed by the finite recognition theorem is itself generated by solid lattice minors.**

At mesh `h_m`, the retained observations through order `k` are therefore only

\[
\{C_{j,h_m}(d):1\le j\le k,\ d\in\mathbb Z\},
\tag{10}
\]

with strict positivity required below the top order. Both arbitrary row geometry and arbitrary column geometry have disappeared from the input certificate. The omitted placements are reconstructed algebraically inside each finite lattice block; the continuum is reconstructed topologically by `h_m\to0`.

The compression is still not finite. The offset `d` ranges over all integers, a vanishing sequence of spatial scales is retained, and the Pólya-frequency target still requires unbounded determinant order. AF-372 remains the obstruction to replacing all-order total positivity by any fixed maximum arity on the unrestricted class.

There is also an all-order sufficient corollary. If `(1)` is strictly positive for **every** finite order `j`, every mesh `h_m`, and every integer offset `d`, then each sampled lattice is strictly totally positive on every finite block, and the vanishing-mesh closure makes `K_f` totally nonnegative of all orders. This does not imply continuum strict total positivity, because strict sampled margins can vanish in the limit.

## Riemann-facing consequence

For the Schoenberg/Gröchenig formulation in which the Laguerre--Pólya target is represented by all-order translation total positivity, AF-385 sharpens the source-side burden identified by AF-384. A prospective arithmetic proof need not first control all lower-order determinant placements. At a fixed target order `k`, it is enough to force the signs of the one-parameter solid families `(1)` through order `k` on a shrinking mesh, with strict signs below the top order.

This is a target-certificate reduction, not an RH argument. The theorem gives no arithmetic reason that the relevant Riemann-associated kernel satisfies `(2)` or `(3)`, does not remove the need for arbitrarily high order, and does not identify rational-prime provenance. In particular, a proof that the solid determinants are positive remains the substantive source-side problem.

The distinction from recent Riemann `xi` coefficient results is unchanged. Consecutive Toeplitz minors of a coefficient sequence live in a different matrix model; they do not automatically supply the translation-kernel families `(1)`, the shrinking-mesh hypothesis, or the all-order signs needed for the Schoenberg target.

## Prior-art and novelty audit

- Christian Grussler and Tobias Damm, **“Efficient `k`-Sign Consistency Verification of Hankel Matrices via Schur Polynomials,”** arXiv:`2602.08122` (8 February 2026), especially Proposition 2. Role: exact finite-matrix recognition theorem used here. Their proposition requires positive lower-order row/column initial minors and nonnegative consecutive order-`k` minors; it does **not** require prior knowledge of all lower-order minors. This distinction is the key sharpening relative to AF-384.
- Allan Pinkus, ***Totally Positive Matrices***, Cambridge University Press (2009; online 2010), Chapter 2. Role: classical Fekete/initial-minor recognition background and the strict-versus-nonnegative boundary underlying Proposition 2.
- Sergey Fomin and Andrei Zelevinsky, **“Double Bruhat Cells and Total Positivity,”** *Journal of the American Mathematical Society* **12** (1999), 335--380. Role: classical total-positivity criteria and explicit discussion of Fekete's solid-minor criterion in the strict setting; confirms that solid-minor compression is established finite-matrix mathematics rather than a new principle.
- I. J. Schoenberg and A. M. Whitney, **“On Pólya Frequency Functions. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves,”** *Transactions of the American Mathematical Society* **74** (1953), 246--259, DOI `10.2307/1990881`. Role: classical translation-determinant target class.

The finite recognition mechanism is classical prior art. The shrinking-lattice passage is an elementary closure argument, and no novelty is claimed for the resulting theorem. The durable Arithmetic Fidelity contribution is the **resource accounting**: the strict side information required to compress order-`k` placement need not consist of the full continuum lower-order determinant family; it can itself be reduced to the sampled solid generators.

## Boundaries and falsification checks

The strict inequalities in `(2)` are load-bearing for this argument. Replacing them by mere nonnegativity does not satisfy Proposition 2 and would silently cross the delicate boundary between strict total positivity and total nonnegativity.

The result does not claim that sampled lower-order strictness implies continuum lower-order strictness. The closure only gives nonnegative continuum minors, and this is sufficient for the stated `TN_k` target.

A sequence of meshes tending to zero is essential for an unrestricted continuous profile. One fixed lattice leaves between-grid freedom unless separate regularity or uniqueness information is added.

The certificate compresses placement, not arity, scale, or source identity. It therefore does not conflict with AF-372's finite-order false positives, AF-374's fixed-lattice gauge obstruction, or the source-identification boundary of AF-370.

Finally, the theorem is source-independent. Uniform lattices and classical matrix recognition do not create rational-prime discrimination. Any arithmetic use must still derive the solid-minor signs from the source rather than assume them.