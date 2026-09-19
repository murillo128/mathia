# MI-041 — Wang natural windows reduce to simultaneous-prime occupancy on fixed-gate subperiod mechanical paths

**Evidence level:** exact synthesis from `VIS-313`--`VIS-321` plus classical rational mechanical/Christoffel geometry. No prime-pair occupancy estimate or RH consequence is claimed.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing because the full cross-base prime-ratio spectrum is dense. Dyadic arithmetic-height shells restore finite-resolution structure, and VIS-315--VIS-316 reduce the finite-window loss to the number of actual prime-ratio frequencies in one Fourier cell, with the destination taper pricing a weighted aggregate of shell excesses.

VIS-317--VIS-318 identify two false reductions. Projecting to the scalar determinant erases the two coordinatewise prime exclusions; fixing the determinant keeps those exclusions but leaves only `O(1)` same-shell points. VIS-319 supplies the faithful coordinates: with `au-bv=1`,

`(q,r)=(ut-bh, vt-ah)`

is a unimodular change of variables and preserves exactly the local two-prime factor `(1-1/ell)^2` modulo every prime.

VIS-320 shows that the long-thin domain consists of at most three branches `t_j(h)=floor(U(h))-j`, selected by a rational rotation whose period is `max(u,v) asymp M`. At the natural Wang scale the determinant window has length `O(M/log log M)=o(M)`, so the physical segment sees less than one rotation period. Full-cycle equidistribution is therefore not a substitute for short-orbit prime occupancy.

VIS-321 makes the branch geometry still more rigid. The increment word is binary and common to all branches; its two lattice steps are

`s_0=(-b,-a)`, `s_1=(u-b,v-a)`,

with `det(s_0,s_1)=1`, and the three candidate branches are translates of one rational mechanical/Christoffel path. The actual moving branch threshold can be frozen: on a subperiod interval the moving/frozen masks differ at no more than `1+floor(2D/min(u,v))` indices per branch, which is eventually at most one at `D=O(M/log log M)`.

This removes the affine gate drift from the list of plausible main difficulties. Up to `O(1)` candidate points, the natural Wang cell is a fixed-gate subword of a unimodular mechanical path carrying two simultaneous primality constraints. The live theorem is therefore a short-orbit arithmetic-distribution statement, or a destination-weighted estimate that avoids worst-cell occupancy altogether.

The reusable lesson is that **coordinate fidelity, arithmetic dimension, orbit length, gate motion and destination weighting are separate resources**. A faithful chart can preserve the prime exclusions; a short physical window can still prevent full-period averaging; and a moving threshold can be provably irrelevant once its symmetric difference is below the destination's `O(1)` tolerance. The next theorem should attack only the resource that survives all three reductions.

**Boundary.** VIS-321 does not prove simultaneous-prime density on these paths, a short-interval Beatty/Christoffel prime theorem, the Wang natural-window estimate, or RH. The `O(1)` gate-freezing statement uses the subperiod/natural-scale regime. The remaining slope, prime occupancy and taper-weighted aggregation are genuinely unresolved.