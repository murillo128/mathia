# AF-487 — Critical moving-window noise has sharp inverse-depth log-generator resolution

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SAMPLING`, `MINIMAX-RESOLUTION`, `SHARP-RATE`, `SIDE-INFORMATION`, `CLASSICAL-PRONY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-486 identifies the sharp **absolute observation scale** for retaining the `J`th ordered generator of a positive Dirichlet source through a fixed-width moving sample window: errors of order `q_J^{-t}` are small enough for joint Hankel recovery below a conditioning constant, while an order-one multiple of the same scale can erase the entire `J`th atom. That does not yet say how accurately the surviving generator can be localized when the observation error actually sits at this critical scale.

For a natural one-parameter local source class, the answer is sharp:

\[
\boxed{
\text{critical sample noise }\asymp q_J^{-t}
\quad\Longrightarrow\quad
\text{best uniform resolution in }\log q_J\asymp \frac1t.
}
\tag{1}
\]

Thus exponential absolute measurement precision does **not** turn into exponential parameter precision. At the survival threshold of AF-486, a finite moving window carries only inverse-depth resolution for the logarithmic generator. This gives a quantitative fidelity modulus between raw observation scale and recoverable source parameter.

The lower bound is deliberately against a continuum of matched positive Dirichlet controls. It is not a lower bound for a decoder that is given the extra arithmetic side information that the unknown generator already belongs to a discrete set such as the rational primes. In fact, a discrete marking with fixed positive log-spacing converts the `O(1/t)` estimate into eventual exact identification by nearest-neighbor projection. That distinction is part of the result: **raw source fidelity and fidelity after adding a discriminator-bearing mark are different problems.**

## Local source family and risk

Start from the AF-486 source

\[
F(s)=\sum_{n\ge1}a_nq_n^{-s},
\qquad
1<q_1<q_2<\cdots,
\qquad a_n>0,
\tag{2}
\]

absolutely convergent for `Re(s)>sigma_0`. Fix a depth `J`, a step `h>0`, and all source data except the `J`th generator. Choose a compact interval

\[
I=[q_-,q_+]
\subset(q_{J-1},q_{J+1})
\tag{3}
\]

containing the reference `q_J` in its interior, with the evident omission of `q_{J-1}` when `J=1`. For `q\in I`, write

\[
F_q(s)
=
\sum_{n<J}a_nq_n^{-s}
+a_Jq^{-s}
+\sum_{n>J}a_nq_n^{-s}.
\tag{4}
\]

Set

\[
M:=2J-2,
\qquad
m_t(q):=\bigl(F_q(t+kh)\bigr)_{k=0}^{M}.
\tag{5}
\]

The observed vector is

\[
y=m_t(q)+\eta,
\qquad
\|\eta\|_\infty\le\varepsilon q^{-t},
\tag{6}
\]

where `epsilon>0` is fixed. For an estimator `\widehat q_t(y)`, measure error in the natural exponential coordinate

\[
\mathcal R_t(\widehat q_t;I)
:=
\sup_{q\in I}
\sup_{\|\eta\|_\infty\le\varepsilon q^{-t}}
\bigl|\log \widehat q_t(m_t(q)+\eta)-\log q\bigr|.
\tag{7}
\]

The source-specific scaling in `(6)` is exactly the critical scale isolated by AF-486.

## Uniform upper bound from the moving Hankel estimator

For each `q\in I`, let

\[
x_i=q_i^{-h}\quad(i<J),
\qquad x_J(q)=q^{-h},
\]

and let `V_J(q)` be the `J x J` Vandermonde matrix on these first `J` nodes. Compactness of `I` inside the ordering gap in `(3)` gives

\[
\sigma_*:=\inf_{q\in I}\sigma_{\min}(V_J(q))>0.
\tag{8}
\]

Let

\[
a_*:=\min_{1\le j\le J}a_j.
\]

Assume

\[
0<\varepsilon<\frac{a_*\sigma_*^2}{J}.
\tag{9}
\]

Form the noisy Hankel determinants `\widetilde D_J(t)` and `\widetilde D_{J-1}(t)` from the `2J-1` samples in `(6)`, exactly as in AF-486, and define

\[
\widehat q_t
:=
\left(
\frac{\widetilde D_J(t)}{\widetilde D_{J-1}(t)}
\right)^{-1/t}.
\tag{10}
\]

AF-486 gives the exact determinant-ratio asymptotic

\[
\frac{D_J(t)}{D_{J-1}(t)}
=C_J(q)q^{-t}(1+o(1)),
\tag{11}
\]

where

\[
C_J(q)
=
\frac{A_J(q)}{A_{J-1}}
=
a_J\prod_{i<J}(q_i^{-h}-q^{-h})^2.
\tag{12}
\]

Because `I` stays a positive distance from the neighboring generators, `C_J(q)` is continuous and bounded above and below by positive constants on `I`. The tail error in AF-486 is also uniform here: when a `q_{J+1}` tail atom exists,

\[
\sup_{q\in I}\frac{q}{q_{J+1}}
\le
\frac{q_+}{q_{J+1}}<1.
\tag{13}
\]

For the noisy numerator, AF-486's Loewner/Vandermonde argument gives uniformly

\[
(1-\kappa)^J
\le
\frac{\widetilde D_J(t)}{D_J(t)}
\le
(1+\kappa)^J,
\qquad
\kappa:=\frac{J\varepsilon}{a_*\sigma_*^2}<1.
\tag{14}
\]

For the denominator, the same absolute sample errors are exponentially smaller than the weakest of the first `J-1` atoms, uniformly over `q\in I`, because

\[
\frac{q^{-t}}{q_{J-1}^{-t}}
\le
\left(\frac{q_{J-1}}{q_-}\right)^t
\to0.
\tag{15}
\]

Hence for all sufficiently large `t` there are constants `0<B_-<B_+<infinity`, independent of `q\in I`, of the admissible noise vector, and of `t`, such that

\[
B_-
\le
\frac{\widetilde D_J(t)/\widetilde D_{J-1}(t)}{q^{-t}}
\le
B_+.
\tag{16}
\]

Taking logarithms in `(10)` therefore yields

\[
\bigl|\log\widehat q_t-\log q\bigr|
\le
\frac{C}{t}
\tag{17}
\]

for a finite source-neighborhood constant `C`. Thus

\[
\boxed{
\mathcal R_t(\widehat q_t;I)\le\frac{C}{t}.
}
\tag{18}
\]

The `1/t` rate is already latent in AF-486's root extraction: every bounded multiplicative uncertainty in the determinant ratio becomes an additive `O(1/t)` uncertainty in `log q`.

## Matching deterministic lower bound

The inverse-depth rate cannot be uniformly improved on this unmarked local source class.

Choose any interior point `q_0\in\operatorname{int}I`. For a fixed `gamma>0` and each large `t`, define

\[
q_1(t):=q_0e^{\gamma/t}.
\tag{19}
\]

Then `q_1(t)\in I` for all sufficiently large `t`, and

\[
|\log q_1(t)-\log q_0|=\frac{\gamma}{t}.
\tag{20}
\]

The two sources are identical except for the `J`th generator. At sample offset `k`,

\[
\begin{aligned}
&F_{q_0}(t+kh)-F_{q_1(t)}(t+kh)\\
&\qquad=
 a_Jq_0^{-(t+kh)}
\left[1-e^{-\gamma(1+kh/t)}\right].
\end{aligned}
\tag{21}
\]

For `0\le k\le M` and all sufficiently large `t`, `1+kh/t\le2`; hence `1-e^{-u}\le u` gives

\[
\|m_t(q_0)-m_t(q_1(t))\|_\infty
\le
2a_J\gamma q_0^{-t}.
\tag{22}
\]

Choose once and for all

\[
0<\gamma
\le
\min\left\{\frac12,\frac{\varepsilon}{4ea_J}\right\}.
\tag{23}
\]

Since `q_1(t)^{-t}=e^{-\gamma}q_0^{-t}` and `e^{-\gamma}\ge e^{-1}`, `(22)`-`(23)` imply, for all sufficiently large `t`,

\[
\|m_t(q_0)-m_t(q_1(t))\|_\infty
\le
\varepsilon q_1(t)^{-t}.
\tag{24}
\]

Therefore the exact datum `y=m_t(q_0)` has two admissible explanations:

- source `q_0` with zero noise;
- source `q_1(t)` with the adversarial noise `m_t(q_0)-m_t(q_1(t))`.

No estimator seeing only `y` can be within less than half the parameter separation of both explanations. By the triangle inequality,

\[
\max\left\{
|\log\widehat q_t(y)-\log q_0|,
|\log\widehat q_t(y)-\log q_1(t)|
\right\}
\ge
\frac{\gamma}{2t}.
\tag{25}
\]

Consequently every estimator obeys

\[
\boxed{
\inf_{\widehat q_t}\mathcal R_t(\widehat q_t;I)
\ge
\frac{c}{t},
\qquad c:=\frac\gamma2>0.
}
\tag{26}
\]

Combining `(18)` and `(26)` gives the sharp local minimax order

\[
\boxed{
\inf_{\widehat q_t}\mathcal R_t(\widehat q_t;I)
=\Theta(t^{-1}).
}
\tag{27}
\]

This is a deterministic finite-window statement. The lower-bound pair depends on `t`, as is standard for a local resolution/minimax argument: two generators approach each other at exactly the scale being tested. It does **not** claim that two fixed distinct sources remain indistinguishable as `t\to\infty`.

## Discrete markings turn approximation into exact identification

Equation `(27)` describes the unmarked continuum neighborhood `I`. Suppose instead that extra side information restricts the unknown generator to a discrete candidate set `Lambda\subset I` with positive logarithmic spacing

\[
\delta_\Lambda
:=
\inf_{\substack{u,v\in\Lambda\\u\ne v}}
|\log u-\log v|
>0.
\tag{28}
\]

If an estimator satisfies `(17)`, then for

\[
t>\frac{2C}{\delta_\Lambda}
\tag{29}
\]

its log-error is strictly below half the candidate spacing. Nearest-neighbor projection in `log q` therefore returns the exact element of `Lambda`.

So the same noisy moving window has two distinct fidelity statements:

\[
\text{unmarked local generator}
\quad\Rightarrow\quad
\Theta(1/t)\text{ resolution},
\tag{30}
\]

whereas

\[
\text{generator + discrete candidate marking}
\quad\Rightarrow\quad
\text{eventual exact identification}.
\tag{31}
\]

For a fixed finite prime candidate region, rational primes provide such a discrete set. But using that set as `Lambda` presupposes exactly the arithmetic marking one would need to explain. Therefore `(31)` is **not** evidence that the raw Dirichlet-sampling compression intrinsically recognizes rational primality. It is instead a clean minimal-lift example: a discrete discriminator supplied as side information changes the recoverability class.

## Prior art and novelty audit

The surrounding parameter-estimation mathematics is classical. Dmitry Batenkov and Yosef Yomdin, **“On the Accuracy of Solving Confluent Prony Systems,”** *SIAM Journal on Applied Mathematics* 73(1), 134–154 (2013), DOI `10.1137/110836584`, studies maximal local accuracy of Prony-type systems under measurement perturbations and formulates stability through the geometry/conditioning of the associated Jacobian, Vandermonde, and Hankel structures. AF-487 does not claim a new general theory of local Prony accuracy.

Celine Aubel and Helmut Bolcskei, **“Deterministic Performance Analysis of Subspace Methods for Cisoid Parameter Estimation,”** *Proc. IEEE ISIT* (2016), 1551–1555, DOI `10.1109/ISIT.2016.7541559`, gives deterministic finite-sample, finite-SNR error analysis for ESPRIT and matrix-pencil methods and ties performance to Vandermonde conditioning. Their later work on **“Vandermonde matrices with nodes in the unit disk and the large sieve,”** *Applied and Computational Harmonic Analysis* 47(1), 53–86 (2019), develops explicit extremal-singular-value and condition-number bounds for such Vandermonde matrices. These are direct prior art for treating node recovery as a conditioning problem.

Ankur Moitra, **“Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices,”** *STOC 2015*, 821–830, DOI `10.1145/2746539.2746561`, proves sharp noisy distinguishability thresholds in a different super-resolution model and explicitly connects impossibility/possibility boundaries to Vandermonde conditioning. Thus neither a two-point indistinguishability lower bound nor a sharp resolution threshold under noisy exponential measurements is claimed as a new general technique.

The Arithmetic Fidelity contribution is narrower: AF-486's moving-rightward Dirichlet compression has a source-dependent **critical absolute error scale** `q_J^{-t}`. At exactly that moving scale, bounded multiplicative uncertainty in the Hankel determinant ratio and a matched two-source construction meet at the same `Theta(1/t)` logarithmic parameter resolution. The new statement is this exact fidelity modulus for the AF-486 compression, together with the explicit separation between unmarked continuum recovery and recovery after a discrete candidate marking. No broader novelty claim is made.

## Boundaries and falsification checks

- The upper bound assumes the uniform AF-486 conditioning gate `(9)`. If the retained Vandermonde nodes approach collision, `sigma_*` can vanish and no uniform constant `C` follows.
- The lower bound is for a local family of positive Dirichlet controls in which `q_J` may vary continuously. It does not apply unchanged when arithmetic side information restricts `q_J` to a known discrete set.
- `J`, `h`, and the window width `2J-1` are fixed while `t\to\infty`. No growing-depth theorem is claimed.
- The data at each `t` consist of one finite moving window. The lower bound does not cover an estimator allowed to accumulate an ever-growing history of earlier windows; such a larger observation channel can contain more information.
- The adversarial noise budget is a fixed nonzero multiple `epsilon q^{-t}`. At zero noise, AF-486 gives exact asymptotic recovery and the lower-bound construction does not apply.
- The alternatives in `(19)` depend on `t`; this proves a local minimax resolution law, not persistent indistinguishability of two fixed sources.
- The norm in `(6)` is the samplewise `l_infinity` norm. Other noise geometries change constants and may change rates if their budgets scale differently with `t`.
- Positivity and strict ordering are inherited from AF-486. Signed/complex amplitudes or accumulating supports require a separate analysis.
- The result remains source-level rather than prime-specific. It quantifies how accurately an ordered generator survives the declared sample compression; it does not identify which source class generated that node.

A direct falsification of the upper rate would require admissible critical-scale perturbations whose determinant ratio changes by more than every bounded multiplicative factor despite the uniform positive-definite bound `(14)`. A falsification of the lower rate would require one estimator to distinguish the two admissible explanations in `(24)` to `o(1/t)` log-error, contradicting their common observed datum and parameter separation `(20)`.

## Research consequence

AF-486 supplied an **observation survival threshold**. AF-487 separates that threshold from **parameter resolution**:

\[
q_J^{-t}\text{ absolute precision}
\quad\Longrightarrow\quad
\Theta(1/t)\text{ raw log-generator resolution}.
\tag{32}
\]

This matters for the broader Arithmetic Fidelity program because “the discriminator survives” is not a binary statement once noise or approximate compression is admitted. One must track a modulus: how observation error is converted into uncertainty along the surviving structural coordinate. Here the modulus is logarithmic-root conditioning, and the `1/t` rate is sharp.

The discrete-marking corollary also gives a controlled example of the line's central distinction between **intrinsic preservation** and **recovery after adding provenance**. If rational-prime membership is supplied beforehand, the approximate generator can eventually be snapped to the exact prime; if the objective is to explain why the source was rational-prime rather than a matched Beurling/control source, that same marking cannot be smuggled in as free side information. The next arithmetic question is therefore not whether the moving window can numerically localize `p_J`—it can—but whether any intrinsic observable carried by the source itself certifies the rational-prime discriminator without assuming the candidate set in advance.