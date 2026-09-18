# RE-209 — Spectral-gap continuum hiding forces an exponential KV prefix tax

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + WEIGHTED-PRIMITIVE-LOWER-BOUND + ORDINARY-PRIME-SOURCE + SELECTOR-DEBT-SCALE + CHEBYSHEV-PREFIX-COERCIVITY + KV-BARRIER + INTEGER-MULTIPLICITIES`.

**Parent findings:** RE-204, RE-208.

`RE-204` proves that hiding one selector-scale Euler atom from an entire vertical interval while every repair frequency is separated by a fixed logarithmic gap `H` costs `exp(Omega(H T))` in reciprocal total variation. `RE-208` shows that ordinary primes can pay a large part of that cost while preserving every fixed Korobov--Vinogradov envelope, reaching every fixed coefficient-variation exponent `kappa<1/2`. Its explicit surviving caveat is that the `1/2` ceiling comes from bounding Chebyshev discrepancy by **absolute** edit mass; perhaps sufficiently interleaved positive and negative edits could have much larger total variation while keeping every signed prefix small.

There is a representation-independent obstruction to that escape. The same B-spline test used for total variation can be integrated by parts one level further. It forces not merely large variation, but a large **exponentially weighted cumulative primitive** of any remote repair measure. For ordinary-prime Euler atoms that primitive is exactly a scaled signed prime-count prefix. Partial summation then converts it into a Chebyshev prefix excursion at the *same physical scale*, so moving the excursion farther out does not make it cheaper relative to the local KV envelope.

Let

\[
X_0:=2Q,
\qquad
B\asymp\frac{\sqrt Q}{\log Q},
\qquad
d_Q:=\frac1{\sqrt Q\log Q}.
\tag{1}
\]

Take the same local packet architecture as `RE-208`: `B` ordinary primes in a relative interval of width `Q^(theta-1)` around `X_0`, with one common perturbation sign, where some fixed `theta<1` is used. Let every remote edit be an ordinary prime `q>=X_0e^H`, for one fixed `H>0`, with coefficient `c_q in {-1,+1}`; the remote support may be arbitrarily far out but is finite. Put

\[
D_Q(s):=
\sum_{q\in\mathcal P_Q}\log(1-q^{-s})^{-1}
+
\sum_{q\in\mathcal R_Q}c_q\log(1-q^{-s})^{-1}.
\tag{2}
\]

Assume `T_Q=O(log Q)`, `H T_Q -> infinity`, and

\[
\boxed{
\sup_{|t|\le T_Q}|D_Q(1+it)|=o(d_Q).
}
\tag{3}
\]

Then the associated prime-Chebyshev perturbation

\[
\Delta\vartheta_Q(x)
:=
\sum_{\substack{q\le x\\q\in\mathcal P_Q}}\log q
+
\sum_{\substack{q\le x\\q\in\mathcal R_Q}}c_q\log q
\tag{4}
\]

must satisfy

\[
\boxed{
\sup_{x\ge X_0e^H}
\frac{|\Delta\vartheta_Q(x)|}{x}
\gg_H
Q^{-1/2}\exp\!\left(\frac{H T_Q}{e}\right).
}
\tag{5}
\]

The constant `1/e` is the optimum of the elementary one-parameter sinc estimate used below; it is not claimed to be the sharp harmonic-analysis constant.

Consequently a repair satisfying, for **every** fixed `b>0`,

\[
|\Delta\vartheta_Q(x)|
=o\!\left(xe^{-bV(x)}\right),
\qquad
V(x):=\frac{(\log x)^{3/5}}{(\log\log x)^{1/5}},
\tag{6}
\]

through all affected scales must obey the necessary condition

\[
\boxed{
\frac{\frac12\log Q-\frac{H}{e}T_Q}{V(Q)}\longrightarrow+\infty.
}
\tag{7}
\]

In particular, if `T_Q=c log Q` with fixed `c`, then no such KV-faithful remote repair exists for

\[
\boxed{
c\ge\frac{e}{2H}.}
\tag{8}
\]

For the corridor used in `RE-203`--`RE-208`, `H=log 8`, this gives the explicit universal ceiling

\[
\boxed{
 c<\frac{e}{2\log8}=0.6536086\ldots
}
\tag{9}
\]

for any continuum-hiding construction of this separated ordinary-prime `{0,1,2}` type. This is far above the current constructive range `c<1/(24(log8)log2)=0.0289079...` from `RE-208`; the result therefore does **not** close the quantitative gap. It does, however, turn the complex vertical branch from “perhaps arbitrary source-side cancellation can always pay the variation” into a genuine two-sided problem: continuum hiding is known below one positive logarithmic-height constant and impossible above another.

## 1. A spectral-gap test controls the weighted cumulative primitive, not only total variation

The harmonic lemma is independent of primes. Let `nu` be a finite real signed measure supported on `[H,infinity)` and suppose

\[
\sup_{|t|\le T}
|1-\widehat\nu(t)|\le\epsilon,
\qquad
0\le\epsilon<1,
\tag{10}
\]

where

\[
\widehat\nu(t):=\int e^{-itL}\,d\nu(L).
\tag{11}
\]

Define the exponentially weighted cumulative primitive

\[
G(L):=\int_{[H,L]}e^u\,d\nu(u)
\tag{12}
\]

and its scale-normalized prefix size

\[
R:=\sup_{L\ge H}e^{-L}|G(L)|.
\tag{13}
\]

For every fixed `a>1`, choose

\[
n:=\left\lfloor\frac{HT}{a}\right\rfloor
\tag{14}
\]

and assume `n>=2`. Let `v_n` be the uniform probability density on `[-T/n,T/n]` and let `w_n=v_n^{*n}`. Then `w_n` is a probability density supported on `[-T,T]`, and

\[
\phi_n(L):=\widehat w_n(L)
=\left(\frac{\sin(LT/n)}{LT/n}\right)^n.
\tag{15}
\]

Pairing (10) against `w_n` gives

\[
\left|1-\int\phi_n(L)\,d\nu(L)\right|
\le\epsilon,
\tag{16}
\]

so

\[
\left|\int\phi_n\,d\nu\right|\ge1-\epsilon.
\tag{17}
\]

Now use `d nu(L)=e^{-L}dG(L)` in the Stieltjes sense. Since `G(H-)=0`, the support of `nu` is finite for the arithmetic application, and `phi_n(L)e^{-L}->0`, integration by parts gives

\[
\int\phi_n\,d\nu
=-\int_H^\infty
G(L)\frac{d}{dL}\left(e^{-L}\phi_n(L)\right)dL.
\tag{18}
\]

Therefore

\[
\left|\int\phi_n\,d\nu\right|
\le
R\int_H^\infty
\left(|\phi_n'(L)|+|\phi_n(L)|\right)dL.
\tag{19}
\]

Write

\[
f(x):=\frac{\sin x}{x},
\qquad
x:=\frac{LT}{n},
\qquad
x_0:=\frac{HT}{n}\ge a.
\tag{20}
\]

For `x>=a>1`,

\[
|f(x)|\le x^{-1},
\qquad
|f'(x)|\le x^{-1}+x^{-2}.
\tag{21}
\]

Hence, with constants depending only on `a` and `H`,

\[
\begin{aligned}
\int_H^\infty|\phi_n'(L)|\,dL
&=
 n\int_{x_0}^\infty
 |f(x)|^{n-1}|f'(x)|\,dx
 \\&\ll_a a^{-n},
\\[4pt]
\int_H^\infty|\phi_n(L)|\,dL
&=
\frac nT\int_{x_0}^\infty|f(x)|^n\,dx
 \\&\ll_{a,H}a^{-n}.
\end{aligned}
\tag{22}
\]

Combining (17), (19), and (22),

\[
\boxed{
R\gg_{a,H}(1-\epsilon)a^n
=
\exp\!\left(
\left(\frac{\log a}{a}+o(1)\right)HT
\right).
}
\tag{23}
\]

The elementary rate `(log a)/a` is maximized at `a=e`, giving

\[
\boxed{
R\gg_H(1-\epsilon)
\exp\!\left(\frac{HT}{e}\right)
}
\tag{24}
\]

up to a fixed multiplicative constant and the harmless integer-part loss in `n`.

This is the new point relative to the total-variation lower bound in `RE-204`. The large dynamic range cannot be hidden purely in rapidly alternating atoms with every cumulative prefix small: after weighting by physical displacement, **some prefix itself must be exponentially large**.

## 2. Exact Euler hiding reduces to the first-harmonic measure uniformly over all remote shells

Return to the prime perturbation. Normalize (2) by multiplying by

\[
\frac{X_0}{B}e^{it\log X_0}.
\tag{25}
\]

Because the local packet has relative diameter `O(Q^(theta-1))` and `T_Q=O(log Q)`, its first Euler harmonic becomes

\[
\frac{X_0}{B}e^{it\log X_0}
\sum_{q\in\mathcal P_Q}q^{-1-it}
=1+o(1)
\tag{26}
\]

uniformly for `|t|<=T_Q`.

For the remote first harmonics define

\[
\mu_Q
:=
\sum_{q\in\mathcal R_Q}
 c_q\frac{X_0}{Bq}
 \delta_{\log(q/X_0)}.
\tag{27}
\]

Then their normalized contribution is exactly `widehat(mu_Q)(t)`.

The exact prime powers do not create an escape even if the remote edits extend to arbitrarily large primes. Uniformly on `Re s=1`,

\[
\log(1-q^{-s})^{-1}=q^{-s}+O(q^{-2}).
\tag{28}
\]

Since every ordinary prime is edited at most once,

\[
\frac{X_0}{B}
\sum_{q\in\mathcal R_Q}O(q^{-2})
\le
\frac{X_0}{B}
\sum_{n\ge X_0e^H}O(n^{-2})
=O(B^{-1})=o(1).
\tag{29}
\]

The local higher-harmonic remainder is `O(X_0^(-1))` after the same normalization. Thus (3) implies

\[
\sup_{|t|\le T_Q}
|1+\widehat\mu_Q(t)|=o(1).
\tag{30}
\]

Apply the harmonic lemma to

\[
\nu_Q:=-\mu_Q.
\tag{31}
\]

For large `Q`, (10) holds with any fixed `epsilon<1`, for example `epsilon=1/4`.

## 3. The weighted primitive is exactly a signed prime-count prefix

Let

\[
C_Q(y):=
\sum_{\substack{q\in\mathcal R_Q\\q\le y}}c_q.
\tag{32}
\]

For `L>=H`, the primitive (12) attached to `nu_Q` is

\[
G_Q(L)
=
-\sum_{\substack{q\in\mathcal R_Q\\q\le X_0e^L}}
\frac{c_q}{B}
=-\frac{C_Q(X_0e^L)}{B}.
\tag{33}
\]

Therefore (24) gives

\[
\boxed{
\sup_{L\ge H}
 e^{-L}|C_Q(X_0e^L)|
\gg_H
B\exp\!\left(\frac{HT_Q}{e}\right).
}
\tag{34}
\]

This is stronger than a lower bound on the total number of edits. It says that at some physical scale the **signed cumulative imbalance**, normalized by that scale's multiplicative displacement, is exponentially large.

Let `L_*` attain the maximum in (34), put

\[
y_*:=X_0e^{L_*},
\qquad
R_Q:=
\frac{e^{-L_*}|C_Q(y_*)|}{B}.
\tag{35}
\]

By maximality, for every `H<=u<=L_*`,

\[
|C_Q(X_0e^u)|\le BR_Qe^u.
\tag{36}
\]

Partial summation over the remote edits gives

\[
\sum_{\substack{q\in\mathcal R_Q\\q\le y_*}}
c_q\log q
=
C_Q(y_*)\log y_*
-
\int_{X_0e^H}^{y_*}
\frac{C_Q(y)}{y}\,dy.
\tag{37}
\]

Using (35)--(36),

\[
\left|
\sum_{\substack{q\in\mathcal R_Q\\q\le y_*}}
c_q\log q
\right|
\ge
BR_Qe^{L_*}
\left(\log y_*-1+O_H(e^{H-L_*})\right).
\tag{38}
\]

The local packet contributes only `O(B log Q)`. Since `H T_Q->infinity`, (34) makes this negligible compared with (38). Dividing by `y_*=X_0e^(L_*)` yields

\[
\frac{|\Delta\vartheta_Q(y_*)|}{y_*}
\gg_H
\frac{B\log Q}{X_0}R_Q
\asymp
Q^{-1/2}R_Q.
\tag{39}
\]

Equations (34) and (39) prove (5).

The location of `y_*` has disappeared from the final normalized lower bound. This is why simply pushing the large prefix to a much more remote shell does not evade the argument: the weighted primitive already prices the larger physical scale by the factor `e^(-L)`.

## 4. KV fidelity forces a logarithmic-height ceiling

Suppose now that (6) holds for every fixed `b>0`. Since `y_*>=X_0e^H` and `V(x)` is eventually increasing,

\[
\frac{|\Delta\vartheta_Q(y_*)|}{y_*}
=o\!\left(e^{-bV(Q)}\right)
\tag{40}
\]

for each fixed `b>0`. But (5) gives

\[
\frac{|\Delta\vartheta_Q(y_*)|}{y_*}
\gg_H
\exp\!\left(
-\frac12\log Q+rac{HT_Q}{e}
\right).
\tag{41}
\]

Thus for every fixed `b>0`,

\[
\frac12\log Q-rac{HT_Q}{e}-bV(Q)
\longrightarrow+\infty.
\tag{42}
\]

This family of inequalities is equivalent to (7).

For `T_Q=c log Q`, the leading exponent in (41) is

\[
-\frac12+\frac{Hc}{e}.
\tag{43}
\]

At `c=e/(2H)` the lower bound is already of constant relative size, whereas every fixed KV envelope tends to zero. Every larger fixed `c` is therefore impossible as well, proving (8)--(9).

This is a genuine source-prefix obstruction, not the absolute-variation bookkeeping used for the constructive side. Arbitrarily many shells, dense sign interleaving, and arbitrarily remote repair locations are all included in the theorem as long as the fixed pre-repair logarithmic gap `H` and unit ordinary-prime multiplicity bound are retained.

## 5. Representation and prior-art audit

The B-spline/sinc test and exponential dynamic-range phenomenon are generic harmonic analysis. `RE-204` already records the classical superoscillation boundary, including Ferreira--Kempf and later surveys, and derives the neighboring total-variation lower bound directly. A fresh search also finds the expected literature on oscillation and sign changes for functions or measures with spectral gaps, but that literature addresses generic spectral-gap oscillation rather than the exact exponentially weighted prefix norm used here.

No external theorem is load-bearing in (10)--(24): the weighted-primitive estimate is the same elementary compactly supported test as `RE-204`, followed by one Stieltjes integration by parts and the elementary bounds (21). No new literature dependency is therefore added to `SOURCES.md`.

The source-specific step is (27)--(39). The reciprocal normalization of an ordinary-prime Euler atom is exactly `e^(-L)/B`; multiplying the primitive by `e^L` turns it into one unit of signed prime count. This precise weight match, plus partial summation, converts generic superoscillatory dynamic range into a pointwise Chebyshev-prefix tax. That conversion is the line-specific content of the finding.

## 6. Adversarial self-review and surviving boundary

**Could higher prime powers cancel the first-harmonic obstruction?** No for the stated `{0,1,2}` source. Equation (29) bounds *all* remote higher harmonics by the tail of `sum n^(-2)`, independently of how many remote shells are used or how far they extend. After selector normalization the entire tail is `o(1)`.

**Could the large signed count prefix occur so far out that the local KV envelope has become larger?** This is the main failure mode the weighted primitive was designed to test. Equation (34) controls `e^(-L)C_Q(X_0e^L)`, and (39) preserves that normalization after converting count to Chebyshev mass. The physical location therefore cancels from the lower bound.

**Could dense positive/negative interleaving keep Chebyshev prefixes small despite large coefficient variation?** Not throughout the whole repair. The harmonic lemma is stated for an arbitrary signed measure and does not count atoms or sign changes. It forces one weighted cumulative prefix to have the exponential size (24).

**Does the theorem rule out repairs that start immediately after the local packet?** No. The factor `H` is load-bearing: without a fixed spectral gap the sinc test has no exponential leverage. The current matched-control constructions deliberately keep such a corridor so that selector-scale debt exists before repair. A source architecture that destroys that corridor is outside this finding and must be assessed against the Robin transient separately.

**Does the constant `e/(2H)` identify the true rigidity threshold?** No. The `1/e` rate comes from the crude universal estimate `|sin x/x|<=1/x` and optimizing one test family. A sharper extremal test may lower the upper ceiling. Conversely, `RE-208` only constructs hiding up to a much smaller constant. The interval

\[
\frac1{24H\log2}
<c<
\frac e{2H}
\tag{44}
\]

remains open.

**Does this prove Robin or exclude a complete matched counterexample source?** No. It proves a new coercive boundary for the separated continuum-vertical Euler observable inside the ordinary-prime bounded-multiplicity control class. It does not show that a hypothetical Robin counterexample supplies such a continuum observation window, nor does it eliminate architectures without a fixed pre-repair gap or simultaneously enforce every CA selector constraint.

The next useful question is therefore quantitative rather than qualitative: improve either side of (44). On the constructive side, replace the absolute-mass realization in `RE-208` by a source-aware synthesis with controlled weighted prefixes. On the obstruction side, replace the sinc-power test by the extremal compactly supported test for the weighted primitive norm. Either improvement directly shrinks the first genuine two-sided interval found for continuum vertical Euler source rigidity.
