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

FD-282 then tests the natural repair of moving the physical transform inside the Perron contour before taking absolute values. On the critical line the grouped kernel does gain frequency decay, but the right horizontal collar near `Re(s)=1` has a genuine self-divisor plateau: for `2<=T<=x/4`, the grouped physical kernel has `l^1` size at least `x/log x` from prime coordinates `p in (x,2x]`. The resulting absolute collar costs `Nx` up to logarithms and is power-inadequate whenever `lambda<(1-theta)/(1-beta)`; at `theta=1/2` this includes every `lambda<=1`. Grouping before absolute values is therefore necessary but not sufficient.

FD-283 narrows the sign-preserving escape on every strict right subcollar `a<=Re(s)<=c` with `a>1`. After exact physical grouping and the absolutely convergent expansion `1/zeta(s)=sum mu(n)n^(-s)`, integrating in `sigma` multiplies each coefficient mode by the strictly positive Mellin weight

`W_(a,c)(r)=int_a^c r^sigma dsigma`.

The phase `exp(iT log(Nu/n))` is independent of `sigma`, and pairing the conjugate upper/lower edges merely extracts its sine quadrature. Thus neither `sigma`-integration nor edge pairing supplies an independent `1/T` mechanism on the strict-right collar.

FD-284 then proves, under RH, that the signed field itself does not collapse at low polynomial heights. On a fixed thin outer strip and uniformly for `x^epsilon<=T<=x^(1/2-epsilon)`, prime self-divisor coordinates retain band norm `Nx^(1-o(1))` after the complete reciprocal-zeta sum, `sigma` integration and upper/lower pairing. FD-285 strengthens the geometry: the reciprocal-zeta phase rotates by at most `log(1/eta)+o(1)` between `1+eta/L` and `1+1/L`, so whenever `eta>e^(-pi/2)` that entire strip stays in one open phase half-plane. Consequently every fixed outer fraction below `1-e^(-pi/2)=0.792120...` of the standard strict-right collar still carries the same `Nx^(1-o(1))` signed prime witness throughout the square-root-height window.

This does not lower-bound the complete horizontal contour. The remaining inner right slice near `Re(s)=1`, the horizontal portion at or left of `1`, or another contour piece may still cancel the protected outer contribution coordinatewise. But the live hard-Perron mechanism is now much narrower: it must produce **cross-collar cancellation against a sign-protected outer strip**, or change the boundary law through smoothing/modified Perron architecture. At the repair scale, the witness is already power-larger than `N^theta x^(2-beta)` whenever `lambda<(1-theta)/(1-beta)`; for `theta=1/2`, every first-row depth `lambda<=1` lies inside that range. If the remaining cancellation problem loses the physical divisor-replication geometry and reduces to a generic Möbius Mellin theorem, it belongs naturally to `mobius_cancellation`; any Farey-specific gain must retain the grouped physical kernel or the cross-collar geometry.