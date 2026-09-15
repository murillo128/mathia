# MI-042 — Finite-prefix pole fidelity is a source-tail property, not a consequence of accurate local observation

**Evidence level:** exact-derived boundary statement from [AF-366](../../findings/AF-366-finite-prefix-observations-need-tail-class-for-dirichlet-pole-fidelity.md), strengthened inside the positive generalized-prime category by [AF-367](../../findings/AF-367-finite-prime-prefix-plus-square-root-beurling-regularity-does-not-determine-zero-geometry.md), and complementary to the global Riesz principal-part theorem AF-365.

AF-366 isolates the unrestricted-completion obstruction. Let an observation `T_N` depend only on the first `N` Dirichlet coefficients. Its observation fibre contains every tail perturbation vanishing on that prefix. In particular, for `rho=beta+i gamma`, `beta<1`,

`d_n = r n^(rho-1) 1_(n>N)`

is completely invisible to `T_N`, while its Dirichlet transform has a simple pole at `s=rho`. Yet `sup_(n>N)|d_n| <= |r|N^(beta-1) -> 0`. Arbitrarily long exact finite observations therefore do not determine meromorphic principal parts over an unrestricted coefficient completion class.

AF-367 shows that this is not merely an artifact of allowing arbitrary signed coefficients. For every finite cutoff `X_0`, there are positive Beurling generalized-prime systems that agree exactly with the ordinary rational primes, and hence with the induced generalized integers, below `X_0`; both satisfy near-square-root integer counting of the form

`N_P(x)=x+O(x^(1/2) exp(c(log x)^(2/3)))`,

but one system has Beurling-RH zero geometry while another has zeros in a de la Vallée-Poussin-type off-critical region. Thus **finite exact prime data + positive Euler-product multiplicativity + this coarse near-square-root global counting class still does not determine zero geometry**.

The complementary recovery currency remains a source-tail/continuation class. If two coefficient sequences satisfy

`|a_n-b_n| <= M n^(theta-1)` for `n>N`,

then their tail Dirichlet difference converges locally uniformly on `Re s>theta`; assuming the transforms continue there, their principal parts in that open half-plane are identical. On `Re s>=theta+eta`, the tail magnitude is at most `(M/eta)N^-eta`. AF-365 gives the transform-side analogue: a zero-free Mellin multiplier protects principal parts only under global/eventual transformed control.

The reusable rule is therefore stricter than “preserve many primes and a good counting law.” Before inferring a pole/zero discriminator from finite data, specify an admissible source category and prove that every completion inside one observation fibre has the same target principal parts. A weighted polynomial tail bound is one sufficient analytic certificate; the Beurling controls show that positivity, multiplicativity and the displayed counting remainder are not.

**Boundary.** AF-367 is a generalized-prime construction, not an alternative factorization of the ordinary integers. It does not show that exact ordinary-integer support, the rational-prime Euler product, a zeta functional equation, or a stronger global cancellation/continuation law can be varied independently. Those are precisely candidate extra resources. The result is a source-class obstruction, not a proof that no stronger arithmetic completion theorem exists.