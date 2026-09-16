# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Match source fidelity to both the spatial capacity and the global normalization actually consumed by Robin

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-037-mertens-normalization-turns-local-robin-shifts-into-tail-debt`.

RE-153--RE-163 identify the exact Pareto-weighted Chebyshev-deficit destination and quantify how coarse-PNT generalized sources can retain order-one terminal ambiguity even under many exact or approximate moment constraints. RE-164 then introduces quantitative Korobov--Vinogradov source fidelity.

RE-165--RE-168 identify one continuous KV source-capacity profile. The remote-tail capacity is

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

while a logarithmic shell of width `W` has capacity `S_b(p;T,W)`. The intrinsic decay length `ell_KV(T)=log T/V(T)` interpolates fixed-shell and remote regimes: only `Theta(ell_KV)` logarithmic width already carries remote-capacity order, and a subpower shell can contain essentially the whole remote ambiguity.

RE-169 adds a different source-fidelity coordinate that the earlier generalized controls did not preserve: the **Mertens-product normalization**. For two sources agreeing below `T`, the difference of their Mertens constants is exactly the full Robin-kernel weighted source discrepancy,

`Gamma(Q_2)-Gamma(Q_1)=int_T^infty (theta_(Q_2)-theta_(Q_1))(-h')`.

Consequently any accumulated post-selector Robin displacement is an exact debt to the unseen tail once `Gamma(Q_1)=Gamma(Q_2)`. Under the same KV envelope, the remaining debt above `U` is bounded by the remote capacity `K_b(p,U)`. A fixed normalized displacement therefore cannot be postponed beyond an `O(1)` neighborhood of the KV capacity center in the intrinsic `V` coordinate.

This does not make qualitative Mertens fidelity sufficient. The matched finite relocations of RE-167--RE-168 move `Gamma` only by `Theta((sqrt(p) log p)^(-1))` while producing order-one normalized Robin displacement, so they still satisfy `Gamma(Q_p)=gamma+o(1)`. The new rigidity enters only when the source class preserves the Mertens normalization at the **critical scale** `o((sqrt(p) log p)^(-1))` (or exactly), together with a KV-rigid tail.

The generalized-source frontier is therefore no longer described by pointwise PNT fidelity alone. A comparison must state both the spatial capacity available inside the KV decay-length window and which global normalization invariants are preserved at the precision the Robin kernel consumes. The live ordinary-prime/CA theorem is to obtain selector-sensitive control from genuine prime structure without simply restating the exact Mertens identity.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch must control target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacities, global normalization and zero-packet gates distinct

The coarse terminal moment hierarchy, quantitative shell/tail capacity profile, Mertens normalization and zero-side packet obstructions answer different questions. A generalized-source comparison must declare its quantitative PNT envelope, allowed displacement region, dimensionless width `xi=W/ell_KV(T)`, the Mertens constant/precision it preserves, and whether the corresponding future compensation capacity tends to zero. None of these source-rigidity statements by itself supplies the missing ordinary-prime selector theorem.
