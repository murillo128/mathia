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
---

# Can actual lcm/source structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's modified q-van der Corput argument in *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) remains the structural comparison: it keeps an arithmetic summation variable alive through differencing/Cauchy so that the diagonal count genuinely changes.

The source/Selberg frame has already consumed a sequence of superficially richer coordinates. `MC-397` collapses source-mode averaging to a signature projector. `MC-398` compresses the squared Selberg pair `(d_1,d_2)` to the lcm coefficient `C_g(ell)`. `MC-399` shows that complete multiplicativity removes the lcm scalar at the first additive q-vdC correlation. `MC-400` proves that the moving hyperbola family is an invertible Dirichlet-convolution coordinate. `MC-401` classifies the complete endpoint `A_I(B^2)` as a classical signed GCD/divisor-incidence energy with an indefinite local kernel.

`MC-402` resolves the generic representation question at an incomplete endpoint. For `X<B^2`,

`A_I(X)=sum_(n<=X) M(floor(X/n)) E_I(n;B)`,

where each `E_I(n;B)` has the same signed GCD/meet factorization as the complete endpoint, restricted to divisors of `n`. This exact Möbius-inversion identity does **not** make `A_I(X)` Mertens-equivalent and does not rule out a direct truncated-lcm theorem, but it shows that the cutoff mask itself is not a free retained variable.

The later quotient audit closes another tempting escape. `MC-405` exhibits an exact source variable outside the lcm algebra, `b -> M(floor(x/b))`, but its Mangoldt-weighted aggregate is exactly a first-order self-coupling of `M`. `MC-406` shows that the source then factors through only `O(sqrt(x))` floor-quotient fibers; their PNT main kernel is classical harmonic Möbius cancellation. `MC-407` further shows that the apparently extra pairing between `M(k)` and adjacent prime-counting-error increments is just discrete-Abel coordinates for the same Möbius-weighted PNT-error convolution. Even a pointwise power saving for that prime error becomes linear after absolute summation over the quotient variable.

`MC-408` closes the scalar version of that signed escape at the target exponent. For `C(x)=sum_(a<=x) mu(a)E(x/a)`, its Mellin transform is `-zeta'(s)/(s zeta(s)^2)-1/((s-1)zeta(s))`; every nontrivial zeta zero creates a nonremovable pole whose leading order cannot cancel, and `C(x)=O_epsilon(x^(1/2+epsilon))` for every positive `epsilon` is equivalent to RH. The finite sequence `C(1),...,C(N)` is also a triangularly invertible re-encoding of `mu(1),...,mu(N)`. Thus the scalar correlation is neither an independent finite information source nor an easier RH-scale auxiliary target merely because it mixes Möbius and prime-counting error.

`MC-409` changes the status of the alternative-representation branch. The positive square `f=(1*g)^2` is not forced by the prime-frame Hilbert-space argument: an upper-bound linear-sieve divisor sum is also pointwise nonnegative, equals one on shell primes above the sifting range, and has the same `N/log` diagonal scale. Iwaniec's factorable variant of the upper linear sieve additionally gives an exact coefficient convolution before triangle inequality. The resulting off-diagonal has the concrete form `sum_(uv<=D) alpha_u beta_v chi(uv) M_chi(N/(uv))`. This does not yet improve a character estimate and complete multiplicativity still kills a naive `m`-only retained-phase argument, but it supplies a real positive frame representation outside the quadratic Selberg/lcm-coefficient bottleneck.

## Research question

Two branches remain legitimate.

First, can the **actual Selberg/source structure** inside the truncated lcm form produce a theorem that is genuinely stronger than generic cutoff inversion? A surviving result must exploit something specific to the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies. It may use the range `X<B^2`, but the gain must not come merely from rewriting the cutoff with `MC-402` and then inserting an unavailable Mertens estimate.

The useful target is therefore no longer “truncation prevents factorization.” It is a source-specific theorem such as a nontrivial estimate for

`A_I(X)=sum_(ell<=X) C_g(ell) chi_I(ell)`

or for the corresponding joint form

`sum_(ell m<=N) C_g(ell) chi_I(ell) chi_I(m)`

whose proof exploits actual `g`/signature structure and, after complete bookkeeping, avoids both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive common-radical cost `P^theta`.

Second, can a different **pre-quadratic arithmetic representation** expose a coefficient/source variable that survives long enough to change the estimate? `MC-409` now gives one concrete candidate rather than only an abstract requirement: replace the Selberg square by a nonnegative factorable upper linear-sieve weight and work with its pre-triangle convolution `sum alpha_u beta_v chi(uv) M_chi(N/(uv))`. The decisive question is whether bilinear/dispersion/family technology can exploit that coefficient factorization before complete multiplicativity and absolute values collapse it back to individual character sums.

It is still not sufficient that a variable merely avoid lcm factorization. The Mangoldt quotient example shows that a visible source coordinate can scalarize after exact summation into a Mertens self-coupling, while `MC-408` shows that the surviving scalar signed prime-error convolution is itself an RH-equivalent target at square-root scale. The desired analogue of Stadlmann must therefore change usable diagonal/off-diagonal information **before scalarization**, rather than only provide a reversible, Abel-equivalent, or RH-equivalent coordinate system.

## Why it may matter

The representation audit now separates several increasingly strong notions that had previously been easy to conflate: a coordinate may be visible, may survive lcm compression, may change a quotient argument, and may even leave a nontrivial signed scalar correlation, yet still fail to provide independent analytic information after aggregation. `MC-405`--`MC-408` give exact examples of these failures without a power gain.

`MC-409` adds a different kind of surviving structure: not extra incidence data, but a classical convolution law for a positive sieve coefficient family that is compatible with the same prime frame. This is narrower than a new arithmetic invariant but stronger than carrying bookkeeping labels. It produces a precise analytic object on which a no-go or a genuine bilinear gain can now be tested.

## Decisive test

For the lcm branch, exhibit a bound in a nontrivial range `X<B^2` or a collective source-signature/bilinear estimate and identify the exact ingredient not present for generic `g` and a generic quadratic character. Propagate it through the source-frame argument and account explicitly for every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation error. The branch survives only if a strict quantitative gain remains.

Reject an argument if its only new step is one of the already-classified representations: complete endpoint signed-GCD energy (`MC-401`), generic cutoff-to-incidence expansion with Mertens weights (`MC-402`), moving hyperbola inversion (`MC-400`), separable lcm phase (`MC-399`), divisor-pair labels after lcm compression (`MC-398`), source-mode labels after projector collapse (`MC-397`), or the Mangoldt quotient/error family that reduces by exact summation and Abel transformation to `MC-405`--`MC-407`.

`MC-408` shows that the scalar signed relation `sum mu(a)E(x/a)` itself is RH-equivalent at square-root scale. A continuation may still attack that correlation as an RH criterion, but it no longer qualifies as an independent retained-variable mechanism. For this clue, the route survives only if the proof exposes additional phase, congruence, translation, source, coefficient-factorization, or bilinear information **before** scalarization and controls that information independently enough to change the final estimate.

For the factorable upper-sieve route of `MC-409`, start from an actual Iwaniec/linear-sieve factorization, not an arbitrary formal convolution. Preserve the nonnegative total upper-sieve weight needed by the Hilbert-space frame, write the resulting source-character off-diagonal before absolute values, and test a concrete bilinear character-sum, dispersion, or family large-sieve theorem against its exact hypotheses. The route survives only if the final source-frame estimate is strictly stronger than applying current individual `M_chi` bounds after triangle inequality. Existing BFI/Maynard/Pascadi distribution theorems are structural prior art, not automatic estimates for this different character-sum geometry.

For any other pre-quadratic alternative, exhibit the kernel before estimating it. It must not factor through the lcm as in `MC-398`; after source expansion, its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`; and after exact aggregation it must not reduce to a scalar Mertens self-coupling, an Abel-equivalent coordinate system, or the RH-equivalent scalar criterion classified by `MC-405`--`MC-408`. Then count the post-Cauchy diagonal exactly and compare the mechanism with Stadlmann's retained-variable gain.

## Evidence boundary

No theorem using the actual Selberg lcm coefficient has yet changed the source-cost scaling, no collective source-signature estimate has escaped the global-modulus horizon, and no factorable-upper-sieve estimate has yet beaten the existing source-character bound. `MC-409` establishes only that positivity, shell-prime normalization, and the correct diagonal scale survive a switch to a well-factorable upper linear-sieve representation, so this alternative is admissible at the frame level.

`MC-402` supplies no bound for `A_I(X)` or `M(x)`. `MC-405`--`MC-407` supply no improved bound for `M(x)` or for the PNT error, and `MC-408` likewise proves no new Mertens estimate: it classifies the remaining scalar signed correlation as an RH-equivalent square-root target and as a finite-prefix re-encoding of Möbius data. Their role is to prevent generic truncation, quotient retention, coordinate changes, or the scalar prime-error correlation itself from being credited as independent arithmetic information.

Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setting and does not imply an endpoint source-cost theorem or improved Möbius cancellation. Likewise, the well-factorable distribution theorems of Bombieri--Friedlander--Iwaniec, Maynard, and Pascadi concern a different modulus/progression geometry and do not by themselves estimate the `MC-409` source-character bilinear form.

## Research disposition

The clue remains `accepted` but now has a concrete alternative representation to test. The original lcm-side obligation is unchanged: exploit the specific Selberg coefficient, source-signature distribution, or a genuinely collective bilinear relation and prove that it changes the source-depth/common-radical scaling without importing Mertens cancellation through `MC-402`.

The strongest immediate alternative is the `MC-409` well-factorable upper-sieve frame. Its next gate is not another representation rewrite but an analytic theorem for the exact bilinear off-diagonal that preserves coefficient factorization long enough to beat the modewise source-depth tariff. Failure of all such estimates would close a real class of positive pre-quadratic sieve representations rather than only another notation choice.

The scalar Möbius--PNT-error branch remains classified by `MC-408`: at the square-root target it is RH-equivalent, so it is not an easier retained-variable intermediate. Any further alternative must remain analytically independent before exact aggregation rather than collapsing to the Möbius--Mangoldt self-coupling, an Abel-equivalent form, or an RH-equivalent scalar target.