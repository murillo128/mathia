# Farey-discrepancy research lines

This file records the current mathematical questions that survive the Farey-discrepancy evidence. It is not a roadmap, task queue, status page, or history.

## Force one-sided repair variation past the positive-capacity boundary

FD-255--FD-264 separate the signed exact-omission threshold from the physical nonnegative-source boundary. The general positive switched-response cone has relative dyadic capacity exponent `beta=log_2(3/2)`, while response monotonicity strengthens this to inverse-linear depletion. The independent first-row obstruction remains at polynomial depth `lambda<=1-Theta`. For a same-amplitude deep repair to beat that ceiling in the general positive cone, the source must force depth amplification beyond `D^(2-beta)`.

Canonical full-grid inversion does not supply that amplifier. FD-262 bounds its total repair mass by `O(D log D)` after the explicit forcing terms are removed. FD-263 shows that deep forcing coordinates are copied only once into a dyadic coefficient band, so the absolute/one-sided ledger crosses the positive-capacity threshold only when its amplitude-density exponent is large enough. FD-264 then shows that signed band aggregation telescopes this population resource into a probability average of Mertens prefixes and gives zero interior weight to the deepest shell.

The live deterministic source question is therefore a theorem on **one-sided or `l^1` within-band repair variation** under the exact replication kernel, or a genuinely different switched-only repair whose intermediate motion changes the source demand. A negative signed mean or a dense population of deep blocks is not enough by itself.

## Decide whether cluster-complete spectral repair can control its complementary remainder

FD-268--FD-273 separate absolute spectral mass from usable source-phase coherence. The finite critical packet has enough absolute `l^1` budget under the natural negative-moment calibration, but its phase-sensitive replicated field is sparse at threshold on integer horizons. Under RH, FD-273 localizes any nonexceptional threshold-sized finite-packet contribution to the close-gap complement of the well-spaced zeros.

FD-274--FD-276 then remove internal close-gap singularity as a free resource. A complete simple-zero cluster recombines into a divided difference, fixed derivative order costs only linear depth-band variation up to logarithms, and a reciprocal-log component of size `m` with collar background `B_C` obeys the exponent ledger

`(m-1) log(2 log(2Nx)) + log B_C >= (1-beta-o(1)) log x`

if it is individually threshold-sized. Thus subpolynomial background requires `m` on the order of `log x/log log x`; internal inverse gaps and zero height do not independently amplify the grouped packet.

FD-277 prices that single-component large-cardinality branch by spectral height. At depth `x=N^(lambda+o(1))`, if the background exponent is `delta<1-beta` and `q=1-beta-delta`, RH forces

`log Gamma/log x >= 2q/(1+2q/(pi(1+1/lambda)))-o(1)`.

For subpolynomial background this gives a uniform exponent floor `0.656590...`, and `0.733210...` at balanced depth.

FD-278 closes the aggregate complete-component loophole at exponent level. For `R=x^(r+o(1))` complete components, maximal reciprocal-log cardinality `(kappa+o(1))log x/log log x`, and maximal background `x^(b+o(1))`, even perfect inter-component coherence can reach threshold only if

`r+kappa+b >= c`, where `c=1-log_2(3/2)`.

If all components lie below `T=x^(tau+o(1))`, RH gives `r<=tau` and `kappa<=tau/[2(1-tau/(pi(1+1/lambda)))]`. Tame aggregate background therefore forces `T>=x^(tau_*(lambda)-o(1))`; uniformly in fixed polynomial depth `tau_*>=0.2683381468...`, with `tau_*(1)=0.2725714441...`. At subpolynomial height the background must pay essentially the full exponent `c`.

FD-279 removes the one component cut by a hard upper spectral boundary as a separate power-scale escape in the same low-height regime. A reciprocal-log component crossing `T=x^(tau+o(1))`, `tau<pi(1+1/lambda)`, has diameter `O(1/log log x)` under RH and simple zeros. Moving an analyst-controlled cutoff just beyond it restores complete-cluster divided-difference cancellation without changing the spectral exponent.

FD-280 shows why that geometric completion cannot be justified by continuity of the complementary hard-truncation remainder. For an exact decomposition `A=C+P_T+E_T`, moving the cutoff from `T_0` to `T_1` gives the identity

`E_(T_1)-E_(T_0)=-(P_(T_1)-P_(T_0))`.

After the consecutive-difference/divisor replication used by the physical destination, the same equal-and-opposite identity persists, including equality of the corresponding `l^1` jump norms. A spectrally tiny cutoff displacement may therefore complete an ill-conditioned close-zero packet while forcing an equally large remainder jump. The packet becomes better conditioned because the decomposition has been repartitioned, not because the total source object has become locally continuous in the cutoff.

FD-281 prices the most direct classical remainder certificate and finds that it becomes harmless too late. Pointwise truncated-Perron error followed by the physical difference/replication map has total size `O(N x^2 log(2Nx)/T+x log(2x))`; at polynomial depth `x=N^(lambda+o(1))`, beating the repair target `N^theta x^(2-beta)` requires Perron-height exponent `beta+(1-theta)/lambda`, already beyond the low-height cluster-pruning regime. This is an ordering obstruction for that certificate, not a lower bound for the exact remainder.

FD-282 then tests the natural repair of moving the physical transform inside the Perron contour before taking absolute values. On the critical line the grouped kernel does gain frequency decay, but the right horizontal collar near `Re(s)=1` has a genuine self-divisor plateau: for `2<=T<=x/4`, the grouped physical kernel has `l^1` size at least `x/log x` from prime coordinates `p in (x,2x]`. The resulting absolute collar costs `Nx` up to logarithms and is power-inadequate whenever `lambda<(1-theta)/(1-beta)`; at `theta=1/2` this includes every `lambda<=1`. Grouping before absolute values is therefore necessary but not sufficient: the remaining low-height route must preserve cancellation along the horizontal contour or between contour pieces rather than majorize the collar pointwise.

The spectral frontier is consequently **cluster-complete, repair-aware and sign-preserving**. Tiny cutoff motion cannot control the remainder; pointwise Perron majorization is quantitatively too late; and even an already-grouped physical kernel retains a depth plateau if the horizontal edge is then made absolute. A viable continuation must estimate the signed grouped horizontal contribution before the destructive absolute-value interface, use a smoothing/modified Perron architecture that genuinely changes the collar frequency law, or supply a stronger destination-norm remainder estimate while the FD-278 population remains prunable. FD-282 does not rule out cancellation in `sigma`, cancellation between upper and lower edges, smoothing, or heights beyond divisor depth; those possibilities must be priced in the exact physical repair norm rather than inferred from the failure of the absolute certificate.