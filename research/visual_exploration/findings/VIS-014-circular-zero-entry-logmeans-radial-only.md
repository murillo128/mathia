# VIS-014 — circular zero-entry log means collapse to radial distance data

## Claim

Let `xi` be Riemann's entire xi function, let `rho` be a zero of exact multiplicity `m>=1`, and normalize away the complete local zero monomial as in `VIS-012` and `VIS-013`:

`H_rho(w)=xi(rho+w)/(a_m w^m)`, with `H_rho(0)=1`.

For a radius `r>0` such that no remaining zero lies on `|w|=r`, define the circular log-modulus mean

`J_rho(r)=(1/(2 pi)) int_0^{2 pi} log|H_rho(r e^{i theta})| d theta`.

Then Jensen's formula gives the exact identity

`J_rho(r)=sum_{rho' != rho, |rho'-rho|<r} m(rho') log(r/|rho'-rho|)`,

where remaining zeros are counted with their multiplicities `m(rho')`.

Equivalently, if `x=log r` and `d_j=|rho_j-rho|` lists the remaining zero distances with multiplicity, then

`J_rho(e^x)=sum_j (x-log d_j)_+`.

Consequently, away from entry radii,

`d/dx J_rho(e^x)=N_rho(e^x)`,

where `N_rho(r)` is the number of remaining zeros in the centered disk `|w|<r`, counted with multiplicity, and in the distributional sense

`d^2/dx^2 J_rho(e^x)=sum_j delta_{log d_j}`.

Thus the complete circular-mean zero-entry profile is **equivalent to the radial zero-distance multiset**. It erases every angular coordinate. Two zero configurations with the same centered distances but radically different angular arrangement have exactly the same `J(r)`.

**Evidence/status:** `CLASSICAL-JENSEN + EXACT-DERIVED + NEGATIVE/BASELINE`.

No novelty is claimed for Jensen's formula, its zero-counting form, or the hinge representation above. The durable Mathia consequence is that the most obvious scalar zero-entry extension left open by `VIS-013` does not supply a new mesoscopic geometry.

## Exact derivation

`H_rho` is entire after the removable singularity at `w=0` is filled and satisfies `H_rho(0)=1`. Fix `r` with no remaining zero on the boundary circle. Jensen's formula for a holomorphic function nonzero at the center states

`(1/(2 pi)) int_0^{2 pi} log|H_rho(r e^{i theta})| d theta
 = log|H_rho(0)|
   + sum_{|a_j|<r} log(r/|a_j|)`,

where `a_j` are the zeros of `H_rho` inside the disk, repeated by multiplicity.

Here `log|H_rho(0)|=0` and the zeros of `H_rho` are exactly the remaining xi zeros translated by `-rho`. This yields the claimed sum.

Writing `r=e^x` turns each zero contribution into

`1_{x>log d_j}(x-log d_j)=(x-log d_j)_+`.

Differentiating between entry radii gives one unit of slope per enclosed zero. Distributionally, each slope change contributes a point mass at its log-radius. Therefore `J` determines and is determined by the multiset `{d_j}`.

The angular-loss statement is immediate: the right-hand side contains `|a_j|` but not `arg(a_j)`. Any angular rearrangement preserving all radii leaves the whole circular-mean profile unchanged.

## Visual check and matched control

The retained artifact

`research/visual_exploration/visualizations/zero-entry-jensen-radial-collapse.md`

uses the 100th critical-line zeta zero as center and 24 neighboring zeros, with the plotting scale

`Delta = 2 pi / log(Im(rho)/(2 pi))`.

The actual local zero coordinates are compared with a deterministic angle-scrambled surrogate that preserves every centered distance exactly but destroys the collinear angular geometry. Over the window `r<=11.3 Delta`, the next omitted zeros lie beyond `12.75 Delta`, so every zero that can enter a plotted disk is included.

For the normalized finite product

`P(w)=prod_j (1-w/a_j)`,

direct 4096-angle quadrature of the circular log mean agrees with the Jensen radial formula to at worst about `1.6e-10` on sampled radii kept away from entry circles. The actual and angle-scrambled products agree with one another to about `4.8e-11`.

This computation is only a numerical integrity check and visualization of the exact identity. The mathematical evidence is Jensen's formula.

## Research consequence

`VIS-013` showed that nested circular shells **before** the first additional zero enters are Poisson-determined by one outer shell. The accepted multiscale clue therefore moved its attention to genuine zero-entry events.

`VIS-014` now removes the simplest scalar version of that escape. Once entry begins, the circular average of `log|H_rho|` is not a new scale observable: it is exactly an integrated zero-counting function for centered radial distances. Its kinks, slopes, and apparent multiscale staircase are forced by the entry radii.

For a center and neighboring zeros all on the critical line, those radii are absolute ordinate differences, so the profile is a deterministic transform of cumulative local gap distances. Without RH, the statement remains exact but records only Euclidean distances in the complex plane and still discards angular arrangement.

A surviving mesoscopic visual statistic must therefore use information that Jensen's radial average deletes. Plausible targets include nonzero angular Fourier modes after explicit zero-entry terms are removed, angular organization of several simultaneously visible zeros, non-circular domains, or cross-center comparisons that cannot be reconstructed from the radial distance multiset.

This does not show that zero-entry geometry is empty. It shows that **radially averaged** zero-entry geometry is already completely classified by classical zero-counting data.

## Prior art and novelty assessment

Jensen's formula is classical complex analysis. Stein and Shakarchi, *Complex Analysis*, Chapter 5 §1, present it explicitly as the relation between zeros in a disk and the logarithmic circular average of a holomorphic function. The equivalent integral form

`J(r)=int_0^r N(t) dt/t`

is also standard.

`VIS-014` claims no new Jensen theorem, zero-counting theorem, or zeta result. Its role is a negative-control specialization: it identifies a visually natural candidate multiscale statistic from the current `visual_exploration` clue as an exact re-encoding of centered radial zero distances.

The angle-scrambled control is not literature evidence. It is a direct demonstration of the information quotient already visible in the formula.

## Boundary conditions and falsification

The displayed formula is stated for radii with no zero on the boundary. Boundary entry values can be handled by limiting versions, but no such refinement is needed for the research consequence.

The result concerns the **zeroth angular Fourier mode**, i.e. the circular mean. It does not classify the nonzero angular modes of `log|H_rho|` after zeros enter the disk. Those modes retain angular information through Poisson-Jensen/Blaschke-type terms and remain a legitimate place to search.

The radial profile may encode an arbitrarily long vector of zero distances; the claim is not that a small fixed list of gaps reconstructs it. The claim is that the profile contains no information beyond that radial-distance multiset.

The statement is independent of RH and of any simplicity assumption at the central zero because the full central multiplicity is removed before applying Jensen's formula.
