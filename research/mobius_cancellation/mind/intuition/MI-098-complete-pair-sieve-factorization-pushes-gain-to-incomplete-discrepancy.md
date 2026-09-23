# MI-098 — Complete pair-sieve factorization pushes any new gain into structured incomplete discrepancy

**Evidence level:** exact derived obstructions from [MC-472](../../findings/MC-472-pair-sieve-complete-period-factorizes.md), [MC-473](../../findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md), and [MC-474](../../findings/MC-474-pair-sieve-fourier-spectral-norm-is-exponential.md), inside the staged pair-sieve channel isolated by MC-471.

For a nonprincipal character `chi mod p`, nonzero shift `h mod p`, and square-free small-prime sieve modulus `W` coprime to `p`, put `K_h(n)=chi(n+h) conjugate(chi(n))` and `A_(W,h)(n)=1_((n(n+h),W)=1)`. MC-472 proves that the complete joint period contains no hidden character-versus-sieve resonance:

`sum_(n mod pW) K_h(n) A_(W,h)(n) = -V_W(h)`,

where `V_W(h)=prod_(q|W)(q-nu_q(h))` is exactly the ordinary pair-sieve survivor count. After normalization the complete mean is just the character mean `-1/p` multiplied by the local sieve density `delta_W(h)=V_W(h)/W`. CRT has separated the character phase and small-prime sieve into independent coordinates.

This leaves the centered incomplete discrepancy

`D_(W,h)(I)=sum_(n in I) K_h(n) A_(W,h)(n) + |I| delta_W(h)/p`

as the genuine rough-by-rough object. MC-473 shows that the most literal attack on it destroys the same structure one needs. Exact Möbius inclusion-exclusion followed by a separate completed Weil bound on every divisor/residue branch gives a tariff

`B_W(h)=sum_(d|W) nu_d(h)=prod_(q|W)(1+nu_q(h))`.

For a primorial pair sieve this lies between `2^omega(W)` and `3^omega(W)` and becomes superpolynomial at a fixed-power sieve cutoff. Each individual progression is easy—its centered translated-ratio character sum is `O(sqrt(p) log p)`—but taking absolute values after branchwise completion converts local forbidden-class choices into exponentially many independent costs. Large `B_W(h)` is therefore a proof-architecture loss, not evidence that the actual discrepancy is large.

MC-474 shows that exact additive Fourier compression does not by itself repair this loss. The normalized Fourier transform of the intact pair-sieve mask tensorizes over sieve primes, and

`||Ahat_(W,h)||_1 = prod_(q|W) L_q(h)`

with `L_q(h)>=7/5` for every `q>=5`. Hence every nonzero primorial channel has an exponentially large Fourier `l^1` norm. A uniform `O(sqrt(p) log p)` estimate for each twisted mode, followed by triangle inequality, therefore pays the full `||Ahat||_1` tariff and is again superpolynomial at a fixed-power cutoff.

The new distinction is that this is **not** a Fourier-energy obstruction. Parseval gives

`||Ahat_(W,h)||_2^2=delta_W(h)`

and, after removing the mean,

`||widehat(A_(W,h)-delta_W(h))||_2^2=delta_W(h)(1-delta_W(h))`.

So exact compression has retained a low-energy coefficient vector even though coefficientwise absolute recombination is expensive. The surviving Fourier route must exploit correlation between that vector and the family of twisted translated-ratio sums before `l^1` scalarization—for example through a restriction, large-sieve, bilinear or dispersion norm. Equivalently, a truncated/factorable pair sieve is useful only if both its approximation error and the joint norm seen by the character family are quantitatively affordable.

Two exact pruning rules remain useful. When the rough sieve contains `2`, every odd shift has zero rough-by-rough population, so that channel is purely even-shift. Averaging `delta_W(h)` through a complete shift period gives `(phi(W)/W)^2`; local enhancements on shifts divisible by sieve primes redistribute density but create no mean gain.

The reusable conclusion is more specific than “prove an incomplete character-sum bound.” A viable conductor-power estimate must keep the pair sieve **compressed while the character phase is still oscillatory and before absolute values separate its modes**. Full-period blocking sees only the ordinary density; full exact inclusion-exclusion plus branchwise completion pays exponential divisor multiplicity; exact Fourier expansion plus independent modewise completion pays exponential spectral `l^1` norm despite small `l^2` energy. The admissible window is therefore a genuinely joint estimate, not another exact reparametrization followed by pointwise control.

**Boundary.** MC-472 is a complete-period identity, while MC-473 and MC-474 are no-go results for two scalarized proof architectures, not lower bounds on `|D_(W,h)(I)|`. The small Fourier `l^2` energy does not itself imply a useful restriction estimate or power saving; such a theorem must still couple the exact pair-sieve coefficients to the translated-ratio character family. Structured sifted-character estimates remain live and must price their approximation/error explicitly. Mixed rough/boundary channels, first-exit terms, retained outer signs and pre-positive cross-component interference are distinct carriers. No Möbius, zero-free-region or RH consequence follows.