# MI-036 — Quantitative PNT fidelity has a KV decay-length capacity profile

**Evidence level:** literature-backed/exact synthesis from [RE-015](../../findings/RE-015-pnt-remainder-controls-upper-robin-tail.md), [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), and [RE-155](../../findings/RE-155-terminal-generalized-source-ambiguity.md) through [RE-168](../../findings/RE-168-kv-decay-length-interpolates-local-and-remote-robin-capacity.md). The quantitative PNT envelope is an explicit source-class hypothesis; no claim is made that arbitrary generalized primes satisfy it.

The terminal moment hierarchy measures ambiguity only inside the source class still allowed after stronger source information is imposed. RE-164--RE-166 identify a sharp Korobov--Vinogradov remote-tail capacity

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

where `V(T)=(log T)^(3/5)/(log log T)^(1/5)`. RE-167 shows that a discrepancy confined to one fixed multiplicative shell has the smaller capacity

`L_b(p,T)=sqrt(p) log p exp(-b V(T))/log T`.

RE-168 identifies the missing spatial scale relating them. In logarithmic height `u=log t`, the KV envelope changes by order one over

`ell_KV(T)=log T/V(T)`.

For a shell of logarithmic width `W=o(log T)`, define

`S_b(p;T,W)=sqrt(p) log p int_T^(T exp W) exp(-bV(t))/(t log t) dt`.

If `xi=W/ell_KV(T)` tends to a finite value, then

`S_b/K_b -> Phi_b(xi)=(5/(3b))(1-exp(-3b xi/5))`.

This formula interpolates the previous sharp capacities. When `xi->0`, `S_b~W L_b`; a fixed multiplicative shell is the extreme local regime. When `xi` is order one, the shell already has remote-capacity order. When `xi->infinity` while `W=o(log T)`, the shell captures asymptotically the full remote integral up to its fixed Laplace constant.

The remote obstruction is therefore **subpower-local**. A width `W=omega_T ell_KV(T)` with `omega_T->infinity` and `omega_T=o(V(T))` still ends at `T^(1+o(1))`, yet contains essentially all of the remote KV capacity. The earlier `Theta(log log p)` separation between fixed-shell and remote capacity-one centers is the price of restricting available width from `Theta(ell_KV)` to `O(1)` in logarithmic height, not evidence for two different source mechanisms.

Matched generalized-prime controls make this an actual capacity law rather than an upper-bound artifact. Concatenate mass-balanced relocations in fixed logarithmic blocks. Each block returns its cumulative Chebyshev discrepancy exactly to zero before the next begins, so the pointwise KV envelope does not accumulate, while Robin displacements add with one sign. The resulting total displacement is a Riemann sum for `S_b`.

The reusable source-fidelity variable is therefore not simply “local versus remote.” It is the dimensionless width

`xi = W V(T)/log T`.

A pointwise source envelope has different destination power depending on how many of its intrinsic decay lengths the unresolved discrepancy may occupy. Restricting source error to a geometrically small or even subpower region can still leave full remote ambiguity if that region contains `omega(1)` KV decay lengths.

For Robin, moment matching becomes relevant only after the actual selector/source geometry is placed relative to this profile. At bounded-multiplicative `T=Bp`, even the fixed-width capacity diverges, so quantitative PNT fidelity still does not identify the source coordinate. A genuinely new ordinary-prime/CA input must constrain **where inside the KV decay-length window** mass can move, not merely improve the global envelope or state that the perturbation is subpower-local.

**Boundary.** The lower sharpness constructions use generalized-prime relocations in the declared quantitative envelope and do not assert that ordinary primes realize them. The interpolation assumes `W=o(log T)` for the stated local expansion, and it is a terminal-source capacity result, not a Robin proof or a zero-side theorem.
