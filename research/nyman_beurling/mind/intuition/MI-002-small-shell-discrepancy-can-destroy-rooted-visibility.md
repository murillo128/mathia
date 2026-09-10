# MI-002 — Small shell discrepancy can make rooted Nyman mixing invisible rather than useful

**Evidence level:** exact target-aware preperiod mixing, coefficient rigidity, and rooted-band invisibility through NB-021

## Core intuition

For the canonical Nyman residual, faster shell mixing is not automatically better transport. The same low discrepancy that lets dilation averages settle early can force the settled scalar to zero while the old normal equations still anchor both ends of the multiplicative edge.

This creates an antagonism between **mixing** and **visibility**. The live quantity is not how quickly the residual becomes simple, but whether the simplification retains a component visible to the section that must pay the Nyman distance budget.

## Strongest justified principle

NB-019 replaces the full shell period by the target-aware coefficient budget `mathfrak A_N=sum j|a_{N,j}|` and gives uniform preperiod mixing error `O(mathfrak A_N/m)`. The actual projection can therefore mix far before the lcm scale if its coefficients permit it.

NB-020 shows that those coefficients are themselves source-rigid. Early harmonic-shell differences recover them by Möbius inversion, giving `|a_{N,n}+mu(n)| <= 2 d_N sigma(n)` and the lower bound `mathfrak A_N >= c min(N^2,d_N^{-2})`. Along `d_N->0`, the sufficient mixing regime cannot start before the inverse-distance scale in the crude coefficient majorant.

NB-021 uses the old `g_2` normal equation to tie the deep-mixing mean `mu_N` to intrinsic consecutive discrepancy `Delta_N`: whenever `2m<=N`, `|mu_N|<=2Delta_N/m`. Hence `Delta_N=o(N)` forces `mu_N->0` and yields a growing band `K_N<=m<=N/2` on which `Q_m r_N->0` uniformly. If the limiting Nyman distance were positive, the full defect on that same band diverges logarithmically while the visible projected defect tends to zero.

## Program consequence

Do not use preperiod shell mixing as a proxy for useful enrichment. Seek source-specific multiplicative energy in channels before the rooted zero-mixing regime or beyond the `N/2` anchor, or prove a quantitative lower bound on the canonical shell discrepancy and show that the resulting nonzero variation is visible in the NB-015 scale-coupled quotient.

## Counterevidence / boundary

NB-021 does not prove `Delta_N=o(N)` for the actual residual and does not control the entire future visibility statistic. Early channels below `K_N` and genuinely unrooted channels beyond `N/2` remain open. The coefficient lower bound is a limitation of the current absolute majorant, not a universal lower bound for every mixing argument.

## Epistemic status

**Exact source-specific incompatibility between sublinear shell discrepancy and useful rooted deep mixing; viable visibility channels remain outside the proved band.**

## Falsification criterion

Produce an actual residual with `Delta_N=o(N)` but a nonvanishing rooted mixed scalar contrary to NB-021, or invalidate the early-shell Möbius inversion/coefficient floor. A positive continuation should prove visible source energy in a channel not erased by the rooted mixing mechanism.
