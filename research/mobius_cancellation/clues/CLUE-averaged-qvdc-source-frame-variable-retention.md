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
  - research/mobius_cancellation/findings/MC-447-crt-source-frame-fibers-collapse-to-shift-common-primes.md
  - research/mobius_cancellation/findings/MC-448-fixed-lcm-fourier-weil-averaging-still-pays-polynomial-occupancy.md
  - research/mobius_cancellation/findings/MC-449-centered-complement-duality-closes-near-complete-fixed-lcm-escape.md
---

# Can actual lcm/source structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

The current single-character q-vdC route has an intrinsic source-depth tariff: `MC-382` identifies the square-root loss paid at successive conductor scales, while `MC-383` shows that a generic family mean value does not by itself remove a fixed positive power of the global modulus. Julia Stadlmann's modified q-van der Corput argument remains the structural comparison because it retains an arithmetic summation variable through differencing/Cauchy and changes the diagonal count.

The Selberg/lcm branch has already consumed source-mode averaging, divisor-pair/lcm coordinates, moving-hyperbola truncation, incidence/GCD energies, quotient variables and Möbius--PNT-error couplings without obtaining an independent source-cost improvement (`MC-397`--`MC-408`). `MC-409` therefore changed the representation itself: a well-factorable upper linear-sieve weight preserves the positive prime-frame architecture while exposing coefficient factorization before triangle inequality. `MC-410`--`MC-412` show that raw multiplicative phase, ordinary completion and zero-residue progression structure are still separable or degenerate.

`MC-413` identifies the first surviving affine datum. After additive differencing, a compatible divisor pair produces an incomplete translated character correlation

`sum_(k in I_de) chi(k+u_de+h[lcm(d,e)]^-1) overline(chi(k+u_de))`.

Every complete conductor block collapses exactly to the divisor-independent Ramanujan scalar `c_q(h)`, so only the incomplete family can retain source phase.

`MC-446` shows that the full `(u,a)` box has genuine root-`H` RMS cancellation, but generic Cauchy can transfer it to a weighted source family only when effective occupancy is roughly `q^2/H`. `MC-447` then shows that in the clean separated regime the source map has no helpful hidden multiplicity: fixing `a=hL^-1` fixes the exact lcm `L`, and for `(h,P(z))=1` the divisor-pair-to-frame map is injective.

`MC-448` tests the next natural repair rather than assuming that fixed `a` is useless. For prime conductor `p`, conditioning on one `a` and Fourier-diagonalizing the remaining start variable gives, by the classical mixed Weil bound plus Parseval,

`|sum_u W(u) S_H(u,a)| <= C sqrt(pH) ||W||_2`.

This lowers the generic occupancy tariff from about `p^2/H` to `p/H`, a real conductor-power gain. But a fixed-lcm CRT slice has support at most `2^omega(L)=p^o(1)` when `L<p`. Hence for every fixed `delta>0` and `H<=p^(1-delta)`, even this improved uniform Fourier-Weil/Cauchy route cannot beat the pointwise bound for sufficiently large `p`.

`MC-449` closes the apparent near-complete exception to that conclusion. After removing the universal zero Fourier mode, the fixed-shift kernel has the exact complement symmetry `G_H(u,a)=-G_(p-H)(u-(p-H),a)`. The relevant incomplete scale is therefore `min(H,p-H)`, not `H` alone. Near a complete period the source-sensitive term is exactly a short complementary correlation, while in the central range the subpolynomial fixed-lcm occupancy can yield at most a subpolynomial gain. Uniform mixed-Weil control plus generic Parseval/Cauchy on one lcm is now power-closed for every interval length.

The failure is therefore much more specific than a generic lack of averaging: the fixed-lcm route must use information discarded by a uniform Fourier envelope, or it must stop being a one-lcm prime-conductor problem before Cauchy.

## Research question

Two branches remain legitimate.

First, can the actual Selberg/source structure inside the truncated lcm form produce a theorem genuinely stronger than generic cutoff inversion? A surviving result must exploit the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies, and after full bookkeeping must avoid both the sequential source-depth tariff and a fixed positive common-radical cost. Merely rewriting the cutoff through `MC-402` and inserting unavailable Mertens cancellation does not qualify.

Second, can the well-factorable upper-sieve CRT image beat the remaining source-depth barrier by using structure discarded by `MC-448`--`MC-449`? In the clean prime-conductor separated regime, pair collisions, a free `a` coordinate, ambient averaging, a uniform mixed-Weil Fourier envelope, and its near-complete complement are all insufficient. The live possibilities are narrower: cancellation in the actual well-factorable coefficients; a theorem for the **specific Fourier spectrum** of the CRT-idempotent weighted set rather than its support size; coupling many lcm values before Cauchy; genuinely collective variable-length dispersion; modulus factorization that reduces the conductor before scalarization; or a quantitatively useful wraparound/nonunit-shift regime outside `MC-447`.

It remains insufficient for a variable merely to survive notation. The desired analogue of Stadlmann must change usable diagonal/off-diagonal information before scalarization, rather than provide a reversible, Abel-equivalent, Fourier-equivalent, residue-permutation-equivalent, complete-period-equivalent, ambient-L2-equivalent, CRT-fibre-equivalent, uniform-Fourier-envelope-equivalent, or complement-equivalent coordinate system.

## Why it may matter

The sequence `MC-446`--`MC-449` now distinguishes four levels that were previously conflated. The incomplete translated family really has collective cancellation; conditioning on the lcm really improves the generic analytic tariff by one conductor power; the actual fixed-lcm source image is still far too sparse to pay that reduced tariff at fixed-power incomplete lengths; and the near-complete interval does not evade the deficit because its centered source-sensitive part is exactly the complementary short interval. This identifies exactly what a future restricted-frame theorem must use beyond support cardinality, a black-box Weil bound, and interval length alone.

A positive result on the detailed weighted CRT spectrum, cross-lcm dispersion, or conductor factorization would supply the first source-specific mechanism not already absorbed by the existing compression results. Conversely, if those structures also reduce to a polynomial occupancy tariff, the well-factorable/q-vdC branch would be close to a genuine closure rather than merely lacking a strong enough individual character-sum estimate.

## Decisive test

For the lcm branch, exhibit a nontrivial bound for the truncated lcm/source form or a collective source-signature/bilinear estimate and identify the ingredient absent for generic coefficients and a generic quadratic character. Propagate it through the source-frame argument with every source-depth factor, common-radical power, exceptional set, logarithmic loss and truncation error visible. Reject any argument whose only gain is one of the already classified coordinate changes in `MC-397`--`MC-408`.

For the factorable upper-sieve branch, start from `MC-413` and the exact restrictions `MC-446`--`MC-449`. In the clean prime-conductor regime `(h,P(z))=1`, `D^2<p`, a fixed-lcm argument must now prove more than a uniform Weil envelope or choose a near-complete interval: compute or bound the **weighted Fourier mass of the actual CRT-idempotent start set** strongly enough that the correlation between `widehat W(t)` and the translated-character multiplier `widehat f_a(t)D_H(t)` beats the effective-occupancy barrier after centering and complement symmetry. Alternatively, retain several lcm/factor variables before Cauchy and prove a dispersion estimate whose diagonal is parametrically smaller after the true well-factorable coefficients are inserted, or factor the source conductor before the fixed-lcm scalarization occurs.

Reject a continuation if it applies individual incomplete character-sum bounds to each divisor pair, applies Cauchy against the full box and fails `MC-446`, completes first and falls back to `c_q(h)` as in `MC-413`, attributes a gain to collisions excluded by `MC-447`, fixes one lcm and uses only `max_t |widehat f_a(t)|=O(sqrt(p))` plus Parseval as in `MC-448`, or claims that `H` close to `p` lowers the source tariff without first subtracting the zero mode and applying `MC-449`.

## Evidence boundary

No theorem using the actual Selberg lcm coefficient has changed the source-cost scaling, and no factorable-upper-sieve estimate has yet beaten the existing source-character bound. `MC-409` establishes only the alternative positive frame; `MC-410`--`MC-413` classify successive separable, degenerate, or complete-period reductions.

`MC-446` is an exact ambient two-variable moment calculation. `MC-447` is exact CRT fibre algebra. `MC-448` is a finite Fourier/Weil consequence for a fixed-lcm prime-conductor slice. `MC-449` is an exact centered complement identity plus the resulting occupancy consequence. None proves that the actual weighted CRT set lacks a sharper restricted estimate, and `MC-448`--`MC-449` deliberately discard the detailed spectrum of the well-factorable source weights when they replace the translated-character multiplier by a uniform `O(sqrt(p))` envelope.

Cross-lcm weighted cancellation, detailed CRT Fourier geometry, smooth/composite modulus factorization, collective variable-length structure and the wraparound/nonunit-shift regimes remain unexploited. The scalar Möbius--PNT-error branch remains classified by `MC-408` as RH-equivalent at the target exponent.

## Research disposition

The clue remains `accepted` and is **materially narrowed by `MC-446`--`MC-449`**. Generic full-box averaging is blocked by quadratic occupancy; hidden frame multiplicity and a free `a` coordinate are absent in the clean separated regime; conditioning on one lcm plus uniform mixed-Weil Fourier control still requires polynomial occupancy at fixed-power incomplete length; and centered complement duality removes the apparent near-complete loophole. Across all interval lengths, generic one-lcm occupancy can yield at most a subpolynomial conductor gain.

The live well-factorable question must therefore exploit detailed weighted CRT Fourier structure, cross-lcm coupling, modulus factorization, genuinely collective variable lengths, or a regime outside the current clean hypotheses. The independent truncated-lcm/source-specific branch remains open.