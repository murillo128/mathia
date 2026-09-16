# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Use the source-fidelity capacity matched to the spatial class of the missing source

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-036-quantitative-pnt-fidelity-rigidifies-the-terminal-source-before-moment-complexity`.

RE-153--RE-163 identify the exact Pareto-weighted Chebyshev-deficit destination and quantify how coarse-PNT generalized sources can retain order-one terminal ambiguity even under many exact or approximate moment constraints. RE-164 then introduces quantitative Korobov--Vinogradov source fidelity.

RE-165--RE-166 give the sharp **remote-tail** capacity

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

while RE-167 gives the smaller fixed-width shell capacity

`L_b(p,T)=sqrt(p) log p exp(-b V(T))/log T`,

with `V(T)=(log T)^(3/5)/(log log T)^(1/5)`. Both scales are sharp against matched generalized-prime relocations, but their capacity-one centers are separated by `Theta(log log p)` in the intrinsic `V` coordinate.

RE-168 shows these are not two unrelated regimes. The KV envelope has logarithmic decay length

`ell_KV(T)=log T / V(T)`.

For a logarithmic shell `[T,T exp(W)]`, the exact source capacity is governed by

`S_b(p;T,W)=sqrt(p) log p int_T^(T exp W) exp(-bV(t))/(t log t) dt`.

If `xi=W/ell_KV(T) -> xi_0`, then relative to the remote capacity

`S_b/K_b -> Phi_b(xi_0)=(5/(3b))(1-exp(-3b xi_0/5))`.

Thus `W=o(ell_KV)` gives `S_b~W L_b`, while only `Theta(ell_KV)` logarithmic width already reaches the **remote-tail capacity scale**. Taking `W=omega_T ell_KV` with `omega_T->infinity` but `omega_T=o(V(T))` captures asymptotically the full remote capacity inside a subpower shell `T^(1+o(1))`.

The source-fidelity gate is therefore genuinely two-dimensional: pointwise KV envelope plus **available displacement width measured in units of `ell_KV`**. “Local shell” and “remote tail” are endpoints of one interpolation, not separate mechanisms. Restricting uncertainty to a subpower neighborhood does not by itself make the source rigid if that neighborhood contains many KV decay lengths.

At every bounded-multiplicative post-selector scale `T=Bp`, even the fixed-width capacity is `p^(1/2-o(1))->infinity`; quantitative PNT fidelity alone still does not identify the normalized Robin coordinate there. The live ordinary-prime/CA theorem must constrain where the actual selector can move Chebyshev mass **inside the KV decay-length window**, or provide a non-terminal channel that bypasses this terminal capacity altogether.

## Control one-sided vertical reciprocal escape without overstating the symmetric obstruction

RE-144--RE-152 put the zero-side packet into reciprocal-scale language and show that one-sided vertical phase geometry can hide a scale-maximal target at lacunary stages while fixed-order global local-correlation statistics remain unchanged. A closure theorem on this branch must control target-conditioned exceptional geometry rather than typical-center averages.

## Keep source capacities, source-spectral ambiguity and zero-packet gates distinct

The coarse terminal moment hierarchy, quantitative shell/tail capacity profile and zero-side packet obstructions answer different questions. A generalized-source comparison must declare its quantitative PNT envelope, the allowed displacement region, the dimensionless width `xi=W/ell_KV(T)`, and whether the corresponding `S_b` actually tends to zero. Neither a sharp source-rigidity capacity nor a zero-side matched obstruction supplies the missing ordinary-prime selector theorem by itself.
