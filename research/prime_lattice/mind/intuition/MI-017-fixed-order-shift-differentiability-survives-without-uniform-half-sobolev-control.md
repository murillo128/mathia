# MI-017 — Zero-order shift transport needs source-structured BV coercivity; once BV is available, the lower-order aperture terms are already C1

**Evidence level:** supported by PL-297--PL-304 and sharpened by [PL-305](../../findings/PL-305-bv-fixed-state-aperture-derivative.md). The needed uniform `C_0+BV` estimate for the actual completed-Weil ground branch, a branch-level shape derivative, and the source-specific sign theorem remain open.

PL-297 separates renormalized Hadamard boundary stress from the critical Fourier first moment. PL-298--PL-299 show that fixed-order shift derivatives can survive the zero-order limit through physical-space bounded variation even while `H^(1/2)` diverges. PL-300--PL-304 then close the generic shortcuts: simple spectral stability, the exact odd gap, every ordinary `L^p` forcing norm, and the full finite-measure forcing space do not make the logarithmic resolvent a `BV` smoother. The missing derivative measure must come from a proper source-generated range, an exact cancellation/commutator law, or a graph norm that explicitly charges first-order frequency.

PL-305 removes a separate kernel-side concern. For every fixed state

`w in C_0((-1,1)) cap BV_0((-1,1))`,

the autocorrelation `C_w` is globally `C^1`, and both `C_w(2)` and `C_w'(2)` vanish at the support edge. In Suzuki's exact scaled form this makes every prime-power activation first-order transparent: the arithmetic term is `C^1` in the aperture even when a new lag enters at `2a=log n`. The completed archimedean remainder is also `C^1`; its aperture derivative is a bounded `L^2` quadratic form because the kernel combination `r''(t)+t r'''(t)` extends continuously across the origin.

Hence, conditional on the state-side `C_0+BV` control, **no additional regularity theorem is needed for the lower-order prime-shift or completion derivative.** The full fixed-state aperture derivative is explicit and continuous through every activation threshold. The obstruction has moved cleanly to the varying state: prove uniform BV/derivative-measure compactness for the actual regularized completed-Weil eigenbranch, justify a branch-level Hadamard/Feynman--Hellmann passage, and obtain the intrinsic logarithmic boundary stress.

The arithmetic sign gate remains independent. Even a valid derivative formula does not imply monotonicity or positivity. A closing argument must show that the weighted prime autocorrelation slopes and boundary term obey a rational-prime-specific sign/first-crossing law unavailable to matched generic shift systems.

**Boundary.** PL-305 is a fixed-state statement. It does not prove differentiability of `a -> lambda_a`, does not produce the missing BV estimate, and does not turn `C^1` dependence into order structure.