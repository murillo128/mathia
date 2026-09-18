# VIS-296 — Wang's relative lower boundary reduces to the mean explicit-formula remainder

## Claim

Let

`H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and fix `lambda<theta`. Let `x=x(T)` satisfy

`x -> infinity`, `1 <= x <= T^lambda`,

and suppose the gamma-subtracted relative-boundary ratio has a finite positive limit

`x^2 log x / L -> kappa in (0,infinity)`.

Use Wang's exact decomposition on `I=(T,T+H]`,

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`,

with

`B_x(t)=log(t+2)/x`

and `E_x(t)=O(1/x)` uniformly in the stated source range. Define the normalized mean explicit-formula remainder

`Q_E(T,x) = (x/H) integral_I E_x(t) dt`.

Then, after the squared-von-Mangoldt coefficient refinement already established in `VIS-291`, Wang's gamma-subtracted statistic

`R_gamma(T,x)=F_I(x)-(H/(2*pi))L^2/x^2`

satisfies

`R_gamma(T,x)`
` = (H/(2*pi)) log x`
`   + (H L/(pi x^2)) Re Q_E(T,x)`
`   + o(H log x)`.

Equivalently,

`R_gamma(T,x)/(H log x)`
` = 1/(2*pi)`
`   + [L/(pi x^2 log x)] Re Q_E(T,x)`
`   + o(1)`

and hence

`R_gamma(T,x)/(H log x)`
` = 1/(2*pi) + Re Q_E(T,x)/(pi kappa) + o(1)`.

Since Wang's pointwise remainder bound gives `Q_E(T,x)=O(1)`, the present theorem leaves exactly one potentially order-one channel at this relative crossover: the **mean of the explicit-formula remainder**. In particular, relative linearization at a boundary family with finite positive `kappa` follows if `Re Q_E(T,x)->0`.

The `O(HL/x^2)` error in Wang's Proposition 2.6 is therefore not a single irreducible obstruction. Its contribution from `int_I |B_x|^2` is an artifact of the coarse estimate `log(t+2)=L+O(1)` and becomes negligible on the power-short interval. At the relative boundary, after that refinement, the surviving `HL/x^2` channel is the `B_x,E_x` cross term.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT ERROR-BUDGET REFINEMENT + BOUNDARY REDUCTION + NO-NOVELTY-CLAIM`.

No estimate for `Q_E` beyond `O(1)`, new pair-correlation asymptotic, new explicit formula, zero-free region, or RH implication is claimed.

## 1. Wang's two sources of the `HL/x^2` scale are different

Wang's Proposition 2.6 gives, uniformly for `1<=x<=T^lambda`,

`F_I(x)`
` = (H/(2*pi))(L^2/x^2+log x)`
`   + O(H + HL/x^2 + H sqrt(L)/x + xL^3 + L/sqrt(x))`.

In the proof, the displayed `HL/x^2` scale occurs in at least two logically different places.

First,

`integral_I |B_x(t)|^2 dt`
` = HL^2/x^2 + O(HL/x^2)`

is obtained only from the uniform replacement `log(t+2)=L+O(1)`.

Second, from `||E_x||_2 << sqrt(H)/x` and `B_x(t) << L/x`, Cauchy--Schwarz gives the mixed term

`2 Re integral_I B_x(t) overline(E_x(t)) dt = O(HL/x^2)`.

These two appearances should not be charged as though they had the same information content. The first is controlled directly by the fact that `I` is short relative to height `T`; the second depends on the unresolved residual in the explicit formula.

## 2. The pure `B_x` error is much smaller on `I=(T,T+H]`

For `t in I`, write

`log(t+2)=L+delta_T(t)`.

Because `H=T^theta` with `theta<1`,

`delta_T(t)=log(1+(t-T+2)/T)=O(H/T)`

uniformly on `I`. Therefore

`integral_I |B_x(t)|^2 dt`
` = x^(-2) integral_I (L+delta_T(t))^2 dt`
` = HL^2/x^2 + O(H^2 L/(T x^2))`.

The quadratic `delta_T^2` contribution is smaller and is absorbed in the displayed error. Thus the `O(HL/x^2)` term in Wang's equation for `int |B_x|^2` is not load-bearing for power-short intervals.

At the relative boundary `x^2 log x/L -> kappa`,

`[H^2 L/(T x^2)] / [H log x]`
` = (H/T) [L/(x^2 log x)]`
` -> 0`.

Hence the pure gamma-factor square contributes only the explicit baseline `HL^2/x^2` plus `o(H log x)` at this crossover.

## 3. All other recorded channels are lower order at the relative boundary

`VIS-291` sharpens the squared-von-Mangoldt coefficient square before any fixed-power specialization to

`sum_n a_n^2 = log x + O(exp(-c V(log x)))`,

where `V(y)=y^(3/5)(log y)^(-1/5)` after weakening constants. Consequently the diagonal `D_x` remainder contributes

`o(H log x)`

whenever `x->infinity`.

The `D_x,E_x` cross term is also negligible at the present boundary. Its recorded size is

`H sqrt(L)/x`,

and

`[H sqrt(L)/x]/[H log x] = sqrt(L)/(x log x)`.

Squaring the last ratio gives

`L/[x^2 (log x)^2]`
` = [L/(x^2 log x)] / log x -> 0`,

so the ratio itself tends to zero.

The remaining terms are smaller still. Since `x<=T^lambda` with fixed `lambda<theta`,

`xL^3/(H log x)->0`.

Also `L/(sqrt(x) H log x)->0`, the `E_x` square is `O(H/x^2)=o(H log x)`, and Wang's `D_x,B_x` cross term `O(L/sqrt(x))` is negligible compared with `H log x`.

Thus, after the refined pure-`B_x` calculation, no recorded term except the `B_x,E_x` cross can remain on the `H log x` scale when `x^2 log x/L` stays of constant order.

## 4. The remaining cross term is a single normalized mean

Again write

`B_x(t)=(L+delta_T(t))/x`,

with `delta_T=O(H/T)`. Then

`2 Re integral_I B_x(t) overline(E_x(t)) dt`
` = (2L/x) Re integral_I overline(E_x(t)) dt`
`   + O(H^2/(T x^2))`.

The error follows from `E_x(t)=O(1/x)` and the uniform bound on `delta_T`. With

`Q_E(T,x)=(x/H) integral_I E_x(t) dt`,

the main cross term becomes

`(2HL/x^2) Re Q_E(T,x)`.

Wang's relation

`2*pi F_I(x)=integral_I |A(x,t)|^2 dt + O(xL^3)`

then gives the formula in the claim after the previously controlled terms are inserted.

The pointwise estimate `E_x(t)=O(1/x)` implies only

`Q_E(T,x)=O(1)`.

That is exactly enough for the mixed term to remain potentially visible when `x^2 log x/L` has constant order, but it supplies no evidence that a nonzero limit actually occurs.

## 5. Interpretation of the lower boundary

`VIS-294` identified `x~sqrt(L)` as the first lower scale where Wang's current errors can reach absolute `H` size. `VIS-295` then showed that after subtracting the explicit gamma term, relative linearization persists farther down while `x^2 log x/L -> infinity`.

The present reduction explains what changes when that ratio stops diverging. Near

`x^2 log x ~ L`,

the square-root cross error `H sqrt(L)/x` is already relatively negligible, and the apparent `HL/x^2` uncertainty from the pure gamma square is removable by using the actual short-interval variation of `log(t+2)`. The remaining relative-scale uncertainty is concentrated in the mean of `E_x` through `Q_E`.

This does **not** prove that `E_x` carries new arithmetic information. In the Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh explicit formula inherited by Wang, `E_x` packages the residual terms left after the prime Dirichlet polynomial and the displayed logarithmic gamma contribution are separated. A more explicit decomposition may show that its interval mean is classical, removable, or smaller than the current pointwise `O(1/x)` bound.

Accordingly, `x^2 log x~L` should not yet be interpreted as an intrinsic pair-correlation transition. It is the first relative scale at which the **mean explicit-formula remainder** must be understood rather than bounded blindly.

## 6. Prior art and evidence boundary

The decomposition `A=-D_x+B_x+E_x`, the bound `E_x(t)<<1/x` in the fixed theorem range, and Proposition 2.6 are from Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), especially equations (2.7)--(2.9) and Proposition 2.6. Wang explicitly obtains the pure-`B_x` estimate from `log(t+2)=L+O(1)` and bounds the `B_x,E_x` cross by `O(HL/x^2)`.

Wang's explicit formula is inherited from S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, and C. L. Turnage-Butterbaugh, **An unconditional Montgomery Theorem for Pair Correlation of Zeros of the Riemann Zeta Function**, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799, Lemma 1, ultimately originating in Montgomery's pair-correlation argument.

No novelty is claimed for the elementary short-interval Taylor estimate for `log(t+2)`, for the source explicit formula, or for Cauchy--Schwarz. The Mathia-specific contribution is only the error-channel accounting at the moving relative boundary: it identifies which occurrence of `HL/x^2` is artificial there and reduces the surviving boundary obstruction to the exact scalar mean `Q_E`.

This finding does not determine `Q_E`, prove that it has a limit, or show that it is arithmetic-specific. It also does not resolve the distinct absolute-`H` boundary at `x=O(sqrt(L))`, where both mixed `E_x` channels can still be order `H`.

## Dependencies

- `VIS-291`: Korobov--Vinogradov-scale refinement of Wang's squared-von-Mangoldt coefficient square.
- `VIS-294`: absolute-`H` lower moving-source boundary.
- `VIS-295`: relative gamma-subtracted boundary `x^2 log x/L -> infinity`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose lower-source branch asks for the load-bearing origins of `H sqrt(L)/x` and `HL/x^2`.

## Research consequence

The next relative-boundary test is now sharply localized. Instead of treating all of Wang's Proposition 2.6 errors as one undifferentiated barrier, analyze the exact remainder mean

`Q_E(T,x)=(x/H) integral_I E_x(t) dt`

for families with `x^2 log x/L -> kappa in (0,infinity)`.

If `Re Q_E -> 0`, the gamma-subtracted linear law extends through that crossover. If a nonzero contribution survives, it must be identified from the explicit-formula remainder itself and tested for whether it is a known gamma/pole correction, a removable normalization term, or genuinely source-sensitive arithmetic. That is a separate mathematical question and is the natural stopping boundary for this invocation.