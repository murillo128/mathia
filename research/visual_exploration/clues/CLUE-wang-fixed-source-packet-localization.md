---
id: CLUE-visual-wang-fixed-source-packet-localization
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-283-wang-fixed-source-cross-frequency-separation.md
  - research/visual_exploration/findings/VIS-291-wang-fixed-power-korobov-vinogradov-envelope.md
  - research/visual_exploration/findings/VIS-293-wang-source-dirichlet-rh-half-plane.md
  - research/visual_exploration/findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md
  - research/visual_exploration/findings/VIS-301-wang-zero-free-localization-log-squared-window.md
  - research/visual_exploration/findings/VIS-302-wang-weighted-mean-value-log-boundary.md
  - research/visual_exploration/findings/VIS-303-wang-odd-shift-power-two-sparsity.md
  - research/visual_exploration/findings/VIS-304-wang-prime-power-spacing-loglog-boundary.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power source branch has already been reduced to a classical arithmetic envelope. `VIS-283`--`VIS-293` isolate Wang's source channel, show that compact-power packet localization does not manufacture new information, and identify half-plane pole exclusion for the squared-von-Mangoldt source transform as RH-equivalent rather than an independent continuation mechanism. `VIS-294`--`VIS-298` then remove the apparent moving lower-source barrier by exact gamma recentering.

The moving upper pointwise branch has also undergone successive boundary corrections. `VIS-301` uses the classical zero-free region to make the localization terms `o(H)` through the first apparent `H/L^2` layer. `VIS-302` evaluates Wang's exact coefficient moment and improves the generic mean-value error from `O(x log^2 x)` to `O(x log x)`, extending the pointwise asymptotic through `x log(2x)=o(H)`. `VIS-303` shows that at the corresponding boundary `x log x asymp H`, the entire odd-additive-shift sector is `o(H)`.

`VIS-304` removes that boundary as well by applying the weighted Montgomery--Vaughan Hilbert inequality to the **actual nonzero prime-power frequency set** `lambda_q=log q`. A Brun--Selberg upper-bound-sieve estimate for reciprocal small prime gaps, together with the sparsity of higher prime powers and Wang's taper, gives

`sum_(q prime power) a_q^2/delta_q << x log log(3x)`,

where `delta_q` is the nearest logarithmic spacing among prime-power frequencies. Hence

`integral_I |D_x(t)|^2 dt`
` = H sum_q a_q^2 + O(x log log(3x))`,

and the full pointwise asymptotic now holds whenever

`x log log(3x)=o(H)`.

The previous `H/log T` layer was therefore another proof-packaging boundary. `VIS-303` remains valid at its own scale, but the larger range of `VIS-304` is obtained without assuming its parity reduction.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, is the support-sensitive weighted-Hilbert cost

`x log log x`

a real obstruction for Wang's endpoint Hilbert forms near

`x log log x asymp H`,

or only the next absolute-value majorant? Can the actual signed/oscillatory off-diagonal form be shown to be `o(H)` farther into the source range, or can an admissible matched construction realize an `H`-scale remainder there?

## Why it may matter

Repeatedly decomposing the first term that reaches output scale has removed the moving lower-source barrier, the fixed exponent gap, the `H/L^3` localization wall, the `H/L^2` coefficient-majorant wall, the unrestricted `H/L` mean-value wall, and the opposite-parity interpretation at that earlier layer. The current surviving upper boundary is now tied to a specific arithmetic object: reciprocal nearest-neighbor spacing of the prime-power frequency support inside the weighted Hilbert norm.

A further gain would enlarge the pointwise source window beyond `H/log log x`. A matching lower construction would instead identify the first boundary in this chain that survives coefficient support, classical zero-free localization, and support-sensitive Hilbert geometry.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work from the exact endpoint Hilbert forms for the prime-power frequencies rather than returning to the ambient integer-spacing estimate. In the regime `x log log(3x) asymp H`, determine whether one of the following holds:

- the weighted reciprocal-spacing sum itself admits a stronger coefficient-specific bound than `O(x log log x)`;
- cancellation in the signed endpoint Hilbert forms makes the actual remainder `o(H)` despite the absolute weighted norm;
- a mathematically admissible matched coefficient/support model produces an `H`-scale remainder and shows that additional arithmetic input is necessary.

Any stronger bound must preserve the actual frequency support and Wang taper and must account for the full localization/gamma budget already isolated by `VIS-298`--`VIS-304`. Do not reopen the old `H/L^3`, `H/L^2`, or `H/L` majorants unless a new hypothesis invalidates the corresponding findings.

## Evidence boundary

`VIS-283`--`VIS-303` establish the previous source reductions and boundary corrections. `VIS-304` proves only an **upper bound** for the mean-value remainder using classical weighted-Hilbert and sieve machinery; it does not show that `x log log x` is attained, optimal, or a transition of `F_I`.

No result here improves a prime-pair sieve theorem, proves a new nearest-prime-gap law, or establishes a stronger RH criterion. The fixed-power source-specific arithmetic question, the `H/log log x` endpoint-Hilbert question, genuinely bounded sources, and moving-test-function versions remain distinct.

## Research disposition

Outcome so far: **upper pointwise branch narrowed to the support-sensitive prime-power Hilbert problem near `x log log x asymp H`**.

The earlier moving-lower-source, localization, coefficient-majorant, and ambient integer-spacing boundaries are closed under the current hypotheses. The accepted clue remains live for the `H/log log x` support-sensitive question and for the separate fixed-power source-specific arithmetic question.
