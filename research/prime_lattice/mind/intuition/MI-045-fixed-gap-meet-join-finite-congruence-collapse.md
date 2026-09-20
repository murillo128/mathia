# MI-045 — Fixed-gap meet/join data collapse to finite congruence decoration

**Evidence level:** exact arithmetic synthesis from [PL-397](../../findings/PL-397-fixed-gap-transition-kernel-is-factorization-blind.md) and [PL-398](../../findings/PL-398-fixed-gap-meet-join-finite-congruence-collapse.md). The conclusion is specific to fixed additive gap and meet/join data determined by `gcd(r,r+d)`; it does not classify separate-vector observables or gaps growing with scale.

In the completed fixed-gap transition layer `q=r+d`, PL-397 leaves a universal archimedean kernel that depends on the gap `d` and transition coordinate but not on the factorization of `r` or `q`. A natural repair is to decorate that kernel by lattice overlap data such as meet/gcd or join/lcm.

PL-398 shows that at **fixed `d`** this repair carries only finite information. The identity `gcd(r,r+d)=gcd(r,d)` forces the meet exponent vector to lie in the finite set indexed by divisors of `d`; only primes dividing `d` can appear. The corresponding join correction is determined by the same finite data. Any meet-only coupling is therefore `d`-periodic and has a finite congruence/Fourier decomposition.

Thus fixed-gap gcd/lcm overlap does not restore the full prime-exponent geometry lost by the universal transition kernel. It only adds a finite periodic decoration to an already additive fixed-gap profile. Increasing the ambient prime lattice or moving to large `r` does not enlarge this information channel while `d` is fixed.

The surviving arithmetic route must retain information not determined by the meet of `r` and `r+d`: separate exponent vectors, divisor data of each endpoint, source weights such as Möbius/von Mangoldt values, cross-level structure, or a gap `d` whose own arithmetic complexity grows. Each such coupling still has to survive exact continuation and interact nontrivially with the transition kernel rather than being appended after scalarization.

**Boundary.** The finite-congruence collapse is not a theorem about all gcd/lcm observables when `d` varies, nor about observables that retain `v(r)` and `v(r+d)` separately. It only closes fixed-gap meet/join data as a source of unbounded prime-lattice discrimination.