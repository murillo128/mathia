# NB-323 — Maximal-denominator folding carries logarithmic mixing resonance to linear scale

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-316, NB-320, NB-321, NB-322
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + LINEAR-SCALE-RESONANCE + MAXIMAL-RATIONAL-DENOMINATOR + ADJACENT-WITNESS + RANK-ONE-ERROR + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let `R_n` be the rank-one comparison operator of `NB-314`. For the scaled adjacent cancellation

\[
u_n:=g_n-\frac{n-1}{n}g_{n-1},
\tag{1}
\]

write `widetilde F_n` for its centered reciprocal profile. For every even integer `n>=4`, take the maximal-denominator rational folding scale

\[
\boxed{
m_n:=n-1=\frac{n(n-1)}{n}.
}
\tag{2}
\]

Thus (2) is the `q=n` endpoint of the rational family `m=P_n/q` from `NB-321`--`NB-322`, and it lies at linear rather than quadratic reciprocal scale.

Define the actual rank-one-subtracted weighted coefficient

\[
\mathcal E_n
:=
\left\langle
(\sqrt{n-1}\,T_{n,n-1}-R_n)g_2,u_n
\right\rangle.
\tag{3}
\]

Then

\[
\boxed{
\mathcal E_n
=
\frac{H_n-H_{n/2}}{4n}+\mathcal T_n,
\qquad
|\mathcal T_n|\le \frac1{n^2}.
}
\tag{4}
\]

Consequently

\[
\boxed{
\mathcal E_n
=
\frac{\log 2}{4n}+O(n^{-2}),
\qquad
n\mathcal E_n\longrightarrow\frac{\log 2}{4}.
}
\tag{5}
\]

Using the adjacent-witness norm bounds already established in `NB-304`/`NB-320`,

\[
\frac{H_{\lfloor n/2\rfloor}-1}{4n^2}
\le
\|u_n\|_2^2
\le
\frac{2H_{n-2}+1+\pi^2/18}{n^2},
\tag{6}
\]

and `||g_2||_2^2=log 2/4`, equation (5) gives

\[
\boxed{
\frac{|\mathcal E_n|}
{\|g_2\|_2\,\|u_n\|_2}
=
\Theta\!\left(\frac1{\sqrt{\log n}}\right).
}
\tag{7}
\]

In particular,

\[
\boxed{
\liminf_{\substack{n\to\infty\\ n\ \mathrm{even}}}
\sqrt{\log n}\,
\|\sqrt{n-1}\,T_{n,n-1}-R_n\|
\ge
\frac{\sqrt{\log 2}}{2\sqrt2}>0.
}
\tag{8}
\]

Thus the logarithmic adjacent resonance found at quadratic rational scales in `NB-320`--`NB-322` survives all the way to the linear-edge scale `m=n-1` along the maximal denominator `q=n`. The `q=o(sqrt n)` range in `NB-322` is therefore not a genuine resonance cutoff for this adjacent channel; it is a limitation of the absolute second-primitive remainder estimate used there.

This does **not** prove a uniform statement for all intermediate denominators `sqrt n << q << n`, and it does not make the comparison operator `R_n` a valid operator-norm asymptotic at linear scale. It proves one explicit weighted matrix coefficient only.

## 1. The endpoint `q=n` turns the adjacent profile into an elementary pulse train

`NB-314` gives, for every integer dilation `m` and `u,v in U_n`, the exact identity

\[
\left\langle
(\sqrt m\,T_{n,m}-R_n)v,u
\right\rangle
=
\int_1^\infty
F_v(t)\widetilde F_u(mt)\,\frac{dt}{t^2}.
\tag{9}
\]

For (1), the cancellation of the `{t}` terms gives

\[
F_{u_n}(s)
=
\left\{\frac{s}{n}\right\}
-
\frac{n-1}{n}
\left\{\frac{s}{n-1}\right\},
\tag{10}
\]

and `NB-316` gives its reciprocal mean `1/(2n)`. With the periodic first Bernoulli function

\[
B_1(x):=\{x\}-\frac12
\]

away from its jump points, the centered profile is therefore

\[
\widetilde F_n(s)
=
B_1(s/n)
-
\frac{n-1}{n}B_1(s/(n-1)).
\tag{11}
\]

At `m=n-1`, put

\[
f_n(t):=\widetilde F_n((n-1)t).
\tag{12}
\]

For `t=k+r`, `0<=r<1`, and `0<=k<=n-1`, equation (11) becomes

\[
f_n(k+r)
=
\mathbf 1_{\{0\le r<k/(n-1)\}}
-
\frac{k+1/2}{n}.
\tag{13}
\]

Indeed

\[
\frac{n-1}{n}(k+r)
=
k+\frac{(n-1)r-k}{n},
\]

and the final fraction lies in `(-1,1)`; its only wrap occurs when `(n-1)r-k<0`, exactly the threshold in (13).

For `g_2`,

\[
F_{g_2}(t)
=
\begin{cases}
0,&t\in[2\ell,2\ell+1),\\[1mm]
1/2,&t\in[2\ell+1,2\ell+2).
\end{cases}
\tag{14}
\]

Since `f_n` has period `n` and `n` is even, the product

\[
h_n(t):=F_{g_2}(t)f_n(t)
\tag{15}
\]

is `n`-periodic. Also `h_n=0` on `[0,1)`, so (9) can be written without a singular lower endpoint as

\[
\mathcal E_n
=
\int_0^\infty h_n(t)\,\frac{dt}{t^2}.
\tag{16}
\]

## 2. The first period is an exact alternating harmonic sum

Fix an odd cell `k<=t<k+1`, with `1<=k<=n-1`, and set

\[
\lambda_k:=\frac{k}{n-1},
\qquad
c_k:=\frac{k+1/2}{n}.
\tag{17}
\]

Equations (13)--(15) give

\[
h_n(t)
=
\frac12
\begin{cases}
1-c_k,&k\le t<k+\lambda_k,\\[1mm]
-c_k,&k+\lambda_k\le t<k+1.
\end{cases}
\tag{18}
\]

Hence the contribution of this odd cell to the first-period weighted integral is

\[
\begin{aligned}
\int_k^{k+1}\frac{h_n(t)}{t^2}\,dt
&=
\frac12\left[
\int_k^{k+\lambda_k}\frac{dt}{t^2}
-c_k\int_k^{k+1}\frac{dt}{t^2}
\right]\\[1mm]
&=
\frac12\left[
\frac1{kn}
-
\frac{k+1/2}{n\,k(k+1)}
\right]\\[1mm]
&=
\boxed{\frac1{4n\,k(k+1)}}.
\end{aligned}
\tag{19}
\]

The simplification uses

\[
k+\lambda_k=\frac{kn}{n-1}.
\]

Summing (19) over the odd integers `1,3,...,n-1`,

\[
\begin{aligned}
I_{n,0}
&:=
\int_0^n h_n(t)\frac{dt}{t^2}\\
&=
\frac1{4n}
\sum_{j=1}^{n/2}
\left(\frac1{2j-1}-\frac1{2j}\right)\\
&=
\boxed{
\frac{H_n-H_{n/2}}{4n}.
}
\end{aligned}
\tag{20}
\]

Thus the leading coefficient is not produced by a primitive supremum or an absolute-value estimate. It is the exact first-period mass of a pulse train whose pulse width and negative pedestal cancel down to a single alternating-harmonic increment on every odd cell.

## 3. All later periods contribute only `O(n^-2)`

It remains to bound

\[
\mathcal T_n
:=
\int_n^\infty h_n(t)\frac{dt}{t^2}.
\tag{21}
\]

The unweighted integral of (18) over an odd cell is

\[
a_k
:=
\int_k^{k+1}h_n(t)\,dt
=
\frac{2k-(n-1)}{4n(n-1)}.
\tag{22}
\]

Summing over all odd cells in one period gives

\[
M_n
:=
\int_0^n h_n(t)\,dt
=
\boxed{\frac1{8(n-1)}}.
\tag{23}
\]

Put

\[
\bar h_n:=\frac{M_n}{n},
\qquad
h_n^0:=h_n-\bar h_n.
\tag{24}
\]

Then `h_n^0` is `n`-periodic with zero mean. Its periodic primitive

\[
H_n^0(t):=\int_0^t h_n^0(s)\,ds
\tag{25}
\]

is uniformly bounded independently of `n`. A crude explicit bound is enough. From (22),

\[
|a_k|\le\frac1{4n},
\]

so the cumulative contribution of all completed odd cells before any point in a period is at most `1/8` in absolute value. Inside one cell, `|h_n|<=1/2`, adding at most `1/2`. Finally `M_n<=1/24` for `n>=4`. Therefore

\[
\boxed{
\|H_n^0\|_\infty\le\frac23.
}
\tag{26}
\]

The mean part of the tail is

\[
\int_n^\infty \bar h_n\frac{dt}{t^2}
=
\frac{M_n}{n^2},
\tag{27}
\]

while integration by parts for the zero-mean part, using `H_n^0(n)=0`, gives

\[
\left|
\int_n^\infty h_n^0(t)\frac{dt}{t^2}
\right|
=
\left|
2\int_n^\infty H_n^0(t)\frac{dt}{t^3}
\right|
\le
\frac{2}{3n^2}.
\tag{28}
\]

Since `M_n<=1/24`, equations (27)--(28) yield

\[
\boxed{
|\mathcal T_n|
\le
\frac{17}{24n^2}
<
\frac1{n^2}.
}
\tag{29}
\]

Combining (20) and (29) proves (4). Since

\[
H_n-H_{n/2}
=\log2+O(n^{-1}),
\tag{30}
\]

(5) follows.

## 4. The normalized resonance persists at the linear edge

Equations (5)--(6) imply

\[
\|u_n\|_2
=\Theta\!\left(\frac{\sqrt{\log n}}{n}\right),
\tag{31}
\]

while `||g_2||_2=sqrt(log 2)/2`. Therefore the normalized matrix coefficient has precisely logarithmic scale, proving (7).

For the explicit operator lower constant, use the upper norm bound in (6):

\[
\begin{aligned}
\|\sqrt{n-1}T_{n,n-1}-R_n\|
&\ge
\frac{|\mathcal E_n|}
{\|g_2\|_2\,\|u_n\|_2}\\[1mm]
&\ge
\frac{\sqrt{\log2}}
{2\sqrt{2H_{n-2}+1+\pi^2/18}}
+o((\log n)^{-1/2}).
\end{aligned}
\tag{32}
\]

As `H_(n-2)~log n`, equation (8) follows.

The location of this resonance is the main structural point. `NB-322` proved non-cancellation for growing rational denominators only under `q=o(sqrt n)`, corresponding to scales strictly above `n^(3/2+o(1))`. Here `q=n`, maximally outside that range, yet the same adjacent witness still leaves a `1/sqrt(log n)` normalized rank-one residue at

\[
m_n=n-1\asymp n.
\tag{33}
\]

Therefore the `q^2/n^2` absolute remainder from the second-primitive estimate in `NB-322` cannot describe the actual endpoint behavior of the weighted coefficient. Large cancellation survives after the denominator crosses `sqrt n`.

This result does not show monotonic persistence in `q`. There may still be intermediate denominator ranges with different behavior. What it rules out is interpreting `q~sqrt n` as an intrinsic transition of the adjacent rational-folding channel solely on the basis of the current remainder estimate.

## 5. Adversarial checks and prior-art audit

The centering in (11) is exactly the reciprocal mean used by `NB-314`--`NB-322`: `mu(u_n)=1/(2n)`. Formula (13) was derived before any estimate, and its threshold remains valid at the endpoint cell `k=n-1`, where `k/(n-1)=1`. The parity restriction is deliberate: when `n` is even, the period `n` of `f_n` is simultaneously a period of `F_(g_2)`, so no extra `2n` bookkeeping is hidden in (16). The tail estimate uses only periodicity, the exact one-period mean, and a bounded zero-mean primitive; it does not assume that the far-external rank-one theorem is already uniform at `m~n`.

The result is also compatible with the earlier source geometry. `NB-306` places `m=n-1` beyond the exact isometric core, while `NB-312`--`NB-313` already show that projected-dilation overlap cannot collapse on bounded linear scales. The present statement is different: it concerns the rank-one-subtracted, `sqrt(m)`-rescaled weighted mixing coefficient and shows that its convergence is only logarithmic along one explicit linear sequence.

A fresh prior-art audit checked the classical multiplicative fractional-part autocorrelation of Báez-Duarte, Balazard, Landreau and Saias (Ramanujan J. 9 (2005), arXiv:math/0306251), Balazard--Martin's Wilton/continued-fraction analysis of that autocorrelation (arXiv:1305.4395), and Ehm's Nyman--Beurling Gram-kernel representations and reciprocity formulae (arXiv:2405.06349). Those works are the correct boundary for raw rational fractional-part correlations and their local arithmetic regularity. The material reviewed did not expose the specific finite-section object in (3), the maximal-denominator pulse identity (13), or the first-period formula (20). This is recorded only as a prior-art boundary, not as a claim of bibliographic novelty. No external theorem is load-bearing for (4)--(8), so no new durable source dependency is added to `SOURCES.md`.

## Classification and next discriminator

This is a rigorous positive structural finding and a method correction. It shows that the apparent `q~sqrt n` boundary of the current `NB-322` remainder is not the endpoint of the adjacent resonance: a logarithmic weighted residue persists at the maximal denominator `q=n` and linear dilation `m=n-1`.

The next useful discriminator is now two-parameter rather than one-sided. Write `n=aq` on the `q|n` subsequences. The cases already controlled correspond to `a->infinity` with `q=o(sqrt n)` and the new endpoint `a=1`. A direct cellwise or summation-by-parts analysis that keeps both `a` and `q` visible should determine whether the logarithmic resonance persists uniformly for fixed `a`, for `a` growing slowly, or across the full corridor `1<=q<=n`. That would distinguish a genuinely broad rational skeleton from separated resonant islands without returning to the lossy second-primitive supremum.

As throughout `NB-303`--`NB-322`, this remains source-side. It does not establish occupation by the first-free Ford datum, a finite-section excess bound, a Nyman approximation rate, or any implication for RH.