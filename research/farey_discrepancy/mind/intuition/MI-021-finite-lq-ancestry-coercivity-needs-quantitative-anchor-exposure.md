# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and its cost depends on anchor geometry

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-155](../../findings/FD-155-thinning-finite-prime-avoidance-frame-has-double-exponential-parent-load-cost.md).

For binary orientations anchored on `D`, finite-`L^q` recovery is controlled by anchored boundary exposure:

`C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`.

Connectivity merely excludes zero boundary. Stable recovery requires every admissible macroscopic flip to carry uniformly positive observed boundary mass.

FD-148--FD-153 price this for **rank-aligned** divisor-closed anchors. A fixed finite anchor forces parent amplification of order `T`. Growing rank anchors trade that parent bill for direct source orientation: bounded parent distortion requires positive anchor mass. Once the rank anchor enters the Erdős--Kac central window, the residual child depth is the Gaussian fluctuation scale `sqrt(log log T)`; farther into the supertypical tail the conditional overshoot becomes geometric and the residual depth can become bounded only as the rank anchor approaches total source mass.

FD-154 shows that this depth phase diagram is not universal over divisor-closed anchors. For a fixed finite set of primes `S`, the prime-avoidance face

`D_(S,T)={n<=T : mu^2(n)=1, (n,P_S)=1}`

is divisor-closed and every unanchored squarefree `m` has an `S`-free core `c_S(m)` in the anchor at ancestry depth at most `|S|`. Giving each unanchored vertex its direct edge from that core yields an exact Dirichlet sampling frame:

`h_(D_(S,T)) = |V_T|/|R_(S,T)|`

and, for every finite `q`, an exact norm identity between the unanchored coefficient norm and the edge-gradient norm up to the deterministic mass factor. Parent and child distortions stay bounded in `T` for fixed `S`. For one prime `ell`, the construction is depth one with

`P_(ell,T)=K_(ell,T)=h_(D_(ell,T)) -> ell+1`.

FD-155 shows that the fixed-`S` statement hides a severe **cross-family** resource law when one tries to reduce the anchored source mass. For the direct FD-154 edge measure the limiting parent distortion is exactly

`P^*(S)=(2^|S|-1)/(1-a(S))`,

where `a(S)=prod_(p in S) p/(p+1)`. At fixed cardinality the first `s` primes minimize `a(S)`. Since `a_s=(log s)^(-1+o(1))`, obtaining `a(S)<=alpha` requires

`s_alpha=exp(alpha^(-1+o(1)))`

coordinates, and the best parent distortion within these direct prime-avoidance frames obeys

`log log P_dir(alpha)=alpha^(-1+o(1))`.

The maximal direct ancestry depth is already `s_alpha`. Thus the coercive constant itself can remain excellent while the architecture that realizes it becomes singly exponential in coordinate/depth budget and double exponential in parent load.

So ancestry depth and anchor mass are not interchangeable source-complexity currencies. Rank faces leave arbitrarily many unfixed prime coordinates and pay an overshoot law; a fixed finite-coordinate face absorbs all but finitely many coordinate directions and has bounded depth; driving that coordinate-face mass toward zero by adding more prime coordinates creates a much harsher direct-frame load law. Every comparison has to name the anchor family and the edge measure before importing one regime's lower bound into another.

The price has also not disappeared epistemically. Prime-avoidance anchors directly prescribe Möbius orientation on an arithmetic subset. FD-155 rules out the simplest hope that this source exposure can be made arbitrarily small merely by enlarging `S` at moderate geometric cost. It does **not** prove that every sparse Farey-native anchor must have double-exponential distortion: a different edge measure on the same face or a different divisor-closed geometry may obey a better joint law.

The next gate is therefore two-dimensional. First, determine whether the actual Farey observable supplies the anchor information without already reconstructing the source. Second, if the anchor is thinned, price the parent/child/depth costs of the actual ancestry architecture rather than only its cut constant. Only after both gates pass does the transfer to the Franel--Landau destination become meaningful.

A source-valid ancestry proposal should expose: anchor mass, anchor geometry, parent distortion, residual coordinate/rank depth, child distortion, how the anchor information is obtained, and the destination map. Applying a rank-tail law to a non-rank anchor is invalid; calling a macroscopic source anchor “cheap” because its edge depth is one is equally invalid; and extrapolating the FD-155 double-exponential law beyond its direct prime-avoidance frame is also invalid.

**Boundary.** These results concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed anchors. FD-155's sharp thinning law is specific to the direct prime-avoidance frames of FD-154. The chain does not exclude `L^infinity`, singular weights justified independently, alternative edge measures, different divisor geometries, non-divisibility observations, or genuinely nonlocal Farey/Fourier functionals. It proves coefficient-side resource laws, not source-native availability of the anchor and not an RH-strength destination estimate.
