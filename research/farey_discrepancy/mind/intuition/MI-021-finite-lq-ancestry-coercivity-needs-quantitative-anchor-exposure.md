# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure; bounded distortion requires endpoint mass or typical-depth reach

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), with the endpoint-weight obstruction quantified by [FD-148](../../findings/FD-148-finite-seed-anchored-expansion-forces-singular-endpoint-marginals.md) and the bounded-distortion nonlocality threshold by [FD-149](../../findings/FD-149-bounded-distortion-ancestry-transfer-must-reach-typical-prime-factor-depth.md).

Let `G=(V,E)` carry vertex and edge probability measures `nu,eta`, let `D` be the anchored seed, and let `b:V->{-1,+1}` equal `+1` on `D`. If `A_b={b=-1}`, then for every finite `q`,

`||b-1||_(L^q(V,nu)) = 2 nu(A_b)^(1/q)`,

`||nabla b||_(L^q(E,eta)) = 2 eta(partial A_b)^(1/q)`.

Every admissible `A subset V\D` occurs as such a binary orientation, so the optimal binary anchored Poincaré constant is exactly

`C^(bin)_(q,D) = h_D(nu,eta)^(-1/q)`,

`h_D(nu,eta)=inf_A eta(partial A)/nu(A)`.

Connectivity is only the zero-boundary endpoint. Finite-`L^q` stability requires a **uniform lower bound on observed boundary mass for every macroscopic flipped region** in the actual source-native weights.

FD-148 shows that one-step nonuniform weighting pays an explicit endpoint tax. On the squarefree ancestry graph, the complement of a fixed finite divisor-closed seed `D` has boundary only through the seed and its immediate descendants. If the edge parent marginal is dominated by `K_T` times uniform, then

`h_(D,T) <= O_D(K_T/T)`;

if the child marginal is dominated by `L_T` times uniform, then

`h_(D,T) <= O_D(L_T/log T)`.

Thus one-step positive expansion requires singular endpoint concentration: average parent amplification of order `T`, logarithmic amplification on the child/prime rays, or an equivalent source-native concentration mechanism.

FD-149 shows that bounded distortion can avoid this tax only by becoming genuinely nonlocal at a quantitatively forced depth. If edges may jump at most `L` prime adjunctions and the child marginal is `K_T`-dominated by the uniform coefficient measure on reachable descendants, then the same complement cut gives

`h_(D,T)^(<=L) <= K_T nu_T(R_(D,L)(T))/(1-nu_T(D))`.

For fixed `L`, Landau's fixed-rank almost-prime law makes the reachable fraction

`nu_T(R_(D,L)(T)) <<_(D,L) (log log T)^(r_D+L-1)/log T`,

so `K_T=O(1)` still forces `h->0`. If instead `K_T<=K` and `h_(D,T)^(<=L_T)>=c>0`, squarefree Erdős--Kac forces

`L_T >= log log T - O_(c,K,D)(sqrt(log log T))`.

Hence the reusable dichotomy is concrete: **a fixed-seed finite-`L^q` ancestry mechanism must pay either singular endpoint mass or genealogical reach essentially up to the typical squarefree prime-factor depth**. A few extra local generations do not change the obstruction.

The source-validity test should therefore ask where that resource comes from. If a proposed weighting concentrates mass, explain the arithmetic mechanism producing the concentration. If it keeps bounded marginals, explain why the observation naturally couples the anchor to descendants roughly `log log T` prime adjunctions away and why that depth is not just hidden source reconstruction.

**Boundary.** These results concern a fixed finite anchor, binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They do not exclude a growing anchor, `L^infinity`, independently justified singular weights, depth on the typical `log log T` scale, or genuinely nonlocal Farey/Fourier destination functionals outside this edge model.