# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Extract transport information special to the actual low Weil eigenbranch

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-284 give the aperture ledger, terminating fixed-aperture positivity certificate, and a conditional positive endpoint at `a=0.8` with a simple isolated ground state and tiny explicit margin.

PL-285--PL-290 separate ambient form regularity from graph-domain regularity. The ambient logarithmic form ball has sharp inverse-log transport, while the exact graph domain has a squared-log Fourier moment and sharp inverse-squared-log transport for the active `2,3,4` von-Mangoldt comb. Thus neither generic form regularity nor generic graph regularity yields a bounded aperture derivative.

PL-291 now uses structure **strictly smaller than the graph ball**. On every source-static interval, Suzuki's bounded remainder preserves every logarithmic Fourier scale, as does the exterior cross-boundary logarithmic-Laplacian term. The eigen-equation therefore bootstraps actual eigenstates to every finite logarithmic Fourier moment. For each fixed `m`, the ground-state prime-shift and eigenvalue transport is `O(log^(-2m)(1/|delta|))`. This closes `log^-2` as a genuine endpoint for the actual low branch, while still giving no positive-order Sobolev moment or aperture derivative.

The live theorem is now quantitative rather than another finite regularity upgrade: control the growth of the all-log constants strongly enough to optimize the hierarchy, obtain a genuine positive-order moment or source-specific cancellation from the low eigen-equation, or certify positivity directly over a nontrivial aperture interval. Merely proving one more logarithmic moment is exhausted.

## Separate ambient topology, graph-domain sharpness, branch-specific structure, source activations and global coercivity

The ambient logarithmic form ball has sharp inverse-log transport. The graph ball has sharp inverse-squared-log transport. Actual eigenstates satisfy every fixed logarithmic moment by PL-291, so their source-static transport is faster than every fixed inverse power of `log(1/|delta|)`, but with uncontrolled constants. These are three distinct regularity levels and none implies a power-law modulus.

Endpoint isolation, all-log branch regularity, quantitative growth of the moment constants, positive-order regularity or cancellation, activation control and aperture-uniform positivity remain separate gates. Do not infer the next one from the previous one without a theorem using the additional structure.
