# MI-041 — Wang natural windows reduce to simultaneous-prime occupancy on subperiod rational-rotation branches

**Evidence level:** exact synthesis from `VIS-313`--`VIS-320` plus the classical separated-frequency large sieve.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing because the full cross-base prime-ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and retaining two-prime sparsity gives the prime-prime shell energy at the correct logarithmic scale.

VIS-315--VIS-316 reduce the finite-window loss to the number of actual prime-ratio frequencies in one Fourier cell. Around a represented ratio `u/v`, the cell becomes the thin determinant strip `|qv-ur| << M^2/V`, and the destination taper only prices a weighted aggregate of shell excesses.

VIS-317--VIS-318 identify two false reductions. Projecting to the scalar determinant `h=qv-ur` erases the two coordinatewise prime exclusions and therefore loses dimension-two sieve density. Freezing `h` keeps `(q,r)` but leaves only `O(1)` same-shell lattice points because the affine step `(u,v)` is itself of size `asymp M`.

VIS-319 supplies the correct exact coordinates. Choose Bezout integers `a,b` with `au-bv=1` and write

`(q,r)=(ut-bh, vt-ah)`.

The map `(t,h)->(q,r)` is unimodular, and modulo every prime `ell` it is a bijection. Exactly `(ell-1)^2` residue pairs have both `q` and `r` nonzero, so the full two-prime local factor `(1-1/ell)^2` is restored.

VIS-320 shows that the resulting long-thin domain is much more rigid than a generic skew lattice region. Under the natural condition `D<M/2`, the active lower and upper shell boundaries do not switch as `h` moves, the `t`-width is always below `3`, and every lattice point lies on one of at most three branches

`t_j(h)=floor(U(h))-j`, `j=0,1,2`,

selected by the exact mask `{U(h)}+j<W(h)`. The fractional part `{U(h)}` is a rational rotation with exact period `max(u,v)`.

At the Wang resolution `D asymp M/log log M`, this period is `asymp M` while the full determinant segment has length `O(D)=o(M)`. The natural window therefore samples **less than one rational period**. Full-cycle residue balance cannot justify prime occupancy on the actual segment, even though the local two-prime exclusions are perfectly preserved.

The live theorem is now a one-parameter arithmetic-distribution problem: uniformly control simultaneous primality of

`q_j(h)=u t_j(h)-bh`, `r_j(h)=v t_j(h)-ah`

on at most three moving mechanical branches over a subperiod rational orbit, then feed the resulting shell excess into the taper-weighted criterion of VIS-316. A generic two-dimensional sieve theorem may be sufficient but is no longer the minimal object; a full-period rational equidistribution theorem is insufficient because the physical window ends before one cycle.

The reusable lesson is that coordinate fidelity, averaging length and periodicity scale are separate resources. The unimodular Bezout chart preserves the source exclusions, the transverse `h` coordinate supplies the family length, and VIS-320 identifies when that length is too short to average a rational orbit globally. A viable proof must use all three scales in the form consumed by the destination taper.

**Boundary.** VIS-320 proves no prime-pair occupancy estimate, short-interval Beatty theorem in this moving rational regime, Wang natural-window bound or RH consequence. It only replaces the generic thin-domain frontier by at most three exact subperiod rational-rotation branches carrying both prime coordinates.