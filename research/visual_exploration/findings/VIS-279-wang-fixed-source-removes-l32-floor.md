# VIS-279 — fixed-source Wang scaling removes the apparent `L^-3/2` D–E floor

## Claim

Keep the short-interval notation used in `VIS-274`–`VIS-278`: `H=T^theta` with fixed `0<theta<1`, `I=(T,T+H]`, `L=log T`, and Wang's decomposition

`A(x,t)=-D_x(t)+B_x(t)+E_x(t)`.

In the fixed-source packet regime

`x=e^(2*pi*q)`,

with `q` restricted to a fixed compact set, the `D_x`–`E_x` cross term does **not** force an `L^(-3/2)` contribution to the normalized pair statistic.

Wang's exact mean-square identity in the proof of Proposition 2.6 is

`integral_I |D_x(t)|^2 dt = H log x + O(H + x log^2(2x)).`

For `x` in a fixed compact `K subset (0,infinity)`, this is simply

`||D_x||_2 = O_K(sqrt(H)).`

Together with Wang's bound

`||E_x||_2 = O_K(sqrt(H)/x)`,

Cauchy–Schwarz gives

`|integral_I D_x(t) overline(E_x(t)) dt| = O_K(H/x).`

Under the fixed-`q` change of variables `d alpha=(2*pi/L)dq` and the pair-statistic normalization `2*pi/(H L)`, this contributes only

`O_K(L^(-2))`.

The larger `L^(-3/2)` scale appears only if one first replaces Wang's exact fixed-`x` identity by the theorem-level uniform bound `||D_x||_2 << sqrt(H L)`, which is designed to remain valid while `x` ranges up to a power of `T`. That loss is unnecessary on a compact fixed-source packet.

Moreover, before absolute-value majorization the cross term is signed:

`-2 Re integral_I D_x(t) overline(E_x(t)) dt`,

because `A=-D+B+E`. Cauchy–Schwarz discards this sign but does not reveal a genuine `L^(-3/2)` mechanism.

**Evidence/status:** `LITERATURE+DERIVED + EXACT REGIME SHARPENING + NEGATIVE/CONTROL + BOTTLENECK LOCALIZATION + NO-NOVELTY-CLAIM`.

No improved global version of Wang's theorem, new pair-correlation asymptotic, new estimate uniform for growing `x`, secondary `L^-2` coefficient, or RH implication is claimed.

## 1. Where the apparent `L^-3/2` scale enters

Wang proves Proposition 2.6 uniformly for a source parameter as large as `x<=T^lambda`. In that global regime the exact identity above is safely coarsened to

`||D_x||_2 << sqrt(H L)`.

His estimate for the explicit-formula remainder gives, in the fixed-source notation used by the visual branch,

`||E_x||_2 << sqrt(H)/x`.

Applying Cauchy–Schwarz after the global coarsening yields

`|<D_x,E_x>| << H sqrt(L)/x`.

The fixed-`q` packet contributes one further factor `1/L` from `d alpha`, while the pair-statistic normalization contributes `1/(H L)`. Therefore a cross-term bound of size `H sqrt(L)` becomes a theorem-level contribution of order

`L^(-3/2)`.

This is a valid uniform error estimate for Wang's theorem. It is not, however, evidence that the fixed-source packet contains an intrinsic term of that size.

## 2. The exact `D_x` identity is one power of `sqrt(L)` sharper on compact source windows

In the proof of Proposition 2.6, Wang obtains

`integral_I |D_x(t)|^2 dt = H log x + O(H + x log^2(2x)).`

Let `q` range in a fixed compact set and write `x=e^(2*pi*q)`. Then `x`, `1/x`, `log x`, and `log(2x)` are all uniformly bounded by constants depending only on that compact set. Since `H->infinity`, the identity reduces uniformly to

`integral_I |D_x(t)|^2 dt = O_K(H)`

and hence

`||D_x||_2 = O_K(sqrt(H)).`

This sharpening uses no new analytic estimate. It is the direct specialization of Wang's own exact mean square before the proof enlarges the source range and replaces it by a uniform theorem-level bound.

Combining it with

`||E_x||_2 = O_K(sqrt(H)/x)`

gives

`|<D_x,E_x>| <= ||D_x||_2 ||E_x||_2 = O_K(H/x).`

Thus the `sqrt(L)` responsible for the apparent `L^-3/2` packet scale disappears completely in the fixed-source regime.

## 3. Fixed-`q` normalization moves the D–E sector to `L^-2`

For the compact-source packet used throughout `VIS-274`–`VIS-278`, the source coordinate is

`alpha = 2*pi*q/L`,

so

`d alpha = (2*pi/L) dq`.

The normalized pair statistic carries an additional factor proportional to `1/(H L)`. Consequently a uniformly `O_K(H)` signed or absolute D–E integral contributes at most

`O_K(H) * O(L^-1) * O((H L)^-1) = O_K(L^-2)`.

The constants coming from the compact `q` support and the factor `x^-1=e^(-2*pi*q)` remain bounded and do not change the logarithmic order.

This does **not** identify the actual `L^-2` coefficient. The signed integral may be smaller, may oscillate, or may combine with other `L^-2` sectors. The result is only an upper-scale localization: the D–E interaction cannot be the compulsory source of an `L^-3/2` term once the source packet is fixed before `T->infinity`.

## 4. The pre-bound cross term retains sign

Expanding

`|A|^2 = |-D+B+E|^2`

shows that the D–E interaction appears exactly as

`-2 Re(D overline(E))`.

After integration over `I`, the relevant quantity is therefore

`-2 Re integral_I D_x(t) overline(E_x(t)) dt`.

The Cauchy–Schwarz step replaces this signed quantity by a positive majorant. That replacement is appropriate for a robust theorem-level error bound but erases any cancellation specific to the fixed-source packet.

Accordingly, a future attempt to extract a secondary coefficient should return to this signed integral rather than interpret the Cauchy–Schwarz envelope as an observed asymptotic term. Such an extraction is a separate research question and is not needed for the present negative control.

## 5. Consequence for the current visual frontier

`VIS-278` showed that the standalone gamma-normalized `|B_x+E_x|^2` source energy appears only at `L^-2`; its residual energy is the classical prime-power constant `C_Lambda`. The remaining apparent `L^-3/2` candidate was therefore naturally pushed toward a cross interaction involving a non-source sector.

The D–E interaction was the first obvious candidate because Wang's global proof bounds it at precisely the larger scale after normalization. The compact-source audit above closes that candidate at the level needed by this branch: its `L^-3/2` size is **bound-induced**, coming from a uniform-in-growing-`x` simplification that is not sharp for fixed `q`.

This narrows the live question again. Any genuine `L^-3/2` mechanism in the fixed-source packet must come from another term, another coupling, or another global-to-local loss that survives after every exact compact-source specialization is restored. It is not enough that the published theorem groups a contribution into an `O(L^-3/2)` remainder.

That next search is an independent research thread and is intentionally left for a later invocation.

## 6. Prior art and novelty boundary

The source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), Proposition 2.6 and its proof, especially equation (2.19). Wang's argument supplies both the exact `D_x` mean-square identity and the larger-range theorem-level simplification used here.

This finding does not improve Wang's stated uniform theorem and makes no novelty claim about the underlying mean-square estimate. Its contribution is only to audit that proof under Mathia's narrower fixed-source representation and to distinguish a bound-induced logarithmic loss from an intrinsic secondary scale.

The specialization is consistent with `VIS-274`–`VIS-278`, which deliberately keep `q` in a fixed compact packet before taking `T->infinity`. Allowing `q=q(T)` or `x=x(T)` to grow restores the need to track the full `H log x + x log^2(2x)` dependence and can recover larger error scales.

No confirmation-zero data, numerical fitting, or visual salience is used in this result.

## Dependencies

- `VIS-274`: fixed-source Wang scaling and packet normalization.
- `VIS-275`–`VIS-277`: source-term reconstruction and normalization audit.
- `VIS-278`: gamma-normalized combined-source energy is only `L^-2`, motivating the search for the apparent larger cross-sector remainder.

## Research consequence

The first non-source candidate for the fixed-packet `L^-3/2` frontier is eliminated: Wang's D–E term is `O(L^-2)` after the exact compact-source mean square is retained. The next invocation should inspect a different interaction or proof-loss boundary rather than refining this one further.