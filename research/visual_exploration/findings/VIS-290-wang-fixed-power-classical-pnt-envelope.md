# VIS-290 — Wang's fixed-power residual obeys a classical PNT stretched-exponential envelope

## Claim

Let `H=T^theta`, `L=log T`, with fixed `0<theta<1`. Fix a compact source-exponent panel

`0 < beta_0 <= beta <= beta_1 < theta`,

and put `x=T^beta`. For Biao Wang's short-interval pair-correlation statistic `F_I(x)`, there exists `c_0>0` such that, uniformly for `beta in [beta_0,beta_1]`,

`F_I(T^beta) = (H/(2*pi))(L^2 T^(-2 beta) + beta L) + O(H exp(-c_0 sqrt(L)))`.

Since the explicit term `H L^2 T^(-2 beta)` is itself `O(H exp(-c_0 sqrt(L)))` after decreasing `c_0` if necessary,

`F_I(T^beta) = (H beta L)/(2*pi) + O(H exp(-c_0 sqrt(L)))`

uniformly on the panel.

Thus the `o(H)` conclusion in `VIS-289` can be made quantitative using only the classical de la Vallée Poussin prime-number-theorem remainder. No fixed-power residual larger than this stretched-exponential envelope can survive Wang's existing decomposition on a compact interior exponent panel.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED + QUANTITATIVE NEGATIVE SCALE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that this is the best possible unconditional remainder, that the stretched-exponential scale is intrinsic to the statistic, or that a nonzero residual exists at or below this scale. Stronger prime-number-theorem remainders would sharpen the envelope without changing the structural conclusion.

## 1. Quantitative squared-von-Mangoldt asymptotic

Write

`A(u)=sum_(n<=u) Lambda(n)^2`.

NIST DLMF §27.12.5 records the classical estimate

`pi(u)-li(u)=O(u exp(-c sqrt(log u)))`

for some `c>0`. Partial summation therefore gives

`sum_(p<=u) (log p)^2 = u log u-u + O(u exp(-c_1 sqrt(log u)))`

for some `c_1>0`: the powers of `log u` introduced by partial summation are absorbed by reducing the constant in the stretched exponential.

The contribution of prime powers `p^k<=u`, `k>=2`, is

`O(sqrt(u) log^3 u)`,

which is smaller than `u exp(-c_2 sqrt(log u))` for a suitable `c_2>0`. Hence

`A(u)=u log u-u+O(u exp(-c_2 sqrt(log u)))`.

This is standard prime-number-theorem arithmetic. The point here is only to retain a quantitative remainder rather than collapse it to the `o(u)` used in `VIS-289`.

## 2. The symmetric coefficient square inherits the same envelope

Wang's coefficients are

`a_n = Lambda(n)/sqrt(n) * min(n/x,x/n)`,

so

`S(x):=sum_n a_n^2`

` = x^(-2) sum_(n<=x) n Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Insert

`A(t)=t log t-t+E(t)`,

with

`E(t)=O(t exp(-c_2 sqrt(log t)))`.

Stieltjes partial summation gives

`x^(-2) sum_(n<=x) n Lambda(n)^2`
` = (1/2) log x - 1/4 + O(exp(-c_3 sqrt(log x)))`,

and

`x^2 sum_(n>x) Lambda(n)^2/n^3`
` = (1/2) log x + 1/4 + O(exp(-c_3 sqrt(log x)))`

for some `c_3>0`. The constants cancel exactly, leaving

`S(x)=log x+O(exp(-c_3 sqrt(log x)))`.

The tail estimate is harmless because

`x^2 integral_x^infinity t^(-3) exp(-c_2 sqrt(log t)) dt`

is `O(exp(-c_3 sqrt(log x)))`; the lower piece is controlled similarly after division by `x^2`.

## 3. Propagate the quantitative input through Wang's proof

Wang's Montgomery–Vaughan mean-value step is

`int_I |D_x(t)|^2 dt`
` = H sum_n a_n^2 + O(sum_n n a_n^2)`.

Lemma 2.5 supplies

`sum_n n a_n^2 << x log^2(2x)`,

so the sharpened coefficient square yields

`int_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c_3 sqrt(log x)) + x log^2(2x))`.

The rest of Wang's Proposition 2.6 proof contributes the same explicit terms already isolated in `VIS-288`:

`HL/x^2`, `H sqrt(L)/x`, `xL^3`, and `L/sqrt(x)`,

besides the displayed main term `HL^2/x^2`.

Now set `x=T^beta`. Since `beta>=beta_0`,

`exp(-c_3 sqrt(log x)) <= exp(-c_3 sqrt(beta_0) sqrt(L))`.

Since also `beta<=beta_1<theta`, every power-decaying remainder is eventually smaller than `H exp(-c_0 sqrt(L))` for a sufficiently small fixed `c_0>0`. For example,

`xL^3/H <= T^(beta_1-theta)L^3`,

and this decays exponentially in `L`, faster than any `exp(-c_0 sqrt(L))`. The same comparison absorbs `x log^2 x`, `HL/x^2`, `H sqrt(L)/x`, `L/sqrt(x)`, and the explicit `HL^2/x^2` term when only the linear baseline is retained.

Therefore

`F_I(T^beta) = (H/(2*pi))(L^2 T^(-2 beta)+beta L)`
`              + O(H exp(-c_0 sqrt(L)))`,

and also

`F_I(T^beta) = (H beta L)/(2*pi)`
`              + O(H exp(-c_0 sqrt(L)))`

uniformly for `beta in [beta_0,beta_1]`.

## 4. Prior art and evidence boundary

The pair-correlation decomposition, coefficient definition, Montgomery–Vaughan mean-value step, and complete error budget are from Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially Lemma 2.5 and Proposition 2.6.

The only new input relative to Wang's displayed proof is to retain the standard quantitative prime-number-theorem remainder rather than use `sum_(n<=u)Lambda(n)^2=u log u+O(u)`. NIST DLMF §27.12.5 gives a classical de la Vallée Poussin estimate sufficient for the stretched-exponential bound above. No novelty is claimed for that prime-number-theorem estimate, its weighted partial-summation consequences, or the resulting improvement as an analytic-number-theory theorem.

A stronger zero-free-region remainder can improve `exp(-c_0 sqrt(L))`; consequently this scale is **not** asserted to be the true residual frontier. The durable Mathia conclusion is only that the compact fixed-power branch is quantitatively smaller than `H` by an explicit unconditional factor, and the size of that factor is inherited from ordinary prime-counting accuracy rather than from a newly exposed pair-correlation mechanism.

## Dependencies

- `VIS-287`: complete-statistic fixed-power linearization at the `HL` scale.
- `VIS-288`: extraction of the apparent `O(H)` fixed-power residual frontier.
- `VIS-289`: removal of that `H`-scale floor via the two-term squared-von-Mangoldt asymptotic.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose sub-`H` fixed-power branch is quantitatively narrowed here.

## Research consequence

On every fixed compact exponent panel inside `(0,theta)`, the complete statistic after subtracting its linear source law has the unconditional bound

`O(H exp(-c_0 sqrt(log T)))`.

A proposed fixed-power source signal that is asymptotically larger than this envelope is already incompatible with the same Wang decomposition once standard quantitative prime-counting input is retained. Continuing the fixed-power branch is justified only by a sharper lower-scale expansion whose candidate term dominates the **complete** improved error budget; otherwise the structurally distinct remaining route is a genuinely moving source boundary not covered by one fixed compact exponent panel.