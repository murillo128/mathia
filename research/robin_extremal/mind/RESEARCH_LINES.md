# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Match source fidelity to both the spatial capacity and the global normalization actually consumed by Robin

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-037-mertens-normalization-turns-local-robin-shifts-into-tail-debt`.

RE-153--RE-163 identify the exact Pareto-weighted Chebyshev-deficit destination and quantify how coarse-PNT generalized sources can retain order-one terminal ambiguity even under many exact or approximate moment constraints. RE-164 then introduces quantitative Korobov--Vinogradov source fidelity.

RE-165--RE-168 identify one continuous KV source-capacity profile. The remote-tail capacity is

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

while a logarithmic shell of width `W` has capacity `S_b(p;T,W)`. The intrinsic decay length `ell_KV(T)=log T/V(T)` interpolates fixed-shell and remote regimes: only `Theta(ell_KV)` logarithmic width already carries remote-capacity order, and a subpower shell can contain essentially the whole remote ambiguity.

RE-169 adds a different source-fidelity coordinate: the Mertens-product normalization. For two sources agreeing below `T`, the difference of their Mertens constants is exactly the full Robin-kernel weighted source discrepancy. Consequently any accumulated post-selector Robin displacement is an exact debt to the unseen tail once the Mertens constants match. Under the KV envelope, the remaining debt above `U` is bounded by `K_b(p,U)`, so Mertens matching becomes prefix-rigid only once the future KV capacity is itself negligible.

RE-170 proves that critical-scale Mertens matching does not supply that localization. Two separated bounded-multiplicative shells can create an order-one intermediate Robin excursion and later cancel it while preserving the KV envelope to vanishing relative error and making the final Mertens mismatch `o((sqrt p log p)^(-1))`.

RE-171 removes the last possible scalar-precision escape. A third Chebyshev-mass-neutral micro-correction, using only `O(log p)` prime pairs and `O((log p)^2)` cumulative Chebyshev discrepancy, can tune the generalized source to **exact** ordinary normalization `Gamma(Q_p)=gamma` while leaving the earlier order-one prefix excursion untouched. After the final shell the full Robin displacement is exactly zero, but between the first and second shells it remains order one.

The generalized-source frontier is therefore not “find a more accurate Mertens normalization.” That axis is exhausted: exact equality still permits transient prefix motion whenever future spatial capacity can repay the debt. The missing resource must be **selector-sensitive localization**—a theorem tying the selected prefix to where opposite-sign future Robin-kernel charge may occur—or another genuinely source-specific nonlocal invariant that the three-shell control cannot preserve.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch must control target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacities, global normalization and zero-packet gates distinct

The coarse terminal moment hierarchy, quantitative shell/tail capacity profile, Mertens normalization and zero-side packet obstructions answer different questions. A generalized-source comparison must declare its quantitative PNT envelope, allowed displacement region, dimensionless width `xi=W/ell_KV(T)`, the Mertens constant it preserves, and whether the corresponding future compensation capacity tends to zero. RE-171 makes the final condition nonoptional even under exact `Gamma=gamma`: a globally exact invariant can coexist with an order-one transient prefix excursion whenever later shells retain enough capacity to repay the debt. None of these source-rigidity statements by itself supplies the missing ordinary-prime selector theorem.