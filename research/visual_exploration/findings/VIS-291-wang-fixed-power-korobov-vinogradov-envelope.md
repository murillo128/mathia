# VIS-291 — Wang's fixed-power residual inherits the Korobov–Vinogradov PNT envelope

## Claim

Let `H=T^theta`, `L=log T`, with fixed `0<theta<1`. Fix a compact source-exponent panel

`0 < beta_0 <= beta <= beta_1 < theta`,

and put `x=T^beta`. Define

`V(y)=y^(3/5) (log y)^(-1/5)`

for sufficiently large `y`. Then there exists `c_0>0`, depending at most on the fixed panel and Wang's fixed parameters, such that Biao Wang's short-interval pair-correlation statistic satisfies

`F_I(T^beta) = (H beta L)/(2*pi)`
`              + O(H exp(-c_0 V(L)))`

uniformly for `beta in [beta_0,beta_1]`.

Equivalently, the complete compact fixed-power residual above the linear source law obeys

`F_I(T^beta)-(H beta L)/(2*pi)`
` = O(H exp(-c_0 L^(3/5) (log L)^(-1/5)))`.

This strictly sharpens the de la Vallée Poussin `exp(-c sqrt(L))` envelope of `VIS-290`. The improvement is not a new pair-correlation mechanism: it is inherited from the Korobov–Vinogradov scale in the strongest standard unconditional prime-number-theorem remainder.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED + QUANTITATIVE NEGATIVE SCALE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that a nonzero residual occurs at this scale, that this scale is intrinsic to `F_I`, or that the bound is optimal for Wang's specially smoothed squared-von-Mangoldt coefficient sum. A sharper estimate for that specific arithmetic input would sharpen the conclusion again.

## 1. Current PNT input at Korobov–Vinogradov scale

Let

`psi(u)=sum_(n<=u) Lambda(n)`.

The Korobov–Vinogradov zero-free-region machinery gives the classical-shaped consequence

`psi(u)=u+O(u exp(-c V(log u)))`

for some `c>0`, where here

`V(log u)=(log u)^(3/5)(log log u)^(-1/5)`.

For the current literature boundary, Bellotti's 2026 refinement gives an essentially optimal PNT error associated with a Korobov–Vinogradov zero-free region in the form

`psi(u)-u << u exp(-omega(u))`,

with `omega` defined from the zero-free width; in particular it implies a bound of the displayed Korobov–Vinogradov shape after weakening constants. NIST DLMF §27.12.6 records the same `3/5,1/5` scale for the classical best asymptotic error in `pi(u)-li(u)`.

Only this weaker shape consequence is used below. No explicit numerical constant is needed.

## 2. Squared von Mangoldt inherits the same scale

Write

`A(u)=sum_(n<=u) Lambda(n)^2`.

First remove prime powers from `psi`. Their total contribution is `O(sqrt(u) log^2 u)`, so the Chebyshev prime sum

`theta(u)=sum_(p<=u) log p`

also satisfies

`theta(u)=u+O(u exp(-c_1 V(log u)))`

for some `c_1>0`.

Partial summation then gives

`sum_(p<=u) (log p)^2`
` = theta(u) log u - integral_2^u theta(t)/t dt`
` = u log u-u + O(u exp(-c_2 V(log u)))`.

Powers of `log u` arising at the endpoint or in the integral are absorbed by decreasing the positive constant in the exponential. The contribution to `A(u)` from `p^k<=u`, `k>=2`, is at most `O(sqrt(u) log^3 u)`, which is much smaller than `u exp(-c_2 V(log u))`. Therefore

`A(u)=u log u-u+O(u exp(-c_3 V(log u)))`.

This is again standard PNT arithmetic; the only purpose is to preserve its strongest known unconditional scale through the coefficient used by Wang.

## 3. Wang's symmetric coefficient square preserves the envelope

Wang's coefficients are

`a_n = Lambda(n)/sqrt(n) * min(n/x,x/n)`,

so, as in `VIS-289` and `VIS-290`, define

`S(x)=sum_n a_n^2`

` = x^(-2) sum_(n<=x) n Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Insert

`A(t)=t log t-t+R(t)`,

with

`R(t)=O(t exp(-c_3 V(log t)))`.

Stieltjes partial summation yields the same exact main pieces

`x^(-2) sum_(n<=x) n Lambda(n)^2`
` = (1/2) log x - 1/4 + O(exp(-c_4 V(log x)))`,

and

`x^2 sum_(n>x) Lambda(n)^2/n^3`
` = (1/2) log x + 1/4 + O(exp(-c_4 V(log x)))`.

For the tail, dyadic decomposition or direct comparison with the monotone stretched-exponential envelope shows that

`x^2 integral_x^infinity t^(-3) exp(-c_3 V(log t)) dt`

has the same form after decreasing the constant. The constants `-1/4` and `+1/4` cancel, hence

`S(x)=log x+O(exp(-c_4 V(log x)))`.

Thus the stronger PNT input survives Wang's symmetric smoothing without creating a new constant-order term.

## 4. Propagation through Wang's complete fixed-power error budget

Wang's Montgomery–Vaughan mean-value step gives

`int_I |D_x(t)|^2 dt`
` = H S(x) + O(sum_n n a_n^2)`,

and Lemma 2.5 gives

`sum_n n a_n^2 << x log^2(2x)`.

Consequently

`int_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c_4 V(log x)) + x log^2(2x))`.

The remaining terms in Wang's Proposition 2.6 are the same ones isolated in `VIS-288` and propagated in `VIS-290`: `HL/x^2`, `H sqrt(L)/x`, `xL^3`, `L/sqrt(x)`, together with the explicit `HL^2/x^2` term if only the linear baseline is retained.

Set `x=T^beta`. On the fixed panel,

`V(beta L) >= c_5 V(L)`

for all sufficiently large `L`, uniformly in `beta`, because `beta>=beta_0>0` and `log(beta L)=log L+O(1)`. Every other error above is polynomially small in `T` relative to `H`, hence exponentially small in `L`, and therefore smaller than `H exp(-c_0 V(L))` after choosing `c_0>0` sufficiently small.

The explicit term `HL^2 T^(-2 beta)` is absorbed for the same reason. Therefore

`F_I(T^beta) = (H beta L)/(2*pi)`
`              + O(H exp(-c_0 L^(3/5)(log L)^(-1/5)))`

uniformly on every pre-fixed compact exponent panel inside `(0,theta)`.

## 5. Prior art and evidence boundary

The pair-correlation decomposition, coefficient definition, Montgomery–Vaughan mean-value step, and complete fixed-power error budget are from Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Lemma 2.5 and Proposition 2.6.

The prime-number-theorem input is standard analytic-number-theory prior art. NIST DLMF §27.12.6 records the Korobov–Vinogradov `exp(-d (log x)^(3/5)(log log x)^(-1/5))` scale for the PNT error. Chiara Bellotti, **A new zero-density estimate for zeta(s) and the error term in the Prime Number Theorem**, *Bulletin of the London Mathematical Society* 58 (2026), e70442, DOI `10.1112/blms.70442`, gives the current essentially optimal error associated with the Korobov–Vinogradov zero-free region directly for `psi(x)-x`.

No novelty is claimed for either PNT estimate or for the partial-summation transfer itself. The Mathia contribution here is only the explicit specialization showing that Wang's complete compact fixed-power residual inherits this stronger unconditional envelope once the arithmetic input is propagated through every already-recorded error term.

The result does not prove an asymptotic secondary term, does not exclude cancellation special to `S(x)` beyond generic PNT bounds, and does not control moving exponents `beta=beta(T)` approaching `0` or `theta`. It supplies no new pair-correlation theorem, zero-density theorem, zero-free region, off-critical-strip gain, or RH criterion.

## Dependencies

- `VIS-287`: complete-statistic fixed-power linearization at the `HL` scale.
- `VIS-288`: localization of the apparent `O(H)` residual frontier.
- `VIS-289`: removal of the bare `H` floor using the two-term squared-von-Mangoldt asymptotic.
- `VIS-290`: first quantitative fixed-power envelope using a de la Vallée Poussin remainder.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose deeper fixed-power branch is narrowed here.

## Research consequence

The compact fixed-power route is now bounded at the standard Korobov–Vinogradov PNT scale:

`O(H exp(-c_0 L^(3/5)(log L)^(-1/5)))`.

Therefore merely replacing Wang's coarse prime input by a stronger **already-known generic PNT remainder** cannot expose a larger fixed-power source signal. A further fixed-power advance must use arithmetic information more specific than the generic PNT envelope — for example a structural expansion of the particular symmetric `Lambda^2` smoothing that survives Wang's full error budget — or require genuinely new prime-counting input. The distinct alternative remains a moving source boundary where no single fixed compact exponent panel applies.