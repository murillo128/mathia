# Prime-flute mathematical questions

## Weighted source/escape balance of the complete mixed response

Can the actual normalized mixed Riesz response be written as `G_n=T_nY_n(a_n)+R_n`, where `Y_n` is the canonical fixed-axis synthesis, `T_n` is uniformly bounded in a positive Sobolev scale, `sup_n sum_i q_i|a_(n,i)|<infinity`, and the physical-high projection of `R_n` tends to zero? [MI-008](intuition/MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance.md) makes this sufficient to eliminate the local shorting-deficit witness.

PF-297 removes one candidate for a hidden local discount: the fixed-axis Robin inverse is `ell^1(q)`-nonexpansive and its complete positive action conserves `q`-mass. PF-298 removes another: the constant-boundary response of a tight one-cusp pant is a large conductance edge plus bounded killing, with isolated scalar transmission `1-O(s_n)`.

PF-299--PF-300 now calibrate the accumulated scalar loss in the **intrinsic prime coordinate** `t_n=F(p_n)`. The exact seam weights

\[
s_n=\frac{(t_n-t_{n-1})+(t_{n+1}-t_n)}2
\]

form a symmetric Riemann quadrature: for every nonnegative decreasing `phi`, convergence of `sum s_n phi(t_n)` is equivalent to convergence of `int phi(t)dt`. In particular

\[
\sum_n\frac{s_n}{(1+F(p_n))^\beta}
\]

diverges for `beta<=1` and converges for `beta>1`. Thus the scalar gate is sharper than “linear versus a fixed superlinear power of `s_n`.” A killing law `epsilon_n\asymp s_n(\log p_n)^{-\beta}` still absorbs the scalar channel for `beta<=1`; for `beta>1` it is summable. At the critical `beta=1`, an asymptotic `epsilon_n\sim a s_n/(1+F(p_n))` would give transmission `(\log p_n)^{-a+o(1)}`.

The next pant calculation should therefore determine the relative killing in the form `epsilon_n=s_n a_n` and control `a_n` in the intrinsic coordinate, rather than search for another depth-uniform contraction gap. Prime-gap irregularity no longer needs to be averaged at the accumulation stage once the exact `F(p_n)` mesh is used.

The complete `P/H`-split return/reassembly map remains the real gate. The scalar constant compression is not known to be invariant under the full Schur problem, so even a resolved scalar accumulation law must be reassembled with nonconstant modes, support loss, source forcing/cancellation, and any residual physical-high term.

## Global heavy-range projection counts after local witnesses vanish

For the PF-287 heavy low/high extension-range projection product, does the full tail have vanishing essential norm, and can its singular-value counting function satisfy the required weak-trace bound? Local high-pass annihilation in [MI-008](intuition/MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance.md) alone supplies neither conclusion. The subtraction estimate in [MI-004](intuition/MI-004-coordinate-amplification-is-not-operator-amplification.md) controls only the artificial central-collar model, not this global product.

## Prime realization within the resolved upstream-memory window

Can consecutive prime-gap isolation realize the moderate graded neck ratios of [MI-001](intuition/MI-001-relative-multigap-geometry-carries-the-spectral-signal.md), or can the surface-to-graph error be sharpened enough to resolve `w_j^2/w_(j-1)` in the hierarchies already known to occur? Arbitrarily strong separation is not the required condition: the correction must still dominate `w_j sqrt(w_1)`.

The fixed-axis `q>1` Robin leakage route is excluded by [MI-007](intuition/MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap.md), not an outstanding estimate. Generic conservative `L1` rigidity is excluded by [MI-005](intuition/MI-005-short-collar-multiplicity-reduces-to-one-local-splice.md); a construction matching only the particular canonical germ is a different claim.