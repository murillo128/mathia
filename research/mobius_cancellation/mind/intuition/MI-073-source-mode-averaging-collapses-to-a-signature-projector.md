# MI-073 — Formal averaging dimensions can collapse under exact regrouping and first-correlation separability

**Evidence level:** exact synthesis from [MC-397](../../findings/MC-397-source-mode-averaging-collapses-to-signature-projector.md), [MC-398](../../findings/MC-398-selberg-divisor-pair-lcm-fiber-collapse.md), and [MC-399](../../findings/MC-399-lcm-retention-separates-from-source-qvdc-phase.md), interpreted against the source-rank/codimension framework of MC-385--MC-396.

Suppose the surviving source modes form a vector space `W<=F_2^R` with common radical modulus `P`. The source characters are indexed by `W`, while the residue class of an integer coprime to `P` maps through a signature homomorphism

`Phi:(Z/PZ)^* -> W^`.

MC-397 shows that `Phi` is surjective. If `K=ker Phi` and `H=|W|`, uniform averaging of the squared source-mode observable does not create a new oscillatory variable: it collapses exactly to a nonnegative residue projector,

`E_(a in W) |A_a(n)|^2 = H 1_((n,P)=1) 1_(n mod P in K)`.

Thus source-mode multiplicity is useful for rank/codimension and fourth-moment geometry, but the isolated mode label is not automatically an arithmetic averaging direction. Fourier orthogonality can consume that index completely and leave only a signature subgroup condition.

MC-398 supplies the same audit one layer later for the standard squared Selberg majorant. If

`f(n)=(sum_(d|n) g(d))^2`,

then simultaneous divisibility depends on the pair only through `ell=[d_1,d_2]`, and every arithmetic inner quantity depending on the pair through that lcm admits the exact regrouping

`sum_(d_1,d_2) g(d_1)g(d_2) T([d_1,d_2]) = sum_ell C_g(ell) T(ell)`.

The pair labels therefore supply coefficient multiplicity, not two independent arithmetic samples, once the quadratic majorant has been formed.

MC-399 shows that surviving an exact regrouping is still not enough to make `ell` a retained q-vdC phase variable. After source Fourier expansion,

`S(N)=sum_I sum_ell C_g(ell)chi_I(ell)M_I(N/ell)`.

For `F_(I,ell)(m)=chi_I(ell m)`, complete multiplicativity gives

`F_(I,ell)(m+h) conjugate(F_(I,ell)(m)) = chi_I(m+h) conjugate(chi_I(m))`.

The `ell`-dependent source scalar disappears at the first additive correlation. Hence writing `chi_I(ell m)` rather than `chi_I(ell)chi_I(m)` cannot manufacture the Stadlmann-type diagonal gain: the putative coupling is representation-dependent.

The reusable test is therefore stronger than “does the index survive algebraic compression?” Before crediting a formal index as a new cancellation dimension, **perform every exact Fourier/regrouping reduction and then apply the first correlation or Cauchy step that is supposed to exploit it**. If the variable separates before that geometry forms, it is not a retained arithmetic phase even when it remains elsewhere in the formula.

For the present endpoint frame, `ell` still matters through the signed coefficient/signature distribution `C_g(ell)chi_I(ell)` and the moving endpoint `N/ell`. A useful theorem could exploit collective cancellation in that hyperbola transform or direct signature incidence. Alternatively, a pre-quadratic representation may survive if a divisor/source variable does not factor through lcm and remains nonseparable through the relevant correlation. Either route must still beat the sequential `2^(-Omega(A))` conductor-depth tariff and fixed-global-modulus costs already isolated elsewhere.

**Boundary.** MC-399 does not prove that the lcm variable is analytically useless, estimate the twisted hyperbola transform, or rule out a genuinely non-lcm-factorable pre-quadratic construction. It rules out only treating the standard lcm factor inside `chi_I(ell m)` as a Stadlmann-style mixed source phase. No improved character-sum estimate, Möbius cancellation or RH consequence follows.