# MC-278 — Rational endpoint decoding beats polynomial degree only by hiding half-depth source mass

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the Boolean-row formulation of `MC-267`, `MC-275`, and `MC-277`. For a target row write

\[
x=(x_1,\ldots,x_k)\in\{-1,+1\}^k,
\qquad
b(x)=\#\{i:x_i=-1\}
=\frac{k-\sum_i x_i}{2}.
\tag{1}
\]

The row is blind exactly when `b(x)=0`. `MC-275` showed that a pointwise polynomial approximation to this endpoint indicator, accurate enough to sum over all

\[
C=\binom{N_y}{t}
\tag{2}
\]

target rows and recover one exceptional blind row, requires source degree

\[
\Omega\!\left(\sqrt{k\log C}\right).
\tag{3}
\]

Rational approximation changes that algebraic degree completely. For any integer `q>=1`, define

\[
F_q(x):=\frac{1}{(1+b(x))^q}.
\tag{4}
\]

Then

\[
F_q(1,\ldots,1)=1,
\qquad
0<F_q(x)\le 2^{-q}\quad(x\ne(1,\ldots,1)).
\tag{5}
\]

Thus `F_q` is a degree-`q` rational endpoint decoder because `1+b(x)` is affine. If `A_y(t)` denotes the number of blind target rows and

\[
R_{q,y}(t):=\sum_{|T|=t}F_q(x(T)),
\tag{6}
\]

then deterministically

\[
\boxed{
A_y(t)
\le R_{q,y}(t)
\le A_y(t)+\bigl(C-A_y(t)\bigr)2^{-q}.
}
\tag{7}
\]

Consequently, whenever

\[
C2^{-q}<\frac12,
\tag{8}
\]

the integer `A_y(t)` is recovered from `R_{q,y}(t)` by nearest-integer rounding; in particular

\[
A_y(t)=0\iff R_{q,y}(t)<\frac12.
\tag{9}
\]

At first sight this seems to evade the polynomial approximate-degree obstruction completely: atom-sensitive accuracy only needs

\[
q=\Theta(\log C)
=\Theta(\!\log y\,\log\log y),
\tag{10}
\]

rather than `(3)`.

The escape is algebraic but **not low-depth in the existing source-support hierarchy**. The unique Walsh expansion of `(4)` is

\[
\boxed{
F_q(x)
=\sum_{S\subseteq[k]}w_{q,k}(|S|)x_S,
}
\tag{11}
\]

with strictly nonnegative radial coefficients

\[
\boxed{
w_{q,k}(j)
=\frac1{\Gamma(q)}
\int_0^\infty
s^{q-1}e^{-s}
\left(\frac{1+e^{-s}}2\right)^{k-j}
\left(\frac{1-e^{-s}}2\right)^j ds.
}
\tag{12}
\]

Since the coefficients are nonnegative and `F_q(1^k)=1`,

\[
\pi_{q,k}(j):=\binom kj w_{q,k}(j)
\tag{13}
\]

is a probability distribution on source degree. If `J` has this law, then exactly

\[
\boxed{
\mathbb E J
=\frac{k}{2}\bigl(1-2^{-q}\bigr),
}
\tag{14}
\]

and

\[
\boxed{
\operatorname{Var}(J)
=\frac{k}{4}\bigl(1-3^{-q}\bigr)
+\frac{k^2}{4}\bigl(3^{-q}-4^{-q}\bigr).
}
\tag{15}
\]

Therefore at the atom-sensitive choice `(8)`, where `C` grows superpolynomially in `k` on the live shell scale,

\[
\mathbb E J=\left(\frac12+o(1)\right)k,
\qquad
\operatorname{Var}(J)=\left(\frac14+o(1)\right)k.
\tag{16}
\]

For every support cutoff `m=o(k)`, Chebyshev then gives

\[
\boxed{
\sum_{j=0}^{m}\binom kj w_{q,k}(j)
=\Pr(J\le m)
=O\!\left(\frac1k\right)=o(1).
}
\tag{17}
\]

In particular, the degree-`m` truncation of the **actual Walsh expansion** of the rational decoder has value only `o(1)` at the blind vector, while the full rational decoder has value exactly `1` there. At the live Christoffel/source depth

\[
m=t+1=\Theta(\log\log y)=o(k),
\tag{18}
\]

the atom-sensitive rational decoder places asymptotically all of its positive Walsh coefficient mass outside the available low-support hierarchy and concentrates that mass around source degree `k/2`.

Equivalently, using the source-shell quantities of `MC-267`,

\[
\boxed{
R_{q,y}(t)
=\sum_{j=0}^{k}w_{q,k}(j)H_{j,y}(t).
}
\tag{19}
\]

Thus rational normalization does identify a genuine representation class not covered by the polynomial approximate-degree lower bound, but its denominator inversion imports essentially half-cube source depth when expressed in the canonical Walsh/Krawtchouk coordinates. It is not a free low-depth escape.

This does **not** rule out a natural arithmetic resolvent, inverse operator, or other mechanism capable of controlling `(6)` directly without expanding the denominator into source subsets. It isolates that as the exact remaining question. No blind relation is excluded here and no estimate for `M(X)` follows.

## 1. Atom-sensitive rational decoding is elementary and exact

The endpoint indicator itself is

\[
\mathbf 1_{\{b=0\}}.
\]

For `b=0`, `(4)` is one. For every nonblind row `b>=1`,

\[
(1+b)^{-q}\le2^{-q},
\]

which proves `(5)`. Summing over the `A_y(t)` blind rows and the `C-A_y(t)` nonblind rows gives `(7)` immediately.

If `(8)` holds, then

\[
0\le R_{q,y}(t)-A_y(t)<\frac12,
\]

so nearest-integer rounding recovers the exact blind count. Unlike the polynomial surrogate in `MC-275`, the rational function does not need to approximate OR through a high-degree polynomial: division supplies the sharp endpoint compression directly.

The distinction between polynomial and rational approximation is classical and substantial. Mahadev and de Wolf, *Rational approximations and quantum algorithms with postselection*, Quantum Information & Computation 15 (2015), 295–307, DOI `10.26421/QIC15.3-4-5`, studies rational approximation of Boolean functions as a complexity resource and its equivalence, up to constants, with postselected quantum query complexity. Modern work on rational degree likewise treats rational representation as genuinely different from polynomial degree. No novelty is claimed for the principle that rational functions can approximate Boolean thresholds far more efficiently than polynomial approximants.

The Mathia-specific point begins only after asking what denominator inversion means in the arithmetic source representation.

## 2. The denominator has an exact positive Walsh expansion

Use the Gamma/Laplace identity

\[
(1+b)^{-q}
=\frac1{\Gamma(q)}
\int_0^\infty s^{q-1}e^{-(1+b)s}\,ds.
\tag{20}
\]

Since `b=\sum_i(1-x_i)/2`,

\[
e^{-sb}
=\prod_{i=1}^{k}e^{-s(1-x_i)/2}.
\]

On `x_i=\pm1`, each factor is exactly

\[
e^{-s(1-x_i)/2}
=\frac{1+e^{-s}}2
+\frac{1-e^{-s}}2\,x_i.
\tag{21}
\]

Put

\[
a_s=\frac{1+e^{-s}}2,
\qquad
c_s=\frac{1-e^{-s}}2.
\tag{22}
\]

Then `a_s,c_s>=0` and `a_s+c_s=1`. Expanding the product in `(21)` gives

\[
e^{-sb}
=\sum_{S\subseteq[k]}a_s^{k-|S|}c_s^{|S|}x_S.
\tag{23}
\]

Substitution into `(20)` proves `(11)`–`(12)`. Because every coefficient is nonnegative and the all-positive vector has `x_S=1`, summing all coefficients gives

\[
\sum_{j=0}^k\binom kjw_{q,k}(j)
=F_q(1^k)=1,
\]

so `(13)` really is a probability law.

This positivity is also consistent with the classical Krawtchouk/Delsarte description of radial positive-definite functions on the Hamming cube already adjacent to `MC-267`–`MC-268`; no new positivity theorem is claimed.

## 3. The source-degree law is a Gamma mixture of almost-fair binomials

Equation `(23)` gives a direct probabilistic representation of `(13)`. Let

\[
S\sim\operatorname{Gamma}(q,1),
\tag{24}
\]

and, conditionally on `S=s`, let

\[
J\mid S=s\sim\operatorname{Binomial}(k,c_s).
\tag{25}
\]

Then `J` has exactly the distribution `(13)`. The Gamma Laplace transform gives

\[
\mathbb E(e^{-S})=2^{-q},
\qquad
\mathbb E(e^{-2S})=3^{-q}.
\tag{26}
\]

Because `c_S=(1-e^{-S})/2`,

\[
\mathbb E c_S=\frac12(1-2^{-q}),
\]

which proves `(14)`. By the law of total variance,

\[
\operatorname{Var}(J)
=k\,\mathbb E[c_S(1-c_S)]
+k^2\operatorname{Var}(c_S).
\tag{27}
\]

Now

\[
\mathbb E[c_S(1-c_S)]
=\frac14(1-3^{-q})
\]

and

\[
\operatorname{Var}(c_S)
=\frac14(3^{-q}-4^{-q}),
\]

which proves `(15)`.

At the live atom-sensitive choice `q>\log_2(2C)`, one has

\[
2^{-q}<\frac1{2C},
\qquad
3^{-q}\le (2C)^{-\log_2 3}.
\tag{28}
\]

From `MC-275`,

\[
\log C
=\left(\frac1{\log2}+o(1)\right)
\log y\,\log\log y,
\qquad
k\sim\frac y{\log y}.
\tag{29}
\]

Hence every fixed power of `k` is negligible against `C`, so the `k^2 3^{-q}` term in `(15)` is `o(1)`. This gives `(16)`.

For `m=o(k)`, the distance from the mean to the low-depth cutoff is

\[
\mathbb EJ-m=\left(\frac12+o(1)\right)k.
\]

Chebyshev therefore yields

\[
\Pr(J\le m)
\le
\frac{\operatorname{Var}(J)}{(\mathbb EJ-m)^2}
=O(k^{-1}),
\]

which is `(17)`.

The conclusion is stronger than a statement about one convenient integral representation. The Walsh expansion on the Boolean cube is unique. Thus the high-degree coefficient mass in `(17)` is an intrinsic property of the rational decoder when viewed through the source characters `x_S`.

## 4. Exact translation to the arithmetic source hierarchy

For the arithmetic row attached to `T`,

\[
x_p(T)=\sigma_p(T)
=\prod_{r\in T}\left(\frac pr\right).
\]

Grouping `(11)` by `|S|=j` gives

\[
F_q(x(T))
=\sum_{j=0}^{k}w_{q,k}(j)
K_j\!\left(b_y(T);k\right),
\tag{30}
\]

because the degree-`j` Walsh shell is exactly the binary Krawtchouk polynomial. Summing `(30)` over `|T|=t` and invoking the exact duality `(5)` of `MC-267` gives `(19)`.

Thus the rational blind counter is an explicit positive radial combination of **all** source-support layers. At the q required to resolve one target row among `C`, its own coefficient distribution says that source supports near `k/2`, not near `t`, carry almost all of the positive Walsh mass.

This also explains why the low rational degree is not in conflict with `MC-275`. Rational degree counts the degree of the numerator and denominator before inversion. The Mathia source hierarchy counts the Walsh degrees appearing after the function is evaluated on Boolean sign vectors. Denominator inversion is precisely the nonlinear operation that converts a degree-one statistic `b(x)` into a function whose Fourier mass reaches macroscopic degree.

## 5. Prior art and novelty boundary

The ingredients are classical: the Gamma integral for reciprocal powers, product expansion on the Boolean cube, Krawtchouk/Walsh radialization, and rational approximation of Boolean functions. Mahadev–de Wolf (2015) is a direct prior-art anchor for rational approximation as a distinct Boolean complexity measure. Iyer, Jain, Kovacs-Deak, Kumar, Schaeffer, Wang and Whitmeyer, *On the Rational Degree of Boolean Functions and Applications*, arXiv:2310.08004, further emphasizes the difference between exact rational degree, polynomial degree, and approximation phenomena for total Boolean functions.

The positive Krawtchouk coefficient viewpoint belongs to the classical harmonic analysis of the Hamming association scheme; `MC-267` and `MC-268` already treat Krawtchouk transforms, Delsarte-type positivity, and Christoffel kernels as prior art. No novelty is claimed for these components or for the elementary moment calculation `(14)`–`(15)` in isolation.

A targeted literature search through 14 September 2026 did not identify the exact combination `(7)` plus `(14)`–`(19)` for the localized Legendre-shell blind-count problem. Absence from that search is not evidence of novelty. The durable contribution claimed here is the frontier diagnosis: the first obvious rational escape from the OR approximate-degree obstruction is real at the numerator/denominator level, but the unique Walsh expansion exposes where it stores the missing information—at essentially half the full source depth.

## Boundaries and falsification tests

- **No obstruction to direct rational/arithmetic inversion.** Equation `(17)` only rules out interpreting the specific rational decoder as a low-source-depth Walsh object. A natural resolvent, transfer operator, continued fraction, or arithmetic identity that controls `(6)` without expanding the denominator remains open.
- **No universal lower bound for rational decoders.** `F_q` is an explicit decoder, not an optimality theorem over all rational functions. Another rational function may distribute its Walsh mass differently.
- **No new polynomial lower bound.** Generic polynomial pointwise approximation is already handled by `MC-275`. The present result explains how rational inversion evades that algebraic resource and why the escape is expensive in this particular source representation.
- **No claim that high coefficient mass forces high numerical contribution on every nonblind row.** On nonblind inputs the signs `x_S` can cancel. The decisive statement is at the blind vector, where every Walsh character is `+1`, so the low-depth truncation provably captures only the mass `(17)` and misses almost the entire unit response.
- **No arithmetic pseudorandomness assumption.** Every identity is finite and deterministic. The only probability law introduced in `(24)`–`(25)` is an exact representation of the positive Fourier coefficients.
- **No RH or Mertens consequence.** The transform recovers the blind count only if the full rational aggregate `(6)` can be controlled. No such arithmetic estimate is supplied.

A direct falsification of the main representation claim would be a negative Walsh coefficient in `(11)`, a failure of `(14)` or `(15)`, or a support-matched truncation whose value at `1^k` stays bounded away from zero at the atom-sensitive q. Equations `(12)`–`(17)` exclude all three.

## Consequence for the research line

`MC-275` made polynomial normalization look intrinsically too deep; `MC-276` and `MC-277` then separated representation loss from conditioning and aggregation. The present result adds a fourth distinction: **algebraic rational degree is not source-support depth**.

A reciprocal endpoint decoder can compress the blind/nonblind decision to logarithmic rational degree and even recover the exact blind count to deterministic error below one half. But when translated back into the canonical source characters, atom-sensitive accuracy moves essentially all positive coefficient mass to degrees near `k/2`. Therefore merely allowing division does not rescue the current low-support Krawtchouk hierarchy.

The genuinely new escape hatch is narrower and more concrete: find an arithmetic mechanism that treats the denominator in `(4)` as an intrinsic inverse/resolvent object rather than expanding it into source subsets. If such a mechanism exists and remains controllable on the tightly localized prime shell, it would evade both the polynomial approximate-degree barrier of `MC-275` and the half-depth expansion diagnosed here. If every natural inverse collapses back to the positive Walsh expansion `(11)`, the rational route is only a re-encoding of full-depth information.