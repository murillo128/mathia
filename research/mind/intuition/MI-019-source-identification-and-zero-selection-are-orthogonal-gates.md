# MI-019 — Source identification and zero selection are orthogonal gates

**Evidence level:** exact cross-line synthesis supported by [AF-370](../../arithmetic_fidelity/findings/AF-370-hamburger-source-class-functional-equation-rigidity.md), [PC-314](../../prime_circle/findings/PC-314-fourier-symmetrized-canonical-packet-has-off-critical-zeros.md), and the orientation-complete extension [PC-315](../../prime_circle/findings/PC-315-oriented-fourier-orbit-eigensectors-have-off-critical-zeros.md), with the underlying converse theorem and periodic-Dirichlet zero theorem already audited in those findings. No transfer theorem between the two source classes is claimed.

AF-370 gives a positive recovery theorem. In Hamburger's class of ordinary Dirichlet series with the required finite-order continuation, the exact completed Riemann functional equation forces `f=c zeta`; the coefficient normalization `a(1)=1` removes the scalar gauge. Here the symmetry is genuinely faithful **because the admissible source class is already rigid enough**.

Prime Circle gives the complementary zero-geometry theorem. After mixed-conductor source data have been compressed to one periodic coefficient, the finite Fourier transform supplies a universal order-four closure. PC-314 proves that, for the canonical `(5,7)` packet, the even `+1/-1` scalar eigensectors have exact Riemann-type functional equations yet fall outside the exceptional single-`L` class and therefore have linearly many zeros in suitable strips with `Re s>1`.

PC-315 shows that this is not an artifact of discarding orientation. Keeping the odd component of the unsymmetrized packet adds the forced `+i/-i` eigensectors, and exact coefficient tests place those sectors on the same generic Saias--Weingartner side. Thus **every scalar sector `+1,-1,+i,-i` in the complete finite-Fourier orbit of this canonical oriented packet has infinitely many zeros in `Re s>1`**. Recovering chirality inside the already periodicized orbit strengthens the symmetry package without supplying zero selection.

Together these results separate two logically different questions:

1. **Identification:** does the retained structure determine which analytic function/source is present inside the declared admissible category?
2. **Zero selection:** what theorem forces the divisor of that already-identified function into the desired region?

A functional equation can contribute decisively to the first question and still answer nothing about the second. Conversely, producing the complete family of scalar transform symmetries in a broad periodic category can be almost free and compatible with extremely bad zero geometry. Even exact recovery of `zeta` does not prove RH; it merely ensures that the remaining divisor problem is about the correct function.

The practical audit is therefore to demand two separate certificates whenever a route uses functional-equation or self-dual language. First prove the source-class recovery statement and its normalization/gauge boundary. Then identify an independent zero-selecting mechanism—positivity, unitarity, sign, spectral self-adjointness, localization, or another theorem whose conclusion actually concerns the divisor. Enlarging a universal transform orbit or restoring a parity/orientation component does not count as that second certificate unless a theorem connects the added structure to zero geometry.

**Boundary.** AF-370 concerns Hamburger's ordinary-Dirichlet finite-order class; PC-314--PC-315 concern periodic Dirichlet series arising from one canonical Prime-Circle packet. The synthesis does not say that every functional-equation family has off-critical zeros or that source identification is unimportant. It says only that **faithful identification, complete transform symmetry and RH-like zero confinement are distinct mathematical obligations** and must not be credited as one another.
