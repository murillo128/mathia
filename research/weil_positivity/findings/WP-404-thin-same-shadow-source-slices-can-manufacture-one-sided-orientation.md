---
id: WP-404
title: Thin same-shadow source slices can manufacture one-sided orientation
branch: weil_positivity
status: supported
kind: compact-operator-matched-control-infinite-codimension-one-sided-fixed-shadow-orientation
claim_strength: exact RH-independent matched-control sharpness result for WP-403; a one-dimensional centered same-shadow source slice can carry a nonzero bounded linear orientation because its order-bounded tangent core is trivial, so orientation on a thin infinite-codimensional slice is not by itself arithmetic evidence
created: 2026-09-22
related: [WP-401, WP-402, WP-403]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - B. Blackadar, Operator Algebras: Theory of C*-Algebras and von Neumann Algebras, Springer (2006), hereditary C*-subalgebras and conditional expectations
---

# WP-404 — Thin same-shadow source slices can manufacture one-sided orientation

## Claim

`WP-403` proves that a closed finite-codimensional source slice cannot create a nonzero closable linear orientation from fixed-shadow positivity: the order-bounded two-sided tangent core remains dense after finitely many linear constraints. The finite-codimension hypothesis is genuinely essential.

There is an explicit non-arithmetic compact-operator model with a **one-dimensional**, hence infinite-codimensional, centered same-shadow source slice `F` and a nonzero bounded linear map

\[
T:F\to\mathbb R
\]

such that

\[
d+h\ge0,\qquad h\in F
\quad\Longrightarrow\quad
T(h)\ge0.
\tag{1}
\]

The mechanism is not a hidden arithmetic sign. The slice is chosen along a singular positive endpoint whose order-bounded tangent core is trivial. Its positive fixed-shadow fibre is exactly a one-sided interval.

This supplies a matched control and a canonicity gate for the surviving linear escape after `WP-403`: merely finding a nonzero orientation on a thin or infinite-codimensional source relation is not evidence for Weil positivity. A viable arithmetic construction must explain why the thin relation and its endpoint are intrinsic to the source, survive analogous non-arithmetic controls, and still recover the finite-prime plus archimedean/global Weil coefficients.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + COMPACT-OPERATOR-MATCHED-CONTROL + CONDITIONAL-EXPECTATION + SAME-SHADOW + ONE-DIMENSIONAL-SOURCE-SLICE + INFINITE-CODIMENSION + ONE-SIDED-POSITIVE-FIBRE + TRIVIAL-ORDER-BOUNDED-TANGENT-CORE + BOUNDED-LINEAR-ORIENTATION + SHARPNESS-OF-WP-403 + CANONICITY-GATE + NOT-A-WEIL-BRIDGE`.

## 1. A compact-operator fixed-shadow model

Let

\[
H=\ell^2(\mathbb N),
\qquad
A=K(H),
\]

with standard basis `e_n`, indexed by `n>=1`. Let `B=c_0` be the diagonal compact operators and let

\[
E:A\to B
\]

be the diagonal conditional expectation. Define

\[
v_n=2^{-n/2},
\qquad
v=(v_n)_{n\ge1}.
\tag{2}
\]

Because `sum 2^{-n}=1`, `v` is a unit vector. Set

\[
d=\operatorname{diag}(2^{-n})\in B_+,
\qquad
\rho=|v\rangle\langle v|\in A_+,
\qquad
k=\rho-d.
\tag{3}
\]

The diagonal of `rho` is exactly `d`, hence

\[
E(\rho)=d,
\qquad
E(k)=0.
\tag{4}
\]

Moreover `d` generates the whole compact-operator algebra hereditarily. Indeed for every matrix unit `e_{ij}`,

\[
d e_{ij}d=2^{-(i+j)}e_{ij},
\tag{5}
\]

so all finite-rank operators lie in the algebraic span of `dAd`, and therefore

\[
\operatorname{Her}_A(d)=\overline{dAd}=K(H).
\tag{6}
\]

Thus `k` lies in the centered tangent space

\[
V_d=\{h\in K(H)_{\rm sa}:E(h)=0\}.
\tag{7}
\]

Take the closed real source slice

\[
F=\mathbb R k.
\tag{8}
\]

The ambient space `V_d` is infinite dimensional: the self-adjoint off-diagonal operators `e_{1n}+e_{n1}`, `n>=2`, are linearly independent elements of it. Hence the one-dimensional `F` has infinite codimension.

For every real `t`,

\[
E(d+tk)=d.
\tag{9}
\]

So the entire line is a genuine same-shadow fibre.

## 2. The positive fibre is exactly one-sided

Using `k=rho-d`,

\[
d+tk=(1-t)d+t\rho.
\tag{10}
\]

We claim

\[
\boxed{d+tk\ge0\quad\Longleftrightarrow\quad 0\le t\le1.}
\tag{11}
\]

If `0<=t<=1`, (10) is a convex combination of the positive operators `d` and `rho`, so positivity is immediate.

If `t>1`, choose a nonzero finite-support vector `x` orthogonal to `v`; for example

\[
x=v_2e_1-v_1e_2.
\tag{12}
\]

Then `rho x=0` while `\langle dx,x\rangle>0`, and therefore

\[
\langle(d+tk)x,x\rangle
=(1-t)\langle dx,x\rangle<0.
\tag{13}
\]

Hence positivity fails for `t>1`.

Now let `t=-s<0`. Positivity would give

\[
(1+s)d-s\rho\ge0,
\]

or equivalently

\[
\rho\le\frac{1+s}{s}d.
\tag{14}
\]

No finite constant can dominate `rho` by `d`. For each `N`, define the finite-support vector

\[
x^{(N)}_n=
\begin{cases}
1/v_n=2^{n/2},&1\le n\le N,\\
0,&n>N.
\end{cases}
\tag{15}
\]

Then

\[
\langle\rho x^{(N)},x^{(N)}\rangle=N^2,
\qquad
\langle d x^{(N)},x^{(N)}\rangle=N.
\tag{16}
\]

The ratio is `N` and is unbounded, contradicting (14) for sufficiently large `N`. This proves (11).

## 3. A nonzero bounded linear orientation now exists

Define

\[
T:F\to\mathbb R,
\qquad
T(tk)=t.
\tag{17}
\]

Since `F` is one dimensional and `k` is nonzero, `T` is bounded, hence closed and closable. By (11), every positive fixed-shadow perturbation in `F` has `0<=t<=1`, so

\[
d+tk\ge0
\quad\Longrightarrow\quad
T(tk)=t\ge0.
\tag{18}
\]

Thus the pointed cone `R_+` really does orient a nonzero linear readout on this source slice. There is no contradiction with `WP-403`: the slice has infinite codimension, and the order-bounded tangent mechanism used there fails maximally.

## 4. The order-bounded tangent core inside the slice is trivial

Recall the `WP-403` core

\[
\mathcal P_d
=\{h\in V_d:\exists M<\infty,\ -Md\le h\le Md\}.
\tag{19}
\]

Here

\[
\boxed{F\cap\mathcal P_d=\{0\}.}
\tag{20}
\]

Suppose first that `t>0` and `tk<=Md`. Since `k=rho-d`, this implies

\[
\rho\le\left(1+\frac Mt\right)d,
\tag{21}
\]

which is impossible by the vectors (15)--(16). If `t<0`, write `t=-s` with `s>0`. The lower order bound `-Md<=tk=-sk` implies `sk<=Md`, and again

\[
\rho\le\left(1+\frac Ms\right)d,
\tag{22}
\]

which is impossible. Therefore only `t=0` can be order bounded by `d` in both signs.

This identifies the exact escape from `WP-403`. In finite codimension, order-bounded tangents can be repaired back into the constrained slice and remain dense. In the present thin slice, there is not even one nonzero order-bounded direction to repair. Fixed-shadow positivity is consequently one-sided at the origin and no longer forces `T(k)` and `-T(k)` into the same pointed cone.

## 5. Finite-dimensional truncations expose the singular limit

The one-sidedness is not already present at every finite matrix size. Let `H_N=span(e_1,...,e_N)` and let `d_N`, `rho_N`, and `k_N=rho_N-d_N` be the corresponding compressions. Because `d_N` is invertible,

\[
d_N^{-1/2}(d_N+t k_N)d_N^{-1/2}
=(1-t)I+t uu^*,
\tag{23}
\]

where `u=(1,...,1)` in `C^N`. The eigenvalues are

\[
1-t
\quad\text{with multiplicity }N-1,
\qquad
1+(N-1)t
\quad\text{along }u.
\tag{24}
\]

Therefore

\[
\boxed{d_N+t k_N\ge0
\quad\Longleftrightarrow\quad
-\frac1{N-1}\le t\le1}
\qquad(N\ge2).
\tag{25}
\]

Every finite truncation retains a small negative tangent interval. Its left endpoint tends to zero as `N` grows, and the infinite-dimensional fibre becomes exactly `[0,1]`. The orientation is therefore produced by an infinite-dimensional singular endpoint, not by a finite-dimensional positive-cone asymmetry hidden in the notation.

This is also a useful diagnostic for numerical experiments. A finite cutoff can misleadingly suggest a small two-sided neighbourhood even though the limiting source slice is genuinely one-sided.

## 6. Consequence for the surviving Mathia route

The construction is deliberately non-arithmetic. No primes, explicit formula, Bost--Connes dynamics, or archimedean term enter it. That is the point: it is a matched control showing that the bare statement

> a thin same-shadow source relation admits a nonzero closable linear orientation from positivity

is too weak to identify the missing Weil sign mechanism.

After `WP-403`, infinite codimension and singular operator domains remain legitimate places where a source-native global relation could carry information destroyed by hereditary localization. `WP-404` does not close those routes. It instead raises the evidentiary threshold. If an arithmetic construction uses a thin slice, a singular domain, or a one-sided admissible fibre, it must identify a source-forced reason for that geometry. Otherwise one can manufacture the same orientation in the generic compact-operator model above simply by choosing a positive endpoint `rho` with the same diagonal shadow as `d`.

For the accepted Bost--Connes completion clue, this means that an eventual source relation cannot be credited merely because it defeats `WP-402`--`WP-403` and yields a sign. It must also survive a **canonicity control**: replacing the arithmetic source by a matched non-arithmetic same-shadow model must destroy the purported coefficient/sign mechanism, or the proposal has not yet isolated arithmetic content. The finite-prime and archimedean/global normalization obligations of the canonical mandate remain untouched.

## 7. Prior-art, novelty, and adversarial audit

The operator-algebra ingredients are standard: diagonal expectation on compact operators, hereditary generation by a strictly positive compact diagonal, and elementary order comparison. The unbounded ratio in (16) is the concrete rank-one obstruction to an inequality `rho<=Cd`; no external theorem is needed for the proof.

A repository novelty search against the current `weil_positivity` findings found no existing same-shadow rank-one control with an exact one-sided fibre or a proof that the finite-codimensional boundary in `WP-403` is sharp. The delta is therefore not a new theorem about compact operators; it is the explicit **matched control** at the newly exposed research boundary.

The main adversarial failure modes are visible in the construction itself. First, `F` is hand-picked from `rho`, so the orientation is manufactured rather than canonical. Second, the sign is only scalar and carries none of the Weil coefficients. Third, finite truncations have a negative interval, so a finite computation cannot by itself certify the limiting one-sided geometry. These are limitations, not hidden assumptions, and they are exactly why the example functions as a falsification/control result rather than a positive bridge.

## 8. Boundary and decisive audit test

`WP-404` does not say that every infinite-codimensional source slice admits an orientation, nor that every singular domain escapes `WP-402`. It only proves that finite codimension in `WP-403` cannot be dropped without replacement: a closed infinite-codimensional slice can avoid the dense two-sided tangent core completely.

The decisive audit for future thin-slice proposals is therefore two-stage. First determine whether the source relation retains a dense order-bounded two-sided tangent core; if it does, the existing no-go machinery applies. If it does not, exhibit the intrinsic source structure that selects the surviving one-sided or singular geometry and compare it against matched non-arithmetic controls of the type above. Only after that can a resulting orientation count as evidence toward the canonical Weil-positivity objective.

The exact conclusion is narrow but useful: **thin same-shadow geometry can manufacture orientation for generic reasons, so thinness is an escape from the previous obstruction, not evidence of the desired arithmetic sign.**
