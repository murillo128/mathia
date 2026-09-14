# MI-023 — Blindness survives rowwise; normalization can move rather than remove source depth

**Evidence level:** proved for the current flat Christoffel source through [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md)--[MC-278](../../findings/MC-278-rational-endpoint-decoder-hidden-half-depth.md). No signed arithmetic cancellation theorem or blind-support exclusion is claimed.

MC-273--MC-277 separate representation, conditioning, normalization and aggregation. A negative witness collapses one row to a homogeneous shell, all negative witnesses can be aggregated at only one extra Walsh degree, and the normalized Christoffel scalar still retains the exact blind bit with rowwise margin `delta_(k,m)~2m/k`. The catastrophic one-exception loss appears when normalization or aggregation discards row provenance, not because the low-depth row representation has already forgotten blindness.

MC-278 shows that replacing polynomial normalization by a rational decoder changes the algebraic complexity but not the source-information bill. The exact endpoint function

`F_q(x)=(1+b(x))^(-q)`

recovers the blind-row count by rounding once `C 2^(-q)<1/2`, so rational degree only `q=Theta(log C)` is enough. But its unique Walsh expansion has nonnegative radial coefficients whose degree distribution satisfies `E J=(k/2)(1-2^(-q))` and, at the atom-sensitive scale, concentrates around `k/2`. For every source cutoff `m=o(k)`, the coefficient mass below degree `m` is `o(1)`.

Thus denominator inversion does not make the endpoint cheap in the canonical arithmetic source hierarchy. It converts a low-degree statistic `b(x)` into a function whose Walsh/Krawtchouk realization imports essentially half-cube source depth. At the live support-matched depth `m=Theta(log log y)`, almost all positive coefficient mass of this rational decoder lies outside the available hierarchy.

The reusable distinction is stronger than polynomial versus rational degree. **Algebraic description complexity and source-support depth are different currencies.** A nonlinear inverse can be concise before expansion while still depending on macroscopic source depth after translation into the characters actually supplied by the arithmetic problem.

This leaves one precise escape open: control a natural arithmetic resolvent, inverse operator or rational aggregate directly, without expanding the denominator into source subsets. Such a mechanism would have to be native to the localized Legendre-shell structure; MC-278 does not rule it out.

**Boundary.** MC-278 analyzes one explicit rational decoder and does not prove an optimal rational lower bound. High positive Walsh coefficient mass is decisive at the blind vector, where all characters equal `+1`; it is not a claim that every nonblind row receives a large numerical contribution. The original signed cross-row residual and direct arithmetic inversion routes remain open.