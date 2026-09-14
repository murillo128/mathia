# MI-023 — Two-island Lambert screening is a cross-scale incidence problem with polynomially many safe windows

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island branch through WI-288, sharpened by WI-289 and [WI-290](../../findings/WI-290-mean-square-prime-gaps-force-polynomially-many-composite-screening-windows.md). This is not a theorem that the required coupled gaps exist or cannot exist.

WI-288 reduces complete screening on two symmetric narrow islands to the nearest-prime-power condition and the Lambert-scale separation

`sqrt(x) delta_pp(x) >= W(c sqrt(x))`.

WI-289 resolves the composite layers through

`delta_pp(x)=min_(k>=1) k delta_p(x^(1/k))`.

The prime layer near `x` demands an enormous `sqrt(x) log x`-scale desert. Prime squares are the unique macroscopically critical composite layer, requiring an approximately mean-gap-sized prime-free interval near `sqrt(x)`; every `k>=3` root window is subunit. On a dyadic shell the composite exclusions still leave residual measure of order `X log log X/log X`.

WI-290 adds the missing topological information. Every prime square is an exact separator of the residual. If the prime-gap second moment at scale `y` is `O(y^(1+theta+epsilon))`, then Cauchy--Schwarz converts the residual mass into at least

`X^((1-theta)/2-epsilon) (log log X/log X)^2`

positive-length safe components. The published `theta=1/4` theorem already yields `X^(3/8-o(1))` such windows. Thus the composite-safe reservoir cannot concentrate into bounded, logarithmic or subpolynomially many exceptional intervals.

The live obstruction is therefore a **cross-scale incidence problem, not a scarcity problem**. A hypothetical giant prime desert near `x` must systematically avoid a polynomial family of composite-safe windows generated primarily by the prime-gap geometry near `sqrt(x)`. Current theorems provide no correlation between those events.

This narrows what a closing theorem must do. It can prove a deterministic coupling between the two scales, exploit null-equation amplitudes/signs that support screening discards, or leave the symmetric two-island topology. Merely improving the total residual measure or showing that one safe interval exists no longer targets the bottleneck.

**Boundary.** WI-290 gives no lower bound on individual safe-window length and no independence/coupling theorem. The recent `77/200` exponent uses an unrefereed preprint; the published `3/8` baseline is sufficient for the qualitative polynomial-fragmentation conclusion.
