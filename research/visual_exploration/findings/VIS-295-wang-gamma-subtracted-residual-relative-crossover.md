# VIS-295 — Wang's gamma-subtracted residual stays relatively linear below the square-root-log H barrier

## Claim

Let

`H=T^theta`, `L=log T`,

with fixed `0<theta<1`, and fix `lambda<theta`. Let the source scale `x=x(T)` satisfy

`x -> infinity`, `1 <= x <= T^lambda`,

and

`x^2 log x / L -> infinity`.

Define Wang's gamma-subtracted residual

`R_gamma(T,x) = F_I(x) - (H/(2*pi)) L^2/x^2`.

Then the error budget already isolated in `VIS-291` and `VIS-294` implies

`R_gamma(T,x) = (H/(2*pi)) log x + o(H log x)`.

Equivalently,

`R_gamma(T,x)/(H log x) -> 1/(2*pi)`.

Thus the `x~sqrt(L)` boundary in `VIS-294` is an **absolute `H`-resolution boundary**, not a leading-order boundary for the gamma-subtracted residual. Relative linearization of that residual persists strictly below `sqrt(L)`, throughout every moving-source regime satisfying `x^2 log x >> L`.

For the illustrative family

`x = sqrt(L)/(log L)^a`,

with fixed `a<1/2`, the condition holds. The propagated theorem budget ceases to force this relative asymptotic at the boundary scale

`x^2 log x ~ L`,

which is of order `sqrt(L/log L)` up to slowly varying factors. This is a boundary of the **current error accounting**, not a claim of an intrinsic transition in pair correlation.

**Evidence/status:** `LITERATURE-SPECIALIZATION + EXACT ERROR-BUDGET EXTRACTION + MOVING-BOUNDARY NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation estimate, prime-number-theorem remainder, zero-free region, lower-boundary asymptotic at `x^2 log x=O(L)`, or RH implication is claimed.

## 1. Start from the retained-gamma error budget

`VIS-294`, using Wang's Proposition 2.6 together with the squared-von-Mangoldt refinement propagated in `VIS-291`, gives on `1<=x<=T^lambda`

`F_I(x)`
` = (H/(2*pi))(L^2/x^2 + log x)`
`   + O(H exp(-c V(log x))`
`       + H L/x^2`
`       + H sqrt(L)/x`
`       + x L^3`
`       + L/sqrt(x))`,

where

`V(y)=y^(3/5)(log y)^(-1/5)`

for sufficiently large `y`, after weakening the positive constant `c` if necessary.

Subtract the explicit gamma contribution. Then

`R_gamma(T,x)`
` = (H/(2*pi)) log x`
`   + O(H exp(-c V(log x))`
`       + H L/x^2`
`       + H sqrt(L)/x`
`       + x L^3`
`       + L/sqrt(x))`.

The question is therefore not whether every error is `o(H)`, which is the criterion used in `VIS-294`, but whether every error is `o(H log x)` relative to the remaining diagonal term.

## 2. Relative normalization pushes the controlled boundary lower

Divide the five error terms by `H log x`.

Because `x->infinity`, the Korobov–Vinogradov term satisfies

`exp(-c V(log x))/log x -> 0`.

The arithmetic source-error term becomes

`L/(x^2 log x) -> 0`

by hypothesis.

The square-root term also vanishes under the same hypothesis. If

`A(T)=x^2 log x/L -> infinity`,

then

`sqrt(L)/(x log x) = 1/(sqrt(A(T)) sqrt(log x)) -> 0`.

For the remaining two terms, the fixed ceiling `x<=T^lambda` with `lambda<theta` gives

`x L^3/(H log x) <= T^(lambda-theta) L^3/log x -> 0`,

while

`L/(H sqrt(x) log x) -> 0`.

Hence the complete propagated remainder is `o(H log x)`, proving

`R_gamma(T,x) = (H/(2*pi)) log x (1+o(1))`.

No cancellation between Wang's error terms is needed for this conclusion.

## 3. The current relative boundary is near sqrt(L/log L)

Take

`x = sqrt(L)/(log L)^a`

with fixed real `a`. Then

`x^2 log x/L = log x/(log L)^(2a)`

and

`log x = (1/2) log L - a log log L`.

Therefore

`x^2 log x/L ~ (1/2)(log L)^(1-2a)`.

For every fixed `a<1/2`, this tends to infinity, so the relative gamma-subtracted asymptotic remains valid even though `x/sqrt(L)->0` when `a>0`.

At `a=1/2`, corresponding to the scale `x` of order `sqrt(L/log L)`, the ratio above remains only constant order. The present `H L/x^2` majorant is then itself of the same order as `H log x`, so Wang's recorded error budget no longer establishes relative linearization of `R_gamma`.

This does **not** show that a new arithmetic phenomenon starts there. It identifies the first lower scale at which the currently propagated estimate loses relative resolving power after the gamma term has been removed.

## 4. The square-root-log scale is still relatively regular

For any fixed `c_0>0`, set

`x=c_0 sqrt(L)`.

Then the condition `x^2 log x/L -> infinity` holds, and more explicitly the retained error budget gives

`R_gamma(T,c_0 sqrt(L))`
` = (H/(2*pi))((1/2)log L + log c_0) + O(H)`.

Consequently

`R_gamma(T,c_0 sqrt(L))/(H log L) -> 1/(4*pi)`.

At the same scale the full statistic is dominated by the explicit gamma term,

`(H/(2*pi)) L^2/x^2 = H L/(2*pi c_0^2)`,

while the gamma-subtracted diagonal term is only order `H log L`. Thus `x~sqrt(L)` has two different meanings depending on the requested resolution:

- at **absolute `H` resolution**, existing `H L/x^2` and `H sqrt(L)/x` errors are already order `H`, exactly as `VIS-294` records;
- at **relative resolution of the gamma-subtracted diagonal**, those same errors are lower order than `H log x`, so the residual still linearizes.

Confusing these two normalizations would make the lower source boundary look earlier than the present theorem actually forces.

## 5. Prior art and evidence boundary

The pair-correlation statistic, coefficient decomposition, and error terms used here come from Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), especially the source decomposition summarized in the preceding Wang findings and Proposition 2.6 as used there.

The Korobov–Vinogradov input for the squared-von-Mangoldt coefficient sum is the classical/current PNT-scale input already audited in `VIS-291`; this finding introduces no stronger arithmetic estimate. Its contribution is only to renormalize the already-persisted complete error budget by the gamma-subtracted diagonal scale `H log x` and identify the resulting moving-source domain.

No novelty is claimed for the underlying estimates or for the elementary comparison of their sizes. In particular, `x^2 log x ~ L` is not proved to be sharp, intrinsic, or visible in the true pair-correlation statistic. A better estimate for the `H L/x^2` contribution, cancellation among Wang's decomposed terms, or a more source-specific arithmetic analysis could move the boundary again.

The accepted clue `CLUE-wang-fixed-source-packet-localization` therefore remains open at its stated **absolute `H`-resolution** lower branch. This finding narrows only the interpretation: merely entering `x=O(sqrt(L))` is not enough to destroy the leading gamma-subtracted diagonal law.

## Dependencies

- `VIS-287`: complete-statistic fixed-power source linearization.
- `VIS-289`: removal of the coarse bare-`H` diagonal floor.
- `VIS-291`: Korobov–Vinogradov envelope for the squared-von-Mangoldt source term.
- `VIS-293`: analytic-cost boundary for half-plane control of the source Dirichlet series.
- `VIS-294`: retained-gamma moving-source estimate and the absolute `H`-resolution square-root-log boundary.
- `CLUE-wang-fixed-source-packet-localization`: accepted source-localization clue whose absolute lower-boundary branch remains live.

## Research consequence

The lower moving-source frontier now splits cleanly by resolution. For absolute `H`-scale secondary structure, `x=O(sqrt(L))` remains the first unresolved region in the current theorem. For the **relative gamma-subtracted profile**, however, the existing estimates already control a much larger sub-square-root region: all `x->infinity` with

`x^2 log x >> L`.

A genuinely new lower-boundary mechanism at that relative scale must therefore reach the regime `x^2 log x=O(L)` or sharpen the `H L/x^2` term enough to push the boundary still lower. That is the next natural quantitative test; extending further within `x^2 log x>>L` would only reparameterize an asymptotic already forced by the existing Wang error budget.