# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate the signed exact-omission density threshold from the nonnegative source boundary

**Linked intuitions:** `MI-041-sublinear-point-sampling-cannot-make-divisor-response-signed-coercive`, `MI-042-subfull-point-sampling-density-cannot-make-divisor-response-signed-coercive`, `MI-043-approximate-density-one-sampling-has-a-defect-plus-residual-coercivity-ledger`, `MI-044-finite-exact-omissions-are-triangular-response-columns-not-arbitrary-sparse-increments`, `MI-045-exact-omission-cost-is-a-harmonic-location-profile`, `MI-046-cross-scale-divisibility-not-low-location-drives-exact-omission-amplification`, `MI-047-alternating-rank-merges-create-factorial-incidence-conditioning-without-reaching-the-macroscopic-scale`, `MI-048-ordered-factorization-entropy-caps-exact-omission-conditioning`, `MI-049-parity-dilation-moves-the-exact-omission-frontier-from-support-to-paired-coefficients`, `MI-050-companion-incidence-not-full-support-incidence-controls-isolated-paired-omissions`, `MI-051-congruence-restricted-companion-chains-lower-the-ordered-factorization-conditioning-exponent`, `MI-052-restricted-inverse-conditioning-counts-only-after-global-extension`, `MI-053-top-half-antichains-make-linear-density-the-sharp-signed-omission-threshold`, `MI-054-bounded-switched-response-forces-power-law-depletion-of-positive-capacity`, `MI-055-first-row-mertens-forcing-caps-polynomial-reservoir-depth`, `MI-056-deep-band-positivity-beats-first-row-only-after-a-source-demand-exponent-threshold`.

FD-241--FD-255 separate qualitative density-one sampling, paired exact-omission reachability, restricted incidence conditioning and the full global Möbius extension constraint. FD-255 gives the decisive signed global result: under `|b_n|<=C_b n`, every exact-omission family with `K=o(H)` has `o(H^2)` total coefficient mass.

FD-256 proves that this sublinear hypothesis is sharp in order. A top-half antichain construction hides more than `KH` signed coefficient mass while the response vanishes outside the omitted locations, and `K=Theta(H)` can asymptotically hide the full top-band envelope. The remaining signed question is only the slowly varying gap between the constructive `KH` scale and the upper bound `KH log(e+log(H/K))`; closing it cannot reopen the settled macroscopic density threshold.

The physical source boundary is stricter because FD-256 is intrinsically signed. FD-257 shows that nonnegative coefficients with bounded switched response have power-depleted dyadic capacity. FD-260 materially strengthens the same mechanism: exact Mertens maxima through `2^19`, followed only by the trivial tail bound, make the positive Volterra kernel contract at `r=2/3`. Thus for divisor scale `x`,

`relative dyadic capacity = O((C+B)x^(-log_2(3/2)))`,

with exponent `beta=0.58496...>1/2`, without any sign assumption on `mu*b`. The old `0.0614...` exponent was not the structural frontier of the method.

FD-259 remains strictly stronger under an extra sign condition. If `g=mu*b>=0`, equivalently the divisor response is monotone, neighboring switched stencils give

`sum_(n<=x)b_n = O((C+B)x)`

and relative capacity `O((C+B)/x)`, sharp in that cone. Positivity of the coefficients and positivity of the response increments are therefore distinct resources.

FD-261 calibrates the missing source lower bound against both capacity laws and the independent first-row ceiling. If a deep-band repair demand has size `N^(theta-o(1))D^(alpha-o(1))` at polynomial depth `D=N^(lambda+o(1))`, the general FD-260 ceiling can contradict it only when `theta+alpha lambda>1+(1-beta)lambda`. A demand merely linear in depth (`alpha=1`) becomes contradictory only after the first-row scale already excluded by FD-258. To make general deep-band depletion decisive no later than that same-amplitude first-row boundary requires `alpha>2-beta=1.415037...`. Under the stronger monotone-response condition of FD-259, by contrast, linear depth accumulation is already exponent-critical.

FD-262 now rules out the canonical FD-225 full-grid divisor inverse as the source of that missing superlinear exponent. Its exact identity

`2 c_d = sum_(q|d)(Delta R_N(q)-B_q(N))`

implies that, after the maximum block-Mertens forcing and full-grid residual increments are factored out, a dyadic band contains only `O(D log D)` total repair mass. For the rounded full-grid flattening the residual increment is bounded, so the depth exponent is at most `1+o(1)`. Repeated divisor inversion therefore cannot generate the `D^(2-beta)` threshold demanded by FD-261. A larger forcing amplitude in deep blocks can change the arithmetic amplitude exponent, but not this depth-amplification ceiling.

The live source question has consequently narrowed. In the general signed-increment positive cone, a successful repair must either derive genuinely stronger arithmetic forcing at deeper multiples, leave full-grid flattening and exploit switched-only freedom whose uncontrolled intermediate residual increments create a different source demand, or prove source structure strong enough to move the physical repair into a sharper cone such as `mu*b>=0`. Small improvements of the FD-260 kernel exponent remain secondary unless a concrete source theorem crosses the resulting phase boundary.

FD-258 remains an independent polynomial-depth ceiling. The first switched row forces `liminf log D_N/log N <= 1-Theta <= 1/2` for all-large-`N` realizations with subpolynomial first-row tolerance. This does not touch the present `D=N^{o(1)}` regime, and FD-261--FD-262 show why a canonical linear-depth full-grid demand cannot improve it in the general positive cone.

## Separate support conditioning, global extension, source positivity, inverse depth amplification and arithmetic-kernel strength

The exact hierarchy now has an additional quantitative layer. Restricted incidence may be badly conditioned; global Möbius extension removes every sublinear macroscopic signed extremizer; coefficient positivity plus bounded switched response forces more-than-square-root depletion after inserting only finite exact Mertens data; response monotonicity strengthens that to inverse-linear depletion; the source-demand exponent decides whether any of those ceilings can beat the separate first-row obstruction; and FD-262 shows that the canonical full-grid inverse itself supplies only linear-log depth mass after its forcing amplitude is removed.

Future arguments must state which sign information is available for `b` and `mu*b`, how much exact arithmetic information enters the positive recurrence, whether the repair is constrained on the full integer-multiple grid or only the switched rows, the size of the intermediate residual increments, and the actual depth exponent of the concrete source repair. A lower bound that does not cross the applicable capacity/first-row phase boundary is informative about the source but is not yet a stronger obstruction.
