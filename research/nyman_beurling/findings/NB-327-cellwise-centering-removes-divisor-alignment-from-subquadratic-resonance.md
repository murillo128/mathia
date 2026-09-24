# NB-327 — Cellwise centering removes divisor alignment from subquadratic resonance

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-323, NB-324, NB-325
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + NONDIVISOR-ALIGNMENT + INTEGER-MULTIPLE-RAYS + LINEAR-TO-SUBQUADRATIC-RESONANCE + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

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

For arbitrary integers

\[
n\ge3,
\qquad
d\ge1,
\qquad
m_{n,d}:=d(n-1),
\tag{2}
\]

define

\[
\mathcal E_{n,d}
:=
\left\langle
(\sqrt{m_{n,d}}T_{n,m_{n,d}}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

No divisibility relation between `d` and `n` is assumed. Then

\[
\boxed{
\left|
\mathcal E_{n,d}-\frac{\log2}{4n}
\right|
\le
\frac{2d}{n^2}.
}
\tag{4}
\]

Consequently, for every integer sequence `d_n` satisfying

\[
\frac{d_n}{n}\longrightarrow0,
\tag{5}
\]

one has

\[
\boxed{
n\mathcal E_{n,d_n}\longrightarrow\frac{\log2}{4}.
}
\tag{6}
\]

Using `||g_2||_2^2=\log2/4` and the adjacent-witness bound from `NB-304`,

\[
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{7}
\]

this gives the same logarithmic obstruction previously obtained only on exact-divisor folds:

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_{n,d_n}}T_{n,m_{n,d_n}}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2}>0.
}
\tag{8}
\]

Thus exact divisor alignment is not the mechanism sustaining the adjacent rank-one-error resonance below quadratic scale. For every fixed `1<=alpha<2`, taking

\[
d_n=\max\{1,\lfloor n^{\alpha-1}\rfloor\}
\tag{9}
\]

gives, along **all sufficiently large integers `n`** rather than an arithmetic subsequence,

\[
m_{n,d_n}=n^{\alpha+o(1)}
\tag{10}
\]

and the lower bound (8) persists. More generally, `d_n=o(n)` allows these resonant integer-multiple rays to approach the quadratic scale by any diverging factor, for example `d_n=\lfloor n/L_n\rfloor` with `L_n->infinity` and `L_n=o(n)`.

The statement remains source-side. It is one explicit matrix coefficient of the rank-one-subtracted rescaled projected-dilation operator. It does not prove a uniform obstruction for arbitrary integers `m`, target occupation by the first-free Ford datum, finite-section excess, a Nyman approximation rate, or RH.

## 1. The nondivisor problem on integer-multiple rays

`NB-324` and `NB-325` considered

\[
m=\frac{n(n-1)}q=d(n-1)
\]

under the exact-divisor relation `q|n`, equivalently `d=n/q` with `d|n`. That relation made the square-wave selector close after one or two `n`-periods and produced the exact harmonic main term.

For the present theorem keep the same integer-multiple scale

\[
m=d(n-1)
\tag{11}
\]

but allow arbitrary integer `d`, including `d\nmid n`. The global product need no longer close after one or two periods. The key observation is that global closure is unnecessary: the first `n` cells already contain the complete harmonic main term up to `O(d/n^2)`, while every later cell has an intrinsic mean of only `O(1/n)`. Centering **inside each cell** therefore controls the infinite weighted tail without any divisor alignment.

By the exact rank-one-error identity from `NB-314`,

\[
\mathcal E_{n,d}
=
\int_0^\infty
F_{g_2}(t)\widetilde F_n(d(n-1)t)
\frac{dt}{t^2},
\tag{12}
\]

where `widetilde F_n` is the centered reciprocal profile of `u_n`. Put

\[
f_n(y):=\widetilde F_n((n-1)y).
\tag{13}
\]

The pulse formula isolated in `NB-323` is algebraic and does not require the parity hypothesis used there for the later folding step: if

\[
y=k+r,
\qquad
0\le k\le n-1,
\qquad
0\le r<1,
\]

then

\[
\boxed{
f_n(k+r)
=
\mathbf1_{\{0\le r<k/(n-1)\}}
-\frac{k+1/2}{n},
}
\tag{14}
\]

and `f_n` extends `n`-periodically.

Changing variables `y=dt` in (12) gives

\[
\boxed{
\mathcal E_{n,d}
=d\int_0^\infty
s_d(y)f_n(y)\frac{dy}{y^2},
\qquad
s_d(y):=F_{g_2}(y/d).
}
\tag{15}
\]

Because `d` is an integer, `s_d` is constant on every unit cell and is the exact square wave

\[
s_d(y)=
\begin{cases}
0,&y\in[2jd,(2j+1)d),\\[1mm]
1/2,&y\in[(2j+1)d,(2j+2)d),
\end{cases}
\qquad j\ge0.
\tag{16}
\]

This cell alignment survives even when `d` does not divide `n`.

## 2. The first `n` cells already give `log 2/(4n)`

Fix a selected cell `[k,k+1)` with `1<=k<=n-1`. Put

\[
\lambda_k:=\frac{k}{n-1},
\qquad
c_k:=\frac{k+1/2}{n}.
\]

Using (14) and `s_d=1/2`, its weighted contribution before the outer factor `d` is

\[
\begin{aligned}
\int_k^{k+1}
\frac{s_d(y)f_n(y)}{y^2}\,dy
&=
\frac12\left[
\int_k^{k+\lambda_k}\frac{dy}{y^2}
-c_k\int_k^{k+1}\frac{dy}{y^2}
\right]\\[1mm]
&=
\frac12\left[
\frac1{kn}
-\frac{k+1/2}{n\,k(k+1)}
\right]\\[1mm]
&=
\boxed{\frac1{4n\,k(k+1)}}.
\end{aligned}
\tag{17}
\]

Therefore the contribution from the first profile period is

\[
I_{n,d}^{(0)}
=
\frac{d}{4n}
\sum_{\substack{1\le k<n\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}.
\tag{18}
\]

The corresponding infinite selected-cell sum is exactly elementary. Each selected `d`-block telescopes:

\[
\sum_{k=(2j+1)d}^{(2j+2)d-1}
\frac1{k(k+1)}
=
\frac1{(2j+1)d}-\frac1{(2j+2)d}.
\tag{19}
\]

Hence

\[
\boxed{
d
\sum_{\substack{k\ge1\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
=
\sum_{j\ge0}
\left(\frac1{2j+1}-\frac1{2j+2}\right)
=
\log2.
}
\tag{20}
\]

The omitted selected terms all have `k>=n`, so

\[
0\le
\frac{\log2}{d}
-
\sum_{\substack{1\le k<n\\ \lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
\le
\sum_{k=n}^\infty\frac1{k(k+1)}
=
\frac1n.
\tag{21}
\]

Multiplying by `d/(4n)` yields the finite estimate

\[
\boxed{
\left|
I_{n,d}^{(0)}-\frac{\log2}{4n}
\right|
\le
\frac{d}{4n^2}.
}
\tag{22}
\]

No period matching between `n` and `2d` has entered.

## 3. Cellwise centering makes the entire later tail `O(d/n^2)`

It remains to control

\[
\mathcal T_{n,d}
:=
d\int_n^\infty
s_d(y)f_n(y)\frac{dy}{y^2}.
\tag{23}
\]

For a global cell `[K,K+1)`, `K>=n`, write

\[
k:=K\bmod n.
\]

By periodicity and (14), the unweighted cell mean is

\[
\begin{aligned}
a_k
&:=
\int_0^1 f_n(k+r)\,dr\\
&=
\frac{k}{n-1}-\frac{k+1/2}{n}\\
&=
\boxed{\frac{2k-(n-1)}{2n(n-1)}}.
\end{aligned}
\tag{24}
\]

In particular,

\[
\boxed{|a_k|\le\frac1{2n}}.
\tag{25}
\]

Put

\[
h_k(r):=f_n(k+r)-a_k.
\]

Then `int_0^1 h_k(r)dr=0`. Also `|f_n|<=1` and, for `n>=3`, `|h_k|<=3/2`. Hence, with `w_K(r)=(K+r)^{-2}`,

\[
\begin{aligned}
\left|
\int_0^1 h_k(r)w_K(r)\,dr
\right|
&=
\left|
\int_0^1 h_k(r)(w_K(r)-w_K(0))\,dr
\right|\\
&\le
\frac{3}{K^3},
\end{aligned}
\tag{26}
\]

because `|w_K(r)-w_K(0)|<=2/K^3`. The mean part satisfies

\[
\left|
a_k\int_0^1w_K(r)\,dr
\right|
\le
\frac1{2nK(K+1)}.
\tag{27}
\]

The selector is constant on the cell and has magnitude at most `1/2`. Therefore

\[
|\mathcal T_{n,d}|
\le
\frac d2
\sum_{K=n}^\infty
\left(
\frac3{K^3}
+
\frac1{2nK(K+1)}
\right).
\tag{28}
\]

For `n>=2`,

\[
\sum_{K=n}^\infty\frac1{K^3}
\le
\frac1{n^2},
\qquad
\sum_{K=n}^\infty\frac1{K(K+1)}
=
\frac1n.
\tag{29}
\]

Thus

\[
\boxed{
|\mathcal T_{n,d}|
\le
\frac{7d}{4n^2}.
}
\tag{30}
\]

Combining (22) and (30) proves (4).

The important point is methodological: the tail estimate uses only the `O(1/n)` **cell mean** in (25) plus zero-mean cancellation against the slowly varying weight `1/y^2`. It does not ask the product `s_df_n` to have zero mean over an exact common period. The divisor conditions in `NB-324`--`NB-325` were therefore sufficient for global folding, not necessary for the resonance itself on the integer-multiple rays (11).

## 4. Consequences across the moving subquadratic window

If `d_n=o(n)`, equation (4) immediately gives (6). Since

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2
\]

and (7) implies

\[
\|u_n\|_2
\le
\frac{\sqrt{2\log n+O(1)}}{n},
\]

we obtain

\[
\begin{aligned}
\|\sqrt{m_{n,d_n}}T_{n,m_{n,d_n}}-R_n\|
&\ge
\frac{|\mathcal E_{n,d_n}|}
{\|g_2\|_2\|u_n\|_2}\\
&\ge
\frac{\sqrt{\log2}+o(1)}{2\sqrt{2\log n}},
\end{aligned}
\tag{31}
\]

which is (8).

This removes two restrictions from the exact-divisor results simultaneously on this lattice of dilation scales. First, there is no parity condition. Second, there is no relation `d|n`, so `q=n/d` need not even be an integer. The resonance therefore persists on nondivisor examples at every subquadratic power scale without passing to specially chosen arithmetic subsequences.

It does **not** yet settle arbitrary off-lattice dilations. The present proof uses that `m/(n-1)=d` is an integer so that the `g_2` selector in (16) is constant on the unit cells of the adjacent pulse train. The next genuinely different arithmetic problem is therefore to understand

\[
m=d(n-1)+r,
\qquad r\ne0,
\tag{32}
\]

where the selector boundaries drift through those cells. A uniform mixing theorem, if one exists below quadratic scale, must exploit that off-lattice drift or a different source/target mechanism; exact-divisor arithmetic alone can no longer be its discriminator.

## 5. Adversarial checks and prior-art boundary

The proof was stress-tested at the points where the earlier divisor arguments were most fragile.

- The pulse formula (14) is used only as an algebraic identity for the centered adjacent profile; the evenness assumption in `NB-323` belonged to the selector-period closure, not to that formula.
- The singular endpoint at `y=0` causes no issue: `s_d(y)=0` throughout `[0,d)`, and every selected first-period cell has `k>=d>=1`.
- The tail proof never assumes that `s_df_n` is periodic with period `n`, `2n`, or any bounded multiple of `n`. It works cell by cell and is therefore valid when `d\nmid n`.
- Equation (4) is a finite estimate, so the moving conclusion (6) does not interchange the fixed-`n` and far-external limits from `NB-314`.
- The normalization in (8) uses an upper bound on the physical norm of the explicit adjacent witness, which is the correct direction for a lower bound on operator norm.

A fresh prior-art audit checked the classical/discrete Nyman--Beurling boundary of Báez-Duarte, the multiplicative fractional-part autocorrelation work of Balazard--Martin, and the recent Gram-geometry work of Carvill. These sources concern the criterion, fractional-part autocorrelation, and Gram decay respectively; none of the inspected statements supplies the finite-section rank-one-subtracted coefficient (3), the nondivisor estimate (4), or the cellwise-centering argument above. This is an audit boundary, not a claim of bibliographic novelty. No external theorem is load-bearing in the proof, so `SOURCES.md` requires no change.

## Research consequence

`NB-324`--`NB-325` left open the possibility that the logarithmic obstruction was tied to the exact-divisor skeleton. Equation (4) rules out that interpretation on the entire integer-multiple family `m=d(n-1)` as long as `d=o(n)`. The surviving source-side question is narrower: **does genuine off-lattice drift `m-d(n-1)` destroy the adjacent resonance, and on what scale?**

That question remains separate from target occupation. Even if the source-side rank-one mixing transition were fully classified, a useful Nyman gain would still require the actual moving first-free datum to occupy the relevant singular directions after the sampling/null decomposition, lower-section conditioning, and off-critical contraction.
