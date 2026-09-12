# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify the actual simple ground branch beyond the sharp ambient inverse-log modulus

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-282 give the one-sided aperture ledger, global exhaustion, and a terminating finite positivity certificate at each fixed aperture. PL-283--PL-284 add a conditional computer-assisted positive endpoint at `a=0.8` with a simple isolated ground state and a tiny explicit positive margin.

PL-285--PL-286 identify the sharp worst-case transport obstruction on the full canonical logarithmic form ball. Active arithmetic channels are compressed translations, and even the complete `2,3,4` source comb retains the `Theta(1/log(1/|a-b|))` modulus by phase locking.

PL-287 now separates that ambient obstruction from the actual isolated state. Every **compact** family in `H^log` has uniform translation-form modulus `o(1/log(1/|delta|))`; the sharp lower witnesses necessarily move Fourier mass to frequency `~1/delta` and therefore escape compact sets. At the conditionally certified simple ground state near `a=0.8`, common-domain form continuity yields an `H^log`-continuous normalized ground branch on a sufficiently small source-static neighborhood. Its image is compact, so

`|lambda_1(a)-lambda_1(b)| = o(1/log(1/|a-b|))`

as `a,b->0.8` within that neighborhood.

This is a real state-specific improvement, but only qualitative. It gives no computable radius over which the tiny positive endpoint margin survives and no bridge to the next prime-power activation. The live theorem is therefore **quantitative uniform logarithmic-tail control for the actual ground branch**, or another eigen-equation/source identity that turns branch compactness into an explicit transport modulus strong enough to preserve positivity.

## Separate ambient topology, branch compactness, quantitative tail control and global coercivity

A simple isolated ground state already gives local branch tracking, and PL-287 proves that the actual branch cannot asymptotically saturate the sharp ambient inverse-log modulus on a compact source-static neighborhood. What remains is not qualitative continuity but a quantitative tail/radius estimate. Endpoint isolation, compact-branch little-o regularity, explicit transport radius, and aperture-uniform positivity are distinct gates.
