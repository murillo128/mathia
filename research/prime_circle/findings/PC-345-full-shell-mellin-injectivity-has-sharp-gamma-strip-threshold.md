# PC-345 — full-shell Mellin injectivity has a sharp Gamma-strip threshold

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the first natural exponential-growth escape beyond the tempered full-shell theorem PC-344.

PC-344 proves that the complete scalar Prime-Circle shell family has no hidden tempered null directions on a zero-free vertical line: after the exact universal zeta factor is exposed, every tempered null selector is supported on zeta zeros. That leaves a precise boundary question. The Gamma factor supplies the intrinsic vertical envelope `exp(-pi|t|/2)`, while objects beyond the tempered dual can compensate part of that decay. Is the full-shell uniqueness theorem robust to a fixed exponential loss of the Gamma envelope, or is the critical half-width `pi/2` exact?

For a natural residual weighted-`L^2` class the threshold is **sharp**. On any zero-free line `sigma>1`, full-shell response is injective when the residual transform retains the whole Gamma strip of half-width `pi/2`, but **every strict loss of strip width creates an infinite-dimensional nullspace even though zeta has no zeros there**.

Thus the first exponential-growth escape beyond PC-344 does exist, but it is pure Hardy/Blaschke interpolation freedom rather than new arithmetic or zeta-zero information.

## 1. Exact shell reduction for the residual transform

Fix

\[
\sigma>1,\qquad \beta:=1-\sigma<0,
\tag{1}
\]

and retain the exact signed-radial Mellin factorization from PC-179,

\[
\mathcal R_n(\sigma+it)
=U_\sigma(t)A_n(t),
\qquad
U_\sigma(t):=-\Gamma(\sigma+it)\zeta(\sigma+it),
\tag{2}
\]

where

\[
A_n(t)
=\sum_{d\mid n}\mu(n/d)d^{\beta-it}.
\tag{3}
\]

Because `sigma>1`, both `zeta(sigma+it)` and its reciprocal are bounded on the real `t` axis, Gamma has no zeros, and hence

\[
U_\sigma(t)\ne0\qquad(t\in\mathbb R).
\tag{4}
\]

For `b>0`, define the residual exponential-envelope class

\[
\mathcal X_{\sigma,b}
:=\left\{T:\ S(t):=U_\sigma(t)T(t),\quad
 e^{b|t|}S(t)\in L^2(\mathbb R)\right\},
\tag{5}
\]

where `T` is an ordinary measurable function modulo almost-everywhere equality. This is deliberately a class **after multiplication by the source-forced universal shell factor** `U_sigma`; it is a boundary classification, not a proposal for a new normalized observable.

Since `b>0`, Cauchy--Schwarz gives `S in L^1(R)`. Therefore every shell response is absolutely defined by

\[
L_T(n)
:=\int_{\mathbb R}T(t)\mathcal R_n(\sigma+it)\,dt
=\int_{\mathbb R}S(t)A_n(t)\,dt.
\tag{6}
\]

Use the Fourier convention

\[
f(x):=\widehat S(x)
=\int_{\mathbb R}S(t)e^{-itx}\,dt.
\tag{7}
\]

Then

\[
L_T(n)
=\sum_{d\mid n}\mu(n/d)d^\beta f(\log d).
\tag{8}
\]

Set

\[
g(d):=d^\beta f(\log d).
\tag{9}
\]

Equation (8) is simply

\[
L_T=\mu*g
\tag{10}
\]

on the divisor semigroup. If `L_T(n)=0` for every `n>1`, then

\[
\mu*g=c\varepsilon,
\qquad c=g(1)=f(0),
\tag{11}
\]

where `epsilon` is the identity for Dirichlet convolution. Convolving with the constant-one arithmetic function and using `1*mu=epsilon` gives

\[
g(d)=c\qquad(d\ge1),
\tag{12}
\]

hence

\[
f(\log d)=c\,d^{-\beta}=c\,d^{\sigma-1}.
\tag{13}
\]

But `S in L^1`, so the Riemann--Lebesgue lemma gives `f(x)->0` as `x->+infinity`. Since `sigma>1`, equation (13) is possible only for `c=0`. Therefore

\[
\boxed{
L_T(n)=0\ \forall n>1
\iff
f(\log m)=0\ \forall m\ge1.
}
\tag{14}
\]

This all-integer logarithmic zero set is exactly the full-shell information isolated in PC-343 and PC-344, now without assuming that `T` itself is tempered.

## 2. The residual envelope is exactly a Hardy strip

For `z=x+iy` with `|y|<b`, equation (7) continues holomorphically as

\[
f(z)=\int_{\mathbb R}S(t)e^{-itz}\,dt.
\tag{15}
\]

Plancherel gives

\[
\int_{\mathbb R}|f(x+iy)|^2\,dx
=2\pi\int_{\mathbb R}|S(t)|^2e^{2ty}\,dt.
\tag{16}
\]

Consequently

\[
e^{b|t|}S(t)\in L^2(\mathbb R)
\iff
f\in H^2(S_b),
\qquad
S_b:=\{z:|\operatorname{Im}z|<b\},
\tag{17}
\]

with equivalent norms. Thus full-shell null selectors in `X_{sigma,b}` are exactly Hardy-strip functions whose zero set contains

\[
\{\log m:m=1,2,3,\ldots\}.
\tag{18}
\]

Map `S_b` conformally to the unit disk by

\[
w=\phi_b(z)
:=\tanh\!\left(\frac{\pi z}{4b}\right).
\tag{19}
\]

The integer-log points become

\[
w_m
=\phi_b(\log m)
=\frac{m^\alpha-1}{m^\alpha+1},
\qquad
\alpha:=\frac{\pi}{2b},
\tag{20}
\]

so

\[
1-w_m=\frac{2}{m^\alpha+1}.
\tag{21}
\]

This single exponent `alpha=pi/(2b)` controls the whole boundary.

## 3. At the full Gamma width the shell map is injective

A nonzero Hardy-space function on the disk can have zeros `{w_m}` only if the Blaschke condition holds,

\[
\sum_m(1-|w_m|)<\infty.
\tag{22}
\]

At the intrinsic Gamma half-width

\[
b=\frac\pi2,
\qquad \alpha=1,
\tag{23}
\]

equations (21)--(22) demand convergence of

\[
\sum_{m\ge1}\frac{2}{m+1},
\tag{24}
\]

which fails. Hence the only `H^2(S_{pi/2})` function vanishing at every integer logarithm is the zero function. Combining this with (14) and the nonvanishing of `U_sigma` gives

\[
\boxed{
\ker\left(T\mapsto(L_T(n))_{n>1}\right)
\cap\mathcal X_{\sigma,\pi/2}
=\{0\}.
}
\tag{25}
\]

The same conclusion holds for every `b>=pi/2`: either repeat the disk calculation, where `alpha<=1` still violates Blaschke, or use the inclusion `X_{sigma,b} subset X_{sigma,pi/2}`.

This recovers the expected side of PC-344. By Stirling,

\[
|U_\sigma(t)|
\asymp
(1+|t|)^{\sigma-1/2}e^{-\pi|t|/2}
\tag{26}
\]

up to bounded nonzero zeta factors on `sigma>1`. Retaining `b=pi/2` therefore leaves at most polynomial behavior after division by the universal Gamma envelope, exactly where tempered uniqueness should still dominate.

## 4. Every narrower strip has an infinite-dimensional full-shell nullspace

Now let

\[
0<b<\frac\pi2.
\tag{27}
\]

Then `alpha>1`, and (21) gives

\[
\sum_{m\ge1}(1-w_m)
=\sum_{m\ge1}\frac{2}{m^\alpha+1}
<\infty.
\tag{28}
\]

Thus `{w_m}` is a genuine Blaschke sequence. There is a nonzero bounded analytic Blaschke product `B_b` on `S_b` whose zeros contain every `log m`.

Choose any `R>b` and put

\[
q_R(z):=\frac1{z^2+R^2}.
\tag{29}
\]

Its poles lie outside the closed strip and

\[
q_R\in H^2(S_b).
\tag{30}
\]

Therefore

\[
f_b(z):=B_b(z)q_R(z)
\tag{31}
\]

is a nonzero member of `H^2(S_b)` satisfying

\[
f_b(\log m)=0\qquad(m\ge1).
\tag{32}
\]

By (17), `f_b` is the Fourier transform of a nonzero `S_b(t)` with

\[
e^{b|t|}S_b(t)\in L^2(\mathbb R).
\tag{33}
\]

Since `U_sigma` has no real zeros, define

\[
T_b(t):=\frac{S_b(t)}{U_\sigma(t)}.
\tag{34}
\]

Then `T_b in X_{sigma,b}`, `T_b!=0`, and equations (14) and (32) give

\[
\boxed{
L_{T_b}(n)=0\qquad\forall n>1.
}
\tag{35}
\]

The kernel is not merely nontrivial. For distinct real numbers `a_j`, the functions

\[
f_{b,a_j}(z):=e^{-ia_jz}f_b(z)
\tag{36}
\]

remain in `H^2(S_b)`, have the same required zero set, and are linearly independent. Hence

\[
\boxed{
\dim\ker\left(T\mapsto(L_T(n))_{n>1}\right)
\cap\mathcal X_{\sigma,b}
=\infty
\qquad(0<b<\pi/2).
}
\tag{37}
\]

Combining (25) and (37), the threshold is exact:

\[
\boxed{
\begin{array}{ll}
b\ge\pi/2:&\text{full-shell injectivity},\\[2mm]
0<b<\pi/2:&\text{infinite-dimensional full-shell kernel}.
\end{array}}
\tag{38}
\]

## 5. These nulls are interpolation ghosts, not zeta data

The choice `sigma>1` is the decisive control. Zeta has no zeros on this half-plane, so none of the null directions constructed in (31)--(37) can be supported by, or attributed to, zeta zeros. They arise solely because a narrower Hardy strip makes the logarithmic sampling set Blaschke-admissible.

Equation (26) also identifies what crossing the threshold means for the original selector. If `b=pi/2-delta`, the residual condition permits division by Gamma to restore roughly

\[
e^{\delta|t|}
\tag{39}
\]

of exponential growth, modulo powers of `|t|`. PC-344 excludes every nonzero **tempered** full-shell null on `sigma>1`; therefore each nonzero example above necessarily lives genuinely beyond the tempered class. An arbitrarily small but fixed exponential allowance is already enough to manufacture invisible selectors.

This is why (38) is a no-go boundary rather than a positive RH mechanism. The nullspace says nothing about the location of zeta zeros: it already exists where there are no zeros at all.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Hardy-space zero sets are governed by the Blaschke condition; bilateral Fourier/Laplace transforms with exponential `L^2` weights give Hardy spaces on strips via Paley--Wiener theory. A directed search located the expected general strip-transform literature, including Zen Harper, *Laplace transform representations and Paley-Wiener theorems for functions on vertical strips*, Documenta Mathematica 15 (2010), 235--254, DOI `10.4171/DM/296`, together with standard Hardy/Blaschke zero-set theory. Recent work on Laplace-transform nonuniqueness under weakened growth hypotheses likewise treats general analytic-transform "ghosts", not this arithmetic shell family.

Searches targeted at logarithms of all integers as a Hardy-strip zero set, Blaschke interpolation at `{log n}`, Gamma-weighted Mellin null selectors, and the Prime-Circle divisor shell factorization found no source supplying an independent RH or spectral mechanism equivalent to (38). No historical novelty is claimed for Paley--Wiener, Blaschke products, or the convergence test `sum m^{-alpha}`.

The line-local exact delta is the combination of two structures already forced internally: the complete Prime-Circle shell family converts by divisor inversion to samples at **every integer logarithm**, while the universal Gamma factor singles out the half-width `pi/2`. Their combination makes the boundary sharp and constructive: at the critical width the sample set is a uniqueness set; at every smaller width the same set is a Blaschke sequence with an infinite-dimensional annihilator.

No new `SOURCES.md` entry is required for the derivation. The load-bearing external machinery is standard Hardy/Paley--Wiener/Blaschke theory already neighboring PC-339--PC-344; Harper is recorded here only as a direct strip-transform prior-art anchor.

## 7. Consequence for the Prime-Circle frontier

PC-344 left open selector spaces larger than tempered distributions because its proof could not control essential/exponential boundary growth. Equation (38) shows that this was a **real mathematical boundary**, not merely a weakness of that proof. The first natural fixed-exponential enlargement already contains many exact full-shell null selectors.

It also means that allowing progressively larger scalar Mellin selector classes cannot be used safely as a route toward a zero-sensitive Prime-Circle criterion. Once the source-forced Gamma strip is narrowed at all, exact non-zeta interpolation ghosts appear on the completely zero-free half-plane `sigma>1`. Any future scalar construction in this direction would need an additional intrinsic condition that eliminates these Hardy/Blaschke degrees of freedom without simply imposing the answer by normalization.

The result does not touch shell-dependent operators, nonlinear observables, matrix-valued/noncommuting carriers, or genuinely cross-shell/cross-level geometric constructions before scalar Mellin evaluation. Those remain outside this threshold theorem.

## Audit / falsification tests

A counterexample to the sharp classification is either (i) a nonzero `T in X_{sigma,pi/2}` on some `sigma>1` annihilating every shell, or (ii) a strict subcritical width `0<b<pi/2` for which no nonzero all-shell null exists.

The load-bearing checkpoints are:

1. divisor convolution in (8)--(13) must force `f(log m)=0` for **all** integers `m>=1`, with Riemann--Lebesgue eliminating the otherwise free `n=1` constant;
2. the weighted-`L^2` condition in (5) must be equivalent to `H^2` control on the strip `|Im z|<b` through (16)--(17);
3. the strip-to-disk map must produce exactly `1-w_m=2/(m^alpha+1)` with `alpha=pi/(2b)`;
4. the Blaschke sum must diverge at and above `b=pi/2` and converge at every strict subcritical width;
5. the subcritical Blaschke product times `q_R` must lie in `H^2(S_b)`, so inverse Paley--Wiener produces a genuine residual function satisfying (33);
6. `U_sigma` must be nonzero on the chosen control line `sigma>1`, making division in (34) legitimate and ensuring the constructed kernel cannot be inherited from zeta zeros.

Failure of any one of these checkpoints would destroy the claimed sharp threshold. Within the stated residual envelope class, all six are exact.