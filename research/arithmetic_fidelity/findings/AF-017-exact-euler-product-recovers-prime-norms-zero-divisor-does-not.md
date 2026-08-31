# AF-017 — Exact Euler-product values recover prime norms; the zero divisor does not

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
Q=\{q_j\}_{j\ge 1},\qquad 1<q_1\le q_2\le\cdots,\qquad q_j\to\infty,
\]

be a locally finite multiset of positive generator norms, counted with multiplicity, and suppose its prime sum

\[
P_Q(s)=\sum_j q_j^{-s}
\]

converges absolutely for `Re(s)>sigma_0`. In that half-plane define the absolutely convergent Euler product

\[
Z_Q(s)=\prod_j(1-q_j^{-s})^{-1}.
\]

Then two analytically adjacent compressions have sharply different Arithmetic Fidelity.

1. **The exact Euler-product function is faithful to the unordered generator-norm multiset.** For `Re(s)>sigma_0`,
   \[
   \log Z_Q(s)=\sum_{m\ge1}\frac{P_Q(ms)}{m},
   \]
   and Möbius inversion gives
   \[
   \boxed{P_Q(s)=\sum_{m\ge1}\frac{\mu(m)}{m}\log Z_Q(ms).}
   \]
   Thus equality of the exact functions `Z_Q` and `Z_R` on a common convergence half-plane implies `P_Q=P_R`, and that equality determines the multisets `Q` and `R` exactly.

2. **The meromorphic zero/pole divisor is not faithful to those norms.** Grosswald and Schnitzer construct, for every choice of real numbers
   \[
   p_n\le q_n\le p_{n+1},
   \]
   the Euler product
   \[
   \zeta^*(s)=\prod_n(1-q_n^{-s})^{-1},
   \]
   which is absolutely convergent for `Re(s)>1`, has a meromorphic continuation to `Re(s)>0`, has a single simple pole at `s=1`, and has exactly the same zeros with the same multiplicities as the Riemann zeta function in `Re(s)>0`. In their proof,
   \[
   \zeta^*(s)=\phi(s)\zeta(s),
   \]
   where `phi` is holomorphic and nonvanishing in `Re(s)>0`.

Therefore one can change the generator-norm multiset while leaving the entire zero divisor, zero multiplicities, and pole location/multiplicity unchanged in the stated half-plane. The missing information lives in the **zero-free multiplicative factor**, not in the divisor.

This yields an exact category-indexed fidelity hierarchy:

\[
\text{normed prime system}
\longrightarrow
\text{exact Euler-product function}
\longrightarrow
\text{meromorphic divisor}.
\]

The first arrow is injective on unordered generator-norm multisets under the hypotheses above; the second is not.

## Derivation

### Exact Euler-product values recover the prime sum

Absolute convergence permits termwise expansion of the logarithm:

\[
\begin{aligned}
\log Z_Q(s)
&=-\sum_j\log(1-q_j^{-s})\\
&=\sum_j\sum_{m\ge1}\frac{q_j^{-ms}}{m}\\
&=\sum_{m\ge1}\frac{P_Q(ms)}{m}.
\end{aligned}
\]

In the convergence half-plane the Euler product is nonzero, so take the analytic logarithm normalized by the positive real values for sufficiently large real `s`. Applying ordinary Möbius inversion to the dilation relation gives

\[
P_Q(s)=\sum_{m\ge1}\frac{\mu(m)}{m}\log Z_Q(ms).
\]

The inversion series converges absolutely for fixed `Re(s)>sigma_0`: as `m` grows, `P_Q(ms)` and hence `log Z_Q(ms)` decay exponentially because the smallest generator norm is strictly larger than one.

For the ordinary rational primes this is the classical prime-zeta identity

\[
P(s)=\sum_p p^{-s}
=\sum_{m\ge1}\frac{\mu(m)}{m}\log\zeta(ms).
\]

So the exact values of the Euler-product function retain more than its zeros: they retain the Dirichlet/Laplace transform of the generator-norm multiset.

### The prime sum determines the norm multiset

Suppose two locally finite multisets `Q` and `R` have the same prime sum for all sufficiently large real `sigma`:

\[
\sum_{q\in Q}q^{-\sigma}=\sum_{r\in R}r^{-\sigma}.
\]

If the multisets differ, let `a>1` be the smallest norm at which their multiplicities differ; local finiteness guarantees such a first disagreement. Cancel all smaller common terms. The difference has the form

\[
0=c\,a^{-\sigma}+\sum_{x>a}c_x x^{-\sigma},
\qquad c\ne0.
\]

Choose any fixed `sigma_1>sigma_0`. Multiplying by `a^sigma` gives

\[
0=c+\sum_{x>a}c_x(a/x)^\sigma.
\]

For `sigma\ge sigma_1`, the absolute tail is dominated by

\[
\sum_{x>a}|c_x|(a/x)^{\sigma_1},
\]

which is finite by absolute convergence of the two prime sums. Each individual tail term tends to zero as `sigma\to\infty`, so dominated convergence forces the whole tail to zero. The limit is therefore `c`, a contradiction.

Hence

\[
\boxed{P_Q=P_R\quad\Longrightarrow\quad Q=R\text{ as multisets}.}
\]

Combining this with the Möbius formula proves that the exact Euler-product function is faithful to the unordered list of generator norms. It does **not** recover any additional labels or provenance attached to equal norms.

### Passing to the divisor destroys that fidelity

Grosswald--Schnitzer give an unusually strong matched control. Starting with the rational primes `p_n`, choose arbitrary real `q_n` satisfying

\[
p_n\le q_n\le p_{n+1}.
\]

The resulting Euler product `zeta*` can use genuinely non-prime norms, yet their Theorem 1 proves that in `Re(s)>0` it has the same zeros as `zeta`, with the same multiplicities, and only one simple pole at `s=1`. Their proof writes

\[
\zeta^*(s)=\phi(s)\zeta(s)
\]

with `phi` holomorphic and nonzero throughout that half-plane.

Thus the divisor map

\[
F\longmapsto\operatorname{div}(F)
\]

quotients out precisely the freedom to multiply by zero-free holomorphic factors. In this class that freedom is large enough to alter every Euler-product generator within a prime-gap interval while leaving the divisor unchanged.

This is stronger than saying that zeros are an incomplete summary in principle. It supplies an explicit same-destination control family at the exact analytic layer relevant to many spectral/RH interpretations.

## Arithmetic-equivalence boundary

The result also sharpens how arithmetic equivalence should be interpreted inside Arithmetic Fidelity.

Equality of Dedekind zeta functions for non-isomorphic number fields is a classical example of lost **arithmetic provenance**. But a Dedekind zeta function still has an Euler product by prime-ideal norms. In its absolute-convergence half-plane, the same Möbius/prime-sum argument recovers the multiset of those local norm factors. Therefore the slogan "the zeta function forgets the primes" is too coarse.

There are at least two different losses:

1. **exact Euler-product function:** retains the multiset of local generator norms but may forget how those local factors are assembled inside a richer upstream arithmetic object;
2. **zero/pole divisor:** can forget even the generator-norm multiset, because zero-free analytic factors are discarded.

Perlis-type arithmetic equivalence witnesses the first kind of non-faithfulness; Grosswald--Schnitzer witness the second.

## Why this matters for Arithmetic Fidelity

AF-015 established that bare multiplication preserves abstract prime type while forgetting the ordinary rational-prime norm. The accepted Beurling/arithmetic-equivalence clue then asked for a concrete destination category in which an independently defined enrichment could be audited against matched controls.

The Euler-product category supplies exactly such a case. Adding the norm and retaining the **full Euler-product function** breaks the prime-permutation ambiguity strongly enough to recover the unordered norm multiset. But the very next canonical compression -- retaining only zeros and poles -- destroys that gain again.

This gives a practical stopping rule for zero-based RH mechanisms. If the proposed destination is determined only by zero locations and multiplicities, then across the Grosswald--Schnitzer control class it cannot certify the ordinary rational-prime norm system. Any prime-specific conclusion needs additional retained analytic structure that fixes or constrains the zero-free factor: exact values, Euler coefficients, a normalization plus a sufficiently rigid functional equation/growth class, or another independently justified datum.

The important point is not that one should always retain the entire zeta function. It is that **"spectral data = zeros" and "Euler-product data" are mathematically different fidelity layers** and must not be treated as interchangeable.

## Prior art and novelty assessment

The underlying mathematics is classical.

The prime-zeta relation

\[
\log\zeta(s)=\sum_{m\ge1}\frac{P(ms)}m,
\qquad
P(s)=\sum_{m\ge1}\frac{\mu(m)}m\log\zeta(ms),
\]

is standard and appears in the classical literature on the prime zeta function, including Fröberg's 1968 treatment. The multiset-uniqueness argument above is the elementary uniqueness of a positive discrete Dirichlet/Laplace sum.

Grosswald and Schnitzer's 1978 theorem is direct prior art for changing Euler-product generators while preserving the complex zeros of `zeta`; no novelty is claimed for that construction. Perlis' arithmetic-equivalence theorem is likewise classical.

The Arithmetic Fidelity contribution is the **boundary placement**: these results identify two adjacent compression categories with opposite answers to the same discriminator question. Exact Euler-product values are faithful to the unordered prime-norm multiset, while the meromorphic divisor is not. This resolves a concrete instance of the line's category-indexed admissibility problem without claiming a new zeta theorem.

## Boundaries and failure modes

- The recovery theorem assumes Euler factors exactly of the form `(1-q^{-s})^{-1}`, local finiteness of the norm multiset, and an absolute-convergence half-plane. More general local factors require their own identifiability analysis.
- Recovery is of the **multiset of norms**, not labels, order, residue fields, splitting provenance, field structure, additive structure, or any richer relation among the generators.
- Equality of full analytic functions is much stronger than equality of zeros, equality of zero statistics, agreement of finitely many values, or matching asymptotics.
- The Grosswald--Schnitzer same-zero theorem is used only in `Re(s)>0`, exactly where their theorem provides the continuation and divisor comparison. No claim is made here that the modified products share every global analytic property of `zeta`.
- Their controls generally do not retain the Riemann zeta functional equation. A downstream category that genuinely retains and uses a rigid functional equation, growth normalization, Euler coefficients, or exact function values is strictly richer than the bare divisor category and must be audited separately.
- A nonvanishing factor can change the residue at the pole even while preserving its location and order. Therefore a "divisor" claim must not silently include residue data.
- This finding has no direct consequence for RH. It constrains what can be inferred from a destination representation that has already discarded the zero-free analytic factor.

## Decisive audit test

For any proposed prime-specific mechanism whose final retained data are spectral zeros or a meromorphic divisor:

1. state whether the destination retains the full analytic function or only its divisor/zero set;
2. if only the divisor is retained, apply a Grosswald--Schnitzer-type matched control and check whether the destination remains unchanged while the Euler-product norm system changes;
3. if the mechanism claims to escape by retaining extra analytic data, specify exactly which data fix or restrict the zero-free factor and prove that this enriched destination still separates the ordinary rational-prime norm system from matched generalized-prime controls.

A same-divisor control with different generator norms kills rational-prime norm recovery at that layer. Equality of the full Euler-product function does not: under the hypotheses above it forces equality of the norm multiset.

## Consequence for the line

Treat **full analytic value data** and **zero-divisor data** as distinct compression categories.

The accepted Beurling/arithmetic-equivalence frontier is resolved for this concrete category: the norm enrichment survives into the exact Euler-product function, but not into the divisor. Future category-indexed audits should therefore locate the precise stage at which a proposed RH representation passes from Euler/local-factor information to a coarser spectral or divisor object and identify what zero-free/provenance information is discarded there.