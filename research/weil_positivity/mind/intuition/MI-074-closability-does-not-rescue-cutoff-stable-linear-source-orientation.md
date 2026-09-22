# MI-074 — Closability does not rescue cutoff-stable linear source orientation

**Evidence level:** exact RH-independent functional-analytic obstruction from [WP-402](../../findings/WP-402-cutoff-stable-closable-source-orientations-are-trivial.md), extending the norm-density result of MI-073/WP-401 from bounded scalar readouts to possibly unbounded Banach-valued linear maps.

The unbounded-linear escape left by WP-401 is much narrower than it appears. Let `D` be a real linear source domain inside a hereditary fixed-shadow corner, stable under the canonical continuous cutoffs `k -> c_n k c_n`. Let `T:D->Y` be a linear map into a Banach space with a pointed cone, and suppose positivity of `d+h` is claimed to orient every admissible response into that cone. If `T` is closable in the source C-star norm, then `T` must vanish identically.

The mechanism is exact. For each `k in D`, cutoff localization gives `k_n=c_nkc_n -> k` while both sufficiently small signs `d±epsilon_n k_n` remain positive. Pointedness then forces `T(k_n)=0` for every `n`. The tails `r_n=k-k_n` satisfy `r_n->0` but `T(r_n)=T(k)`. Closability of the graph forces `T(k)=0`.

Thus **unboundedness alone is not a new orientation resource**. A nonzero linear source response of this type must fail at least one structural hypothesis: its domain must not be preserved by the canonical source cutoffs, its graph must be genuinely nonclosable/singular, or its sign must not arise as an ordinary pointed-cone consequence of positivity of the fixed-shadow fibre.

This is stronger than the bounded-readout conclusion of MI-073 because no norm continuity of `T` is used. The cutoff sequence itself supplies an explicit graph-defect witness for every attempted nonzero response. At the same time it does not collapse the whole unbounded category: closed cutoff-stable unbounded operators exist, but they cannot also satisfy this two-sided positivity-orientation rule nontrivially.

The durable audit for a proposed unbounded linear completion is therefore concrete. Check whether the source domain survives `k -> f_n(d) k f_n(d)` and whether the response is closable. If both hold, hereditary positivity cannot supply a nonzero linear orientation. A surviving mechanism must exhibit the cross-scale quantity destroyed by those cutoffs or leave the linear pointed-cone setting entirely.

**Boundary.** WP-402 does not rule out nonlinear or quadratic energies, one-sided domains, nonclosable singular maps, cutoff-unstable global relations, or a finite--archimedean assembly in which the source direction changes under completion. It is a matched-control obstruction using no prime arithmetic and supplies no Weil positivity by itself.