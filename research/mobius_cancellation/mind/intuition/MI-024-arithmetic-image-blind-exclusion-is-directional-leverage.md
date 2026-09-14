# MI-024 — Arithmetic-image leverage reduces to near-injectivity, affine obstruction, or exponentially sparse support

**Evidence level:** exact variational/certificate reduction from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md), sharpened through MC-282, MC-284--MC-287 and [MC-288](../../findings/MC-288-geelen-odd-girth-density-trichotomy.md). The Geelen step is established finite-geometric prior art composed with the line's exact padding criterion. No theorem is claimed that the desired Christoffel certificate exists for the actual shell.

For feature matrix `A` on the actual arithmetic shell and blind row `v`, the endpoint-normalized energy is directional synthesis cost, not generic nonblindness. Moderate-conductor Legendre shadows can already be Boolean-complete, yet favorable endpoint leverage still requires stronger geometry.

For odd target weight `t`, MC-286 identifies the exact affine obstruction: failure of an odd zero-sum row is equivalent to `0 notin aff(S)`, hence to one generated product character that is constantly `-1` on the occupied shell. MC-287 showed that support denser than half the cube plus enough collisions already forces the target row.

MC-288 makes the surviving concentration branch much sharper. If the collision excess satisfies `N-K>=t-1` and no target row exists, the occupied support has odd girth greater than `t`. Geelen's geometric Andrásfai--Erdős--Sós theorem then gives, in the support's own rank-`r` span, either the exact affine obstruction or

`K/2^r <= (t+2)/2^(t+1)`.

Together with the collision-poor case, every odd energy-`<1` candidate must therefore satisfy at least one of three rigid alternatives:

`N-K <= t-2`, or `0 notin aff(S)`, or `K/2^r <= (t+2)/2^(t+1)`.

At the live `t=(1/log 2+o(1)) log log y` scale, the non-affine branch occupies only `(log y)^(-1+o(1))` of its own span. The old undifferentiated “half-cube concentration” escape has split into an exact one-character obstruction and an exponentially sparse non-affine image.

The arithmetic target is correspondingly sharper. One can attack the affine branch by ruling out a constant-negative generated quadratic character; attack the sparse branch by proving a much weaker occupancy lower bound than full cube coverage; and attack near-injectivity through its already expensive rank/conductor cost. High rank or generic diversity alone does not remove these three alternatives.

**Boundary.** The Geelen density threshold is sharp for general binary matroids. Improving it for the actual Legendre shell requires additional arithmetic structure. None of the three necessary branches is itself excluded by MC-288, and no Möbius summatory estimate follows.
