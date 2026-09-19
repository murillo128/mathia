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
  - research/visual_exploration/findings/VIS-305-cramer-parity-control-loglog-spacing-norm.md
---

# Does Wang packet localization preserve source information without manufacturing strip gain?

## Observation

The fixed-power source branch has already been reduced to a classical arithmetic envelope. `VIS-283`--`VIS-293` isolate Wang's source channel, show that compact-power packet localization does not manufacture new information, and identify half-plane pole exclusion for the squared-von-Mangoldt source transform as RH-equivalent rather than an independent continuation mechanism. `VIS-294`--`VIS-298` then remove the apparent moving lower-source barrier by exact gamma recentering.

The moving upper pointwise branch has also undergone successive boundary corrections. `VIS-301` uses the classical zero-free region to make the localization terms `o(H)` through the first apparent `H/L^2` layer. `VIS-302` evaluates Wang's exact coefficient moment and improves the generic mean-value error from `O(x log^2 x)` to `O(x log x)`, extending the pointwise asymptotic through `x log(2x)=o(H)`. `VIS-303` shows that at the corresponding boundary `x log x asymp H`, the entire odd-additive-shift sector is `o(H)`.

`VIS-304` removes that boundary as well by applying the weighted Montgomery--Vaughan Hilbert inequality to the actual nonzero prime-power frequency set `lambda_q=log q`. A Brun--Selberg upper-bound-sieve estimate for reciprocal small prime gaps, together with the sparsity of higher prime powers and Wang's taper, gives

`sum_(q prime power) a_q^2/delta_q << x log log(3x)`,

where `delta_q` is the nearest logarithmic spacing among prime-power frequencies. Hence

`integral_I |D_x(t)|^2 dt = H sum_q a_q^2 + O(x log log(3x))`,

and the full pointwise asymptotic now holds whenever

`x log log(3x)=o(H)`.

`VIS-305` tests whether this new `log log x` factor is itself already removable at the level of sparse spacing geometry. It is not: a parity-matched independent Bernoulli support with mean density `1/log x` and Wang-scale shell weights has

`E sum b_q^2/delta(q)=Theta(x log log x)`.

Thus the absolute reciprocal-spacing scale is reproduced even after prime arithmetic is replaced by an independent density-matched control. The factor is not by itself evidence for a prime-specific transition, but neither can it be removed by a spacing argument that uses only density, parity, and generic sparsity.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can one go beyond the `x log log x` absolute spacing norm by using information absent from the Bernoulli control? There are now two genuinely different possibilities:

- prove that the actual prime-power support has arithmetic spacing correlations strong enough to give a coefficient-weighted improvement over the density/parity baseline; or
- bypass the absolute local-spacing norm and prove cancellation in the signed endpoint Hilbert forms themselves.

A third decisive outcome would be a matched admissible coefficient/support model whose **signed** endpoint form really attains `H` scale near `H asymp x log log x`, showing that additional arithmetic input is necessary.

## Why it may matter

Repeatedly decomposing the first term that reaches output scale has removed the moving lower-source barrier, the fixed exponent gap, the `H/L^3` localization wall, the `H/L^2` coefficient-majorant wall, the unrestricted `H/L` mean-value wall, and the ambient integer-spacing wall. The current surviving upper boundary is therefore much more specific than the original theorem packaging.

`VIS-305` now separates two notions that had still been conflated. The `log log x` growth of the **absolute** local-spacing norm is generic for a sparse parity-matched support; any further gain for actual primes must come from arithmetic correlations beyond that null or from oscillatory phase cancellation that the absolute norm discards.

A further gain would enlarge the pointwise source window beyond `H/log log x`. A matching signed lower construction would instead identify the first boundary in this chain that survives coefficient support, classical zero-free localization, support-sensitive Hilbert geometry, and the density/parity null.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work from the exact endpoint Hilbert forms for the prime-power frequencies rather than returning to the ambient integer-spacing estimate. In the regime `x log log(3x) asymp H`, determine whether one of the following holds:

- the **actual prime-power** weighted spacing sum is `o(x log log x)` for an arithmetic reason not shared by the parity-matched Bernoulli control;
- cancellation in the signed endpoint Hilbert forms makes the actual remainder `o(H)` despite the `Theta(x log log x)` matched absolute norm;
- a mathematically admissible matched coefficient/support model produces an `H`-scale signed remainder and shows that additional arithmetic input is necessary.

Any stronger bound must preserve the actual frequency support and Wang taper and must account for the full localization/gamma budget already isolated by `VIS-298`--`VIS-304`. Do not reopen the old `H/L^3`, `H/L^2`, `H/L`, ambient-spacing, or density-only local-spacing majorants unless a new hypothesis invalidates the corresponding findings.

## Evidence boundary

`VIS-283`--`VIS-303` establish the previous source reductions and boundary corrections. `VIS-304` proves only an upper bound for the mean-value remainder using classical weighted-Hilbert and sieve machinery; it does not show that `x log log x` is attained, optimal, or a transition of `F_I`.

`VIS-305` proves an exact negative control for the **absolute spacing norm**: parity-matched independent sparse occupancy already has expected order `x log log x`. It does not prove the same lower order for actual prime powers and does not evaluate the signed endpoint Hilbert form. The possibility of exact-prime arithmetic improvement or phase cancellation therefore remains open.

No result here improves a prime-pair sieve theorem, proves a new nearest-prime-gap law, or establishes a stronger RH criterion. The fixed-power source-specific arithmetic question, the signed `H/log log x` endpoint-Hilbert question, genuinely bounded sources, and moving-test-function versions remain distinct.

## Research disposition

Outcome so far: **upper pointwise branch narrowed past density-only spacing geometry to exact-prime correlation or signed-phase cancellation**.

The earlier moving-lower-source, localization, coefficient-majorant, ambient integer-spacing, and generic sparse-spacing escape routes are closed under the current hypotheses. The accepted clue remains live for the signed endpoint-Hilbert question, for any arithmetic spacing gain absent from the Bernoulli control, and for the separate fixed-power source-specific arithmetic question.
