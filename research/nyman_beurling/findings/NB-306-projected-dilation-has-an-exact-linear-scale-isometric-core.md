# NB-306 — projected dilation has an exact linear-scale isometric core

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-305
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + INTEGER-DILATION + FINITE-SECTION + SINGULAR-SPECTRUM + MOVING-CUTOFF + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\}
\]

and let `A_m` be the normalized integer dilation from `NB-290`,

\[
(A_mf)(x)=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\]

For integer `m>=2`, set

\[
q:=\left\lfloor\frac Nm\right\rfloor.
\]

Then the canonical Nyman section contains an exact isometric copy of its lower-index core:

\[
\boxed{
A_mU_q\subseteq U_N.
}
\tag{1}
\]

Consequently, for the projected-dilation operator isolated in `NB-299` and `NB-305`,

\[
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\tag{2}
\]

we have

\[
\boxed{
T_{N,m}v=A_mv,
\qquad
T_{N,m}^*T_{N,m}v=v
\quad(v\in U_q).
}
\tag{3}
\]

Hence singular value `1` has right singular subspace containing `U_q` and multiplicity at least `dim U_q`. In particular,

\[
\boxed{
2m\le N
\quad\Longrightarrow\quad
\beta_{N+1}(m)=1.
}
\tag{4}
\]

Thus projected dilation has an **exact linear-scale plateau**: no operator-norm decay is possible anywhere in the integer-dilation regime `m<=N/2`. Together with the superquadratic decay from `NB-303`, this brackets the unresolved generic source-overlap transition between linear and quadratic scales.

## 1. Exact finite-section inclusion

`NB-290` records the canonical dilation covariance

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{5}
\]

Take `2<=j<=q=floor(N/m)`. Then `mj<=N`. Since `m>=2` and `q>=2` whenever the core is nontrivial, also `m<=N`, so both `g_(mj)` and `g_m` belong to `U_N`. Equation (5) therefore gives

\[
A_mg_j\in U_N
\qquad(2\le j\le q).
\]

By linearity,

\[
A_mU_q\subseteq U_N,
\]

which proves (1).

This is not the statement that the full section `U_N` is dilation invariant. The inclusion loses all generators with index above `floor(N/m)`. It identifies the maximal obvious canonical core on which the multiplicative index map `j -> mj` remains inside the same finite section.

## 2. Unit singular-value plateau

For `v in U_q`, equation (1) makes the projection in (2) inactive:

\[
T_{N,m}v
=P_{U_N}A_mv
=A_mv.
\tag{6}
\]

The normalized dilation `A_m` is an isometry, hence

\[
\|T_{N,m}v\|_2=\|v\|_2
\qquad(v\in U_q).
\tag{7}
\]

On all of `U_N`, `T_{N,m}` is a contraction because it is an orthogonal projection composed with an isometry. Therefore

\[
I-T_{N,m}^*T_{N,m}\succeq0.
\]

For `v in U_q`, equation (7) gives

\[
\left\langle
(I-T_{N,m}^*T_{N,m})v,v
\right\rangle=0.
\]

A positive operator has zero quadratic form on `v` only when it annihilates `v`, so

\[
T_{N,m}^*T_{N,m}v=v.
\]

This proves (3). The corresponding left singular vectors are the isometric images `A_mU_q subset U_N`.

If `2m<=N`, then `q>=2` and `U_q` contains the nonzero generator `g_2`. Thus `T_(N,m)` has norm at least `1`; since it is already a contraction,

\[
\beta_{N+1}(m)=1,
\]

proving (4).

More generally, the theorem gives a staircase of exact unit singular directions: whenever `floor(N/m)=q>=2`, the entire lower section `U_q` survives projection without any norm loss. No linear-independence assertion about the displayed generators is needed; the safe multiplicity statement is `dim U_q`.

## 3. What this changes after NB-303–NB-305

`NB-303` proves the universal source-side upper bound

\[
\frac{m}{N^2}\longrightarrow\infty
\quad\Longrightarrow\quad
\beta_{N+1}(m)\longrightarrow0.
\tag{8}
\]

`NB-304` then shows that the quadratic exponent is power-sharp for **support localization**, while `NB-305` shows that its explicit adjacent-cancellation witness is nevertheless asymptotically self-orthogonal under dilation. That left open whether the actual cross-correlation operator might already become small far below `N^2`.

Equation (4) gives the first exact lower boundary for that question:

\[
\boxed{
 m\le N/2:\ \beta_{N+1}(m)=1,
\qquad
 m/N^2\to\infty:\ \beta_{N+1}(m)\to0.
}
\tag{9}
\]

So the projected-dilation transition cannot occur below linear scale. The remaining generic source-side window is genuinely intermediate,

\[
N\lesssim m\lesssim N^2,
\tag{10}
\]

up to constants at the lower edge and the asymptotic nature of the upper edge.

This also resolves an apparent tension with `NB-305`. Its high-index adjacent cancellation can lose its self-correlation while `T_(N,m)` still has norm exactly one, because the norm is carried by a **different, lower-index core** `U_floor(N/m)`. For `m=N^(2-eta)` that core is eventually trivial when `eta<1`, so `NB-305` probes beyond the exact plateau; for `m=o(N)`, by contrast, the isometric core grows and operator-norm decay is impossible.

A useful way to read (3) is that the singular-spectrum problem is already partially solved at the bottom: before any arithmetic cancellation estimate is invoked, the multiplication table of the canonical indices forces a block of singular values to be pinned exactly at one. Any future upper bound for `beta` must therefore begin only after this finite-section semigroup core disappears.

## 4. Adversarial and prior-art audit

The proof uses only three ingredients already established in the line: the exact covariance (5), the nested canonical sections, and the isometry of `A_m`. The index check is essential: `g_m` belongs to `U_N` because the nontrivial-core assumption `q>=2` implies `m<=N/2<N`, while `g_(mj)` belongs to `U_N` because `j<=floor(N/m)`. No statement is made for `m>N/2`, where this particular nonzero core vanishes.

The step from norm preservation to `T^*T v=v` uses positivity of `I-T^*T`; it is stronger than merely observing one Rayleigh quotient. Conversely, nothing here proves that the unit singular subspace is **exactly** `U_q`, nor that its multiplicity equals the number of displayed generators. Additional accidental unit directions could exist, and no linear-independence count is required for the theorem.

A fresh prior-art search around Nyman--Beurling integer dilations, finite generator sections, semigroup formulations, and multiplicative Gram ladders found the classical integer-dilation/discrete framework surveyed by Bagchi and established in the Báez-Duarte strengthening, together with recent work of Carvill on Gram decay along multiplicative ladders. Those sources support the surrounding dilation viewpoint but, in the material reviewed, do not state the finite-section inclusion (1) or the resulting exact unit-singular-value plateau (4). No external theorem is load-bearing here, so `SOURCES.md` requires no new dependency.

The result remains entirely source-side. It gives no first-free sample estimate, no Ford-target occupation statement, no control of sample-Gram conditioning, no finite-section excess bound, and no implication for the Nyman distance or RH. In particular, `beta=1` below linear scale says only that **some** source directions survive projected dilation isometrically; the relevant target may be orthogonal to them.

## Conclusion

The bilinear question left by `NB-305` does have a rigid obstruction, but it comes from a simpler place than the quadratic tail witness. Integer dilation transports the whole lower canonical section `U_floor(N/m)` exactly inside `U_N`, so projected dilation cannot contract that core at all. Therefore

\[
\boxed{
2m\le N
\Longrightarrow
\|P_{U_N}A_m|_{U_N}\|=1.
}
\]

Combined with `NB-303`, the unknown source-overlap transition is now bracketed between **linear** and **quadratic** multiplicative scales. The next discriminating problem is no longer whether decay can begin below linear scale—it cannot—but how rapidly the unit core disappears and the largest singular value falls in the intermediate window `N/2<m\lesssim N^2`, before target-aware information is brought back in.