# MI-021 — Finite-`L^q` binary ancestry coercivity is exactly quantitative anchored cut exposure

**Evidence level:** exact/proved classification from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md), refining the disconnected-component gauge of FD-145 and the rank-wall dilution example of FD-146.

Let `G=(V,E)` carry vertex and edge probability measures `nu,eta`, let `D` be the anchored seed, and let `b:V->{-1,+1}` equal `+1` on `D`. If `A_b={b=-1}`, then for every finite `q`,

`||b-1||_(L^q(V,nu)) = 2 nu(A_b)^(1/q)`,

`||nabla b||_(L^q(E,eta)) = 2 eta(partial A_b)^(1/q)`.

Every admissible `A subset V\D` occurs as such a binary orientation, so the optimal binary anchored Poincare constant is exactly

`C^(bin)_(q,D) = h_D(nu,eta)^(-1/q)`,

`h_D(nu,eta)=inf_A eta(partial A)/nu(A)`.

This separates two resources sharply. Connectivity says only that no admissible cut has zero observed boundary; finite-`L^q` stability requires a **uniform lower bound on the boundary mass of every macroscopic flipped region** in the actual normalization. For `q=infinity`, the mass disappears and connectivity is again the relevant binary condition.

On the full squarefree ancestry graph with uniform measures, a fixed finite seed cannot provide that exposure. Let `D` be the finite squarefree divisor closure of the prescribed seed and flip the orientation on `V_T\D`. The full graph has `|E_T| ~ T log log T/zeta(2)`, while the boundary of fixed `D` has size `~ kappa_D T/log T`. Hence

`eta_T(partial D) = Theta_D(1/(log T log log T))`,

while the flipped vertex mass tends to one. The ancestry defect is therefore `Theta_D((log T log log T)^(-1/q))` although coefficient error tends to `2`, and

`C^(bin)_(q,D)(T) >= c_D (log T log log T)^(1/q)`.

The reusable test for a proposed ancestry observable is thus not “are all coefficients connected to the anchor?” but “what is its anchored cut profile under the exact source-native weights?” Uniformly adding local edges or fixing finitely many coefficients cannot repair a vanishing cut ratio.

**Boundary.** The statement is exact for binary orientations and finite `L^q`. It does not exclude nonuniform source-native weights with a uniform cut lower bound, `L^infinity`, growing/direct anchoring, or genuinely nonlocal Farey/Fourier functionals that do not reduce to local coefficient recovery.