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
  - research/visual_exploration/findings/VIS-307-prime-power-random-phase-hilbert-cancellation.md
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

`VIS-307` strengthens the control without changing the support at all. It keeps every actual prime power and every Wang coefficient magnitude, randomizing only one independent unit-modulus phase per prime-power support point. Exact phase orthogonality and a dyadic estimate of the squared reciprocal-log kernel give

`E R_I^epsilon=0`,
`E|R_I^epsilon|^2 << x log^3(3x)`.

Hence

`R_I^epsilon=O_p(sqrt(x) log^(3/2)(3x))=o_p(H)`

at `H asymp x log log(3x)`. The actual prime-power spacing pattern therefore does not by itself sustain the boundary-scale signed remainder: the missing information must lie in deterministic phase organization that this stronger null deliberately destroys.

## Research question

Two source routes remain distinct.

For the **fixed-power real-axis source**, is there a property of

`mu=sum Lambda(n)^2/n delta_(log n)`

strictly weaker than the RH-equivalent half-plane pole exclusion of `VIS-293` that improves the generic Korobov--Vinogradov envelope and survives Wang's complete error budget?

For the **moving upper pointwise layer**, can the actual deterministic prime-power endpoint phases be shown to cancel beyond the `x log log x` weighted-Hilbert bound, or can one isolate a concrete phase-coherence mechanism that genuinely prevents such cancellation? Support geometry is no longer enough: `VIS-307` preserves the exact prime-power support, all spacings, and all coefficient magnitudes while still giving `o_p(H)` after phase randomization.

The useful next alternatives are therefore narrower:

- prove that Wang's true deterministic prime-power endpoint form is `o(H)` near `H asymp x log log x`;
- identify a specific deterministic phase relation, such as base-prime harmonic coherence or a structured endpoint alignment, and prove that it can sustain an `H`-scale contribution;
- construct a stronger matched control that preserves that explicit phase relation and test whether the obstruction survives.

A support-only refinement, even one preserving the exact arithmetic spacings, is no longer a candidate explanation by itself.

## Why it may matter

Repeatedly decomposing the first term that reaches output scale has removed the moving lower-source barrier, the fixed exponent gap, the `H/L^3` localization wall, the `H/L^2` coefficient-majorant wall, the unrestricted `H/L` mean-value wall, the ambient integer-spacing wall, the interpretation of the `x log log x` absolute spacing norm as a signed obstruction, and now the hypothesis that exact prime-power spacing geometry alone is enough.

`VIS-305`--`VIS-307` separate four levels: sparse occupancy, its absolute Hilbert majorant, exact arithmetic support geometry, and deterministic coefficient phase organization. The first three can reproduce large reciprocal-spacing costs while their matched signed controls remain `o_p(H)`. A genuine barrier at `H/log log x` must therefore live in the fourth level or in a still more structured interaction coupled to it.

A cancellation theorem for the true phase pattern would enlarge the pointwise source window beyond `H/log log x`. A coherent matched lower construction would instead identify the first boundary in this chain that survives exact support, exact coefficient magnitudes, classical zero-free localization, support-sensitive Hilbert geometry, and phase-randomized signed cancellation.

## Decisive test

For the fixed-power branch, state a concrete real-axis estimate or secondary expansion for `S(x)-log x`, derive it from arithmetic information strictly weaker than the pole exclusion of `VIS-293`, and propagate it through all source, gamma, localization, and cross-term errors. Kill the route if the gain is only a generic PNT substitution, smoothing attenuation, an RH-equivalent continuation assumption, or a term swallowed by another Wang remainder.

For the moving upper branch, work from the exact signed endpoint Hilbert form on the actual prime-power logarithmic frequencies in the regime `x log log(3x) asymp H`. Any claimed obstruction must now identify a **phase-coherence invariant** lost by the independent-support-phase control of `VIS-307`. A natural next control is to restore one shared unit phase per base prime, so that the coefficient at `p^k` carries the harmonic phase `epsilon_p^k`, while leaving Wang's magnitudes and exact support untouched. If that phase-preserving control still gives `o_p(H)`, the candidate mechanism must be narrower again.

Conversely, a cancellation theorem for the true deterministic phases should control the full signed form and still account for the localization/gamma budget already isolated by `VIS-298`--`VIS-304`.

Do not reopen the old `H/L^3`, `H/L^2`, `H/L`, ambient-spacing, density-only local-spacing, plain Bernoulli signed-control, or exact-support/independent-phase routes unless a new hypothesis invalidates the corresponding findings.

## Evidence boundary

`VIS-283`--`VIS-303` establish the previous source reductions and boundary corrections. `VIS-304` proves only an upper bound for the actual mean-value remainder using classical weighted-Hilbert and sieve machinery; it does not show that `x log log x` is attained, optimal, or a transition of `F_I`.

`VIS-305` proves an exact negative control for the **absolute spacing norm**. `VIS-306` proves a complementary negative control for the **signed Bernoulli shell remainder**. `VIS-307` preserves the **exact prime-power support and Wang coefficient magnitudes** and shows that after independent coefficient-phase randomization its signed remainder has second moment `O(x log^3 x)` and is still `o_p(H)` at the current boundary.

`VIS-307` deliberately does not preserve multiplicative phase coherence among `p,p^2,p^3,...`; it therefore does not estimate the actual deterministic form and does not rule out a mechanism carried by shared base-prime harmonics or by endpoint-phase alignment. No stronger RH criterion, new prime-gap theorem, or new random quadratic-form theorem is established.

## Research disposition

Outcome so far: **upper pointwise branch narrowed from support geometry to explicit deterministic phase coherence**.

The accepted clue remains live for the true signed prime-power endpoint form and for the separate fixed-power source-specific arithmetic question. The next matched obstruction must preserve a concrete phase-coherence mechanism rather than refine support geometry again.