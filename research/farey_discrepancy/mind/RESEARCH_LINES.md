# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate the signed exact-omission density threshold from the nonnegative source boundary

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`, `MI-049-parity-dilation-moves-the-exact-omission-frontier-from-support-to-paired-coefficients`, `MI-050-companion-incidence-not-full-support-incidence-controls-isolated-paired-omissions`, `MI-051-congruence-restricted-companion-chains-lower-the-ordered-factorization-conditioning-exponent`, `MI-052-restricted-inverse-conditioning-counts-only-after-global-extension`, `MI-053-top-half-antichains-make-linear-density-the-sharp-signed-omission-threshold`, `MI-054-bounded-switched-response-forces-power-law-depletion-of-positive-capacity`, `MI-055-first-row-mertens-forcing-caps-polynomial-reservoir-depth`.

FD-241--FD-255 separate qualitative density-one sampling, paired exact-omission reachability, restricted incidence conditioning and the full global Möbius extension constraint. FD-255 gives the decisive signed global result: under `|b_n|<=C_b n`, every exact-omission family with `K=o(H)` has `o(H^2)` total coefficient mass.

FD-256 proves that this sublinear hypothesis is sharp in order. A top-half antichain construction hides more than `KH` signed coefficient mass while the response vanishes outside the omitted locations, and `K=Theta(H)` can asymptotically hide the full top-band envelope. The remaining signed question is only the slowly varying gap between the constructive `KH` scale and the upper bound `KH log(e+log(H/K))`; closing it cannot reopen the settled macroscopic density threshold.

The physical source boundary is stricter because FD-256 is intrinsically signed. FD-257 shows that nonnegative coefficients with bounded switched response have power-depleted dyadic capacity. FD-260 materially strengthens the same mechanism: exact Mertens maxima through `2^19`, followed only by the trivial tail bound, make the positive Volterra kernel contract at `r=2/3`. Thus for divisor scale `x`,

`relative dyadic capacity = O((C+B)x^(-log_2(3/2)))`,

with exponent `0.58496...>1/2`, without any sign assumption on `mu*b`. The old `0.0614...` exponent was not the structural frontier of the method.

FD-259 remains strictly stronger under an extra sign condition. If `g=mu*b>=0`, equivalently the divisor response is monotone, neighboring switched stencils give

`sum_(n<=x)b_n = O((C+B)x)`

and relative capacity `O((C+B)/x)`, sharp in that cone. Positivity of the coefficients and positivity of the response increments are therefore distinct resources.

The live subpolynomial-depth source question is now concrete: obtain a lower bound on the positive slack consumed by the actual Mertens repair and compare it with the FD-260 ceiling in the genuinely signed-increment regime, or with the sharper FD-259 ceiling if monotonicity can be proved. Further improvements of the FD-257/260 kernel exponent are secondary unless they cross the source-specific lower bound.

FD-258 adds an independent polynomial-depth ceiling. The first switched row forces `liminf log D_N/log N <= 1-Theta <= 1/2` for all-large-`N` realizations with subpolynomial first-row tolerance. This does not touch the present `D=N^{o(1)}` regime, but it says that later-row conditioning or extra positive capacity cannot extend the same reservoir architecture uniformly beyond the zero-frontier depth without changing which source variables affect the first samples.

## Separate support conditioning, global extension, source positivity and arithmetic-kernel strength

The exact hierarchy now has an additional quantitative layer. Restricted incidence may be badly conditioned; global Möbius extension removes every sublinear macroscopic signed extremizer; coefficient positivity plus bounded switched response forces more-than-square-root depletion after inserting only finite exact Mertens data; and response monotonicity strengthens that to inverse-linear depletion. FD-258 supplies a separate first-row ceiling at polynomial depth.

Future arguments must state which sign information is available for `b` and `mu*b`, how much exact arithmetic information enters the positive recurrence, and what lower bound the concrete source repair actually requires. Improving an abstract capacity ceiling without connecting it to source demand is not by itself progress toward the final obstruction.
