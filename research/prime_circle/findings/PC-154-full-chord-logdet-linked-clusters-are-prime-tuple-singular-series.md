# PC-154 — fixed-support full-chord log-determinant clusters are prime-tuple singular-series functionals

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY`. PC-150 and PC-151 classify the first Mertens-scale displacement of fixed-radius and full-radius spectral functions, while PC-153 classifies every **fixed polynomial moment** of the full primitive-shell inverse-square operator by the number of primitive vertices visited by its edge words. The remaining natural scalar question is whether a genuinely non-polynomial spectral determinant can resum infinitely many moment orders at one fixed geometric support size and thereby generate arithmetic beyond the Hardy--Littlewood tuple hierarchy.

It does not. There is an exact vertex-subset Möbius decomposition of the shifted full spectral determinant into connected support clusters. For every fixed support size `v>=2`, the complete all-chord `v`-vertex cluster has natural Mertens scale `1/(log x)^(v-1)` and converges, locally uniformly for nonnegative determinant coupling, to an **absolutely convergent Hardy--Littlewood `v`-tuple singular-series functional**. The geometry survives only in an explicit finite-vertex log-determinant cumulant built from the limiting inverse-square chord kernel.

Thus passing from moments to `log det` really does perform an infinite resummation in moment order, but at every fixed connected support size its arithmetic coefficients remain exactly the same classical reduced-residue tuple densities already exposed by PC-149/PC-153. This closes the fixed-support non-polynomial scalar-determinant escape. It does **not** control support size growing with the conductor, the simultaneous resummation over all cluster sizes, eigenvectors/projectors, or cross-level coherent transport.

## 1. The full spectral determinant has an exact support-cluster decomposition

As in PC-151--PC-153, put

\[
N_x:=\prod_{p\le x}p,
\qquad
\phi_x:=\varphi(N_x),
\qquad
U_x:=(\mathbb Z/N_x\mathbb Z)^\times,
\]

and let

\[
A_x:=N_x^{-2}L_{N_x}^{\rm int}.
\]

For distinct primitive residues `a,b`, write

\[
g_{N_x,a-b}:=
\frac{1}{4N_x^2\sin^2(\pi(a-b)/N_x)},
\qquad
q_{ab}:=e_a-e_b.
\]

Then

\[
A_x=
\sum_{\{a,b\}\subset U_x}
 g_{N_x,a-b}\,q_{ab}q_{ab}^*.
\tag{1}
\]

For every finite subset `S subset U_x`, let `A_x[S]_{int}` denote the weighted Laplacian using **only** chords whose two endpoints lie in `S`. For `t>=0`, define

\[
F_{x,t}(S):=
\log\det\!\left(I+tA_x[S]_{\rm int}\right),
\qquad
F_{x,t}(S)=0\quad(|S|\le1).
\tag{2}
\]

The matrix is positive definite, so no logarithm branch is involved. Define the Boolean-lattice Möbius cumulant

\[
\boxed{
\kappa_{x,t}(S)
:=
\sum_{T\subseteq S}
(-1)^{|S|-|T|}F_{x,t}(T).
}
\tag{3}
\]

Ordinary Möbius inversion is exact at every finite conductor:

\[
\boxed{
\log\det(I+tA_x)
=
\sum_{\substack{S\subseteq U_x\\|S|\ge2}}
\kappa_{x,t}(S)
=
\sum_{v=2}^{\phi_x} C_{x,v}(t),
}
\tag{4}
\]

where

\[
C_{x,v}(t):=
\sum_{\substack{S\subseteq U_x\\|S|=v}}
\kappa_{x,t}(S).
\tag{5}
\]

This decomposition is canonical for the induced chord geometry. The cumulant removes every contribution already present on a proper vertex subset. In the usual linked-cluster language it is therefore the connected `v`-vertex part of the spectral determinant.

This is already stronger than a fixed-moment expansion. At a fixed `v`, `kappa_{x,t}(S)` contains the complete `t`-dependence of the finite induced spectral determinant and hence resums edge words of **all** lengths that remain supported on `S`.

## 2. Every fixed support cluster is weighted by one exact reduced-residue tuple count

Fix `v>=2`. Represent a `v`-set by choosing a root `a`, ordering the other `v-1` vertices, and writing their signed residues relative to `a` as

\[
H=\{0,h_1,\ldots,h_{v-1}\}.
\]

Take each `h_j` in the canonical interval `(-N_x/2,N_x/2]`, and require the resulting residues to be pairwise distinct. Every unordered `v`-subset has exactly

\[
v(v-1)!=v!
\]

such rooted ordered representations. Translation invariance of the chord kernel makes `kappa_{x,t}` depend only on the offset configuration. Therefore

\[
\boxed{
C_{x,v}(t)
=
\frac1{v!}
\sum_{\mathbf h\in\mathcal D_{v,x}}
J_H(N_x)\,\kappa_{x,t}(H),
}
\tag{6}
\]

where

\[
J_H(N_x)
:=
\#\{a\bmod N_x:
 a+h\in U_x\text{ for every }h\in H\}.
\tag{7}
\]

This is exactly the simultaneous-coprimality count of PC-149/PC-153. If

\[
\nu_p(H):=\#\{h\bmod p:h\in H\},
\]

CRT gives

\[
\boxed{
\frac{J_H(N_x)}{\phi_x}
=
\prod_{p\le x}
\frac{p-\nu_p(H)}{p-1}.
}
\tag{8}
\]

For an admissible fixed integer offset set define the ordinary Hardy--Littlewood tuple singular series

\[
\mathfrak S_v(H)
:=
\prod_p
\frac{1-\nu_p(H)/p}{(1-1/p)^v},
\tag{9}
\]

and set it to zero when a local obstruction occurs. Mertens' product theorem then gives

\[
\boxed{
(\log x)^{v-1}
\frac{J_H(N_x)}{\phi_x}
\longrightarrow
 e^{-(v-1)\gamma}\mathfrak S_v(H).
}
\tag{10}
\]

No prime-tuple conjecture enters: (8) is an exact count inside the reduced residue system of the primorial. The Hardy--Littlewood singular series appears only as the normalized limit of that exact finite CRT product.

## 3. Connectedness supplies exactly the inverse-square decay needed at full chord radius

The nontrivial step is to pass (6) to all integer offsets without fixing a chord cutoff. A raw bound on `F_{x,t}(S)` would fail because it does not force every vertex to participate. The Möbius cumulant does force that participation, and standard connected forest interpolation makes it quantitative.

Introduce independent nonnegative edge parameters in the induced Laplacian. For

\[
R=(I+tL)^{-1}
\]

with `L>=0`, one has `||R||<=1`. Mixed derivatives of `log det(I+tL)` in `k` distinct edge parameters are cyclic products of resolvent matrix elements. Since an edge incidence vector has squared norm `2`,

\[
\left|
\partial_{e_1}\cdots\partial_{e_k}
\log\det(I+tL)
\right|
\le
(k-1)!(2t)^k
\prod_{j=1}^k g_{e_j}.
\tag{11}
\]

Applying the standard connected Brydges--Kennedy--Abdesselam--Rivasseau forest interpolation to the induced-set Möbius difference (3) gives, for every fixed `v` and every compact `0<=t<=T`,

\[
\boxed{
|\kappa_{x,t}(S)|
\le
C_{v,T}
\sum_{\tau\in\operatorname{Tree}(S)}
\prod_{e\in\tau}g_e.
}
\tag{12}
\]

The important feature is not the constant: every connected `v`-vertex cumulant carries at least one spanning tree, hence `v-1` inverse-square chord factors.

For a canonical nonzero cyclic displacement `d`, PC-151/PC-153 use

\[
0<g_{N,d}\le\frac1{16d^2}.
\tag{13}
\]

PC-153 also proves the uniform partial-singular-series bound

\[
\prod_{p\le x}
\frac{1-\nu_p(H)/p}{(1-1/p)^v}
\ll_v
\bigl(\log\log(3\Delta(H))\bigr)^{C_v},
\qquad
\Delta(H)=\prod_{i<j}|h_i-h_j|.
\tag{14}
\]

Fix one spanning tree in (12) and parametrize a rooted placement by the `v-1` signed canonical increments on its tree edges. All pair differences are tree-path sums. Combining (8), boundedness of

\[
(\log x)\prod_{p\le x}(1-1/p),
\]

(12)--(14), and the same harmless `polyloglog <= |d|^epsilon` majorization used in PC-153 yields, for any fixed `0<epsilon<1`, a uniform summable envelope

\[
C_{v,T,\epsilon}
\prod_{e\in\tau}|d_e|^{-2+\epsilon}.
\tag{15}
\]

There are finitely many labelled spanning trees for fixed `v`. Thus the complete all-chord rooted cluster sum is absolutely dominated, uniformly for `t` in compact subsets of `[0,infinity)`.

For fixed integer offsets, meanwhile,

\[
g_{N_x,h_i-h_j}
\longrightarrow
w(h_i-h_j)
:=\frac1{4\pi^2(h_i-h_j)^2}.
\tag{16}
\]

Let `L(H)` be the complete weighted Laplacian on the finite integer offset set `H`, with pair weights `w(h_i-h_j)`, and define its limiting induced-subset cumulant

\[
\kappa_t(H)
:=
\sum_{T\subseteq H}
(-1)^{v-|T|}
\log\det(I+tL(T)).
\tag{17}
\]

Dominated convergence in (6) now gives the fixed-support full-radius theorem:

\[
\boxed{
\lim_{x\to\infty}
\frac{(\log x)^{v-1}}{\phi_x}
C_{x,v}(t)
=
\frac{e^{-(v-1)\gamma}}{v!}
\sum_{\substack{h_1,\ldots,h_{v-1}\in\mathbb Z\\
0,h_1,\ldots,h_{v-1}\;\mathrm{distinct}}}
\mathfrak S_v(0,h_1,\ldots,h_{v-1})
\,\kappa_t(0,h_1,\ldots,h_{v-1}).
}
\tag{18}
\]

The series is absolutely convergent and the convergence is locally uniform for `t>=0`. Local inadmissibility is understood to set the singular series to zero.

Equation (18) is the non-polynomial analogue of the fixed-support moment theorem in PC-153: it resums all moment orders first and only then takes the primorial/full-radius limit, yet the arithmetic coefficient class does not change.

## 4. The two- and three-vertex clusters recover PC-151 and PC-152

For `v=2`, write

\[
a_h:=\frac1{4\pi^2h^2}.
\]

The two-vertex weighted Laplacian has eigenvalues `0,2a_h`, so

\[
\kappa_t(0,h)=\log(1+2ta_h).
\tag{19}
\]

The factor `1/2!` in (18) combines the two signed orientations. Hence

\[
\boxed{
\lim_{x\to\infty}
\frac{\log x}{\phi_x}C_{x,2}(t)
=
 e^{-\gamma}
\sum_{\substack{h\ge1\\2\mid h}}
\mathfrak S_2(h)
\log\left(1+\frac{t}{2\pi^2h^2}\right).
}
\tag{20}
\]

This is exactly the shifted-log-determinant specialization of PC-151's full spectral-displacement law.

For `v=3`, take offsets `{0,h,k}` and put

\[
a=w(h),\qquad b=w(k),\qquad c=w(h-k),
\]

\[
S=a+b+c,
\qquad
P=ab+ac+bc.
\]

The weighted triangle Laplacian has

\[
\det(I+tL)=1+2tS+3t^2P.
\]

Subtracting its three two-vertex subclusters gives the exact connected determinant cumulant

\[
\boxed{
\kappa_t(0,h,k)
=
\log
\frac{1+2tS+3t^2P}
{(1+2ta)(1+2tb)(1+2tc)}.
}
\tag{21}
\]

For `t>0` this is nonpositive because the denominator exceeds the numerator by

\[
t^2P+8t^3abc>0.
\]

At small `t`,

\[
\boxed{
\kappa_t(0,h,k)=-t^2P+O(t^3).
}
\tag{22}
\]

By symmetry, the three terms in `P` give equal sums in (18). Therefore the coefficient of `t^2` in the `v=3` limit is exactly

\[
-\frac{t^2}{2}
\frac{e^{-2\gamma}}{16\pi^4}
\sum_{\substack{h,k\in\mathbb Z\setminus\{0\}\\h\ne k}}
\frac{\mathfrak S_3(h,k)}{h^2k^2},
\tag{23}
\]

which is `-t^2/2` times PC-152's complete three-vertex contribution to `Tr(A_x^2)`, as required by

\[
\log\det(I+tA_x)
=t\operatorname{Tr}A_x-rac{t^2}{2}\operatorname{Tr}(A_x^2)+\cdots.
\]

Thus both lower-support controls close exactly against already established Prime-Circle results.

## 5. Prior-art and novelty audit

The ingredients are classical in their respective domains. Pabhapote--Laohakosol's generalized Euler/Lucas totients already cover the simultaneous-coprimality counts in (7)--(10), as used in PC-149. Hardy--Littlewood tuple singular series are the standard normalized local densities. Abdesselam--Rivasseau, **Trees, forests and jungles: a botanical garden for cluster expansions**, *Lecture Notes in Physics* 446 (1995), 7--36, DOI `10.1007/3-540-59190-7_20`, arXiv:`hep-th/9409094`, is a classical source for the forest interpolation/linked-cluster tree technology used in (12). The exact pair-level Mellin/Dirichlet continuation that can expose Riemann zeros is already the Goldston--Suriajaya singular-series generating function identified in PC-151.

Directed searches across reduced-residue graph determinants, primorial Laplacians, spectral determinants weighted by Hardy--Littlewood singular series, and prime-tuple graph cluster expansions did not locate equation (18) as a published specialization. No historical theorem-level novelty is claimed for it. Its durable value is an internal **classification theorem**: the fixed-moment result PC-153 extends to a genuine non-polynomial spectral determinant at every fixed connected vertex support.

The RH audit remains negative at this boundary. For fixed `v` and `t>=0`, (18) contains no intrinsic complex spectral variable, analytic-continuation law, gamma factor, `s <-> 1-s` symmetry, or self-adjoint condition selecting zeta zeros. The `v=2` coefficient can be Mellin-transformed into the classical zero-sensitive singular-series Dirichlet function of Goldston--Suriajaya, but that zero dependence is inherited after an external transform, not generated by the determinant cluster. Higher-tuple transforms would require their own analytic-number-theory audit.

## 6. Boundary and falsification surface

1. At every finite conductor, direct subset enumeration must satisfy the exact Möbius identity (4). For `N=30` and `t=1`, direct diagonalization gives `log det(I+A)=0.0691704882085`; the successive support sums are approximately `C_2=0.0693551275071`, `C_3=-0.000185101822`, `C_4=4.63449e-7`, `C_5=-9.27e-10`, whose sum already agrees to displayed precision.
2. The `v=2` limit must equal PC-151's log-determinant law exactly; any normalization mismatch in (20) falsifies the rooted `1/v!` factor.
3. The `t^2` coefficient of the `v=3` limit must equal `-1/2` times PC-152's triple wedge limit, as in (23). This independently audits both the connected-subset sign and the three rooted edge-pair multiplicities.
4. The full-radius theorem depends on fixed support size. The tree bound (12) has constants depending on `v`, and no uniform estimate in `v` is asserted. One may not sum (18) over `v` after taking the limit without a new argument.
5. Equation (18) gives the **leading natural Mertens scale of each fixed support stratum**. It is not a complete power-series asymptotic expansion of the total determinant in `1/log x`: subleading corrections from smaller support sizes can live at the same numerical scale as the leading term of a larger support size.
6. A materially new scalar-determinant continuation must therefore be genuinely nonperturbative in support size, for example by controlling `v=v(x)->infinity` or the complete simultaneous cluster sum. Alternatively it must leave scalar determinants for eigenvector/projector, cross-level coherent, or other relational data. Fixed `v` plus a more elaborate resummation in moment order does not cross the Prime-Circle novelty gate.
