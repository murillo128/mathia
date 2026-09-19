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
  - research/visual_exploration/findings/VIS-306-bernoulli-signed-shell-hilbert-cancellation.md
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

Thus the absolute reciprocal-spacing scale is reproduced even after prime arithmetic is replaced by an independent density-matched control.

`VIS-306` then evaluates the **signed** mean-square remainder for that same control on the central shell. Writing the off-diagonal term as a Bernoulli quadratic form and using the exact endpoint kernel gives

`|E R_I| << x`,
`Var(R_I) << x log^3 x`,

uniformly in `T,H`. Therefore

`R_I=O_p(x)`,

and in particular `R_I=o_p(H)` at `H asymp x log log x`. The `log log x` absolute norm is therefore not merely non-prime-specific; it is also a poor predictor of signed obstruction size in the obvious matched sparse control.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can the actual prime-power endpoint Hilbert form be shown to cancel beyond the `x log log x` absolute spacing bound? The decisive distinction is now between ordinary sparse occupancy and **prime-specific coherence**. Possible outcomes are:

- prove that the true prime-power signed endpoint form is `o(H)` near `H asymp x log log x`, for example by using arithmetic spacing correlations and phase cancellation unavailable to the Bernoulli control;
- prove a stronger coefficient/support statement such as an `O(x)`-scale signed remainder over the relevant tapered prime-power range;
- construct an admissible matched support/coefficient model that preserves enough arithmetic or phase coherence to produce an `H`-scale signed remainder, thereby identifying what information is missing from the Bernoulli null.

The plain density/parity Bernoulli model is no longer a candidate for the third outcome: `VIS-306` rules it out.

## Why it may matter

Repeatedly decomposing the first term that reaches output scale has removed the moving lower-source barrier, the fixed exponent gap, the `H/L^3` localization wall, the `H/L^2` coefficient-majorant wall, the unrestricted `H/L` mean-value wall, the ambient integer-spacing wall, and finally the interpretation of the `x log log x` absolute spacing norm as a signed obstruction.

`VIS-305` and `VIS-306` together now separate three layers that were previously conflated: sparse nearest-neighbor geometry, its absolute weighted Hilbert majorant, and the actual signed endpoint form. Density and parity reproduce the first two at the `log log x` scale, but the signed form of the same ensemble is only `O_p(x)`. Any genuine barrier at `H/log log x` must therefore involve coherence that survives the sign/phase structure rather than only large reciprocal spacings.

A further gain for the true prime-power form would enlarge the pointwise source window beyond `H/log log x`. A coherent matched lower construction would instead identify the first boundary in this chain that survives coefficient support, classical zero-free localization, support-sensitive Hilbert geometry, density/parity matching, and ordinary Bernoulli signed cancellation.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work from the exact signed endpoint Hilbert forms on the prime-power logarithmic frequencies. In the regime `x log log(3x) asymp H`, determine whether the true tapered form admits a gain unavailable to the Bernoulli control. Any proposed gain should identify the arithmetic or phase-coherence input actually used, rather than return to the absolute local-spacing norm.

A matched obstruction must now preserve more than density, parity, coefficient size and generic sparsity. It should encode a concrete additional feature of the prime-power support or endpoint phases and then show that feature can sustain an `H`-scale signed form. Conversely, a cancellation theorem should control the full signed form and still account for the localization/gamma budget already isolated by `VIS-298`--`VIS-304`.

Do not reopen the old `H/L^3`, `H/L^2`, `H/L`, ambient-spacing, density-only local-spacing, or plain Bernoulli signed-control routes unless a new hypothesis invalidates the corresponding findings.

## Evidence boundary

`VIS-283`--`VIS-303` establish the previous source reductions and boundary corrections. `VIS-304` proves only an upper bound for the mean-value remainder using classical weighted-Hilbert and sieve machinery; it does not show that `x log log x` is attained, optimal, or a transition of `F_I`.

`VIS-305` proves an exact negative control for the **absolute spacing norm**: parity-matched independent sparse occupancy already has expected order `x log log x`. `VIS-306` proves a complementary negative control for the **signed shell remainder** of that same ensemble: its expectation is `O(x)`, its variance is `O(x log^3 x)`, and hence it is `o_p(H)` at the `H asymp x log log x` boundary.

Neither result estimates the actual signed prime-power endpoint form. Prime-pair singular-series structure, higher prime powers, the full tapered range, and deterministic endpoint phases may still create or destroy coherence absent from the Bernoulli model. No stronger RH criterion or new prime-gap theorem is established.

## Research disposition

Outcome so far: **upper pointwise branch narrowed past absolute spacing geometry and ordinary sparse signed controls to prime-specific arithmetic/phase coherence**.

The accepted clue remains live for the true signed prime-power endpoint form and for the separate fixed-power source-specific arithmetic question. A future matched obstruction must preserve an explicit coherence mechanism beyond the density/parity Bernoulli null.