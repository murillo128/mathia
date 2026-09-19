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
---

# Can independent lcm-coefficient structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) gives a nearby but structurally different mechanism: a modified q-van der Corput argument retains an arithmetic `y`-summation variable inside the differencing/Cauchy geometry, reducing the diagonal count and enlarging the admissible parameter range.

The endpoint source/Selberg frame has now passed four exact representation tests. `MC-397` shows that pre-modewise source averaging Fourier-collapses to a source-signature projector, so the source-mode index is not an extra arithmetic sample. `MC-398` shows that the squared Selberg divisor pair `(d_1,d_2)` enters the arithmetic only through `ell=[d_1,d_2]`, with the pair fiber compressed to one coefficient `C_g(ell)`. `MC-399` shows that complete multiplicativity separates `chi_I(ell m)` and removes the lcm scalar at the first additive q-vdC correlation, so `ell` is not a Stadlmann-style mixed source-phase variable.

`MC-400` now classifies the remaining moving-boundary escape. For a fixed source mode define

`A_I(X)=sum_{ell<=X} C_g(ell) chi_I(ell)`

and

`T_I(N)=sum_{n<=N} f(n) chi_I(n)`.

The standard lcm transform has the exact pair

`T_I(N)=sum_m chi_I(m) A_I(N/m)`

and

`A_I(N)=sum_d mu(d) chi_I(d) T_I(N/d)`.

Thus the moving hyperbola boundary is a reversible summatory Dirichlet-convolution representation. Keeping `N/ell` visible does not by itself supply a new arithmetic dimension. Any useful standard-lcm route must inject independent information about `C_g`, its source-signature distribution, or a genuinely joint bilinear structure rather than cycling through this inversion pair.

## Research question

The retained-variable question now has two legitimate branches.

First, can one prove an **independent lcm-coefficient/signature theorem** strong enough to change the source-cost scaling? The clean target is the twisted partial sum

`A_I(X)=sum_{ell<=X} C_g(ell) chi_I(ell)`,

or the corresponding sums restricted to source-signature classes. A successful estimate must be derived from special arithmetic structure of the Selberg weights/lcm fibers, or from a genuinely collective bilinear theorem, and must avoid both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive common-radical cost `P^theta`. It does not count to obtain `A_I` from the inverse formula in `MC-400` and feed it back into the forward formula without an independent quantitative gain.

Second, can a different **pre-quadratic arithmetic representation** expose a divisor/source variable whose phase or congruence does not factor through `[d_1,d_2]` and remains nonseparable through the relevant Cauchy/q-vdC correlation? This remains the direct analogue of Stadlmann's retained-variable mechanism.

A direct structured source-signature incidence estimate is admissible under the first branch when it proves information about the actual lcm/signature coefficient distribution rather than merely Fourier-expanding the same projector and reapplying the existing individual character bounds.

## Why it may matter

Four apparent extra dimensions have now been separated from the actual analytic content by exact algebra: source-mode averaging, the Selberg divisor-pair labels, the lcm factor inside the source phase, and the moving hyperbola boundary considered merely as a new sample coordinate. This sharply reduces the risk of mistaking a richer notation for a stronger estimate.

The surviving standard-lcm branch is consequently concrete: prove new arithmetic control of `C_g(ell) chi_I(ell)` or its signature classes and quantify how that control propagates through the hyperbola transform. If that also fails at the source-depth/common-radical barrier, the remaining escape is no longer another rearrangement of the squared Selberg frame but a genuinely different pre-quadratic kernel.

## Decisive test

For the standard-lcm branch, derive a bound for `A_I(X)` or the signature-class analog **directly from the structure of `C_g` and the source family**, or prove a joint bilinear estimate for

`sum_{ell m<=N} C_g(ell) chi_I(ell) chi_I(m)`

whose gain is not a formal consequence of the convolution identities in `MC-400`. Propagate the estimate to `T_I(N)` and account explicitly for every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation. The direction survives only if a strict quantitative improvement remains after that accounting.

Reject an argument if its only new step is the moving boundary `m<=N/ell`; `MC-400` proves that the resulting scale-indexed lcm and Selberg partial sums are exact Möbius-inversion partners. Also reject a purported lcm gain if it merely treats `chi_I(ell m)` as nonseparable (`MC-399`), keeps the divisor-pair labels after they have collapsed to an lcm fiber (`MC-398`), or reuses the source-mode index after its exact projector collapse (`MC-397`). Generic family estimates with a fixed positive global-modulus cost remain subject to `MC-383`.

For a pre-quadratic alternative, exhibit the kernel before estimating it. It must not factor through the lcm as in `MC-398`, and after source Fourier expansion its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`. Then count the post-Cauchy diagonal exactly and compare the mechanism with Stadlmann's genuine retained-variable gain.

## Evidence boundary

No independent estimate for `A_I(X)` or its source-signature class analog has been proved, and no genuinely non-lcm-factorable pre-quadratic variable has been exhibited. `MC-400` does not rule out a useful lcm theorem; it only rules out crediting the reversible hyperbola representation itself as additional arithmetic information.

Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setting and does not imply an endpoint source-cost theorem or improved Möbius cancellation. None of `MC-397`--`MC-400` yields a bound for the Mertens function.

## Research disposition

The clue remains `accepted` but is narrower. The standard-lcm branch is now **an arithmetic theorem obligation**: obtain independent cancellation/concentration for `C_g(ell) chi_I(ell)`, source-signature lcm sums, or a genuinely collective bilinear form, and show that it changes the source-depth/common-radical scaling. The moving boundary alone is no longer a candidate mechanism after `MC-400`.

The second branch remains unchanged: find a pre-quadratic arithmetic variable that survives both lcm compression and source-phase separation and then verify, by an exact post-Cauchy diagonal count, that it produces the retained-variable effect missing from the present representation.