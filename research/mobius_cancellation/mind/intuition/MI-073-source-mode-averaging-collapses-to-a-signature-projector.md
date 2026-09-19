# MI-073 — Formal source and Selberg averaging dimensions can collapse under exact representation changes

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md) and [MC-398](../../findings/MC-398-selberg-divisor-pair-lcm-fiber-collapse.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

Suppose the surviving source modes form a vector space `W<=F_2^R` with common radical modulus `P`. The source characters are indexed by `W`, while the residue class of an integer coprime to `P` maps through a signature homomorphism

`Phi:(Z/PZ)^* -> W^`.

MC-397 shows that `Phi` is surjective. If `K=ker Phi` and `H=|W|`, uniform averaging of the squared source-mode observable does not create a new oscillatory variable: it collapses exactly to a nonnegative residue projector,

`E_(a in W) |A_a(n)|^2 = H 1_((n,P)=1) 1_(n mod P in K)`.

Thus source-mode multiplicity is useful for rank/codimension and fourth-moment geometry, but the isolated mode label is not automatically an arithmetic averaging direction. Fourier orthogonality can consume that index completely and leave only a signature subgroup condition.

MC-398 supplies the same audit one layer later for the standard squared Selberg majorant. If

`f(n)=(sum_(d|n) g(d))^2`,

then simultaneous divisibility depends on the pair only through `ell=[d_1,d_2]`, and for every arithmetic inner quantity `T(ell)` one has the exact regrouping

`sum_(d_1,d_2) g(d_1)g(d_2) T([d_1,d_2]) = sum_ell C_g(ell) T(ell)`,

with `C_g(ell)=sum_([d_1,d_2]=ell)g(d_1)g(d_2)`. The pair labels therefore supply coefficient multiplicity, not two independent arithmetic samples, once the quadratic majorant has been formed.

The reusable test is **representation invariance of the claimed averaging gain**. Before crediting a formal index as a new cancellation dimension, perform every exact regrouping or Fourier dualization that leaves the arithmetic quantity unchanged. If the proposed diagonal thinning disappears after replacing source modes by the signature projector or divisor pairs by their lcm-fibre coefficient, the gain belongs to the expansion, not to the arithmetic problem.

The surviving candidate in the present endpoint frame is narrower but not empty. The single lcm/shell variable `ell` changes interval length, coprimality and source signature, so it is genuine arithmetic data. A different pre-quadratic representation may also survive if its phase, congruence or interval genuinely distinguishes divisor/source variables separately and does not factor through lcm. Either route must still beat the sequential `2^(-Omega(A))` conductor-depth tariff and the fixed-global-modulus costs already isolated elsewhere in the line.

**Boundary.** MC-397 does not remove source families as rank/codimension resources, and MC-398 does not rule out the lcm variable or a genuinely non-lcm-factorable pre-quadratic construction. Neither finding supplies a better character-sum estimate, Möbius cancellation or an RH consequence. They rule out only formal dimensions that exact algebra has already consumed.