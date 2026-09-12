# MI-005 — Stable tails are cumulative imbalance between q-adic continuation and prediction-refinement charges

**Evidence level:** supported by NB-063--NB-078. The finite-dimensional continuation, prediction, branching, and q-adic refinement identities are exact; no arithmetic estimate proving summable imbalance control or closing the stable-tail criterion is established.

NB-066--NB-073 reduce a hypothetical persistent Nyman target to a global continuation problem. NB-074 introduces the nonstationary charge `J_(R,N)`: bounded charge along an unbounded sequence rules out a stable tail, while any nonzero stable tail forces divergence for every finite horizon schedule. NB-075--NB-076 resolve it as

`J_(R,N)=L_R-C_(R,N)`,

where `L_R` is raw continuation volume and `C` is a nonnegative cross-cut area built from future-conditioned partial-correlation charges.

NB-077 shows that exact integer branching preserves both currencies monotonically. A coarse cross-cut information charge survives in the fine descendants, and `L_R<=L_(qR)`. This removes signed Gram cancellation as an explanation for losing predictive information, but separate monotonicities do not compare their growth.

NB-078 resolves that missing comparison coordinate. In each `q`-descendant block, the normalized average is exactly the shifted coarse innovation and the orthogonal complement is a canonical branch-contrast space. The cross-cut refinement gain is the sum of three nonnegative conditional mutual informations involving past/future contrasts. The raw continuation refinement gain has a parallel decomposition into nonnegative edge and contrast charges.

Along a `q`-adic ray let

`ell_m=L_(R_m)-L_(R_(m-1)) >=0`

and

`c_m=C_(R_m,N_m)-C_(R_(m-1),N_(m-1)) >=0`.

Then the remaining continuation charge telescopes exactly:

`J_m=J_0+sum_(r<=m)(ell_r-c_r)`.

A stable tail must therefore create an unbounded cumulative excess of **new continuation information over new prediction information** on every such ray. Conversely, one ray satisfying `ell_m<=c_m+e_m` with `sum e_m<infinity` kills the stable tail. The final theorem can be attacked increment by increment rather than by comparing two large determinants at the endpoint.

The remaining issue is source control of those increments. NB-078 does not prove that branch-contrast prediction stays near the cut, and contrast correlations may live on rectangles whose additive width grows with scale. Mesoscopic localization is still a plausible mechanism for proving `c_m` large enough, but the exact target is now broader: any arithmetic theorem that prevents persistent positive cumulative refinement imbalance suffices.

**Boundary.** The Gaussian language is only an exact log-determinant representation of deterministic Gram matrices. NB-078 does not prove finite-band localization, `ell_m<=c_m`, or a stable-tail contradiction. Its durable contribution is the common nonnegative multiresolution ledger and the summable-error criterion.