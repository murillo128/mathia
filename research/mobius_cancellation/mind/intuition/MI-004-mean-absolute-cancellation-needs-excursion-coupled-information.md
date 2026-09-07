# MI-004 — Mean-absolute Mertens control needs excursion information beyond fixed local feedback

**Evidence level:** exact Mellin/checkpoint results, literature-backed Pintz lower bound, matched-control barriers, and fixed-local feedback classifications through MC-124

## Core intuition

The mean-absolute endpoint is RH-complete, but several natural weaker carriers forget exactly the information that endpoint consumes. MC-117--MC-120 show that sub-`L^1` moments can miss rare coherent amplitude even after square-free support, multiplicativity, polynomial windows, and one fixed multiplicative comparator are imposed. MC-121 separately shows that once the **actual Möbius** first absolute mean reaches the square-root exponent on any unbounded checkpoint sequence, dense output coverage is unnecessary.

MC-122--MC-124 now sharpen the source side. Deterministically weighted amplitude feedback is quadratic path energy in disguise; scalar state-local one-step feedback has only a potential part plus unoriented occupation; and adding any fixed amount of local Möbius memory does not create a new sign-odd logarithmic information channel, because every fixed cylinder observable reduces to classical fixed-shift `mu/mu^2` correlations.

The surviving difficulty is therefore not to decorate a local feedback rule. A successful source theorem must recover first-absolute excursion amplitude from information that leaves the **fixed state/fixed-memory cylinder class** in a quantitative way: growing or state-coupled memory, multiscale/nonlocal structure, a genuinely arithmetic occupation theorem, or another source statistic with a polynomial information budget.

## Strongest justified principle

MC-115 proves that square-root-scale mean-absolute Mertens control is equivalent to RH. MC-121 uses Pintz's every-large-scale lower bound to show that this control need only hold on an arbitrary unbounded sequence for the actual Möbius function. Thus scale density of the final endpoint is not the missing theorem.

For every `0<p<1`, MC-117--MC-120 quantify and realize the gap between weak moments and first-absolute amplitude even under increasingly strong generic multiplicative controls. MC-122 then proves for arbitrary deterministic weights

`2 sum w_n mu_n M_{n-1} + sum w_n mu_n^2 = w_N M_N^2 + sum_{n<N}(w_n-w_{n+1})M_n^2`,

so weighting the amplitude correlation does not create a new signed carrier. MC-123 classifies every `Psi(M_{n-1},mu_n)` as a potential increment plus reversal-even edge/loop occupation; no additional oriented one-step state-local degree of freedom exists on the scalar Mertens tree.

MC-124 tests the first genuine topological escape. Finite memory creates cycles, but every fixed finite-window observable odd under simultaneous Möbius sign reversal expands exactly into fixed shifted products of `mu` and `mu^2`. The Tao--Teräväinen product criterion makes every such term `o(log x)` under logarithmic averaging. Fixed memory therefore escapes the tree topology without escaping the established fixed-correlation information class.

## Counterevidence / boundary

None of MC-122--MC-124 says that occupation statistics, growing memory, or nonlocal correlations are useless. MC-123 explicitly leaves reversal-even occupations as potentially arithmetic, and MC-124 is qualitative/logarithmic and fixed-window only. A quantitative theorem for a growing/state-dependent observable could lie outside these no-go classes.

Likewise, logarithmic invisibility does not imply small ordinary partial sums. The existing multiplicative controls show that qualitative correlation cancellation can coexist with very large cumulative excursions. Any proposed escape must state the quantitative transfer to `D_M`, not merely a new nonzero cycle or correlation.

## Epistemic status

**Proved/literature-backed endpoint reduction and exact fixed-local feedback restrictions; open Möbius-specific quantitative source mechanism outside those classes.** No improved unconditional Mertens bound is asserted.

## Falsification criterion

Derive the RH-scale first absolute mean on some unbounded sequence from a source condition genuinely weaker than that conclusion and satisfied by Möbius, while showing why the MC-117--MC-124 controls cannot satisfy or neutralize it. Conversely, exhibit a fixed state-local or fixed finite-memory sign-odd observable that carries a quantitatively new oriented component contrary to the exact decompositions above.