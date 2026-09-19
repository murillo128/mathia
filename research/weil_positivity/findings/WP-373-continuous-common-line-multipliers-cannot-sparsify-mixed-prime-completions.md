---
id: WP-373
title: Continuous common-line multipliers cannot sparsify the mixed-prime positive completion
branch: weil_positivity
status: supported
kind: common-line-continuous-multiplier-mixed-prime-sparsification-obstruction
claim_strength: exact no-go for scalar translation-invariant common-line filters with continuous Fourier symbol that erase all mixed two-prime modes of the WP-372 completion while retaining any nonzero prime-power lane, together with an exact finite-cutoff control
created: 2026-09-19
related: [WP-098, WP-272, WP-283, WP-296, WP-372]
clues: [CLUE-weil-positivity-mixed-prime-positive-completion-selector-quotient]
prior_art:
  - classical density of irrational two-generator additive subgroups of the real line
  - continuity of Fourier transforms of L1 kernels and Fourier-Stieltjes transforms of finite measures
  - classical smooth interpolation on finite subsets of the frequency line
---

# WP-373 — Continuous common-line multipliers cannot sparsify the mixed-prime positive completion

## Claim

`WP-372` shows that the positive critical one-prime rays can be completed with finite total mass once mixed-prime Fourier modes are allowed. For its explicit product completion, the coefficient of a reduced two-prime character

\[
r=2^m3^n,
\qquad m,n\in\mathbb Z\setminus\{0\},
\tag{1}
\]

is

\[
\widehat\mu_C(2^m3^n)
=C^{-1}(\log2)(\log3)2^{-|m|/2}3^{-|n|/2},
\tag{2}
\]

which is nonzero for every such pair.

Restrict the prime torus to Mathia's common prime-log line

\[
\theta_p=t\log p.
\tag{3}
\]

Then (1) becomes the scalar frequency

\[
\lambda_{m,n}=m\log2+n\log3.
\tag{4}
\]

The set

\[
\Lambda_{2,3}^{\rm mix}
:=\{m\log2+n\log3:m,n\in\mathbb Z\setminus\{0\}\}
\tag{5}
\]

is dense in `R`. Consequently, if a scalar translation-invariant operator on the common line is represented on characters by a **continuous ordinary Fourier multiplier**

\[
T(e^{i\lambda t})=M(\lambda)e^{i\lambda t},
\qquad M:\mathbb R\to\mathbb C\text{ continuous},
\tag{6}
\]

and it erases every mixed two-prime mode of the `WP-372` completion, then

\[
M(\lambda)=0
\qquad(\lambda\in\Lambda_{2,3}^{\rm mix}),
\tag{7}
\]

so continuity forces

\[
\boxed{M\equiv0.}
\tag{8}
\]

Hence no nonzero continuous scalar common-line multiplier can take the `WP-372` positive completion, delete all mixed-prime modes, and retain even one nonzero prime-power arithmetic mode. The obstruction already appears using only the primes `2` and `3`; adding the rest of the prime system cannot repair it.

This no-go is genuinely infinite. For every **finite** collection of mixed frequencies to erase and pure prime-power frequencies to retain, there exists `M in C_c^infty(R)` taking exactly the prescribed `0/1` values. Its inverse Fourier transform is Schwartz, so every finite truncation admits an arbitrarily regular exact convolution selector. What fails is passing to the full dense mixed spectrum while keeping a continuous symbol.

**Classification:** `EXACT-DERIVED + NEGATIVE-OBSTRUCTION + MIXED-PRIME-COMMON-LINE-DENSITY + CONTINUOUS-SCALAR-MULTIPLIER-NO-GO + FINITE-CUTOFF-MATCHED-CONTROL + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + SELECTOR-BOUNDARY/NOT-WEIL-POSITIVITY + NO-GRAND-NOVELTY-CLAIM`.

## 1. Two mixed prime coordinates already generate a dense common-line spectrum

The ratio `log 2/log 3` is irrational. Otherwise there would be nonzero integers `a,b` with

\[
a\log2=b\log3,
\tag{9}
\]

hence `2^a=3^b`, contradicting unique factorization.

It follows by the elementary irrational-approximation argument that the additive subgroup

\[
\mathbb Z\log2+\mathbb Z\log3
\tag{10}
\]

is dense in `R`. The restriction `m,n!=0` does not destroy density. Indeed irrational approximation gives arbitrarily small nonzero combinations

\[
\delta=r\log2+s\log3,
\qquad r,s\in\mathbb Z\setminus\{0\}.
\tag{11}
\]

For a target `x!=0` and tolerance `epsilon>0`, choose such a `delta` with

\[
0<|\delta|<\min(\epsilon,|x|),
\tag{12}
\]

then choose a nearest integer `k` to `x/delta`. It is nonzero and satisfies

\[
|x-k\delta|\le\frac{|\delta|}{2}<\epsilon.
\tag{13}
\]

But

\[
k\delta=(kr)\log2+(ks)\log3
\tag{14}
\]

has both integer coefficients nonzero. For `x=0`, (11) itself gives mixed frequencies arbitrarily close to zero. This proves the density of (5).

There is also no accidental collision between a mixed frequency (4) and a pure prime-power frequency `ell log p` with `ell!=0`. Such a collision would exponentiate to

\[
2^m3^n=p^\ell,
\tag{15}
\]

which unique factorization forbids when both `m` and `n` are nonzero. Thus the obstruction below is not caused by identifying a desired pure mode with an unwanted mixed mode. It is caused by **topological accumulation** of unwanted modes around every common-line frequency.

## 2. Continuity kills every scalar selector

For the `WP-372` product completion, (2) is nonzero for every `m,n!=0`. A scalar Fourier multiplier that deletes those mixed modes must therefore satisfy (7).

Since `Lambda_{2,3}^{mix}` is dense and `M` is continuous, for any `lambda in R` choose a sequence `lambda_j in Lambda_{2,3}^{mix}` with `lambda_j -> lambda`. Then

\[
M(\lambda)
=\lim_{j\to\infty}M(\lambda_j)
=0.
\tag{16}
\]

This proves (8).

In particular, for every prime `p` and every nonzero integer `ell`,

\[
M(\ell\log p)=0.
\tag{17}
\]

So the desired two-stage operation

\[
\text{positive mixed completion}
\quad\longrightarrow\quad
\text{regular common-line scalar selector}
\quad\longrightarrow\quad
\text{sparse prime-power carrier}
\tag{18}
\]

cannot preserve even a single arithmetic lane unless the second arrow leaves the class (6).

The regularity assumption covers the most ordinary convolution responses. If `T f=K*f` with `K in L^1(R)`, then `M=\widehat K` is continuous and vanishes at infinity. If `T` is convolution by a finite signed or complex Borel measure, its Fourier-Stieltjes transform is again continuous. Both therefore obey the no-go.

The statement is intentionally not extended to every translation-invariant distributional operator. A general distributional multiplier need not be represented by an ordinary continuous function, and (8) cannot be inferred in that larger category without additional hypotheses.

## 3. Finite truncations pass an exact smooth matched control

Fix finite disjoint sets

\[
E=\{\lambda_1,\ldots,\lambda_a\}
\subset\Lambda_{2,3}^{\rm mix}
\tag{19}
\]

of mixed frequencies to erase and

\[
K=\{\kappa_1,\ldots,\kappa_b\}
\tag{20}
\]

of pure prime-power frequencies to retain. By the no-collision observation after (15), all points in `E union K` can be taken distinct after removing repetitions.

Choose pairwise disjoint small intervals around those finitely many points and smooth compactly supported bump functions `psi_j` satisfying

\[
\psi_j(\kappa_j)=1
\tag{21}
\]

and supported away from every point of `E` and from the other prescribed points. Then

\[
M_{E,K}(\lambda)=\sum_{j=1}^b\psi_j(\lambda)
\tag{22}
\]

lies in `C_c^infty(R)` and satisfies exactly

\[
M_{E,K}|_E=0,
\qquad
M_{E,K}|_K=1.
\tag{23}
\]

Its inverse Fourier transform is Schwartz. Thus not only does every finite truncation admit a selector; it admits one with a very regular convolution kernel.

This matched control rules out a merely local algebraic incompatibility. The failure occurs only when the complete infinite mixed spectrum is imposed. It also shows why finite-prime or bounded-frequency numerics can be misleading: they can realize the desired keep/erase pattern perfectly while no locally uniform continuous limit can realize the infinite selector. Any locally uniform limit that vanished on all mixed frequencies would vanish everywhere by (16).

## 4. Adversarial boundary and relation to earlier no-go results

The theorem is deliberately narrow enough that its hypotheses can be falsified.

First, if continuity is dropped, an abstract pointwise symbol can assign `0` to every mixed frequency and `1` to selected pure frequencies. The resulting symbol is necessarily discontinuous at every retained point because mixed frequencies accumulate there. This is not excluded by the present theorem; it is evidence that any surviving scalar quotient must pay with genuinely rough/discontinuous spectral behavior rather than inherit positivity from an ordinary regular convolution response.

Second, non-scalar, nonlinear, source-dependent, or genuinely geometric quotient mechanisms are outside (6). `WP-098` already closes a different natural class: same-algebra positive unital maps preserving the coordinate unitaries cannot erase mixed products because the preserved unitaries enter the multiplicative domain. The present argument assumes neither positivity nor unitality of the selector and works only after restriction to the common line, so it is not a restatement of `WP-098`.

Third, `WP-272` concerns continuity constraints for a pole-completed carrier, `WP-283` uses Paley-Wiener/Jensen-type zero-density restrictions for compact-memory filters against a zeta-zero screen, and `WP-296` classifies multiplicative shift-equivariant nonlocal couplings as Dirichlet convolution. None gives the density obstruction (5)-(8). Conversely the present theorem makes no claim about zeta-zero screens, compact support in physical space, or multiplicative equivariance.

The ingredients here are classical: irrational two-generator density, Fourier-transform continuity, and smooth interpolation on finite sets. The contribution is their exact application to the source-forced mixed sector exposed by `WP-372`. No broad theorem novelty is claimed.

## 5. Consequence for the Weil-positivity search

`WP-372` changed the positivity budget decisively: mixed-prime correlations can reduce the critical scalar completion cost from a divergent additive tax to one finite shared mass. A natural next hope was to accept that positive completion first and then recover the arithmetic prime-power selector by a regular common-line response. Equations (5)-(8) close that hope for the entire continuous scalar multiplier class.

Therefore a viable descendant of `WP-372` must do at least one of two harder things. It can retain a source-forced mixed-prime sector in the final global pairing and show that the full arithmetic-plus-archimedean structure still matches a Weil criterion, or it can supply a quotient/response outside the continuous scalar common-line class -- for example a non-scalar, nonlinear, source-dependent, or intrinsically rough construction -- together with its **own independent geometric positivity theorem**.

Nothing here supplies the missing Gamma/polar terms or a Weil positivity proof. The result is a negative boundary: it prevents the finite-mass mixed completion from being converted into the desired sparse arithmetic object by the most regular scalar post-processing route, while the finite-cutoff control shows exactly where that obstruction becomes global.
