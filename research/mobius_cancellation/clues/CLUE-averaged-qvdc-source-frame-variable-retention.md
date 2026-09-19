---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-382-iterated-q-vdc-has-an-intrinsic-loglog-source-horizon.md
  - research/mobius_cancellation/findings/MC-383-small-doubling-family-mean-value-retains-global-modulus-horizon.md
  - research/mobius_cancellation/findings/MC-396-paired-block-packing-removes-inverse-gap-depth-tax.md
  - research/mobius_cancellation/findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md
  - research/mobius_cancellation/findings/MC-398-selberg-divisor-pair-lcm-fiber-collapse.md
  - research/mobius_cancellation/findings/MC-399-lcm-retention-separates-from-source-qvdc-phase.md
  - research/mobius_cancellation/findings/MC-400-twisted-lcm-hyperbola-transform-is-mobius-invertible.md
  - research/mobius_cancellation/findings/MC-401-full-lcm-endpoint-is-signed-gcd-energy.md
---

# Can truncated lcm structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) gives a nearby but structurally different mechanism: a modified q-van der Corput argument retains an arithmetic `y`-summation variable inside the differencing/Cauchy geometry, reducing the diagonal count and enlarging the admissible parameter range.

The endpoint source/Selberg frame has now passed five exact representation tests. `MC-397` shows that pre-modewise source averaging Fourier-collapses to a source-signature projector, so the source-mode index is not an extra arithmetic sample. `MC-398` shows that the squared Selberg divisor pair `(d_1,d_2)` enters the arithmetic only through `ell=[d_1,d_2]`, with the pair fiber compressed to one coefficient `C_g(ell)`. `MC-399` shows that complete multiplicativity separates `chi_I(ell m)` and removes the lcm scalar at the first additive q-vdC correlation. `MC-400` then shows that the moving hyperbola boundary is an exactly reversible Dirichlet-convolution representation rather than an independent arithmetic coordinate.

`MC-401` now classifies the **complete lcm endpoint** left inside that branch. For one source mode,

`A_I(B^2)=sum_{ell<=B^2} C_g(ell) chi_I(ell)`

has the exact meet-matrix factorization

`A_I(B^2)=sum_k (mu *_D chi_I)(k) (sum_{k|d<=B} g(d) chi_I(d))^2`.

This is classical GCD/meet-matrix incidence algebra. The diagonal weights are signed whenever a unit prime has `chi_I(p)=-1`, and the local two-point kernel is already indefinite, so the full endpoint supplies neither positivity nor generic cancellation. If all unit primes through `B` have positive character value, the endpoint instead collapses to a single perfect square. Thus generic structure of the **complete** lcm coefficient is no longer a plausible missing mechanism by itself.

## Research question

The retained-variable question now has two legitimate branches.

First, can one prove an **independent truncated-lcm or actual-weight theorem** strong enough to change the source-cost scaling? The standard-lcm target is no longer the complete endpoint `A_I(B^2)`. It is one of:

- a genuinely truncated partial sum `A_I(X)` with `X<B^2`, where the mask `[d_1,d_2]<=X` prevents the complete meet-matrix square decomposition;
- a theorem using special structure of the actual Selberg coefficient `g`, rather than the generic lcm/GCD kernel;
- source-signature class information or a collective bilinear estimate not determined by the complete quadratic form.

A successful estimate must avoid both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive common-radical cost `P^theta`. It does not count to recover the complete endpoint by the classical meet-matrix factorization in `MC-401`, nor to obtain lcm partial sums from the inversion formula in `MC-400` and feed them back without an independent quantitative gain.

Second, can a different **pre-quadratic arithmetic representation** expose a divisor/source variable whose phase or congruence does not factor through `[d_1,d_2]` and remains nonseparable through the relevant Cauchy/q-vdC correlation? This remains the direct analogue of Stadlmann's retained-variable mechanism.

## Why it may matter

Five apparent escape dimensions have now been separated from genuine analytic content by exact algebra: source-mode averaging, the Selberg divisor-pair labels, the lcm factor inside the source phase, the hyperbola boundary viewed merely as a new sample coordinate, and the complete lcm endpoint viewed as an unexplained quadratic statistic. Each reduction prevents a richer notation from being mistaken for a stronger estimate.

The surviving lcm-side question is consequently sharper. **Truncation, actual Selberg-weight structure, or extra signature distribution must do real mathematical work.** If they do not, the remaining escape is no longer another rearrangement of the squared Selberg frame but a genuinely different pre-quadratic kernel.

## Decisive test

For the lcm branch, exhibit a theorem that is genuinely unavailable at the complete endpoint classified by `MC-401`. Concretely, prove a bound for `A_I(X)` in a nontrivial range `X<B^2`, a source-signature analog, or a joint bilinear form

`sum_{ell m<=N} C_g(ell) chi_I(ell) chi_I(m)`

using arithmetic structure of the truncation, the actual Selberg coefficient, or the source family. Propagate the estimate to the source-frame bound and account explicitly for every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation. The direction survives only if a strict quantitative improvement remains after that accounting.

Reject an argument if it uses only the full endpoint `A_I(B^2)`: `MC-401` gives its exact classical signed GCD/divisor-energy factorization and shows that the underlying kernel is indefinite rather than generically cancelling. Also reject a purported gain if its only new step is the moving boundary `m<=N/ell` (`MC-400`), if it treats `chi_I(ell m)` as nonseparable (`MC-399`), keeps divisor-pair labels after lcm compression (`MC-398`), or reuses the source-mode index after projector collapse (`MC-397`). Generic family estimates with a fixed positive global-modulus cost remain subject to `MC-383`.

For a pre-quadratic alternative, exhibit the kernel before estimating it. It must not factor through the lcm as in `MC-398`, and after source Fourier expansion its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`. Then count the post-Cauchy diagonal exactly and compare the mechanism with Stadlmann's genuine retained-variable gain.

## Evidence boundary

No nontrivial uniform estimate for truncated `A_I(X)` has been proved, no theorem exploiting special structure of the actual Selberg coefficient has changed the source-cost scaling, and no genuinely non-lcm-factorable pre-quadratic variable has been exhibited. `MC-401` does not rule out any of those routes; it only closes the generic complete-endpoint lcm statistic as an independent mechanism.

Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setting and does not imply an endpoint source-cost theorem or improved Möbius cancellation. None of `MC-397`--`MC-401` yields a bound for the Mertens function.

## Research disposition

The clue remains `accepted` but is narrower. The standard-lcm branch is now a **truncated/actual-weight arithmetic theorem obligation**: exploit the cutoff `[d_1,d_2]<=X`, special structure of the actual Selberg weight, source-signature distribution beyond the complete meet-matrix energy, or a genuinely collective bilinear form, and show that the resulting estimate changes the source-depth/common-radical scaling.

The second branch remains unchanged: find a pre-quadratic arithmetic variable that survives both lcm compression and source-phase separation and then verify, by an exact post-Cauchy diagonal count, that it produces the retained-variable effect missing from the present representation.