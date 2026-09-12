# MI-005 — Stable tails are the uncancelled cross-cut area of interval-conditioned correlations

**Evidence level:** supported by NB-063--NB-076. The stationary prediction/feedthrough criterion is exact for scalar branch filters, and NB-074--NB-076 give exact finite-dimensional continuation identities for the nonstationary causal geometry; no arithmetic estimate closing those criteria is proved.

NB-066--NB-073 reduce a hypothetical persistent Nyman target to a global continuation problem and show that local memory, finite causal flags, exact branching, far-mass necessity, and ordinary global Gram conditioning do not decide it. NB-074 gives the nonstationary charge `J_(R,N)`: bounded charge along an unbounded sequence rules out a stable tail, while any nonzero stable tail forces the charge to diverge for every finite horizon schedule.

NB-075 resolves that determinant into raw continuation volume `L_R` minus nonnegative future-conditioned multiple-correlation charges. NB-076 resolves the multiple correlations one step further. For `j<n`, residualize `D_j` and `D_n` against the intervening span `D_(j+1),...,D_(n-1)`, let `rho_(j,n)` be their endpoint correlation, and put

`kappa_(j,n)=-log(1-|rho_(j,n)|^2)>=0`.

Then the exact chain rule is

`-log(1-beta_(R,n)) = sum_(j<R) kappa_(j,n)`,

so

`J_(R,N)=L_R-sum_(j<R<=n<=N) kappa_(j,n)`.

Each lattice atom has the contiguous-Gram form

`kappa_(j,n)=log(Delta_(j,n-1) Delta_(j+1,n) / (Delta_(j,n) Delta_(j+1,n-1)))`.

It is therefore a nonnegative mixed log-determinant curvature for one contiguous interval. The entire future cancellation is the area of those atoms crossing the cut `R`; no atom is double-counted.

This produces a genuinely smaller source target. Define the width-`H` cross-cut band by summing `kappa_(j,j+h)` over `1<=h<=H` and intervals that cross `R`. If along unbounded `R_k` some finite `H_k` makes this band at least `L_(R_k)-C`, then the stable tail is zero. The stronger condition using the sum of `|rho_(j,j+h)|^2` also suffices.

The durable interpretation is that the obstruction is not “future prediction” in the abstract. It is a **deficit of interval-conditioned correlation area** relative to the raw continuation volume. An arithmetic proof may attack a finite/mesoscopic family of contiguous Gram blocks near the cut rather than one growing inverse Gram matrix.

**Boundary.** A nonzero stable tail forces the infinite remainder `L_R-sum_(j<R<=n)kappa_(j,n)` to diverge, but the converse is not asserted for a general growing-dimensional family. Raw pairwise correlations do not replace the conditioned `rho_(j,n)`; even raw-orthogonal endpoints can become strongly linked after the intervening block is removed. NB-076 supplies an exact localization of the cancellation budget, not the missing arithmetic lower bound.
