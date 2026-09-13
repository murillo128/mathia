# MI-011 — Canonical deflation cancels raw Cauchy crowding at determinant level, not at conditioning level

**Evidence level:** exact for every fixed finite set of pairwise distinct right-half zero states through [NB-095](../../findings/NB-095-finite-distinct-zero-states-add-their-growing-depth-volume-repair.md) and [NB-096](../../findings/NB-096-canonical-deflation-cancels-raw-cauchy-crowding-volume.md). Growing cardinality, confluent/multiple zeros and target-distance conversion remain open.

For a fixed distinct zero set `F`, the raw normalized exponential-state Gram has the Cauchy determinant

`det G_F(infinity)=prod_(r<s) delta_(rs)^2`,

where `delta_(rs)=|(lambda_r-lambda_s)/(lambda_r+conj(lambda_s))|` is the pseudo-hyperbolic separation. Raw zero-state crowding therefore appears to collapse the state volume as zeros approach each other.

But the actual Nyman construction does not use those raw coordinates. Successive canonical Blaschke deflation introduces a triangular change of coordinates `T_F` whose diagonal factors satisfy

`|det T_F|^2 = prod_(r<s) delta_(rs)^(-2)`.

Hence

`|det T_F|^2 det G_F(infinity)=1`

**exactly**. The apparent Cauchy crowding penalty and the deflation-coordinate gain are reciprocal. For the interacting leverage matrix this sharpens the fixed-finite law to

`q^(-2 A_F) det M_(m,q) -> 1`

when `m,q -> infinity`, and therefore the unnormalized determinant repair has leading coefficient one:

`det K^[F]/det A = q^(2 A_F)(1+o_F(1))`.

The cancellation is only volumetric. It does not imply `T_F^* G_F T_F=I`, and near collisions can still make the smallest singular value tiny while the determinant remains canonically normalized. Exact confluence/multiple zeros also require a different Jordan/confluent state system. Likewise the diagonal-normalization cost in the final correlation determinant remains only `O_F(1)`, not known to vanish uniformly.

So raw Cauchy determinant crowding is **not** the hidden growing-family tax. If a growing-divisor extension fails, the obstruction must be stronger: spectral conditioning, finite-window loss with increasing dimension, nonuniform discretization error, accumulated coordinate-normalization cost, or genuine confluent structure.

**Boundary.** This remains generator/correlation-volume geometry. It does not convert the finite-state repair into a lower bound for the Nyman target distance, and the exact fixed-finite determinant cancellation must not be extrapolated to growing `|F|` without uniform spectral control.