# MI-011 — Canonical deflation cancels crowding through two states; any half-line conditioning loss is collective

**Evidence level:** exact for every fixed finite set of pairwise distinct right-half zero states through [NB-095](../../findings/NB-095-finite-distinct-zero-states-add-their-growing-depth-volume-repair.md), [NB-096](../../findings/NB-096-canonical-deflation-cancels-raw-cauchy-crowding-volume.md), and the canonical-pivot/two-state conditioning theorem [NB-097](../../findings/NB-097-canonical-deflation-has-unit-pivots-and-uniform-two-zero-conditioning.md). Growing cardinality, finite-window uniformity, confluent/multiple zeros and target-distance conversion remain open.

For a fixed distinct zero set `F`, the raw normalized exponential-state Gram has the Cauchy determinant

`det G_F(infinity)=prod_(r<s) delta_(rs)^2`,

where `delta_(rs)=|(lambda_r-lambda_s)/(lambda_r+conj(lambda_s))|` is the pseudo-hyperbolic separation. Raw zero-state crowding therefore appears to collapse state volume as zeros approach one another.

NB-096 shows that the actual Nyman causal coordinates cancel this volume loss exactly. Successive canonical Blaschke deflation introduces an upper-triangular matrix `T_F` with

`|det T_F|^2 = prod_(r<s) delta_(rs)^(-2)`,

so `|det T_F|^2 det G_F(infinity)=1`. The apparent Cauchy crowding penalty and the deflation-coordinate gain are reciprocal.

NB-097 strengthens this from a final determinant identity to every finite prefix. If

`C_F=T_F^* G_F(infinity) T_F`,

then every leading principal minor of `C_F` is exactly one. Equivalently its Cholesky factor is unit upper triangular: **every canonical Schur pivot is identically one**. Growing conditioning therefore cannot arise from a sequence of collapsing canonical pivots.

The two-zero case closes the most obvious spectral loophole as well. For distinct zero states,

`C_2 = [[1,chi],[conj(chi),1+|chi|^2]] = [[1,chi],[0,1]]^* [[1,chi],[0,1]]`,

with `|chi|<=2`. Hence

`(3-2 sqrt(2)) I <= C_2 <= (3+2 sqrt(2)) I`

uniformly over all locations and through arbitrarily close distinct-zero collisions. Pairwise crowding can saturate this bounded shear, but it cannot create an unbounded two-state condition number after canonical deflation.

The half-line growing-divisor frontier is therefore genuinely many-body. Unit pivots do not control a high-dimensional unit-triangular matrix: collective off-diagonal shear in the Cholesky factor can still grow with `|F|`. A counterexample to uniform conditioning must involve at least three states or increasing dimension; it cannot be attributed to one near-colliding pair or to a hidden determinant tax.

Even uniform half-line shear control would not finish the Nyman problem. One must still make the replacement of the finite-window Gram by its half-line limit uniform in the growing divisor, control the currently `O_F(m^-1)` discretization and accumulated diagonal-normalization costs, handle genuine confluent/multiple-zero causal states, and convert generator-state geometry into the target Nyman distance.

**Boundary.** Canonical deflation is not generally the Takenaka--Malmquist orthogonalization; `C_F` need not be the identity. NB-097 proves uniform two-state conditioning, not dimension-free conditioning for arbitrary finite divisors. Distinct-zero collision limits are path-dependent and do not define the repeated-factor/Jordan system.
