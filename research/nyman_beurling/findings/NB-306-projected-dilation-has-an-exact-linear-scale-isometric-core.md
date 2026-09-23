# NB-306 — projected dilation has an exact linear-scale isometric core

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-305
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + INTEGER-DILATION + FINITE-SECTION + SINGULAR-SPECTRUM + EXACT-THRESHOLD + MOVING-CUTOFF + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\]

with the convention `U_r={0}` for `r<2`, and let `A_m` be the normalized integer dilation from `NB-290`,

\[
(A_mf)(x)=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\]

For integers `N>=2` and `m>=2`, set

\[
q:=\left\lfloor\frac Nm\right\rfloor.
\]

Then the canonical Nyman section has the exact finite-section intersection law

\[
\boxed{
A_mU_N\cap U_N=A_mU_q.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
\{v\in U_N:A_mv\in U_N\}=U_q.
}
\tag{2}
\]

For the projected-dilation operator isolated in `NB-299` and `NB-305`,

\[
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\tag{3}
\]

this identifies the complete unit right-singular subspace:

\[
\boxed{
\ker(I-T_{N,m}^*T_{N,m})=U_q.
}
\tag{4}
\]

The canonical generators are finitely linearly independent, so

\[
\dim U_q=\max\{q-1,0\}.
\]

Hence singular value `1` has multiplicity exactly `max{floor(N/m)-1,0}`, and the operator norm has the sharp threshold

\[
\boxed{
\beta_{N+1}(m)=1
\iff
2m\le N,
}
\tag{5}
\]

while

\[
\boxed{
2m>N
\quad\Longrightarrow\quad
\beta_{N+1}(m)<1.
}
\tag{6}
\]

Thus the linear-scale plateau is not only a sufficient inclusion regime: `m=N/2` is the exact point at which the unit singular core disappears. Together with the superquadratic decay from `NB-303`, the unresolved generic source-overlap problem is now quantitative rather than qualitative: determine how far below `1` the largest singular value lies throughout `N/2<m\lesssim N^2`.

## 1. Finite linear independence of the canonical generators

The canonical Bagchi generators are

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\}.
\tag{7}
\]

On the reciprocal shell

\[
I_k=(1/(k+1),1/k],
\]

`NB-301`--`NB-304` use the exact constant value

\[
g_j|_{I_k}=r_j(k),
\qquad
r_j(k)=\frac{k\bmod j}{j}.
\tag{8}
\]

Suppose for some finite `M` that

\[
\sum_{j=2}^{M}a_jg_j=0
\quad\text{in }L^2(0,1).
\tag{9}
\]

Because the left-hand side is constant on the interior of every shell, (9) gives

\[
b_k:=\sum_{j=2}^{M}a_jr_j(k)=0
\qquad(k\ge1).
\tag{10}
\]

For `k>=2`, the shell sequence satisfies

\[
r_j(k)-r_j(k-1)
=
\frac1j-\mathbf 1_{j\mid k}.
\tag{11}
\]

Therefore, with

\[
C:=\sum_{j=2}^{M}\frac{a_j}{j},
\]

subtracting consecutive equations in (10) yields

\[
0=b_k-b_{k-1}
=C-\sum_{\substack{2\le j\le M\\ j\mid k}}a_j.
\tag{12}
\]

Choose a prime `p>M`. No index `2<=j<=M` divides `p`, so (12) gives `C=0`. Hence for every `2<=k<=M`,

\[
\sum_{\substack{2\le j\le M\\ j\mid k}}a_j=0.
\tag{13}
\]

These divisor equations are triangular. For `k=2`, (13) gives `a_2=0`; if `a_2,...,a_{k-1}=0`, every proper divisor of `k` has already vanished and (13) gives `a_k=0`. Thus all coefficients are zero. Consequently

\[
\boxed{
\{g_2,\ldots,g_M\}\text{ is linearly independent for every finite }M.
}
\tag{14}
\]

In particular,

\[
\dim U_M=M-1
\qquad(M\ge2).
\tag{15}
\]

This elementary shell proof is included here because exactness of the intersection below needs more than the one-sided inclusion previously used for the plateau.

## 2. Exact finite-section intersection

`NB-290` records the canonical dilation covariance

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{16}
\]

First take `v in U_q`. If `q<2`, there is nothing to prove. If `q>=2`, then `mq<=N`, which also implies `m<=N/2<=N`. Thus for every `2<=j<=q`, both `g_(mj)` and `g_m` belong to `U_N`, and (16) gives

\[
A_mU_q\subseteq U_N.
\tag{17}
\]

Since trivially `A_mU_q subset A_mU_N`, this proves

\[
A_mU_q\subseteq A_mU_N\cap U_N.
\tag{18}
\]

For the reverse inclusion, write an arbitrary `v in U_N` uniquely as

\[
v=\sum_{j=2}^{N}a_jg_j.
\]

Equation (16) gives

\[
A_mv
=
\sqrt m
\left(
\sum_{j=2}^{N}a_jg_{mj}
-
\left(\sum_{j=2}^{N}\frac{a_j}{j}\right)g_m
\right).
\tag{19}
\]

Assume `A_mv in U_N`. In the finite linear relation obtained by subtracting a representation of `A_mv` in `g_2,...,g_N`, every generator `g_(mj)` with `mj>N` occurs only in the first sum of (19): the indices `mj` are distinct, none equals `m`, and none lies among `2,...,N`. Finite linear independence therefore forces

\[
a_j=0
\qquad(mj>N).
\tag{20}
\]

Equivalently, `a_j=0` for every `j>floor(N/m)=q`, so `v in U_q`. Hence

\[
\{v\in U_N:A_mv\in U_N\}=U_q,
\]

which proves (2). Since `A_m` is an isometry and therefore injective, applying it gives the exact intersection (1).

The compensating `g_m` term in (19) does not create hidden unit directions above the cutoff. When `m<=N` it already lies in the old section and cannot cancel any `g_(mj)` with `mj>N`; when `m>N` it is itself outside the section but still has an index distinct from every `mj`, so finite independence again prevents a cancellation.

## 3. Exact unit singular subspace and sharp threshold

For every `v in U_N`, orthogonal projection gives

\[
\|T_{N,m}v\|_2
=
\|P_{U_N}A_mv\|_2
\le
\|A_mv\|_2
=
\|v\|_2.
\tag{21}
\]

Equality in (21) holds exactly when projection loses no component, namely exactly when

\[
A_mv\in U_N.
\tag{22}
\]

By (2), this is equivalent to `v in U_q`. Since `I-T^*T` is positive,

\[
\|T v\|=\|v\|
\iff
\langle(I-T^*T)v,v\rangle=0
\iff
(I-T^*T)v=0.
\]

Therefore

\[
\ker(I-T_{N,m}^*T_{N,m})=U_q,
\]

proving (4). By (15), the multiplicity of singular value `1` is exactly

\[
\max\left\{\left\lfloor\frac Nm\right\rfloor-1,0\right\}.
\tag{23}
\]

If `2m<=N`, then `q>=2`, so (4) contains a nonzero unit singular vector and `T_(N,m)` has norm exactly `1`. Conversely, if `2m>N`, then `q<2` and (4) says there is no nonzero vector on which equality holds in (21). Because `U_N` is finite-dimensional, the norm of `T_(N,m)` is attained on its unit sphere. A contraction whose norm were `1` would therefore have a nonzero unit singular vector, contradicting (4). Hence `beta_(N+1)(m)<1`.

This proves both directions of (5)--(6). It also gives the exact staircase of unit multiplicities before the threshold, rather than merely a lower bound on them.

## 4. Consequence for the linear-to-quadratic window

`NB-303` proves the universal source-side upper bound

\[
\frac{m}{N^2}\longrightarrow\infty
\quad\Longrightarrow\quad
\beta_{N+1}(m)\longrightarrow0.
\tag{24}
\]

`NB-304` shows that the quadratic exponent is power-sharp for support localization, while `NB-305` shows that its adjacent-cancellation witness is nevertheless asymptotically self-orthogonal under dilation. The exact threshold above now resolves the qualitative lower edge completely:

\[
\boxed{
2m\le N:\ \beta_{N+1}(m)=1,
\qquad
2m>N:\ \beta_{N+1}(m)<1,
\qquad
m/N^2\to\infty:\ \beta_{N+1}(m)\to0.
}
\tag{25}
\]

Thus there is no accidental continuation of the unit plateau after the obvious multiplicative core disappears. The remaining generic source-side question is a **gap problem**:

\[
\text{quantify }1-\beta_{N+1}(m)
\quad\text{for}\quad
N/2<m\lesssim N^2.
\tag{26}
\]

This is sharper than asking whether decay can begin in that window: strict contraction begins immediately once `m>N/2`, but no uniform or asymptotic rate follows from the present argument. In particular, (6) is compatible with `beta_(N+1)(m)` remaining arbitrarily close to `1` along moving sequences just above the linear threshold.

The result also explains the apparent tension with `NB-305`. High-index adjacent cancellations can lose self-correlation while lower-index directions still carry exact unit singular values for `2m<=N`; after that core disappears, compactness guarantees only a strict gap, not its size.

## 5. Adversarial and prior-art audit

The exactness argument has three potentially fragile points. First, finite linear independence is proved directly from the actual reciprocal-shell values in (8)--(15), rather than assumed from Gram nonsingularity. Second, the covariance expansion (19) cannot hide a high-index `g_(mj)` inside the compensator because `m` is distinct from every `mj` with `j>=2`. Third, the passage from absence of equality vectors to `beta<1` uses finite dimensionality; the analogous statement would be false for a general infinite-dimensional contraction whose norm is not attained.

Boundary cases are consistent. If `q>=2`, covariance gives the old exact isometric core. If `q<2`, including `m>N`, the high-index coefficients in (19) force `v=0`, so the intersection is trivial. No quantitative lower bound for `1-beta` is claimed. The theorem remains entirely source-side: it gives no first-free sample estimate, Ford-target occupation statement, sample-Gram conditioning bound, finite-section excess estimate, Nyman-distance improvement, or implication for RH.

A fresh literature search around the Báez-Duarte integer-dilation criterion, Nyman--Beurling semigroup formulations, finite generator sections, and dilation/operator spectra found the classical discrete criterion of Báez-Duarte, Bagchi's semigroup-oriented survey, and later weighted-composition-semigroup work studying spectra and invariant subspaces. These sources establish the surrounding dilation framework, but in the material reviewed do not state the finite-section intersection law (1), the exact unit eigenspace (4), or the sharp finite-section threshold (5). No external theorem is load-bearing for the proof, so `SOURCES.md` needs no additional dependency.

## Conclusion

Integer dilation transports exactly, not merely at least, the lower canonical section that survives the multiplicative index cutoff:

\[
\boxed{
A_mU_N\cap U_N=A_mU_{\lfloor N/m\rfloor}.
}
\]

Consequently the projected operator has unit right-singular space exactly `U_floor(N/m)`, and

\[
\boxed{
\|P_{U_N}A_m|_{U_N}\|=1
\iff
2m\le N.
}
\]

The lower boundary of the source-overlap transition is therefore settled exactly. What remains between the linear and quadratic scales is no longer the existence of contraction but its quantitative strength.