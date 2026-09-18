# VIS-302 — Wang's exact coefficients save one logarithm in the interior mean-value boundary

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and let

`a_n = (Lambda(n)/sqrt(n)) min(n/x,x/n)`

be Biao Wang's Dirichlet-polynomial coefficients. Put

`M(x)=sum_n n a_n^2`.

Then, as `x->infinity`,

`M(x) = (4/3)x log x + (8/9)x + O(x exp(-c V(log x)))`,

for some `c>0`, where `V(y)=y^(3/5)(log y)^(-1/5)` as in `VIS-291`. In particular,

`M(x) << x log(2x)`.

Wang's displayed `M(x)<<x log^2(2x)` bound therefore loses one logarithm because it uses only the pointwise estimate `Lambda(n)<=log n`; the weighted coefficient moment itself inherits the same prime-number-theorem input already used for the diagonal sum in `VIS-291`.

Combining this coefficient-specific estimate with the gamma-recentered interior decomposition and the zero-free localization argument of `VIS-298`--`VIS-301` gives the pointwise asymptotic

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`

for every moving source `x=x(T)->infinity` satisfying

`x log(2x)/H -> 0`.

Thus the `H/L^2` layer isolated in `VIS-301` is not a genuine boundary of the current proof. The first unresolved generic interior scale moves to `x log x asymp H`, equivalently `x` of order `H/L` in the polynomial source regime.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + COEFFICIENT-SPECIFIC PROOF-STRUCTURE REFINEMENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not improve the Montgomery--Vaughan mean-value theorem, the prime-number theorem, Wang's pair-correlation theorem, or the classical zero-free region. It only evaluates the particular error weight appearing when the mean-value theorem is applied to Wang's exact coefficients.

## 1. The weighted moment has an explicit PNT asymptotic

Let

`A(u)=sum_(n<=u) Lambda(n)^2`.

`VIS-291` derives from the classical Korobov--Vinogradov prime-number-theorem remainder that

`A(u)=u log u-u+R(u)`,

with

`R(u)=O(u exp(-c_0 V(log u)))`.

From the definition of `a_n`,

`M(x)`
` = x^(-2) sum_(n<=x) n^2 Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^2`.

For the lower piece, Stieltjes partial summation gives

`x^(-2) sum_(n<=x) n^2 Lambda(n)^2`
` = x^(-2)[x^2 A(x)-2 integral_2^x t A(t) dt]`
` = x[(1/3)log x-1/9]`
`   + O(x exp(-c_1 V(log x)))`.

The fixed lower endpoint contributes only `O(x^-2)` and is absorbed.

For the upper piece,

`x^2 sum_(n>x) Lambda(n)^2/n^2`
` = -A(x)+2x^2 integral_x^infinity A(t)/t^3 dt`
` = x(log x+1)`
`   + O(x exp(-c_1 V(log x)))`.

The stretched-exponential remainder keeps the same shape after either weighted integral, after decreasing the positive constant if necessary. Adding the two pieces yields

`M(x)=(4/3)x log x+(8/9)x+O(x exp(-c_1 V(log x)))`.

The constants are not needed for the boundary argument, but they show that the natural size really is `x log x`; the saved logarithm is not merely a softer upper bound.

## 2. The Montgomery--Vaughan interior error moves from `x log^2 x` to `x log x`

The Montgomery--Vaughan mean-value theorem used by Wang gives on an interval of length `H`

`integral_I |D_x(t)|^2 dt`
` = H sum_n a_n^2 + O(M(x))`.

`VIS-291` already gives

`sum_n a_n^2 = log x + O(exp(-c_2 V(log x)))`.

Hence

`integral_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c_2 V(log x)) + x log(2x))`.

For every `x->infinity` with `x log(2x)=o(H)`, both errors are `o(H)`. The interior Dirichlet-polynomial energy is therefore asymptotic at absolute `H` resolution well beyond the `x=o(H/L^2)` range inherited from Wang's coarser coefficient estimate.

No cancellation in the actual off-diagonal time integral is used here. The improvement occurs before that question: the generic mean-value theorem was already being fed an unnecessarily large bound for its coefficient weight.

## 3. The zero-free localization estimate remains negligible up to this larger scale

`VIS-301` sharpened Wang's localization proof using the classical zero-free-region factor

`q_T(x)=x^(-eta_T)`,

with

`eta_T asymp L^(-2/3)(log L)^(-1/3)`.

Its explicit bounds are

`integral_(R\I)|A_I|^2 + integral_I|A-A_I|^2`
` << x q_T(x)^2 L^2 + x L^2 H/T^2`,

and for the inside--outside coherence

`|C_I(x)| << x q_T(x)^2 L^3 + x q_T(x)L^2 H/T`.

To reuse them under the present hypothesis, split exactly as in `VIS-301`. If

`x<=H/L^4`,

the original `O(xL^3)` localization estimate is already `o(H)`. Otherwise

`x>H/L^4`,

so

`log x >= theta L-4 log L`

and consequently `q_T(x)` is super-polynomially small in `L`. In this range `log x asymp L`, and the assumption

`x log(2x)/H ->0`

implies `xL/H->0`. Therefore

`x q_T(x)^2 L^3/H = (xL/H)[q_T(x)^2 L^2] ->0`,

while the pure leakage terms are smaller. The far-zero cross term also satisfies

`x q_T(x)L^2/T ->0`,

because `x=o(H/L)` and `H L/T=T^(theta-1)L->0`.

Thus the complete localization difference remains `o(H)` throughout the new range. The `L^-2` layer of `VIS-301` was caused by the interior coefficient bound, not by a hidden return of localization leakage.

## 4. Reassemble the pointwise statistic

The gamma-recentered decomposition of `VIS-298`--`VIS-299` needs only `x->infinity` and `x<T` for the remaining gamma, absolutely convergent zeta, pole/trivial-zero, and frequency-aware cross terms to be `o(H)` at the present scale. The condition `x log(2x)=o(H)` with `H=T^theta`, `theta<1`, gives `x<T` eventually.

Combining those estimates with Sections 2 and 3 yields

`integral_I |A(x,t)|^2 dt`
` = H log x + H(L-log(2*pi))^2/x^2 + o(H)`,

and the interval/full-zero localization comparison contributes another `o(H)`. Hence

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`.

For sources of polynomial size relative to `T`, `log x asymp L`, so the unresolved scale is now

`x L asymp H`,

rather than `x L^2 asymp H`.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the coefficient sequence and the Montgomery--Vaughan mean-value step. In Lemma 2.5 the bound `sum n a_n^2 << x log^2(2x)` is obtained from a direct pointwise estimate on `Lambda`; the present calculation instead inserts the standard asymptotic for the summatory square of `Lambda`.

The prime-number-theorem input is exactly the classical Korobov--Vinogradov-scale input already audited in `VIS-291`, including the 2026 Bellotti refinement used there only through a weaker standard-shaped consequence. The two Stieltjes partial-summation calculations above are elementary specializations to Wang's weight. No claim of novelty is made for weighted PNT moments or for the Montgomery--Vaughan theorem.

The new conclusion is only a proof-boundary correction: the exact coefficients do not support an `x log^2 x` obstruction. This finding does **not** show that the actual mean-value remainder has size `x log x`, does not prove an asymptotic at `x log x asymp H`, and does not rule out further cancellation in the off-diagonal time integral.

## Dependencies

- `VIS-291`: Korobov--Vinogradov asymptotic for `A(u)=sum_(n<=u)Lambda(n)^2` and for `sum a_n^2`.
- `VIS-298`: exact gamma recentering and frequency-aware interior decomposition.
- `VIS-299`: proof-level moving-ceiling argument for the pointwise statistic.
- `VIS-300`: exact localization-energy decomposition.
- `VIS-301`: zero-free suppression of the localization terms and identification of the previously apparent `H/L^2` interior boundary.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose upper branch asks for a coefficient-specific audit of the mean-value remainder.

## Research consequence

Do not treat `x asymp H/L^2` as the next pointwise source barrier. The coefficient moment entering Montgomery--Vaughan is asymptotic to `(4/3)x log x`, so the current proof already reaches every moving source with

`x log(2x)=o(H)`.

The next upper-source question is narrower and genuinely off-diagonal: near `x log x asymp H`, is the Montgomery--Vaughan error for Wang's exact coefficients asymptotic to a nonzero `H`-scale correction, can its oscillatory off-diagonal contribution cancel further, or can a matched admissible coefficient/control model show that this scale is sharp without assuming the pair-correlation conclusion?