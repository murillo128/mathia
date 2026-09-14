# MI-016 — Coherent unresolved prime blocks already force super-RMS Ising energy

**Evidence level:** exact consequence of [VIS-192](../../findings/VIS-192-long-start-variance-scale.md), VIS-218, VIS-223--VIS-224 and [VIS-225](../../findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md) in the strictly subcritical midpoint-symmetric taper regime. No critical/supercritical or access-time conclusion is claimed.

After midpoint gauge, the relevant static prime-phase problem is a real signed ratio-shell matrix `B`. Near ratio `1`, continuity of the centered taper transform and `r_v(0)=1` make the couplings uniformly positive. Partition the top-half primes into cells of additive width `asymp y/H`; strict subcriticality gives many prime pairs inside those unresolved cells.

Assign one common sign to each cell and choose those cell signs independently. In expectation every cross-cell coupling cancels while every positive within-cell coupling survives. The probabilistic method therefore produces a deterministic binary assignment with

`I_abs(B) >> y/(H log y)`.

Against the Haar RMS scale `sqrt(R_v)asymp H^-1/2`, this gives

`I_abs(B)/sqrt(R_v) >> y/(sqrt(H) log y) -> infinity`

throughout `H log y/y ->0`.

The useful structural point is that the divergence does not require delicate global phase optimization. **Local coherent prime blocks below the Fourier resolution already carry enough one-signed interaction mass.** The constant-factor Grothendieck comparison then transfers the same bounded-versus-divergent conclusion to the exact continuous-phase torus optimum and the real SDP.

This changes the frontier from “can static worst starts exceed RMS?” to “what happens at the transition, what is the sharp organized energy, and can the physical one-parameter orbit access such configurations?” Those questions need new information; making the static relaxation stronger cannot undo the binary lower bound.

**Boundary.** The taper and `alpha<1/2` are fixed, midpoint symmetry supplies the real gauge, and the theorem is strictly subcritical. The argument proves existence, not a canonical maximizing sign pattern or a short access time.
