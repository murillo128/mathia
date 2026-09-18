# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-210](../../findings/RE-210-exact-sinc-tail-geometry-sharpens-the-separated-vertical-kv-ceiling.md). The compact-support Fourier/spectral-gap geometry is classical; the Mathia content is its exact pullback to separated ordinary-prime Euler repairs at selector scale under KV source fidelity.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs only when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then uncertainty is no longer a rank question: the gap forces an exponentially large weighted cumulative primitive.

RE-209 identifies the physical primitive after pulling the generic harmonic statement back to ordinary primes. The exponentially weighted primitive is exactly a signed prime-count prefix, and partial summation converts it into a Chebyshev-prefix excursion. Thus the continuum observation width is priced in a source currency that fixed Korobov--Vinogradov fidelity constrains.

RE-210 sharpens the exponential rate without changing the architecture. Keeping the exact first sidelobe of the repeated-uniform sinc test gives

`log R >= (gamma_*+o(1)) H T`,  with `gamma_*=0.5979019108...`,

rather than the earlier `1/e` rate. For selector-scale ordinary-prime repairs preserving every fixed KV envelope, `T_Q=c log Q` must satisfy

`c < 1/(2 gamma_* H)`.

At the current gap `H=log 8`, the universal ceiling is `0.4021548838...`, while explicit ordinary-prime hiding is constructed below `0.0289079...`. The continuum vertical problem is therefore genuinely two-sided: ordinary primes can pay an exponential hiding cost for a positive logarithmic-height range, but beyond a larger explicit range the required signed prefix violates the source envelope.

The reusable distinction is between **local spectral rank and global continuum source cost**. A finite panel asks whether source vectors are distinguishable at sampled phases; a continuum interval plus support separation asks how much weighted signed prefix must be generated to approximate an entire Fourier profile. The latter can be coercive even though every finite panel remains aliasable.

The remaining gap is itself in the correct currency. On the obstruction side, improving the compact-support extremal test can strengthen the exponential prefix rate. On the constructive side, the relevant target is no longer merely small total variation: a better repair must directly control its signed weighted prefixes. Either improvement changes the actual source budget rather than the nominal number of vertical samples.

**Boundary.** The coercive theorem assumes a fixed pre-repair logarithmic gap, ordinary-prime edits with the stated integer multiplicities, selector-scale local mass and fidelity to every fixed KV envelope. The numerical `gamma_*` is the exact rate of the current sinc-power family, not an optimal compact-support constant. The result does not prove Robin, eliminate repairs without a fixed separation gap, or show that a hypothetical Robin counterexample necessarily supplies the required continuum vertical observation.
