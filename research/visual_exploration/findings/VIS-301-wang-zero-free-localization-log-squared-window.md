# VIS-301 — the classical zero-free region pushes Wang's pointwise localization window to `x=o(H/log^2 T)`

## Claim

Let

`I=(T,T+H]`, `H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and let `F_I(x)` be Biao Wang's short-interval pair-correlation statistic. Suppose

`x=x(T) -> infinity`,

and

`x L^2 / H -> 0`.

Then

`F_I(x) = (H/(2*pi))[log x + (L-log(2*pi))^2/x^2] + o(H)`.

Thus the `x=o(H/L^3)` pointwise range of `VIS-299` is not the true limit of Wang's displayed localization machinery. The classical Vinogradov--Korobov zero-free region suppresses the near-height zero contributions to the interval field and omitted-zero tail strongly enough that the localization cross-coherence isolated in `VIS-300` is `o(H)` throughout the larger range `x=o(H/L^2)`.

At this enlarged scale the first generic `H`-sized term in the current proof is no longer localization. It is the Montgomery--Vaughan mean-value error

`O(x log^2(2x))`

for the Dirichlet polynomial `D_x`, which reaches `H` scale when `x asymp H/L^2`.

**Evidence/status:** `LITERATURE+DERIVED + PROOF-STRUCTURE REFINEMENT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not improve the classical zero-free region, does not improve the Montgomery--Vaughan mean-value theorem, and does not prove an asymptotic at `x asymp H/L^2`.

## 1. Zero-free geometry gives a decaying weight on every near-height zero

Write each non-trivial zero as

`rho=1/2+delta+i gamma`.

Mossinghoff, Trudgian, and Yang prove that for `|gamma|>=3`,

`beta <= 1 - 1/[55.241 (log|gamma|)^(2/3)(log log|gamma|)^(1/3)]`.

For all zeros with `|gamma|<=3T`, monotonicity of the displayed denominator therefore gives, for sufficiently large `T`,

`delta <= 1/2 - eta_T`,

where one may take

`eta_T = 1/[55.241 (log(3T))^(2/3)(log log(3T))^(1/3)]`.

Define

`q_T(x)=x^(-eta_T)`.

Wang's field is

`A(x,t)=sum_rho 2 x^(delta+i(gamma-t)) / [1+((t-gamma)+i delta)^2]`.

Hence every zero with `|gamma|<=3T` contributes an additional factor at most `q_T(x)` relative to the crude `x^delta<=sqrt(x)` bound used in Wang's Lemma 2.4:

`x^delta <= sqrt(x) q_T(x)`.

This is an unconditional suppression. It does not use RH or pair correlation.

## 2. Re-running Wang's localization bounds with the zero-free factor

Let `A_I` be Wang's field restricted to zeros with ordinates in `I`, and put

`R_I=A-A_I`.

Because every zero contributing to `A_I` has ordinate near `T`, the unit-interval zero-count argument used by Wang in (2.14) immediately sharpens to

`|A_I(x,t)| << sqrt(x) q_T(x) L`

for `t in I`.

For `t=T+a in I`, put `b=H-a`. Repeating the proof of Wang's (2.15), but retaining the zero-free factor on the zeros with `|gamma|<=3T`, gives

`|R_I(x,t)|`
` << sqrt(x) q_T(x) L[(1+a)^(-1)+(1+b)^(-1)]`
`    + sqrt(x) L/T`.

The final term is the same far-zero contribution `|gamma|>3T` already isolated in Wang's proof; no uniform `q_T` is needed there.

Similarly, because `A_I` contains only zeros from `I`, Wang's exterior estimate (2.16) sharpens to

`|A_I(x,t)| << sqrt(x) q_T(x) L/[1+dist(t,I)]`

for `t notin I`.

Consequently,

`integral_(R\I) |A_I|^2 dt << x q_T(x)^2 L^2`,

and

`integral_I |R_I|^2 dt`
` << x q_T(x)^2 L^2 + x L^2 H/T^2`.

These are the two pure leakage energies in the exact decomposition of `VIS-300`.

## 3. The inside--outside coherence also becomes negligible before the `L^-2` scale

The only `H`-scale ambiguity left by `VIS-300` was

`C_I(x)=integral_I A_I(x,t) overline(R_I(x,t)) dt`.

Using the two sharpened pointwise bounds above and

`integral_0^H [(1+a)^(-1)+(1+H-a)^(-1)] da << log(2+H) << L`,

one obtains

`|C_I(x)|`
` << x q_T(x)^2 L^3 + x q_T(x) L^2 H/T`.

This already removes the apparent `H/L^3` barrier in the range where the zero-free factor is effective.

To cover the full hypothesis `xL^2/H->0`, split only for the proof. If

`x <= H/L^4`,

then the original localization estimate from `VIS-299` gives

`xL^3 <= H/L = o(H)`.

If instead

`x > H/L^4`,

then

`log x >= theta L - 4 log L`,

so

`eta_T log x >> L^(1/3)/(log L)^(1/3)`.

Therefore

`q_T(x)^2 L -> 0`.

Since `xL^2/H->0`, it follows that

`x q_T(x)^2 L^3 / H`
` = (xL^2/H)[q_T(x)^2 L] -> 0`.

For the far-zero cross contribution,

`x q_T(x) L^2 H/T = o(H)`

because `xL^2/H->0` and `H/T=T^(theta-1)->0`.

The two pure leakage energies are smaller still. Hence the complete localization difference satisfies

`2*pi F_I(x) - integral_I |A(x,t)|^2 dt = o(H)`

throughout every moving range with `x->infinity` and `xL^2/H->0`.

## 4. The interior field already has the required asymptotic in this range

The remaining step is the interior energy

`J_I(x)=integral_I |A(x,t)|^2 dt`.

For the lower subrange `x<=H/L^4`, this is already covered by `VIS-299`. In the complementary range, `x>H/L^4` and `xL^2/H->0` imply `x<T` for large `T`, so the explicit-formula decomposition and frequency-aware estimates of `VIS-298` apply directly.

The arithmetic diagonal from `VIS-291` is

`integral_I |D_x(t)|^2 dt`
` = H log x`
`   + O(H exp(-c V(log x)) + x log^2(2x))`,

with the first error `o(H)` because `x->infinity`. The present hypothesis gives

`x log^2(2x) = O(xL^2)=o(H)`.

The gamma term, the absolutely convergent right-half-plane zeta term, their frequency-aware cross terms, and the explicit-formula remainder remain `o(H)` exactly as in `VIS-298`--`VIS-299`. Thus

`J_I(x)`
` = H log x + H(L-log(2*pi))^2/x^2 + o(H)`.

Combining this with the sharpened localization estimate proves the claim.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the field `A`, the exact full-line energy identity, the unit-interval zero-count localization proof, and the coefficient-square mean-value error. In particular, his equations (2.14)--(2.16) are the bounds sharpened here by retaining the real-part information of the zeros rather than replacing every `x^delta` by `sqrt(x)`.

Michael J. Mossinghoff, Timothy S. Trudgian, and Andrew Yang, **Explicit zero-free regions for the Riemann zeta-function**, *Research in Number Theory* 10, 11 (2024), DOI `10.1007/s40993-023-00498-y`, prove the unconditional explicit Vinogradov--Korobov region used above. No novelty is claimed for that zero-free region or for inserting its bound into Wang's summation argument.

The derived point is narrower: once the classical zero-free information is kept inside Wang's localization proof, the `L^3` localization wall disappears before the existing `xL^2` interior mean-value wall. This does not show that `H/L^2` is an intrinsic transition of `F_I`; it identifies the next unresolved term in the current proof architecture.

## Dependencies

- `VIS-291`: diagonal estimate with explicit `x log^2(2x)` mean-value error and Korobov--Vinogradov arithmetic remainder.
- `VIS-298`: gamma recentering and frequency-aware interior-field decomposition.
- `VIS-299`: pointwise asymptotic through `x=o(H/L^3)`.
- `VIS-300`: exact localization-energy decomposition and identification of `C_I` as the only `H`-scale ambiguity at the old boundary.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose upper branch asks whether the localization coherence is genuinely load-bearing.

## Research consequence

The upper localization branch of the accepted clue is no longer blocked at `x asymp H/L^3`. Classical zero-free geometry alone makes the inside--outside coherence negligible throughout

`x=o(H/L^2)`.

The next pointwise upper-source question is therefore interior rather than geometric: can the `O(x log^2(2x))` mean-value error for Wang's exact Dirichlet-polynomial coefficients be sharpened, evaluated, or shown sharp near `x asymp H/L^2` without assuming the pair-correlation conclusion one is trying to prove?

The separate fixed-power source-specific arithmetic branch remains unchanged.