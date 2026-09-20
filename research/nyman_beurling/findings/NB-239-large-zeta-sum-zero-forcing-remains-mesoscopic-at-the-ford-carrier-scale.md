# NB-239 — Large-zeta-sum zero forcing remains mesoscopic at the Ford carrier scale

**Date:** 2026-09-20  
**Status:** `LITERATURE+DERIVED + FRESH-PRIOR-ART-AUDIT + ZETA-SPECIFIC + EXACT-SCALE-SEPARATION + FORD-CARRIER + NEGATIVE/METHOD-BOUNDARY + NB-237/NB-238-REFINEMENT`.

A fresh 2026 inverse theorem of Dong, Wang, Wang and Zhang gives unusually local information about zeros of `zeta`: one abnormally large partial sum

\[
S(x,t)=\sum_{n\le x} n^{it}
\]

forces many zeros into a disk centered near `1+it`. This is much closer in spirit to the surviving `NB-237` source-side problem than ordinary zero-density or global pair-correlation results, so it is a natural candidate to test against the exact Ford carrier.

The test gives a sharp scale mismatch. Put

\[
Q=\log T,
\qquad
\ell=\log Q,
\qquad
R=Q^{2/3}\ell^{1/3},
\]

and specialize the theorem to the arithmetic scale

\[
X:=\log x\asymp R,
\]

which is exactly the moving-shell/Ford diagonal used in `NB-223`--`NB-238`. If the large-sum theorem is written with its zero-count parameter `\mathcal L`, then its forced disk has radius

\[
\boxed{
 r_{\rm DWWZ}(\mathcal L)
 =
 \mathcal L\frac{Q}{X^2}.
}
\]

The Ford carrier, by contrast, resolves vertical phase at scale `1/X asymp 1/R`. Hence

\[
\boxed{
\frac{r_{\rm DWWZ}(\mathcal L)}{1/X}
=
\mathcal L\frac{Q}{X}
\asymp
\mathcal L\frac{Q}{R}
\longrightarrow\infty.
}
\]

The missing factor is therefore

\[
\boxed{
\frac QR
=
Q^{1/3}\ell^{-1/3}.
}
\]

It does not disappear by changing `\mathcal L`, because both the forced zero count and the disk radius grow linearly in `\mathcal L`. Equivalently, the theorem guarantees only average zero density

\[
\frac{\#\{\rho\text{ forced}\}}{r_{\rm DWWZ}}
\asymp
\frac{X^2}{Q},
\]

whereas the carrier-locked packets left alive by `NB-231` and `NB-237` have vertical density `Theta(X)`. The zero-forcing theorem is therefore short by the same diverging factor `Q/X asymp Q/R` needed to resolve one zero per carrier cell.

This is not a criticism of the new theorem: its disks are genuinely microscopic on the ordinary unit scale. The point is that the Nyman/Ford endpoint has already descended to the much finer `1/R` scale. The new inverse theorem lives in the mesoscopic gap between those two regimes and, in its published form, cannot exclude the phase-locked Ford packet.

## 1. The fresh inverse theorem and the scale dictionary

Dong, Ruihua Wang, Weijia Wang and Hao Zhang prove in Theorem 1.1 of *Large zeta sums and zeros of the Riemann zeta function* (arXiv:2608.31060, submitted 31 August 2026) the following pointwise implication. There are absolute constants such that if

\[
T\le |t|\le 2T,
\qquad
\exp(\sqrt{\log T})\le x\le \sqrt T,
\]

and

\[
|S(x,t)|=\frac{x}{N},
\qquad
N\le (\log x)^{1/100},
\]

then there is a real `phi` with

\[
|\phi-t|\ll N
\]

such that, for every

\[
cN^6\le \mathcal L\le \frac{\log x}{2},
\]

the disk

\[
\boxed{
\left\{
 s:
 |s-(1+i\phi)|
 <
 \mathcal L\frac{\log T}{(\log x)^2}
\right\}
}
\]

contains at least `\mathcal L/360` nontrivial zeros of `zeta`, counted with multiplicity.

The source theorem is genuinely local near the one-line and is proved by adapting the Granville--Soundararajan zero-forcing mechanism to the twisted zeta sum. Its published radius is the only feature needed in the scale audit below.

Now place it on the current line's exact Ford diagonal. Write

\[
X=\log x=YR,
\qquad
Y\to Y_*\in(0,\infty).
\]

The theorem's admissible `x` range is automatically satisfied for all sufficiently large `Q`, because

\[
\sqrt Q
\ll
R
\ll
Q.
\]

Thus there is no range obstruction to comparing the new theorem with the source scale in `NB-223`--`NB-238`.

Its disk radius becomes

\[
\boxed{
 r_{\rm DWWZ}(\mathcal L)
 =
 \frac{\mathcal L}{Y^2}
 \frac{Q}{R^2}.
}
\tag{1}
\]

Since

\[
\frac{Q}{R^2}
=
Q^{-1/3}\ell^{-2/3}
\longrightarrow0,
\]

the disk is indeed `o(1)`. But the relevant comparison is not with one; it is with the Ford carrier period

\[
\Delta_F
\asymp
\frac1X
\asymp
\frac1R.
\tag{2}
\]

Equations (1)--(2) give

\[
\boxed{
\frac{r_{\rm DWWZ}(\mathcal L)}{\Delta_F}
\asymp
\mathcal L\frac QR.
}
\tag{3}
\]

Because `Q/R -> infinity`, even the most favorable bounded-`\mathcal L` output spans a diverging number of carrier periods.

## 2. The mismatch is a density loss, not a poor choice of `\mathcal L`

Theorem 1.1 forces at least

\[
\frac{\mathcal L}{360}
\]

zeros inside a disk of radius (1). Ignoring harmless constants, the corresponding guaranteed population per unit vertical length is therefore at most the scale

\[
\frac{\mathcal L}{r_{\rm DWWZ}(\mathcal L)}
\asymp
\frac{X^2}{Q}.
\tag{4}
\]

One Ford phase cell has length `Theta(1/X)`, so the number of zeros forced per carrier cell by (4) is only

\[
\boxed{
\frac{X^2}{Q}\frac1X
=
\frac XQ
\asymp
\frac RQ
\longrightarrow0.
}
\tag{5}
\]

By contrast, the matched critical packet from `NB-231` has

\[
\gamma_j=t+\frac{2\pi qj}{X},
\]

so its spacing is `Theta(1/X)` and its local density is `Theta(X)`. It places order-one population in a positive fraction of carrier cells while keeping the phases

\[
e^{iX(\gamma_j-t)}
\]

aligned. Comparing this density with (4) gives

\[
\boxed{
\frac{X}{X^2/Q}
=
\frac QX
\asymp
\frac QR
\to\infty.
}
\tag{6}
\]

Thus the same factor found geometrically in (3) reappears as a population-density deficit. Increasing `\mathcal L` cannot repair it: the theorem asks for proportionally more zeros but simultaneously enlarges the disk by exactly the same factor.

A carrier-scale inverse theorem with comparable linear count would instead need a radius of order

\[
\boxed{
 r_{\rm carrier}(\mathcal L)
\lesssim
\frac{\mathcal L}{X},
}
\tag{7}
\]

up to constants or slowly varying losses. Relative to (1), this asks to save precisely

\[
\frac{r_{\rm DWWZ}}{\mathcal L/X}
=
\frac QX
\asymp
\frac QR.
\tag{8}
\]

Equation (8) is the quantitative gap between the new inverse theorem and the current Nyman/Ford endpoint.

## 3. It also misses the critical horizontal depth and the selected ordinate

The critical packet is not only vertically microscopic. In the conservative regime used in `NB-231`--`NB-238`,

\[
1\ll J:=\frac RH\le \ell,
\]

and the dangerous zeros lie at Ford depth

\[
1-\beta
=
\frac{\log J+O(1)}{X}.
\tag{9}
\]

Since `N>=1` for every partial sum, the smallest admissible parameter in the new theorem is bounded below by an absolute positive constant. Hence every disk supplied by Theorem 1.1 has radius at least

\[
 r_{\min}
\gg
\frac{Q}{X^2}.
\tag{10}
\]

Comparing (10) with (9),

\[
\frac{r_{\min}}{(\log J)/X}
\gg
\frac{Q}{X\log J}
\asymp
\frac{Q}{R\log J}
\longrightarrow\infty
\qquad(J\le\ell).
\tag{11}
\]

So even the smallest forced disk is horizontally much thicker than the entire `YD-log J=O(1)` transition layer isolated in `NB-230`--`NB-234`. It cannot distinguish the depth mark that drives the critical Ford residue.

There is a second localization loss. The theorem guarantees a center `1+i\phi` only with

\[
|\phi-t|\ll N.
\tag{12}
\]

The current carrier window has width

\[
\frac1H
=
\frac JR
=o(1),
\tag{13}
\]

and its phase itself changes on the still finer scale `1/X`. Since `N>=1`, the guaranteed localization precision in (12) is not enough to place the forced cluster inside the specific `1/H` window selected by the Nyman carrier. This does not say that the actual `phi` must be far from `t`; it says that the theorem as stated gives no deterministic control at the scale required by (13).

The same comparison also explains why this result does not subsume Bellotti's carrier-scale disk estimate used in `NB-224`. Bellotti's local theorem operates at radii `K/R` for `K` only polylogarithmic in `Q`. Already the minimal DWWZ radius corresponds to

\[
K_{\rm DWWZ}
:=Rr_{\min}
\gg
\frac QR
=
Q^{1/3}\ell^{-1/3},
\]

which eventually dominates every `O(\ell)` Bellotti window. The two theorems occupy genuinely different local scales.

## 4. The source antecedent is also not the current Euler-shell observable

There is an independent interface issue before the scale mismatch above is even reached. The new theorem starts from a large **unweighted initial-segment sum**

\[
S(x,t)=\sum_{n\le x}n^{it}.
\]

The surviving Nyman source route instead studies a localized von-Mangoldt shell, schematically

\[
\sum_n
\Lambda(n)
 h_{X,H}(\log n)
 n^{-\sigma_X-it},
\]

or its positive-return defect. The shell occupies a narrow multiplicative band and reads prime weight; the zeta sum reads all integers in the whole prefix. No result currently persisted in this line shows that an `o(1)` Euler-shell return at Ford scale forces

\[
|S(e^X,t)|\ge \frac{e^X}{N}
\]

with `N` in the range required by the inverse theorem.

This distinction matters because the scale obstruction above survives even if that missing bridge is granted for free in the strongest favorable case `N=O(1)`. Thus the finding does not rest on the antecedent mismatch: **even a hypothetical perfect bridge to a maximal zeta sum would still leave the published zero cluster too coarse by the factor `Q/R`.**

Conversely, the new paper remains potentially useful as a method template. Its pretentious/Gaussian zero-forcing argument is genuinely source-sensitive. A shell-weighted or prime-weighted adaptation would become relevant to the Ford endpoint if it could simultaneously produce

\[
\text{vertical radius }O(\mathcal L/X),
\qquad
|\phi-t|=O(J/X),
\]

and retain enough horizontal information to resolve depth `(log J)/X`. Those requirements are substantially stronger than Theorem 1.1 as presently stated, but they give a precise target for any attempted adaptation.

## 5. Adversarial checks, prior-art boundary, and route consequence

Several possible escapes do not change the conclusion.

First, the parameter `\mathcal L` cannot be optimized away: both count and radius are linear in it, so the density ratio (5) is independent of `\mathcal L`. Second, allowing `N` to grow only worsens the geometric localization because the admissible lower endpoint `\mathcal L\ge cN^6` increases. The audit therefore uses the most favorable case `N=O(1)`. Third, one could make the DWWZ radius carrier-sized by taking `\log x` much closer to `Q`; however the current Nyman source is tied to `X\asymp R`, and changing `X` to `Theta(Q)` changes the arithmetic shell rather than improving the same endpoint theorem. No existing bridge transports the Ford-shell return to that larger auxiliary scale.

The result is a method boundary, not a statement about actual zero statistics. It does not assert that zeta contains the matched packet from `NB-231`, nor that the Dong--Wang--Wang--Zhang method cannot be sharpened or localized further. It says only that their **published Theorem 1.1**, after the exact Ford substitution required by this line, does not provide the phase/depth resolution needed to rule out that packet.

The primary prior-art source is:

- Zikang Dong, Ruihua Wang, Weijia Wang, Hao Zhang, *Large zeta sums and zeros of the Riemann zeta function*, arXiv:2608.31060 (2026), Theorem 1.1, https://arxiv.org/abs/2608.31060.

That theorem and its Granville--Soundararajan ancestry are not claimed as new. The line-local contribution is the exact scale dictionary (1)--(13): on the Ford diagonal, its zero-forcing disk is smaller than a unit interval but larger than a carrier cell by the diverging factor `Q/R`, and it is simultaneously too thick to resolve the critical Ford depth.

A decisive falsification of this finding would be a stronger theorem already implicit in the cited paper that, under the same large-sum hypothesis and with `X\asymp R`, localizes `Theta(\mathcal L)` zeros to radius `O(\mathcal L/X)` around an ordinate known to accuracy `O(J/X)`, or an equivalent phase-sensitive statement. The published Theorems 1.1--1.2 do not provide such a conclusion.

## Route consequence

`NB-238` showed that half-isolated-zero clustering is too coarse because it collapses the dangerous `1/R` packet into one clump. `NB-239` shows that the newest pointwise **source-to-zero inverse theorem** is substantially finer than classical unit-scale zero counts but still lands above the same carrier resolution: its natural radius is

\[
\mathcal L\frac{Q}{R^2}
=
\frac QR
\left(\frac{\mathcal L}{R}\right),
\]

whereas the phase-locked packet lives on radius `Theta(\mathcal L/R)`.

The source-side frontier therefore remains unchanged but more sharply quantified. A useful new inverse theorem must recover the missing factor `Q/R`, or bypass geometric zero forcing and estimate the signed `R^{-1}zeta'/zeta` carrier of `NB-237` directly. Merely importing the present large-zeta-sum zero cluster does not resolve the Ford endpoint.