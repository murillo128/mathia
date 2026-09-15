# MI-025 — The current zero-count rank budget caps the fully visible geometric base alphabet

**Evidence level:** exact source-envelope/sample-budget obstruction from [NB-135](../../findings/NB-135-current-zero-count-budget-caps-fully-visible-geometric-annihilators-to-a-finite-base-alphabet.md), closing the naive growing-base escape left by [NB-134](../../findings/NB-134-fixed-multibase-visibility-still-permits-simultaneous-superpolynomial-annihilator-collapse.md)

In the NB-132 polynomial-height regime, a genuine right-half zero packet in a fixed ordinate window `W` at height at most `R^A` has the explicit rank allowance

`d(F) <= C_(A,W) log R + 0.24460 log log R + O_(A,W)(1)`,

with

`C_(A,W)=A(W/(4*pi)+0.10076)`.

A `q`-geometric trace inside the natural prefix `1,...,R` contains only `log_q R+O(1)` samples. The full order-`d(F)` recurrence is therefore uniformly certified by the current source bound only when

`C_(A,W) < 1/log q`.

For fixed `A,W` this leaves a finite base alphabet

`q < exp(1/C_(A,W))`.

Shrinking the fixed ordinate width does not make that alphabet unbounded: the explicit endpoint error leaves the limiting cap

`q < exp(1/(0.10076 A))`.

This closes the simplest response to NB-134. NB-134 already shows that every fixed finite family of fully visible scalar geometric annihilators can collapse simultaneously in a matched formal packet. NB-135 shows that the same zero-count gate cannot supply an unbounded sequence of *additional* bases on which a separate full recurrence remains visible. Growing the number of scalar views eventually outruns the available recurrence depth.

The resource mismatch is exact: the current source rank budget is `Theta(log R)`, while per-base sample depth is `(log R)/(log q)`. A successful growing representation must therefore obtain more conditioned information per unit of zero-count rank rather than merely add more independently scalarized clocks. Plausible escape classes are a stronger actual-zero law with `d(F)=o(log R)`, joint use of many partial traces before annihilation, natural-grid phase information, or a different height regime.

**Boundary.** Failure of the inequality is a limitation of the present source certificate, not a theorem that actual zeta zeros have maximal allowed rank or that a large base contains no useful information. The result only caps separately certified **full** scalar recurrences under the current polynomial-height zero-count envelope; partial/joint representations and stronger source laws remain open.