# WI-371 — Desogus's corrected gamma floor has linearly growing negative index

**Status:** `EXACT-DERIVED + PRIMARY-SOURCE-CRITICAL-AUDIT + POSITIVE-BULK-NEGATIVE-INDEX-DENSITY + DECISIVE-REPAIR-BARRIER + NON-ESTABLISHED-RH`.

## Claim

WI-369 reconstructed the exact gamma-corrected odd archimedean block from Marco Desogus's *The Three Gates: A Rooted-Operator Approach to Weil Positivity* (`arXiv:2609.20367v1`) as

\[
\mathcal A_A+C_\Gamma I=R_A\succeq0,
\qquad
C_\Gamma=\frac\pi2+\gamma+\log(8\pi),
\tag{1}
\]

where `R_A` is the sum of a screened difference form, a positive endpoint multiplier and a positive Hankel image. The near-floor sector is not merely of unbounded dimension: its negative form index has a strictly positive asymptotic density on the natural `A` scale.

For a Hermitian quadratic form `q` on the common core and `eta>0`, define its depth-`eta` negative index by

\[
\iota_\eta(q):=
\sup\left\{\dim V:
V\subset C_c^1(0,1),\ 
q[f]\le-\eta\|f\|_2^2\text{ for every }f\in V
\right\}.
\tag{2}
\]

At depth zero, retain the strict negative form index

\[
\iota_0(q):=
\sup\left\{\dim V:
V\subset C_c^1(0,1),\ 
q[f]<0\text{ for every }0\ne f\in V
\right\}.
\]

Write `iota_eta(A)=iota_eta(mathcal A_A)`. Let

\[
M_2:=\int_0^\infty s^2h(s)\,ds
=7\zeta(3)+\frac{\pi^3}{4},
\qquad
h(s)=\frac{e^{-s/2}}{1-e^{-2s}},
\tag{3}
\]

as in WI-369. Then, for every fixed `0<eta<C_Gamma`,

\[
\boxed{
\liminf_{A\to\infty}\frac{\iota_\eta(A)}A
\ge
c_\eta
:=
\frac1\pi\sqrt{\frac{C_\Gamma-\eta}{M_2}}.
}
\tag{4}
\]

Consequently,

\[
\boxed{
\liminf_{A\to\infty}\frac{\iota_0(A)}A
\ge
c_{\rm bulk}
:=
\frac1\pi\sqrt{\frac{C_\Gamma}{M_2}}
=0.1834951935083428577\ldots .
}
\tag{5}
\]

Equivalently, for every `c<c_bulk`, one has `iota_0(A)>=floor(cA)` for all sufficiently large `A`.

The earlier explicit disjoint-bump proof in this finding gave only

\[
c_*=
\sqrt{\frac{C_\Gamma}{4C_1}},
\qquad
C_1=\frac{16\pi^2}{3}M_2,
\qquad
c_*=0.0397278747626\ldots .
\tag{6}
\]

The Dirichlet-band argument below improves that coefficient by the exact factor

\[
\boxed{\frac{c_{\rm bulk}}{c_*}=\frac8{\sqrt3}=4.6188021535\ldots .}
\tag{7}
\]

This strengthens the repair obstruction correspondingly. If `K_A` is any bounded self-adjoint additive correction and

\[
\mathcal A_A+K_A\succeq0
\tag{8}
\]

for all sufficiently large `A`, then necessarily

\[
\boxed{
\liminf_{A\to\infty}\frac{\operatorname{rank}K_A}{A}
\ge c_{\rm bulk}.
}
\tag{9}
\]

If moreover `K_A` belongs to the Schatten class `S_p`, `1<=p<infinity`, then

\[
\boxed{
\liminf_{A\to\infty}A^{-1/p}\|K_A\|_{\mathfrak S_p}
\ge
\sigma_p,
}
\tag{10}
\]

where the explicit optimized constant is

\[
\sigma_p
:=
\frac{2p}{2p+1}C_\Gamma
\left[
\frac1\pi
\sqrt{\frac{C_\Gamma}{(2p+1)M_2}}
\right]^{1/p}>0.
\tag{11}
\]

Conversely, any family of bounded self-adjoint corrections with uniformly bounded finite Schatten norm leaves the same asymptotic negative-index density `c_bulk`; so does any single fixed compact self-adjoint correction. More precisely, if `sup_A ||K_A||_{S_p}<infinity`, then

\[
\boxed{
\liminf_{A\to\infty}
\frac{\iota_0(\mathcal A_A+K_A)}A
\ge c_{\rm bulk},
}
\tag{12}
\]

and the same conclusion holds for one fixed compact `K` in place of `K_A`.

Thus WI-370's scalar-budget obstruction is only the first manifestation of the corrected gamma problem. An additive repair cannot act on finitely many exceptional modes, on an `o(A)`-rank sector, through a fixed compact perturbation, or with uniformly bounded finite Schatten mass. It must supply coercivity on a genuinely bulk family of interior modes, or use a non-additive coupling that changes the relevant geometry.

This remains a repair barrier, not a disproof of the full Desogus program and not a result about RH. The paper's active arithmetic/source geometry grows with the localization scale and may have enough effective dimension to evade every bounded-complexity hypothesis used here.

## 1. Exact screened-difference control

The exact decomposition from WI-369 writes `R_A` as a sum of three nonnegative channels. For the screened difference term,

\[
D_A[f]
:=\frac A2\iint h(A|u-v|)|f(u)-f(v)|^2\,du\,dv.
\tag{13}
\]

For `0<t<1`, the fundamental theorem of calculus and Cauchy--Schwarz give

\[
|f(u+t)-f(u)|^2
\le
 t\int_u^{u+t}|f'(x)|^2\,dx.
\tag{14}
\]

After integration in `u`, every point `x` is counted for a set of `u` of length at most `t`, so

\[
\int_0^{1-t}|f(u+t)-f(u)|^2\,du
\le t^2\|f'\|_2^2.
\tag{15}
\]

Using symmetry and changing variables `s=At`,

\[
\begin{aligned}
D_A[f]
&=A\int_0^1 h(At)
  \int_0^{1-t}|f(u+t)-f(u)|^2\,du\,dt\\
&\le A\|f'\|_2^2\int_0^1t^2h(At)\,dt\\
&\le
\boxed{\frac{M_2}{A^2}\|f'\|_2^2.}
\end{aligned}
\tag{16}
\]

This deterministic inequality is the only place where the actual nonlocal screened kernel is compressed to a local second-derivative cost.

## 2. Interior Dirichlet bands beat disjoint bumps

Fix `0<delta<1/2` and put

\[
I_\delta=(\delta,1-\delta),
\qquad
L_\delta=1-2\delta.
\tag{17}
\]

For functions supported in `I_delta`, the other two positive pieces of `R_A` are uniformly negligible. WI-369's exact endpoint formula and monotonicity of `H` give

\[
E_A[f]
\le2H(A\delta)\|f\|_2^2.
\tag{18}
\]

For the Hankel image, `u+v>=2delta` on the support, so monotonicity of `h` and Cauchy--Schwarz give

\[
0\le J_A[f]
\le A h(2A\delta)\|f\|_1^2
\le A L_\delta h(2A\delta)\|f\|_2^2.
\tag{19}
\]

Hence, with

\[
\varepsilon_A(\delta)
:=2H(A\delta)+A L_\delta h(2A\delta),
\qquad
\varepsilon_A(\delta)\longrightarrow0,
\tag{20}
\]

one has on the interior core

\[
\boxed{
R_A[f]
\le
\left[
\frac{M_2}{A^2}
\frac{\|f'\|_2^2}{\|f\|_2^2}
+\varepsilon_A(\delta)
\right]\|f\|_2^2.
}
\tag{21}
\]

Now use the full low-frequency Dirichlet band on `I_delta` instead of splitting the interval into disjoint cells. The first `m` Dirichlet eigenfunctions have maximal Rayleigh quotient

\[
\Lambda_m(I_\delta)
=\left(\frac{m\pi}{L_\delta}\right)^2.
\tag{22}
\]

Their zero extensions lie in `H_0^1(0,1)` rather than literally in the chosen `C_c^1` core. This causes no loss: `C_c^\infty(I_delta)` is dense in `H_0^1(I_delta)`, and finite-dimensional approximation gives the following core version. For every fixed `m` and every `rho>0`, there is an `m`-dimensional subspace

\[
V_{m,\rho}\subset C_c^\infty(I_\delta)
\tag{23}
\]

such that

\[
\sup_{0\ne f\in V_{m,\rho}}
\frac{\|f'\|_2^2}{\|f\|_2^2}
\le
\left(\frac{m\pi}{L_\delta}\right)^2+\rho.
\tag{24}
\]

Indeed, approximate a basis of the finite Dirichlet eigenspace simultaneously in `H^1`; for sufficiently small approximation the linear map from the eigenspace is injective and both Gram matrices remain arbitrarily close. This is purely finite-dimensional and introduces no closure assumption on `mathcal A_A`.

## 3. Positive bulk density of the negative sector

Fix `0<eta<C_Gamma`. Choose any

\[
c<\frac{L_\delta}{\pi}
\sqrt{\frac{C_\Gamma-\eta}{M_2}}.
\tag{25}
\]

Let `m_A=floor(cA)`. Because the inequality in (25) is strict, there is a fixed positive margin `mu` such that

\[
M_2\left(\frac{c\pi}{L_\delta}\right)^2
\le C_\Gamma-\eta-2\mu.
\tag{26}
\]

For each `A`, choose the core approximation in (24) fine enough that its contribution to (21) is at most `mu/2`, and then take `A` large enough that `epsilon_A(delta)<=mu/2`. Equations (21)--(26) yield, uniformly on the resulting `m_A`-dimensional core subspace,

\[
R_A[f]
\le(C_\Gamma-\eta-\mu)\|f\|_2^2.
\tag{27}
\]

Using (1),

\[
\boxed{
\mathcal A_A[f]
\le-(\eta+\mu)\|f\|_2^2
\le-\eta\|f\|_2^2.
}
\tag{28}
\]

Therefore

\[
\liminf_{A\to\infty}
\frac{\iota_\eta(A)}A
\ge
\frac{L_\delta}{\pi}
\sqrt{\frac{C_\Gamma-\eta}{M_2}}.
\tag{29}
\]

Since `delta>0` was arbitrary, let `delta` decrease to zero and obtain (4). Since `iota_0(A)>=iota_eta(A)` for every positive `eta`, letting `eta` decrease to zero proves (5).

This also identifies exactly where the old coefficient was lost. The disjoint `sin^2` bumps had derivative cost `(16pi^2/3)m^2` on an interval of length `1/2`; the full Dirichlet band uses the min--max optimal cost `(m pi/L)^2` and then lets `L` approach one. The quotient of the resulting density constants is exactly `8/sqrt(3)`.

Within the sole majorization (16), the Dirichlet min--max step is asymptotically optimal: no different `m`-dimensional subspace supported in an interval of length `L` can lower the maximal derivative Rayleigh quotient below `(m pi/L)^2`. This does **not** make `c_bulk` the true negative-index density of the nonlocal operator. Any further gain must retain more of the screened kernel than its second-moment bound (16), or exploit the source-conditioned arithmetic coupling.

## 4. Rank, Schatten and compact-repair consequences

Let `V_A` be a depth-`eta` negative subspace supplied by (4), with dimension `d_A` satisfying

\[
\liminf_{A\to\infty}\frac{d_A}{A}\ge c_\eta.
\tag{30}
\]

Suppose first that a bounded self-adjoint correction `K_A` makes the total form nonnegative. For every `f in V_A`,

\[
\langle f,K_Af\rangle
\ge\eta\|f\|_2^2.
\tag{31}
\]

Thus the compression to `V_A` satisfies

\[
P_{V_A}K_AP_{V_A}\succeq\eta I_{V_A}.
\tag{32}
\]

It follows immediately that `rank(K_A)>=d_A`. Passing to the limit and then letting `eta` decrease to zero proves (9).

If `K_A` lies in `S_p`, compression does not increase its Schatten norm, so (32) gives

\[
\|K_A\|_{\mathfrak S_p}
\ge\eta d_A^{1/p}.
\tag{33}
\]

For fixed `eta`, divide by `A^(1/p)` and use (30). Maximizing

\[
\eta
\left[
\frac1\pi\sqrt{\frac{C_\Gamma-\eta}{M_2}}
\right]^{1/p}
\tag{34}
\]

over `0<eta<C_Gamma` gives

\[
\eta_*=\frac{2p}{2p+1}C_\Gamma,
\tag{35}
\]

and exactly the constant `sigma_p` in (11). This proves (10).

Now assume only that `sup_A ||K_A||_{S_p}<=M`; no positivity of `K_A` is required. Compress `K_A` to a depth-`eta` subspace `V_A`. At most

\[
\left(\frac{2M}{\eta}\right)^p
\tag{36}
\]

eigenvalues of this self-adjoint compression can exceed `eta/2`, because its singular values are dominated in `l^p` by those of `K_A`. On the orthogonal complement of those directions inside `V_A`,

\[
(\mathcal A_A+K_A)[f]
\le-\frac\eta2\|f\|_2^2.
\tag{37}
\]

The loss in dimension in (36) is independent of `A`. Hence

\[
\liminf_{A\to\infty}
\frac{\iota_0(\mathcal A_A+K_A)}A
\ge c_\eta.
\tag{38}
\]

Letting `eta` decrease to zero proves (12).

For a single fixed compact self-adjoint `K`, the spectral subspace corresponding to eigenvalues larger than `eta/2` is finite-dimensional for every fixed positive `eta`. The same argument therefore gives (38) with an `O_eta(1)` loss and again yields the density `c_bulk` after `eta` decreases to zero. Likewise any finite-rank family with `rank(K_A)=o(A)` leaves at least the same asymptotic negative-index density.

## 5. Provenance and novelty audit

**Primary source under audit.** Marco Desogus, *The Three Gates: A Rooted-Operator Approach to Weil Positivity*, `arXiv:2609.20367v1`, submitted 17 September 2026, with supplementary material DOI `10.5281/zenodo.22799713`. The source claims a proof of RH. Mathia does not import that conclusion: WI-361 and its descendants treat the paper as a candidate architecture under independent audit.

**Internal exact dependencies.** WI-369 supplies (1), the exact functions `h,H`, positivity of the three remainder channels and the moment identity (3). WI-370 supplies the separate scalar-budget obstruction. The original version of WI-371 established linear negative-index growth using disjoint compactly supported bumps. The present strengthening keeps the exact screened-difference estimate (16) but replaces those bumps by an asymptotically optimal low Dirichlet band, producing the exact density lower bound (5).

**Classical background.** Equation (22) is the elementary one-dimensional Dirichlet spectrum/min--max principle; (23)--(24) use density of the smooth compactly supported core in `H_0^1`. Equations (31)--(38) are finite-dimensional compression, eigenvalue counting and standard compact/Schatten facts. These ingredients are classical and are not claimed as new.

**Fresh source audit.** A targeted search of Desogus v1 for `negative index`, `Schatten`, and `bulk` found no corresponding statement. The local Mathia trail contains earlier generic compact/finite-rank obstruction observations (notably MI-029, MI-032 and WI-303), but none gives the gamma-corrected depth profile (4), the density constant (5), or the repair constants (9)--(12). This is recorded as a novelty audit result, not as a claim of historical priority.

No new external source is needed for this strengthening: it is an exact deduction from the already anchored Desogus form plus classical one-dimensional min--max geometry.

## 6. Boundary and research consequence

The conclusion is deliberately about the **gamma-corrected odd archimedean block plus bounded self-adjoint additive corrections**. It does not show that Desogus's complete source network has sublinear effective rank or bounded Schatten mass; its active arithmetic/source space grows with localization scale. Nor does it rule out a genuinely non-additive Schur mechanism whose coupling changes the bulk subspace rather than merely perturbing the archimedean block.

What it does impose is a substantially stronger necessary condition than the original disjoint-bump estimate. The corrected block contains at least

\[
(c_{\rm bulk}-o(1))A
\]

independent negative directions, and at every fixed depth `eta<C_Gamma` it contains at least `(c_eta-o(1))A` directions below `-eta`. A successful additive source/polar repair must therefore act coherently on a positive-density bulk sector; if it is Schatten, its norm must grow at least at the explicit `A^(1/p)` rate (10).

The next unresolved test is correspondingly sharper. The second-moment bound (16) deliberately discards the exact nonlocal Fourier/spectral profile of the screened difference kernel. Improving the negative-index density further requires analyzing that nonlocal bulk symbol or, on the opposite side, proving that the source-conditioned Schur correction has enough rank and singular-value mass **in the same interior modes**. Either route tests the actual load-bearing mechanism rather than another scalar reserve.