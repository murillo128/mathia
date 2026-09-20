# MI-057 — Paired sign cubes transfer Banach type ceilings into source-relative mixture fidelity

**Evidence level:** exact geometric synthesis from [AF-458](../../findings/AF-458-rademacher-type-controls-sparse-mixture-fidelity-through-paired-secants.md), interpreted against AF-456--AF-457. The conclusion is conditional on the completed physical source-law secant carrier containing the stated paired cube; no arithmetic source is asserted to contain one.

For a bounded barycentric marking `phi:A->Y` with `sup_a ||phi(a)||<=M`, Banach type already limits how well growing sparse mixtures can remain separated in TV. If `Y` has type `p in [1,2]`, the unrestricted `k`-sparse modulus satisfies

`kappa_k^TV(phi) <= T_p(Y) M k^(1/p-1)`.

The exponent is the correct ambient type scale: the one-hot marking into `l^p` realizes `M(2k)^(1/p-1)`. At `p=2` this recovers the square-root scarcity behind AF-457, while Hilbert geometry supplies the sharper constant `M/sqrt(2k)`.

AF-458 also turns the unrestricted obstruction into a source-relative certificate. It is not necessary that the physical source contain the whole `k`-sparse simplex. It is enough that its completed secant carrier contain a complete paired `k`-cube: `2k` source atoms split into `k` disjoint pairs, with every balanced sign orientation represented by completable source-law secants. Rademacher averaging on that cube produces the same type-`p` upper bound on the restricted source modulus.

The source-side condition is therefore the load-bearing part. If growing paired cubes exist, adding target dimension or optimizing bounded marks cannot remove the type tariff. If the arithmetic source forbids one of the required orientations, couples coefficients, or forces a lower-dimensional family, this particular proof no longer applies. But cube exclusion by itself is not positive conditioning; the surviving secants still need their own lower-gain theorem.

**Boundary.** This is an affine/barycentric TV statement for bounded marks. It does not cover nonlinear observations, other source metrics, unbounded encodings, or restricted source classes that do not contain the paired cube. Type `p=1` gives no decaying exponent, so the useful obstruction there must come from additional target or source structure.
