# VIS-270 — a fixed translated Wang-null packet can isolate the first prime-power quadratic carrier

## Claim

Let

`xi_2 = log(2)/(2*pi)`,

`xi_3 = log(3)/(2*pi)`.

Fix a short-interval exponent `theta` satisfying

`theta > xi_2`.

Then one can choose fixed parameters

`0 < eta < xi_2`, `b>0`, `lambda`

with

`b < min(eta, xi_2-eta, xi_3-xi_2)`,

`xi_2+b < lambda < theta`,

and construct a real even test `g in C_c^infinity((-lambda,lambda))` such that simultaneously

`g(0)=0`,

`int_R |q| g(q)dq=0`,

and the Rodgers quadratic prime-power channel from `VIS-264` is nonzero and supported on exactly the first prime frequency:

`C_2(g) = C_2^pp(g)`

` = -(log(2)^2/(16*pi^4)) g''(xi_2) != 0`.

In particular, the Wang leading functional

`g(0)+int_R |q|g(q)dq`

vanishes exactly, while the zero-frequency pole-compensation term in the Rodgers quadratic carrier also vanishes because it is proportional to `g(0)`. The surviving quadratic carrier is therefore purely nonconstant prime-power structure.

The construction can be made with fixed bandwidth and fixed seminorms, independent of `T`. Thus Wang's moving-test estimate from `VIS-266` applies with normalized leading-term error

`O_(g,lambda,theta)(1/log T + T^(lambda-theta) log T) = o(1)`.

This does **not** transfer the Rodgers lower-order coefficient into Wang's short-interval statistic: Wang's theorem still supplies only its leading Montgomery functional and an error whose `O(1/log T)` component is too large to identify an unspecified lower-order coefficient at that scale. The result instead closes a representation question left by `VIS-269`: diagonal and cusp cancellation do not themselves force prime-power blindness. The blindness was caused by shrinking the support below `xi_2`.

**Evidence/status:** `EXACT-DERIVED + COMPOSITION OF CANONICAL FINDINGS + EXPLICIT FEASIBLE TEST CLASS + SOURCE-SELECTIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, short-interval lower-order expansion, prime-power identity, or RH implication is claimed.

## 1. An explicit two-band compensation packet

Choose a real even bump

`phi in C_c^infinity((-1,1))`

with

`M_0 = int_R phi(x)dx != 0`

and

`phi''(0) != 0`.

For `a>b>0`, define the even translated packet

`P_(a,b)(q) = phi((q-a)/b) + phi((q+a)/b)`.

Because `b<a`, the two components are supported away from zero. Since `phi` is even,

`int_R |q| P_(a,b)(q)dq = 2ab M_0`.

Indeed, on the positive component write `q=a+bx`; then `|q|=a+bx`, and the odd part integrates to zero. The negative component contributes the same amount.

Now choose `eta` and `b` as in the claim and set

`g(q) = P_(xi_2,b)(q) - (xi_2/eta) P_(eta,b)(q)`.

Both packet pairs are supported away from zero, so

`g(0)=0`.

Their cusp pairings cancel exactly:

`int_R |q|g(q)dq`

` = 2b M_0 xi_2 - (xi_2/eta) 2b M_0 eta`

` = 0`.

Thus `g` is an exact Wang-leading-null test without using a shrinking bandwidth or a growing normalization.

## 2. The compensation band can be placed below every prime frequency

The smallest positive Rodgers arithmetic frequency is `xi_2`. There are no prime-power samples in `(0,xi_2)`.

Choose the compensation center `eta` strictly below `xi_2` and the width so that

`b < xi_2-eta`.

Then the support of `P_(eta,b)` does not meet `xi_2`. Also require

`xi_2+b < xi_3`.

Since `xi_3` is the next positive prime-power frequency after `xi_2` (`xi_3 < 2xi_2`), the complete positive support of `g` intersects the prime-power spectrum at exactly one point: `xi_2`.

At that point the compensation packet and the reflected component centered at `-xi_2` vanish together with all derivatives. Therefore

`g''(xi_2)=b^(-2) phi''(0) != 0`.

The translated low-frequency compensation needed to kill Wang's cusp functional is consequently invisible to the nonconstant Rodgers sampler.

## 3. The quadratic carrier is purely first-prime arithmetic

`VIS-264` gives, with `g=hat omega`,

`C_2(omega)`

` = g(0)/(2*pi^2)`

`   - (1/(8*pi^4)) sum_p sum_(m>=1)`

`       [(log p)^2/p^m] g''(m log(p)/(2*pi)).`

For the present test, `g(0)=0`, so the pole-compensation/DC channel is absent.

The support choice leaves only `(p,m)=(2,1)`. Hence

`C_2(omega)`

` = -(1/(8*pi^4)) [(log 2)^2/2] g''(xi_2)`

` = -(log(2)^2/(16*pi^4 b^2)) phi''(0)`.

This is nonzero by construction.

Thus the first-prime packet simultaneously satisfies three properties that were separated in the preceding branch:

1. it annihilates Wang's point-diagonal term;
2. it annihilates Wang's limiting cusp term;
3. its Rodgers quadratic carrier has neither a DC contribution nor cancellation between several prime powers.

The surviving coefficient is an exact single-frequency prime-power sample.

## 4. Wang compatibility has a sharp first-frequency threshold

The construction fits Wang's current fixed-margin theorem whenever its support lies in some fixed

`[-lambda,lambda]`, `lambda<theta`.

Because the packet must reach `xi_2`, such a fixed margin exists if and only if the chosen source-window exponent satisfies

`theta > xi_2 = log(2)/(2*pi) approx 0.110317...`.

For every such `theta`, choose `b` small enough and then choose

`xi_2+b < lambda < theta`.

All seminorms of `g` are fixed finite constants. The quantitative bound of `VIS-266` therefore reduces to

`O_(g,lambda,theta)(1/L + T^(lambda-theta)L)`

with `L=log T`, which tends to zero.

Conversely, within Wang's present support condition, no test supported in `[-lambda,lambda]` with `lambda<theta<=xi_2` can reach any nonzero Rodgers prime-power frequency. The number `xi_2` is therefore the exact first arithmetic-access threshold for this shared frequency-side representation.

This threshold is very different from the near-Montgomery-edge regime of `VIS-265`: isolating the first prime-power mode does not require `theta` close to one. It requires only enough support to cross the first discrete arithmetic frequency.

## 5. What the construction does and does not solve

`VIS-269` proved that any packet family whose support shrinks entirely below `xi_2` eventually loses every fixed-order nonconstant prime-power jet. The present construction shows the converse design point at quadratic order: retain one fixed band at `xi_2`, use a second subprime band only to cancel the universal cusp functional, and detailed arithmetic survives exactly.

This removes a possible algebraic obstruction. The Wang-null conditions are compatible with a pure source-selective quadratic carrier, and they can be satisfied without the `b(T)^(-4)`-type derivative growth of a unit quadratic packet whose bandwidth itself shrinks to zero.

But this is not yet a short-interval lower-order theorem. Rodgers' `C_2` belongs to the fixed smooth macroscopic source expansion audited in `VIS-260`--`VIS-264`; Wang's theorem supplies only the leading short-interval Montgomery functional. The present test lies in both *test-function classes*, but no canonical finding currently proves that Wang's short-interval statistic has a lower-order term equal to the Rodgers coefficient above, or any specified multiple of it.

Moreover, the normalized Wang remainder contains an `O(1/L)` term even for a fixed test. If the desired source-specific short-interval correction is itself `Theta(1/L)`, the present theorem cannot identify its coefficient. A useful transfer must either carry the lower-order arithmetic term explicitly or improve the remainder below the candidate scale for this exact fixed packet.

## 6. Prior-art and novelty boundary

The external inputs remain the two already audited sources for this branch.

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, arXiv:1203.3275, supplies the exact smooth source kernel whose quadratic carrier was decomposed in `VIS-264`.

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the short-interval leading Montgomery theorem and fixed support condition used in `VIS-265`--`VIS-268`.

The packet construction above uses only translation and dilation of a smooth bump plus one exact linear cancellation. A targeted source check found no reason to treat that elementary construction as a new general theorem, and no novelty is claimed for compensated band-pass test design. The durable Mathia content is the exact interface composition: under the conventions already frozen by the canonical findings, one can satisfy Wang's complete leading-null functional while isolating the first nonzero Rodgers arithmetic frequency with no DC contamination.

## Boundaries and falsification

The construction assumes the shared frequency-side dictionary used in `VIS-264` and reaffirmed in `VIS-269`. If a later source audit shows that the Wang test `g` and Rodgers `hat omega` cannot be identified in the intended statistic, the composition must be withdrawn.

The packet bandwidth `b` is fixed. Allowing `b=b(T)` to shrink reintroduces the seminorm conditioning studied in `VIS-266`--`VIS-268`; shrinking it below the first-frequency separation scale is unnecessary for the present single-prime isolation.

The claim is only quadratic. Higher fixed even carriers sample higher derivatives and may retain additional zero-frequency derivative terms even when `g(0)=0`, as shown in `VIS-269`.

No untouched confirmation-zero data are used.

## Research consequence

The shrinking subprime packet route is closed, but the first-prime translated route is algebraically viable. The next coherent question is now entirely a theorem-transfer question rather than another packet-existence problem:

for the fixed Wang-null test above, does a short-interval pair-correlation expansion contain the explicit first-prime Rodgers quadratic coefficient with a remainder asymptotically smaller than that coefficient's normalized scale?

Until such a result is derived or found, this packet is a clean source-selective calibration coordinate, not a validated short-interval arithmetic residual. Further generic moment cancellation or further narrowing of the same packet would move away from, rather than toward, the arithmetic frequency it is designed to retain.