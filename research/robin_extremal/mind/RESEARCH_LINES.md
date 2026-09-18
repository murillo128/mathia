# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable Robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the scalar Euler frontier between exact identification and selector-scale stable rigidity

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-051-finite-laplace-source-capacity-grows-only-logarithmically-with-the-transform-rectangle-at-fixed-precision`.

The matched-control program has progressively removed apparent scalar rigidity thresholds. Ordinary-prime `{0,1,2}` controls can preserve every fixed KV source envelope and an order-one transient Robin excursion while matching exact Mertens/Euler data at fixed depth, growing depth and separated temperatures. RE-188 optimizes the deep Euler-jet repair to a linear-width Chebyshev window and keeps non-rigidity throughout

`K=o((log p)^(5/3)(loglog p)^(1/3))`.

RE-189 supplies a qualitatively different upper-scale obstruction. For a prime factor with `L=log q`, the factorial-normalized `j`th boundary derivative equals a universal `1` plus nonzero pole modes of size roughly `exp(-c j/L^2)`. Once `j` reaches the log-squared scale, primes in a fixed multiplicative selector window become exponentially indistinguishable to these normalized jets. A finite packet is seen primarily through net multiplicity; zero-net-multiplicity packets have exponentially small normalized response.

RE-190 closes the shrinking-boundary loophole. For a packet supported on a fixed multiplicative selector shell `q~p`, the entire exact Euler profile sampled at `s=1+tau/log p` with `|tau|=o(log p)` becomes, after trivial normalization, operator-norm close to the single reciprocal-mass functional `sum c_q/q`. Dense sampling in an `o(1)` neighborhood is asymptotically rank one at the natural weighted source scale.

RE-191 shows that moving a fixed constant distance into `Re s>1` does not restore a large robust source rank either. On `s=1+u`, `0<=u<=U`, the exact Euler channel reduces uniformly on the selector shell to a compact finite-Laplace kernel plus `O(p^-1)`, and its rank-`m` approximation error is bounded by `e^(UM)(UM)^m/m!+O(p^-1)`. A whole exact interval is analytically source-rigid, but at fixed precision its stable source rank remains bounded independently of `p` and of the number of available shell primes.

RE-192 identifies the dimensionless resource behind both spectral collapses. For a packet supported on `[Q_-,Q_+]`, the lower-edge-normalized Euler channel on `1<=s<=1+U` has rank-`m` error at most

`[U log(Q_+/Q_-)]^m/m! + O(Q_-^-1)`.

Thus spectral span and logarithmic source width trade through `R=U log(Q_+/Q_-)`. RE-193 sharpens the large-`R` side: for tolerance `epsilon` above the prime-power floor, a dyadic decomposition gives separated rank

`O((1+log(1+R))(1+log(1/epsilon)))`.

RE-194 converts the canonical selector's shrinking absolute debt `d_p~1/(sqrt(p)log p)` into the relative tolerance `epsilon_Rob~min(1,d_p/V)`, with `V=sum |c_q|/q`, producing the worst-case capacity upper bound

`O((1+log(1+R))(1+log_+(V/d_p)))`.

RE-195 closes the tempting converse interpretation of that formula. Reciprocal variation is **not a coercive source-complexity resource** under the current matched-control class. For every fixed jet depth `K` and every prescribed finite `Lambda_p`, one can append a finite remote `{+1,-1}` prime packet beginning at `p^2` with reciprocal variation at least `Lambda_p`, while greedy Chebyshev sign balancing keeps its signed primitive `O(log x)`. Abel summation then makes its complete fixed Euler profile `O_U(p^-2)` on every fixed `1<=s<=1+U` and its fixed boundary jets `O_j((log p)^j/p^2)=o(d_p)`. Using a disjoint prime-index parity channel, the exact RE-182 repair still matches every fixed jet through depth `K`, preserves `{0,1,2}` multiplicities, the KV envelope and the order-one transient selector excursion.

RE-196 closes the natural “observe the whole positive real Euler ray” escape at every fixed logarithmic precision depth. The RE-182 repair has bounded centered logarithmic transport moments at selector scale. After factoring the common decay `p^{-(s-1)}`, exact matching of the first `K` boundary jets makes the normalized discrepancy vanish to order `K+1`; the remaining Taylor term is suppressed globally by

`sup_(u>=0) u^(K+1) p^(-u) ~ (log p)^(-(K+1))`.

At the same time the Chebyshev-balanced padding used in RE-195 is uniformly `O(p^-2)` for **all** real `s>=1`, independently of its arbitrarily large reciprocal variation. Consequently, for every fixed `K`, the matched control can satisfy

`sup_(s>=1)|D_Q(s)| <<_K d_p/(log p)^(K+1)`

while retaining exact jets through order `K`, KV fidelity, an order-one transient Robin excursion and arbitrarily large reciprocal variation. For every fixed `A`, choosing fixed `K>A` makes the entire real Euler profile `o(d_p/(log p)^A)`.

RE-197 makes this precision collapse uniform at growing depth for the fixed-width microstep repair. If `K log log p=o(log p)`, the canonical RE-186 ordinary-prime `{0,1,2}` control satisfies

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1)) K log log p)`

while retaining exact jet matching, KV fidelity and the order-one pre-repair Robin transient. The complete positive real Euler ray is therefore near-null at superlogarithmic precision throughout the whole fixed-width subcritical regime.

RE-198 pushes the same full-ray conclusion through the linear-width RE-188 geometry. Writing `L=log p`, for every growing `K=o(L)` the matched control obeys

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1)) K log(L/K))`.

The mechanism is the first omitted centered Laplace moment: RE-188 pays spatial radius `W~K`, producing `(CK)^(K+1)`, while selector damping contributes `L^(-(K+1))`. Thus the previous `L/log L` precision boundary was not intrinsic. The full real ray remains stably noncoercive through **every sublinear jet depth**. The first unresolved continuum transition now begins at `K~L`, where repair radius and selector damping compete at order one.

Thus exact continuum identification and selector-scale stable discrimination remain sharply separated. RE-174 is still valid at infinite precision: exact values on an unbounded temperature set identify the source. RE-196--RE-198 show that the inverse has no Robin-scale modulus along increasingly deep ordinary-prime matched directions, now through all `K=o(log p)`. Enlarging the positive real spectral window, inflating reciprocal variation, or increasing real sampling density does not restore scalar coercivity at any tolerance above the RE-198 scale.

The scalar frontier is consequently narrower. Exact jet repair itself survives much deeper, through the RE-188 range `K=o((log p)^(5/3)(loglog p)^(1/3))`, while RE-189 identifies a different high-order common-mode collapse near `K~(log p)^2`. Between `K~log p` and those larger scales, the current absolute-moment argument no longer controls the whole real ray. A future scalar rigidity argument therefore needs signed control of the first omitted moment, a repair representation with smaller effective centered radius, a **coercive signed/quotiented source complexity** that survives balanced directions, or it must leave the one-sided scalar Euler channel for a joint/nonlocal invariant tied directly to Robin.

## Control one-sided reciprocal escape independently

The zero-side packet obstruction remains separate. One-sided vertical phase geometry can hide a scale-maximal target along lacunary stages while fixed-order typical local-correlation statistics remain unchanged. Closing that branch still needs target-conditioned exceptional geometry rather than average-center statistics.

## Keep exact identification, stable information and destination leverage distinct

Finite ordinary-prime rigidity, full exact Euler-germ identification, fixed/growing jet matching, KV fidelity, weighted reset complexity, repair width, high-order jet saturation, shrinking-window rank-one collapse, fixed-window factorial compression, spectral-logwidth compression, dyadic logarithmic compression, full-real-ray fixed and growing-depth suppression, Robin-scale precision conversion, reciprocal total variation, Chebyshev-balanced signed response and transient Robin displacement answer different questions. RE-198 makes the current separation explicit: an analytically injective full real continuum can remain uniformly almost blind through every matched depth `K=o(log p)` while the Robin destination coordinate changes by order one.

Future proposals should therefore state the surviving source ambiguity, exact invariant family, optimized repair width, source-fidelity cost, integer-multiplicity constraints, normalization, inverse conditioning, spectral/source diameter, **source-visible signed complexity rather than only unsigned reciprocal variation**, precision scale and selector-normalized destination effect. A scalar family should be credited as Robin leverage only after matched repair, high-depth common-mode collapse, shrinking-window low-rank collapse, finite-Laplace compression, balanced-padding invisibility and full-real-ray near-nullity at the actual physical parameters are ruled out.