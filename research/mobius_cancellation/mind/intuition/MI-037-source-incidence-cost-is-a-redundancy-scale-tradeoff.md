# MI-037 — Source-incidence cost is a second-order scale tradeoff whose generic endpoint is a diagonal projective cap problem

**Evidence level:** exact/literature-derived source-incidence consequence from [MC-312](../../findings/MC-312-generalized-hamming-source-redundancy-scale-tradeoff.md), with generic coding boundary from [MC-313](../../findings/MC-313-generalized-griesmer-erasure-list-boundary.md), second-order sharpening from [MC-314](../../findings/MC-314-second-order-source-scale-near-capacity-erasure-boundary.md), and exact projective reformulation from [MC-315](../../findings/MC-315-diagonal-projective-generalized-cap-frontier.md).

For fixed lower-prime representatives of `R` independent endpoint generators, let `A` be the binary source-incidence matrix, `n` its number of source coordinates, `Z` its largest source prime, and `d_t` the generalized Hamming weights of its row space. The source-cut theorem gives

`d_t log Z >= (1-(2+o(1))(R+1)/2^t) log y - O(1)`.

MC-313 shows why the first-order consequence is not yet arithmetic. At `t_R=ceil(2 log_2(R+1))`, generic full-length `[2R,R]` binary codes can realize `d_t=R-O(R/log R)` across the relevant hierarchy. MC-314 then isolates the second-order currency: if

`log Z <= ((1+eta_R)/R) log y`,

then

`R-d_(t_R) <= R eta_R/(1+eta_R)+2+o(1)`.

At exact equal share the allowed defect is only `2+o(1)`, while `eta_R=o(1/log R)` already forces a defect smaller than the generic guarantee currently proved.

MC-315 removes an ambiguity in what must be proved next. For a full `[2R,R]` code, view the generator columns as a spanning multiset `M` of `2R` points in `PG(R-1,2)`. The exact identity

`2R-d_t(C)=max_(codim U=t) M(U)`

turns the constant-defect endpoint into a diagonal generalized-cap question: can one choose `2R` spanning projective points so that every codimension-`t_R` subspace contains at most `R+2` of them? Writing `N_R` for the maximal admissible multiset size, generic realizability is exactly the question whether `N_R>=2R` eventually.

This is stronger than saying that current coding bounds are inconclusive. It identifies the precise matched-control frontier. Standard incidence averaging and classical one-weight bounds miss the diagonal scale by large factors, so neither their success nor failure decides the endpoint. The next generic theorem is a finite-geometry theorem about simultaneous high-codimension caps.

The reusable lesson is that **source scale, hereditary redundancy and ambient realizability must be priced in the same asymptotic regime**. A small source-scale error becomes an additive generalized-weight defect, and that defect must then be compared with the exact projective incidence envelope rather than with a coarse coding inequality.

**Boundary.** The projective multiset is an abstraction of a generic binary representation; MC-315 does not prove that such a `2R`-point configuration exists or fails. The actual arithmetic Legendre-incidence columns satisfy additional provenance constraints not encoded by arbitrary projective geometry. None of MC-312--MC-315 estimates `M(x)` or closes the Möbius endpoint.