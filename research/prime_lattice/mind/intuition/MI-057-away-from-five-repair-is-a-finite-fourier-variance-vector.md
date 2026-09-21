# MI-057 — Away-from-five repair is one signed character-variance supertrace

**Evidence level:** exact source/representation synthesis from [PL-414](../../findings/PL-414-away-from-5-residue-variance-projection.md) and [PL-415](../../findings/PL-415-away-from-5-dirichlet-character-variance-supertrace.md), refining the actual-prime transfer boundary left by MI-056.

The source-realized `p=5` de-aliasing has two exact finite representations. PL-414 writes its lag multiplier as the additive Fourier projector

`g_5(h)=76/75-(4/75) sum_(j=1)^4 e(jh/5)`,

which yields five rational-frequency quadratic variance sectors. PL-415 diagonalizes the same local factor on the unit group modulo `5` in the multiplicative character basis. Up to the explicit power-of-5 exceptional terms, the repaired source-subtracted variance is the single signed superposition

`Delta T_X^(5)(L) = Delta T_(X,chi_0)(L) - (1/15)Delta T_(X,chi_2)(L) - (2/15)Delta T_(X,chi_4)(L) + E_5(X,L)`,

where `chi_0` is principal, `chi_2` is quadratic, and `chi_4` represents the conjugate quartic pair. The exceptional term is polynomially negligible on the short-interval scales used by the cubic kernel.

This changes the intrinsic quantitative target. Separate power-saving bounds for all five additive sectors, or even for the three real character sectors, are sufficient but not necessary. What the source bridge actually needs is one bound on their fixed signed combination. Cancellation between the principal, quadratic and quartic channels is therefore a legitimate resource that componentwise triangle inequalities would erase.

If the combined remainder obeys

`|Delta T_(X,chi_0)(L) - (1/15)Delta T_(X,chi_2)(L) - (2/15)Delta T_(X,chi_4)(L)| << X L (L/X)^mu (log X)^B`

uniformly on the effective kernel support, the PL-407 transfer is unchanged: for `H=X^theta`, it is sufficient that

`mu > 3 theta / (4(1-theta))`.

Thus the representation improves the target's structure without improving the required exponent by itself.

The character basis also exposes a guardrail. The nonprincipal sectors are genuine primitive Dirichlet-`L` short-interval variance channels. Standard zero-pair routes to strong individual estimates are commonly formulated under GRH for those auxiliary `L(s,chi)`, which would import information stronger than RH for zeta alone. The safe route is therefore to analyze the fixed signed supertrace directly, or to derive an explicit-formula cancellation specific to that combination, rather than assume independent critical-line control for each sector.

The reusable lesson is that finite coordinate count is not the intrinsic complexity of a linear source repair. After exact diagonalization, the destination may depend on a lower-dimensional signed combination, and estimating components independently can destroy the only cancellation the source actually preserves.

**Boundary.** PL-414--PL-415 are exact representation and source-bridge identities, not the missing power-saving theorem. The character transform alone does not improve the cubic source-replacement error, and no cancellation of Dirichlet-`L` zeros is established on the spectral side. The principal character also includes the deleted `p=5` Euler factor, and the power-of-5 terms remain an explicit controlled remainder rather than disappearing identically.
