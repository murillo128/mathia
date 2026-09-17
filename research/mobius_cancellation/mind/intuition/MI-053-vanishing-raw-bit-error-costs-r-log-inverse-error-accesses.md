# MI-053 — Vanishing raw-bit error costs `R log(1/error)` discrimination divergence

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-source-entropy-prices-low-energy-dephasing.md), [MC-344](../../findings/MC-344-bit-flip-source-readout-capacity.md), [MC-345](../../findings/MC-345-adaptive-source-query-feedback-capacity.md), [MC-346](../../findings/MC-346-adaptive-raw-bit-reliability-overhead.md), and [MC-347](../../findings/MC-347-variable-fidelity-source-query-divergence-budget.md).

The linear capacity budget and the cost of reliable raw-coordinate reconstruction are different statements. MC-344--MC-345 show that at fixed BSC crossover `q<1/2`, even fully adaptive noisy coordinate access carries at most `c(q)` mutual information per actual query. This forces `Omega(R)` expected accesses for a fixed nontrivial source-information target, but does not make positive noise fatal.

MC-346 sharpens the regime in which the desired downstream operation requires the individual source bits to become increasingly reliable. At fixed BSC quality, if the final decoder has average coordinate error `bar p`, pairwise change-of-measure across neighboring source states forces

`E[tau] = Omega_q(R log(1/bar p))`.

Fixed error and vanishing error therefore have different asymptotic prices: polynomially small error costs `Omega(R log R)`, while repeated sampling with majority decoding matches the logarithmic order.

MC-347 identifies the invariant behind that query-count theorem. Allow an adaptive controller to choose, at each history, an arbitrary raw-coordinate observation kernel `K_t(.|s)`. A high-fidelity query can carry much more discrimination than a weak one, so nominal access count can be reparameterized by changing measurement quality. Define the accumulated directional discrimination budget

`mathfrak D = E sum_(t<=tau) D(K_t(.|X_(J_t)) || K_t(.|-X_(J_t)))`.

Then the same reciprocal-source geometry forces

`mathfrak D = Omega(R log(1/bar p))`

as `bar p -> 0`, with explicit even/odd-rank constants in MC-347. The fixed BSC result is recovered exactly from `mathfrak D=D_q E[tau]`.

For endpoint dephasing, the practical audit is therefore two-stage. Translate the target gain into the source-coordinate resolution actually required. If a fixed gain tolerates constant source uncertainty, the linear mutual-information/capacity obstruction is the relevant currency. If approaching the matched-filter floor forces `bar p->0`, capacity alone understates the cost and the accumulated pairwise discrimination divergence must grow logarithmically with inverse error.

This prevents an artificial escape in which a protocol appears to beat an access lower bound simply by declaring fewer, more accurate measurements. Stronger experiments are allowed, but their extra distinguishability is charged automatically by KL. Conversely, if every permitted raw query has discrimination at most `D_*`, then `mathfrak D<=D_* E[tau]` and the divergence theorem immediately restores a query-count lower bound.

**Boundary.** This is a theorem for adaptive **raw-coordinate** experiments. A coded observation depending jointly on many source bits has a different alternative-hypothesis graph and requires its own information/reliability accounting. The result does not prove that a Möbius mechanism must recover individual bits, nor that `R log(1/error)` is universal for arbitrary arithmetic observables. Its reusable content is the separation between aggregate capacity and vanishing-error reliability, with discrimination divergence rather than query count as the invariant currency when measurement fidelity varies.