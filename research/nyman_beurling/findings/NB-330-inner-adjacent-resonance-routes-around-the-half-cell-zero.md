# NB-330 — Inner adjacent resonance routes around the half-cell zero

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-327, NB-328, NB-329
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + INNER-ADJACENT-WITNESS + ONE-CELL-DRIFT + PHASE-UNIFORM-RESONANCE + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let `R_n` be the rank-one comparison operator from `NB-314`. Put

\[
q:=n-1,
\qquad
u_q:=g_q-\frac{q-1}{q}g_{q-1}.
\tag{1}
\]

For integers

\[
n\ge9,
\qquad d\ge1,
\qquad 0\le r\le d,
\]

set

\[
\rho:=\frac rd\in[0,1],
\qquad
m:=d(n-1)+r=d(q+\rho),
\tag{2}
\]

and define the inner-adjacent rank-one-error coefficient

\[
\mathcal F_{n,d,r}
:=
\left\langle
(\sqrt m\,T_{n,m}-R_n)g_2,\nu_q
\right\rangle.
\tag{3}
\]

Then the whole one-cell drift has the phase-uniform estimate

\[
\boxed{
\left|
\mathcal F_{n,d,r}
+\frac{\log2}{4(n-1)}
\right|
\le
\frac{28d}{(n-1)^2}.
}
\tag{4}
\]

Consequently, for arbitrary integer sequences `d_n=o(n)` and `0<=r_n<=d_n`, with no convergence assumption on `r_n/d_n`, one has

\[
\boxed{
(n-1)\mathcal F_{n,d_n,r_n}
\longrightarrow
-\frac{\log2}{4}.
}
\tag{5}
\]

Using the adjacent-witness norm bound from `NB-304`, this yields the phase-uniform operator obstruction

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_n}T_{n,m_n}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2},
}
\tag{6}
\]

where `m_n=d_n(n-1)+r_n`.

Thus the half-cell zero of `NB-329` is not an operator-level mixing window. The outer adjacent witness `u_n` cancels at `rho=1/2`, but the immediately inner adjacent witness `u_(n-1)` remains resonant with the same leading magnitude, uniformly throughout the full drift cell `0<=rho<=1`.

## 1. Shift the witness inward by one adjacent mode

The exact rank-one-error identity from `NB-314` applies to every target in `U_n`. Since `nu_q in U_n`,

\[
\mathcal F_{n,d,r}
=
\int_0^\infty
F_{g_2}(t)\,\widetilde F_q(mt)\frac{dt}{t^2},
\tag{7}
\]

where

\[
\widetilde F_q(z)
=
\left\{\frac zq\right\}
-\frac{q-1}{q}
\left\{\frac z{q-1}\right\}
-\frac1{2q}.
\tag{8}
\]

Scale by the integer `d` rather than by the drifting factor. Define

\[
A:=q+\rho,
\qquad
h_{q,\rho}(y):=\widetilde F_q(Ay),
\qquad
s_d(y):=F_{g_2}(y/d).
\tag{9}
\]

Then

\[
\boxed{
\mathcal F_{n,d,r}
=
d\int_0^\infty
s_d(y)h_{q,\rho}(y)\frac{dy}{y^2}.
}
\tag{10}
\]

As in `NB-327`--`NB-329`, because `d` is an integer the source selector is constant on every unit cell:

\[
s_d(y)=
\begin{cases}
0,&y\in[2jd,(2j+1)d),\\[1mm]
1/2,&y\in[(2j+1)d,(2j+2)d).
\end{cases}
\tag{11}
\]

The change from `NB-329` is entirely in the target witness. The scale `A=q+rho` lies one adjacent cell farther out than the `q-1+rho` scale seen by `u_q` in the previous interpolation.

## 2. The inner witness has a phase-independent cell coefficient

Fix

\[
1\le k\le K:=\left\lfloor\frac q4\right\rfloor,
\qquad
y=k+x,
\qquad 0\le x<1.
\]

For `q>=8` the two relevant fractional parts have at most one carry on these cells, uniformly for `rho in [0,1]`. Their carry thresholds are

\[
\alpha_k
:=
\frac{q-\rho k}{q+\rho},
\qquad
\beta_k
:=
\frac{q-1-(1+\rho)k}{q+\rho}.
\tag{12}
\]

Direct substitution into (8) cancels every affine `x` term and gives

\[
\boxed{
h_{q,\rho}(k+x)
=
-\mathbf1_{\{x\ge\alpha_k\}}
+\frac{q-1}{q}\mathbf1_{\{x\ge\beta_k\}}
-\frac{k+1/2}{q}.
}
\tag{13}
\]

The two threshold locations satisfy the exact identities

\[
k+\alpha_k
=
\frac{q(k+1)}{A},
\qquad
k+\beta_k
=
\frac{(q-1)(k+1)}{A}.
\tag{14}
\]

Hence

\[
\int_{k+\alpha_k}^{k+1}\frac{dy}{y^2}
=
\frac{\rho}{q(k+1)},
\tag{15}
\]

while

\[
\frac{q-1}{q}
\int_{k+\beta_k}^{k+1}\frac{dy}{y^2}
=
\frac{1+\rho}{q(k+1)}.
\tag{16}
\]

The baseline contributes

\[
\frac{k+1/2}{q}
\int_k^{k+1}\frac{dy}{y^2}
=
\frac{k+1/2}{qk(k+1)}.
\tag{17}
\]

Combining (15)--(17), all dependence on `rho` disappears:

\[
\boxed{
\int_k^{k+1}
h_{q,\rho}(y)\frac{dy}{y^2}
=
-\frac1{2q\,k(k+1)}.
}
\tag{18}
\]

This is the central mechanism. `NB-329` found an outer-adjacent coefficient proportional to `1-2rho`; shifting the witness inward by one mode produces a cell coefficient that is exactly constant across the same drift interval.

Because a selected source cell has `s_d=1/2`, the contribution of the first `K` cells is

\[
I^{(0)}_{n,d,r}
=
-\frac d{4q}
\sum_{\substack{1\le k\le K\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}.
\tag{19}
\]

The full selector sum still telescopes block by block:

\[
d
\sum_{\substack{k\ge1\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
=
\log2.
\tag{20}
\]

Since `K+1>q/4`, truncating (20) at `K` costs at most `1/(K+1)<4/q`. Therefore

\[
\boxed{
\left|
I^{(0)}_{n,d,r}
+\frac{\log2}{4q}
\right|
\le
\frac d{q^2}.
}
\tag{21}
\]

## 3. Cellwise centering keeps the remaining tail at `O(d/q^2)`

Introduce the centered sawtooth

\[
\phi_j(z):=\left\{\frac zj\right\}-\frac12.
\]

Then

\[
h_{q,\rho}(y)
=
\phi_q(Ay)
-\frac{q-1}{q}\phi_{q-1}(Ay).
\tag{22}
\]

For any global unit cell `[J,J+1)`, put

\[
b_J:=\int_0^1h_{q,\rho}(J+x)\,dx.
\tag{23}
\]

After `z=Ay`, the interval has length `A=q+rho`. A centered `phi_q` integrates to zero over every interval of length `q`, leaving a residual interval of length at most one. A centered `phi_(q-1)` integrates to zero over every interval of length `q-1`, leaving a residual interval of length at most two. Since every centered sawtooth has magnitude at most `1/2`,

\[
\boxed{
|b_J|
\le
\frac{3}{2A}
\le
\frac{3}{2q}.
}
\tag{24}
\]

Also `|h_(q,rho)|<1`. Thus, for `q>=8`, the centered cell function

\[
q_J(x):=h_{q,\rho}(J+x)-b_J
\]

has mean zero and `|q_J|<=3/2`. With `w_J(x)=(J+x)^(-2)`, the same one-cell variation estimate as in `NB-329` gives

\[
\left|
\int_0^1q_J(x)w_J(x)\,dx
\right|
\le
\frac3{J^3},
\tag{25}
\]

and the mean part satisfies

\[
\left|
b_J\int_0^1w_J(x)\,dx\right|
\le
\frac{3}{2qJ(J+1)}.
\tag{26}
\]

Let `L=K+1>q/4`. Using `|s_d|<=1/2`,

\[
\begin{aligned}
|\mathcal T_{n,d,r}|
&\le
\frac d2
\sum_{J=L}^\infty
\left(
\frac3{J^3}
+
\frac{3}{2qJ(J+1)}
\right)\\[1mm]
&\le
\frac d2
\left(
\frac3{L^2}
+
\frac{3}{2qL}
\right)\\[1mm]
&\le
\boxed{\frac{27d}{q^2}}.
\end{aligned}
\tag{27}
\]

Combining (21) and (27) proves (4).

## 4. The half-cell zero is only a witness-level cancellation

The estimate (4) is uniform in `rho`; in particular no limit of `r/d` is needed. If `d_n=o(n)`, then

\[
q\mathcal F_{n,d_n,r_n}
\longrightarrow
-\frac{\log2}{4}
\]

for every choice `0<=r_n<=d_n`. This includes the exact half-cell phases with even `d_n` and `r_n=d_n/2`, the shrinking neighborhoods of half drift singled out by `NB-329`, and both endpoint lattices.

Now `NB-304`, applied at index `q=n-1`, gives

\[
\|\nu_q\|_2^2
\le
\frac{2H_{q-2}+1+\pi^2/18}{q^2},
\tag{28}
\]

while

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2.
\tag{29}
\]

Therefore

\[
\|\sqrt mT_{n,m}-R_n\|
\ge
\frac{|\mathcal F_{n,d,r}|}{\|g_2\|_2\,\|\nu_q\|_2},
\tag{30}
\]

and (5), (28), and `H_q~log q` give (6).

So the operator routes around the zero found in `NB-329` in the most local possible way: it moves from `u_n` to `u_(n-1)`. No optimization over a large family is required. The surviving obstruction has exactly the same asymptotic `1/sqrt(log n)` scale as the endpoint resonances.

The conclusion is limited to the one-cell bands

\[
d(n-1)\le m\le dn,
\qquad d=o(n).
\tag{31}
\]

These bands do not cover the whole intermediate window. In particular, the gaps between the `d`-band and the `(d+1)`-band remain unanalysed when `d<<n`. The live source-side question therefore moves from half-cell cancellation to **multi-cell drift across those gaps**.

## 5. Adversarial checks and prior-art boundary

The derivation was pressure-tested at the points most likely to generate a false routing argument.

- The target `nu_q` lies in `U_n`, so the finite-section projection disappears legitimately in the bilinear pairing, while `R_n` still subtracts the intrinsic reciprocal mean of `nu_q`.
- The scale is `A=q+rho`, not `q-1+rho`; this one-index shift is exactly what changes the affine `1-2rho` law of `NB-329` into the phase-independent coefficient (18).
- For `q>=8` and `k<=floor(q/4)`, both fractional parts have at most one carry uniformly for all `rho in [0,1]`; equations (12)--(18) therefore require no hidden phase subdivision.
- The two carry contributions depend on `rho`, but their difference is exactly `1/[q(k+1)]`; the cancellation of `rho` occurs before any asymptotic limit.
- The tail estimate uses only cellwise centering. It does not assume a common global period for intermediate rational phases.
- The asymptotic operator bound is uniform in the phase sequence. It therefore covers `rho_n->1/2`, exact half drift, and phases that do not converge.
- The result remains source-side. It does not show that the moving first-free Ford datum occupies this inner adjacent direction, does not give a finite-section target gain, and has no RH consequence by itself.

A fresh prior-art audit again found the nearest classical domains in Michel Balazard's work on integer dilations of the fractional-part function and in the multiplicative autocorrelation work of Michel Balazard and Bruno Martin. Werner Ehm's Nyman--Beurling Gram formulas and Hugh Carvill's multiscale Gram-decay work are also nearby structurally. The audited material concerns weighted fractional-part correlations, distances between dilates, or Gram structure; it did not state the present finite-section two-adjacent routing mechanism or the phase-uniform cell coefficient (18). This is an audit boundary, not a claim of bibliographic novelty.

External results are not load-bearing. The proof uses only the persisted identities from `NB-304`, `NB-314`, and `NB-327`--`NB-329` plus elementary fractional-part algebra and weighted one-cell estimates. `SOURCES.md` therefore needs no new dependency entry.

Relevant audit anchors:

- Michel Balazard, *Sur les dilatations entières de la fonction partie fractionnaire*, Functiones et Approximatio Commentarii Mathematici 35 (2006), DOI `10.7169/facm/1229442615`.
- Michel Balazard and Bruno Martin, *Sur l'autocorrélation multiplicative de la fonction "partie fractionnaire" et une fonction définie par J. R. Wilton*, arXiv:1305.4395.
- Werner Ehm, *On certain Gram matrices and their associated series*, arXiv:2405.06349.
- Hugh Carvill, *Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing*, arXiv:2510.18132.

## Research consequence

`NB-329` identified a genuine zero of the outer adjacent matrix coefficient at half-cell drift, but that zero does not survive even the smallest structural enlargement of the witness family. The next inner adjacent mode supplies a phase-independent coefficient of the same leading size across the entire cell.

Therefore a subquadratic operator-mixing theorem cannot be based on the half-cell cancellation, nor on a shrinking neighborhood of that phase, inside the bands `d(n-1)<=m<=dn` with `d=o(n)`. Any actual transition must occur in the multi-cell gaps between these bands, exploit a different scaling geometry, or enter through the still-separate destination-side occupation problem.
