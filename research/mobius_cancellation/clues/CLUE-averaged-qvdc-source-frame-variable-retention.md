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
---

# Can a genuinely nonseparable arithmetic variable or lcm transform beat the source-depth barrier?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) gives a concrete nearby mechanism: her modified q-van der Corput argument retains an arithmetic summation variable inside differencing. In the proof sketch, the earlier treatment does not exploit the `y`-sum and its diagonal forces `Delta<N/Y^2`; after reorganizing the congruence so that both `n` and `y` remain inside q-vdC, the diagonal contributes `O(Delta N/Y)` and permits `Delta<N/Y`.

`MC-397` performs the corresponding pre-modewise source summation exactly in the present endpoint Selberg/Bombieri frame. The source-mode index is Fourier-dual rather than an arithmetic summation variable: summing it produces a source-signature weight, and the uniform source average becomes a multiplicative subgroup projector. Thus the source index itself cannot supply Stadlmann's retained-variable gain in this representation.

`MC-398` tests the most literal Selberg-divisor escape inside the already-squared majorant. The two labels `(d_1,d_2)` enter the arithmetic inner sum only through `ell=[d_1,d_2]`; exact regrouping replaces the whole pair fiber by one scalar coefficient `C_g(ell)`. Therefore the pair labels themselves are not independent arithmetic samples.

`MC-399` now tests the remaining standard lcm coordinate. After finite source Fourier expansion the incidence sum is exactly

`sum_I sum_ell C_g(ell) chi_I(ell) M_I(N/ell)`.

Complete multiplicativity gives `chi_I(ell m)=chi_I(ell)chi_I(m)`, so the scalar `chi_I(ell)` cancels at the first additive van-der-Corput correlation in `m`. The lcm coordinate therefore does not remain nonseparably inside the source-character phase and cannot reproduce Stadlmann's specific diagonal-thinning mechanism merely by being left visible in the standard representation.

## Research question

The retained-variable question is now narrower and has two legitimate forms.

First, can the **twisted lcm/end-point transform**

`sum_ell C_g(ell) chi_I(ell) M_I(N/ell)`

or its equivalent source-signature incidence form be estimated collectively in a way that avoids both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive global-radical cost `P^theta`? Any gain here must come from genuine arithmetic cancellation/concentration in the lcm coefficients, signature classes, or moving hyperbola boundary; `MC-399` rules out crediting it to a nonseparable source phase that is not actually present.

Second, can a different **pre-quadratic arithmetic representation** expose a divisor/source variable whose phase or congruence does not factor through `[d_1,d_2]` and does not separate multiplicatively before the relevant Cauchy/q-vdC correlation? This is the remaining direct analogue of Stadlmann's retained-variable mechanism.

A direct structured estimate for the source-signature incidence operator is also admissible when it gives information beyond Fourier-expanding the projector and reapplying the same individual character bounds.

## Why it may matter

Three formal dimensions have now been removed by exact algebra rather than by weak estimates. `MC-397` turns source-mode averaging into a signature projector; `MC-398` turns Selberg divisor-pair multiplicity into one lcm coefficient; `MC-399` shows that the surviving lcm source phase itself separates and disappears under the first additive correlation.

This makes the residual branch substantially more informative. A success can no longer come from keeping one of those indices unevaluated. It must either prove cancellation in the actual lcm/signature coefficient geometry or construct a kernel with genuinely nonseparable arithmetic dependence. A failure of both possibilities would close the retained-variable escape rather than merely repeat the current character-sum barrier in another expansion.

## Decisive test

For the standard lcm route, start from equation `(2)` of `MC-399`. Do **not** count `ell` as an extra q-vdC sample through `chi_I(ell m)`, because `(5)`--`(6)` of that finding prove this dependence separable. Instead isolate the exact operator

`T_I(N)=sum_ell C_g(ell) chi_I(ell) M_I(N/ell)`

and determine whether its lcm coefficient/signature structure or moving hyperbola boundary yields a uniform saving that is not obtainable by termwise bounds on `M_I`. The direction survives only if the resulting estimate changes the source-cost scaling while avoiding both a sequential `2^{-Omega(A)}` differencing tariff and a fixed positive power of the common radical.

For a pre-quadratic alternative, exhibit the proposed arithmetic kernel before estimating it and apply both representation tests already established. It must not factor through the lcm as in `MC-398`, and after source Fourier expansion its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`. Then count the post-Cauchy diagonal exactly and compare it with Stadlmann's genuine retained-variable gain.

Reject a candidate if the supposed extra average is only the source-mode index killed by `MC-397`, if pair labels only repackage one lcm fiber, if complete multiplicativity removes the retained coordinate from the source phase, if arbitrary mode-dependent weights trigger the matched-filter obstruction of `MC-332`, or if the final family estimate has the fixed-global-modulus shape excluded by `MC-383`.

As the literature control, preserve the exact feature of Stadlmann's argument responsible for the gain: an arithmetic summation variable remains coupled inside the differencing/Cauchy geometry and reduces the diagonal count. Similar terminology or an extra visible summation index without that structural effect is not a valid transfer.

## Evidence boundary

No collective estimate for the twisted lcm/end-point transform has been proved, and no genuinely non-lcm-factorable pre-quadratic variable has been exhibited. Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setup and does not imply an endpoint source-cost theorem or improved Möbius cancellation.

`MC-397` resolves the source-index interpretation, `MC-398` resolves the independent divisor-pair interpretation inside the standard squared Selberg majorant, and `MC-399` resolves the standard lcm-as-nonseparable-source-phase interpretation. None of them rules out arithmetic cancellation among the lcm coefficients/signature classes, a useful theorem exploiting the moving endpoint `N/ell`, a direct structured signature-incidence estimate, or a genuinely nonseparable pre-quadratic representation.

## Research disposition

The clue remains accepted but is narrowed to the two surviving mathematical obligations above. The standard lcm variable is no longer a candidate for a Stadlmann-style mixed source-phase q-vdC gain: `MC-399` proves that this phase separates before the first additive correlation. The live question is whether the **twisted lcm/signature hyperbola transform itself has new collective cancellation**, or whether a different pre-quadratic construction exposes an arithmetic variable that survives both lcm compression and source-phase separation while respecting `MC-332` and `MC-383`.