# VIS-299 — Wang's pointwise source asymptotic extends to `x=o(H/log^3 T)`

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`. Let `x=x(T)` satisfy

`x -> infinity`,

and

`x L^3 / H -> 0`.

Then Biao Wang's short-interval pair-correlation statistic satisfies

`F_I(x) = (H/(2*pi)) [log x + (L-log(2*pi))^2/x^2] + o(H)`.

Thus the fixed exponent ceiling `x<=T^lambda`, `lambda<theta`, used in `VIS-298` is not the actual pointwise ceiling of the displayed Wang estimates. After re-running the localization proof rather than substituting a moving `lambda` into a fixed-parameter theorem, the same gamma-recentered asymptotic remains valid throughout the much larger moving range

`x=o(H/L^3)`.

For a power representation `x=T^beta(T)`, this condition is exactly

`(theta-beta(T))L - 3 log L -> +infinity`.

In particular, every family

`x = H/L^(3+epsilon)`

with fixed `epsilon>0` is admissible, even though its effective exponent approaches `theta`.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT-DERIVED MOVING-BOUNDARY REFINEMENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not prove a moving-support version of Wang's Theorem 2.2, does not control the boundary `x asymp H/L^3`, and does not improve the prime-number-theorem input governing the fixed-power arithmetic residual.

## 1. Re-run the localization estimate instead of moving a fixed theorem parameter

Wang states Lemma 2.4 uniformly for `1<=x<=T^lambda` with fixed `lambda<theta`, obtaining

`2*pi F_I(x) = integral_I |A(x,t)|^2 dt + O(x L^3)`.

The fixed-parameter statement by itself cannot be used with `lambda=lambda(T)`. The proof, however, exposes the dependence needed here. Its load-bearing estimates are the zero-count bound on unit intervals together with

`|A(x,t)|+|A_I(x,t)| << sqrt(x) L`,

`|A(x,t)-A_I(x,t)|`
` << sqrt(x)L[(1+t-T)^(-1)+(1+T+H-t)^(-1)]`,

and the analogous off-interval decay for `A_I`. The resulting comparison error is explicitly `O(xL^3)`; no denominator involving `theta-lambda` is introduced in the displayed proof.

Under `xL^3=o(H)` one has `x<T` for all sufficiently large `T`, because `H=T^theta` with `theta<1`. Therefore the same argument may be re-run directly at the chosen moving `x(T)`, giving

`2*pi F_I(x) = integral_I |A(x,t)|^2 dt + o(H)`.

This is a proof-level reinspection of Lemma 2.4, not an appeal to uniformity that Wang did not state.

## 2. The arithmetic diagonal remains `H log x+o(H)`

`VIS-291` derives the stronger coefficient-square estimate

`integral_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c V(log x)) + x log^2(2x))`,

where `V(y)=y^(3/5)(log y)^(-1/5)` for sufficiently large `y`.

Because `x->infinity`, the first error is `o(H)`. Since `x<T` eventually, `log(2x)=O(L)`, and the moving-ceiling assumption gives

`x log^2(2x) = O(xL^2) = o(H)`.

Hence

`integral_I |D_x(t)|^2 dt = H log x + o(H)`

throughout the entire range `xL^3=o(H)`. No fixed positive lower or upper source exponent is needed for this step.

## 3. The exact gamma-recentered pieces stay negligible at absolute `H` resolution

`VIS-298` rewrites Wang's explicit formula as

`A(x,t) = -D_x(t) + x^(-1)[G(t)+Z(t)] + R_x(t)`,

with

`G(t)=-chi'/chi(-1/2+it)`,

`Z(t)=zeta'/zeta(3/2-it)`,

and the pole/trivial-zero remainder

`R_x(t)=O(x^(1/2)/T^2+x^(-5/2)/T)`.

The same estimates used there remain uniform for the present range because `x<T` eventually. On `I`,

`G(t)=L-log(2*pi)+O(H/T+1/T)`,

so

`x^(-2) integral_I |G(t)|^2 dt`
` = H(L-log(2*pi))^2/x^2 + o(H)`.

The absolutely convergent right-half-plane series gives

`x^(-2) integral_I |Z(t)|^2 dt = O(H/x^2)=o(H)`.

The frequency-aware cross-term bounds from `VIS-298` are

`x^(-1)|integral_I D_x overline(G)| << L/sqrt(x)`,

`x^(-1)|integral_I D_x overline(Z)| << x^(-1/2)`,

and

`x^(-2)|integral_I G overline(Z)| << L/x^2`.

All are `o(H)`. The square of `R_x` and its cross terms are also `o(H)` because `x<T`, `H<=T`, and `x->infinity`. Therefore

`integral_I |A(x,t)|^2 dt`
` = H log x + H(L-log(2*pi))^2/x^2 + o(H)`.

Combining this with the re-run localization estimate proves the claim.

## 4. The fixed exponent gap collapses to an explicit logarithmic localization layer

Write `x=T^beta(T)`. Then

`xL^3/H = exp(-(theta-beta(T))L + 3 log L)`.

Consequently `xL^3/H->0` is equivalent to

`(theta-beta(T))L - 3 log L -> +infinity`.

The pointwise statistic therefore permits the source exponent to approach `theta`; the gap need not remain fixed. For example,

`beta(T)=theta-(3+epsilon)log L/L`

gives `x=H/L^(3+epsilon)` and lies in the proved range.

This identifies a much narrower unresolved upper layer. At

`x asymp H/L^3`,

Wang's current localization comparison contributes only `O(H)`, so the present argument no longer yields an absolute-`H` asymptotic. That is a limitation of the localization step, not evidence that the statistic changes regime there. A further advance must sharpen or structurally evaluate the localization tails rather than merely improve the already-controlled interior source decomposition.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), states the pair-correlation machinery with fixed `0<lambda<theta<1`. Lemma 2.4 gives the `O(xL^3)` localization error, Lemma 2.5 gives coefficient estimates uniform for `x>=1`, and Proposition 2.6 assembles the fixed-parameter pointwise estimate. The present result does not silently let Wang's `lambda` drift: it re-runs the displayed localization proof at the selected moving `x(T)` and combines it with the exact decomposition already persisted in `VIS-298`.

Baluyot, Goldston, Suriajaya, and Turnage-Butterbaugh's unconditional Montgomery framework supplies the underlying explicit formula used by Wang and unpacked in the preceding visual findings. No external novelty claim is made for any of these ingredients or for the elementary conversion between `xL^3=o(H)` and the moving exponent condition.

The result is only about the pointwise statistic `F_I(x)`. It does **not** establish Wang's integrated Theorem 2.2 for a test function whose support moves with `T`; such a statement would require separate control of the test family and its implied constants. It also does not show that `H/L^3` is an intrinsic barrier, only that the currently displayed localization error reaches order `H` there.

## Dependencies

- `VIS-291`: Korobov–Vinogradov-scale diagonal estimate with explicit `x log^2(2x)` mean-value error.
- `VIS-298`: exact gamma recentering and frequency-aware control of all non-diagonal pieces.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose upper-ceiling branch is narrowed here.

## Research consequence

Do not treat a fixed exponent gap `lambda<theta` as the remaining upper-source obstruction for Wang's **pointwise** statistic. The existing argument already reaches every moving source with `x=o(H/L^3)`.

The live upper-ceiling question is now localized to the `xL^3/H` layer: can the comparison between the full zero statistic and the interval-restricted explicit-formula energy be sharpened, recombined, or evaluated when `x` approaches `H/L^3` and beyond? The separate fixed-power arithmetic question remains unchanged.