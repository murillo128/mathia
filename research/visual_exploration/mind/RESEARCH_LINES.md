# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-293 separate the isolated coefficient profile, Wang's complete pair statistic, deterministic gamma structure and the RH-equivalent continuation boundary of the exact source transform. VIS-294--VIS-298 then close the apparent moving lower-source branch: after exact gamma recentering, every moving `x(T)->infinity` under a fixed upper exponent has

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `sqrt(log T)` and related lower-source thresholds were proof-packaging artifacts rather than arithmetic transitions.

## Replace hard-tail finite-window transfer by energy-sensitive infinite-spectrum control

**Linked intuition:** `MI-040-wang-pointwise-upper-ceiling-is-a-localization-coherence-budget`.

VIS-299--VIS-304 progressively move the first generic upper error wall from localization leakage to the coefficient-specific prime-power spacing bound `x log log x=o(H)`. VIS-305--VIS-308 show that this absolute scale is not itself a signed arithmetic obstruction: density/parity controls, exact support with randomized phases, and completely multiplicative same-base harmonic controls all cancel well below `H` at the candidate boundary.

VIS-309 then compares those controls to the actual common-time orbit. For fixed `x,H`, the deterministic phases `p^(-it)` have the same long-time quadratic mean as Haar completely multiplicative phases. The Bohr mean square is `O(x log^3(3x))`, so generic deterministic alignment across primes is not the missing mechanism.

VIS-310 quantifies the crudest finite-window transfer. Hard truncating the infinite prime-power series and compressing every retained ratio frequency to one global minimum gap yields a sufficient averaging horizon only at

`V >> x^5 log^3 x/(log log x)^2`

when `H~x log log x`. That quintic scale is a proof-representation cost, not a lower bound on true dephasing.

VIS-311 removes most of the worst-gap loss. Keeping the local spacing `delta_lambda` of each grouped rational-ratio frequency and its coefficient energy gives

`sum_lambda m_lambda |B_lambda|^2 << x^2 log^3(3x)`,

where `m_lambda` is the reduced rational height. The weighted Montgomery--Vaughan inequality then lowers the sufficient finite-window horizon to

`V >> x^3 log^3 x/(log log x)^2`.

Two powers of `x` were therefore artifacts of global-gap compression. The remaining cubic loss comes from the **uniform hard-tail estimate**, which forces the optimized cutoff far beyond the natural support before the full remainder is certified small.

The live finite-height problem is now narrower. A useful next theorem should keep the infinite ratio spectrum in an energy norm—through a smooth/dyadic decomposition, direct nontruncated mean square, or another coefficient-sensitive tail estimate—and ask whether the observation window can approach the natural `V~H~x log log x` scale. The opposite useful outcome would be an explicit sparse family of near-resonant ratios and heights carrying enough Wang coefficient mass to force an `H`-scale remainder despite the small Bohr energy.

The accepted clue `CLUE-wang-fixed-source-packet-localization` already records this destination. Another hard-cutoff spacing estimate that leaves the uniform tail untouched is no longer the most informative move.

## Recombine exact deterministic structure and decompose every newly exposed proof wall before interpreting it

The current ledger separates packet variation, source exponent, localization leakage, coefficient majorants, support-sensitive spacing, random versus completely multiplicative phases, the actual prime-log time orbit, Bohr/Haar equivalence, global versus local ratio spacing, hard versus energy-sensitive tail treatment, finite-window length, moving-frequency limits and the analytic domain of the source transform.

VIS-294--VIS-311 give a repeated control pattern. Exact deterministic pieces can be split too early; generic majorants can lose logarithms; matched support models can show an absolute norm is generic; exact support can still cancel after phase randomization; same-base harmonic relations can be preserved without restoring the boundary; the true deterministic orbit can have the same long-time quadratic mean as Haar; and even a finite-window proof can manufacture polynomial horizons by compressing weighted spectrum or paying the tail in uniform norm.

A structural transition is credible only after the surviving **finite-height/moving-frequency coherence mechanism** defeats a control that preserves the coefficient distribution, local ratio geometry, infinite tail and destination quantifier at the same scale.