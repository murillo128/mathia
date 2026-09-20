# MI-041 — Direct original-period Minkowski decimation closes Wang branchwise occupancy without a center-gap hierarchy

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-329](../../findings/VIS-329-direct-minkowski-decimation-closes-wang-transition.md), plus classical rational mechanical-word geometry, Minkowski's convex-body theorem and the dimension-two Selberg upper-bound sieve. No prime-pair asymptotic or RH consequence is claimed.

The cutoff-free Wang remainder has no useful global nearest-frequency spacing, but dyadic shells reduce the finite-window loss to simultaneous-prime occupancy on a few rational mechanical branches with a taper-weighted destination. VIS-317--VIS-324 identify faithful unimodular Bézout coordinates and show that sufficiently long affine packets have the natural two-prime Selberg upper-bound scale.

VIS-325--VIS-328 originally treated fragmentation through the center-gap denominator `k=|u-v|`: lower-denominator mechanical words, Christoffel parents and finally a determinant-`k` Minkowski vector progressively closed the range `k>L`. That analysis correctly exposed how packet length, arithmetic dimension and conductor have to be controlled together, but it left a near-maximal transition when `k<=L`.

VIS-329 shows that the transition belonged to the intermediate representation. Return to the original Wang phase denominator `m=max(u,v)` with `L<m` and the lattice

`Lambda_(c,m)={(s,e) in Z^2 : e=cs (mod m)}`.

Its covolume is `m`, so Minkowski gives a nonzero vector with `1<=s<=2 sqrt(m)` and `1<=E=|e|<=2 sqrt(m)`. Along an `s`-step, the branch has one constant Wang displacement except at at most `E` edges. Removing those edges partitions the whole candidate branch into at most `s+E` affine runs. The same vector makes the step coefficients `O(E)` and the two-form resultant `O(s+E)`, so the arithmetic conductor is polynomial in `M`; at the natural scale the step is automatically nondegenerate.

The classical two-form upper-bound sieve then gives, uniformly in the center gap,

`P_j << L (log log M)^2/log^2 M`

when `L asymp M/log log M` and `m asymp M`. Relative to the natural two-prime cell scale this is only `A_M=O((log log M)^2)`, and its square root lies inside the taper allowance isolated in VIS-316. The complete natural subperiod branchwise occupancy problem is therefore closed at the required upper-bound scale.

The reusable lesson is stronger than “fragmentation should be renormalized.” A faithful representation should be judged by the finite-window cost it exposes, not by whether its intermediate symbolic decomposition looks canonical. The source-native period `m` already carries a short Diophantine vector that controls **packet count, exceptional edges, arithmetic dimension and conductor simultaneously**. Passing first to the center-gap denominator can reveal structure, but it is not automatically the representation that should govern the final estimate.

This moves the critical path away from branchwise Wang occupancy. The remaining source-sensitive question is the fixed-power real-axis route: whether the squared-von-Mangoldt source admits a quantitatively useful statement strictly weaker than the RH-equivalent half-plane pole exclusion already isolated by VIS-293. Occupancy refinements should be reopened only if a later destination needs more than the VIS-316 upper-bound criterion or a flaw is found in the direct decimation.

**Boundary.** VIS-329 is an upper-bound closure for the moving-upper candidate branches in the subperiod regime `L<m`. It does not give a prime-pair asymptotic, lower bound, complete Wang theorem, improved fixed-power source estimate or stronger RH criterion. Center-gap/Christoffel descriptions remain valid mathematics; they are simply not load-bearing for this upper-bound destination.