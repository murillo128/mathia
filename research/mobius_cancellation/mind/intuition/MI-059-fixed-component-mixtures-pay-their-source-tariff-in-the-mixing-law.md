# MI-059 — Mixture source tariffs split between latent-law motion and component motion

**Evidence level:** exact synthesis from [MC-353](../../findings/MC-353-edge-jeffreys-is-the-exact-local-dephasing-currency.md), [MC-357](../../findings/MC-357-fixed-component-mixture-edge-tariff.md), and [MC-358](../../findings/MC-358-source-dependent-mixture-component-tariff.md). Relative-entropy chain rule, Jeffreys divergence and data processing are classical; the Mathia content is their composition with the reciprocal endpoint discrimination lower bound and the architecture-relative resource ledger.

Suppose a source-dependent latent architecture factors as

`Theta~nu_x`, `Y|Theta=theta~K_x(.|theta)`,

with lifted joint law `Q_x(dtheta,dy)=nu_x(dtheta)K_x(dy|theta)` and output marginal `P_x`. For a neighboring source edge `e={x,x'}`, write `b_e(Y)` for output half-Jeffreys divergence, `b_e(Theta)` for latent-law half-Jeffreys divergence, and let `c_e(K)` be the symmetrized conditional KL cost of changing the paired component kernels on the same latent fibers.

The KL chain rule gives the exact joint split

`(1/2)J(Q_x,Q_x') = b_e(Theta)+c_e(K)`,

while marginalization gives

`b_e(Y) <= b_e(Theta)+c_e(K)`.

MC-353 independently forces `E_e b_e(Y) >= eta^2/C-o(1)` under bounded coefficient energy `C` and fixed nontrivial dephasing `eta`. Therefore every such admitted mixture architecture must pay

`E_e[b_e(Theta)+c_e(K)] >= eta^2/C-o(1)`.

MC-357 is the fixed-component boundary `c_e(K)=0`: all source discrimination must then be carried by the latent selector. MC-358 shows that allowing the components themselves to move does not remove the tariff; it only creates a second place to pay it. The exact resource is the half-Jeffreys divergence of the **actual lifted architecture**, not visual complexity of the marginal mixture.

At the exact endpoint the support statement also splits cleanly. If neighboring output laws are mutually singular, the lifted joint laws must be singular. For a finite categorical latent variable, every label with positive weight under both neighboring source states must therefore pair mutually singular component laws. Fixed components force disjoint weight supports; moving components may share a label only by making that shared fiber singular.

The decomposition is meaningful only when the latent coordinate has common architectural semantics across source states. A source-dependent relabeling can move cost between the latent and conditional terms, and an arbitrary post-hoc decomposition of the same marginal law is not evidence that the system paid either tariff. Hidden adaptive branches, random seeds, selectors, metadata or other source-dependent paths must be included in the lifted transcript before the accounting is applied.

The reusable point is that **mixture complexity and source discrimination are different resources, and source dependence cannot be made free by choosing whether it lives in weights or components**. A surviving endpoint mechanism must exhibit the required adjacent lifted divergence or singularity somewhere in its real source graph.

**Boundary.** MC-358 supplies no arithmetic upper bound on the lifted tariff and does not prove a bound for `M(x)`. A large latent-plus-component tariff is necessary but not sufficient for dephasing because marginalization may discard it. Approximate endpoints require quantitative divergence/near-singularity rather than literal support separation. The next productive step is architecture-specific: expose an actual Möbius-derived lifted law and prove a source-edge upper theorem for it, or identify the mathematically forced source-dependent channel that prevents such an upper bound.