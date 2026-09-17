# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable Robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the scalar Euler frontier between repairability and stable-rank collapse

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-051-finite-laplace-source-capacity-grows-only-logarithmically-with-the-transform-rectangle-at-fixed-precision`.

The matched-control program has progressively removed apparent scalar rigidity thresholds. Ordinary-prime `{0,1,2}` controls can preserve every fixed KV source envelope and an order-one transient Robin excursion while matching exact Mertens/Euler data at fixed depth, growing depth and separated temperatures. RE-188 optimizes the deep Euler-jet repair to a linear-width Chebyshev window and keeps non-rigidity throughout

`K=o((log p)^(5/3)(loglog p)^(1/3))`.

RE-189 supplies a qualitatively different upper-scale obstruction. For a prime factor with `L=log q`, the factorial-normalized `j`th boundary derivative equals a universal `1` plus nonzero pole modes of size roughly `exp(-c j/L^2)`. Once `j` reaches the log-squared scale, primes in a fixed multiplicative selector window become exponentially indistinguishable to these normalized jets. A finite packet is seen primarily through net multiplicity; zero-net-multiplicity packets have exponentially small normalized response.

RE-190 closes the shrinking-boundary loophole. For a packet supported on a fixed multiplicative selector shell `q~p`, the entire exact Euler profile sampled at `s=1+tau/log p` with `|tau|=o(log p)` becomes, after trivial normalization, operator-norm close to the single reciprocal-mass functional `sum c_q/q`. Dense sampling in an `o(1)` neighborhood is asymptotically rank one at the natural weighted source scale.

RE-191 now shows that moving a **fixed constant distance** into `Re s>1` does not restore a large robust source rank either. On `s=1+u`, `0<=u<=U`, the exact Euler channel reduces uniformly on the selector shell to a compact finite-Laplace kernel plus `O(p^-1)`, and its rank-`m` approximation error is bounded by `e^(UM)(UM)^m/m!+O(p^-1)`. A whole exact interval is analytically source-rigid, but at fixed precision its stable source rank remains bounded independently of `p` and of the number of available shell primes.

RE-192 identifies the dimensionless resource behind both spectral collapses. For a packet supported on `[Q_-,Q_+]`, the lower-edge-normalized Euler channel on `1<=s<=1+U` has rank-`m` error at most

`[U log(Q_+/Q_-)]^m/m! + O(Q_-^-1)`.

Thus spectral span and logarithmic source width trade exactly through the product `R=U log(Q_+/Q_-)`. This closes a mixed loophole left by the earlier statements: even polynomially separated support `p^A<=q<=p^B` remains factorially compressible if it is observed only in a `T/log p` boundary window, because then `R=T(B-A)=O(1)`. Logarithmically separated source scales are therefore not by themselves a growing-rank resource; they matter only when the accompanying spectral span makes `R` grow.

RE-193 sharpens the large-`R` side of that statement. A dyadic decomposition of the positive finite-Laplace kernel shows that, for every tolerance `epsilon` above the prime-power floor, the exact Euler channel has a separated approximation of rank

`O((1+log(1+R))(1+log(1/epsilon)))`.

The reason is geometric: source coordinates at logarithmic distance `x` only matter outside the exponentially small tail when the spectral coordinate is `u=O(1/x)`, so each dyadic source scale costs only `O(log(1/epsilon))` directions. Consequently fixed `U>0` with polynomial support `p^A<=q<=p^B` has only `O_epsilon(loglog p)` stable scalar dimension at fixed precision, despite `R=Theta(log p)`. Merely making `R_p` diverge is therefore a much weaker resource than RE-192's global Taylor bound suggested.

RE-194 resolves the previously unspecified precision conversion for the canonical selector mechanism. Its absolute Euler/Mertens signal is the selector debt `d_p~1/(sqrt(p)log p)`, but the relevant **relative** tolerance is not a `p`-only scale: for source reciprocal variation `V=sum |c_q|/q`, Robin-scale resolution is `epsilon_Rob~min(1,d_p/V)`. Inserting that into RE-193 gives the precision-aware capacity

`O((1+log(1+R))(1+log_+(V/d_p)))`,

provided the explicit prime-power remainder `V/Q_-` is below `d_p`. The original selector packet itself has `V=(1+o(1))d_p`, so it is a fixed-relative-size signal despite its shrinking absolute magnitude. Likewise, a local `{0,1,2}` repair changing only `O(p d_p)=O(sqrt(p)/log p)` primes at scale `p` has `V=O(d_p)` and receives no shrinking-precision bonus. Any attempt to exploit the `log(1/epsilon)` factor must therefore inflate reciprocal source variation beyond the selector scale; `epsilon_p` is not an independent scalar resource.

The scalar frontier is now variation-dependent rather than tolerance-dependent. The open derivative region remains the intermediate window between constructive repair and `j~(log p)^2` saturation. On the spectral side, a claim of `K` robust independent Euler coordinates at selector-scale absolute resolution can evade the RE-193/194 upper bound only by making `R` sufficiently large or by inflating `V/d_p` roughly exponentially in `K/(1+log(1+R))`. The next useful scalar test is therefore whether honest `{0,1,2}` matched controls can generate that much reciprocal variation while preserving a fixed KV envelope, exact matching and the transient Robin excursion. If variation inflation remains cheap, the scalar route is still non-rigid; if source fidelity or selector combinatorics cap it, the precision loophole closes. Otherwise the investigation should move to a joint/nonlocal invariant tied directly to Robin rather than enlarge the Euler rectangle again.

## Control one-sided reciprocal escape independently

The zero-side packet obstruction remains separate. One-sided vertical phase geometry can hide a scale-maximal target along lacunary stages while fixed-order typical local-correlation statistics remain unchanged. Closing that branch still needs target-conditioned exceptional geometry rather than average-center statistics.

## Keep exact identification, stable information and destination leverage distinct

Finite ordinary-prime rigidity, full exact Euler-germ identification, fixed/growing jet matching, KV fidelity, weighted reset complexity, repair width, high-order jet saturation, shrinking-window rank-one collapse, fixed-window factorial compression, spectral-logwidth compression, dyadic logarithmic compression, Robin-scale precision conversion and transient Robin displacement answer different questions. RE-194 sharpens the distinction further: the absolute destination-relevant scale can shrink while the relative source resolution stays fixed, and any apparent precision gain must be charged to reciprocal source variation.

Future proposals should therefore state the surviving source ambiguity, exact invariant family, optimized repair width, source-fidelity cost, integer-multiplicity constraints, normalization, inverse conditioning, spectral/source diameter, reciprocal variation budget, precision scale and selector-normalized destination effect. A scalar family should be credited as Robin leverage only after matched repair, high-depth common-mode collapse, shrinking-window low-rank collapse and finite-Laplace compression at the actual `R_p`, `V_p` and Robin-scale tolerance are ruled out.
