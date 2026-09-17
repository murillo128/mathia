# MI-053 — Vanishing raw-bit error costs `R log(1/error)` noisy accesses

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-source-entropy-prices-low-energy-dephasing.md), [MC-344](../../findings/MC-344-bit-flip-source-readout-capacity.md), [MC-345](../../findings/MC-345-adaptive-source-query-feedback-capacity.md), and [MC-346](../../findings/MC-346-adaptive-raw-bit-reliability-overhead.md).

The linear BSC capacity budget and the cost of reliable raw-coordinate reconstruction are different statements. MC-344--MC-345 show that at fixed crossover `q<1/2`, even fully adaptive noisy coordinate access carries at most `c(q)` mutual information per actual query. This forces `Omega(R)` expected accesses for a fixed nontrivial source-information target, but does not make positive noise fatal.

MC-346 sharpens the regime in which the desired downstream operation requires the individual source bits to become increasingly reliable. If the final decoder has average coordinate error `bar p`, then adjacent source states differing in one bit must become increasingly distinguishable. A change-of-measure argument summed over cube edges gives

`E[tau] >= const * (R/D_q) [log(const/bar p)]_+`.

Thus fixed error and vanishing error have different asymptotic prices. At fixed `q`, `bar p=Theta(1)` is compatible with `Theta(R)` access, while `bar p->0` costs `Omega_q(R log(1/bar p))`; polynomially small error costs `Omega(R log R)`. Repeated sampling with majority decoding has the same order, so the logarithmic overhead is a real reliability tariff rather than an artifact of the proof.

For endpoint dephasing, the practical audit is to translate the target gain into the coordinate error actually required. If a fixed gain tolerates constant source uncertainty, the linear capacity theorem is the relevant obstruction. If approaching the matched-filter floor forces `bar p->0`, linear information alone understates the cost and the reliability divergence must be charged.

**Boundary.** This is a theorem for adaptive raw-coordinate BSC access, not for arbitrary coded measurements or arithmetic observables. It does not prove that a Möbius mechanism needs bitwise recovery, nor that `R log(1/error)` is universal outside this acquisition primitive. Its reusable content is the separation between fixed-quality capacity and vanishing-error reliability.