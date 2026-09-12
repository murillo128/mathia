# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify the actual simple ground branch with state-specific tail regularity, not one-stroke `L^2` localization alone

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-282 give the one-sided aperture ledger, global exhaustion, and a terminating finite positivity certificate at each fixed aperture. PL-283--PL-284 add a conditional computer-assisted positive endpoint at `a=0.8` with a simple isolated ground state and a tiny explicit positive margin.

PL-285--PL-286 identify the sharp worst-case transport obstruction on the full canonical logarithmic form ball. Active arithmetic channels are compressed translations, and even the complete `2,3,4` source comb retains the `Theta(1/log(1/|a-b|))` modulus by phase locking.

PL-287 separates that ambient obstruction from the actual isolated state. Every compact family in `H^log` has uniform translation-form modulus `o(1/log(1/|delta|))`; conditional endpoint isolation makes the local ground branch compact in that topology. The improvement is real but qualitative.

PL-288 tests whether the existing one-stroke finite reduction already supplies the missing quantitative tail control. It does not. The certified lower form has an order-one coercive discarded block and head-tail coupling below `10^-100`, while the exact ground eigenvalue is at most `2.27e-17`; this yields the strong exact-state bound `||tail||_2<6.65e-9`. But bounded shift expectations then carry `O(10^-8)` tail uncertainty—about nine orders above the certified positivity margin—and fixed-domain translations are not norm-continuous, so `L^2` smallness gains no factor of the aperture displacement. A two-dimensional model shows the `sqrt(lambda_1)` tail scale is sharp from these inputs even for an isolated exact eigenvector.

The live theorem is therefore narrower: obtain **state-specific weighted Fourier-tail regularity with explicit constants**, a source/eigen-equation orthogonality that suppresses head-tail shift cross terms, or a direct finite certificate on a nontrivial aperture interval. Stronger bookkeeping of the one-stroke `L^2` decomposition cannot by itself transport the tiny endpoint margin.

## Separate ambient topology, branch compactness, `L^2` tail localization, quantitative frequency regularity and global coercivity

PL-287 proves the actual compact branch beats the sharp ambient inverse-log modulus qualitatively. PL-288 proves that spectacular finite-block localization in ordinary `L^2` still does not price translation transport at the required scale. Endpoint isolation, compact-branch little-o regularity, small `L^2` tail norm, weighted frequency-tail control, explicit transport radius, and aperture-uniform positivity are distinct gates.
