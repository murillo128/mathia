# MI-042 — Finite-prefix pole fidelity is a source-tail property, not a consequence of accurate local observation

**Evidence level:** exact-derived boundary statement from [AF-366](../../findings/AF-366-finite-prefix-observations-need-tail-class-for-dirichlet-pole-fidelity.md), complementing the global Riesz principal-part theorem AF-365.

Let an observation `T_N` depend only on the first `N` Dirichlet coefficients. Its observation fibre contains every tail perturbation vanishing on that prefix. In particular, for `rho=beta+i gamma`, `beta<1`,

`d_n = r n^(rho-1) 1_(n>N)`

is completely invisible to `T_N`, while

`sum d_n n^-s = r[zeta(s-rho+1) - sum_(n<=N)n^(rho-1-s)]`

has a simple pole at `s=rho` of residue `r`. Yet `sup_(n>N)|d_n| <= |r|N^(beta-1) -> 0`. Hence arbitrarily long exact finite observations, even with an unseen tail small in unweighted sup norm, do not determine the meromorphic principal parts of the completed Dirichlet object.

The complementary recovery currency is the **tail class**. If two coefficient sequences satisfy

`|a_n-b_n| <= M n^(theta-1)` for `n>N`,

then their tail Dirichlet difference converges locally uniformly on `Re s>theta`; assuming the transforms continue there, their principal parts in that open half-plane are identical. On `Re s>=theta+eta`, the tail magnitude is at most `(M/eta)N^-eta`. The boundary `Re s=theta` is sharp for this elementary class.

For finite Riesz data this distinction is literal: the profile on `1<=X<=N` factors through the same finite coefficient prefix, so smoothing cannot manufacture information about future coefficients. AF-365's zero-free Mellin multiplier protects poles only when the transformed error is controlled **globally/eventually**. AF-366 shows that replacing that hypothesis by a finite horizon silently changes the problem from transform fidelity to admissible completion.

The reusable rule is concrete: before inferring a pole/zero discriminator from finite data, specify the completion class and prove that differences inside one observation fibre are holomorphic in the target half-plane. A finite window plus small raw tail coefficients is not such a theorem; a weighted polynomial tail bound is one sufficient certificate.

**Boundary.** The pole-inserting controls are general Dirichlet coefficient sequences, not matched rational-prime or Euler-product sources. The result proves an observation-topology obstruction, not that every arithmetic source class admits those completions. Nor does the tail bound solve stable analytic continuation at its boundary. The remaining arithmetic task is precisely to justify a source restriction or nonlocal certificate strong enough to exclude the invisible pole-carrying tails.