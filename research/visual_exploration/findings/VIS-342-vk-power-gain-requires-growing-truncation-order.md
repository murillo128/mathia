# VIS-342 — changing the Vinogradov–Korobov power class requires polynomially growing scalar truncation order

## Claim

Keep the scalar Vinogradov–Korobov optimization model from `VIS-341`. Let

`nu(t)=A (log t)^(-2/3)(log log t)^(-1/3)`

for sufficiently large `t`, let `u=log x`, and allow the polynomial truncation/smoothing order to depend on `u`:

`Omega_r(u)=inf_(t>=t0) {u nu(t)+r(u) log t}`.

Write `w=u/r(u)`. Then there is an exact scaling identity

`Omega_r(u)=r(u) Omega_1(w)`,

where

`Omega_1(w)=inf_(t>=t0) {w nu(t)+log t}`.

Consequently, whenever `w=u/r(u)->infinity`, the fixed-order asymptotic from `VIS-341` immediately gives

`Omega_r(u) ~ C_A u^(3/5) r(u)^(2/5) [log(u/r(u))]^(-1/5)`,

with the same constant `C_A` as in `VIS-341`.

Two regimes follow.

If `r(u)=u^{o(1)}`, then

`Omega_r(u)=u^(3/5+o(1)) (log u)^(-1/5)`

up to the explicit subpower contribution `r(u)^(2/5)`. Thus subpolynomial growth of the scalar truncation order does not produce a fixed improvement in the `u`-power exponent.

If

`r(u)=u^(alpha+o(1))`

for a fixed `0<=alpha<1`, then

`Omega_r(u) ~ C_A (1-alpha)^(-1/5) u^((3+2alpha)/5+o(1)) (log u)^(-1/5)`.

Therefore, **within this scalar zero-free-width/truncation model, changing the Vinogradov–Korobov power class by a fixed positive amount requires polynomial growth of the effective truncation/smoothing order in `u=log x`**. More precisely, a target exponent `3/5+delta` with fixed `0<delta<2/5` requires

`r(u)=u^(5 delta/2+o(1))`.

This is a conditional classification of the scalar optimization model, not a theorem that every multiscale packet or Wang-type transform admits such an effective scalar order.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ZERO-FREE-OPTIMIZATION CONTEXT + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

## 1. Exact rescaling

For every positive `r=r(u)`, factor `r` from the objective:

`u nu(t)+r log t = r[(u/r) nu(t)+log t]`.

Since `r` is constant with respect to the minimization variable `t`, taking the infimum gives exactly

`Omega_r(u)=r Omega_1(u/r)`.

No saddle-point approximation is needed for this step. It also makes the relevant large parameter explicit: once the truncation order is allowed to grow, the asymptotic regime is governed by `u/r`, not by `u` alone.

## 2. Variable-order Vinogradov–Korobov asymptotic

`VIS-341` established, for a large argument `z`,

`Omega_1(z) ~ C_A z^(3/5)(log z)^(-1/5)`.

Apply this with `z=u/r(u)`. If `u/r(u)->infinity`, then

`Omega_r(u)`
` = r(u) Omega_1(u/r(u))`
` ~ C_A r(u) [u/r(u)]^(3/5) [log(u/r(u))]^(-1/5)`
` = C_A u^(3/5) r(u)^(2/5) [log(u/r(u))]^(-1/5)`.

The formula is uniform only to the extent justified by the one-variable asymptotic after substitution; no claim is made here for the transition regime `u/r=O(1)`.

## 3. Subpolynomial order cannot change the power class

Suppose `log r(u)=o(log u)`. Then

`r(u)^(2/5)=u^{o(1)}`

and

`log(u/r(u))=(1+o(1)) log u`.

Hence

`Omega_r(u)=C_A u^(3/5+o(1))(log u)^(-1/5)`.

A polylogarithmic order illustrates the boundary. If `r(u)=(log u)^beta`, then

`Omega_r(u) ~ C_A u^(3/5)(log u)^((2 beta-1)/5)`

up to the negligible replacement of `log(u/r)` by `log u`. The logarithmic factor changes, but the `u^(3/5)` power does not.

Thus an argument that merely accumulates a slowly growing number of scalar inverse-frequency powers cannot by itself claim a new fixed `u`-power exponent through this optimization.

## 4. Polynomial order changes the class exactly

Suppose

`r(u)=u^(alpha+o(1))`, `0<=alpha<1`.

Then

`r(u)^(2/5)=u^(2 alpha/5+o(1))`

and

`log(u/r(u))=(1-alpha+o(1)) log u`.

Substitution yields

`Omega_r(u) ~ C_A (1-alpha)^(-1/5) u^((3+2alpha)/5+o(1))(log u)^(-1/5)`.

If one asks for a fixed power gain `delta` over `3/5`, then

`(3+2alpha)/5 = 3/5+delta`

forces

`alpha=5 delta/2`.

So the scalar mechanism pays for a genuine power-class improvement with polynomially growing effective order. As `alpha` approaches `1`, the assumption `u/r->infinity` approaches its boundary and this asymptotic no longer describes the `r` comparable to `u` transition.

## 5. Consequence for the Wang packet clue

The accepted Wang packet clue asks whether a localized or multiscale construction can exploit nonstationary source structure without merely repackaging the classical Vinogradov–Korobov balance.

`VIS-341` ruled out a fixed finite scalar-order explanation. The present result sharpens that gate: even an unbounded scalar order is insufficient to change the power class if it grows only subpolynomially in `u`. A fixed positive power improvement through the same scalar objective would require an effective order growing like a positive power of `u`.

This does **not** show that a Wang packet has an effective scalar order, nor that a multiscale signed construction must pay the same absolute truncation cost. It supplies a falsification control. Any proposed packet gain should either:

- certify polynomial growth of a genuinely relevant effective scalar order while keeping leakage and all destination terms under control; or
- exhibit a non-scalar signed/arithmetic mechanism for which reduction to `u nu(t)+r log t` is mathematically invalid.

Merely adding finitely many, logarithmically many, or other subpolynomially many scalar smoothing powers cannot count as a new Vinogradov–Korobov power class.

## Prior-art audit

The zero-free-width input and classical prime-number-theorem optimization context are the same as in `VIS-341`, including the Bellotti–Wong explicit Vinogradov–Korobov zero-free region and Johnston's analysis of the corresponding prime-number-theorem error-term barrier. This finding does not claim a new zero-free region, a new prime-number-theorem estimate, or a literature-level asymptotic theorem.

The new statement here is an elementary rescaling and regime classification of the already-recorded scalar optimization functional when its truncation exponent is allowed to vary with `u`. Its role in Mathia is diagnostic: it quantifies how fast an effective scalar order would have to grow before the power exponent can change.

## Status

The exact scaling identity and its consequences above are established within the stated scalar model. No claim is made that Wang's transform, an arbitrary multiscale packet, or a signed arithmetic localization admits such a scalar `r(u)` description. No improved bound for primes, zeta zeros, `theta(x)-x`, or Wang's final error term is proved.