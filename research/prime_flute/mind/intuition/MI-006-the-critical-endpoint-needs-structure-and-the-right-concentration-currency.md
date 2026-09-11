# MI-006 — Exponential far propagation leaves only a logarithmic low-output window to control

**Evidence level:** proved sufficient/necessary leakage reduction; not a physical-source estimate.

Let `K>=kappa I>0`, `B` bounded, and `E_Lambda=1_[Lambda,2Lambda)(K)`. Suppose the far leg satisfies `||P 1_[M,infinity)(K)||<=C exp(-dM)`. For an input weight `R>=0`, [PF-271](../../findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage.md) gives the sufficient condition

\[
A>R/d,\quad \varepsilon>0,\quad
\|1_{[\kappa,A\log\Lambda]}(K)B E_\Lambda\|
\lesssim\Lambda^{-R-\varepsilon}
\ \Longrightarrow\ PBK^R1_{[Z,\infty)}(K)\text{ bounded}.
\]

The output above `A log Lambda` is already paid for by propagation. Hence failure of a bare comparable-high-input/high-output estimate does not refute this composed map. For the exact propagator `P=exp(-dK)`, boundedness conversely forces `||1_[kappa,M](K) B E_Lambda|| <= 2^R ||PBK^R1_[Z,infinity)|| exp(dM) Lambda^-R`; every fixed output row must obey the full `Lambda^-R` decay.

With only polynomial far smoothing, a sublinear window `Lambda^theta` suffices if the far leg pays an exponent `p` with `theta p>R` and the low leakage has the same extra `epsilon` decay. These are operator-ordering reductions, not assertions that Robin conversion satisfies the hypotheses. The fixed-axis normalized source fails the supercritical fixed-row requirement by [MI-007](MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap.md); do not retain that instance as an open positive escape.
