# MI-007 — Aliased radial prediction has a positive Szegő floor

**Evidence level:** exact for the single-integer-dilation radial certificate through NB-085. Whether the aggregate floor charge stays bounded on an unbounded sequence remains open, and failure of the radial certificate does not classify the full nonstationary future.

NB-084 turns each integer-dilation descendant ray into an anchored Toeplitz prediction problem with the actual periodized spectral density `W_(j,q)`. NB-085 proves more than almost-everywhere positivity: one central alias plus the exact Nyman source formula gives `log W_(j,q) in L^1(T)`. Szegő--Kolmogorov therefore yields a strictly positive geometric-mean floor `G_(j,q)` and `E_(j,q,L) downarrow G_(j,q)`.

This changes the role of depth. For qualitative stable-tail exclusion, the relevant quantity is the aggregate mismatch `S_(R,q)=sum_(j<R) log(G_(j,q)/PiHat_(j,R)^2)`. If that charge is bounded along unbounded `R`, finite depths can always be chosen far enough down each ray to obtain the required bounded certificate. If the charge diverges, increasing depth on the same ray can never repair it.

Thus the radial route has a **floor gate before a rate gate**. Convergence speed becomes important only after the floor is acceptable and one asks for a prescribed quantitative horizon. A poor radial floor is not a stable-tail theorem; it redirects the search toward cross-ray or genuinely nonradial prediction.

**Boundary.** The Szegő floor is ray-specific and source-specific. NB-085 does not estimate its large-`j,R` aggregate size, prove bounded floor charge, or show that the full future shares the radial obstruction.