# MI-065 — Compressibility profiles turn tail decay into a resolution condition curve

**Evidence level:** exact synthesis from [AF-475](../../findings/AF-475-compressibility-profiles-set-resolution-dependent-hilbert-conditioning.md), building on the fixed-tail estimate in [AF-474](../../findings/AF-474-best-s-term-tail-mass-gives-sharp-additive-hilbert-fidelity.md).

Let `phi(s)` be a nonincreasing source bound on best-`s`-term tail mass, `tau_s(mu)<=phi(s)`. For the coordinate Hilbert map `H(mu)=sqrt(2) mu`, every pair with `d_1(mu,nu)>=delta` has inverse condition number bounded by

`K_phi(delta) = inf_(s: 2 phi(s)<delta) sqrt(s)/(1-2 phi(s)/delta)`.

This is the useful compression ledger: the source supplies the whole approximation profile `s -> phi(s)`, while the destination supplies the smallest separation `delta` it must preserve. The optimal support budget is the `s` minimizing their combined cost; increasing `s` reduces the unresolved tail but worsens the `sqrt(s)` Hilbert factor.

Two regimes make the scaling explicit. If `phi(s)<=A s^(-alpha)`, then the coordinate construction gives `K_phi(delta)=O((A/delta)^(1/(2 alpha)))` as `delta->0`. If `phi(s)<=A exp(-c s^beta)`, then `K_phi(delta)=O((log(A/delta))^(1/(2 beta)))`. Hard support is the limiting special case where a finite `s_0` has `phi(s_0)=0`, recovering scale-free `sqrt(s_0)` conditioning.

The arithmetic question is therefore not whether a carrier is vaguely “compressible”, but whether its persisted source law proves a useful `phi_arith(s)`, whether the retained coordinates still distinguish the prime-derived source from matched controls, and whether the downstream theorem only needs resolution `delta_arith` for which `K_(phi_arith)(delta_arith)` is acceptable.

**Boundary.** `K_phi` is an achieved bound for the canonical coordinate Hilbert representation, not a minimax lower bound over all embeddings. AF-475 does not establish any arithmetic tail profile or downstream separation scale; those must be proved at their own layers.