# MI-047 — Growing scalar Euler depth remains non-rigid when repair width is paid spatially

**Evidence level:** exact constructive synthesis from RE-173, RE-178, RE-182 and [RE-184](../../findings/RE-184-growing-euler-jet-depth-below-kv-shell-scale-remains-nonrigid.md) through [RE-187](../../findings/RE-187-expanding-chebyshev-windows-push-euler-jet-non-rigidity-past-the-scalar-crossover.md). The stated depth range is sufficient, not claimed sharp.

Scalar Euler depth does not become rigid merely because it reaches or exceeds the first apparent capacity crossover. Earlier constructions progressed from fixed depth to `K=Theta(V(p))` and then, after conditioning the moving interpolation frame, to every

`K=o(log p/loglog p)`

while preserving ordinary-prime support, multiplicities in `{0,1,2}`, every fixed Korobov--Vinogradov source envelope and an order-one transient Robin excursion.

RE-187 shows that the coincidence with `log p/loglog p` was a fixed-window artifact. The centered Euler kernels admit an exact prime-power resummation in a Chebyshev coordinate. If the logarithmic interpolation window is widened to

`W_p ~ K^2/log p`,

the full prime-power tail becomes exponentially harmless while microstepped residue tracks keep the ordinary-prime repair shells disjoint. The remaining cost is no longer scalar interpolation conditioning but **where the repair reservoir must live**.

Requiring that the enlarged reservoir remain invisible to every fixed KV fidelity envelope yields the sufficient range

`K=o((log p)^(4/3)(loglog p)^(1/6))`,

which is parametrically larger than `log p/loglog p`. Exact boundary jets at those depths still fail to select the ordinary-prime source uniquely at Robin scale.

The reusable lesson is that **representation capacity can migrate between coordinates**. Optimizing the polynomial basis removed an interpolation-conditioning tariff; microstepping removed the coarse-generation transport tariff; widening the window then trades still larger scalar depth for a spatial source-placement tariff. A claimed scalar rigidity threshold is not intrinsic until all such equivalent repair coordinates have been priced.

The live resource is now the spatial width needed to realize a deep exact jet while remaining source-invisible. RE-187 pays `W~K^2/log p`; proving that some comparable lower bound is unavoidable would turn this construction into a genuine source-capacity boundary. Finding a more adaptive frame or nonuniform repair could instead push non-rigidity deeper.

**Boundary.** RE-187 does not prove the quadratic width tariff sharp, does not make the full Euler germ cheaply non-rigid, and does not show that scalar data are irrelevant when coupled to a genuinely joint/nonlocal source invariant. It is a matched-control theorem: deep scalar Euler agreement, even beyond the old crossover, still does not by itself force the Robin destination.