# MI-018 — Fixed algebraic CA-height corrections are governed by near-edge zero geometry, while CA placement resolves the signed packet

**Evidence level:** exact in the attained finite-edge branch through [RE-120](../../findings/RE-120-isolated-finite-zero-edges-determine-every-algebraic-ca-height-correction.md), [RE-121](../../findings/RE-121-spectral-boundary-mass-flatness-replaces-horizontal-isolation-in-ca-height-closure.md), [RE-122](../../findings/RE-122-algebraic-ca-anomalies-require-polynomial-height-zero-edge-approach.md), and [RE-123](../../findings/RE-123-regular-ca-phases-resolve-the-full-subedge-packet-superalgebraically.md). The required height-approach and signed-cancellation laws are not known for zeta zeros; no claim is made for a non-attained edge or the `Theta=1` branch.

RE-119 shows that regular CA states sample the leading edge profile with phase mesh finer than every inverse power of `nu=log log C`. RE-120 then proves under a fixed horizontal gap below an attained edge that every fixed algebraic correction is already a deterministic stable-filter descendant of that same profile.

RE-121 identifies exactly what the horizontal gap was buying. Retaining the complete high strip gives an edge hierarchy plus a damped subedge correction. If `W(t)` is the weighted mass of subedge zeros within horizontal distance `t`, its positive Laplace--Stieltjes envelope satisfies, for every fixed `A>0`,

`W(t)=O(t^A)  <=>  L(u)=O(u^-A)`.

Thus superpolynomial boundary-mass flatness preserves every fixed algebraic edge-only correction even when real parts accumulate at the edge.

RE-122 makes that condition geometric. Let `H(t)` be the least ordinate of a subedge zero within horizontal distance `t` of the attained edge and define `kappa_H=liminf log H(t)/log(1/t)`. Riemann--von Mangoldt yields `W(t) << log(eH(t))/H(t)`, so the order-`K` residual is `o(nu^-A)` for every `A<min(kappa_H,K+1)`. Conversely, an actual residual `>=c nu^-A` forces a subedge zero within horizontal distance `O(log nu/nu)` at ordinate `O(nu^A log nu)`. **A finite-edge anomaly therefore needs polynomial-height spectral approach, not merely accumulation at the edge.**

RE-123 shows that arithmetic placement of regular CA states does not add another fixed-order obstruction after that approach condition. The full signed subedge packet has coefficients of reciprocal-square size. At accuracy `u^-A`, the ordinate tail above a polynomial cutoff is already `o(u^-A)`, while the derivative of the retained packet is only polylogarithmic. Since adjacent regular-CA phases are separated by `O(e^(-u/2)u^(3/2))`, the actual CA phase set samples the entire packet with error smaller than every prescribed inverse power.

Therefore a continuum signed excursion of fixed algebraic size cannot hide between CA states. The remaining signed gate is **internal spectral cancellation**, not selector sparsity: polynomial-height near-edge zeros may still cancel each other or carry too little weighted mass, but if their complete packet produces an algebraic excursion, regular CA placement transmits it to the destination at the same scale.

The reusable separation is now three resources. Positive boundary mass determines whether subedge information can be algebraically visible; height approach prices access to that mass; signed zero correlation determines whether the visible packet survives cancellation. Regular CA placement is already superalgebraically fine relative to every fixed algebraic order and is no longer an independent resource in this branch.

**Boundary.** The height estimate is one-way through a positive envelope, and RE-123 does not prove any nonzero signed excursion. Its argument is fixed-order: the auxiliary spectral cutoff may grow polynomially for each requested accuracy, but no all-orders expansion with `K` growing with `u` is asserted. The nonattained-edge and `Theta=1` branches remain outside this synthesis.