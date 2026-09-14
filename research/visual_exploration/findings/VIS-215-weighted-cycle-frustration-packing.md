# VIS-215 — fractional cycle packing gives a weighted holonomy deficit certificate

## Claim

Keep the finite Hermitian zero-diagonal matrix setup of `VIS-214`. On an oriented support edge `e=u->v`, write

`A_(u,v)=w_e exp(i theta_e)`, with `w_e>0`,

and for a torus point `z_u=exp(i phi_u)` put

`delta_e = theta_e + phi_v - phi_u  (mod 2 pi)`.

As before,

`G(z)=2 sum_e w_e cos(delta_e)`,

`B(A)=2 sum_e w_e`.

Define the positive- and negative-envelope deficits

`E_+(z)=B(A)-G(z)=sum_e w_e |1-exp(i delta_e)|^2`,

`E_-(z)=B(A)+G(z)=sum_e w_e |1+exp(i delta_e)|^2`.

For every oriented simple support cycle `C`, let

`H_+(C)=exp(i sum_(e in C) theta_e)`,

`H_-(C)=(-1)^|C| H_+(C)`,

and define its harmonic resistance

`R(C)=sum_(e in C) 1/w_e`.

Then every torus point satisfies the sharper weighted cycle bounds

`E_+(z) >= |1-H_+(C)|^2 / R(C)`,

`E_-(z) >= |1-H_-(C)|^2 / R(C)`.

More importantly, frustrated cycles can be accumulated instead of taking only the strongest single cycle. Let `lambda_C>=0` be any fractional cycle packing satisfying

`sum_(C contains e) lambda_C <= 1`

for every support edge `e`. Then

`E_+(z) >= sum_C lambda_C |1-H_+(C)|^2 / R(C)`,

`E_-(z) >= sum_C lambda_C |1-H_-(C)|^2 / R(C)`.

Therefore, if

`P_+ = max_lambda sum_C lambda_C |1-H_+(C)|^2/R(C)`,

`P_- = max_lambda sum_C lambda_C |1-H_-(C)|^2/R(C)`,

where each maximum is over the same edge-capacity polytope of fractional cycle packings, then

`-B(A)+P_- <= G(z) <= B(A)-P_+`

for every `z`, and hence

`max_z |G(z)| <= B(A)-min(P_+,P_-)`.

The optimization defining `P_+` and `P_-` is a linear program once cycle holonomies and edge weights are fixed. It converts the qualitative cycle-frustration obstruction of `VIS-214` into a global certificate that can add contributions from many distributed frustrated cycles while respecting shared-edge capacity.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-U(1)-SYNCHRONIZATION/FRUSTRATION SETTING + FRACTIONAL-CYCLE-PACKING CERTIFICATE + NO-NOVELTY-CLAIM`.

No claim is made that the fractional-packing inequality is a new general graph-theoretic theorem. Its role is to give the prime-phase torus program an explicit weighted certificate in the normalization of `VIS-213`/`VIS-214` and to identify exactly what an asymptotic argument would have to make large.

## 1. A cycle controls weighted synchronization energy through its holonomy

For the positive envelope set

`r_e=exp(i delta_e)`.

Around a cycle, the vertex phases telescope, so

`prod_(e in C) r_e = H_+(C)`.

For unit complex numbers `r_1,...,r_k`, the telescoping product identity gives

`1-prod_(j=1)^k r_j = sum_(j=1)^k (prod_(l<j) r_l)(1-r_j)`.

All prefactors have modulus one, hence

`|1-H_+(C)| <= sum_(e in C) |1-r_e|`.

Weighted Cauchy-Schwarz now yields

`(sum_(e in C) |1-r_e|)^2`
` <= (sum_(e in C) 1/w_e)(sum_(e in C) w_e |1-r_e|^2)`.

Therefore

`sum_(e in C) w_e |1-r_e|^2 >= |1-H_+(C)|^2/R(C)`.

Since `E_+(z)` contains the same nonnegative edge terms over the whole support graph, the first positive-envelope bound follows.

For the negative envelope use

`q_e=-exp(i delta_e)`.

Then

`E_-(z)=sum_e w_e |1-q_e|^2`

and the cycle product is

`prod_(e in C) q_e = (-1)^|C| H_+(C)=H_-(C)`.

The identical argument gives the negative-envelope bound.

The certificate is orientation-independent: reversing a cycle conjugates `H_+` and `H_-`, leaving `|1-H|` unchanged, while `R(C)` is unchanged.

## 2. Fractional packing accumulates distributed frustration

Apply the single-cycle inequality before discarding its edge-local form:

`lambda_C |1-H_+(C)|^2/R(C)`
` <= lambda_C sum_(e in C) w_e |1-r_e|^2`.

Summing over cycles gives

`sum_C lambda_C |1-H_+(C)|^2/R(C)`
` <= sum_e w_e |1-r_e|^2 sum_(C contains e) lambda_C`.

The packing constraints make the final factor at most one on every edge, hence the right side is at most `E_+(z)`. This proves the packed positive certificate. Replacing `r_e` by `q_e` proves the negative one.

Edge-disjoint cycles are the integral special case `lambda_C in {0,1}`. Fractional packing is useful because dense support graphs can contain many informative short cycles that overlap; the capacity constraint prevents counting the same edge energy more than once while still allowing several incompatible holonomies to contribute.

The best certificate `P_+` or `P_-` is therefore the optimum of a cycle-packing linear program with cycle reward

`rho_+(C)=|1-H_+(C)|^2/R(C)`

or

`rho_-(C)=|1-H_-(C)|^2/R(C)`.

This is a lower bound on the full nonlinear synchronization/frustration energy, not an exact formula for it.

## 3. Relation to the one-cycle certificate in VIS-214

`VIS-214` used only

`m(C)=min_(e in C) w_e`

and the fact that at least one switched edge must carry phase error at least `h(C)/|C|`. That gives a deliberately crude one-edge certificate. The present inequality keeps the weighted `L2` energy around the whole cycle and replaces the minimum edge weight by the harmonic cycle scale `1/R(C)`.

For equal weights `w_e=w` on a `k`-cycle with holonomy angle `h in [0,pi]`, the new one-cycle reward is

`(4w/k) sin^2(h/2)`.

In the small-holonomy regime this is

`w h^2/k + O(w h^4/k)`,

whereas the `VIS-214` minimum-edge argument behaves as

`w h^2/k^2 + O(w h^4/k^4)`.

Thus even before packing several cycles, retaining the distributed cycle energy removes one factor of `k` in the small-holonomy scaling for uniform weights. The main conceptual gain, however, is accumulation: a graph carrying many sufficiently weighted frustrated cycles can have a macroscopic certificate even when no individual cycle dominates.

## 4. Classical synchronization and magnetic-Laplacian boundary

The energy

`sum_e w_e |1-exp(i delta_e)|^2`

is a standard `U(1)` synchronization/magnetic-connection energy after fixing unit-modulus vertex labels. The surrounding language of switching, gauge invariance, frustration and connection Laplacians is therefore classical.

Afonso S. Bandeira, Amit Singer, and Daniel A. Spielman, **A Cheeger Inequality for the Graph Connection Laplacian**, *SIAM Journal on Matrix Analysis and Applications* 34:4 (2013), 1611–1630, DOI `10.1137/120875338`, treats synchronization energy through the graph connection Laplacian and relates synchronization quality to its spectrum.

Carsten Lange, Shiping Liu, Norbert Peyerimhoff, and Olaf Post, **Frustration index and Cheeger inequalities for discrete and continuous magnetic Laplacians**, *Calculus of Variations and Partial Differential Equations* 54 (2015), 4165–4196, DOI `10.1007/s00526-015-0935-x`, develops switching-invariant frustration for weighted graphs with cyclic and `U(1)` signatures and the corresponding magnetic Cheeger theory.

A close current prior-art boundary is Lluís Torres-Hugas, Jordi Duch, Sergio Gómez, and Alex Arenas, **Cycle holonomy induces higher-order constraints and controls remote synchronization transitions via twisted Laplacian spectra**, arXiv:`2604.19682` (2026), which explicitly treats `U(1)` connections, cycle holonomy and spectral frustration. This rules out any novelty claim based merely on the principle that nontrivial cycle holonomy creates a global synchronization obstruction.

The elementary weighted cycle and fractional-packing inequalities above were derived directly for the Mathia objective. They are not attributed to these references and are not claimed to be absent from the broader synchronization, magnetic-graph, gain-graph, or cycle-packing literature.

## 5. Representation audit

The reduction preserves the pieces needed for the envelope question:

- each support edge keeps its coefficient magnitude `w_e`;
- its preferred phase is retained modulo vertex gauge through cycle holonomy;
- the torus action is represented exactly as switching of edge phases;
- positive and negative coefficient envelopes are kept distinct through `H_+` and `H_-`;
- edge sharing is retained by the packing capacities rather than treating cycles as independent observations.

The reduction is intentionally lossy in one direction. The collection of cycle rewards `rho_±(C)` does not determine the torus optimum and the fractional packing does not reconstruct the optimizer. Two gain graphs can have similar packing certificates but different detailed synchronization landscapes. The certificate is therefore safe as a lower bound on unavoidable frustration, not as a complete representation of `G(z)`.

Trees remain the correct boundary case: there are no support cycles, so `P_+=P_-=0`, consistent with every edge phase being switchable away. A single cycle reduces exactly to the one-cycle inequality above. Vanishing holonomy on every cycle gives `P_+=0`; vanishing shifted holonomy on every cycle gives `P_-=0`, matching the exact attainability criteria of `VIS-214`.

## 6. Prime-phase consequence and remaining gate

Applied to the prime-phase matrix `A_(y,H)` of `VIS-213`, the next quantitative problem is no longer merely to find one visibly frustrated triangle. It is to prove that the support graph contains a fractional packing of cycles whose combined reward

`sum_C lambda_C |1-H_±(C)|^2/R(C)`

is large on the coefficient scale relevant to the desired envelope suppression.

This cleanly separates three questions that had been mixed in a raw phase plot:

1. **topological obstruction:** whether cycle holonomies are nontrivial (`VIS-214`);
2. **weighted concentration:** whether enough nontrivial holonomy lies on cycles with substantial harmonic edge weight (this finding);
3. **orbit access:** whether the one-parameter prime-log trajectory reaches favorable torus regions on the finite time scale of interest (`VIS-213`), which remains untouched.

The present result answers the second question only at the deterministic certificate level. It does not prove that `P_+` or `P_-` has a useful asymptotic lower bound for the actual prime matrix, does not compare that bound to the Haar RMS scale, and does not resolve finite-time access. Establishing any of those would require new arithmetic information about the coefficient-weighted cycle ensemble and belongs to a later research thread.
