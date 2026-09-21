# MI-046 — Cross-scale divisibility, not low location, drives exact-omission amplification

**Evidence level:** exact divisor-poset synthesis from [FD-247](../../findings/FD-247-primitive-increment-support-gives-sharp-linear-exact-omission-cost.md), strengthening the location profile in FD-246. Primitive/divisibility-antichain language is classical; the line-specific content is the exact omission consequence.

Let `g=Delta Y` be the active response-increment support. If its nonzero indices form a divisibility antichain, divisor inversion is diagonal on those active coordinates: `b_d=g(d)` for every active `d`. The envelope `|b_n|<=Cn` then gives

`sum_(n<=N)|b_n| <= C N |supp(g)| <= 2 C N K`

for `K` exact omissions.

Any omission set contained in one multiplicative octave `(M,2M]` has this property automatically, regardless of how low `M` lies. Thus `K=o(N)` omissions in one octave remain macroscopically coercive with the sharp normalized `K/N` cost. Moving a sublinear defect downward is not enough to recover the worse reciprocal-divisor behavior.

The new durable parameter is the **divisibility incidence geometry of the active increments**, not absolute location alone. Large harmonic footprint can be harmless when the active support is primitive. Any exact-omission family that genuinely amplifies beyond linear `NK` must create cross-scale divisibility chains or a denser incidence pattern in `supp(Delta Y)`.

**Boundary.** This remains a signed exact-response theorem. It does not settle approximate residuals or physical positivity/capacity/coherence, and it does not yet quantify how the norm grows with a general divisibility-poset incidence profile. That incidence-conditioned inverse norm is the remaining response-side object.