# MI-016 — Coherent unresolved prime blocks determine the strictly subcritical static energy scale

**Evidence level:** exact consequence of [VIS-192](../../findings/VIS-192-long-start-variance-scale.md), VIS-218, VIS-223--VIS-224 and [VIS-225](../../findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md)--[VIS-226](../../findings/VIS-226-subcritical-symmetric-taper-worst-start-exact-scale.md) in the strictly subcritical midpoint-symmetric taper regime. No critical/supercritical, sharp-constant, optimizer-identification or access-time conclusion is claimed.

After midpoint gauge, the static prime-phase problem is a real signed ratio-shell matrix `B`. Near ratio one, continuity of the centered taper makes the couplings uniformly positive. Partitioning top-half primes into cells of width `asymp y/H` and assigning one sign per cell gives the VIS-225 lower bound

`I_abs(B) >> y/(H log y)`.

VIS-226 shows this is already the correct order. The absolute tapered off-diagonal envelope from VIS-190 gives the matching upper bound

`I_abs(B) << y/(H log y)`

throughout `H log y/y ->0`. The constant-factor symmetric Grothendieck comparison then yields the same two-sided scale for the exact continuous-phase torus optimum and the real correlation SDP.

Against the Haar RMS scale `sqrt(R_v) asy H^-1/2`, all three normalized objectives therefore satisfy

`I_abs/sqrt(R_v) asy M_abs/sqrt(R_v) asy U_abs^R/sqrt(R_v) asy y/(sqrt(H) log y)`.

The useful structural point is stronger than super-RMS divergence: **local unresolved coherent prime blocks already set the complete coarse static energy scale**. Global phase optimization and higher-rank SDP freedom can change only constants in this regime.

The frontier has moved to information that the static scale does not contain: the transition at `H asy y/log y`, sharp constants/optimizer geometry, arithmetic matched controls within the same order of magnitude, and the time required for the physical one-parameter prime-log orbit to access a near-optimal torus configuration.

**Boundary.** The taper and `alpha<1/2` are fixed, midpoint symmetry supplies the real gauge, and the theorem is strictly subcritical. The order estimate does not identify a maximizing sign pattern or establish any finite dynamical access time.
