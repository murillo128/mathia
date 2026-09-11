# MI-001 — The resolved eigenvalue remembers the upstream neck; the determinant does not

**Evidence level:** proved for the fixed-topology graded window; prime realization of that window remains conditional.

For a fixed path of `N` hyperbolic pants, let the separating lengths satisfy `w_1=epsilon -> 0` and `w_j/w_{j-1}=epsilon^{alpha_j}`, with `0<alpha_2<...<alpha_{N-1}<1/2`. This concrete sufficient window makes both the downstream correction and Burger's surface-to-graph error smaller than the upstream term. For `2<=j<=N-1`, [PF-091](../../findings/PF-091-graded-multiscale-burger-window-resolves-an-upstream-memory-ladder.md) gives

\[
\lambda^{(j)}=\frac{j+1}{2\pi^2j}w_j-
\frac{(j+1)(j-1)^2}{2\pi^2j^3}\frac{w_j^2}{w_{j-1}}
+o(w_j^2/w_{j-1}).
\]

The coefficient comes from the centered path resistance `R_j=j^{-2} sum_{m<j} m^2/w_m`; the preceding neck dominates this sum. The error comparison that matters is `w_j sqrt(w_1)/(w_j^2/w_{j-1})=sqrt(w_1)/(w_j/w_{j-1}) -> 0`, not merely the fact that the necks are hierarchical.

For prime-derived tangents with `w_j=4 sqrt(d_j/d_{j+1})(1+o(1))`, the correction is proportional to `d_j^{3/2}/(d_{j+1} sqrt(d_{j-1}))`: it retains an ordered three-gap relation. In contrast, the weighted-path identity `pdet G=N product_j w_j` erases that correction; in the two-neck example `mu_+ mu_-=3ab` although the individual eigenvalues have opposite `b^2/a` shifts ([PF-089](../../findings/PF-089-low-energy-determinant-cancels-hierarchical-interscale-memory.md)). Preserve the resolved eigenvalue if that upstream dependence is the intended observable.

The surface calculation does not establish that consecutive prime gaps recurrently realize the displayed moderate hierarchy. Stronger separation supplied by isolation results need not lie above the Burger error floor. Nor does retaining relative gap shape by itself distinguish primes from matched nonprime endpoint sequences.
