# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Turn the exact squared-log eigenstate regularity into a quantitatively useful source-specific transport bound

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-282 give the one-sided aperture ledger, global exhaustion, and a terminating finite positivity certificate at each fixed aperture. PL-283--PL-284 add a conditional computer-assisted positive endpoint at `a=0.8` with a simple isolated ground state and a tiny explicit positive margin.

PL-285--PL-286 identify the sharp worst-case transport obstruction on the full canonical logarithmic form ball. PL-287 shows that the actual compact ground branch beats that inverse-log modulus qualitatively. PL-288 proves that even extremely strong ordinary `L^2` tail localization from the existing finite reduction still pays a square-root transport barrier and is many orders too weak for the certified margin.

PL-289 now supplies the missing state-specific frequency regularity exactly. For Suzuki's one-dimensional principal logarithmic operator `T` on `(-1,1)`,

`D(T) = {u : (log|xi|+gamma) Fourier(Eu)(xi) in L^2}`, 

and

`(1/(2 pi)) int (log|xi|+gamma)^2 |Fourier(Eu)(xi)|^2 dxi <= ||Tu||_2^2 + (pi^2/2)||u||_2^2`.

The canonical Weil operator is a bounded perturbation of `T` on every source-static aperture interval, so its eigenstates inherit a uniform squared-log Fourier moment. Their translation/autocorrelation modulus is consequently

`O(1/log^2(1/|delta|))`,

a full logarithmic power better than the sharp ambient `Theta(1/log)` law and stronger than the qualitative compact-family little-o from PL-287.

The ambient regularity barrier is therefore no longer the live theorem. The remaining problem is quantitative and arithmetic: obtain a sufficiently small **state-specific constant**, an eigen-equation/source cancellation identity that suppresses the moving prime-shift contribution, or a direct finite certificate over a nontrivial aperture interval. A coefficient of ordinary size multiplying `log^-2` is still far too large to transport the `~10^-17` endpoint margin over a useful aperture displacement.

## Separate ambient topology, graph-domain regularity, quantitative constant, source activations and global coercivity

PL-289 is an operator-domain theorem, not an ambient form-domain estimate. It removes the generic inverse-log obstruction for actual eigenstates but does not make the resulting modulus numerically useful, and aperture activations still require the existing source bookkeeping. Endpoint isolation, squared-log moment, explicit transport constant, activation control and aperture-uniform positivity remain separate gates.