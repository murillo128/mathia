# MI-023 — Two-island Lambert screening is a coupled prime-gap problem at `x` and `sqrt(x)`

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island branch through WI-288 and sharpened by [WI-289](../../findings/WI-289-lambert-prime-power-screening-has-a-critical-prime-square-layer.md). This is not a theorem that the required coupled gaps exist or cannot exist.

WI-288 reduces complete screening on two symmetric narrow islands to the nearest-prime-power condition

`2b <= delta_pp(x)`,

and combines it with the prime-deleted spectral zero-bottom condition to require

`sqrt(x) delta_pp(x) >= W(c sqrt(x))`.

WI-289 resolves what the composite prime powers contribute to that arithmetic obstruction. Exactly,

`delta_pp(x)=min_(k>=1) k delta_p(x^(1/k))`.

At the Lambert radius `D_c(x)=W(c sqrt(x))/sqrt(x)`, the corresponding root-scale prime-free interval has length

`(2/k) x^(1/k-1/2) W(c sqrt(x))(1+o(1))`.

Only `k=2` is macroscopically critical beyond the prime layer. The prime condition near `x` demands a desert of size about `sqrt(x) log x`; the square condition becomes a prime-free interval near `sqrt(x)` of length

`log sqrt(x)-log log sqrt(x)+O(1)`,

approximately one mean prime gap. Every `k>=3` root window is subunit and contributes only sparse resonance exclusions.

The dyadic coverage calculation makes this structural distinction quantitative. Composite prime-power Lambert neighborhoods cannot cover `[X,2X]`: the square layer leaves a deficit of order `X log log X/log X`, while all deeper powers occupy only `O(X^(5/6) log X)`. Thus “prime powers are denser than primes” is not enough to close the two-island route.

The live obstruction is a **coupled two-scale placement problem**. One must show that a hypothetical `sqrt(x) log x`-scale prime desert near `x` cannot simultaneously avoid the critical prime-square layer near `sqrt(x)` (and the sparse deeper resonances), or use null-equation amplitude/sign information beyond support screening. WI-289 does not supply the needed correlation between the two scales.

**Boundary.** The square-layer coverage deficit does not prove that centers of enormous prime gaps intersect the composite-power-free residual set. No independence between gap events at `x` and `sqrt(x)` is assumed or obtained.
