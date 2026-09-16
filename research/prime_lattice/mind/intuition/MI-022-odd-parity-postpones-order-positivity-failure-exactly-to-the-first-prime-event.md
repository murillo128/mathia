# MI-022 — Odd parity postpones order-positivity failure exactly to the first prime event

**Evidence level:** exact-derived and literature-grounded by [PL-324](../../findings/PL-324-odd-sector-first-prime-positivity-threshold.md) from Suzuki's localized Weil form and classical Beurling--Deny theory.

The full localized Weil form loses the standard Beurling--Deny modulus inequality before any rational-prime lag becomes active, so full-space semigroup positivity is not an arithmetic discriminator. The odd sector changes that conclusion sharply.

Identify odd functions on `(-a,a)` with `L^2(0,a)` and use the cone modulus `u#(x)=sgn(x)|u(x)|`. Parity pairs each same-half separation `|x-y|` with the larger opposite-half separation `x+y`. The relevant continuous defect kernel is strictly increasing, so this pairing gives the favorable modulus sign for the **entire archimedean part at every aperture**.

The first obstruction is therefore exactly arithmetic. No prime-power translation has positive-measure overlap while `a <= (1/2)log 2`. Once `a>(1/2)log 2`, some prime-power lag lies in `(a,2a)` and crosses the two halves. Its Weil coefficient gives the opposite modulus sign. A localized two-bump test makes that one-dimensional translation defect order `epsilon` while the favorable continuous interaction is only order `epsilon^2`, so the Beurling--Deny criterion fails immediately.

Hence

`odd-sector semigroup positivity preserving  <=>  0<a<=(1/2)log 2`.

This is valuable because the odd Weil test class is RH-relevant: parity removes the generic archimedean order obstruction and exposes the first rational-prime event as the exact failure point. But the result is still negative for the route. Failure of modulus contraction is not failure of Weil-form positivity and gives no off-critical zero.

The remaining arithmetic gate must therefore preserve the **signed** prime interaction rather than force it through a positive cone. Source-specific eigenstate sign, first-crossing, boundary/flux, or another scalar compatibility law can still be relevant; ordinary positivity-preserving semigroup theory cannot propagate through the first prime event.
