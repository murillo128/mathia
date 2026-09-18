# VIS-294 — Wang's lower moving-source regime is controlled above the square-root-log crossover

## Claim

Let `H=T^theta`, `L=log T`, with fixed `0<theta<1`, and fix once and for all `lambda<theta`. Let `x=x(T)` satisfy

`x/sqrt(L) -> infinity`

and

`1 <= x <= T^lambda`

for all sufficiently large `T`. Then Biao Wang's short-interval pair-correlation statistic satisfies

`F_I(x) = (H/(2*pi))(L^2/x^2 + log x) + o(H)`.

More quantitatively, with

`V(y)=y^(3/5)(log y)^(-1/5)`

for sufficiently large `y`, the argument of `VIS-291` extends before the fixed-power specialization to

`F_I(x) = (H/(2*pi))(L^2/x^2 + log x)`
`       + O(H exp(-c V(log x))`
`           + H L/x^2`
`           + H sqrt(L)/x`
`           + x L^3`
`           + L/sqrt(x))`

for some fixed `c>0`, uniformly in the displayed source range once `x` is sufficiently large.

Thus a moving exponent `beta(T)=log x/log T -> 0` is not by itself a new lower-boundary regime. After the explicit gamma term `H L^2/(2*pi x^2)` is retained, Wang's existing theorem plus standard prime-number-theorem input already controls the complete statistic to `o(H)` throughout every lower-source family with `x >> sqrt(log T)` and `x<=T^lambda` for one fixed `lambda<theta`.

In particular, for every fixed `epsilon>0`, the choice

`x=(log T)^(1/2+epsilon)`

lies in this controlled moving-boundary corridor even though `beta(T)->0`.

If one subtracts the gamma term as well and asks for

`F_I(x)-(H/(2*pi))log x=o(H)`,

the sufficient lower condition becomes `x/L -> infinity`. The distinction is structural: `x~sqrt(L)` is where Wang's **remaining theorem errors** first reach `H` scale, while `x~L` is where the explicit gamma main term itself falls to `H` scale.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT ERROR-BUDGET EXTRACTION + MOVING-BOUNDARY NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation estimate, PNT remainder, zero-free region, RH implication, or theorem at the actual `x=O(sqrt(L))` crossover is claimed.

## 1. Keep Wang's explicit gamma term instead of hiding it in the residual

Wang's Proposition 2.6, as recorded in `VIS-287`, is uniform for `1<=x<=T^lambda` with fixed `lambda<theta` and gives

`F_I(x)`
` = (H/(2*pi))(L^2/x^2 + log x)`
`   + O(H + H L/x^2 + H sqrt(L)/x + x L^3 + L/sqrt(x))`.

The term `H L^2/(2*pi x^2)` is explicit. Near the lower source boundary it should therefore be retained as part of the known baseline rather than misidentified as an unexplained residual.

`VIS-289`--`VIS-291` remove the coarse bare `O(H)` floor by evaluating Wang's squared-von-Mangoldt coefficient sum more sharply. Before setting `x=T^beta`, the same calculation gives

`S(x)=log x+O(exp(-c V(log x)))`

as `x->infinity`, and hence replaces the coarse `H` contribution by

`O(H exp(-c V(log x)))`.

Combining this with the other explicit errors of Proposition 2.6 yields the quantitative formula in the claim.

## 2. The lower moving family is still controlled when `x >> sqrt(L)`

Divide every remainder by `H`. Under `x/sqrt(L)->infinity`,

`L/x^2 -> 0`

and

`sqrt(L)/x -> 0`.

Because `x->infinity`, also

`exp(-c V(log x)) -> 0`.

The localization term is harmless under one fixed theorem ceiling:

`x L^3/H <= T^(lambda-theta) L^3 -> 0`.

Finally,

`L/(H sqrt(x)) -> 0`

trivially. Therefore every non-main term is `o(H)`, proving

`F_I(x)=(H/(2*pi))(L^2/x^2+log x)+o(H)`.

This argument is genuinely moving-source: it allows `beta(T)=log x/L` to tend to zero. What stays fixed is only Wang's theorem parameter `lambda<theta`, not a positive lower exponent bound.

## 3. The square-root-log crossover is the first unresolved `H`-scale lower boundary

The two source-dependent errors most relevant near the lower boundary are

`H L/x^2`

and

`H sqrt(L)/x`.

Both become order `H` when `x` is of order `sqrt(L)`. Thus the existing theorem stops giving an `o(H)` remainder precisely at that scale, even after the explicit gamma term is retained.

This is different from the gamma crossover. The explicit term

`H L^2/(2*pi x^2)`

is order `H` when `x` is of order `L`, but it is known exactly and can be retained or subtracted. Between `sqrt(L)` and `L`, that gamma contribution may be much larger than `H`, while the **unknown** remainder is nevertheless `o(H)`.

Accordingly, a visual or asymptotic effect obtained merely by choosing a vanishing exponent with, say, `x=L^(3/4)` is not evidence of a new source mechanism. It lies inside a regime already explained to `H` accuracy by Wang's two explicit main terms.

## 4. Relation to the accepted packet-localization clue

`CLUE-wang-fixed-source-packet-localization` left `beta(T)->0` as one possible escape from the compact fixed-power panel. The present extraction narrows that escape substantially.

A lower-boundary investigation that aims to reveal genuinely new `H`-scale information must now enter `x=O(sqrt(L))`, or else change the target scale below `H` and reprice every remainder accordingly. Merely allowing `beta(T)` to vanish is insufficient.

The theorem-ceiling branch remains separate. Nothing here lets Wang's fixed `lambda<theta` drift toward `theta`; near-ceiling source families still require a new uniformity argument.

## 5. Prior art and evidence boundary

The complete source-uniform pair-correlation formula is Biao Wang's Proposition 2.6 in **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026). The squared-von-Mangoldt refinement uses only the standard Korobov--Vinogradov-scale prime-number-theorem input already audited and propagated in `VIS-291`.

No novelty is claimed for either ingredient. The Mathia-specific content is the explicit moving-boundary regime extraction from the already-recorded error budget: keeping the gamma term visible shows that the current theorem remains `o(H)`-accurate all the way down to sources satisfying `x >> sqrt(log T)`.

The finding does not control `x=O(sqrt(L))`, does not identify an actual secondary term there, and does not show that the crossover is intrinsic rather than an artifact of Wang's present error bounds. It only establishes that no genuinely uncontrolled `H`-scale lower-boundary regime begins earlier.

## Dependencies

- `VIS-287`: Wang's complete source-uniform Proposition 2.6 error budget.
- `VIS-289`--`VIS-291`: replacement of the coarse `O(H)` arithmetic floor by the standard PNT/Korobov--Vinogradov envelope.
- `VIS-293`: excludes treating RH-equivalent source holomorphy as a cheaper fixed-power escape.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose lower moving-boundary branch is narrowed here.

## Research consequence

The lower moving-source frontier should no longer be described merely as `beta(T)->0`. At `H` resolution and with the explicit gamma baseline retained, the unresolved region begins only when

`x=O(sqrt(log T))`.

A useful next lower-boundary test must therefore work at or below that crossover and rederive or sharpen the `H sqrt(L)/x` and `H L/x^2` terms rather than extrapolating fixed-power intuition.