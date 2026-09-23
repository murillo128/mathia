# MI-098 — Complete pair-sieve factorization pushes any new gain into structured incomplete discrepancy

**Evidence level:** exact derived obstructions from [MC-472](../../findings/MC-472-pair-sieve-complete-period-factorizes.md) and [MC-473](../../findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md), inside the staged pair-sieve channel isolated by MC-471.

For a nonprincipal character `chi mod p`, nonzero shift `h mod p`, and square-free small-prime sieve modulus `W` coprime to `p`, put `K_h(n)=chi(n+h) conjugate(chi(n))` and `A_(W,h)(n)=1_((n(n+h),W)=1)`. MC-472 proves that the complete joint period contains no hidden character-versus-sieve resonance:

`sum_(n mod pW) K_h(n) A_(W,h)(n) = -V_W(h)`,

where `V_W(h)=prod_(q|W)(q-nu_q(h))` is exactly the ordinary pair-sieve survivor count. After normalization the complete mean is just the character mean `-1/p` multiplied by the local sieve density `delta_W(h)=V_W(h)/W`. CRT has separated the character phase and small-prime sieve into independent coordinates.

This leaves the centered incomplete discrepancy

`D_(W,h)(I)=sum_(n in I) K_h(n) A_(W,h)(n) + |I| delta_W(h)/p`

as the genuine rough-by-rough object. But MC-473 shows that the most literal attack on it destroys the same structure one needs. Exact Möbius inclusion-exclusion followed by a separate completed Weil bound on every divisor/residue branch gives a tariff

`B_W(h)=sum_(d|W) nu_d(h)=prod_(q|W)(1+nu_q(h))`.

For a primorial pair sieve this lies between `2^omega(W)` and `3^omega(W)` and becomes superpolynomial at a fixed-power sieve cutoff. Each individual progression is easy—its centered translated-ratio character sum is `O(sqrt(p) log p)`—but taking absolute values after branchwise completion converts local forbidden-class choices into exponentially many independent costs. Large `B_W(h)` is therefore a proof-architecture loss, not evidence that the actual discrepancy is large.

Two exact pruning rules remain useful. When the rough sieve contains `2`, every odd shift has zero rough-by-rough population, so that channel is purely even-shift. Averaging `delta_W(h)` through a complete shift period gives `(phi(W)/W)^2`; local enhancements on shifts divisible by sieve primes redistribute density but create no mean gain.

The reusable conclusion is more specific than “prove an incomplete character-sum bound.” A viable conductor-power estimate must keep the pair sieve **compressed while the character phase is still oscillatory**: for example by a quantitatively controlled truncated/factorable sieve, or by a bilinear/dispersion transform that couples divisor levels before triangle/Cauchy closure. Full-period blocking sees only the ordinary density, while full exact inclusion-exclusion plus branchwise completion pays exponential multiplicity. The admissible window lies between those two collapses.

**Boundary.** MC-472 is a complete-period identity and MC-473 is a no-go for one termwise proof architecture, not a lower bound on `|D_(W,h)(I)|`. Structured sifted-character estimates remain live and must price their approximation/error explicitly. Mixed rough/boundary channels, first-exit terms, retained outer signs and pre-positive cross-component interference are distinct carriers. No Möbius, zero-free-region or RH consequence follows.