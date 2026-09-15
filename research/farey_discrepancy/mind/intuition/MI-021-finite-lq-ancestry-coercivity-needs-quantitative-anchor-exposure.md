# MI-021 — Finite-`L^q` binary ancestry coercivity is exactly anchored cut exposure, and fixed-seed expansion requires singular endpoint weight

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), with the nonuniform-weight endpoint quantified by [FD-148](../../findings/FD-148-finite-seed-anchored-expansion-forces-singular-endpoint-marginals.md).

Let `G=(V,E)` carry vertex and edge probability measures `nu,eta`, let `D` be the anchored seed, and let `b:V->{-1,+1}` equal `+1` on `D`. If `A_b={b=-1}`, then for every finite `q`,

`||b-1||_(L^q(V,nu)) = 2 nu(A_b)^(1/q)`,

`||nabla b||_(L^q(E,eta)) = 2 eta(partial A_b)^(1/q)`.

Every admissible `A subset V\D` occurs as such a binary orientation, so the optimal binary anchored Poincare constant is exactly

`C^(bin)_(q,D) = h_D(nu,eta)^(-1/q)`,

`h_D(nu,eta)=inf_A eta(partial A)/nu(A)`.

Connectivity is only the zero-boundary endpoint. Finite-`L^q` stability requires a **uniform lower bound on observed boundary mass for every macroscopic flipped region** in the actual source-native weights.

FD-148 shows that simply allowing arbitrary nonuniform weights does not make this gate free. On the squarefree ancestry graph, test the cut given by the complement of a fixed finite divisor-closed seed `D`. Its boundary has two endpoint descriptions: mass leaving the fixed seed and mass entering the one-step child set `C_D(T)`. If the edge parent marginal is dominated by `K_T` times the uniform vertex scale, then

`h_(D,T) <= O_D(K_T/T)`.

If the child marginal is dominated by `L_T` times the uniform scale, then

`h_(D,T) <= O_D(L_T/log T)`.

Consequently any weighting with `K_T=o(T)` or `L_T=o(log T)` still has vanishing anchored expansion. A positive fixed-seed limit forces singular endpoint concentration: order-one edge mass must remain on a fixed seed boundary, which corresponds to average parent amplification of order `T`, or to logarithmic amplification on the relevant child/prime rays. For `D={1}`, the prime fan itself must receive `Omega(log T)` overweight relative to uniform normalization.

The reusable test is therefore sharper than “choose better weights.” A source-native weighting must explain **where the compensating endpoint mass comes from and why that singular concentration is intrinsic rather than inserted to force coercivity**. Uniformly comparable marginals cannot solve the fixed-seed finite-`L^q` problem.

**Boundary.** The result is exact for the fixed finite seed and local ancestry cut geometry. It does not exclude a growing anchor, `L^infinity`, deliberately singular but independently justified arithmetic weights, or genuinely nonlocal Farey/Fourier functionals. It says only that nonuniform local weighting pays an explicit endpoint-concentration tax before it can yield uniform anchored expansion.