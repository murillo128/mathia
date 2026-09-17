# MI-052 — Finite positivity must be gauge-invariant to track zero geometry

**Evidence level:** literature+derived synthesis from [AF-406](../../findings/AF-406-finite-polya-frequency-positivity-is-not-zero-set-faithful-under-exponential-gauge.md), with the local finite-order translation-kernel frontier supplied independently by [AF-403](../../findings/AF-403-complete-confluent-flags-globalize-strict-translation-total-positivity.md)--[AF-405](../../findings/AF-405-full-euler-log-is-strictly-sign-regular-through-order-four.md). Katkova's finite Pólya-frequency results and the all-order Pólya-frequency/Laguerre--Pólya characterization are prior art; the fidelity statement is their quotient interpretation.

For

`xi_1(z)=xi(sqrt(z)+1/2)`,

multiplication by a zero-free exponential leaves the complete zero divisor unchanged:

`Z(e^{nz}xi_1)=Z(xi_1)`.

Yet Katkova proves that for every fixed finite order `m` there is `n_0(m)` such that

`e^{nz}xi_1 in PF_m` for every `n>=n_0(m)`.

Thus finite **coefficient-sequence** `PF_m` membership is not a function of the zero divisor. Along one exact zero-preserving gauge orbit the RH-relevant zero geometry is constant while this finite positivity verdict can be driven into the positive class. A coefficient `PF_m` certificate can therefore be mathematically real and still fail the target-fidelity test.

The quantifier boundary is decisive. The statement

`for every m there exists n_0(m) such that e^{nz}xi_1 in PF_m for n>=n_0(m)`

does not produce one finite exponential tilt that lies in `PF_m` for every `m`. All-order Pólya-frequency positivity remains equivalent to the Laguerre--Pólya zero condition in the classical setting. The obstruction is specifically to interpreting any **fixed finite coefficient level** as an intrinsic approximation to zero geometry without first controlling the gauge.

AF-406 also shows that the gauge audit is representation-specific. If a positive translation profile is changed by an affine exponential tilt

`f(t) -> exp(at+b) f(t)`,

every translation determinant acquires only a positive row/column factor. Its confluent Hankel determinants satisfy `H_r -> exp(r(at+b))H_r`, while the normalized ratios `R_r=H_r/f^r` and the logarithmic curvature `q=-(log f)''` are unchanged. Consequently the Toda gate `(log R_4)''<4q` is invariant under this profile gauge.

This distinction matters. Multiplying the entire generating function by `e^{nz}` can manufacture finite coefficient `PF_m` membership, but that does **not** imply that the same gauge can manufacture finite translation-kernel total positivity. The coefficient sequence and the translation kernel are different positivity representations, and a gauge obstruction may be transferred between them only after the action of the gauge has been computed in the representation actually used by the proof.

The confluent Toda program therefore remains a legitimate structural question on its own terms. AF-403--AF-405 place the first possible failure of the Euler-log translation kernel at order at least five, and AF-406's coefficient-gauge counterexample does not invalidate the order-five test. A positive fifth Toda gate still would not by itself prove RH, but the reason is no longer this particular affine exponential gauge: the translation-kernel certificate already survives that gauge and must be judged against the remaining zero-selection and destination-faithfulness gates.

The reusable audit is: **before using finite positivity as evidence for a zero-set target, compute the actual gauge action on the exact positivity object being certified**. If `F` and `gF` have the same divisor for an admissible nowhere-zero factor `g` but that certificate changes, it belongs to the representation rather than intrinsically to the zero geometry. If the certificate is invariant, this gauge objection is closed for that representation, but target sufficiency still has to be proved separately.

**Boundary.** AF-406 does not settle `H_5`, determine the first bad total-positivity order, or show that every finite positivity notion is gauge-manufacturable. It proves a coefficient `PF_m` obstruction and, separately, affine-exponential invariance of the translation-kernel Toda hierarchy. More general zero-preserving changes of representation may require a separate audit. Gauge invariance is necessary for intrinsic zero-set evidence, not a zero-selection theorem by itself.
