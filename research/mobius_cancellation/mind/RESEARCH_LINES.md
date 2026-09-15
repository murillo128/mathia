# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert forced source-incidence cost into an arithmetic realizability obstruction beyond generic half-rate coding

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-039-generic-half-rate-codes-realize-the-constant-defect-endpoint`.

MC-307--MC-312 turn endpoint projection and source cuts into a hereditary generalized-Hamming support law. MC-313 identifies the coarse coding boundary, MC-314 makes the natural equal-share source demand precise at constant defect, and MC-315--MC-316 show that the corresponding projective occupancy, systematic submatrix-rank, primal/dual generalized-weight and erasure formulations are all presentations of the same generic endpoint.

MC-317 closes that generic endpoint in the permissive direction. For all sufficiently large `R`, there exist full binary `[2R,R]` codes with

`d_(t_R) >= R-2`,  `t_R=ceil(2 log_2(R+1))`.

The construction uses a finite-blocklength random-linear erasure list-recovery theorem at a gap `epsilon_R=Theta(1/R)`, obtains a code only `O(1)` dimensions below half rate with `O(R)` lists, and then augments those missing dimensions at only a constant list-size factor. Consequently the diagonal generalized-cap envelope satisfies `N_R>=2R` eventually, and systematic matrices with the entire MC-316 rank profile do exist.

The generic projective/coding route is therefore exhausted at the natural constant-defect scale. Length, dimension, generalized weights, projective occupancy, ordinary erasure capacity, systematic submatrix ranks and their primal/dual recodings do **not** distinguish the arithmetic source from matched binary controls.

The live theorem is now source-specific. Either prove the source scale sharp enough to enter the constant-defect regime **and** identify a Legendre/reciprocal-prime incidence property that arbitrary `[2R,R]` codes need not satisfy, or derive a different arithmetic invariant whose endpoint cost is not already realized by the MC-317 controls. The obstruction must constrain realizability of the actual source matrices, not strengthen another generic code inequality on the same rank profile.

## Identify the arithmetic property excluded by random-linear matched controls

**Linked intuition:** `MI-039-generic-half-rate-codes-realize-the-constant-defect-endpoint`.

MC-317 removes the matrix-existence problem itself. The useful comparison class now contains exact matched controls at the endpoint, so a proposed arithmetic restriction should be stated as a property of the source-incidence matrices `P_R` that the random-linear/augmented controls are not forced to obey.

Candidates must be tested in the exact destination currency. A source restriction is relevant only if it forces a stronger generalized-weight/support defect, forbids the required submatrix profile, or yields another endpoint inequality not implied by generic half-rate coding. Merely noting that the arithmetic matrices are structured, deterministic, Legendre-derived or sparse in their construction is not coercivity until that structure excludes the known matched controls quantitatively.

## Keep target projection, source scale, generalized-weight defect and arithmetic realizability distinct

A large number of expensive endpoint directions is not the same as expensive common support. The source package is priced simultaneously by its coordinate count, largest-prime scale and hereditary support profile. MC-314 shows that a first-order statement `log Z=(1+o(1))log y/R` is too coarse unless the error is quantified on the `1/log R` scale; MC-315--MC-317 then show that even the resulting constant-defect support endpoint is generically realizable.

Any closing argument must state which source quotient is used, what representative package is fixed, how source supports overlap, what `eta_R` is actually proved, and which additional arithmetic property places the realized systematic matrix outside the now-established generic endpoint class.

## Preserve matched controls through the second-order boundary

MC-317 is now the sharp matched control for the diagonal half-rate endpoint: the constant-defect demand itself survives generic binary coding. Future work must preserve that control rather than infer arithmetic coercivity from the gap between coarse `O(R/log R)` bounds and `O(1)` defect, or count primal and dual constraints twice. Progress requires an arithmetic theorem that the matched code family can fail.