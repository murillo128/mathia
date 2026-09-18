# RE-210 — Exact sinc-tail geometry sharpens the separated vertical KV ceiling

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + WEIGHTED-PRIMITIVE-LOWER-BOUND + SINC-TAIL-OPTIMIZATION + ORDINARY-PRIME-SOURCE + SELECTOR-DEBT-SCALE + CHEBYSHEV-PREFIX-COERCIVITY + KV-BARRIER + INTEGER-MULTIPLICITIES`.

**Parent finding:** RE-209.

`RE-209` turns continuum vertical hiding with a fixed logarithmic repair gap into a genuine source-side obstruction. Its B-spline test proves that hiding `|t|<=T` forces a weighted signed prefix of size `exp((1/e+o(1))HT)`, and hence that a separated ordinary-prime repair preserving every fixed Korobov--Vinogradov envelope must have

\[
T_Q=c\log Q,
\qquad
c<\frac{e}{2H}.
\]

The constant `1/e` there came only from the crude tail estimate `|sin x/x|<=1/x`. The same test family contains substantially more information. Once the exact first sidelobe of `sinc` is retained, the weighted-prefix exponent improves from `1/e=0.367879...` to

\[
\boxed{
\gamma_\star=0.5979019108\ldots .
}
\tag{1}
\]

Consequently every separated ordinary-prime `{0,1,2}` repair that hides a selector-scale local packet from the whole interval `|t|<=T_Q` while preserving every fixed KV envelope must satisfy

\[
\boxed{
\frac{\frac12\log Q-\gamma_\star H T_Q}{V(Q)}\longrightarrow+\infty,
\qquad
V(Q)=\frac{(\log Q)^{3/5}}{(\log\log Q)^{1/5}}.
}
\tag{2}
\]

For `T_Q=c\log Q`, this gives the improved universal ceiling

\[
\boxed{
c<\frac1{2\gamma_\star H}.
}
\tag{3}
\]

In the corridor used by `RE-203`--`RE-209`, `H=\log 8`, so

\[
\boxed{
c<0.4021548838\ldots .
}
\tag{4}
\]

This lowers the `RE-209` ceiling `0.6536086...` by about thirty-eight percent. The current constructive range from `RE-208`,

\[
0<c<\frac1{24H\log2}=0.0289079\ldots,
\]

is unchanged, so a large quantitative gap remains. The point is not that (4) is sharp; it is that a sizeable part of the previous gap was an artifact of throwing away the oscillatory geometry of the very same compactly supported test.

## 1. The first sinc sidelobe gives a uniform tail constant

Put

\[
f(x):=\frac{\sin x}{x},
\qquad f(0):=1.
\tag{5}
\]

Let `beta_1` be the first solution of

\[
\tan\beta=\beta
\tag{6}
\]

in `(pi,3pi/2)`. Numerically,

\[
\beta_1=4.4934094579\ldots .
\tag{7}
\]

At every nonzero stationary point of `f`, equation (6) gives

\[
f(\beta)=\cos\beta,
\qquad
|f(\beta)|=\frac1{\sqrt{1+\beta^2}}.
\tag{8}
\]

The stationary points after `pi` occur one per half-period and their absolute heights decrease strictly because their locations increase. Since `f` vanishes at every positive integer multiple of `pi`, the first negative sidelobe is therefore the largest absolute sidelobe after the first zero. Define

\[
M_\star
:=\sup_{x\ge\pi}|f(x)|
=\frac1{\sqrt{1+\beta_1^2}}
=0.2172336282\ldots .
\tag{9}
\]

On `(0,pi)`, `f` is positive and strictly decreasing. Hence there is a unique `a_\star in (0,pi)` satisfying

\[
\frac{\sin a_\star}{a_\star}=M_\star.
\tag{10}
\]

Numerically,

\[
a_\star=2.5535658093\ldots .
\tag{11}
\]

Combining monotonicity before `pi` with (9) gives the exact global tail statement

\[
\boxed{
\sup_{x\ge a_\star}\left|\frac{\sin x}{x}\right|=M_\star.
}
\tag{12}
\]

Finally set

\[
\boxed{
\gamma_\star:=\frac{\log(1/M_\star)}{a_\star}
=0.5979019108\ldots .
}
\tag{13}
\]

No external extremal theorem is being used here: (8)--(12) are elementary one-variable calculus.

## 2. The RE-209 B-spline lemma with the exact tail

Let `nu` be a finite real signed measure supported on `[H,infinity)` and assume

\[
\sup_{|t|\le T}|1-\widehat\nu(t)|\le\epsilon,
\qquad
0\le\epsilon<1,
\tag{14}
\]

where

\[
\widehat\nu(t):=\int e^{-itL}\,d\nu(L).
\tag{15}
\]

Define, exactly as in `RE-209`,

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u),
\qquad
R:=\sup_{L\ge H}e^{-L}|G(L)|.
\tag{16}
\]

Assume `HT -> infinity` and choose

\[
n:=\left\lfloor\frac{HT}{a_\star}\right\rfloor.
\tag{17}
\]

Let `v_n` be the uniform probability density on `[-T/n,T/n]`, let `w_n=v_n^{*n}`, and write

\[
\phi_n(L):=\widehat w_n(L)
=\left(
\frac{\sin(LT/n)}{LT/n}
\right)^n.
\tag{18}
\]

Because `n<=HT/a_star`, every `L>=H` satisfies

\[
\frac{LT}{n}\ge a_\star.
\tag{19}
\]

Pairing (14) against the nonnegative probability density `w_n` yields

\[
\left|\int\phi_n(L)\,d\nu(L)\right|
\ge1-\epsilon.
\tag{20}
\]

As in `RE-209`, use `dnu=e^{-L}dG` in the Stieltjes sense and integrate by parts:

\[
\int\phi_n\,d\nu
=-\int_H^\infty
G(L)\frac{d}{dL}\left(e^{-L}\phi_n(L)\right)dL.
\tag{21}
\]

Therefore

\[
1-\epsilon
\le
R\int_H^\infty
\left(|\phi_n'(L)|+|\phi_n(L)|\right)dL.
\tag{22}
\]

The only place where `RE-209` lost the new constant was its estimate of this integral. Put

\[
x:=\frac{LT}{n}.
\tag{23}
\]

Choose once and for all any fixed `X>1/M_star`. On the compact interval `[a_star,X]`, equation (12) gives `|f(x)|<=M_star`, while `|f'(x)|` is bounded. Hence

\[
\int_{a_\star}^{X}|f(x)|^n dx
\ll_X M_\star^n,
\tag{24}
\]

and

\[
n\int_{a_\star}^{X}|f(x)|^{n-1}|f'(x)|dx
\ll_X nM_\star^{n-1}.
\tag{25}
\]

For `x>=X`, use the elementary estimates

\[
|f(x)|\le x^{-1},
\qquad
|f'(x)|\le x^{-1}+x^{-2}.
\tag{26}
\]

Since `X^{-1}<M_star`, their tails are exponentially smaller than (24)--(25). Returning to `L`, and noting that `n/T=O_H(1)`, we obtain

\[
\boxed{
\int_H^\infty
\left(|\phi_n'|+|\phi_n|\right)dL
\ll_{H,X} nM_\star^{n-1}.
}
\tag{27}
\]

Combining (22) and (27),

\[
R
\gg_{H,X}
\frac{1-\epsilon}{n}M_\star^{-(n-1)}.
\tag{28}
\]

Using (17),

\[
\boxed{
\log R
\ge
\left(\gamma_\star+o(1)\right)HT
}
\tag{29}
\]

whenever `HT->infinity` and `epsilon` stays bounded away from `1`. More explicitly, the omitted term is only `O_H(log(HT)+1)` in the logarithm.

This is the same weighted-cumulative-primitive norm as `RE-209`; only the compactly supported test is being estimated more faithfully.

## 3. Pulling the stronger harmonic bound back to ordinary primes

Use the arithmetic setup of `RE-209`. Let

\[
X_0:=2Q,
\qquad
B\asymp\frac{\sqrt Q}{\log Q},
\qquad
D_Q(s)
:=
\sum_{q\in\mathcal P_Q}\log(1-q^{-s})^{-1}
+
\sum_{q\in\mathcal R_Q}c_q\log(1-q^{-s})^{-1},
\tag{30}
\]

where the local packet `mathcal P_Q` consists of `B` ordinary primes in a relative `o(1/log Q)` neighborhood of `X_0`, all with one sign, every remote edit is an ordinary prime with coefficient `c_q in {-1,+1}`, and

\[
q\ge X_0e^H
\tag{31}
\]

for one fixed `H>0`. Assume `T_Q=O(log Q)`, `HT_Q->infinity`, and

\[
\sup_{|t|\le T_Q}|D_Q(1+it)|=o(d_Q),
\qquad
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{32}
\]

After multiplying by `(X_0/B)e^{it log X_0}`, the local first Euler harmonic is `1+o(1)`. The remote first harmonics define the measure

\[
\mu_Q
:=
\sum_{q\in\mathcal R_Q}
 c_q\frac{X_0}{Bq}
 \delta_{\log(q/X_0)}.
\tag{33}
\]

Because each ordinary prime is edited at most once,

\[
\frac{X_0}{B}
\sum_{q\ge X_0e^H}O(q^{-2})
=O(B^{-1})=o(1),
\tag{34}
\]

so exact Euler prime powers are negligible uniformly on `Re s=1`. Thus `nu_Q:=-mu_Q` satisfies (14) with, say, `epsilon=1/4` for large `Q`.

For this measure the weighted primitive is exactly a signed prime-count prefix. If

\[
C_Q(y):=
\sum_{\substack{q\in\mathcal R_Q\\q\le y}}c_q,
\tag{35}
\]

then

\[
G_Q(L)=-\frac{C_Q(X_0e^L)}{B}.
\tag{36}
\]

Consequently (29) gives

\[
\boxed{
\sup_{L\ge H}
 e^{-L}|C_Q(X_0e^L)|
\ge
B\exp\left((\gamma_\star+o(1))HT_Q\right).
}
\tag{37}
\]

The maximal-prefix partial-summation step of `RE-209` is unchanged. Applied to (37), it converts the signed count imbalance into a Chebyshev excursion at the same physical scale:

\[
\boxed{
\sup_{x\ge X_0e^H}
\frac{|\Delta\vartheta_Q(x)|}{x}
\ge
Q^{-1/2}
\exp\left((\gamma_\star+o(1))HT_Q\right),
}
\tag{38}
\]

where

\[
\Delta\vartheta_Q(x)
:=
\sum_{\substack{q\le x\\q\in\mathcal P_Q}}\log q
+
\sum_{\substack{q\le x\\q\in\mathcal R_Q}}c_q\log q.
\tag{39}
\]

Equation (38) is the strengthened source-side tax. It remains insensitive to how violently the positive and negative remote edits interleave: some signed prefix must still become exponentially large.

## 4. The KV ceiling drops from 0.6536 to 0.4022 for the current corridor

Suppose the repair is required to satisfy, through every affected scale and for every fixed `b>0`,

\[
|\Delta\vartheta_Q(x)|
=o\left(xe^{-bV(x)}\right).
\tag{40}
\]

Since every affected scale in (38) is at least `Q`, the lower bound there is compatible with (40) only if

\[
\boxed{
\frac{\frac12\log Q-\gamma_\star HT_Q}{V(Q)}
\longrightarrow+\infty.
}
\tag{41}
\]

For `T_Q=c\log Q`, this forces

\[
\boxed{
c<\frac1{2\gamma_\star H}.
}
\tag{42}
\]

With `H=log 8`,

\[
\frac1{2\gamma_\star\log8}
=0.4021548838\ldots,
\tag{43}
\]

whereas `RE-209` gave `e/(2log8)=0.6536086...`.

Together with `RE-208`, the presently proved two-sided interval is therefore

\[
\boxed{
0.0289079\ldots
< c_{\mathrm{transition}}
<0.4021549\ldots
}
\tag{44}
\]

in the limited sense that ordinary-prime separated hiding is explicitly constructed below the left constant and is impossible, under fixed-KV fidelity, at or above the right constant. No sharp transition is asserted to exist.

## Representation audit

The improvement in Sections 1--2 is **generic Fourier geometry**. It does not use primes, Robin, Euler products, or integer multiplicities. In particular, the numerical constant `gamma_star` is not source-specific and is not claimed to be a new extremal constant for compactly supported tests. It is merely the exact rate obtained from the same repeated-uniform/B-spline family already used by `RE-209` once its true sinc tail is retained.

The source-specific step is Section 3: for ordinary-prime Euler atoms the exponentially weighted primitive becomes a signed prime-count prefix, and partial summation converts that prefix into a Chebyshev discrepancy. That transfer is exactly the arithmetic mechanism isolated by `RE-209`; the present finding strengthens only its harmonic input.

The hard constraints are unchanged: ordinary primes, edit coefficients in `{-1,+1}`, a fixed pre-repair logarithmic gap `H`, exact Euler factors, selector-scale local mass, and fidelity to every fixed KV envelope. The relaxed object appears only inside the generic harmonic lemma, where an arbitrary finite signed measure is allowed in order to prove a lower bound that therefore also applies to the discrete prime source.

No new external theorem is load-bearing. The sinc-lobe calculation is elementary and the PNT/KV input is already anchored in `SOURCES.md`, so no source update is required.

## Clue impact

Neither active clue changes state. `CLUE-clean-peak-selector-height-coupling` concerns source-selected clean CA peak geometry, while `CLUE-extremal-exchange-discretization-budget` concerns discretization of the extremal exchange model. The present result only sharpens the continuum vertical-Euler coercivity constant inside an already separated matched-control architecture.

## Adversarial self-review

**Could a later sinc lobe exceed the first one?** No. Every post-`pi` interior extremum solves `tan x=x`, and at such a point its absolute height is `1/sqrt(1+x^2)`, which strictly decreases with the extremum location. Endpoints are zeros. Thus (9) is global, not a first-lobe heuristic.

**Does the uniform bound `|f|<=M_star` make the integral in (27) diverge over an infinite half-line?** It would if used alone. The proof deliberately splits at fixed `X>1/M_star`; on the compact piece the exact sidelobe bound supplies `M_star^n`, while on the infinite tail `|f(x)|<=1/x` is integrable after the `n`th power and decays faster because `X^{-1}<M_star`.

**Does differentiating `phi_n=f^n` lose the improved exponent?** Only a polynomial factor `n` and one power of `M_star`, both contributing `o(HT)` to `log R`. They do not alter `gamma_star`.

**Does the floor in `n=floor(HT/a_star)` matter?** No. It changes `n` by at most one and hence changes `log R` by `O(1)`.

**Is the decimal ceiling in (43) a proved optimal barrier?** No. It is a rigorously available stronger ceiling from one explicit compactly supported test family. An extremal compact-support test could lower it further, and a better source-aware construction could raise the constructive constant.

**Does this prove Robin or eliminate all matched counterexample sources?** No. It remains a theorem about the separated continuum-vertical Euler architecture. It does not prove that a hypothetical Robin counterexample supplies this observation interval, does not eliminate repairs with no fixed pre-repair gap, and does not simultaneously enforce the full CA selector structure.

The next high-value step is now cleanly quantitative. On the obstruction side, determine or tightly bound the true extremal compact-support constant for the weighted primitive norm rather than another crude sinc estimate. On the constructive side, replace the coefficient-heavy one-sided binomial synthesis of `RE-208` by a source-aware repair whose **signed weighted prefixes**, not merely absolute variation, are controlled. Either direction attacks the remaining factor-of-fourteen gap in (44) in the physical currency that now matters.
