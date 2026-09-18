# MI-068 — Iterated q-van der Corput has an intrinsic log-log source horizon

**Evidence level:** exact method-level synthesis from [MC-382](../../findings/MC-382-iterated-q-vdc-has-an-intrinsic-loglog-source-horizon.md), interpreted against the common-source endpoint bounds MC-377--MC-381.

MC-381 raises the exact-endpoint common-radical obstruction to a linear-in-rank law until an analytic `log log y` ceiling takes over. MC-382 identifies why the current terminal character-sum architecture naturally stops there rather than merely failing to optimize a pruning constant.

Write the source modulus scale as `q=y^a`, with the interval length `N~y`. In the iterated q-van der Corput factorization used by the current frame argument, every nontrivial preliminary factor must remain below the interval scale, while a generic square-root terminal estimate can absorb at most a terminal modulus of order `N^(2+o(1))`. Consequently reaching source exponent `a` requires differencing depth

`k >= a-2-o(1)`.

The q-vdC iteration converts the terminal saving into an exponent of order `2^(-k)`. Even granting an ideal square-root terminal estimate, the power-saving exponent available to the source frame is therefore bounded at the scale

`sigma(a) <= 2^(-a+O(1))`.

The endpoint contradiction needs this saving to remain asymptotically visible, in particular `sigma(a) log y -> infinity`. Hence repacking the same factorization can only support

`a <= O(log log y)`

up to constant-factor changes. The `log log y` ceiling in the current source-cost theorem is thus tied to an **exponential differencing-depth tax**, not to the earlier square-root rank loss or to tiny-prime deletion.

The reusable proof-design lesson is that removing combinatorial waste does not automatically move an analytic ceiling. Once the source exponent itself forces a linearly growing number of differencing stages and each stage halves the terminal saving exponent, constant-factor improvements to factor packing cannot change the asymptotic source horizon. Beating it requires a different terminal estimate, a collective estimate that sees several factors at once, or a different source-to-destination mechanism that avoids the depth cascade.

**Boundary.** This is an obstruction to the present q-vdC/character-sum architecture, not a theorem that Möbius cancellation cannot access source moduli beyond `y^(O(log log y))`. It does not rule out other character-sum methods, multilinear estimates, spectral input or a different endpoint representation, and it does not itself imply a bound for `M(x)`.