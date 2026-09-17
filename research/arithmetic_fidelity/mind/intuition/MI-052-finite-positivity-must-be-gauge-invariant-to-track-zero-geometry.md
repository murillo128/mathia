# MI-052 — Finite positivity must be gauge-invariant to track zero geometry

**Evidence level:** literature+derived synthesis from [AF-406](../../findings/AF-406-finite-polya-frequency-positivity-is-not-zero-set-faithful-under-exponential-gauge.md), with the local finite-order translation-kernel frontier supplied independently by [AF-403](../../findings/AF-403-complete-confluent-flags-globalize-strict-translation-total-positivity.md)--[AF-405](../../findings/AF-405-full-euler-log-is-strictly-sign-regular-through-order-four.md). Katkova's finite Pólya-frequency results and the all-order Pólya-frequency/Laguerre--Pólya characterization are prior art; the fidelity statement is their quotient interpretation.

For

`xi_1(z)=xi(sqrt(z)+1/2)`,

multiplication by a zero-free exponential leaves the complete zero divisor unchanged:

`Z(e^{nz}xi_1)=Z(xi_1)`.

Yet Katkova proves that for every fixed finite order `m` there is `n_0(m)` such that

`e^{nz}xi_1 in PF_m` for every `n>=n_0(m)`.

Thus finite `PF_m` membership is not a function of the zero divisor. Along one exact zero-preserving gauge orbit the RH-relevant zero geometry is constant while the finite positivity verdict can be driven into the positive class. A finite positivity certificate can therefore be mathematically real and still fail the target-fidelity test.

The quantifier boundary is decisive. The statement

`for every m there exists n_0(m) such that e^{nz}xi_1 in PF_m for n>=n_0(m)`

does not produce one finite exponential tilt that lies in `PF_m` for every `m`. All-order Pólya-frequency positivity remains equivalent to the Laguerre--Pólya zero condition in the classical setting. The obstruction is specifically to interpreting any **fixed finite level** as an intrinsic approximation to zero geometry without first controlling the gauge.

This also sharpens the meaning of the confluent Toda program. AF-403--AF-405 prove genuine finite-order structure of the full Euler-log translation kernel and place its first possible failure at order at least five. Continuing to the order-five gate `(log R_4)''<4q` remains a legitimate structural question. But success at another finite level would not by itself become RH evidence: one must additionally show that the retained positivity datum descends through the zero-free exponential freedom, or fix that freedom by an independently justified canonical normalization.

The reusable audit is simple: **before using finite positivity as evidence for a zero-set target, test whether the certificate is constant on zero-preserving gauge fibres**. If `F` and `gF` have the same divisor for an admissible nowhere-zero factor `g` but the finite certificate changes, the certificate belongs to the representation rather than intrinsically to the target zero geometry.

**Boundary.** AF-406 does not settle `H_5`, determine the first bad total-positivity order, or show that every finite positivity notion is gauge-manufacturable. Canonical gauge fixing may remove this particular obstruction, but it does not make a fixed finite positivity condition sufficient for RH. The finding supplies a necessary target-fidelity audit, not a new zero-selection theorem.