# VIS-281 — Wang's zero-window localization is power-small on a fixed-source packet

## Claim

Keep the fixed-source regime of `VIS-274`–`VIS-280`: `H=T^theta` with fixed `0<theta<1`, `L=log T`, `I=(T,T+H]`, and

`x=e^(2*pi*q)`

with `q` restricted to a fixed compact set. Then the localization step in Biao Wang's Lemma 2.4,

`2*pi F_I(x) = integral_I |A(x,t)|^2 dt + O(x L^3)`,

is power-small after the fixed-source pullback and pair-statistic normalization.

Indeed, compact `q` makes `x=O_K(1)`, so the localization error is `O_K(L^3)` pointwise. The change of variables

`alpha = 2*pi*q/L`

contributes `d alpha=(2*pi/L)dq`, while the normalized pair statistic contributes a factor proportional to `1/(H L)`. Therefore a bounded fixed-`q` packet sees at most

`O_K(L^3) * O(L^-1) * O((H L)^-1) = O_K(L/H)`.

Since `H=T^theta`,

`L/H = o(L^-m)`

for every fixed `m>0`. In particular, the passage from the interval-restricted zero field `A_I` to the full field `A` cannot generate an intrinsic fixed-source `L^(-3/2)` term, an `L^(-2)` term, or any other fixed negative power of `L`.

**Evidence/status:** `LITERATURE+DERIVED + EXACT REGIME SPECIALIZATION + NEGATIVE/CONTROL + BOTTLENECK LOCALIZATION + NO-NOVELTY-CLAIM`.

No sharpening of Wang's theorem uniformly for `x` growing with `T`, no new zero-density estimate, no secondary coefficient for the full pair statistic, and no RH implication is claimed.

## 1. The localization loss in Wang's proof

Wang defines the full zero field

`A(x,t)=sum_rho 2 x^(delta+i(gamma-t)) / (1+((t-gamma)+i delta)^2)`

and its restriction `A_I(x,t)` to zero ordinates `gamma in I`. Lemma 2.3 gives the exact identity

`2*pi F_I(x)=integral_R |A_I(x,t)|^2 dt`.

Lemma 2.4 then replaces the globally integrated interval-restricted field by the full field integrated only over the physical interval:

`2*pi F_I(x)=integral_I |A(x,t)|^2 dt+O(x L^3)`.

The proof separates two localization effects. For `t in I`, zeros outside `I` give

`|A(x,t)-A_I(x,t)| << sqrt(x) L [1/(1+t-T)+1/(1+T+H-t)]`,

which yields

`integral_I ||A|^2-|A_I|^2| dt << x L^2 log(2+H) << x L^3`.

For `t` outside `I`, the tail of the interval-restricted field satisfies

`integral_(R\I) |A_I(x,t)|^2 dt << x L^2`.

Thus the published `O(x L^3)` term is specifically the cost of replacing the exact short-interval zero field by the full explicit-formula field plus boundary tails.

## 2. Fixed physical source removes this loss from every logarithmic frontier

The theorem-level estimate is uniform up to `x<=T^lambda`, where `x L^3` can become a genuine large-range error. That is not the regime used by the current visual packet.

For `q` in a fixed compact set and `x=e^(2*pi*q)`, both `x` and `sqrt(x)` are bounded independently of `T`. Wang's entire localization loss is therefore only

`O_K(L^3)`.

Let `h(q)` be any fixed bounded packet supported in that compact set. Pulling the error through `alpha=2*pi q/L` gives

`integral h(q) O_K(L^3) (dq/L) = O_(K,h)(L^2)`.

After the ordinary `1/(H L)` pair-statistic normalization, this becomes

`O_(K,h)(L/H)`.

Because `H=T^theta=e^(theta L)`, this is smaller than every inverse power of `L`. The conclusion is insensitive to sign: even the absolute localization envelope is already far below the logarithmic scales under investigation.

## 3. Consequence for the `L^-3/2` audit

`VIS-279` showed that the apparent `L^-3/2` `D_x`–`E_x` cross is an artifact of using a bound uniform for growing `x`; at fixed source it falls to `L^-2`. `VIS-280` then showed that the `D_x`–`B_x` cross is power-small after the same pullback.

The present finding closes a different proof boundary. The `A_I -> A` localization in Lemma 2.4 cannot hide a fixed-source `L^-3/2` mechanism either: its complete published error contributes only `O(L/H)` after the physical-source scaling.

This matters because the `x L^3` term is one of the explicit errors carried into Proposition 2.6 and then integrated in the proof of Theorem 2.2. On a fixed positive-`alpha` band it can matter because `x=T^alpha`; on a fixed physical-`q` packet, `alpha=2*pi q/L` and the same term collapses below every logarithmic order. Treating the theorem-uniform error as though it retained its global size after the source pullback would therefore create another false logarithmic frontier.

The result does not show that the complete fixed-source theorem has no `L^-3/2` term. It removes only this localization boundary. Any surviving mechanism must come from a different theorem-level sector after its exact fixed-source specialization is restored.

## 4. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), Lemmas 2.3 and 2.4, especially equations (2.10)–(2.16). Wang proves the localization estimate itself. His Proposition 2.6 carries it forward as the `x L^3` error term, and the proof of Theorem 2.2 later integrates that error uniformly over `x=T^alpha`, `0<=alpha<=lambda`.

The Mathia-specific step is only to transport Wang's published estimate through the narrower physical-source coordinate already fixed by `VIS-274`: `alpha=2*pi q/L` with compact `q`. No novelty is claimed for the zero-window estimate or its proof.

The argument is deliberately not extended to `q=q(T)` growing with `T`. Once `x=e^(2*pi q)` is no longer uniformly bounded, the factor `x L^3` must be tracked honestly and can re-enter at larger scales. Such a moving-source regime is outside this finding rather than a counterexample to it.

## Dependencies

- `VIS-274`: fixed physical-source coordinate and packet normalization.
- `VIS-279`: fixed-source specialization removes the apparent `L^-3/2` `D_x`–`E_x` floor.
- `VIS-280`: the remaining direct `D_x`–`B_x` cross is power-small.

## Research consequence

The zero-window localization step is excluded as a compulsory source of the fixed-source `L^-3/2` frontier. The next invocation should audit a different theorem-level loss or replacement step rather than refine the `A_I -> A` boundary further.
