# MI-041 — Wang natural windows require pair-coordinate occupancy on a long-thin Bezout strip

**Evidence level:** exact synthesis from `VIS-313`--`VIS-319` plus the classical separated-frequency large sieve.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing because the full cross-base prime-ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and retaining two-prime sparsity gives the prime-prime shell energy at the correct logarithmic scale.

VIS-315--VIS-316 reduce the finite-window loss to the number of actual prime-ratio frequencies in one Fourier cell. Around a represented ratio `u/v`, the cell becomes the thin determinant strip `|qv-ur| << M^2/V`, and the destination taper only prices a weighted aggregate of shell excesses.

VIS-317--VIS-318 identify two false reductions. Projecting to the scalar determinant `h=qv-ur` erases the two coordinatewise prime exclusions and therefore loses dimension-two sieve density. Freezing `h` keeps `(q,r)` but leaves only `O(1)` same-shell lattice points because the affine step `(u,v)` is itself of size `asymp M`.

VIS-319 supplies the correct exact coordinates. Choose Bezout integers `a,b` with `au-bv=1` and write

`(q,r)=(ut-bh, vt-ah)`.

The map `(t,h)->(q,r)` is unimodular, and modulo every prime `ell` it is a bijection. Exactly `(ell-1)^2` residue pairs have both `q` and `r` nonzero, so the full two-prime local factor `(1-1/ell)^2` is restored. The representation problem is therefore solved at the local sieve-dimension level.

What remains is geometric rather than representational. The shell pulls back to a **long-thin skew domain**: for each determinant coordinate `h`, the `t`-interval has bounded length, while `h` ranges over a long interval. The missing theorem is a uniform upper-bound sieve/congruence-discrepancy estimate on that thin domain, with constants controlled uniformly in the slope/center and strong enough after Wang taper weighting.

The reusable lesson is that coordinate fidelity and averaging length can live in different directions. The unimodular Bezout chart preserves both prime exclusions exactly, while the transverse `h` direction supplies the long family that fixed slices lacked. A viable proof should sieve the joint domain rather than project away the prime coordinates or demand asymptotics on each microscopic fibre.

**Boundary.** VIS-319 restores the local sieve dimension but does not prove the required thin-domain prime occupancy theorem, natural-window Wang estimate or RH consequence. Uniformity in the skew domain and destination-weighted aggregation remain the load-bearing analytic questions.