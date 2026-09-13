# MI-007 — Radial Szegő charge is bounded below by visible terminal correlation entropy

**Evidence level:** exact for the single-integer-dilation radial certificate through NB-086. Whether the terminal visible correlation energy diverges or the aggregate floor charge stays bounded on an unbounded sequence remains open; failure of the radial certificate does not classify the full nonstationary future.

NB-084 turns each integer-dilation descendant ray into an anchored Toeplitz prediction problem with the actual periodized spectral density `W_(j,q)`. NB-085 proves `log W_(j,q) in L^1(T)`, so Szegő--Kolmogorov yields a strictly positive geometric-mean floor `G_(j,q)` and the finite-depth prediction error decreases to that floor.

This makes the aggregate mismatch `S_(R,q)=sum_(j<R) log(G_(j,q)/PiHat_(j,R)^2)` the qualitative gate. If it is bounded along unbounded `R`, finite radial depths can be chosen afterwards; if it diverges, additional depth on that fixed ray cannot repair the certificate.

NB-086 now produces a finite-window lower bound that avoids estimating the individual Szegő floors. On the terminal block `j>=ceil(R/q)`, the first radial descendant `qj` lies beyond the visible cutoff, so radial prediction cannot alter the current window at all. The unrestricted causal future still contains all intermediate visible innovations. Reverse Gram--Schmidt therefore gives

`S_(R,q) >= -log det R_(R,q)`,

where `R_(R,q)` is the normalized Gram/correlation matrix of those terminal visible innovations.

The determinant deficit has a quantitative consequence: bounded radial floor charge forces the total squared off-diagonal correlation energy of the entire growing terminal block to remain `O(1)`. Conversely, divergence of that normalized terminal pair-correlation energy forces `S_(R,q)->infinity`. Thus a fixed-`q` radial proof can be falsified using only visible finite-window source geometry, before any detailed asymptotic analysis of the aliased spectral floors.

The live source test is now concrete: determine whether the actual Nyman terminal innovations become sufficiently decorrelated to keep this correlation entropy bounded, or whether their normalized visible correlation energy accumulates. Exact branching and global long-range mass alone do not decide this because they control different, unnormalized correlation quantities.

**Boundary.** NB-086 gives a necessary condition for bounded single-ray charge, not its converse and not a theorem about the full nonstationary future. Divergent radial correlation entropy redirects the proof toward cross-ray/nonradial cancellation; it does not imply a nonzero stable tail.