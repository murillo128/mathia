# MI-005 — The sharp logarithmic predecessor window is source-tagged above the linear mass floor

**Evidence level:** proved for the current predecessor geometry by [FD-102](../../findings/FD-102-adaptive-nonhead-retagging-has-an-exact-logarithmic-source-budget.md), [FD-103](../../findings/FD-103-power-dense-record-ladders-saturate-the-logarithmic-source-budget.md), [FD-104](../../findings/FD-104-direct-core-compression-uniformizes-predecessor-transport-above-the-linear-mass-floor.md) and [FD-105](../../findings/FD-105-adaptive-low-source-cap-keeps-logarithmic-predecessor-chains-at-polynomial-source-scale.md). No branch-sensitive contradiction or RH consequence is claimed.

FD-102 removes carrier identity from the deterministic nonhead budget. For a state with horizon `H` and sampled source quotient `x`,

`A(H,x)=log_2((H-1)/(8x-1))`

drops by one under a nonhead predecessor unless retagging pays through genuine source descent. FD-103 proves that the resulting `(1-Theta+o(1)) log_2 H` source-neutral window is geometrically sharp on actual power-dense source-record ladders.

FD-104 closes the old fixed-certificate transport caveat above the linear nonsquarefree-mass floor. If `U_H>=H^(1+delta)`, direct single-state core compression gives, for fixed `1/2<sigma<Theta`, a genuine predecessor `C<H` with

`U_C/C^(2sigma) >= b_sigma U_H/H^(2sigma)`.

The construction no longer needs an occupied additive block or fixed projective-quality lower bound. The actual normalized mass is the induction currency.

FD-105 then shows that high mass carries its own source tag. The exact low-source cap

`E_H^(<=L) <= 2H(L+1)`

allows the adaptive threshold `L_H=floor(U_H/(H log H))`. Almost all high-mass nonsquarefree energy lies above `L_H`, and the exact predecessor repairs preserve a destination mask above `L_H/2`. Thus the same step can be chosen with

`U_C^(>L_H/2)/C^(2sigma) >= b_sigma U_H/H^(2sigma)`

and consequently `C >> U_H/(H log H)`.

Starting from a strict false-RH record entry, the guaranteed `xi log H_0` chain therefore cannot escape by collapsing to bounded physical or source scale. For every admissible `xi`, both the realized horizons and the transported source quotients remain at a positive power of the original `H_0` throughout the guaranteed window.

The remaining obstruction is finer than survival. The scalar constant `b_sigma` takes the worst branch and discards the correlation between **how much normalized mass is lost, how strongly the horizon contracts, and how much source descent occurs**. FD-102 shows the deterministic source-neutral ceiling is already sharp, so a contradiction must recover this branchwise joint information rather than improve a global minimum constant.

**Boundary.** The theorem needs fixed-power high mass; the source tag degenerates at the exact linear floor. The logarithmic chain and its polynomial source scale do not by themselves force source descent faster than the sharp FD-102 budget.