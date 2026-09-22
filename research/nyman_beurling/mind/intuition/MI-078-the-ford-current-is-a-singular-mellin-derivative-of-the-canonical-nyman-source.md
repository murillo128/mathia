# MI-078 — The Ford current is a singular Mellin derivative of the canonical Nyman source

**Evidence level:** exact source identity from [NB-276](../../findings/NB-276-the-ford-divisor-current-is-the-singular-mellin-derivative-of-the-canonical-mobius-nyman-core.md), with the canonical Abel-regularization tradeoff from [NB-277](../../findings/NB-277-abel-damping-that-preserves-ford-depth-cannot-soften-the-differentiated-mobius-source.md). This synthesis is independent of the proposed/pending NB-273--NB-275 claims.

For the canonical Nyman synthesis

`N[P](s)=zeta(s)/s (P(s)-P(1))`

and the Möbius source `P_*(s)=1/zeta(s)`, the source itself gives `N[P_*]=1/s`. Differentiating the source before synthesis produces

`P_*'(s)=-zeta'(s)/zeta(s)^2`, `P_*'(1)=1`,

and therefore the exact continued identity

`-s N[P_*'] = zeta'(s)/zeta(s) + zeta(s)`.

The right-hand side is the Ford divisor current: its Euler singularity cancels while the nontrivial-zero residues remain. The arithmetic object is therefore not missing from the canonical Nyman source. It appears after a **singular Mellin differentiation** of that source.

The singularity matters. On finite Dirichlet approximants, differentiation inserts the coefficient factor `log k`; multiplication by `s` is unbounded in the relevant Hardy geometry; and the zero poles arise only after meromorphic continuation. The exact continued identity is consequently not by itself an admissible `H^2` approximation theorem.

NB-277 shows that the most canonical horizontal Abel smoothing cannot remove this difficulty without moving the Ford scale. Replacing the source by `1/zeta(s+epsilon)` shifts the shell geometry by `X epsilon`. Ford-depth fidelity requires `X epsilon->0`; in precisely that regime `k^(-epsilon)=1+o(1)` on `log k~X`, so the logarithmic derivative tariff survives. Strong damping requires a displacement that is no longer Ford-depth faithful.

The durable inference is that the promising source-native route is no longer “find the Ford current inside Nyman--Beurling”; it is **realize an already exact source identity through a finite legal regularization that pays the derivative and topology costs**. Truncation, cancellation before norm passage, or another zero-preserving regularization remain logically distinct from the failed canonical Abel shift.

**Boundary.** NB-276--NB-277 do not prove `H^2` convergence, a lower bound for every legal regularizer, or failure of Möbius cancellation. They do not promote or depend on NB-273--NB-275. They identify the exact source-level current and show only that horizontal Abel damping cannot simultaneously preserve Ford depth and soften the differentiated source.
