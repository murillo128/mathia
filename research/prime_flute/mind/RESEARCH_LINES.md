# Prime-flute mathematical questions

## Weighted source/escape balance of the complete mixed response

Can the actual normalized mixed Riesz response be written as `G_n=T_nY_n(a_n)+R_n`, where `Y_n` is the canonical fixed-axis synthesis, `T_n` is uniformly bounded in a positive Sobolev scale, `sup_n sum_i q_i|a_(n,i)|<infinity`, and the physical-high projection of `R_n` tends to zero? [MI-008](intuition/MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance.md) makes this sufficient to eliminate the local shorting-deficit witness.

PF-297 removes one candidate for a hidden local discount: the fixed-axis Robin inverse is `ell^1(q)`-nonexpansive and its complete positive action conserves `q`-mass. PF-298 removes another: the constant-boundary response of a tight one-cusp pant is a large conductance edge plus bounded killing, with relative killing `r_n=\kappa_n/c_n=O(s_n)`.

PF-299--PF-300 identify the intrinsic prime coordinate `t_n=F(p_n)` and its symmetric seam quadrature. PF-301 now removes PF-300's monotonicity caveat for the actual scalar coefficients. With

\[
b_n=\frac{\kappa_n}{c_ns_n}
\]

and `\psi_n` the triangular hat on the exact intrinsic mesh, `\int\psi_n=s_n` and

\[
B_N(t)=\sum_{n\ge N}b_n\psi_n(t)
\]

obeys the exact identity

\[
\int_{t_{N-1}}^\infty B_N(t)\,dt
=\sum_{n\ge N}\frac{\kappa_n}{c_n}.
\]

The coefficient sequence may be arbitrarily oscillatory and prime-gap correlated. Since `b_n` is bounded and `\sum s_n^2<\infty`, the directional scalar transmission satisfies

\[
\prod_{n\ge N}(1+\kappa_n/c_n)^{-1}>0
\quad\Longleftrightarrow\quad
B_N\in L^1,
\]

and its finite products are, up to one positive constant, `exp(-int B_N)` asymptotically. The scalar accumulation question is therefore no longer “find a monotone slowly varying envelope.” It is to determine the **total intrinsic mass of the actual bounded attenuation density** `b_(n,\pm)=\kappa_(n,\pm)/(c_ns_n)`, using any valid block, density, or oscillatory information.

The complete `P/H`-split return/reassembly map remains the real gate. The scalar constant compression is not known to be invariant under the full Schur problem, so even a resolved intrinsic attenuation mass must be reassembled with nonconstant modes, support loss, source forcing/cancellation, and any residual physical-high term.

## Global heavy-range projection counts after local witnesses vanish

For the PF-287 heavy low/high extension-range projection product, does the full tail have vanishing essential norm, and can its singular-value counting function satisfy the required weak-trace bound? Local high-pass annihilation in [MI-008](intuition/MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance.md) alone supplies neither conclusion. The subtraction estimate in [MI-004](intuition/MI-004-coordinate-amplification-is-not-operator-amplification.md) controls only the artificial central-collar model, not this global product.

## Prime realization within the resolved upstream-memory window

Can consecutive prime-gap isolation realize the moderate graded neck ratios of [MI-001](intuition/MI-001-relative-multigap-geometry-carries-the-spectral-signal.md), or can the surface-to-graph error be sharpened enough to resolve `w_j^2/w_(j-1)` in the hierarchies already known to occur? Arbitrarily strong separation is not the required condition: the correction must still dominate `w_j sqrt(w_1)`.

The fixed-axis `q>1` Robin leakage route is excluded by [MI-007](intuition/MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap.md), not an outstanding estimate. Generic conservative `L1` rigidity is excluded by [MI-005](intuition/MI-005-short-collar-multiplicity-reduces-to-one-local-splice.md); a construction matching only the particular canonical germ is a different claim.