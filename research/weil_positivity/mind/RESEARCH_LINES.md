# Weil-positivity research lines

This file holds the current mathematical questions suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-forced mixed-prime sign mechanism beyond universal positive completion and regular scalar sparsification

**Linked intuitions:** `MI-039-enriched-semigroups-inherit-obstructed-scalar-shadows-or-universal-lifts` through `MI-055-centered-prime-power-toeplitz-positivity-pays-a-divergent-diagonal-tax`.

WP-356--WP-370 classify the finite Hecke, finite--archimedean and componentwise Whittaker scale routes. Genuine arithmetic incidence survives in nonconstant finite modes, but canonical positive squares scalarize critical half-density; common homogeneous globalization separates variables; the unique critical power scale freezes `nY`; exact diagonal Hecke equivariance forces that same ray; and ordinary positive boundary `L^2` squares the desired amplitude.

WP-371 isolates the prime-power Toeplitz carrier. The desired nonzero Fourier coefficients are exactly those of the centered Poisson kernel, but the centered kernel is indefinite. If each prime ray is completed independently by a scalar diagonal, positivity requires at least `2 log p/(sqrt(p)+1)` at prime `p`, and summing these local taxes diverges.

WP-372 shows that this divergence is **not** a global scalar positivity obstruction once arbitrary mixed-prime coefficients are allowed. On the prime torus, a positive measure with the prescribed positive-sign one-prime rays exists iff its total mass satisfies `C>=C_+^*=sup_p 2 log p/(sqrt(p)+1)`, and the sharp supremum is finite. Requiring mixed-prime coefficients to vanish restores the divergent sum tax; the same sparse obstruction survives after restriction to the common prime-log line.

WP-373 closes the most regular attempt to recover sparsity *after* taking the finite-mass mixed completion. For the explicit WP-372 product completion, already the two-prime mixed frequencies

`m log 2 + n log 3`, `m,n!=0`,

are dense in the common line. Any continuous scalar Fourier multiplier that erases all those mixed modes must vanish on a dense set and hence vanish identically, so it cannot preserve even one pure prime-power lane. This covers ordinary `L^1` convolution kernels and finite-measure convolution responses. The obstruction is genuinely infinite: every finite keep/erase pattern admits an exact `C_c^infinity` multiplier with Schwartz kernel.

The surviving Weil route must therefore do more than “complete positively, then filter regularly.” It must either retain a source-forced mixed-prime sector in the final global pairing and prove the correct Weil orientation there, or leave the continuous scalar common-line multiplier class through a non-scalar, nonlinear, source-dependent, intrinsically rough or genuinely geometric quotient equipped with its own positivity theorem. Finite truncations are not evidence that such an infinite selector exists.

## Keep arithmetic content, positivity, mixed-prime completion and selector topology distinct

The current audit distinguishes finite Hecke incidence, critical half-density, diagonal Hilbert squaring, prime-power Toeplitz coupling, zero-mode completion cost, mixed-prime Fourier freedom, sparse versus dense prime support, common-line restriction, selector continuity and sign coercivity.

WP-372 adds the global completion diagnostic: a divergent local positive-completion tax can disappear when cross-coordinate coefficients are allowed. WP-373 adds a second, topological diagnostic: once the mixed sector is present on the common line, a selector that kills it everywhere cannot be both scalar and continuous while retaining the sparse arithmetic lanes. A finite frequency truncation passes an exact smooth matched control, so numerics at bounded support can systematically hide the infinite obstruction.

Any next proposal should state which mixed-prime coefficients are actually forced by the finite/archimedean arithmetic construction, whether those constraints admit a finite positive completion, whether the final criterion may retain those mixed coefficients, and—if sparsification is still required—what operator class performs it and why its topology evades the WP-373 density obstruction. Independent local Poisson blocks are too sparse; an arbitrary product completion is too free; a regular scalar post-selector is too rigid.
