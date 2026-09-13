# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit source-conditioned prime/selector rigidity beyond the `173/200` ambient frontier

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps`, `MI-002-ordinary-sigma-rejects-composite-substitute-atoms-at-every-fixed-ca-layer`, `MI-003-fixed-threshold-cells-freeze-prime-source-data`, `MI-004-higher-layer-ca-switches-carry-quantized-residual-charge`, `MI-005-matched-first-layer-packets-conserve-the-endpoint-prime-multiset`, `MI-006-first-layer-timing-is-large-in-transport-but-summable-in-robin-metric`, `MI-007-matched-packets-convert-selector-dilation-into-chebyshev-underdensity`, `MI-008-reciprocal-mertens-recovery-forces-corrected-chebyshev-growth`, `MI-009-smooth-dilation-front-is-not-the-obstruction`, `MI-010-deep-support-boundaries-have-vanishing-threshold-measure`, `MI-011-depth-two-short-interval-elimination-is-governed-by-an-exceptional-mass-max-law`.

RE-076--RE-085 reconstruct the late selector geometry and remove bounded fixed-order mixed-event mass as a leading escape. RE-086 turns selection of a fixed-layer event as an adjacent support boundary into an anchored ordinary-prime-gap cost, while RE-087 shows that summing marginal one-sided gap capacity over all candidate primes is too generous to contradict the CA amplitude.

RE-088 removes sufficiently deep selected boundaries: under a positive off-RH exponent gap, some finite depth cutoff makes all deeper layers threshold-negligible. The challenged RE-089 formulation has been withdrawn. RE-090 uses Järviniemi's `0.57+epsilon` aggregate length bound for square-root-sized consecutive-prime gaps to make every fixed same-depth higher-layer chamber family threshold-negligible whenever `Theta>0.57`, leaving first-layer contact or finite mixed-depth higher-layer configurations.

RE-091 removes that purely higher-layer mixed-depth residual once the false-RH frontier is farther right. A selected cell touching depth `3` or deeper has only `X^(1/3+o(1))` possible boundary hosts, while its first-layer inverse image lies in an ordinary prime gap. Cauchy--Schwarz with Stadlmann's mean-square prime-gap bound `sum d_n^2 << X^(1.23+epsilon)` gives the depth-`r` physical-mass exponent

`beta_r=(1/2)(1.23+1/r)`.

For `r=3` this is `469/600`. Above that threshold every depth-`>=3` boundary family is negligible; together with RE-090, every surviving cell has a first-layer atom on at least one boundary outside threshold measure `o(1)`.

RE-092 stress-tests the tempting next step: use the fact that a mixed `1/r` cell forces **two** anchored ordinary-prime gaps, one at scale `X` and one at the host scale `X^(1/r)`. A full-width matched control shows that, under the same host-count and separate gap-moment information, the host-layer gap lower bound becomes asymptotically below the deterministic gap floor while the first-layer gaps saturate exactly the RE-091 exponent. Thus paired gap **magnitudes** do not improve `beta_r`; the Cauchy--Schwarz frontier is sharp for this scalar information package.

For the surviving depth-2 channel this gives the explicit scalar barrier `beta_2=173/200`. Hence throughout `469/600<Theta<=173/200`, merely imposing both gap-size inequalities on the same cell cannot force the opposite boundary to become first-layer. For `Theta>173/200`, the existing RE-091 depth-2 host/moment estimate itself makes that channel negligible.

RE-093 then inserts the exact analytic incidence omitted by RE-092. For a depth-2 source label `q`, set `x_q=eta_1^{-1}(eta_2(q))`; then `x_q~q^2/2` and consecutive integer host labels give sample spacing `gg sqrt(X)`. A PNT-dense **integer-label common source** can be surgically arranged so that `eta_1(p_q)` and `eta_2(q)` are adjacent events of the complete generalized event staircase, with the correct one-sided first-layer hole at `x_q`, while the total first-layer gap-square cost remains `X^(3/2-2b+o(1))`. This still fits the Stadlmann `1.23` budget exactly for `b>=27/200`, i.e. through `Theta<=173/200`.

RE-094 gives the exact ambient exceptional-set splice for those quadratic sample points. If a short-interval PNT at length `H=X^vartheta` has bad-start measure `X^(m(vartheta)+o(1))`, then the residual mixed first/depth-two threshold measure is

`<< X^(b_1+vartheta-1/2+o(1)) + X^(b_1-1+m(vartheta)+o(1))`.

Thus this route works only when `vartheta<1/2-b_1` and `m(vartheta)<1-b_1`, or at exponent level `Theta>max(1/2+vartheta,m(vartheta))`. To improve the existing `173/200` frontier one therefore needs some `vartheta<73/200` with a genuine power-saving exceptional exponent `m(vartheta)<173/200`. Current general Gafni--Tao majorants do not certify that inequality near the frontier, while almost-all prime interval results with exceptional size `X(log X)^(-B)` still have polynomial exponent `m=1` and are noncoercive for this sparse host family.

Thus exact cross-scale identity, common-source membership, orientation, full generalized event adjacency and present ambient almost-all short-interval technology all fail to improve the `173/200` frontier. The live theorem in `469/600<Theta<=173/200` must now use a source-conditioned input absent from those controls: ordinary primality at the sampled points `x_q`, a short-interval/gap theorem conditioned on `q` prime, the standard/reciprocal prime-race coupling, accumulated CA height, skipped-span effects, or rightmost-maximizer compatibility. Such a theorem can evade the ambient exceptional-mass max law because it need not control all starts in `[X,2X]`.

Below `469/600`, the finite mixed-depth reduction from RE-088--RE-090 remains the correct weaker frontier.

## Keep event mass, selected-boundary depth, gap moments, incidence geometry, ambient exceptional mass and genuine source arithmetic separate

RE-085 says high layers carry vanishing normalized event mass; RE-088 says sufficiently deep selected boundaries occupy vanishing threshold measure; RE-090 says fixed same-depth higher-layer chambers also occupy vanishing threshold measure above `Theta>0.57`; RE-091 combines sparse hosts with an ordinary-prime-gap second moment to force one-sided first-layer boundary contact above `Theta>469/600`; RE-092 proves that adding the opposite anchored-gap **size** does not strengthen that scalar package before the corresponding `beta_r` threshold.

RE-093 sharpens the separation: even the deterministic pairing `q -> eta_1^{-1}(eta_2(q))`, same-source integer labels, orientation and complete generalized staircase adjacency can coexist with the same moment budget up to `173/200`. RE-094 then separates interval length from exceptional-set mass: an ambient almost-all theorem helps only if its power-law bad-set exponent beats the sparse-host/capacity max law; logarithmic density-zero exceptional sets may still contain every prime-indexed quadratic host. The remaining obstruction is which **ordinary-prime** gap occurs at those analytic sample points under the actual CA selector, together with arithmetic/selection information that ambient integer-start controls cannot reproduce. The `469/600` and `173/200` numbers remain information-class frontiers for the present host-count/gap-moment/ambient-exceptional-set methods, not intrinsic phase transitions of the CA mechanism.