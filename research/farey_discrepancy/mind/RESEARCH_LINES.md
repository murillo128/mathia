# Farey-discrepancy research lines

This file records current mathematical questions for the Farey-discrepancy line. It is a mutable synthesis, not a chronology or task list.

## Move beyond Vinogradov–Korobov-scale switched blindness to an intrinsic coercive boundary or one cofinal source

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-212--FD-221 show that the periodic switched schedule admits a physical super-square-root blind mode and that every fixed block can be realized by one exact-Euler comparison source below literal prefix coverage. FD-222 extends this to `J=O(log log N)`. FD-223 removes that first quantitative frontier: with `Phi(N)=(log N)^(3/5)/(log log N)^(1/5)`, the same reservoir/triangular-repair construction works for every `J<=kappa_beta Phi(N)` after using Vinogradov--Korobov-scale prime and Möbius input.

In that range the sampled divisor depth satisfies `D asymp 2^J`, every switched observation is at most `O_beta(D)=N^(o(1))`, yet the earlier prefix remains `X_N(N) asymp_beta N/(D log N)=N^(1-o(1))`. Exact Euler relations still hold through every prime `p<=beta N`, with `beta<1`. Thus stretched-logarithmically many scheduled observations remain noncoercive while the source may be rebuilt for each horizon.

The live question is no longer whether one can push past log-log growth. A positive route must identify an **intrinsic** failure of reservoir capacity/repair that cannot be repaired by stronger source estimates, force literal Euler-prefix coverage, or impose compatibility across an unbounded sequence of horizons so that one source rather than a scale-dependent comparison source carries the observations. Merely reaching the current Vinogradov--Korobov analytic ceiling is not evidence that the filter itself becomes coercive.

## Keep observation depth, analytic input, reservoir capacity, literal coverage and source identity distinct

The FD-223 threshold mixes two quantitative costs: divisor reservoirs shrink like `2^-J` while the triangular correction grows exponentially in `J`; unconditional Vinogradov--Korobov cancellation absorbs both up to a fixed multiple of `Phi(N)`. Failure of this particular proof beyond that scale could therefore reflect the available analytic remainder rather than loss of source freedom.

Future work should say which currency changes. Literal coverage removes unused prime coordinates. Cofinal compatibility removes the freedom to rebuild a new source at each `N,J`. A genuinely intrinsic capacity theorem would show that every admissible repair fails for structural reasons. These are different statements, and none follows merely from exhausting the present VK estimate.