# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-211](../../findings/RE-211-blackman-window-powers-strengthen-the-separated-vertical-kv-ceiling.md). The compact-support Fourier/spectral-gap geometry is classical; the Mathia content is its exact pullback to separated ordinary-prime Euler repairs at selector scale under KV source fidelity.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs only when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then uncertainty is no longer a rank question: the gap forces an exponentially large weighted cumulative primitive.

RE-209 identifies the physical primitive after pulling the generic harmonic statement back to ordinary primes. The exponentially weighted primitive is exactly a signed prime-count prefix, and partial summation converts it into a Chebyshev-prefix excursion. Thus the continuum observation width is priced in a source currency that fixed Korobov--Vinogradov fidelity constrains.

RE-210 sharpens the repeated-uniform test to the exact optimized sinc-tail rate `gamma_*=0.5979019108...`. RE-211 shows that this rate is not extremal over nonnegative compact-support tests: a normalized Blackman base window, followed by the same convolution-power construction, gives the certified rate

`log R >= (gamma_B+o(1)) H T`, with `gamma_B=0.7415820315...`.

For selector-scale ordinary-prime repairs preserving every fixed KV envelope, `T_Q=c log Q` must therefore satisfy

`c < 1/(2 gamma_B H)`.

At the current gap `H=log 8`, the universal ceiling is `0.3242381331...`, while explicit ordinary-prime hiding is constructed below `0.0289079...`. The continuum vertical problem is therefore genuinely two-sided: ordinary primes can pay an exponential hiding cost for a positive logarithmic-height range, but beyond a larger explicit range the required signed prefix violates the source envelope.

The reusable distinction is between **local spectral rank and global continuum source cost**. A finite panel asks whether source vectors are distinguishable at sampled phases; a continuum interval plus support separation asks how much weighted signed prefix must be generated to approximate an entire Fourier profile. The latter can be coercive even though every finite panel remains aliasable.

The obstruction-side constant is a window-design quantity, not a property of sinc. For a nonnegative probability density `w` supported on `[-1,1]`, the convolution-power mechanism is governed by the tradeoff between how far one must move in frequency before `|w_hat|` is uniformly small and the logarithmic depth of that tail. RE-211 proves that shaping the base window improves this tradeoff, while the triangular-window negative control shows that mere smoothing/self-convolution does not.

The remaining gap is itself in the correct currency. On the obstruction side, determine or tightly bound the compact-support extremal functional `Gamma(w)=sup_a[-log sup_{|x|>=a}|w_hat(x)|]/a`. On the constructive side, a better repair must directly control signed weighted prefixes rather than merely total variation. Either improvement changes the actual source budget rather than the nominal number of vertical samples.

**Boundary.** The coercive theorem assumes a fixed pre-repair logarithmic gap, ordinary-prime edits with the stated integer multiplicities, selector-scale local mass and fidelity to every fixed KV envelope. The numerical `gamma_B` is a conservative certified rate from one classical Blackman window, not an optimal compact-support constant. The result does not prove Robin, eliminate repairs without a fixed separation gap, or show that a hypothetical Robin counterexample necessarily supplies the required continuum vertical observation.
