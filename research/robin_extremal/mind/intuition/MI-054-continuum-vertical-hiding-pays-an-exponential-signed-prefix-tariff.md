# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff, with predictor norm, capacity and KV controlling different layers

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-216](../../findings/RE-216-off-center-binomial-synthesis-lifts-constructive-vertical-budget.md). The compact-support Fourier/spectral-gap geometry and prime-count estimates are classical; the Mathia content is their pullback to separated ordinary-prime Euler repairs at selector scale.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then the gap forces an exponentially large weighted cumulative primitive, which becomes a normalized signed ordinary-prime prefix after arithmetic pullback.

RE-210--RE-213 optimize the leading exponential converse and show that nonnegative compact windows cannot beat unit exponent. RE-215 sharpens the source-independent realization bound to

`R >>_H (1-epsilon)e^(HT)/(HT log(HT))`,

so bounded ordinary-prime multiplicity implies

`HT_Q <= (1/2)log Q + log log Q + log log log Q + O_H(1)`.

The leading half-logarithmic ceiling is therefore a carrier-capacity obstruction. KV fidelity remains a different currency: it excludes the exact endpoint and enforces a stronger deficit below it.

RE-216 now sharpens the **constructive** side without changing the ordinary-prime realization. The previous centered binomial predictor paid coefficient-variation exponent `12 log 2=8.3177...`. Moving the expansion center and using an off-center binomial synthesis lowers the proven exponent to at most `6.08073274`. At `H=log 8`, the explicit hiding range improves from `c<0.0289079...` to `c<0.0395410...`, about a 36.8% increase, while the arithmetic carrier mechanism is unchanged.

This separates another resource that had been partially conflated with source capacity: **spectral predictor/Wiener norm is not prime-placement capacity**. A poor analytic representation can consume more signed-prefix budget than the arithmetic realization intrinsically requires. Changing basis or expansion center can therefore improve a constructive range materially without providing new arithmetic information or weakening the converse-side carrier bound.

The reusable audit is now four-level. First identify the continuum observability exponent. Second optimize the analytic predictor or representation norm used to realize the desired spectral profile. Third compare the resulting signed-prefix demand with raw source capacity. Only after those are exhausted should finer arithmetic fidelity such as KV be credited with the remaining exclusion. A convenient predictor constant is not structural merely because the unit exponential rate is.

The fixed-constant gap remains substantial. At `H=log 8`, explicit hiding is proved only for `c<0.0395410...`, while raw bounded-multiplicity capacity forbids fixed `c>1/(2H)=0.240449...`. Progress should therefore target the predictor/source-norm mismatch, stronger signed-prefix realization, a sharper source-independent converse inside that gap, or a different architecture rather than further positive-window shaping alone.

**Boundary.** RE-216 does not prove `6.08073274` optimal, alter the unit exponential converse, change the leading capacity threshold, or remove the need for KV at the exact endpoint. The whole analysis remains conditional on the separated ordinary-prime bounded-multiplicity architecture and selector-scale normalization; different carriers or nonseparated designs are outside it.