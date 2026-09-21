# MI-066 — Realizable tail breadth is the minimax side of compressibility

**Evidence level:** exact metric synthesis from [AF-476](../../findings/AF-476-compressibility-profiles-force-hamming-cube-lower-conditioning.md), complementary to the achieved coordinate upper bound in [AF-475](../../findings/AF-475-compressibility-profiles-set-resolution-dependent-hilbert-conditioning.md).

For the full profile class

`C_phi = {mu : tau_s(mu) <= phi(s) for every s}`,

define the tail breadth visible at resolution `delta` by

`N_phi(delta) = sup {k >= 1 : phi(k) >= delta/2}`,

with the finite-alphabet cutoff `2k+1 <= |A|` when needed. Whenever `phi(k) >= delta/2`, the class contains an explicit `k`-dimensional Hamming cube: put mass `1-delta/2` on one common atom and split the remaining `delta/2` among `k` independent paired private atoms. Cube edges then have `d_1` length `delta/k` and antipodes have distance exactly `delta`.

The Hilbert/Enflo cube inequality therefore gives a representation-independent obstruction. For every globally `1`-Lipschitz map `F:C_phi -> H`, some antipodal pair at source distance `delta` has Hilbert distance at most `delta/sqrt(k)`. Hence every resolution-`delta` inverse estimate must pay

`K_phi,H^opt(delta) >= sqrt(N_phi(delta))`.

For two-sided regular profiles this matches the coordinate-map order from AF-475. If `phi(s)` has two-sided polynomial order `s^(-alpha)`, the optimal Hilbert condition grows like `delta^(-1/(2 alpha))`; for two-sided stretched-exponential decay it grows like the corresponding polylogarithmic power. The square root of the effective support scale is therefore not merely a coordinate-embedding artifact on the full envelope class.

The arithmetic distinction is now two-sided. An upper approximation profile says how efficiently every source can be truncated; a lower realizable-breadth profile asks how many independent tail switches the actual arithmetic source class really contains at the same resolution. If the two scales match, Hilbert compression is pinned from both sides. If they do not, the gap is itself mathematical information: arithmetic relations have made the source thinner than the generic compressibility envelope.

**Boundary.** AF-476 is a minimax theorem for the full class `C_phi`, not automatically for a narrower prime-derived subclass. A one-sided upper law `tau_s <= phi(s)` does not prove that the private-tail cubes are realizable there. No arithmetic tail profile, realizable-cube dimension, downstream separation, or rational-prime discriminator is established by this synthesis.