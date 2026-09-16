# MI-034 — Chebyshev capacity pins the growing-moment terminal threshold at `4 tau_r`

**Evidence level:** exact-derived and sharp in the generalized terminal-packet class by [RE-162](../../findings/RE-162-chebyshev-interpolation-pins-the-growing-terminal-threshold-at-four-factorial-radii.md), sharpening the order-of-magnitude hierarchy of RE-159--RE-161.

Exact matching of placement moments through degree `r-1` annihilates every polynomial of degree below `r`. The remaining terminal-kernel ambiguity is therefore a uniform polynomial-approximation problem, not specifically an endpoint Taylor-remainder problem.

For terminal width `L=o(1)` in the stated growing-order regime, the optimal normalized discrepancy is

`D_(r,U)(L) = (4+o(1)) (L/4)^r/r!`.

Chebyshev interpolation gives the upper bound because the monic degree-`r` polynomial of minimum sup norm on `[0,L]` has size `2(L/4)^r`. Opposite level sets of the same scaled Chebyshev polynomial give two equal-weight `r`-point packets with exactly matching lower moments and attain the same asymptotic constant. The lower construction evaluates the full nonlinear kernel through divided differences, so it does not rely on truncating after the first uncancelled Taylor term.

With `tau_r=(r! eta_p)^(1/r)`, the PNT-small source capacity is therefore governed by

`F_p = (L/(4 tau_r))^r`.

If `F_p=O(1)`, every vanishing insertion budget has `o(1)` Robin leverage. If `F_p->infinity`, vanishing-budget matched controls can retain any prescribed fixed source separation. The sharp factorial radius is

`L_crit = 4 tau_r = (4/e+o(1)) r eta_p^(1/r)`.

This replaces the previous universal-constant uncertainty by a sharp exponential-scale boundary. RE-161's approximate-moment warning remains independent and load-bearing: the Chebyshev threshold assumes exact lower-moment matching; with errors one must still control the weighted leakage `sum_(k<r)|mu_k|/k!` at the destination scale.

The source-side frontier is now explicit. A prime/CA theorem must either keep terminal width on the stable side of `4 tau_r`, provide the required factorial precision for approximate moments, or exploit a signed arithmetic relation outside this moment-matching capacity class. Merely increasing exact moment order without respecting the Chebyshev radius is not leverage.
