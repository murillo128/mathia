# MI-026 — Full natural-prefix oversampling does not cure logarithmic-rank near-confluence

**Evidence level:** exact matched-control conditioning obstruction from [NB-136](../../findings/NB-136-full-natural-prefix-oversampling-still-permits-superpolynomial-matched-packet-conditioning-collapse.md), refining the recurrence/representation boundaries in NB-133--NB-135

NB-128 shows that the full natural prefix can resolve one common vertical translation at scale `1/log R`. NB-136 shows that this single-parameter resolution does not imply stable recovery of a whole logarithmic-rank packet.

For any fixed polynomial height exponent `A>0`, choose `0<c<0.10076A`. There are formal simple right-half packets of rank

`d_R=floor(c log R)`

whose heights and horizontal depths satisfy the same coarse zero-count and Vinogradov--Korobov envelopes used in NB-132--NB-135, while all ordinates lie in an `o(1)` cluster. Using **every** natural sample `1<=n<=R`, the evaluation matrix

`V_R=(n^(-conj(rho_j)))_(n,j)`

has normalized smallest singular value at most

`exp(-(cB+o(1))(log R)^2)`

for an arbitrary fixed `B>0`. Equivalently its condition number is superpolynomial, and a unit coefficient combination can be uniformly that small on the entire natural prefix.

Thus the failure is not sample scarcity: `R` observations are available for only `Theta(log R)` modes. It is high-order near-confluent cancellation. Zero-count rank, polynomial height, horizontal zero-free depth and natural-prefix oversampling do not control the relative arrangement that determines the lower frame bound.

The reusable distinction is between **translation resolution** and **packet conditioning**. A representation may resolve a one-dimensional motion sharply while becoming almost singular on a growing collection of nearby modes. Stable packet access needs an additional source law on separation, local multiplicity, coefficient occupation, divided-difference structure, or a representation whose conditioning is intrinsically stable under confluence.

**Boundary.** The NB-136 packets are matched formal packets, not asserted zeta zeros, and the bad singular vector is not asserted to equal the actual Nyman coefficient vector. The result says only that the current coarse actual-zero envelopes cannot by themselves supply a polynomial lower frame bound for the full natural-prefix zero-power coordinates.