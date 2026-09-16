# MI-023 — The first-prime overlap algebra and fixed-aperture endpoint law do not orient the RH state

**Evidence level:** exact source-specific synthesis from [PL-324](../../findings/PL-324-odd-sector-order-positivity-breaks-exactly-at-first-prime.md), [PL-325](../../findings/PL-325-first-prime-shift-algebra-prior-art.md), and [PL-326](../../findings/PL-326-fixed-aperture-endpoint-law-does-not-orient-first-prime-reflection.md). The single-shift flip decomposition is public prior art and independently reconstructed in PL-325; no external computer-assisted positivity certificate is adopted.

Once `2a` crosses `log 2`, the first active prime-power channel is the truncated translation by `b=log 2`. In the first-prime window this operator is exactly a flip between the two overlap edge strips, with a zero middle strip. Therefore its spectrum is `{-1,0,1}`, both signed eigenspaces are infinite-dimensional, and its bounded-operator norm is exactly one for every positive overlap however small.

This sharpens PL-324 without solving its sign problem. Odd parity removes the generic archimedean order obstruction until the first prime appears, but the active prime channel itself is already an indefinite reflection. The arithmetic question is not whether both signs exist—they do—but **which signed state the full Weil operator selects and how that state couples to the endpoint/source structure**.

PL-326 closes the tempting inference from the fixed-aperture endpoint law. Write the aperture just above threshold as `a_delta=(log 2)/2+delta`. The first-prime reflection then acts on a shrinking layer of width `2delta`. Two continuous families can have exactly the same critical endpoint germ and satisfy the fixed-aperture residual law in its strongest form, while an antisymmetric interior bump reverses the reflection functional. The bump has `L^2` mass `O(delta)` and logarithmic endpoint-potential cost `O(delta log(1/delta))`, both tending to zero.

The obstruction is a quantifier mismatch. Pointwise `Q m(Q)->0` at each fixed aperture does not control the moving layer sampled when `delta->0`. The positive critical profile contributes only order `delta/log(1/delta)`, so an absolutely small antisymmetric component can still dominate its sign. A sufficient uniform scale is roughly

`||r_delta||_2 = o(|C_delta| sqrt(delta/log(1/delta)))`,

or an equivalent source/eigen-equation estimate that controls the reflection directly.

The norm jump therefore gives the wrong perturbative intuition, and fixed-aperture endpoint asymptotics give the wrong uniformity intuition. Near threshold the overlap remains norm-one while it is form-small, yet neither absolute smallness nor an eventual endpoint germ orients the signed channel. The load-bearing resource is a **uniform source-selected orientation theorem on the shrinking arithmetic overlap layer**.

PL-325 also establishes a research-allocation boundary: the flip decomposition, its `±1` sectors, Legendre compression and related single-prime finite-scale machinery are already public prior art. PL-326 adds that one cannot bridge the remaining gap merely by combining that algebra with the closed fixed-aperture Green/endpoint transfer.

The surviving mechanism must be aperture-uniform and state-selective: a signed first-crossing/eigenstate-orientation law, a source/endpoint-flux identity suppressing the antisymmetric moving-layer component, or another arithmetic theorem that controls the reflection functional directly. The relevant resource is **orientation of the full source-selected state at the moving threshold**, not the existence, norm, form-smallness or fixed-aperture boundary germ of the first-prime overlap.

**Boundary.** The PL-326 comparison families are not eigenstates and do not determine the sign of the actual ground branch. Their role is only to prove that the currently known endpoint law plus absolute layer smallness is insufficient. The public prior-art project contains stronger computer-assisted finite-scale claims, but this intuition does not import those as evidence.
