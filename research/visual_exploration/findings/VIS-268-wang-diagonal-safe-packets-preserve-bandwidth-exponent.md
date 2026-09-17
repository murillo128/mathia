# VIS-268 — Wang-diagonal-safe cusp packets preserve the sharp bandwidth exponent

## Claim

Fix an integer `m>=1`, a fixed support margin `0<lambda<theta<1`, and write `L=log T`. Let `0<b<lambda`.

There exists a real even smooth test

`g_b in C_c^infinity((-b,b))`

satisfying simultaneously

`g_b(0)=0`,

`int g_b(q)dq=0`,

`int |q|g_b(q)dq=0`,

`int q^(2j)g_b(q)dq=0`, `j=1,...,m-1`,

and

`int q^(2m)g_b(q)dq=1`.

For such a family, the complete leading Montgomery functional appearing in `VIS-266`,

`g_b(0) + int |q|g_b(q)dq`,

vanishes exactly. The extra pointwise condition `g_b(0)=0` is necessary at the theorem interface: the cusp cancellation used in `VIS-267` kills the `int |q|g_b(q)dq` term but does not by itself cancel Wang's diagonal `g_b(0)` contribution.

Adding this diagonal-zero constraint does **not** change the sharp bandwidth powers from `VIS-267`. Every admissible packet still obeys

`||g_b||_infinity >= (2E_m)^(-1)b^(-(2m+1))`,

`||g_b'||_infinity >= (2E_m)^(-1)b^(-(2m+2))`,

where

`E_m = dist_(C[0,1])(t^(2m), span{1,t,t^2,t^4,...,t^(2m-2)}).`

Conversely, for every fixed `m` one can choose a fixed real even profile `h_m in C_c^infinity((-1,1))` satisfying the same cancellations together with `h_m(0)=0` and unit `2m`-th moment. The dilation

`g_b(q)=b^(-(2m+1))h_m(q/b)`

then has

`||g_b||_infinity = Theta_m(b^(-(2m+1)))`,

`||g_b'||_infinity = Theta_m(b^(-(2m+2))).`

Therefore the Wang proof budget from `VIS-266` has the same scale-sharp admissibility conditions as in `VIS-267`, while the leading term is now identically zero:

`1/(L b^(2m+2)) -> 0`,

`T^(lambda-theta)L/b^(2m+1) -> 0`.

For logarithmic bandwidth `b=L^(-q)` and fixed `lambda<theta`, the second condition is automatic and the exact proof-interface exponent gate remains

`q < 1/(2m+2).`

Thus the quadratic branch still requires `q<1/4`, and the quartic branch still requires `q<1/6`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-TRANSFER + INTERFACE CORRECTION + SCALE-SHARP CONTROL + NO-NOVELTY-CLAIM`.

No lower-order arithmetic coefficient, moving-support theorem, new pair-correlation theorem, or RH implication is claimed.

## 1. `VIS-267` cancels the cusp term but not the full Wang main term

`VIS-266` extracts from the proof of Biao Wang's Theorem 2.2 the normalized family formula

`(2*pi/(H L)) W_I(g_T)`
` = g_T(0) + int_R |alpha|g_T(alpha)dalpha`
`   + O_(lambda,theta)( ||g_T'||_infinity/L`
`       + ||g_T||_infinity[1/L + L^(-3/2) + T^(lambda-theta)L + 1/(H L)] ).`

The packet class in `VIS-267` imposes

`int |alpha|g_b(alpha)dalpha=0`

because that is the Fourier-side cusp nuisance inherited from the low-frequency extraction problem. But it imposes no condition on `g_b(0)`. Consequently a generic smooth realization from that class is not a leading-null Wang test: even after the cusp integral vanishes, the concentrated diagonal contribution can remain through the point evaluation at zero.

This is an interface distinction rather than a contradiction. `VIS-267` correctly computes the seminorm price of realizing the signed packet smoothly, but a future use of that packet as a *null probe* for Wang's leading law must also remove `g_b(0)`.

## 2. The diagonal-zero constraint is compatible with all moment conditions

Work in the real vector space of even functions `C_c^infinity((-1,1))`. Consider the finite family of linear functionals

`h -> h(0)`,

`h -> int h(x)dx`,

`h -> int |x|h(x)dx`,

and

`h -> int x^(2j)h(x)dx`, `j=1,...,m`.

These functionals are linearly independent. To see this, suppose a linear combination vanishes on every even smooth compactly supported `h`. First restrict to tests supported away from zero. On `(0,1)` the corresponding distribution is then integration against a function of the form

`a_0 + a_1 x + a_2 x^2 + a_4 x^4 + ... + a_(2m)x^(2m)`.

If its pairing with every smooth test supported in an arbitrary subinterval of `(0,1)` vanishes, that polynomial-like function is identically zero there. The functions `1,x,x^2,x^4,...,x^(2m)` are linearly independent on `(0,1)`, so all integral coefficients vanish. The remaining coefficient multiplying point evaluation at zero must then vanish as well.

Hence the finite-dimensional evaluation/moment map has full rank and is onto. In particular, one may choose a fixed even `h_m` for which the point value, mass, cusp moment, and lower even moments vanish while the `2m`-th moment equals one.

This proves existence without tuning `b` or using zeta-zero data.

## 3. Dilation preserves the cancellations with the same norm exponents

Set

`g_b(q)=b^(-(2m+1))h_m(q/b)`.

Then `g_b(0)=0`. A change of variables gives zero mass, zero cusp moment, all required zero lower even moments, and

`int q^(2m)g_b(q)dq=1`.

The norms scale exactly as

`||g_b||_infinity=b^(-(2m+1))||h_m||_infinity`,

`||g_b'||_infinity=b^(-(2m+2))||h_m'||_infinity`.

The universal lower bounds from `VIS-267` also continue to apply because this new class is a subclass of the packet class treated there. Therefore imposing `g_b(0)=0` changes constants and profile choice but not the optimal bandwidth exponents.

This matters operationally: making the probe diagonal-safe does not buy a cheaper transfer, but neither does it impose another inverse power of `b`.

## 4. Composition with Wang leaves the `1/(2m+2)` gate unchanged

For the diagonal-safe family,

`g_b(0) + int |alpha|g_b(alpha)dalpha = 0`.

Therefore `VIS-266` bounds the entire normalized statistic by its seminorm remainder. With the scale-sharp profile above this is

`O_(m,lambda,theta)( 1/(L b^(2m+2))`
` + 1/(L b^(2m+1))`
` + T^(lambda-theta)L/b^(2m+1)`
` + lower terms ).`

For `b<=1`, the derivative term dominates the elementary `1/L` amplitude term. Thus the same two conditions isolated in `VIS-267` are sufficient for the normalized Wang statistic of this leading-null family to tend to zero.

If `b=L^(-q)` and `delta=theta-lambda>0` is fixed, the support-tail term has the factor

`T^(-delta)L^(1+q(2m+1)) -> 0`

for every fixed `q`, while the derivative term tends to zero exactly when

`q<1/(2m+2)`.

At the proof-interface level, the extra diagonal cancellation is therefore free in exponent: it repairs what the test cancels without relaxing or worsening the scale barrier.

## 5. Prior-art and novelty boundary

The load-bearing external input is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Theorem 2.2 and the proof bookkeeping already audited in `VIS-266`. Wang's leading smooth-test functional contains both the point evaluation `g(0)` and the cusp pairing `int |alpha|g(alpha)dalpha`.

The additional construction here uses only finite-dimensional linear independence of elementary distributions, dilation, and the sharp packet norm bounds already established in `VIS-267`. A targeted source check found no claim in Wang's paper about this Mathia-specific cusp-and-moment carrier class; the paper's object is the short-interval pair-correlation theorem, not optimization of signed null probes.

No novelty is claimed for moment interpolation, point-evaluation constraints, or dilation separately. The durable content is the interface correction: the accepted visual branch must work in a test class that annihilates **both** pieces of Wang's leading functional if it wants to expose a lower-order residual, and doing so preserves the previously derived bandwidth exponent.

## 6. Boundaries and falsification

This finding says only that diagonal-safe packets exist and have the same scale exponents under the fixed-margin Wang interface. It does not show that any lower-order arithmetic residual survives in that class.

The fixed support margin `lambda<theta` remains essential. No uniformity as `lambda` approaches `theta` is obtained, so the support-edge obstruction from `VIS-265` is unchanged.

The `q<1/(2m+2)` threshold characterizes what Wang's present seminorm proof can certify for this unit-carrier family; it is not a lower bound on the true pair-correlation error and not an impossibility theorem beyond the threshold.

A stronger theorem controlled by weaker test norms, an explicit lower-order expansion with structured error, or a direct nonsmooth-test formulation could change the admissible scale. Likewise, a source-specific coefficient may force a different normalization from the unit `2m`-th moment used here.

No untouched confirmation-zero data are used.

## Research consequence

The smooth-transfer branch now has the correct leading-null interface. Future quadratic or quartic source tests should not use the `VIS-267` moment constraints alone; they should impose `g(0)=0` as well before interpreting any residual beneath Wang's leading Montgomery term.

That repair leaves the real bottleneck where it belongs. The next useful step is source-specific: derive a pre-registered arithmetic coefficient for a diagonal-safe quadratic or quartic packet and compare its size with a remainder that remains small after the same `b^(-(2m+2))` seminorm amplification. If no such signal/error window exists inside `q<1/4` or `q<1/6`, respectively, the corresponding branch should be killed rather than rescued by further generic moment cancellation.