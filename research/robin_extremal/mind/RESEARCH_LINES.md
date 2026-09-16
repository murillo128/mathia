# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Match source fidelity to both the spatial capacity and the global normalization actually consumed by Robin

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-037-mertens-normalization-turns-local-robin-shifts-into-tail-debt`.

RE-153--RE-163 identify the exact Pareto-weighted Chebyshev-deficit destination and quantify how coarse-PNT generalized sources can retain order-one terminal ambiguity even under many exact or approximate moment constraints. RE-164 then introduces quantitative Korobov--Vinogradov source fidelity.

RE-165--RE-168 identify one continuous KV source-capacity profile. The remote-tail capacity is

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

while a logarithmic shell of width `W` has capacity `S_b(p;T,W)`. The intrinsic decay length `ell_KV(T)=log T/V(T)` interpolates fixed-shell and remote regimes: only `Theta(ell_KV)` logarithmic width already carries remote-capacity order, and a subpower shell can contain essentially the whole remote ambiguity.

RE-169 adds a different source-fidelity coordinate: the Mertens-product normalization. For two sources agreeing below `T`, the difference of their Mertens constants is exactly the full Robin-kernel weighted source discrepancy. Consequently any accumulated post-selector Robin displacement is an exact debt to the unseen tail once the Mertens constants match. Under the KV envelope, the remaining debt above `U` is bounded by `K_b(p,U)`, so critical-scale Mertens matching becomes prefix-rigid only once the future KV capacity is itself negligible.

RE-170 proves that the tail condition is load-bearing. Two separated bounded-multiplicative shells can create an order-one intermediate Robin excursion and later cancel it while preserving the KV envelope to vanishing relative error and achieving

`Gamma(Q_p)-gamma=o((sqrt(p) log p)^(-1))`.

Thus even the **critical** Mertens precision identified by RE-169 does not determine a finite selected prefix by itself. Global normalization constrains the net weighted charge, but ample later shell capacity can transport an opposite charge and erase it asymptotically.

The generalized-source frontier is therefore a two-resource condition, not a stronger single normalization statement: one needs a global Mertens constraint at the scale the Robin kernel consumes **and** a spatial/tail theorem that prevents later compensation. The live ordinary-prime/CA question is to derive that selector-sensitive localization from genuine prime structure without merely restating the exact Mertens identity.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch must control target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacities, global normalization and zero-packet gates distinct

The coarse terminal moment hierarchy, quantitative shell/tail capacity profile, Mertens normalization and zero-side packet obstructions answer different questions. A generalized-source comparison must declare its quantitative PNT envelope, allowed displacement region, dimensionless width `xi=W/ell_KV(T)`, the Mertens constant/precision it preserves, and whether the corresponding future compensation capacity tends to zero. RE-170 makes the final condition nonoptional: a globally matched invariant can coexist with an order-one transient prefix excursion whenever a later shell still has enough capacity to repay the debt. None of these source-rigidity statements by itself supplies the missing ordinary-prime selector theorem.