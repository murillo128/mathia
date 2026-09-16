# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and its cost depends on anchor geometry

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-154](../../findings/FD-154-finite-prime-avoidance-anchors-give-exact-finite-depth-coercivity.md).

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

So ancestry depth is not an intrinsic source-complexity currency. It is a cost **relative to the geometry of what has already been anchored**. Rank faces leave arbitrarily many unfixed prime coordinates and pay an overshoot law; a finite-coordinate face absorbs all but finitely many coordinate directions and has bounded depth.

The price has not disappeared. Prime-avoidance anchors directly prescribe Möbius orientation on a macroscopic arithmetic subset: for one prime `ell`, anchor mass tends `ell/(ell+1)`, and for `ell=2` it is `2/3`. The next gate is therefore not another generic ancestry-depth lower bound. It is whether the actual Farey observable supplies that macroscopic coordinate-face information **without already reconstructing the source** and whether the resulting exact coefficient coercivity transfers to the Franel--Landau destination.

A source-valid ancestry proposal should expose: anchor mass, anchor geometry, parent distortion, residual coordinate/rank depth, child distortion, how the anchor information is obtained, and the destination map. Applying a rank-tail law to a non-rank anchor is invalid; calling a macroscopic source anchor “cheap” because its edge depth is one is equally invalid.

**Boundary.** These results concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed anchors. They do not exclude `L^infinity`, singular weights justified independently, non-divisibility observations, or genuinely nonlocal Farey/Fourier functionals. FD-154 proves coefficient-side coercivity, not source-native availability of its anchor and not an RH-strength destination estimate.
