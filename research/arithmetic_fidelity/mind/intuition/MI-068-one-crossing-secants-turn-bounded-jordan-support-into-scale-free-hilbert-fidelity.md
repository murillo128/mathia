# MI-068 — One-crossing secants turn bounded Jordan support into scale-free Hilbert fidelity

**Evidence level:** exact metric synthesis from [AF-478](../../findings/AF-478-single-crossing-gibbs-laws-retain-scale-free-hilbert-fidelity.md), refining the realizable-complexity warning in AF-476--AF-477.

A source family can be infinite and nonlinearly parameterized yet avoid the generic sparse-mixture cube obstruction if every pairwise secant has a uniformly simple sign geometry. AF-478 isolates a sufficient invariant: after orienting each signed difference `nu=mu-mu'`, suppose the positive Jordan part of `nu` is supported on at most `N` atoms. Then the coordinate Hilbert embedding

`H(mu)=sqrt(2) (mu(x))_(x in X)`

obeys the scale-free two-sided estimate

`(1/sqrt(2N)) ||mu-mu'||_1 <= ||H(mu)-H(mu')||_2 <= ||mu-mu'||_1`.

The point is not finite parameter dimension. The lower bound comes from where the positive mass of each **realizable secant** can live. A bounded Jordan-support side prevents the mass from spreading over an arbitrarily large independent Hamming cube even when the ambient simplex or tail envelope is much larger.

Ordered Gibbs families provide an exact example. For `mu_sigma(n) proportional a_n exp(-sigma E_n)` with strictly increasing energies and `sigma>=sigma_0`, the likelihood ratio of two temperatures is monotone in the energy index. Their difference therefore has at most one sign crossing. AF-478 shows that the positive Jordan side is confined to a fixed low-energy prefix of size `N_0` determined by the certified parameter range, so the same Hilbert condition bound holds uniformly over the whole family.

This changes the arithmetic-fidelity frontier. An upper compressibility profile and an ambient realizable-tail breadth are not enough to predict Hilbert distortion; the actual secant sign/ordering geometry of the source class can suppress the independent switches that drive the generic lower bound. The prime-derived problem should therefore measure realizable secant complexity directly, not infer it from ambient support size or parametric dimension.

**Boundary.** The one-crossing mechanism is not a rational-prime discriminator. The same ordered Gibbs argument applies to matched nonprime energy sequences with the same monotonicity. AF-478 proves a metric fidelity mechanism, not arithmetic identification, and it does not imply that a general prime-derived class has bounded Jordan support. That support bound must be established for the actual admissible secants before the scale-free estimate transfers.