# MI-053 — Top-half antichains make linear density the sharp signed omission threshold

**Evidence level:** exact constructive synthesis from [FD-256](../../findings/FD-256-linear-density-exact-omissions-can-saturate-signed-capacity.md), paired with the sublinear upper bound of FD-255.

The macroscopic signed exact-omission transition is a density threshold, not an incidence-conditioning threshold. FD-255 proves that `K=o(H)` omitted response values cannot hide `Theta(H^2)` coefficient mass under `|b_n|<=C n`. FD-256 shows that `K=Theta(H)` can hide that scale almost maximally by moving the defects into the top divisibility antichain.

For `e>H/2`, neither `e` nor `e+1` has a second multiple below `H`. An isolated response spike `Y(e)=e` therefore produces the exact coefficient pair

`b_e=e`, `b_(e+1)=-e`

with no cross-talk to the rest of the horizon. `K` disjoint adjacent pairs contribute more than `KH` top-band mass. At `H=4M`, `K=M`, the pairs partition `(H/2,H]` and their coefficient mass is `6M^2` against the maximum envelope capacity `6M^2+M`, so the relative saturation tends to one.

This identifies the structural reason the threshold changes at linear density. Sparse defects must propagate through global Möbius rows and lose macroscopic reachability; a positive density of defects can instead occupy a region where divisibility below the horizon is effectively diagonal. The transition does not require a badly conditioned divisor-incidence matrix.

The useful residual signed question is only the sublinear extremal rate: FD-255 gives an upper scale `KH log(e+log(H/K))`, while FD-256 supplies `KH` constructively where its disjoint-pair geometry applies. Closing that slowly varying gap would sharpen the norm but not alter the macroscopic threshold.

**Boundary.** The construction is signed and finite-horizon. Its negative right-endpoint coefficients are of the same order as its positive ones, so it is not a nonnegative Farey source and does not bypass the source-side positivity/capacity obstruction. The density threshold proved here belongs to the exact signed response map.