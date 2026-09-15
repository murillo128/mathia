# MI-019 — Source identification and zero selection are orthogonal gates

**Evidence level:** exact cross-line synthesis supported by [AF-370](../../arithmetic_fidelity/findings/AF-370-hamburger-source-class-functional-equation-rigidity.md) and [PC-314](../../prime_circle/findings/PC-314-fourier-symmetrized-canonical-packet-has-off-critical-zeros.md), with the underlying converse theorem and periodic-Dirichlet zero theorem already audited in those findings. No transfer theorem between the two source classes is claimed.

AF-370 gives a positive recovery theorem. In Hamburger's class of ordinary Dirichlet series with the required finite-order continuation, the exact completed Riemann functional equation forces `f=c zeta`; the coefficient normalization `a(1)=1` removes the scalar gauge. Here the symmetry is genuinely faithful **because the admissible source class is already rigid enough**.

PC-314 gives the complementary zero-geometry theorem. After Prime Circle has been compressed to a periodic coefficient and universally finite-Fourier symmetrized, the canonical `(5,7)` `+` and `-` eigensectors satisfy exact scalar Riemann-type functional equations. Yet both fall outside the exceptional single-`L`-function class, so Saias--Weingartner forces linearly many zeros in suitable strips strictly inside `Re s>1`.

Together these results separate two logically different questions:

1. **Identification:** does the retained structure determine which analytic function/source is present inside the declared admissible category?
2. **Zero selection:** what theorem forces the divisor of that already-identified function into the desired region?

A functional equation can contribute decisively to the first question and still answer nothing about the second. Conversely, producing an exact critical-axis symmetry in a broad category can be almost free and compatible with extremely bad zero geometry. Even exact recovery of `zeta` does not prove RH; it merely ensures that the remaining divisor problem is about the correct function.

The practical audit is therefore to demand two separate certificates whenever a route uses functional-equation or self-dual language. First prove the source-class recovery statement and its normalization/gauge boundary. Then identify an independent zero-selecting mechanism—positivity, unitarity, sign, spectral self-adjointness, localization, or another theorem whose conclusion actually concerns the divisor. Do not credit the same symmetry twice.

**Boundary.** AF-370 concerns Hamburger's ordinary-Dirichlet finite-order class; PC-314 concerns periodic Dirichlet series arising from one canonical Prime-Circle packet. The synthesis does not say that every functional-equation family has off-critical zeros or that source identification is unimportant. It says only that **faithful identification and RH-like zero confinement are separate mathematical obligations** and must be proved separately.
