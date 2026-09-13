# MI-008 — Source size, observation scale and destination geometry are separate conditioning resources

**Evidence level:** supported by Arithmetic Fidelity through [AF-325](../../arithmetic_fidelity/findings/AF-325-bounded-support-height-uniformizes-prime-antipodal-conditioning.md) and Prime Flute through [PF-331](../../prime_flute/findings/PF-331-completed-low-polar-factor-has-uniform-gap-and-cannot-amplify-locality-defects.md). No theorem transfers the numerical moduli between the two lines.

Arithmetic Fidelity now makes the quantifier hierarchy quantitative. Exact eight-prime recovery, fixed-support conditioning, bounded-height support variation and unrestricted support-union topology are different statements. AF-323 shows unrestricted supports at fixed nonzero time fill the finite phase torus. AF-324 prices bounded support variation: prime tuples with `p<=H` form a net whose mesh is at most `O(H^(-19/40))`. AF-325 prices the opposite exclusion direction uniformly over that finite-height family:

`dist(Z_P(t),A_8) >= exp[-C(log H)^2 log(e+|t|log H)]`.

Thus source height `H` and observation time `t` form a genuine two-resource conditioning window. Retaining a finite support is not a binary stability resource; the downstream theorem must consume a modulus compatible with how both resources grow.

Prime Flute supplies the complementary destination geometry. PF-329 identifies the completed total-energy packet variable. PF-330 proves that final low normalization does not damp packet mass: it unitarily rotates a tight frame and preserves the exact Hilbert--Schmidt packet average. PF-331 then shows the polar unitary has no independent instability because its generating factor `F=A_0^(1/2)Q_L^(-1/2)` satisfies `F^*F>=I`; translation/localizer commutators of the polar factor are bounded by those of `F`.

So an upstream witness can remain fully present in the relevant Hilbert norm while becoming useless only through **destination-sensitive geometry**, here spatial locality of a concrete square-root operator. Conversely, a source restriction can provide exact recovery while its conditioning deteriorates with source size and observation scale.

The reusable diagnostic is therefore not simply “does the information survive?” For a candidate witness, specify the source family and size parameter, the observation/limit scale, the failure-set closure, the quantitative modulus under that quantifier order, and the exact norm/locality structure consumed by the destination. A theorem may conserve total mass and still lose localization; it may retain exact source identity and still lose conditioning as the admissible family grows.

**Boundary.** AF-324--AF-325 do not decide exact middle-singular incidence or give a sharp `H` asymptotic. PF-330--PF-331 do not prove square-root locality. This is a resource-accounting synthesis, not a common stability theorem.