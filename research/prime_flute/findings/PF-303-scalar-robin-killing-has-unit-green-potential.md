# PF-303 — scalar Robin killing has exactly unit Green potential

**Status:** `EXACT-DERIVED + CLASSICAL-MATRIX-MECHANISM + POSITIVE/ROUTE-NARROWING`.

PF-297 shows that the canonical fixed-axis Robin inverse is nonamplifying but has no depth-uniform contraction gap. PF-298--PF-302 then isolate the constant-boundary response of each neighboring pant as a positive conductance edge with two strictly positive shifted-killing terms, and show that scalar bidirectional attenuation accumulates. Those results still leave the accepted source-weighted-return clue without the requested Green-potential certificate.

On every finite chain of these **scalar constant-mode pant compressions**, the missing positive-potential calculation is in fact exact. After assembling the local killed-conductance matrices, the Robin killing vector is precisely the row deficit of the finite return kernel. Its Green potential is the constant vector:

\[
\boxed{G_N d=\mathbf 1.}
\]

Equivalently, after the natural diagonal normalization, if `K_N` is the substochastic scalar return kernel and `\delta_N=(I-K_N)\mathbf 1` is its row-deficit vector, then

\[
\boxed{\sum_{m\ge0}K_N^m\delta_N=\mathbf 1.}
\]

Thus any nonnegative scalar forcing dominated by the local escape budget, `0\le \xi_N\le C\delta_N`, has uniformly bounded return potential

\[
\boxed{\sum_{m\ge0}K_N^m\xi_N\le C\mathbf 1}
\]

with **no uniform spectral-gap assumption**. The source-weighted mechanism requested by the accepted clue therefore exists exactly on the assembled scalar killed-conductance chain. What remains open is the genuinely physical step: whether the actual energy-normalized `P/H` mixed forcing and its nonconstant-mode reassembly can be put in a currency dominated by this deficit, or by a comparable excessive majorant.

This is not an arithmetic spectral invariant. The identity is a generic finite killed-network fact and survives constant, shuffled, and surrogate pant data. Its value is route-narrowing: it identifies the exact scalar source currency that compensates arbitrarily long nearly conservative returns and moves the unresolved gate from "find a scalar Green majorant" to "compare the actual mixed forcing/reassembly with scalar killing."

## Claim

For `n=1,\ldots,N`, let the PF-298 constant-boundary compression of the `n`th pant be

\[
M_n
=
c_n
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}
+
\operatorname{diag}(\kappa_{n,L},\kappa_{n,R}),
\qquad
c_n>0,
\quad
\kappa_{n,L},\kappa_{n,R}>0.
\tag{1}
\]

Assemble the pants along scalar cuff variables `u_0,\ldots,u_N`. The finite-chain quadratic form is

\[
\mathcal E_N(u)
=
\sum_{n=1}^{N}
\left[
 c_n|u_{n-1}-u_n|^2
 +\kappa_{n,L}|u_{n-1}|^2
 +\kappa_{n,R}|u_n|^2
\right]
=u^*H_Nu.
\tag{2}
\]

Write

\[
H_N=L_{c,N}+D_N,
\qquad
D_N=\operatorname{diag}(d_0,\ldots,d_N),
\tag{3}
\]

where `L_{c,N}` is the weighted path Laplacian and

\[
\boxed{
 d_0=\kappa_{1,L},
\qquad
 d_j=\kappa_{j,R}+\kappa_{j+1,L}\quad(1\le j\le N-1),
\qquad
 d_N=\kappa_{N,R}.
}
\tag{4}
\]

Then `H_N` is positive definite, its inverse `G_N=H_N^{-1}` is entrywise nonnegative, and

\[
\boxed{H_N\mathbf 1=d,
\qquad
G_Nd=\mathbf 1.}
\tag{5}
\]

By symmetry also

\[
\boxed{d^TG_N=\mathbf 1^T.}
\tag{6}
\]

Consequently, for every nonnegative scalar source `f`,

\[
\boxed{d^TG_Nf=\mathbf 1^Tf,}
\tag{7}
\]

and if `0\le f\le Cd` componentwise then

\[
\boxed{0\le G_Nf\le C\mathbf 1.}
\tag{8}
\]

There is an equivalent return-kernel form. Put

\[
a_j=d_j+\sum_{k\sim j}c_{jk},
\qquad
A_N=\operatorname{diag}(a_j),
\qquad
K_N:=I-A_N^{-1}H_N.
\tag{9}
\]

Then `K_N\ge0`, each row sum is at most one, and

\[
\boxed{
\delta_N:=(I-K_N)\mathbf1=A_N^{-1}d.
}
\tag{10}
\]

Moreover `\rho(K_N)<1`, so

\[
\boxed{
(I-K_N)^{-1}\delta_N
=\sum_{m\ge0}K_N^m\delta_N
=\mathbf1.
}
\tag{11}
\]

Hence every `0\le\xi_N\le C\delta_N` obeys

\[
\boxed{
\sum_{m\ge0}K_N^m\xi_N\le C\mathbf1.
}
\tag{12}
\]

Equations (11)--(12) are exactly the source-adapted excessive-potential mechanism asked for in the accepted clue, but only for the scalar constant-mode assembled chain.

## 1. Assembly exposes the exact killing currency

The conductance part of every local matrix in (1) annihilates equal constants. When two neighboring pants are glued at an interior scalar cuff, their diagonal killing terms simply add. This gives (2)--(4), and because a graph Laplacian annihilates constants,

\[
L_{c,N}\mathbf1=0.
\tag{13}
\]

Therefore

\[
H_N\mathbf1=D_N\mathbf1=d,
\tag{14}
\]

which is the first identity in (5). This is the key point: the vector of shifted Robin losses is not merely a convenient positive weight. It is **exactly the defect of the conservative conductance operator on the constant function**.

Every `\kappa_{n,\pm}` is strictly positive by PF-298, so `d_j>0` here. In particular

\[
u^*H_Nu
=
\sum_n c_n|u_{n-1}-u_n|^2+\sum_jd_j|u_j|^2>0
\]

for nonzero `u`; `H_N` is positive definite.

## 2. Positivity of the Green matrix is elementary in return coordinates

Let `W_N` be the nonnegative weighted-adjacency matrix of the path, so

\[
H_N=A_N-W_N=A_N(I-K_N),
\qquad
K_N=A_N^{-1}W_N\ge0.
\tag{15}
\]

The `j`th row sum of `K_N` is

\[
\sum_k(K_N)_{jk}
=
\frac{\sum_{k\sim j}c_{jk}}{d_j+\sum_{k\sim j}c_{jk}}
=1-\frac{d_j}{a_j}<1.
\tag{16}
\]

Thus `\|K_N\|_\infty<1` for this finite PF chain, so `\rho(K_N)<1` and the Neumann series is justified:

\[
H_N^{-1}
=(I-K_N)^{-1}A_N^{-1}
=\sum_{m\ge0}K_N^mA_N^{-1}\ge0.
\tag{17}
\]

This proves entrywise nonnegativity of `G_N` without importing a separate matrix theorem. In classical language `H_N` is a symmetric nonsingular `M`-matrix (a Stieltjes matrix), and (17) is its inverse-positivity mechanism.

Applying `G_N` to (14) gives `G_Nd=\mathbf1`. Symmetry of `G_N` gives (6). Positivity then immediately yields (8).

## 3. The substochastic Green potential is exactly normalized

Equation (16) identifies the row deficit as

\[
\delta_{N,j}=\frac{d_j}{a_j},
\tag{18}
\]

hence (10). Since `\rho(K_N)<1`, multiply (10) by `(I-K_N)^{-1}` to obtain

\[
\sum_{m\ge0}K_N^m\delta_N
=(I-K_N)^{-1}(I-K_N)\mathbf1
=\mathbf1.
\tag{19}
\]

This is stronger and more precise than asking for a depth-independent one-step contraction. The worst row sum of `K_N` may approach one as the chain moves into the narrow-pant tail, exactly as PF-298 warns, while the **source matched to the local deficit** still has unit total occupation potential.

For any `0\le\xi_N\le C\delta_N`, positivity gives termwise

\[
0\le K_N^m\xi_N\le C K_N^m\delta_N.
\]

Summation and (19) prove (12). This is the finite scalar realization of the clue's abstract excessive-majorant criterion, with `h=\mathbf1` and `h-K_Nh=\delta_N` exactly.

## 4. Relation to PF-302: extinction and bounded source potential are different questions

PF-302 proves that the two directional relative-killing masses cannot both be summable and that scalar round trips are extinguished at infinite depth. The present identity addresses a different issue. It does not estimate a bare survival product; it asks whether **forcing is paid in the same currency as escape**.

A nearly conservative state can have a long lifetime, but a source of size proportional to its row deficit injects proportionally less mass. Equation (19) says these effects cancel exactly in the finite scalar chain. Thus the absence of a uniform local contraction gap from PF-298 and the accumulated extinction from PF-302 are perfectly compatible with a uniformly normalized source-adapted Green potential.

This also sharpens the accepted clue's scalar calibration. The scalar question is no longer whether some mysterious potential weight exists: `d` (or `\delta=A^{-1}d` after return normalization) is the canonical one. The difficult question is whether the physical mixed forcing has this scale.

## 5. Consequence for the actual mixed-response gate

The accepted clue asks for the real PF-290 energy-normalized mixed response in PF-296 source coordinates. Nothing above proves that its return operator is `K_N`, that its forcing is nonnegative, or that its absolute-value majorant is bounded by `C\delta_N`.

The next discriminating calculation is therefore precise. After deriving the true finite-section `P/H`-split return/reassembly equation, compare its source term `\xi_{n,r,L}` with the scalar deficit generated by the neighboring pant chain. A sufficient positive route would establish, in the correct weighted coefficient currency,

\[
0\le\xi_{n,r,L}\le C\delta_L
\tag{20}
\]

or construct another uniformly summable excessive majorant that survives the nonconstant-mode factors. If (20) fails, identify the concrete component that exceeds the scalar killing budget and determine whether signed cancellation still controls the physical response.

This is stronger guidance than another generic matrix counterexample: it gives a canonical comparison quantity fixed by the actual local PF-298 response. It also makes a failure informative. If physical mixed forcing systematically dominates `d`, then the obstruction is not simply "returns are nearly conservative"; it is a mismatch between how the mixed source is injected and how shifted Robin mass leaks out.

## 6. Prior art and novelty audit

The abstract algebra is classical. Finite killed random walks, substochastic kernels, Green/fundamental matrices, nonsingular `M`-matrices, and excessive/superharmonic potentials all encode the same mechanism. In particular the inverse-positivity of nonsingular `M`-matrices is standard; see A. Berman and R. J. Plemmons, *Nonnegative Matrices in the Mathematical Sciences*, SIAM Classics in Applied Mathematics 9 (1994), especially the inverse-positivity/M-matrix chapters. A targeted structure-level search found the standard matrix/Markov mechanism, not a novel theorem represented by (11).

No novelty is claimed for `Gd=1`, the substochastic Neumann series, `M`-matrix inverse positivity, or the deficit-potential identity in abstract form. The Mathia-specific contribution is the **identification of the PF-298 assembled Robin killing as the exact source currency for that classical mechanism**, together with its placement after PF-302 inside the still-open PF-290/PF-296 mixed-response gate.

Because the proof above derives positivity and the potential identity directly from (1), no external theorem is load-bearing for the exact project statement.

## 7. Boundary conditions and falsification tests

The result is finite-section and scalar. It uses the exact constant-boundary compression (1); it does not assert that constants form an invariant subspace of the full boundary DtN/Schur problem. Nonconstant modes, the physical `P/H` projections, fixed-axis Robin operators, seam transports, or signed couplings can change both the return kernel and the forcing currency.

The entrywise majorant is also stronger than the signed physical problem. Failure of `|\xi|\lesssim\delta` would not by itself imply divergence of the actual mixed response, because cancellation may survive. Conversely, a scalar bound proves no basis-invariant compactness statement until it is inserted into the PF-296 synthesis and returned to the PF-290 shorting deficit.

The finite identity has no arithmetic discrimination: replacing the prime sequence by a matched surrogate while retaining positive local conductances/killing preserves the proof. Any RH-relevant content must enter through how the true mixed forcing, nonconstant reassembly, or a later observable depends on ordered prime geometry.

A direct falsification audit is simple: assemble several consecutive PF-298 matrices numerically or symbolically, verify `H_N\mathbf1=d`, and check that solving `H_Nv=d` returns `v=\mathbf1` to numerical precision. More importantly, audit the first genuine `P/H`-split finite return equation against (20). If its physical forcing is not controlled by the scalar deficit and no alternate excessive majorant exists, this scalar certificate remains only a calibration result rather than a solution of the accepted clue.