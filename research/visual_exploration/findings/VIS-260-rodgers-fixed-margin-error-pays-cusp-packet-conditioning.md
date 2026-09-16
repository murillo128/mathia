# VIS-260 — Rodgers' fixed-margin pair-correlation error can pay cusp-packet conditioning only above an explicit bandwidth rate

## Claim

Assume RH and use Brad Rodgers' smooth pair-correlation theorem in the notation of his Theorem 1.4. Fix `epsilon>0` and a fixed weight `omega` whose Fourier transform is smooth and compactly supported. Let `P_T(alpha)` denote the normalized zeta pair statistic on the left-hand side of that theorem and `BK_T(alpha)` its Bogomolny--Keating prediction on the right-hand side. Then for every fixed

`0 < delta < epsilon/2`

Rodgers proves, uniformly for

`|alpha| < 1-epsilon`,

that

`P_T(alpha)-BK_T(alpha)=O_delta(T^(-delta))`.

Consequently, for any finite real signed measure `nu_b` supported on `[-b,b]` with

`b < 1-epsilon`,

linearity plus the uniform estimate gives the exact transfer rule

`| integral [P_T(alpha)-BK_T(alpha)] dnu_b(alpha) |`
` <= C_(epsilon,omega,delta) T^(-delta) ||nu_b||_TV`.

Now impose the cusp-adapted cancellations of `VIS-259`: zero mass, zero `|alpha|` pairing, and vanishing even moments through order `2m-2`, and normalize the first retained moment by

`|m_(2m)(nu_b)|=1`.

`VIS-259` proves that the minimum possible total variation over all such packets is exactly

`E_m^(-1) b^(-2m)`,

where

`E_m = dist_infinity(alpha^(2m), span{1,alpha,alpha^2,alpha^4,...,alpha^(2m-2)})`

after scaling the support to `[0,1]`. Choosing an extremal packet therefore yields the rigorous Rodgers-transfer bound

`| integral [P_T-BK_T] dnu_b |`
` <= C_(epsilon,omega,delta) E_m^(-1) T^(-delta) b^(-2m)`.

Hence Rodgers' stated fixed-margin theorem certifies that this normalized packet error tends to zero whenever

`T^(-delta) b^(-2m) -> 0`.

For a power-law bandwidth

`b=T^(-beta)`,

such a `delta<epsilon/2` exists exactly when

`beta < epsilon/(4m)`.

In particular, the sharp quadratic packet from `VIS-257` can be certified by this theorem for any `beta<epsilon/4`, while the sharp quartic packet from `VIS-258` can be certified for any `beta<epsilon/8`, provided the other hypotheses remain fixed.

This is a **fixed-support-margin result only**. Rodgers' theorem fixes `epsilon` and `omega` before `T->infinity`. It does not give a uniform conclusion for a family with edge margin `epsilon_T->0`, nor for an `omega_T` whose seminorms or Fourier support vary with `T`. It also remains a two-level pair-correlation theorem, so it does not supply the four-level cross-window covariance required by the original edge--edge statistic in the accepted Montgomery support-edge clue.

**Evidence/status:** `LITERATURE+DERIVED + QUANTITATIVE TRANSFER GATE + NEGATIVE BOUNDARY + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, Bogomolny--Keating formula, source-specific quadratic/quartic coefficient, four-level estimate, or RH implication is claimed.

## 1. Rodgers supplies a genuinely uniform fixed-margin scalar error

Rodgers' Theorem 1.4 states, under RH, that for fixed `epsilon>0` and fixed `omega` with smooth compactly supported Fourier transform,

`P_T(alpha) = BK_T(alpha) + O_delta(T^(-delta))`

for every `delta<epsilon/2`, uniformly on `|alpha|<1-epsilon`.

The prediction contains the explicit Bogomolny--Keating arithmetic kernel `Q_t(u)`, built from `(zeta'/zeta)'`, the prime sum `B`, and the Euler product `A`, rather than merely the sine-kernel/GUE term. Rodgers further notes that this prediction differs from the naive GUE prediction by more than his error term in the regime he resolves. Thus this is not merely a qualitative Montgomery-support statement: inside a fixed margin it gives a polynomially decaying uniform error for an arithmetic pair-correlation prediction.

For the present purpose, only the uniformity in `alpha` is needed. If `nu_b` is supported inside the same fixed permitted interval, then

`| integral (P_T-BK_T) dnu_b |`
` <= sup_(|alpha|<=b)|P_T(alpha)-BK_T(alpha)| ||nu_b||_TV`,

which gives the displayed `T^(-delta)||nu_b||_TV` bound without any assumption about the sign or atomic form of the packet.

## 2. VIS-259 converts the theorem error into an exact packet-conditioning rate

The subtlety exposed by `VIS-257`--`VIS-259` is that cancelling the universal low-frequency nuisance is not free. After mass and cusp cancellation, a unit quadratic carrier costs `8b^(-2)` total variation. If the quadratic channel is also cancelled, a unit quartic carrier costs `E_2^(-1)b^(-4)`. `VIS-259` proves the general exact cost `E_m^(-1)b^(-2m)`.

Because Rodgers' error is uniform pointwise in the frequency variable, total variation is exactly the norm that propagates that error through a signed packet. Substituting the sharp packet cost gives

`error <= C E_m^(-1) T^(-delta)b^(-2m)`.

This does not assert that the actual error saturates the bound; cancellation inside the unknown theorem remainder could make it smaller. It states what Rodgers' published uniform estimate alone is sufficient to certify after the packet normalization has been paid.

For `b=T^(-beta)`, the exponent of `T` in the bound is

`-delta + 2m beta`.

A decaying certified error therefore requires `2m beta<delta`. Since Rodgers allows any fixed `delta<epsilon/2`, such a choice is possible precisely when `beta<epsilon/(4m)`. The quadratic and quartic thresholds follow by taking `m=1` and `m=2`.

## 3. The fixed-margin hypothesis is the load-bearing boundary

The rate above can look generous if `epsilon` is treated as an arbitrary constant, but the current support-edge program cannot silently do that. `VIS-141` shows that when one tensor factor approaches the Montgomery edge, with support radius `1-epsilon_L`, a support-safe independent companion is forced into a shrinking band `b_L<epsilon_L`.

Rodgers' theorem does not state an estimate uniform as `epsilon->0`. Its admissible exponent is itself restricted by

`delta < epsilon/2`,

and the implied constant is part of a theorem with fixed `epsilon`. Therefore substituting `epsilon=epsilon_L` after the fact does not provide a valid edge-closing asymptotic theorem. In particular, one may not infer a bound such as

`T^(-epsilon_L/2+o(1))`

with controlled constants for an arbitrary sequence `epsilon_L->0` from Theorem 1.4 as stated.

This matters independently of packet conditioning. Even before the factor `b_L^(-2m)` is paid, the published theorem does not supply the uniform moving-support-margin estimate needed by the edge-approaching branch.

The same warning applies to the physical weight. Rodgers fixes `omega`; the bounded-tent constructions in the visual support-edge thread use an `L`-dependent source geometry. A transfer from Rodgers' fixed smooth weight to that exact family needs its own uniform comparison rather than treating a fixed-test theorem as automatically stable under changing windows.

## 4. What this resolves and what remains source-side

The result gives a concrete positive statement about one part of the accepted support-edge clue: **inside a genuinely fixed support margin and for a fixed smooth weight, a rigorous arithmetic pair-correlation theorem has enough polynomial accuracy to survive optimally conditioned quadratic or quartic cusp packets, provided the companion bandwidth shrinks slowly enough.** The packet normalization by itself is therefore not an absolute obstruction in that fixed-margin regime.

It does not identify the desired arithmetic carrier. Rodgers' `Q_t(u)` makes the lower-order arithmetic correction explicit, but showing that the exact zeta-minus-null observable used by the visual branch has a nonzero quadratic coefficient, quartic coefficient, or other first surviving carrier after its declared cancellations is a separate derivation. `VIS-259` already shows that without such a coefficient there is no reason to climb the cancellation ladder.

Nor does this result solve the original covariance problem. Rodgers controls a two-level pair statistic. `VIS-139` shows that covariance of disjoint quadratic pair statistics is a four-level functional, and `VIS-140`--`VIS-141` show why the familiar restricted-support theorem does not automatically reach the edge--edge configuration. A two-level source calibration cannot substitute for that missing four-level dependence law.

The useful next source-side question is therefore narrower: for one predeclared fixed-margin smooth pair statistic, compute the first nonzero Taylor coefficient of the explicit Bogomolny--Keating-minus-matched-null prediction after the same cusp-adapted cancellation, and compare its size with the `T^(-delta)b^(-2m)` transfer gate above. Only after that coefficient is established should one ask whether an `L`-dependent window or an edge-closing support family preserves it.

## 5. Prior-art and novelty boundary

The external theorem is:

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, arXiv `1203.3275`. The relevant inputs are Theorem 1.4, its uniform range `|alpha|<1-epsilon`, the admissible error exponent `delta<epsilon/2`, and the subsequent remark on integrating the frequency variable.

Rodgers explicitly presents the result as a rigorous smooth-test realization of the Bogomolny--Keating lower-order pair-correlation prediction under RH and distinguishes it from the naive GUE approximation. No novelty is claimed here for that theorem, for Bogomolny--Keating arithmetic corrections, or for restricted-support pair correlation.

The Mathia-specific derived content is only the composition with the exact packet-conditioning theorem `VIS-259`: the published fixed-margin error `T^(-delta)` becomes `T^(-delta)b^(-2m)` after the optimally normalized cusp-adapted packet, producing the explicit power-law admissibility condition `beta<epsilon/(4m)` and exposing why the same argument cannot simply be pushed to a moving edge margin.

## Research consequence

For the accepted Montgomery support-edge residual clue, Rodgers' theorem can now be used as a **fixed-margin calibration theorem**, not as a generic edge-limit escape. If a quadratic or quartic source coefficient is derived for a fixed smooth pair statistic, the theorem error can be propagated through the exact `VIS-257`/`VIS-258` packet cost using the rate above.

Do not use Theorem 1.4 to justify an edge factor with `epsilon_L->0`, an `L`-dependent source window, or the missing four-level covariance without a new uniform theorem. Those are separate load-bearing steps.

No untouched confirmation-zero data are used.