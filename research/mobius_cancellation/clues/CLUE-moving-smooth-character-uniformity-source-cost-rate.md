---
id: CLUE-mobius-cancellation-moving-smooth-character-uniformity-source-cost-rate
type: research-clue
status: resolved
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md
  - research/mobius_cancellation/findings/MC-373-explicit-moving-order-burgess-gives-effective-near-endpoint-rate.md
  - research/mobius_cancellation/findings/MC-241-smooth-conductor-blind-support-divergence.md
---

# Can explicit moving-parameter smooth character sums quantify the MC-377 source-cost divergence?

## Observation

`MC-377` proves that the common lower-prime source radical `P` of an exact endpoint must escape every fixed power of the shell scale `y`, but the proof is intentionally qualitative: after assuming `P<=y^A`, the smoothness exponent, the Cochrane--Granville--Zheng character-sum parameters, the Selberg cutoff, and the final saving all depend on the fixed constant `A`. The finding therefore gives `log P/log y -> infinity` with no rate.

The underlying Cochrane--Granville--Zheng proof exposes considerably more parameter structure than the fixed-parameter corollary used in `MC-377`. In their Theorem 3, for `f(x)=x` and `g(x)=0`, the differencing depth `k` enters through `D=2^{k+1}` and an exponent of size `eta asymp 4^{-k}`, together with the explicit admissibility conditions `k 2^k << log log Q*`, `Q* >= (log Q)^{12D}`, and `k < N^eta`. The proof of their Theorem 4 chooses `k` on the scale `1/delta` after factoring a smooth modulus. Their Remark 1 also states that the method allows `delta` to move with the modulus.

There is, however, a uniformity point that cannot be skipped. If `k` is allowed to grow, the displayed Theorem 3 condition `k 2^k << log log Q*` must be reconciled with the broader moving-`delta` discussion in Remark 1, and the implicit constants in the theorem cannot simply be treated as fixed. This is analogous to the issue resolved explicitly for moving Burgess order in `MC-373`, but the constant bookkeeping is different.

## Research question

Redo only the `f(x)=x`, `g(x)=0` part of the smooth-modulus argument with all dependence on the moving differencing depth retained, and feed that explicit estimate into the source-incidence kernel plus Selberg/Bombieri frame proof of `MC-377`.

The concrete target is a uniform implication of the following shape. If an exact endpoint has rank `R` and common source radical `P<=y^{A(y)}`, can one rule this out throughout a genuinely growing range of `A(y)` determined by the two independent costs already visible in the proof: the `O(A^2)` codimension needed to kill rough source columns, and the exponential-in-`A` loss of the smooth character-sum differencing depth? A plausible first theorem surface is a condition comparable to

\[
A(y)^2=o(R),
\qquad
A(y)2^{C A(y)}=o(\log\log y)
\]

for some absolute `C`, which would already turn the qualitative divergence of `MC-377` into an explicit iterated-logarithmic source-cost lower bound. The displayed condition is a research target, not an established consequence.

## Why it may matter

`MC-377` has already removed every fixed polynomial common-radical escape. The next useful distinction is therefore quantitative: whether the endpoint can survive with a source exponent that grows arbitrarily slowly, or whether the same smooth-subspace mechanism forces a definite rate tied to `R` and `y`.

An effective rate would make the surviving source package substantially more rigid and could interact with the independent rank, incidence, and minimum-conductor constraints elsewhere in the endpoint branch. A negative result is also valuable if it identifies the exact parameter in the smooth-character theorem that prevents any rate from being extracted. As in `MC-373`, the point is not a better black-box asymptotic but an audited moving-parameter transfer through the actual prime-frame proof.

## Decisive test

Start from Cochrane--Granville--Zheng Theorem 3 and the factorization step in the proof of Theorem 4 rather than from fixed-`delta` Corollary 2. Specialize to primitive squarefree quadratic characters arising as pair products of endpoint source characters. Track explicitly the dependence on `k` of the complete-sum constants, the differencing inequalities, the exceptional integer `Delta(x,0,k)`, and the final normalized character-sum bound.

In parallel, redo the `MC-377` kernel step with moving `A`: kill source-incidence columns from primes above a threshold `y^{c/A}` and from primes dividing the moving exceptional integer, and retain the resulting codimension rather than hiding it in `O_A(1)`. Then propagate the moving character-sum saving through the Selberg cutoff. The diagonal term must be kept as `O(1/b)` after normalization when the cutoff exponent `b=b(y)` tends to zero, rather than reused as the fixed-parameter `O_A(1)` term from `MC-377`.

Keep the direction only if all constants can be bounded uniformly enough to make the frame upper bound `o(H/R)` for some explicit growing range `A=A(y)`. Narrow or reject it if the theorem's moving-parameter constants, exceptional-prime cost, or Selberg diagonal consume the gain. In particular, do not infer the wider uniformity claimed informally in Remark 1 until it is shown to be compatible with the displayed `k 2^k` condition used in Theorem 3.

## Evidence boundary

No effective lower bound on `log P/log y` is established here. `MC-377` remains the canonical theorem and proves only divergence. Cochrane--Granville--Zheng's published arXiv statement gives a fixed-parameter theorem plus a moving-parameter discussion, but the required uniform constant propagation through the specialized proof and through Mathia's prime-frame argument has not yet been completed.

The candidate iterated-logarithmic range above is therefore only a falsifiable theorem surface. This clue does not strengthen `MC-377`, does not assert that Remark 1 is incorrect, and does not imply any estimate for `M(x)`.

## Research disposition

Outcome: supported and narrowed

Resolved by:
- [[research/mobius_cancellation/findings/MC-378-moving-smooth-frame-forces-iterated-log-source-cost-rate.md]]

The moving-parameter audit succeeds in a conservative range. After killing source columns from primes above `y^{c/A}` and from the moving Cochrane--Granville--Zheng exceptional integer, the surviving mode space has codimension `O(A^2)`. Their displayed Theorem 3 dependence gives a character-sum saving `sigma_A >= 2^{-C_1 A}` provided `A 2^{C_0 A}=o(log log y)` for a sufficiently large absolute `C_0`. The imprimitive-character divisor loss is smaller in the same range, and choosing the Selberg cutoff exponent `b=sigma_A/100` keeps the diagonal cost at `O(sigma_A^{-1})` while retaining a power-saving off diagonal.

Consequently an exact endpoint cannot have `P<=y^{A(y)}` whenever

\[
A(y)^2=o(R),
\qquad
A(y)2^{C_0A(y)}=o(\log\log y).
\]

One explicit non-optimized corollary is

\[
\frac{\log P}{\log y}
\ge
c\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
\log\log\log y
\right\}
\]

for some absolute `c>0` and all sufficiently large exact endpoints. The clue is resolved at this proof rate only. The `log log log y` ceiling comes from the explicit `k2^k` tariff in Theorem 3 and is not claimed to be optimal; no estimate for `M(x)` follows.