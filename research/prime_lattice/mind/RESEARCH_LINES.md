# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Extract transport information special to the actual low Weil eigenbranch

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-284 give the aperture ledger, terminating fixed-aperture positivity certificate, and a conditional positive endpoint at `a=0.8` with a simple isolated ground state and tiny explicit margin.

PL-285--PL-291 separate ambient form regularity, graph-domain regularity and actual eigenbranch regularity. Generic form and graph balls have only inverse-log and inverse-squared-log transport, while the source-static eigen-equation places actual eigenstates in every finite logarithmic Fourier scale.

PL-292 now quantifies that all-log hierarchy. On compact source-static aperture intervals the logarithmic moments can be bounded by `exp(C m^2 log(m+2))`; optimizing over `m` gives a subpower modulus roughly `exp(-c (log log(1/|delta|))^2/log log log(1/|delta|))`. This is faster than every fixed inverse-log power but still slower than every Hölder modulus.

The same finding isolates a method barrier: physical cutoffs on the logarithmic spaces have norm at least `(c m)^m`, so the generic PL-291 bootstrap cannot be upgraded to positive-order Sobolev/Hölder regularity merely by tightening its cutoff constants. The live theorem must exploit state-specific endpoint cancellation, another structure that avoids the worst-case cutoff, or certify positivity directly over a nontrivial aperture interval.

## Separate ambient topology, graph-domain sharpness, optimized all-log transport and positive-order regularity

The regularity ladder is now quantitative. Ambient form control gives inverse-log transport; graph-domain control gives inverse-squared-log transport; actual eigenstates have an optimized subpower modulus from all logarithmic moments. None supplies a positive power of `|delta|` or a justified aperture derivative.

The cutoff lower bound is a method obstruction, not an eigenstate obstruction. It does not prove that the actual low eigenfunction saturates the bad boundary tail. A further improvement must therefore visibly use the selected eigenstate/source equation rather than repeat the generic cutoff bootstrap at higher logarithmic order.