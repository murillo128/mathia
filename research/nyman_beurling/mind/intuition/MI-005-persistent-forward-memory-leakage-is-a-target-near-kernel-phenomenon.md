# MI-005 — Stable tails are prediction/feedthrough gaps in stationary branch filters, not consequences of local flags or global conditioning

**Evidence level:** supported by NB-063--NB-073; the exact prediction/feedthrough criterion is proved only for stationary scalar branch filters, and no stable-tail triviality theorem for the actual nonstationary Nyman source is proved.

NB-066--NB-067 show that a hypothetical persistent Nyman target is a global continuation problem visible through finite normalized Schur complements. NB-068--NB-071 then rule out local memory, finite causal flags, exact branching, far-mass necessity, and ordinary global Gram conditioning as sufficient invariants: an exact-branching matched control can remain uniformly Riesz-conditioned while carrying a nonzero stable tail.

NB-072 identifies the analytic mechanism. If `D_j=psi(V_m)e_j` and `psi=theta g` is the inner--outer factorization, then the stable tail is `K_theta tensor ker(V_m*)`; it vanishes exactly when `psi` is outer. The complete global Gram depends only on the outer factor because multiplication by `theta` is isometric, so the inner defect is erased from pure energy geometry.

NB-073 identifies exactly what restores the erased information. On one Wold ray define the future-prediction energy

`Pi(psi)^2 = inf_{x in future span} ||psi(V_m)(w+x)||^2`.

It is the monotone limit of finite Gram Schur complements and equals `|g(0)|^2`. The actual first causal cell supplies the feedthrough energy `c(psi)^2=|psi(0)|^2`, hence

`c(psi)^2/Pi(psi)^2 = |theta(0)|^2`.

Therefore the stable tail is zero exactly when the Gram-predicted one-step error equals the actual causal feedthrough. A strict gap is precisely the inner obstruction. The logarithmic gap `log(Pi^2/c^2)=-2log|theta(0)|` also sees singular inner mass, not only Blaschke zeros.

This criterion is distinct from conditioning. For `psi=1-rho z`, the inner defect appears only for `rho>1`; at `rho=1` the source is outer but noninvertible, the Gram lower bound collapses, yet the prediction/feedthrough gap remains zero. Thus **conditioning, future prediction, causal feedthrough, and continuation defect are separate resources**.

The reusable target for the arithmetic source is now a nonstationary prediction identity rather than an abstract factorization slogan. The genuine Nyman system already has causal newest-cell vectors and finite future Schur complements. The missing theorem is to construct a canonical prediction scale `Pi_R` from the actual future Gram geometry and show that `Pi_R^2/||C_R||^2 -> 1` (or a suitable uniform analogue). In the stationary control class this is exactly equivalent to excluding the stable tail.

**Boundary.** The actual Nyman innovation system is not shown to equal one stationary `psi(V_m)`, so the scalar Szego/Wold formula does not transfer automatically. Burnol's outer half-plane multiplier lives in a different analytic variable. NB-073 supplies the correct matched-control discriminator and a concrete nonstationary target; it does not prove the required arithmetic prediction theorem.