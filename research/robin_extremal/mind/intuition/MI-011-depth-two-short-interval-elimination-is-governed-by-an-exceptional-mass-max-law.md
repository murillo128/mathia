# MI-011 — Depth-two short-interval elimination is governed by an exceptional-mass max law

**Evidence level:** exact transfer law through RE-094 for the residual mixed first/depth-two CA cells. The comparison with current Gafni--Tao and almost-all short-interval technology calibrates what is presently provable; it is not a lower bound for the true exceptional set.

**Representation.** Work on a bounded-ratio physical shell `Y_C asymp X` and a compact false-RH fan exponent interval `J=[b_0,b_1]`. A residual depth-two boundary is indexed by an ordinary prime `q asymp X^(1/2)` and is sampled at the exact cross-layer point `x_q=eta_1^(-1)(eta_2(q))~q^2/2`. Let an ambient short-interval PNT theorem at length `H=X^vartheta` have exceptional-start measure `X^(m(vartheta)+o(1))`.

RE-094 proves that the total threshold measure of the mixed first/depth-two cells obeys

`sum_C |I_C| << X^(b_1+vartheta-1/2+o(1)) + X^(b_1-1+m(vartheta)+o(1))`.

The two terms come from different resources: the first pays the `X^(1/2)` sparse depth-two host count times the short interval length, while the second pays the ambient exceptional set through the CA threshold-capacity factor. Vanishing therefore requires simultaneously

`vartheta < 1/2 - b_1` and `m(vartheta) < 1 - b_1`.

At the false-RH exponent level this becomes the sharp information-splice condition

`Theta > max(1/2 + vartheta, m(vartheta))`,

and the best frontier obtainable from an ambient exceptional profile is `beta_exc(m)=inf_vartheta max(1/2+vartheta,m(vartheta))`.

This identifies the missing resource at the current depth-two barrier. To improve `Theta=173/200` by this route, one needs some `vartheta<73/200` with **power-law exceptional exponent** `m(vartheta)<173/200`. Merely proving primes in much shorter intervals for almost all starts is not enough if the exceptional set is only logarithmically sparse: `X(log X)^(-B)=X^(1+o(1))` behaves as `m=1` and can still contain every `X^(1/2+o(1))` prime-indexed depth-two host.

Current general Gafni--Tao zero-density/additive-energy majorants do not certify the required inequality just below `173/200`; RE-094 exhibits an admissible zero-density parameter whose resulting majorant remains above the target. This is a **technology boundary**, not evidence that the true prime exceptional set is that large.

The escape is correspondingly source-specific. A theorem conditioned directly on `q` prime and the quadratic sample `x_q`, or one retaining the CA rightmost-maximizer or standard/reciprocal prime-race state, need not pay ambient exceptional measure and can bypass the max law. The key distinction is therefore not “shorter interval versus longer interval” but **ambient exceptional mass versus sparsely sampled source-conditioned control**.

**Boundary.** The max law is sufficient for this particular host-count + chamber-length + one-variable exceptional-measure splice. It does not prove `173/200` intrinsic, constrain source-conditioned sampled-gap theorems, or replace the separate `469/600` reduction for deeper mixed layers.