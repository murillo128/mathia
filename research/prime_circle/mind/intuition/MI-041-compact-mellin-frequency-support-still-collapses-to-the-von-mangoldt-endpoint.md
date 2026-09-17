# MI-041 — Compact Mellin-frequency support still collapses to the von Mangoldt endpoint

**Evidence level:** exact synthesis from [PC-335](../../findings/PC-335-bounded-mellin-selectors-cannot-isolate-prime-powers.md) through [PC-338](../../findings/PC-338-compact-mellin-support-collapses-to-von-mangoldt-endpoint.md). The Paley--Wiener/Jensen growth principles are classical; the Mathia content is their application to the exact cyclotomic radial-flux factorization.

The finite point-support classification of PC-337 is not the real boundary. Fix a vertical Mellin line `s=sigma+it` and let `T` be any compactly supported distribution in the real frequency `t`. If the induced shell response annihilates every mixed semiprime `pq`, PC-338 proves

`L_T(n)=0` for every `n>1` when `sigma!=1`,

while on the endpoint line `sigma=1` the only visible response is

`L_T(n)=c Lambda(n)`.

The mechanism is an analytic uncertainty principle. Multiplying `T` by one prime shell and testing the second prime produces an entire function of finite exponential type whose zeros include `log q` for every prime `q`. Prime logarithms are far too dense for a nonzero entire function of that growth, so the function vanishes identically. Off the endpoint this kills the response by polynomial-growth/Bezout arguments; at the endpoint compact support leaves only a scalar delta at `t=0`, hence ordinary von Mangoldt.

Therefore widening a finite Mellin selector into a compact interval, compact singular measure, compact distribution of arbitrary finite order or finite union of compact bands does not create a new exact prime-power selector. The endpoint `s=1` remains the unique visible compact-frequency semiprime-null channel.

This sharpens the representation boundary: **the escape is not “continuous instead of discrete frequency support,” but genuinely noncompact/global frequency structure or leaving the fixed scalar shell readout category altogether**. Shell-dependent selectors, nonlinear operations, matrix-valued refinement or cross-shell coupling may still retain structure unavailable to compact scalar distributions, but simply taking more frequencies inside a bounded Mellin window does not.

**Boundary.** PC-338 is an exact selector classification, not a zero theorem. It says nothing about noncompact Mellin-frequency support, analytic functionals outside compact distributions, shell-dependent symbols, nonlinear/matrix readouts or cross-shell couplings. Components of `T` supported at zeros of the universal zeta envelope may survive as distributions but are invisible to every shell, so they are not a shell spectral mechanism.