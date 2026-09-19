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
---

# Can actual lcm/source structure or a genuinely nonseparable pre-quadratic variable beat the source-depth barrier?

## Observation

`MC-382` shows that the current single-character Cochrane--Granville--Zheng recursion pays one square-root loss per conductor-scale layer, forcing an exponential-in-source-exponent saving tariff and hence a `log log y` analytic horizon. `MC-396` removes the earlier inverse-gap packing loss but leaves that `2^{O(A)}` tariff intact. `MC-383` shows that replacing individual estimates by a generic thin-family mean value is not enough when the theorem still charges a fixed positive power of one global modulus.

Julia Stadlmann's modified q-van der Corput argument in *On primes in arithmetic progressions and bounded gaps between many primes* (Advances in Mathematics 474 (2025), 110190; arXiv:2309.00425) remains the structural comparison: it keeps an arithmetic summation variable alive through differencing/Cauchy so that the diagonal count genuinely changes.

The current source/Selberg frame has now passed six exact representation tests. `MC-397` collapses source-mode averaging to a signature projector. `MC-398` compresses the squared Selberg pair `(d_1,d_2)` to the lcm coefficient `C_g(ell)`. `MC-399` shows that complete multiplicativity removes the lcm scalar at the first additive q-vdC correlation. `MC-400` proves that the moving hyperbola family is an invertible Dirichlet-convolution coordinate. `MC-401` classifies the complete endpoint `A_I(B^2)` as a classical signed GCD/divisor-incidence energy with an indefinite local kernel.

`MC-402` now resolves the generic representation question at an incomplete endpoint. For `X<B^2`,

`A_I(X)=sum_(n<=X) M(floor(X/n)) E_I(n;B)`,

where each `E_I(n;B)` has the same signed GCD/meet factorization as the complete endpoint, restricted to divisors of `n`. This is an exact Möbius-inversion identity. It does **not** make `A_I(X)` Mertens-equivalent and does not rule out a direct truncated-lcm theorem. It does show that the cutoff mask itself is not a free retained variable: the natural incidence resolution of `[d_1,d_2]<=X` introduces the Mertens staircase as its outer coefficient.

## Research question

Two branches remain legitimate.

First, can the **actual Selberg/source structure** inside the truncated lcm form produce a theorem that is genuinely stronger than generic cutoff inversion? A surviving result must exploit something specific to the real coefficient `g`, the source-signature family, or a collective bilinear relation among the incidence energies. It may use the range `X<B^2`, but the gain must not come merely from rewriting the cutoff with `MC-402` and then inserting an unavailable Mertens estimate.

The useful target is therefore no longer “truncation prevents factorization.” It is a source-specific theorem such as a nontrivial estimate for

`A_I(X)=sum_(ell<=X) C_g(ell) chi_I(ell)`

or for the corresponding joint form

`sum_(ell m<=N) C_g(ell) chi_I(ell) chi_I(m)`

whose proof exploits actual `g`/signature structure and, after complete bookkeeping, avoids both the sequential `2^{-Omega(A)}` source-depth tariff and a fixed positive common-radical cost `P^theta`.

Second, can a different **pre-quadratic arithmetic representation** expose a divisor/source variable whose phase or congruence does not factor through `[d_1,d_2]` and remains nonseparable through the relevant Cauchy/q-vdC correlation? This remains the direct analogue of Stadlmann's retained-variable mechanism.

## Why it may matter

The representation audit has now consumed six superficially richer coordinates without using a deep analytic estimate: source modes, divisor-pair labels, the standard lcm source phase, the moving hyperbola endpoint, the complete lcm quadratic statistic, and finally the generic incomplete lcm mask under divisor-incidence resolution.

That leaves a much cleaner distinction. A useful theorem must derive leverage from **source-specific coefficient law or genuinely joint arithmetic**, not from keeping a coordinate visible after an exact reversible or classical incidence transform. This is precisely where a Stadlmann-style gain would have to differ from the current frame.

## Decisive test

For the lcm branch, exhibit a bound in a nontrivial range `X<B^2` or a collective source-signature/bilinear estimate and identify the exact ingredient not present for generic `g` and a generic quadratic character. Propagate it through the source-frame argument and account explicitly for every source-depth factor, common-radical power, exceptional set, logarithmic loss, and truncation error. The branch survives only if a strict quantitative gain remains.

Reject an argument if its only new step is one of the already-classified representations:

- complete endpoint signed-GCD energy (`MC-401`);
- generic cutoff-to-incidence expansion with Mertens weights (`MC-402`);
- moving hyperbola inversion (`MC-400`);
- separable lcm phase (`MC-399`);
- divisor-pair labels after lcm compression (`MC-398`);
- source-mode labels after projector collapse (`MC-397`).

A use of `MC-402` can still be productive only if the proof exploits non-generic structure of the incidence energies and controls the resulting Mertens-weighted combination without assuming the target cancellation.

For a pre-quadratic alternative, exhibit the kernel before estimating it. It must not factor through the lcm as in `MC-398`, and after source Fourier expansion its retained variable must remain nonseparable through the relevant first correlation rather than cancelling as in `MC-399`. Then count the post-Cauchy diagonal exactly and compare the mechanism with Stadlmann's retained-variable gain.

## Evidence boundary

No theorem using the actual Selberg coefficient has yet changed the source-cost scaling, no collective source-signature estimate has escaped the global-modulus horizon, and no genuinely non-lcm-factorable pre-quadratic variable has been exhibited.

`MC-402` supplies no bound for `A_I(X)` or `M(x)`. Its role is narrower: it prevents generic truncation/incidence algebra from being credited as independent arithmetic information. A direct theorem for truncated `A_I(X)` remains open if it uses structure beyond that identity.

Stadlmann's theorem concerns averaged prime distribution to smooth moduli in a different Type I setting and does not imply an endpoint source-cost theorem or improved Möbius cancellation.

## Research disposition

The clue remains `accepted` but is narrower. The lcm-side obligation is now **actual-weight/source-family arithmetic**, not truncation by itself: exploit the specific Selberg coefficient, source-signature distribution, or a genuinely collective bilinear relation and prove that it changes the source-depth/common-radical scaling without importing Mertens cancellation through `MC-402`.

The alternative branch remains unchanged: find a pre-quadratic arithmetic variable that survives both lcm compression and source-phase separation, then verify by an exact post-Cauchy diagonal count that it produces the retained-variable effect missing from the present representation.
