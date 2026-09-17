# MI-047 — Growing scalar Euler depth below the KV shell scale remains non-rigid

**Evidence level:** exact constructive synthesis from RE-173, RE-178, RE-182 and [RE-184](../../findings/RE-184-growing-euler-jet-depth-below-kv-shell-scale-remains-nonrigid.md). The stated growing-depth range is sufficient, not claimed sharp.

The failure of scalar Euler data is not confined to fixed dimension. Let

`V(p)=(log p)^(3/5)/(log log p)^(1/5)`.

RE-184 constructs ordinary-prime-supported `{0,1,2}` controls matching every Euler boundary derivative through a depth `K(p)` whenever

`K(p) log(K(p)+2)=o(V(p))`,

while preserving every fixed Korobov--Vinogradov source envelope and an order-one transient Robin displacement. In particular `K(p)=floor((log p)^(1/2))` is already admissible.

The mechanism is quantitative shell interpolation. Recentring the Euler jets keeps the Vandermonde response controlled, and the growing interpolation overhead is only `exp(O(K log K))`; KV-wide prime shells still provide enough honest source mass for exact infinite-tail compensation. Thus **unbounded scalar dimension is not itself a source-rigidity mechanism** when the admissible source fibre can absorb the corresponding interpolation cost.

The live transition is therefore quantitative rather than finite-versus-infinite. RE-178 identifies the much larger raw capacity scale `K_cap(p) asymp log p/log log p`, while RE-184 proves non-rigidity throughout a substantial subcritical range. Any scalar-jet rigidity theorem must locate a genuine crossover between these regimes or add a joint placement/integrality constraint that the shell interpolation cannot satisfy.

**Boundary.** RE-184 does not reach the RE-178 capacity scale, prove sharpness of `K log K=o(V)`, or treat arbitrary growing temperature panels. The repair still uses an infinite continuation; finite ordinary-prime perturbations remain rigid under RE-172. The conclusion concerns the declared `{0,1,2}` source class and does not make the full Euler germ a cheaply conditioned invariant.