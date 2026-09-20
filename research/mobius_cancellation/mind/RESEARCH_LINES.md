# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Price any factor-lift escape after projecting to the arithmetic source state

**Linked intuitions:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`, `MI-074-thin-hyperbolic-shells-tax-independent-coordinate-bandwidth`, `MI-075-exact-product-tangent-fibers-have-subpolynomial-state-volume`, `MI-076-fixed-depth-factor-lifts-cannot-amplify-the-short-shell-state-exponent`, `MI-077-factor-multiplicity-does-not-survive-a-mobius-sign-projection`.

MC-423--MC-424 show that fixed-depth exact-product fibers and whole short factor shells cannot manufacture an additional polynomial state exponent. MC-425 then applies the source projection at arbitrary active depth: retaining each factor only through its Möbius sign leaves fewer than `2^omega(n)=X^(o(1))` source-sign words even when depth reaches its arithmetic maximum.

MC-426 closes a much wider retained-data class. Suppose every prime contributes a uniformly bounded vector `a(p) in Z^m`, with fixed `m` and fixed bound `B`, and each factor is retained only through the additive summary `S(u)=sum_(p|u)a(p)`. Across every ordered active factorization and every depth, the total number of summary words is

`exp(O_(B,m)(omega(n))) = X^(o(1))`.

For fixed `B`, polynomial state volume `X^delta` already requires retained dimension `m=Omega_(B,delta)(log log X)`. Thus exact block counts, fixed lists of prime-class incidences and other fixed-dimensional bounded additive summaries do not rescue the factor-lift bandwidth. The sign-only obstruction is one coarse instance of a broader conservation-of-additive-mass collapse.

The live question is consequently not whether more factor labels can be generated, nor whether a slightly richer fixed-dimensional additive statistic can be attached to them. A viable factor lift must identify source information that escapes the MC-426 hypotheses—growing dimension, unbounded or increasingly precise weights, exact prime/factor identities, growing-modulus residue or character data, or genuinely non-additive relations—and then show that this extra information actually drives cancellation after coefficient, shell and closure costs are paid. Alternatively, leverage must come from analytic organization inside a subpolynomial retained family rather than from crediting discarded tuple multiplicity.

## Audit state count, retained source information and closure faces in the same coordinates

Scalar filter banks, positive Toeplitz forms and operator-valued channels stay inside the earlier closure obstructions unless they introduce a genuinely new arithmetic variable. MC-423--MC-426 show that tangent dimension, raw factor multiplicity, Möbius-sign words and fixed-dimensional bounded additive summaries are not independent bandwidth currencies.

Any proposed escape should remove unit padding, quotient parameter labels to physical arithmetic states, project those states to the exact datum consumed by the mechanism, and only then count independent channels. If the retained datum is a fixed-dimensional bounded additive prime-local statistic, the entire all-depth factorization family is still subpolynomial. A polynomial-capacity claim must identify exactly which boundedness, dimensionality, additivity or source-projection hypothesis fails and why the replacement datum is canonical and cancellation-relevant.