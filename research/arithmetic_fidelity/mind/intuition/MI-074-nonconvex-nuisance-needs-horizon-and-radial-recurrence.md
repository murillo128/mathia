# MI-074 — Nonconvex nuisance fidelity needs horizon slope plus radial recurrence

**Evidence level:** exact finite-dimensional asymptotic synthesis from [AF-493](../../findings/AF-493-nonconvex-nuisance-horizon-scaling-vs-recession.md), extending the convex recession decomposition of MI-073 without importing its convex conclusion into the nonconvex setting.

For a nonempty closed set `C` in a finite-dimensional normed space with `0 in C`, define the discriminator-ray profile

`d_C(t;s)=dist(t s,C)`

and the horizon/scaling cone

`C^infty={h : c_n/t_n -> h for some c_n in C, t_n -> infinity}`.

AF-493 proves the exact first-order law

`liminf_(t->infinity) d_C(t;s)/t = dist(s,C^infty)`.

Thus the convex recession-space test has a precise nonconvex replacement at linear scale. If `s` lies outside `C^infty`, the discriminator eventually escapes at a positive linear rate, so every fixed deterministic noise radius permits only bounded target ambiguity. Translation recession alone is insufficient outside convexity: sparse or recurrent aliases can have trivial translation recession while filling many asymptotic directions.

The converse needs a second datum. Membership `s in C^infty` says only that separation is sublinear along some unbounded sequence. It does **not** say that the absolute separation stays bounded. AF-493 exhibits both extremes: `C=Z` has exact aliases at arbitrarily large depth, while the sparse curved set `{0} union {+-(n,sqrt(n))}` has `e_1 in C^infty` but `d_C(t;e_1)->infinity`, so every fixed noise radius still has finite ambiguity.

The resulting nonconvex fidelity ledger is therefore two-scale. **The horizon cone decides whether linear-rate escape is unavoidable; the full radial distance profile decides whether sublinear recurrence is close enough to create fixed-noise aliases.** For convex symmetric nuisance these layers collapse to the recession quotient plus bounded residual geometry of MI-073, but that collapse is a convex regularity theorem rather than a generic property of nuisance sets.

This sharpens the arithmetic question. An arithmetic source restriction matters only after asking whether its nuisance difference set changes the horizon seen by the rational-prime discriminator; if the discriminator remains in that horizon, one must then estimate the actual recurrence distances rather than infer non-identifiability from normalized asymptotics alone.

**Boundary.** The liminf identity uses finite-dimensional compactness. It does not classify infinite-dimensional nuisance, and at zero noise one must distinguish an actual difference set from its closure. Neither horizon exclusion nor radial recurrence supplies rational-prime provenance: AF-493 contains no prime-specific estimate and no RH consequence.