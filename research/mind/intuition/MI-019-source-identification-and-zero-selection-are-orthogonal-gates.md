# MI-019 — Source identification and zero selection are orthogonal gates

**Evidence level:** exact cross-line synthesis supported by [AF-370](../../arithmetic_fidelity/findings/AF-370-hamburger-source-class-functional-equation-rigidity.md), the Prime-Circle scalar-sector results [PC-314](../../prime_circle/findings/PC-314-fourier-symmetrized-canonical-packet-has-off-critical-zeros.md)--[PC-315](../../prime_circle/findings/PC-315-oriented-fourier-orbit-eigensectors-have-off-critical-zeros.md), and the genuinely coupled extension [PC-319](../../prime_circle/findings/PC-319-small-mordell-tornheim-coupling-preserves-off-critical-zeros.md)--[PC-320](../../prime_circle/findings/PC-320-canonical-mordell-tornheim-off-critical-zeros-form-local-hypersurface.md). No transfer theorem between the source classes is claimed.

AF-370 gives a positive recovery theorem. In Hamburger's class of ordinary Dirichlet series with the required finite-order continuation, the exact completed Riemann functional equation forces `f=c zeta`; coefficient normalization removes the scalar gauge. Here the symmetry is genuinely faithful because the admissible source class is already rigid enough.

Prime Circle gives the complementary zero-geometry theorem at progressively richer representations. PC-314--PC-315 show that complete finite-Fourier scalar symmetry, including orientation, is compatible with infinitely many zeros in `Re s>1`. PC-319 then moves before scalar cyclic compression: the exact canonical `(5,7)` Mordell--Tornheim carrier itself inherits off-critical zeros for every sufficiently small positive coupling.

PC-320 removes the remaining temptation to blame a frozen slice. Joint holomorphy and Weierstrass preparation show that the canonical off-critical zero extends to a complex-analytic hypersurface finite over an open bidisk of the other Mellin parameters, still contained in `Re s>1`. Nonvanishing holomorphic completion factors preserve this divisor and local biholomorphic coordinate changes preserve its dimension. Thus even **faithful source coefficients + genuine multivariable coupling + full local divisor geometry + ordinary completion** do not supply zero selection.

The two obligations are therefore distinct:

1. **Identification:** does the retained structure determine which analytic source/function or source-dependent object is present inside the declared category?
2. **Zero selection:** what independent theorem forces the relevant divisor or spectrum into the desired region?

A functional equation, exact coefficient vector, invertible source representation or nonseparable multivariable carrier can settle part of the first question while answering none of the second. Even exact recovery of `zeta` would not prove RH; it would only ensure that the remaining divisor problem concerns the correct function.

The practical audit is to demand separate certificates. First prove the source-class recovery statement and its normalization/gauge boundary. Then identify a genuinely zero-selecting mechanism—positivity, unitarity, sign, self-adjoint spectrum, a source-forced distinguished submanifold/divisor relation, or another theorem whose conclusion actually concerns the relevant zero set. Completion or coordinate changes do not count when they leave the bad divisor invariant.

**Boundary.** AF-370 concerns Hamburger's ordinary-Dirichlet finite-order class; PC-314--PC-320 concern canonical periodic/Mordell--Tornheim objects in Prime Circle. The synthesis does not say that every multivariable family has off-critical zeros or that source identification is unimportant. It says that faithful identification, transform symmetry, nonseparability and RH-like zero confinement remain separate mathematical obligations until a theorem links them.
