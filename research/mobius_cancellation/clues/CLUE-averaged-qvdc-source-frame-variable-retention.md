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
  - research/mobius_cancellation/findings/MC-402-truncated-lcm-mask-is-mertens-weighted-divisor-energy.md
  - research/mobius_cancellation/findings/MC-405-mangoldt-quotient-self-coupling-needs-cross-scale-cancellation.md
  - research/mobius_cancellation/findings/MC-406-mangoldt-quotient-fibers-collapse-to-harmonic-mobius.md
  - research/mobius_cancellation/findings/MC-407-prime-error-increment-coupling-abel-collapse.md
  - research/mobius_cancellation/findings/MC-408-signed-pnt-error-correlation-is-rh-equivalent.md
  - research/mobius_cancellation/findings/MC-409-well-factorable-upper-sieve-preserves-prime-frame.md
  - research/mobius_cancellation/findings/MC-410-factorable-sieve-character-phase-is-mellin-separable.md
  - research/mobius_cancellation/findings/MC-411-fourier-completion-product-phase-is-dual-permutation.md
  - research/mobius_cancellation/findings/MC-412-zero-residue-well-factorable-degeneracy.md
  - research/mobius_cancellation/findings/MC-413-additive-differencing-complete-block-ramanujan-collapse.md
  - research/mobius_cancellation/findings/MC-446-source-frame-box-mean-square-has-quadratic-occupancy-threshold.md
---

# Can actual lcm/source structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

The current single-character q-vdC route has an intrinsic source-depth tariff: `MC-382` identifies the square-root loss paid at successive conductor scales, while `MC-383` shows that a generic family mean value does not by itself remove a fixed positive power of the global modulus. Julia Stadlmann's modified q-van der Corput argument in *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) remains the structural comparison because it retains an arithmetic summation variable through differencing/Cauchy and thereby changes the diagonal count.

The Selberg/lcm side has already consumed several apparently richer coordinates without changing that information budget. `MC-397`--`MC-402` show successively that source-mode averaging, divisor-pair/lcm coordinates, moving-hyperbola truncation, and the complete or truncated lcm forms reduce to projectors, invertible transforms, signed incidence/GCD energies, or Mertens-weighted incidence energies. The quotient/Mangoldt variants `MC-405`--`MC-408` likewise collapse after exact aggregation to Möbius self-couplings, Abel-equivalent forms, or an RH-equivalent scalar target at square-root scale. These remain useful classifications, but none supplies an independent source-cost improvement.

`MC-409` establishes a genuinely different positive representation: a well-factorable upper linear-sieve divisor weight preserves shell-prime normalization and the correct diagonal scale without passing through the quadratic Selberg coefficient. `MC-410`--`MC-412` then show that its raw multiplicative phase, ordinary additive completion, and zero-residue progression interpretation are still separable or degenerate. `MC-413` identifies the first surviving affine datum: after additive differencing, a compatible divisor pair produces an incomplete translated correlation

`sum_(k in I_de) chi(k+u_de+h[lcm(d,e)]^-1) overline(chi(k+u_de))`.

Every complete conductor block collapses exactly to the Ramanujan scalar `c_q(h)`, so only the incomplete family can retain divisor-dependent source phase.

`MC-446` now tests the most naive collective version of that remaining family. For a primitive character, the exact full `(u,a)`-box second moment is

`sum_(u,a) |S_H(u,a)|^2 = sum_(k,l<=H) |c_q(k-l)|^2`.

In the squarefree rough range `H <= P^-(q)`, this is `H phi(q)^2 + H(H-1)`. Thus ambient incomplete correlations really do have square-root-scale RMS cancellation, but Cauchy can transfer that cancellation to a weighted source family only if its effective occupancy exceeds approximately `q^2/H` when `phi(q) ~ q`. Generic full-box averaging therefore cannot rescue a sparse CRT/source-frame image. The surviving question is no longer whether the ambient family cancels; it is whether the **specific arithmetic image of `(d,e) -> (u_de,a_de)` admits a restricted moment or dispersion estimate with a substantially cheaper diagonal**.

## Research question

Two branches remain legitimate.

First, can the actual Selberg/source structure inside the truncated lcm form produce a theorem genuinely stronger than generic cutoff inversion? A surviving result must exploit the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies, and after full bookkeeping must avoid both the sequential source-depth tariff and a fixed positive common-radical cost. Merely rewriting the cutoff through `MC-402` and inserting unavailable Mertens cancellation does not qualify.

Second, can the well-factorable upper-sieve CRT image beat the `MC-446` occupancy barrier by using structure that the ambient `(u,a)` box discards? The candidate mechanisms are now concrete: fibres or collisions of `(d,e) -> (u,a)`, grouping by the constrained shift `a=h[d,e]^-1`, well-factorable cancellation in the outer coefficients, a restricted Fourier/dispersion form, or modulus factorization that reduces the conductor before the source variables are scalarized. The target is a restricted second moment or bilinear form whose post-Cauchy diagonal is parametrically smaller than the full-box `H phi(q)^2` tariff after the actual divisor weights are included.

It remains insufficient for a variable merely to survive notation. The desired analogue of Stadlmann must change usable diagonal/off-diagonal information before scalarization, rather than provide a reversible, Abel-equivalent, Fourier-equivalent, residue-permutation-equivalent, complete-period-equivalent, ambient-L2-equivalent, or RH-equivalent coordinate system.

## Why it may matter

`MC-446` separates a false negative from a real obstruction. The incomplete shifted character family is not devoid of collective cancellation: the full box has an exact favorable second moment. What fails is the transfer of that cancellation to a sparse source family by a generic Cauchy step. This sharply identifies the missing resource as **arithmetic structure of the sampled frame**, rather than stronger individual short-character bounds or another completion identity.

If a restricted-frame moment beats the ambient occupancy threshold, it would supply precisely the kind of retained pre-quadratic information the current source-depth argument lacks. If every natural restricted moment inherits the same diagonal tariff, the well-factorable/q-vdC branch can be closed much more decisively than by individual Burgess or Pólya--Vinogradov estimates.

## Decisive test

For the lcm branch, exhibit a nontrivial bound for the truncated lcm/source form or a collective source-signature/bilinear estimate and identify the ingredient absent for generic coefficients and a generic quadratic character. Propagate it through the source-frame argument with every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation error visible. Reject any argument whose only gain is one of the already classified coordinate changes in `MC-397`--`MC-408`.

For the factorable upper-sieve branch, start from the exact CRT map of `MC-413` and the occupancy no-go of `MC-446`. Compute a **restricted** second moment or dispersion form on the actual weighted image, not on the ambient `(Z/qZ)^2` box. The first useful target is to fix or group the constrained shift `a=hL^-1`, determine the multiplicity/fibre structure of the compatible `u` values, insert the well-factorable coefficients before Cauchy, and count the resulting diagonal exactly. The branch survives only if the resulting effective threshold is parametrically smaller than `phi(q)^2/H` in a range that still survives the later source-frame bookkeeping.

Reject a continuation if it applies an individual incomplete character-sum bound to each divisor pair, applies Cauchy against the full box and fails the `MC-446` occupancy threshold, completes first and falls back to `c_q(h)` as in `MC-413`, or uses the arithmetic relation `a=hL^-1` only as a relabeling without reducing the actual diagonal/off-diagonal cost.

## Evidence boundary

No theorem using the actual Selberg lcm coefficient has yet changed the source-cost scaling, and no factorable-upper-sieve estimate has yet beaten the existing source-character bound. `MC-409` establishes only the alternative positive frame; `MC-410`--`MC-413` classify successive separable, degenerate, or complete-period reductions.

`MC-446` is an exact finite harmonic-analysis result, not an improved character-sum or Mertens estimate. It proves that full ambient averaging has an effective-occupancy requirement of order `q^2/H` in the squarefree rough regime; it does **not** prove that the actual CRT image fails a sharper restricted estimate. The special relation `a=hL^-1`, collisions/fibres of `(d,e)->(u,a)`, variable interval lengths, and well-factorable coefficient cancellation remain unexploited.

Stadlmann's theorem concerns a different Type I averaged-prime setting and does not transfer automatically. Heath-Brown/Irving q-vdC theory and sliding-sum/trace-function methods show that incomplete oscillatory families can be exploitable, but they do not by themselves establish the required weighted restricted-frame estimate. The scalar Möbius--PNT-error branch remains classified by `MC-408` as RH-equivalent at the target exponent.

## Research disposition

The clue remains `accepted` and is **materially narrowed by `MC-446`**. Generic collective averaging over all translation/start pairs is no longer a live mechanism: its exact second moment carries a quadratic effective-occupancy threshold. The live well-factorable question is now specifically whether the arithmetic CRT/source-frame subset has a restricted moment, fibre decomposition, or dispersion structure whose diagonal cost is parametrically below that ambient threshold. The independent truncated-lcm/source-specific branch remains open under its previous stronger-than-generic requirement.