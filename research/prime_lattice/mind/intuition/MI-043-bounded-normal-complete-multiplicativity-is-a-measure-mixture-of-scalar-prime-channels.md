# MI-043 — Bounded normal complete multiplicativity is a measure mixture of scalar prime channels

**Evidence level:** exact synthesis from [PL-377](../../findings/PL-377-bounded-normal-infinite-representations-scalarize-to-measures-on-semicharacters.md), extending the finite-dimensional classification PL-374--PL-376.

Let `rho:N->B(H)` be a bounded normal completely multiplicative representation. The commuting normal prime operators generate an abelian C*-algebra, so Gelfand theory identifies them with scalar coordinate functions on a compact spectrum `X`. Pointwise, every integer acts through a scalar semicharacter

`chi_x(n)=prod_p lambda_p(x)^(v_p(n))`.

Consequently every bounded linear observable is a measure mixture of scalar channels,

`L(rho(n)) = integral_X chi_x(n) dmu_L(x)`.

In the unitary case this is a measure on a prime torus; in the contractive case the same scalarization holds in the normal-convergence region of the associated Euler channels.

This closes a natural “infinite dimension will create operator-valued coupling” escape. Infinite Hilbert dimension and normality can enlarge the **measure of scalar characters**, but they do not create irreducible noncommutative cross-prime source geometry under exact complete multiplicativity. Analytic continuation, zero selection or positivity does not follow merely from writing the scalar family as an operator representation.

The next category change must therefore be explicit: nonnormality, unboundedness/domain data, nonlinear observables, a controlled failure of exact complete multiplicativity, or a global support/boundary condition on the representing measure that contributes genuinely new information.

**Boundary.** PL-377 is a bounded-normal classification. It does not classify nonnormal or unbounded infinite-dimensional representations, nonlinear operator observables, or global constraints on the Gelfand measure. Formal Euler products remain valid only in their proved normal-convergence region.