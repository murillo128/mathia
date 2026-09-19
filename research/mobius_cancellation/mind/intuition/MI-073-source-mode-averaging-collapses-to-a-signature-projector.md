# MI-073 — Averaging over source modes can collapse exactly to a signature projector

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

Suppose the surviving source modes form a vector space `W<=F_2^R` with common radical modulus `P`. The source characters are indexed by `W`, while the residue class of an integer coprime to `P` maps through a signature homomorphism

`Phi:(Z/PZ)^* -> W^`.

MC-397 shows that `Phi` is surjective. If `K=ker Phi` and `H=|W|`, uniform averaging of the squared source-mode observable does not create a new oscillatory variable: it collapses exactly to a nonnegative residue projector,

`E_(a in W) |A_a(n)|^2 = H 1_((n,P)=1) 1_(n mod P in K)`.

This changes how source-mode multiplicity should be priced. A large mode family is useful for rank/codimension and fourth-moment geometry, but **averaging over the mode label itself is not automatically an arithmetic averaging direction**. Fourier orthogonality can consume that index completely and leave only a signature subgroup condition.

The surviving analytic gain must therefore come from a variable whose variation changes the arithmetic diagonal geometry after source Fourier collapse: for example a Selberg divisor/lcm variable, a genuinely varying shell/source parameter, or another source-native quantity not already dualized into the projector.

The reusable test is to Fourier-expand the source family before crediting an additional averaging dimension. If orthogonality converts that dimension into an exact indicator of a kernel/coset condition, then it has reorganized the source rather than supplied new cancellation.

**Boundary.** MC-397 does not remove the value of source-mode families for codimension, exceptional-set or moment arguments, and it does not prove that every possible joint average collapses. It rules out treating the isolated uniform source-mode index as an independent van-der-Corput/cancellation variable after the stated signature reduction.