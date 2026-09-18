# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff, with capacity and KV controlling different endpoint layers

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-215](../../findings/RE-215-continuous-kaiser-window-sharpens-prime-count-capacity-bound.md). The compact-support Fourier/spectral-gap geometry and prime-count estimates are classical; the Mathia content is their pullback to separated ordinary-prime Euler repairs at selector scale.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then the gap forces an exponentially large weighted cumulative primitive, which becomes a normalized signed ordinary-prime prefix after arithmetic pullback.

RE-210--RE-213 optimize the leading exponential rate and show that nonnegative compact windows cannot beat unit exponent. RE-214 used a twofold Kaiser test to make the required tail norm integrable and obtained `R>>e^(HT)/(HT)^2`. RE-215 shows that the square is not the right subexponential price: subtracting the endpoint value before normalization gives the continuous Kaiser--Bessel window, whose transform is a difference of nearby sinc terms. Their first tails cancel and one obtains

`R >>_H (1-epsilon)e^(HT)/(HT log(HT))`.

Bounded ordinary-prime multiplicity independently gives `R<<sqrt(Q)`. Hence source capacity alone forces

`HT_Q <= (1/2)log Q + log log Q + log log log Q + O_H(1)`.

The leading half-logarithmic ceiling is unchanged, but its source-independent boundary layer is significantly thinner than RE-214 showed. This is a useful separation: **the unit exponential rate is structural, while the polynomial/logarithmic correction can depend on how efficiently the positive test realizes the spectral gap.**

KV fidelity remains a different currency. RE-213 proves `((1/2)log Q-HT_Q)/V(Q)->+infinity`, so it excludes the exact endpoint and enforces a much thicker deficit below it. Carrier cardinality determines the leading ceiling above the endpoint; optimized window geometry narrows the source-independent second-order layer; arithmetic fidelity controls the endpoint and subendpoint regime.

The reusable audit is therefore three-level. First identify the continuum observability exponent. Then compare its subexponential realization cost with raw source capacity. Only after those are exhausted should finer arithmetic fidelity be credited with the remaining exclusion. Using a strong PNT/KV input where carrier capacity already suffices hides the real mechanism; treating one convenient window's polynomial loss as structural can exaggerate the capacity gap.

**Boundary.** The capacity obstruction assumes the separated ordinary-prime bounded-multiplicity architecture and selector-scale normalization of RE-209--RE-215. RE-215 does not prove `A log A` optimal, improve the constructive lower range, or remove the need for KV at the exact endpoint. Unbounded multiplicity, different carriers, nonfixed separation or a fundamentally different hiding architecture remain outside this result.