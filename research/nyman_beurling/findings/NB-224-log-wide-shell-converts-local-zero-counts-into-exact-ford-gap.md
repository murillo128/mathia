# NB-224 — Log-wide shell converts local zero counts into an exact-Ford gap

**Date:** 2026-09-19  
**Status:** `LITERATURE+DERIVED + ZETA-SPECIFIC + EXPLICIT-FORMULA + LOCAL-ZERO-COUNT + WIDE-LOG-SHELL + POSITIVE-EULER + CONSTANT-GAP + EXACT-FORD-SCALE + NB-223-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-223` reaches every fixed logarithmic margin below the Ford denominator for a fixed-width logarithmic shell, but at the exact scale its proof loses to the final near-one layer because the carrier has vertical width `Theta(1)` while generic local zero mass is `Theta(log |t|)`. Bellotti's 2026 paper contains a stronger local input than the global density theorem used there: Lemma 2.4 bounds the number of zeros in a disk of radius `K/R` around `1+it` by `O(K)` for `K << log log t`, where

\[
R=(\log t)^{2/3}(\log\log t)^{1/3}.
\]

This local count becomes effective at the exact Ford scale if the source shell is deliberately widened in the logarithmic coordinate. Taking width `H=theta X` narrows the carrier in the vertical zero coordinate from order one to order `1/X`. At Ford height `X/R=Theta(1)`, that is narrow enough to sum Bellotti's `O(K)` disk count directly, without paying the global `O(log |t|)` population in the delicate near-edge layers.

Consequently, for every fixed `r>0`, `theta>0`, and nonzero `phi>=0` in `C_c^infinity((0,1))`, there are constants `kappa_0,eta>0` such that the normalized positive Euler return defect associated with the shell

\[
u\in[X,X+\theta X]
\]

satisfies

\[
\boxed{
\mathcal A_{X,\theta X}(t)\ge\eta
\qquad
\left(
1\le |t|
\le
\exp\!\left[
\kappa_0\frac{X^{3/2}}{(\log X)^{1/2}}
\right]
\right)
}
\]

for all sufficiently large `X`. This reaches the exact Ford denominator, but it does so by sacrificing multiplicative resolution: in the original integer variable the source now spans roughly `[e^X,e^{(1+theta)X}]`. It therefore does **not** solve the fixed-width endpoint left open by `NB-223`.

## 1. Widening the log shell preserves order-one source mass and narrows the carrier

Fix `r>0`, `theta>0`, and a nonzero `phi in C_c^infinity((0,1))` with `phi>=0`. Put

\[
H=\theta X,
\qquad
\sigma_X=1+\frac rX,
\qquad
h_{X,H}(u)=\frac1H\phi\!\left(\frac{u-X}{H}\right),
\]

and define

\[
S_{X,H}(t)
:=
\sum_{n\ge2}
\Lambda(n)h_{X,H}(\log n)n^{-\sigma_X-it}.
\tag{1}
\]

The prime number theorem and Stieltjes partial summation give

\[
S_{X,H}(0)
\longrightarrow
m_{\phi,\theta,r}
:=
\int_0^1
\phi(y)e^{-r(1+\theta y)}\,dy
>0.
\tag{2}
\]

Thus the factor `1/H` keeps the total positive source mass at order one despite the logarithmically wide support.

Its Fourier carrier is

\[
L_{X,H}(v)
:=
\int h_{X,H}(u)e^{ivu}\,du
=
e^{iXv}F(Hv),
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{3}
\]

The one-sided support is important. For `Im z>=0`, repeated integration by parts gives, for every fixed `A`,

\[
|F(z)|\ll_{A,\phi}(1+|z|)^{-A},
\tag{4}
\]

because `|e^{izy}|<=1` on the positive `y` support and all boundary terms vanish. Hence for every nontrivial zero `rho=beta+i gamma`, at the pole

\[
v_\rho=(\gamma-t)+i(\sigma_X-\beta)
\]

of `-zeta'/zeta(\sigma_X+i(t+v))`, one has

\[
|L_{X,H}(v_\rho)|
\ll_A
 e^{-X(\sigma_X-\beta)}
\left(
1+H\sqrt{(\gamma-t)^2+(\sigma_X-\beta)^2}
\right)^{-A}.
\tag{5}
\]

In particular,

\[
|L_{X,H}(v_\rho)|
\ll_A
 e^{-r}e^{-X(1-\beta)}
(1+H|\gamma-t|)^{-A}.
\tag{6}
\]

Compared with the fixed-width shell of `NB-223`, the vertical residue kernel has narrowed from width `Theta(1)` to width `Theta(1/H)=Theta(1/X)`.

Exactly as in `NB-223`, Fourier inversion on `Re(s)>1` followed by a global upward shift of the `v` contour yields

\[
\boxed{
|S_{X,H}(t)|
\ll_A
Z_{X,H}(t)
+O_A((H|t|)^{-A})
+O(e^{-cX}(1+\log |t|)),
}
\tag{7}
\]

where

\[
Z_{X,H}(t)
:=
\sum_\rho m(\rho)e^{-X(1-\beta)}
(1+H|\gamma-t|)^{-A}.
\tag{8}
\]

The zeta pole at `1` lies at real carrier coordinate `-t` and is absorbed by the `(H|t|)^{-A}` term. The shift again stops before the first trivial zero. The extra radial decay in (5) is available but is not needed below.

## 2. Bellotti's local disk count matches the narrowed carrier

Write

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\qquad
Y=\frac XR.
\tag{9}
\]

Bellotti's Lemma 2.4 gives the following local form: there is a fixed admissible constant `c_B>0` such that, uniformly for

\[
1\le K\le c_B L,
\]

the disk

\[
\left|1+i\tau-\rho\right|
\le
C\frac K{R}
\]

contains `O_C(K)` nontrivial zeros, counted with multiplicity, whenever `tau` is comparable with the large ordinate under consideration. Constants in the radius only shrink `c_B` and change the implied constant.

For `K` in this range let

\[
C_t(K)
:=
\sum_{\substack{\rho:\ R(1-\beta)\le K}}
(1+H|\gamma-t|)^{-A}.
\tag{10}
\]

Partition the vertical axis near `t` into intervals of length `K/R`. In each interval, every zero counted by (10) lies in one Bellotti disk after enlarging its radius by a fixed factor, so the number of such zeros is `O(K)`. Summing the vertical weights over the intervals gives

\[
\begin{aligned}
C_t(K)
&\ll
K\sum_{j\in\mathbb Z}
\left(1+c\frac{HK}{R}|j|\right)^{-A}\\
&\ll
K\left(1+\frac{R}{HK}\right)
=K+\frac{R}{H}.
\end{aligned}
\tag{11}
\]

Because `H=theta X`,

\[
\frac RH=\frac1{\theta Y}.
\tag{12}
\]

Thus when `Y` is bounded below by a positive constant,

\[
\boxed{C_t(K)\ll_{\theta,\phi} K}
\qquad
(1\le K\le c_B L).
\tag{13}
\]

This is the key gain. A fixed-width carrier can only sum a unit vertical neighborhood and therefore sees `O(Q)` zeros before near-one density is imposed. The log-wide shell reduces that neighborhood to scale `1/X`; Bellotti's local disk estimate then prices the relevant population by the horizontal depth `K` itself.

## 3. A fixed Ford budget now kills every horizontal layer

The Vinogradov--Korobov zero-free region supplies a fixed `a_0>0` such that, for zeros with ordinate comparable with `t`,

\[
R(1-\beta)\ge a_0.
\tag{14}
\]

Choose an integer layering of the shallow range

\[
a_0\le R(1-\beta)\le c_B L.
\]

Using (13), the contribution of the layer `j<=R(1-beta)<j+1` to (8) is at most

\[
\ll (j+1)e^{-Yj}.
\]

Consequently

\[
Z_{\mathrm{shallow}}
\ll
\sum_{j\ge a_0-1}(j+1)e^{-Yj}
\ll e^{-c_0Y}
\tag{15}
\]

for some fixed `c_0>0` once `Y>=1`.

For the remaining zeros with

\[
R(1-\beta)>c_B L,
\]

the horizontal factor alone contributes

\[
e^{-X(1-\beta)}
\le
e^{-c_BYL}
=Q^{-c_BY}.
\tag{16}
\]

Ordinary local zero counting gives `O(Q)` zeros in each unit vertical interval, and the kernel `(1+H|gamma-t|)^(-A)` is summable. Hence

\[
Z_{\mathrm{deep}}
\ll
Q^{1-c_BY}.
\tag{17}
\]

Zeros with ordinate not comparable with `t` are smaller still by the same vertical Schwartz kernel and standard zero counting. Combining (15)--(17),

\[
\boxed{
Z_{X,H}(t)
\ll
e^{-c_0Y}+Q^{1-c_BY}+o(1).
}
\tag{18}
\]

This is the endpoint mechanism missing from `NB-223`. No growing lower bound such as `Y>=L^d` is needed. It is enough that `Y=X/R` exceed a sufficiently large **fixed** constant.

Indeed suppose

\[
Q
\le
\kappa\frac{X^{3/2}}{(\log X)^{1/2}}.
\tag{19}
\]

At the upper edge,

\[
R
=
\left((3/2)^{1/3}+o(1)\right)\kappa^{2/3}X,
\]

so uniformly throughout (19),

\[
Y=\frac XR
\ge
\left((2/3)^{1/3}+o(1)\right)\kappa^{-2/3}.
\tag{20}
\]

Choose a fixed `Y_0` large enough that both `c_BY_0>2` and the first term in (18), with all implied constants restored, is less than `m_{phi,theta,r}/4`. Then choose `kappa_0>0` sufficiently small that the right-hand side of (20) exceeds `Y_0` whenever `kappa<=kappa_0`. Equations (7) and (18) yield

\[
\boxed{
|S_{X,H}(t)|
\le
\frac12m_{\phi,\theta,r}
}
\tag{21}
\]

for all sufficiently large ordinates satisfying (19) with `kappa=kappa_0`.

The restriction to a sufficiently small fixed Ford constant is genuine in this argument. Bellotti's local count gives a finite exponential-in-`Y` saving, not an arbitrarily strong one at every fixed `Y`.

## 4. The wide shell has a constant positive-return gap at exact Ford scale

For bounded nonzero ordinates, the same conclusion follows without zero density. The PNT main term is

\[
e^{-itX}
\int_0^1
\phi(y)e^{-r(1+\theta y)}e^{-itHy}\,dy,
\tag{22}
\]

which tends to zero uniformly on every compact set `1<=|t|<=T_0` by repeated integration by parts because `H=theta X -> infinity`; the PNT remainder is uniform on such a fixed compact set. Thus (21), after enlarging the threshold in `X`, holds throughout

\[
1\le |t|
\le
\exp\!\left[
\kappa_0\frac{X^{3/2}}{(\log X)^{1/2}}
\right].
\tag{23}
\]

Define the normalized positive-return defect

\[
\mathcal A_{X,H}(t)
:=
\frac{1}{S_{X,H}(0)}
\sum_{n\ge2}
\Lambda(n)h_{X,H}(\log n)n^{-\sigma_X}
|e^{-it\log n}-1|.
\tag{24}
\]

Since all weights are nonnegative,

\[
\mathcal A_{X,H}(t)
\ge
\frac{|S_{X,H}(t)-S_{X,H}(0)|}{S_{X,H}(0)}
\ge
1-\frac{|S_{X,H}(t)|}{S_{X,H}(0)}.
\tag{25}
\]

Using (2) and (21), there exists `eta=eta(phi,theta,r)>0` such that for all sufficiently large `X`,

\[
\boxed{
\mathcal A_{X,\theta X}(t)
\ge\eta
\qquad
\left(
1\le |t|
\le
\exp\!\left[
\kappa_0\frac{X^{3/2}}{(\log X)^{1/2}}
\right]
\right).
}
\tag{26}
\]

Thus a constant positive Euler gap reaches the exact Ford denominator once the log shell is allowed width proportional to its carrier position.

## 5. What the theorem does and does not buy

The price is substantial. The source support is no longer a fixed logarithmic shell. It lies in

\[
\log n\in[X,X+\theta X],
\]

so in the integer variable it spans the power range

\[
e^X\lesssim n\lesssim e^{(1+\theta)X}.
\tag{27}
\]

Therefore (26) is **not** an endpoint completion of `NB-223` for the same observable. It proves a resolution-versus-zero-density trade: a `Theta(X)` log width buys a `Theta(1/X)` vertical carrier width, which is precisely what lets Bellotti's local disk count replace the global near-edge population at Ford scale.

This is also consistent with `NB-217`. That finding proves that widening support upward does not remove the reconstruction tariff when a Mellin primitive is decoupled from its kernel by absolute norms. Here no primitive reconstruction is being estimated by `||K||_1 sup|P|`; the proof keeps the explicit-formula residue geometry and uses the narrowed carrier directly. There is therefore no contradiction between the two statements.

The one-sided placement of the profile is structural for the clean estimate (4). A profile extending a proportional distance below `X` can make `F(Hv)` grow when `Im v>0`, exactly reflecting the smaller physical carrier scale. The present theorem deliberately uses an upward shell so that widening never cancels the horizontal zero penalty `e^{-X(1-beta)}`.

This remains source-side and positive. It does not produce a quantitative Nyman--Beurling distance bound, and it does not prove that a successful signed/complex Nyman approximant must realize the return observable (24). The fixed-width exact-Ford problem also remains open.

## 6. Adversarial checks and prior-art boundary

The potentially dangerous final near-one layer is handled by a genuinely local theorem, not by extrapolating Bellotti's global Theorem 1.1 beyond its stated `K << (log log T)^alpha`, `alpha<1`, range. The only use of a depth proportional to `L=log log t` is as the endpoint of Lemma 2.4's local-disk regime `K << L`; all deeper zeros are suppressed by `Q^{-c_BY}` and ordinary zero counting.

Multiplicity is harmless because Bellotti's zero counts and the residue sum count zeros with multiplicity. The comparison of `R` at nearby slab centers with `R(t)` is uniform for ordinates comparable with `t`. Remote slabs are killed by the `H`-scaled Schwartz factor before their slowly growing zero count can accumulate.

The load-bearing modern input is Chiara Bellotti, *A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem*, Bull. London Math. Soc. 58 (2026), e70442, DOI `10.1112/blms.70442`, arXiv:2508.02041. Lemma 2.4 supplies the local disk count used in (11); the same paper is already anchored in `SOURCES.md`. The Vinogradov--Korobov zero-free input is already anchored separately in the line. The smooth explicit formula and local `O(log t)` zero count are classical and were already used and anchored by `NB-223`.

A targeted prior-art audit found the classical smoothing/explicit-formula framework and Bellotti's local disk lemma, but not the specific source-side deduction that a log shell of width `Theta(X)` converts that lemma into a constant positive-return gap at the exact Ford denominator. No novelty is claimed for the zeta zero theorem itself.

The representation audit separates the generic and arithmetic pieces. Any meromorphic spectrum with a Ford-type zero-free strip and a Bellotti-type `O(K)` local disk count would satisfy the same wide-carrier estimate. The zeta-specific content is that `-zeta'/zeta` supplies exactly such a spectrum and the PNT normalizes the positive von-Mangoldt source to nonzero mass. Thus the mechanism is arithmetic/spectral rather than intrinsically Nyman-geometric.

## Route consequence

`NB-223` left two apparent exact-Ford escapes: stronger control of the final near-one zero layer, or cancellation among zero residues. `NB-224` shows a third, orthogonal option: **change the source resolution until the existing local zero theorem is already strong enough**. At width `H=Theta(X)`, no new zero-density theorem is required to reach the exact Ford denominator with a constant positive gap, although only below a sufficiently small fixed Ford constant.

The remaining sharp questions are now separated. For the original fixed-width shell, one still needs genuinely stronger near-edge information or phase cancellation. For source architectures allowed to widen, the useful optimization problem is to determine the minimal growth of `H(X)` that makes Bellotti's local count competitive, and whether such widening can be connected back to a destination-visible Nyman quantity without reintroducing the reconstruction tariff isolated in `NB-217`.