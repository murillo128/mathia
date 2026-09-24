# NB-325 — Two-period complementarity extends divisor resonance to odd denominators

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-323, NB-324
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + ODD-DIVISOR-DENOMINATOR + TWO-PERIOD-COMPLEMENTARITY + LINEAR-TO-SUBQUADRATIC-RESONANCE + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

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

Let `q>=3` be an **odd divisor** of `n`, and put

\[
d:=\frac nq,
\qquad
m_{n,q}:=\frac{n(n-1)}q=d(n-1).
\tag{2}
\]

Define the same rank-one-subtracted matrix coefficient as in `NB-324`,

\[
\mathcal E_{n,q}
:=
\left\langle
(\sqrt{m_{n,q}}T_{n,m_{n,q}}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

Then

\[
\boxed{
\mathcal E_{n,q}
=
\frac{H_{q-1}-H_{(q-1)/2}}{4n}
+\mathcal T^{\mathrm{odd}}_{n,q},
}
\tag{4}
\]

with the uniform tail bound

\[
\boxed{
|\mathcal T^{\mathrm{odd}}_{n,q}|
\le
\frac{3}{4nq}.
}
\tag{5}
\]

Consequently, for every sequence of odd divisors `q_n|n` with

\[
q_n\longrightarrow\infty,
\tag{6}
\]

and with no restriction on the relative growth of `q_n` and `n`, one has

\[
\boxed{
n\mathcal E_{n,q_n}
\longrightarrow
\frac{\log2}{4}.
}
\tag{7}
\]

Using the adjacent-witness norm bound from `NB-304`,

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{8}
\]

and `||g_2||_2^2=\log2/4`, equation (7) gives

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

Combining this odd-divisor theorem with the even-divisor theorem `NB-324` removes the parity restriction completely:

\[
\boxed{
q_n\mid n,
\quad q_n\to\infty
\quad\Longrightarrow\quad
n\mathcal E_{n,q_n}\to\frac{\log2}{4},
}
\tag{10}
\]

for **every** growing exact divisor denominator.

In particular, the resonance is not an even-denominator artifact. On `n=3^K`, choosing

\[
d=3^{\lfloor(\alpha-1)K\rfloor},
\qquad
q=n/d,
\tag{11}
\]

produces odd divisors `q->infinity` and

\[
m=d(n-1)=n^{\alpha+o(1)}
\tag{12}
\]

for every fixed `1<=alpha<2`, while the lower bound (9) persists. Thus purely odd arithmetic subsequences already carry the same logarithmic rank-one-mixing obstruction throughout the full linear-to-subquadratic power window.

The statement remains source-side. It is an absolute matrix-coefficient obstruction for the rank-one-subtracted rescaled projected-dilation operator. It is not a lower bound for first-free Ford occupation, finite-section excess, a Nyman approximation rate, or RH.

## 1. The odd case is not periodic over `n`, but it closes exactly over `2n`

`NB-314` and `NB-324` give

\[
\mathcal E_{n,q}
=
\int_0^\infty
F_{g_2}(t)\widetilde F_n(m_{n,q}t)\,\frac{dt}{t^2},
\tag{13}
\]

where `widetilde F_n` is the centered reciprocal profile of `u_n`. Put

\[
f_n(y):=\widetilde F_n((n-1)y).
\tag{14}
\]

The exact pulse formula of `NB-323` is

\[
\boxed{
f_n(k+r)
=
\mathbf1_{\{0\le r<k/(n-1)\}}
-
\frac{k+1/2}{n},
}
\tag{15}
\]

for `0<=k<=n-1` and `0<=r<1`, extended `n`-periodically.

At the scale (2),

\[
\widetilde F_n(m_{n,q}t)=f_n(dt).
\]

After `y=dt`,

\[
\boxed{
\mathcal E_{n,q}
=d\int_0^\infty
F_{g_2}(y/d)f_n(y)\,\frac{dy}{y^2}.
}
\tag{16}
\]

Write

\[
s_d(y):=F_{g_2}(y/d),
\qquad
p_{n,q}(y):=s_d(y)f_n(y).
\tag{17}
\]

The selector `s_d` is `2d`-periodic and equals `1/2` on the blocks

\[
[(2j+1)d,(2j+2)d),
\tag{18}
\]

and zero on the alternating blocks. For even `q`, `2d|n`, which is the one-period alignment used in `NB-324`. For odd `q`, the shift by one `n=qd` period flips the selector instead:

\[
\boxed{
s_d(y+n)=\frac12-s_d(y)}
\tag{19}
\]

away from block boundaries. Since `f_n(y+n)=f_n(y)`,

\[
\boxed{
p_{n,q}(y)+p_{n,q}(y+n)=\frac12f_n(y).}
\tag{20}
\]

The centered profile has zero mean over its `n`-period,

\[
\int_0^n f_n(y)\,dy=0.
\tag{21}
\]

Therefore `p_(n,q)` is `2n`-periodic and has zero mean over that period:

\[
\boxed{
\int_0^{2n}p_{n,q}(y)\,dy=0.
}
\tag{22}
\]

This two-period complementarity is the exact replacement for the even-divisor one-period alignment. Odd parity does not destroy the fold; it merely doubles the period before the selector closes.

## 2. The first period gives the odd alternating-harmonic increment exactly

On a selected unit cell `[k,k+1)` in the first `n`-period, equation (15) gives exactly the weighted identity already used in `NB-324`,

\[
\boxed{
\int_k^{k+1}
\frac{p_{n,q}(y)}{y^2}\,dy
=
\frac1{4n\,k(k+1)}.
}
\tag{23}
\]

Because `q` is odd, write `q=2s+1`. Inside `[0,n)`, the selected `d`-blocks are

\[
[(2j+1)d,(2j+2)d),
\qquad
0\le j<s.
\tag{24}
\]

Summing (23) over the `d` cells in one selected block telescopes:

\[
\sum_{k=(2j+1)d}^{(2j+2)d-1}
\frac1{k(k+1)}
=
\frac1{(2j+1)d}-\frac1{(2j+2)d}.
\tag{25}
\]

Hence the contribution of the complete first `n`-period to (16) is

\[
\begin{aligned}
I_{n,q}^{(0)}
&=
\frac{d}{4n}
\sum_{j=0}^{s-1}
\left(
\frac1{(2j+1)d}-\frac1{(2j+2)d}
\right)\\[1mm]
&=
\frac1{4n}
\sum_{j=0}^{s-1}
\left(
\frac1{2j+1}-\frac1{2j+2}
\right)\\[1mm]
&=
\boxed{
\frac{H_{q-1}-H_{(q-1)/2}}{4n}.
}
\end{aligned}
\tag{26}
\]

Thus the same dyadic harmonic mass already appears before the complementary second period is used. The only remaining question is whether the later periods can change it at order `1/n`.

## 3. Two-period zero mean makes the whole later tail only `O(1/(nq))`

The unweighted integral of `p_(n,q)` over a selected cell with local index `k mod n` is again the exact quantity from `NB-324`,

\[
a_k
:=
\int_k^{k+1}p_{n,q}(y)\,dy
=
\frac{2k-(n-1)}{4n(n-1)},
\qquad 0\le k<n,
\tag{27}
\]

whenever that copy of the cell is selected. In particular,

\[
\boxed{|a_k|\le\frac1{4n}.}
\tag{28}
\]

Across any complete `2n`-period, the selector chooses exactly `n` unit cells. Starting from the block boundary `y=n`, define

\[
P_{n,q}(Y):=\int_n^Yp_{n,q}(y)\,dy.
\tag{29}
\]

For `n<=Y<=3n`, the completed selected cells contribute at most

\[
n\cdot\frac1{4n}=\frac14
\tag{30}
\]

in total absolute value. Inside the at most one current selected unit cell, `|p_(n,q)|<=1/2`, adding at most `1/2`. Therefore

\[
\boxed{
\sup_{n\le Y\le3n}|P_{n,q}(Y)|\le\frac34.
}
\tag{31}
\]

By (22), `P_(n,q)` repeats after `2n`, so (31) holds for every `Y>=n`.

The tail after the first period is

\[
\mathcal T^{\mathrm{odd}}_{n,q}
=d\int_n^\infty p_{n,q}(y)\,\frac{dy}{y^2}.
\tag{32}
\]

Integration by parts, using `P_(n,q)(n)=0`, boundedness of `P_(n,q)`, and (31), gives

\[
\begin{aligned}
|\mathcal T^{\mathrm{odd}}_{n,q}|
&\le
2d\|P_{n,q}\|_\infty
\int_n^\infty\frac{dy}{y^3}\\[1mm]
&\le
\frac{3d}{4n^2}
=
\boxed{\frac{3}{4nq}}.
\end{aligned}
\tag{33}
\]

This proves (5). The important point is that no factor growing with the odd denominator is lost: the selector mismatch is repaired exactly after two periods, and the primitive remains uniformly bounded.

## 4. Every growing exact divisor denominator has the same asymptotic coefficient

For odd `q`,

\[
H_{q-1}-H_{(q-1)/2}
=
\log2+O(q^{-1}).
\tag{34}
\]

Together with (33), this gives

\[
n\mathcal E_{n,q}
=
\frac14\left(H_{q-1}-H_{(q-1)/2}\right)
+O(q^{-1})
=
\frac{\log2}{4}+O(q^{-1}),
\tag{35}
\]

uniformly in the relative size of `q` and `n`. This proves (7).

`NB-324` proves the corresponding statement for even divisors,

\[
\mathcal E_{n,q}
=
\frac{H_q-H_{q/2}}{4n}
+O\!\left(\frac1{nq}\right).
\tag{36}
\]

Equations (35)--(36) therefore give (10) for arbitrary growing divisors `q|n`.

Finally,

\[
\|\sqrt mT_{n,m}-R_n\|
\ge
\frac{|\mathcal E_{n,q}|}{\|g_2\|_2\|u_n\|_2}.
\tag{37}
\]

Insert (7), (8), and `||g_2||_2^2=\log2/4`. Since `H_(n-2)~\log n`, this gives (9) with the same limiting constant as the even-divisor family.

The power-scale construction (11)--(12) is purely odd: on `n=3^K`, both `d` and `q` are odd. Thus the full interval `1<=alpha<2` of explicit source resonances survives even after excluding every even denominator.

## 5. What this closes and what remains live

`NB-324` left odd denominators as the nearest possible arithmetic escape from the exact rational pulse train. Equations (19)--(33) show that this escape is not real. The parity mismatch does not produce cancellation at the weighted `1/t^2` level; it only changes the closure period from `n` to `2n`.

The exact-divisor classification is now parity-complete: **every growing divisor denominator carries the same leading coefficient `log 2/(4n)`**. The live arithmetic questions are therefore narrower:

- `q` not dividing `n`, where the selector and adjacent pulse train no longer close after one or two exact section periods;
- near-rational scales, where the exact block boundaries drift across the pulse locations;
- source families different from the adjacent witness, if a uniform theorem is allowed to project away or otherwise neutralize the explicit divisor resonance.

A future upper mixing theorem cannot use parity as its discriminator. It must exploit arithmetic genuinely absent from the exact divisor skeleton or add a mechanism that is target-aware.

This finding does not show that `||sqrt(m)T-R_n||` stays order one; the certified residue is only of order `1/sqrt(log n)` after Hilbert normalization. It also does not give a lower bound for `beta_(n+1)(m)`, and no target-occupation statement follows.

## 6. Adversarial checks and prior-art audit

The proof was checked against the two parity-sensitive failure points.

First, for odd `q` the product in (17) is **not** `n`-periodic, so importing the `NB-324` tail argument unchanged would be invalid. Equation (19) records the exact flip, and (20)--(22) close it only after `2n`.

Second, the tail estimate does not assume pointwise cancellation. It uses only the exact selected-cell mean (27), the uniform bound (28), the duty-one-half selector, and the exact zero mean over the doubled period. Thus the `O(1/(nq))` bound is denominator-uniform and does not hide a factor of `q`.

Finite direct summation of the piecewise-constant pulse formula was used only as a sign and normalization check before the proof: odd denominators approach the same `log 2/4` scaled coefficient as the even family. No numerical observation is used as evidence.

A fresh prior-art search on 2026-09-24 checked the classical Nyman--Beurling/Báez-Duarte Hilbert-space literature, generalized Gram-structure work of Alouges--Darses--Hillion, and recent multiplicative-ladder Gram analysis by Carvill. Those sources provide neighboring fractional-part, dilation, and Gram machinery, but the reviewed material did not expose this finite-section odd-divisor two-period folding statement or the parity-complete rank-one-mixing obstruction. This is an audit result, not a claim of bibliographic novelty.

No external theorem is load-bearing here: the argument uses the exact reciprocal-shell identities already established inside the line plus elementary periodic integration. `SOURCES.md` therefore needs no new dependency.
