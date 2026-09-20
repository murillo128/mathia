# Farey-discrepancy research lines

This file records current mathematical questions for the Farey-discrepancy line. It is a mutable synthesis, not a chronology or task list.

## Isolate a capacity-feasible oscillatory null cushion after smooth scale-adapted fills fail

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-212--FD-224 separate periodic switched blindness, exact-Euler source quantifiers and literal coverage. The long blind constructions keep one absolute cutoff `p<=beta N<N`; a fixed positive fractional exact-Euler rule across dyadic horizons instead reaches the original prefix after finitely many steps and identifies the source there. Cofinal exhaustive exact Euler compatibility is therefore source identity, not a remaining switched-filter problem.

FD-225 removes switched-matrix conditioning. The full divisor-reservoir response has an exact inverse, so all integer-multiple samples through depth `D` can be flattened to one common value up to unit rounding error while retaining an `N^(1-o(1))` earlier defect through the certified Vinogradov--Korobov range. FD-226 then replaces equal-width reservoirs by exact floor cells whose width scales with the divisor, removing one power of `D` from the prime-resolution error. The certified depth still does not improve because a common positive occupancy cushion must absorb the physical Mertens correction.

FD-227 now kills the most natural nonconstant escape. For

`(A b)(m)=sum_(d<=m) b_d M(floor(m/d))`

and any `b_d=c d^sigma+o(d^sigma)` with `sigma>0`,

`(A b)(m)=c m^(sigma+1)/((sigma+1) zeta(sigma+1))+o(m^(sigma+1))`,

so every fixed positive-order dyadic root row `(T-I)^r` sees the same leading power multiplied by `(2^(sigma+1)-1)^r`. In particular the natural capacity profile `b_d asymp d` creates a quadratic switched signal. The constant cushion is exceptional because `A 1=1` exactly and every positive-order root difference kills it.

The live capacity question is therefore no longer whether an arbitrary smooth scale-adapted target can let larger reservoirs carry more correction. Any successful nonconstant switched-null cushion must have order-one relative oscillation, depletion or redistribution across divisor scales. The decisive next test is whether the exact switched nullspace contains a **capacity-feasible oscillatory occupancy profile** with enough cellwise lower slack to absorb the physical Mertens correction, or whether every such null profile is forced to expose small-capacity cells often enough to restore the present bottleneck.

## Keep literal coverage, exact inversion, prime resolution and oscillatory capacity distinct

The present frontier has four different currencies. Literal exact-Euler coverage controls whether relaxed sources exist at all. Full-divisor inversion controls whether the switched observation equations are algebraically hard. Scale-adapted cells control how accurately primes resolve those equations. The remaining source-capacity problem controls whether a positive physical realization can absorb the Mertens baseline while also lying in the switched nullspace.

FD-227 shows that this last currency has a genuine **shape** constraint: smooth positive power-law occupancy is asymptotically visible even when algebraic inversion and prime resolution are favorable. A stronger blind construction must therefore exploit an oscillatory capacity profile rather than repackage the first three currencies. Conversely, an intrinsic coercive result must show that every capacity-feasible switched-null profile necessarily loses enough positive slack; ruling out only the current constant cushion or smooth fixed-fraction fills is not enough.