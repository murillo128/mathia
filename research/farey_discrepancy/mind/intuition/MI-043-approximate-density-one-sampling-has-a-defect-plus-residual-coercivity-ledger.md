# MI-043 — Approximate density-one sampling has a defect-plus-residual coercivity ledger

**Evidence level:** exact source-specific synthesis from [FD-242](../../findings/FD-242-density-one-approximate-sampling-is-stable-under-weighted-response-residual.md), extending the exact-zero density-one threshold FD-240--FD-241. This concerns unrestricted signed profiles under `|b_n|<=Cn`; it does not transfer to physical nonnegative/source-coherent profiles without a separate theorem.

Let `Y(m)` be the divisor response, `S` the sampled locations, `R(N)=|[1,N]\S|`, and define the weighted adjacent sampled variation

`V_S(N)=sum_(m<=N, m,m-1 sampled) |Y(m)-Y(m-1)|/m`.

FD-242 gives the capacity-scale stability estimate

`sum_(N/2<n<=N)|b_n| / sum_(N/2<n<=N)n << C sqrt((R(N)+1)/N) + V_S(N)/N`.

The simpler sampled-amplitude functional `Q_S(N)=sum_(m<=N,m in S)|Y(m)|/m` satisfies `V_S(N)<=2Q_S(N)`. Hence density-one sampling plus `Q_S(N)=o(N)` still forces normalized octave capacity to zero; in particular sampled `Y(m)=o(m)` is enough.

The mechanism is the stable form of the exact support localization. Möbius inversion gives `g(m)=Y(m)-Y(m-1)`. Exact zeros put `g` on the sparse omission boundary; approximate data instead split `g` into arbitrary increments on a sparse defect set and explicitly measured adjacent increments on sampled runs. The coefficient envelope controls the first part by the same square-root omission penalty, while `V_S` measures the second exactly.

The residual scale is meaningful rather than cosmetic. Existing signed blind profiles with macroscopic capacity can have `Y(m)=O(m)` everywhere, and FD-242 forces their weighted residual mass to be linear along the relevant scales. Thus **sublinear weighted sampled residual is the robust capacity-coercive regime, while merely linear residual cannot be ruled out in the unrestricted signed class**.

**Boundary.** `V_S(N)=o(N)` is a sufficient stability condition, not a classification of every noisy kernel. The coefficient envelope remains load-bearing, density one remains necessary for universal capacity coercivity, and this result says nothing about finer-than-capacity norms or about extra positivity, reservoir and arithmetic-coherence constraints.