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

`MC-409` changes the status of the alternative-representation branch. The positive square `f=(1*g)^2` is not forced by the prime-frame Hilbert-space argument: an upper-bound linear-sieve divisor sum is also pointwise nonnegative, equals one on shell primes above the sifting range, and has the same `N/log` diagonal scale. Iwaniec's factorable variant of the upper linear sieve additionally gives an exact coefficient convolution before triangle inequality. The resulting off-diagonal has the concrete form `sum_(uv<=D) alpha_u beta_v chi(uv) M_chi(N/(uv))`. This supplies a real positive frame representation outside the quadratic Selberg/lcm-coefficient bottleneck.

`MC-410` and `MC-411` sharply restrict what can be credited to that representation. `MC-410` proves that the raw source phase `chi(uvm)` is tensor-separable and that a smooth product cutoff is Mellin-diagonal. `MC-411` then shows that ordinary additive Fourier/Poisson completion does not manufacture a missing interaction: the apparent dual phase `e(h u v m/q)` is removed exactly by the unit permutation `h -> h uv`, leaving the same scalar `chi(uv)` and only archimedean scale dependence. Thus neither coefficient factorization, product localization, nor plain completion creates the Stadlmann-style retained arithmetic variable.

## Research question

Two branches remain legitimate.

First, can the **actual Selberg/source structure** inside the truncated lcm form produce a theorem that is genuinely stronger than generic cutoff inversion? A surviving result must exploit something specific to the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies. It may use the range `X<B^2`, but the gain must not come merely from rewriting the cutoff with `MC-402` and then inserting an unavailable Mertens estimate.

The useful target is therefore no longer “truncation prevents factorization.” It is a source-specific theorem such as a nontrivial estimate for

`A_I(X)=sum_(ell<=X) C_g(ell) chi_I(ell)`

or for the corresponding joint form

`sum_(ell m<=N) C_g(ell) chi_I(ell) chi_I(m)`

whose proof exploits actual `g`/signature structure and, after complete bookkeeping, avoids both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive common-radical cost `P^theta`.

Second, can a different **pre-quadratic arithmetic representation** expose a coefficient/source variable that survives long enough to change the estimate? `MC-409` supplies the positive well-factorable upper-sieve frame, but `MC-410`--`MC-411` show that its bare product-character form is too diagonal: even completion only permutes dual modes. The live question is therefore whether an identity or dispersion step can create a congruence, additive translation, reciprocal phase, or another genuinely nonseparable relation **before** coefficient factorization is consumed by Cauchy/triangle inequalities.

It is still not sufficient that a variable merely avoid lcm factorization. The Mangoldt quotient example shows that a visible source coordinate can scalarize after exact summation into a Mertens self-coupling, while `MC-408` shows that the surviving scalar signed prime-error convolution is itself an RH-equivalent target at square-root scale. The desired analogue of Stadlmann must therefore change usable diagonal/off-diagonal information **before scalarization**, rather than only provide a reversible, Abel-equivalent, Fourier-equivalent, or RH-equivalent coordinate system.

## Why it may matter

The representation audit now separates several increasingly strong notions that had previously been easy to conflate: a coordinate may be visible, may survive lcm compression, may change a quotient argument, may survive as a coefficient convolution, and may even display an apparently bilinear Fourier phase, yet still fail to provide independent analytic information after exact reindexing or aggregation.

`MC-409` remains important because it supplies a positive frame with classical coefficient factorization. But `MC-410`--`MC-411` show that the gain, if any, must come from **new arithmetic geometry introduced before estimation**, not from the factorization or completion syntax itself. This leaves a more precise target on which a dispersion theorem can be accepted or killed.

## Decisive test

For the lcm branch, exhibit a bound in a nontrivial range `X<B^2` or a collective source-signature/bilinear estimate and identify the exact ingredient not present for generic `g` and a generic quadratic character. Propagate it through the source-frame argument and account explicitly for every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation error. The branch survives only if a strict quantitative gain remains.

Reject an argument if its only new step is one of the already-classified representations: complete endpoint signed-GCD energy (`MC-401`), generic cutoff-to-incidence expansion with Mertens weights (`MC-402`), moving hyperbola inversion (`MC-400`), separable lcm phase (`MC-399`), divisor-pair labels after lcm compression (`MC-398`), source-mode labels after projector collapse (`MC-397`), or the Mangoldt quotient/error family that reduces by exact summation and Abel transformation to `MC-405`--`MC-407`.

`MC-408` shows that the scalar signed relation `sum mu(a)E(x/a)` itself is RH-equivalent at square-root scale. A continuation may still attack that correlation as an RH criterion, but it no longer qualifies as an independent retained-variable mechanism. For this clue, the route survives only if the proof exposes additional phase, congruence, translation, source, coefficient-factorization, or bilinear information **before** scalarization and controls that information independently enough to change the final estimate.

For the factorable upper-sieve route, start from the actual `MC-409` factorization and write the first transformed kernel explicitly. `MC-410` forbids credit for the raw `chi(uvm)` tensor product, and `MC-411` forbids credit for an additive completion whose only apparent coupling is `e(h u v m/q)`, because `h -> h uv` removes it. The branch now survives only if a pre-estimation identity creates a relation that is not equivariant under this unit reindexing: for example a translated character phase, a congruence comparing independently varying products, or a reciprocal/Kloosterman-type phase generated intrinsically by dispersion. Then count the post-Cauchy diagonal and propagate the actual modulus/source cost. Existing BFI/Maynard/Pascadi theorems remain structural prior art, not automatic estimates for this source-character geometry.

For any other pre-quadratic alternative, exhibit the kernel before estimating it. It must not factor through the lcm as in `MC-398`; after source expansion, its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`; and after exact aggregation it must not reduce to a scalar Mertens self-coupling, an Abel/Fourier-equivalent coordinate system, or the RH-equivalent scalar criterion classified by `MC-405`--`MC-408`. Then count the post-Cauchy diagonal exactly and compare the mechanism with Stadlmann's retained-variable gain.

## Evidence boundary

No theorem using the actual Selberg lcm coefficient has yet changed the source-cost scaling, no collective source-signature estimate has escaped the global-modulus horizon, and no factorable-upper-sieve estimate has yet beaten the existing source-character bound. `MC-409` establishes only that positivity, shell-prime normalization, and the correct diagonal scale survive a switch to a well-factorable upper linear-sieve representation. `MC-410` and `MC-411` are negative structural classifications: they prove that raw multiplicative factorization, Mellin localization, and ordinary Fourier/Poisson completion do not themselves create the missing nonseparable source variable.

`MC-402` supplies no bound for `A_I(X)` or `M(x)`. `MC-405`--`MC-407` supply no improved bound for `M(x)` or for the PNT error, and `MC-408` likewise proves no new Mertens estimate: it classifies the remaining scalar signed correlation as an RH-equivalent square-root target and as a finite-prefix re-encoding of Möbius data.

Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setting and does not imply an endpoint source-cost theorem or improved Möbius cancellation. Likewise, the well-factorable distribution theorems of Bombieri--Friedlander--Iwaniec, Maynard, and Pascadi concern a different modulus/progression geometry and do not by themselves estimate the `MC-409` source-character form.

## Research disposition

The clue remains `accepted` but is narrower. The original lcm-side obligation is unchanged: exploit the specific Selberg coefficient, source-signature distribution, or a genuinely collective bilinear relation and prove that it changes the source-depth/common-radical scaling without importing Mertens cancellation through `MC-402`.

For the well-factorable frame, the next gate is now **not** generic bilinear character sums and not ordinary completion. A continuation must derive an actual nonseparable arithmetic relation before estimation, verify that it is not removable by multiplicativity or dual-mode permutation, and only then test whether well-factorability lowers the resulting diagonal/source cost. Failure at that step would close a substantially more precise class of positive pre-quadratic sieve representations.

The scalar Möbius--PNT-error branch remains classified by `MC-408`: at the square-root target it is RH-equivalent, so it is not an easier retained-variable intermediate. Any further alternative must remain analytically independent before exact aggregation rather than collapsing to the Möbius--Mangoldt self-coupling, an Abel/Fourier-equivalent form, or an RH-equivalent scalar target.