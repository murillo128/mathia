# MI-041 — Wang natural windows require pair-coordinate occupancy across a family of short determinant slices

**Evidence level:** exact synthesis from `VIS-313`--`VIS-318` plus the classical separated-frequency large sieve.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing because the full cross-base prime-ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and retaining two-prime sparsity gives the prime-prime shell energy at the correct logarithmic scale.

VIS-315 shows that the finite-window loss is controlled by the number `kappa_M(V)` of actual prime-ratio frequencies in one Fourier cell of width `O(1/V)`. A frequency cluster around a represented ratio `u/v` becomes a thin determinant strip

`|qv-ur| << M^2/V`

with all four prime coordinates at scale `M`. VIS-316 then shows that the destination does not need a uniform shell theorem: the Wang taper sees only a weighted aggregate of the shell excesses.

VIS-317 identifies the first trap. Passing from `(q,r)` to the scalar determinant `h=qv-ur` preserves the cell geometry, but for every odd prime away from `uv` every residue class of `h` remains compatible with both `q` and `r` nonzero. The determinant quotient has erased the two coordinatewise exclusions that carry the prime-pair sieve dimension. Determinant-only residue sifting therefore cannot recover the desired `log^(-2) M` factor.

VIS-318 identifies the opposite trap. If `h` is frozen and `u/v` is a represented same-shell center, then the integer solutions are

`(q,r)=(q_0,r_0)+t(u,v)`.

Because `u,v asymp M`, changing `t` by one already moves a distance comparable with the shell width. Each exact determinant slice therefore contains only `O(1)` candidate lattice points. The two prime coordinates have been retained, but there is no long affine parameter on a fixed slice over which a dimension-two sieve can obtain its asymptotic density saving.

These two obstructions locate the correct representation between projection and freezing. **The sieve dimension lives in `(q,r)`, while the averaging length lives across many neighboring determinant slices.** A viable occupancy argument must keep both at once: a two-coordinate sieve on the whole thin strip, a rational/Beatty-type organization of the moving short slices, or a weighted/additive-energy argument with equivalent pair information.

The reusable lesson is that preserving the right coordinates is not sufficient if the chosen fibre is too short to average, and having a long aggregate is not sufficient if projection has erased the local exclusions that supply arithmetic saving. The destination taper should price the aggregate only after both information resources are retained.

**Boundary.** VIS-318 applies to represented centers whose primitive step vector is comparable with the shell scale; a deliberately smaller primitive direction would require a new audit. No prime-ratio occupancy theorem, natural-window Wang theorem or stronger RH criterion is proved. The surviving whole-strip sieve/energy mechanisms remain conjectural research directions.