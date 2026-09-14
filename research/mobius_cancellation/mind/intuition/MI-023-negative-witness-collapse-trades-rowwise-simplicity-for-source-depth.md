# MI-023 — Blindness survives rowwise; positive endpoint decoding forces macroscopic source depth

**Evidence level:** proved for the current flat Christoffel source through [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md)--[MC-279](../../findings/MC-279-positive-definite-endpoint-decoder-half-depth-barrier.md). No signed arithmetic cancellation theorem or blind-support exclusion is claimed.

MC-273--MC-277 separate representation, conditioning, normalization and aggregation. A negative witness collapses one row to a homogeneous shell, all negative witnesses can be aggregated at only one extra Walsh degree, and the normalized Christoffel scalar still retains the exact blind bit with rowwise margin `delta_(k,m)~2m/k`. The catastrophic one-exception loss appears when normalization or aggregation discards row provenance, not because the low-depth row representation has already forgotten blindness.

MC-278 first showed that replacing polynomial normalization by one rational decoder changes algebraic complexity but not the source-information bill. Its endpoint function has low rational degree, yet its nonnegative Walsh mass concentrates near degree `k/2`; at every source cutoff `m=o(k)`, the low-degree mass is `o(1)`.

MC-279 turns that example into a representation boundary. If a Boolean endpoint decoder has nonnegative Fourier/Walsh coefficients, equals one at the blind vector and is uniformly small away from it, then for every fixed `delta>0` the total coefficient mass below degree `(1/2-delta)k` tends to zero. Radiality, the Gamma form and the specific resolvent of MC-278 are irrelevant. Positive definiteness plus pointlike endpoint localization itself forces essentially half-cube source depth.

The reusable distinction is now sharper than polynomial versus rational degree. **Algebraic description complexity, positivity and source-support depth are different currencies.** A concise positive scalar inverse can still require macroscopic character depth when translated into the source basis actually supplied by the arithmetic problem.

This closes the generic positive-definite scalar-decoder escape. A viable alternative must use signed Fourier mass, exploit restrictions of the actual localized Legendre image that are absent on the full Boolean cube, or act as a genuinely source-native operator/resolvent before reduction to a positive point-selector.

**Boundary.** MC-279 is a lower bound for positive-definite endpoint decoders on the Boolean cube; it is not a lower bound for arbitrary signed decoders or for operators whose action cannot be represented by such a scalar function. The original signed cross-row residual and arithmetic source restriction remain open.