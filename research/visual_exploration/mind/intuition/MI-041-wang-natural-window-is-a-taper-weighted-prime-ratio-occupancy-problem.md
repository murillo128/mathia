# MI-041 — Wang natural windows are a taper-weighted prime-ratio occupancy problem

**Evidence level:** exact synthesis from `VIS-313`--`VIS-316` plus the classical separated-frequency large sieve.

The cutoff-free Wang remainder no longer has a meaningful global nearest-frequency spacing: the full cross-base ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and retaining two-prime sparsity gives the prime-prime shell energy

`E_M^pp << M v_x(M)^4 log^2 M`.

VIS-315 shows that the remaining finite-window loss is controlled by the number `kappa_M(V)` of actual prime-ratio frequencies in one Fourier cell of width `O(1/V)`, not by the minimum spacing of all reduced rational ratios. A coloring argument gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

Moreover a frequency cluster around one represented ratio `u/v` is exactly, up to constants, a thin determinant-strip problem

`|qv-ur| << M^2/V`

with all primes at scale `M`. The unresolved harmonic-analysis tariff has therefore been converted into a concrete local-density question for prime ratios.

VIS-316 then shows that the destination does not need a uniform density theorem over all shells. If

`kappa_M(V) << 1 + A_M M^2/(V log^2 M)`,

the dyadic recombination sees only

`B(x,V)=sum_M w(M/x) sqrt(A_M)`,

with `w(r)=r^(7/2)` below `1` and `w(r)=r^(-1/2)` above `1`. At the natural scale `V~H~x log log x`, it is enough that

`B=o((log log x)^(3/2))`.

The reusable lesson is to **price local spectral crowding through the exact taper used by the destination before asking for a worst-case density theorem**. Remote exceptional shells can be harmless after weighting, while persistent excess near `M~x` is genuinely expensive. The sharp next arithmetic input is therefore a taper-weighted determinant-strip/local-energy estimate, or a coherent central cluster that demonstrably violates it.

**Boundary.** No prime-ratio occupancy theorem is proved by this synthesis, and the criterion is mean-square in starting height rather than pointwise. Nearby sparse-large-sieve or Beatty-prime results do not automatically supply the moving-slope two-prime estimate. No stronger RH criterion follows without the missing density/energy input and the remaining destination steps.
