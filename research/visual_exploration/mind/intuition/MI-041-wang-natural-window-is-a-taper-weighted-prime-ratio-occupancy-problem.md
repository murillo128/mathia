# MI-041 — Wang natural windows are a taper-weighted prime-ratio occupancy problem whose sieve must remain two-coordinate

**Evidence level:** exact synthesis from `VIS-313`--`VIS-317` plus the classical separated-frequency large sieve.

The cutoff-free Wang remainder no longer has a meaningful global nearest-frequency spacing: the full cross-base ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and retaining two-prime sparsity gives the prime-prime shell energy

`E_M^pp << M v_x(M)^4 log^2 M`.

VIS-315 shows that the remaining finite-window loss is controlled by the number `kappa_M(V)` of actual prime-ratio frequencies in one Fourier cell of width `O(1/V)`, not by the minimum spacing of all reduced rational ratios. A coloring argument gives

`V^(-1) integral |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

Moreover a frequency cluster around one represented ratio `u/v` is, up to constants, a thin determinant-strip problem

`|qv-ur| << M^2/V`

with all primes at scale `M`. VIS-316 shows that the destination does not need a uniform density theorem over all shells. If

`kappa_M(V) << 1 + A_M M^2/(V log^2 M)`,

the dyadic recombination sees only `B(x,V)=sum_M w(M/x) sqrt(A_M)`, with `w(r)=r^(7/2)` below `1` and `w(r)=r^(-1/2)` above `1`. At the natural scale `V~H~x log log x`, it is enough that `B=o((log log x)^(3/2))`.

VIS-317 identifies a crucial loss in the tempting scalar reduction `h=qv-ur`. For every odd prime `ell` not dividing `uv`, the number of nonzero pairs `(q,r) mod ell` with determinant `h` is exactly `ell-1` when `h=0` and `ell-2` otherwise. Hence **no odd-prime residue class of `h` is forbidden** by the two primality conditions. The determinant coordinate preserves the geometric cell width because `|q/r-u/v|=|h|/(rv)`, but it compresses the two coordinatewise prime exclusions into multiplicities. Determinant-only residue sifting therefore cannot recover the two-prime `log^(-2) M` density scale.

The reusable lesson is to price local spectral crowding through the destination taper **without quotienting away the arithmetic dimension that supplies the saving**. The determinant is an excellent geometric coordinate for a ratio cell, but the sieve should still act on `(q,r)` or on a one-parameter determinant slice where `q` and `r` remain two affine linear forms. A weighted/additive-energy route is also viable only if it retains equivalent two-coordinate information.

**Boundary.** No prime-ratio occupancy theorem is proved by this synthesis, and the criterion is mean-square in starting height rather than pointwise. VIS-317 rules out only determinant-only residue sifting; it does not exclude a two-coordinate Selberg sieve, a singular-series treatment depending on `h`, affine-linear-form methods on fixed determinant slices, or coefficient-weighted energy estimates. No stronger RH criterion follows without the missing density/energy input and the remaining destination steps.
