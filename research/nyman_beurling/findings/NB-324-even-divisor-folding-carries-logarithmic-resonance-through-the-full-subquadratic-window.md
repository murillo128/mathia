# NB-324 — Even-divisor folding carries logarithmic resonance through the full subquadratic window

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-320, NB-322, NB-323
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + GROWING-RATIONAL-DENOMINATOR + LINEAR-TO-SUBQUADRATIC-RESONANCE + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

let `R_n` be the rank-one comparison operator from `NB-314`, and use the scaled adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1}.
\tag{1}
\]

Let `q>=2` be an **even divisor** of `n`, put

\[
d:=\frac nq,
\qquad
m_{n,q}:=\frac{n(n-1)}q=d(n-1),
\tag{2}
\]

and define

\[
\mathcal E_{n,q}
:=
\left\langle
(\sqrt{m_{n,q}}T_{n,m_{n,q}}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

Then the coefficient has the exact first-period main term

\[
\boxed{
\mathcal E_{n,q}
=
\frac{H_q-H_{q/2}}{4n}+\mathcal T_{n,q},
}
\tag{4}
\]

with the denominator-uniform tail bound

\[
\boxed{
|\mathcal T_{n,q}|
\le
\frac{19}{24}\frac1{nq}
<\frac1{nq}.
}
\tag{5}
\]

Consequently, for every sequence of even divisors `q_n|n` with

\[
q_n\longrightarrow\infty,
\tag{6}
\]

with **no further restriction on the relative growth of `q_n` and `n`**, one has

\[
\boxed{
n\mathcal E_{n,q_n}
\longrightarrow
\frac{\log2}{4}.
}
\tag{7}
\]

Using the adjacent-witness norm bound

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2}
\tag{8}
\]

and `||g_2||_2^2=\log2/4`, equation (7) implies

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_{n,q_n}}T_{n,m_{n,q_n}}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2}>0.
}
\tag{9}
\]

Thus the logarithmic adjacent resonance does not disappear in the intermediate-denominator region left open by `NB-322`--`NB-323`. Along the exact even-divisor skeleton it persists for **every growing rational denominator**, from `q=o(sqrt n)` through `sqrt n<<q<<n` and up to `q asymp n`. Since `m=n(n-1)/q`, this gives explicit logarithmic rank-one-mixing obstructions throughout the entire linear-to-subquadratic range on arithmetic subsequences.

In particular, for every fixed

\[
1\le\alpha<2,
\tag{10}
\]

there are power-of-two subsequences with

\[
m_n=n^{\alpha+o(1)}
\tag{11}
\]

for which the lower bound (9) holds. The endpoint `alpha=1` includes every fixed integer multiple `m=d(n-1)` after restricting to `2d|n`; the case `d=1` is exactly `NB-323`.

This remains an absolute matrix-coefficient obstruction for the rank-one-subtracted rescaled operator. It is not a lower bound for the first-free Ford occupation, finite-section excess, a Nyman approximation rate, or RH.

## 1. Every even-divisor scale is a compressed copy of the endpoint pulse train

`NB-314` gives the exact coefficient identity

\[
\mathcal E_{n,q}
=
\int_0^\infty
F_{g_2}(t)\widetilde F_n(m_{n,q}t)\,\frac{dt}{t^2},
\tag{12}
\]

where `widetilde F_n` is the centered reciprocal profile of `u_n`; the interval `(0,1)` may be inserted because `F_(g_2)=0` there.

`NB-323` analyzed the endpoint profile

\[
f_n(y):=\widetilde F_n((n-1)y).
\tag{13}
\]

For `y=k+r`, `0<=r<1`, `0<=k<=n-1`, it proved the exact pulse formula

\[
\boxed{
f_n(k+r)
=
\mathbf 1_{\{0\le r<k/(n-1)\}}
-
\frac{k+1/2}{n}.
}
\tag{14}
\]

At (2),

\[
\widetilde F_n(m_{n,q}t)=f_n(dt).
\tag{15}
\]

Make the change of variables `y=dt`. Since `F_(g_2)` has period `2`,

\[
\boxed{
\mathcal E_{n,q}
=d\int_0^\infty
F_{g_2}(y/d)f_n(y)\,\frac{dy}{y^2}.
}
\tag{16}
\]

The factor `F_(g_2)(y/d)` equals `1/2` precisely on the blocks

\[
[(2j+1)d,(2j+2)d),
\qquad j\ge0,
\tag{17}
\]

and vanishes on the alternating blocks. Because `q` is even and `n=qd`, the period `2d` of this selector divides the period `n` of `f_n`. Hence their product is `n`-periodic. This divisibility is the mechanism that removes the growing-`q` remainder loss of `NB-322`.

## 2. The first period telescopes exactly to one harmonic dyadic increment

On any selected unit cell `[k,k+1)`, equation (14) is exactly the cell analyzed in `NB-323`. Its weighted contribution before the outer factor `d` is

\[
\int_k^{k+1}
\frac{F_{g_2}(y/d)f_n(y)}{y^2}\,dy
=
\frac1{4n\,k(k+1)}.
\tag{18}
\]

Within the first period `0<=y<n`, the selected cells are

\[
k=(2j+1)d,\ldots,(2j+2)d-1,
\qquad
0\le j<q/2.
\tag{19}
\]

The sum over each selected `d`-block telescopes:

\[
\sum_{k=(2j+1)d}^{(2j+2)d-1}
\frac1{k(k+1)}
=
\frac1{(2j+1)d}-\frac1{(2j+2)d}.
\tag{20}
\]

Therefore the complete first-period contribution is

\[
\begin{aligned}
I_{n,q}^{(0)}
&=
\frac{d}{4n}
\sum_{j=0}^{q/2-1}
\left(
\frac1{(2j+1)d}-\frac1{(2j+2)d}
\right)\\[1mm]
&=
\boxed{
\frac{H_q-H_{q/2}}{4n}.
}
\end{aligned}
\tag{21}
\]

This already explains the universality of the coefficient: as soon as the number `q/2` of selected blocks tends to infinity, their alternating harmonic mass approaches `log 2`, independently of how strongly the endpoint pulse train has been compressed.

## 3. All later periods cost only `O(1/(nq))`

Put

\[
p_{n,q}(y):=F_{g_2}(y/d)f_n(y).
\tag{22}
\]

It is `n`-periodic. On a selected unit cell its unweighted integral is, again from the pulse formula,

\[
a_k
:=
\int_k^{k+1}p_{n,q}(y)\,dy
=
\frac{2k-(n-1)}{4n(n-1)},
\tag{23}
\]

while it is zero on an unselected cell. Summing (23) over (19) gives the exact one-period mean mass

\[
\boxed{
M_{n,q}:=\int_0^n p_{n,q}(y)\,dy
=
\frac{d}{8(n-1)}.
}
\tag{24}
\]

Let

\[
\bar p_{n,q}:=\frac{M_{n,q}}n,
\qquad
p^0_{n,q}:=p_{n,q}-\bar p_{n,q}.
\tag{25}
\]

Since `|a_k|<=1/(4n)` and there are `n/2` selected cells, the contribution from all completed selected cells before any point of one period is at most `1/8` in absolute value. Inside one selected cell, `|p_(n,q)|<=1/2`, costing at most another `1/2`. Finally, because `q>=2`, `d<=n/2`, and for `n>=4`

\[
0\le M_{n,q}\le\frac1{12}.
\tag{26}
\]

Hence the zero-mean periodic primitive

\[
P^0_{n,q}(Y)
:=
\int_0^Y p^0_{n,q}(y)\,dy
\tag{27}
\]

satisfies the uniform bound

\[
\boxed{
\|P^0_{n,q}\|_\infty
\le
\frac{17}{24}.
}
\tag{28}
\]

The tail after the first period in (16) is

\[
\mathcal T_{n,q}
=
d\int_n^\infty p_{n,q}(y)\,\frac{dy}{y^2}.
\tag{29}
\]

Its mean part contributes exactly

\[
d\int_n^\infty\bar p_{n,q}\frac{dy}{y^2}
=
\frac{dM_{n,q}}{n^2}
=
\frac{d^2}{8(n-1)n^2},
\tag{30}
\]

while integration by parts for the zero-mean part, using `P^0_(n,q)(n)=0`, gives

\[
\left|
d\int_n^\infty p^0_{n,q}(y)\frac{dy}{y^2}
\right|
\le
\frac{17d}{24n^2}.
\tag{31}
\]

Since `d/(8(n-1))<=1/12`, equations (30)--(31) yield

\[
|\mathcal T_{n,q}|
\le
\frac{19d}{24n^2}
=
\boxed{
\frac{19}{24nq}
},
\tag{32}
\]

which proves (5).

## 4. The intermediate-denominator gap is absent on the exact even-divisor skeleton

If `q=q_n->infinity`, then

\[
H_q-H_{q/2}=\log2+O(q^{-1}),
\tag{33}
\]

and (32) gives

\[
n\mathcal T_{n,q}=O(q^{-1}).
\tag{34}
\]

Equations (21), (33), and (34) prove (7). Dividing by `||g_2||_2 ||u_n||_2` and using (8) gives (9).

The scale map is

\[
m_{n,q}=\frac{n(n-1)}q.
\tag{35}
\]

Thus a growing even divisor `q` may move arbitrarily slowly, producing a scale just below quadratic, or may be comparable with `n`, producing a linear scale. In particular, on `n=2^K`, choosing

\[
d=2^{\lfloor(\alpha-1)K\rfloor},
\qquad
q=n/d,
\tag{36}
\]

gives an even divisor `q->infinity` for every fixed `1<=alpha<2` and

\[
m=d(n-1)=n^{\alpha+o(1)}.
\tag{37}
\]

This fills the power-scale interval left unresolved by the combination of `NB-322` and `NB-323`: the earlier `q=o(sqrt n)` restriction was entirely a remainder-estimate artifact on this divisor family. It does **not** prove the same statement for odd denominators, for `q` not dividing `n`, or for near-rational scales; those remain separate arithmetic questions.

The conclusion is also deliberately about the rank-one-subtracted rescaled coefficient, not about `beta_(n+1)(m)` itself. A logarithmic residue of `sqrt(m)T-R_n` may coexist with substantial projected-dilation overlap, and no target-occupation statement follows from the present source witness.

## 5. Adversarial checks and prior-art audit

The proof uses exact identities before estimates. The parity hypothesis is structural: `q` even is exactly what makes the selector period `2d` divide the endpoint-profile period `n=qd`. The selected blocks in (19) then contain exactly `n/2` integer cells, including the last block ending at `n`; no endpoint cell is omitted. The tail estimate keeps the nonzero one-period mean explicitly and applies integration by parts only to the centered periodic remainder. At `q=n`, `d=1` and (4)--(5) recover the main term and `O(n^-2)` tail scale of `NB-323`. For fixed `q`, (5) is only `O(1/n)` and need not identify the leading constant, consistently with the separate rational-boundary analysis of `NB-320`--`NB-322`.

A fresh prior-art audit checked the classical multiplicative fractional-part autocorrelation of Báez-Duarte, Balazard, Landreau and Saias (arXiv:math/0306251), Balazard--Martin's Wilton/autocorrelation analysis (arXiv:1305.4395), Vasyunin/cotangent-sum formulations including Darses--Hillion (arXiv:2004.10086), and cotangent-sum work connected to Nyman--Beurling. Those sources explain why rational dilations and Bernoulli/fractional-part arithmetic are natural neighboring objects. In the material reviewed, I did not find this finite-section statement: an even-divisor compression of the adjacent endpoint pulse train giving the explicit coefficient `(H_q-H_(q/2))/(4n)` with a uniform `O(1/(nq))` tail for the rank-one-subtracted projected-dilation operator. No external theorem is load-bearing here, and this finding makes no bibliographic novelty claim.

## 6. Research consequence

The live source-side question after `NB-323` was whether the resonance could disappear or oscillate in the intermediate range `sqrt n<<q<<n`. On the exact even-divisor family the answer is now rigid: it does neither. The coefficient converges to the same `log 2/(4n)` law throughout every growing-denominator regime.

Accordingly, a future upper theorem for weighted rank-one mixing on `N<<m<=O(N^2)` cannot hope to obtain uniform decay merely by separating small, intermediate, and maximal rational denominators. It must exploit arithmetic outside the exact divisor skeleton, cancellation unavailable to the adjacent witness, or a genuinely target-aware mechanism. The unresolved arithmetic boundary is now concentrated on odd/nondivisor and near-rational scales rather than on the size of an even exact denominator itself.
