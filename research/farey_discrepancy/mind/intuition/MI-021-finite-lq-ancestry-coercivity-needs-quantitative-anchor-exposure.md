# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and its cost depends on anchor geometry

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-156](../../findings/FD-156-one-parent-prime-face-forests-force-exponential-expansion-load-tradeoff.md).

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

FD-156 identifies the architecture-invariant core of that bill for every **one-parent** forest on the same face. The `2^s-1` nontrivial squarefree divisors of `P_S` form a forced Boolean packet whose ancestry chains all terminate at the anchor root `1`. Removing the root partitions that packet among disjoint descendant branches. Testing the lightest branch in the anchored Cheeger quotient gives the exact universal tradeoff

`P_(S,T)^pi / h_(S,T)^pi >= 2^s-1`.

The direct star attains equality, so it is product-optimal over the complete one-parent class. A sequential parent map illustrates the only available rearrangement: it lowers anchor load from exponential to `s K_(S,T)` but simultaneously lowers expansion to `K_(S,T)/2^(s-1)`. Unique-parent rerouting can move the exponential bill from congestion into a narrow descendant cut; it cannot remove it.

Consequently, at any fixed positive expansion, the FD-155 double-exponential thinning cost survives arbitrary one-parent depths and arbitrary nonnegative edge weights. This is stronger than the earlier direct-frame statement but still geometry-specific: it uses the pure-prime Boolean packet forced by the finite-prime avoidance anchor and the partition property of unique ancestry.

So ancestry depth, anchor mass, parent load and expansion are not interchangeable source-complexity currencies. Rank faces leave arbitrarily many unfixed prime coordinates and pay an overshoot law; a fixed finite-coordinate face absorbs all but finitely many coordinate directions and has bounded depth; driving that coordinate-face mass toward zero creates a large Boolean packet; one-parent architectures must pay for that packet either at the anchor or through loss of cut exposure.

The remaining escape on this anchor is genuinely **multi-parent**, or else a different divisor-closed geometry. A DAG may let several ancestry edges share the Boolean packet without partitioning it into disjoint root branches, so FD-156 does not decide that case. Nor does any of this solve the epistemic gate: a Farey-native observable must still supply the anchor orientation without reconstructing Möbius, and the resulting coefficient norm must still control the nonlocal Franel--Landau destination.

A source-valid ancestry proposal should expose: anchor mass, anchor geometry, parent distortion, anchored expansion, residual coordinate/rank depth, child distortion, whether the graph is one-parent or genuinely multi-parent, how the anchor information is obtained, and the destination map. Applying a rank-tail law to a non-rank anchor is invalid; calling a macroscopic source anchor “cheap” because its edge depth is one is invalid; and proposing a clever unique-parent rerouting after FD-156 does not change the `2^s-1` expansion/load product law.

**Boundary.** These results concern binary Möbius orientations, finite `L^q`, positive divisibility-ancestry observations and divisor-closed anchors. FD-156's sharp law covers arbitrary nonnegative **one-parent** forests on the finite-prime avoidance face, not multi-parent DAGs, signed edge measures, different anchor geometries, `L^infinity`, non-divisibility observations, or genuinely nonlocal Farey/Fourier functionals. The chain proves coefficient-side resource laws, not source-native availability of the anchor and not an RH-strength destination estimate.