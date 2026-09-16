# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with genuinely structured joint information

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-044-the-quartic-floor-is-shared-by-incidence-and-fixed-modulus-bias-energy`.

MC-307--MC-321 reduce the reciprocal endpoint to a source-character family on the exact dyadic prime shell and show that generic coding capacity, smooth-modulus zero-free information and ordinary interval cancellation do not address the required population. MC-321 closes the controlled-common-modulus endpoint by a prime Halász--Montgomery obstruction.

MC-322--MC-324 then turn shell-bias energy, varying-modulus conductor costs and weighted source incidence into the quartic common-radical floor `liminf log P/log y >= 4`. MC-325 shows sparse even layers reproduce the same half-loading limit. MC-326 makes the proof-architecture ceiling universal: every nonempty nonnegative mode weighting has an abstract source column with loading at least `2^(R-1)/(2^R-1)>1/2`.

MC-327 constrains the actual source rather than only the abstract worst case. If `B_R` is the logarithmically weighted squared deviation of source-column occupancy from `R/2`, then

`liminf (1-B_R) log P/log y >= 4`.

Therefore any package saturating the quartic floor has `B_R->0`: essentially all logarithmic source mass is forced onto near-half-loaded columns.

MC-328 closes the next natural escape. If a nonnegative mode weighting is a polynomial of degree `d_R<R/2` in the exact endpoint coefficient `x(a)=(-1)^|a|(1-2|a|/R)`, its Walsh spectrum lives only within Hamming distance `d_R` of the two ends of the cube. Every source column in the complementary middle band then has exact loading `1/2+w_0/(2W)>=1/2`. Under quartic saturation, MC-327 puts `1-o(1)` of the actual logarithmic source mass in that band; hence every degree-`o(R)` endpoint-polynomial weighting remains asymptotically half-loaded. Fixed even moments can move almost all weight onto near-quadratic-conductor modes and still recover only the same exponent four.

MC-329 reaches the same quartic boundary through a genuinely different route. Schlage-Puchta's prime Halász--Montgomery input bounds the total character-bias energy for the complete fixed-common-modulus family throughout every range `q<=y^(4-delta)`. Applied to the reciprocal endpoint family, whose exact squared-bias demand is `2^R/R-1`, this gives a contradiction whenever the common modulus `q=4P` remains below `y^(4-delta)` and `R y^(-c_delta) log y ->0`. Thus `liminf log P/log y>=4` follows without the pair-incidence/half-loading argument.

The strengthened MC-329 exponent audit also rules out moving the Burgess/Halász--Montgomery order as a fixed-power escape. At order `k` the neutral threshold is `alpha<4k/(k+1)`; at `alpha=4` a positive `1/k^2` exponent remains, and no `alpha>4` is admissible for any `k`. Letting `k` grow can approach four from below but cannot cross to a fixed exponent beyond four, with the saving degenerating quadratically near the boundary.

MC-330 closes generic signed postprocessing after energy compression. Once the character family has been compressed to the `ell^2` bias-energy estimate, every signed linear statistic satisfies Cauchy--Schwarz and every quadratic kernel satisfies the operator-norm bound `|beta^*K beta|<=||K||_op ||beta||_2^2`; the reciprocal endpoint already saturates the normalized bound.

MC-331 moves the operation upstream and closes every **common** prime prefilter. Schlage-Puchta's theorem is uniform in one arbitrary prime-supported coefficient vector, while the exact endpoint transform has the unweighted shell asymptotically at its top operator norm. The coefficient norm therefore cancels between endpoint demand and analytic control. Translation-invariant/Walsh-diagonal filters on the character cube are included in this common-vector class.

MC-332 closes the opposite overcorrection. If every character mode receives an arbitrary coefficient row `w_(chi,r)`, rowwise Cauchy is sharp because the matched filter `w_(chi,r)=c_chi conjugate(chi(r))` cancels the character phase pointwise. At the reciprocal endpoint the character-evaluation matrix itself has rank only `R`, so even a rank-`R` restriction still contains an exact dephasing filter for all `2^R-1` nonprincipal modes. **Mode dependence and low rank are not resources by themselves; unrestricted joint freedom erases the oscillation the analytic theorem is supposed to exploit.**

The live linear route is therefore sharply constrained: define a **source-natural restricted joint prime--mode coefficient class** that is richer than one common vector but provably excludes or penalizes the conjugate-character evaluation geometry, and prove a family estimate sensitive to that extra joint structure rather than reducing again to rowwise or common-vector `ell^2`. Alternatives are a genuinely higher-order/nonlinear invariant, a prime-character theorem with different exponent geometry, or a different endpoint/source representation.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a recent probabilistic Möbius route fails before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting the asserted independence, and the auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired route must use a dependence law valid on a non-degenerate stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Treat observation category, conductor cost, source loading, Fourier degree, coefficient-class geometry and analytic family horizon as separate currencies

A theorem about many characters helps only when it controls the exact population and scale demanded by the endpoint. MC-326 makes universal source loading minimax-sharp; MC-327 adds equality-case rigidity for actual economical packages; MC-328 shows that low Fourier degree in the endpoint coefficient cannot resolve the resulting central source band. MC-329 adds an independent ceiling: even the full endpoint character family at one common modulus is controlled only up to the quartic fixed-power horizon by the present bias-energy input, and optimizing its Burgess order does not move that horizon beyond four. MC-330 adds a placement gate: arbitrary signed linear or quadratic processing of the already-compressed bias vector has no operator-normalized advantage over total energy. MC-331 shows one common upstream coefficient vector has the same problem. MC-332 shows the fully unrestricted joint matrix is too expressive because it contains the exact matched filter, even at rank `R`.

Future proposals must expose the analytic bill per mode, the logarithmic occupancy distribution of the source columns actually realized, the Walsh/Fourier complexity of any proposed weighting, the common-modulus range and exponent geometry of the character theorem being invoked, **the admissible geometry of any joint coefficient class and why it excludes phase matching**, where signed/joint structure is used relative to energy compression, and any arithmetic structure remaining inside the forced half-loaded band before interpreting family size, rank, mode dependence or order growth as leverage.