# MI-047 — Growing scalar Euler depth remains non-rigid with only a linear spatial repair tariff

**Evidence level:** exact constructive synthesis from RE-173, RE-178, RE-182 and [RE-184](../../findings/RE-184-growing-euler-jet-depth-below-kv-shell-scale-remains-nonrigid.md) through [RE-188](../../findings/RE-188-logarithmic-chebyshev-growth-cuts-the-euler-jet-spatial-tariff-to-linear.md). The stated depth range is sufficient, not claimed sharp; the linear-width lower bound is specific to the full-window Gauss--Chebyshev representation.

Scalar Euler depth does not become rigid merely because it reaches or exceeds the first apparent capacity crossover. Earlier constructions progressed from fixed depth to `K=Theta(V(p))`, then to every `K=o(log p/loglog p)`, and RE-187 pushed farther by paying a growing spatial repair width.

RE-188 shows that the quadratic width `W~K^2/log p` used there was itself a proof artifact. Exact logarithmic exterior growth of the Chebyshev modes makes the prime-power tail exponentially harmless already with

`W=4K`.

The ordinary-prime microstepped repair then survives with multiplicities in `{0,1,2}`, exact matching of every boundary Euler derivative through depth `K`, every fixed Korobov--Vinogradov source envelope, and the same order-one transient Robin ambiguity throughout the larger sufficient range

`K=o((log p)^(5/3)(loglog p)^(1/3))`.

Within the same full-window Gauss--Chebyshev frame, `W=Omega(K)` is also necessary in the deep regime if the exact shell matrix is to remain uniformly close to its DCT model. Thus this representation's spatial tariff is genuinely linear up to constants, while the previous quadratic tariff was not intrinsic.

The reusable lesson is sharper: **representation capacity can migrate repeatedly until the remaining tariff is proved intrinsic in the actual representation.** Basis conditioning, coarse transport and then quadratic spatial width all disappeared under better coordinates or estimates. Even the surviving linear width is only a theorem about this repair frame, not a universal scalar-rigidity barrier.

The next useful selector should therefore be joint/nonlocal and destination-sensitive rather than another scalar family whose repair cost can move into source placement. Any claimed scalar threshold must first survive optimized conditioning, exact prime-power resummation, microstepping and the linear Chebyshev width scale.

**Boundary.** RE-188 does not make the full Euler germ cheaply non-rigid, prove a universal `Omega(K)` width bound for arbitrary nonlinear/nonuniform repairs, or show scalar information is irrelevant when coupled to a genuinely relational source invariant. It strengthens the matched-control statement: deep scalar Euler agreement remains compatible with transient Robin ambiguity much farther than the previous capacity heuristics suggested.