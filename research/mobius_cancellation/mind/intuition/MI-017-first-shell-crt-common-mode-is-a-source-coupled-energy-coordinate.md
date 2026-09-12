# MI-017 — First-shell parity is already a singleton-cell problem, but not a divisibility-pairing problem

**Evidence level:** supported by the exact CRT and incidence-cell reductions in MC-228--MC-231; no new Möbius cancellation estimate is claimed.

For the first square-defect shell, MC-228--MC-229 show that high incidence is cheap by support. Incidence above one quarter of `log X/loglog X` contributes only target-scale weighted energy, so the hard source region is low/mesoscopic incidence.

MC-230 removes a further apparent coupling obligation. If `C_S` is the signed Möbius sum on the exact incidence cell `I_y(n)=S` and

\[
\mathcal C_y(X)=\sum_S w(S)|C_S(X)|^2,
\]

then the number of possible shell subsets is `X^{o(1)}` and

\[
W_y(X)\le X^{o(1)}\mathcal C_y(X).
\]

Thus cross-cell anti-alignment is not power-essential: target-scale aggregate cancellation inside the exact cells is already sufficient.

MC-231 shows that this cellwise problem is not merely mesoscopic. For each shell coordinate `d`, the exact singleton cell retains asymptotically all of its nonzero square-free support and therefore reproduces the same unsigned `X^{2-o(1)}` energy scale. The difficult parity geometry is already present when the input hits exactly one shell square.

At the same time, multiplicativity does not give a cheap internal involution. If `m<n` lie in the same singleton cell and `m|n`, then

\[
\frac nm\equiv1\pmod{d^2},
\]

so the ratio is at least `d^2+1`. Any disjoint opposite-sign pairing built from same-cell divisibility must use its smaller endpoint below `X/(d^2(d^2+1))` and can touch only an `o(1)` fraction of the singleton support. Adding or removing factors while preserving the cell therefore cannot be the missing parity certificate.

The remaining theorem must control Möbius signs among mostly divisibility-incomparable singleton inputs, or introduce genuinely additive, bilinear, harmonic, or cross-cell arithmetic information. The exact-cell diagonalization makes inter-cell cancellation optional; MC-231 makes naive intra-cell multiplicative matching ineffective.

**Boundary.** The diagonal target is sufficient rather than necessary, and MC-231 rules out only disjoint same-cell divisibility pairings. It does not rule out many-to-many identities, additive pairings, spectral methods, or source-coupled mechanisms that move between cells.
