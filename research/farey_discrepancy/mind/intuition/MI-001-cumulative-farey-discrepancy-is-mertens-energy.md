# MI-001 — Farey transfer has a critical host budget, a polynomial-packet tradeoff, and a two-thirds normalization barrier

**Evidence level:** supported by exact source/occupation reductions through FD-064 plus the cited all-short-interval Möbius theorem; no positive global occupation theorem is claimed.

The cumulative Farey obstruction is controlled by the physical shell source

\[
c(n)=\Delta\mathcal H(n)=\sum_{dm=n}\frac{\mu(m)}d.
\]

FD-054--FD-058 separate deterministic transfer, genuine short-interval cancellation, sparse represented-start sampling, and maximal ambient-window localization. FD-059 identifies the deterministic critical host scale `Q_X=X/A_X`, where `A_X=|\mathcal H(X)|`: favorable squarefree hosts at `q\asymp Q_X` force a nearby nonsquarefree row that retains a fixed fraction of the spike. FD-060 shows that subpower slack can be spent on packet multiplicity.

FD-062--FD-063 show that physical short-interval cancellation changes the geometry and removes combinatorial host scarcity. If `A_X(\log X)^B\ge X^\vartheta`, `\vartheta>0.55`, then logarithmic saving can move the host below `Q_X` while buying a growing packet, and the packet lower bound can hold uniformly over an entire host corridor. Multiples of four provide the nonsquarefree density; a growing CRT modulus is not intrinsic.

FD-064 classifies the larger **power-gap** family. On a zero-frontier spike `A_X=X^{\Theta+o(1)}`, choose a host exponent

\[
1-\Theta<\lambda\le1-\vartheta,
\]

and packet exponent

\[
0<\kappa<\Theta+\lambda-1.
\]

Then `q\asymp X^\lambda` supports a polynomial packet `K_X=X^{\kappa+o(1)}` with

\[
U_{qX,D}\ge\left(\frac1{4\zeta(2)}-o(1)\right)K_XA_X^2.
\]

The new power is real locally: moving the host outward by `X^\delta` creates exactly `\delta` powers of packet budget. But after normalizing by the generic zero-frontier energy envelope at the later horizon `T=qX`, the optimized loss exponent is

\[
b_\Theta(\lambda)
=\frac{1-\Theta+(2\Theta-1)\lambda}{1+\lambda},
\qquad
b_\Theta'(\lambda)=\frac{3\Theta-2}{(1+\lambda)^2}.
\]

Hence `\Theta=2/3` is an invariant crossover for this entire direct-transfer family. If `\Theta>2/3`, moving away from the critical host only worsens the exponent and the optimum collapses back to the FD-061 boundary. If `1/2<\Theta<2/3`, pushing to the largest host allowed by the current short-interval theorem still loses to the all-horizon FD-049 exponent. At `\Theta=2/3`, every admissible `\lambda` gives the same `1/3` loss. **Polynomial packet multiplicity does not beat the existing two-thirds barrier because its gain is exactly offset by horizon cost.**

FD-064 also identifies a geometric phase boundary. The packet rows have

\[
r=T^{\lambda/(1+\lambda)+o(1)}.
\]

A direct all-short-interval theorem available only for interval exponents `\vartheta>1/2` keeps these rows strictly inside the cube-root Jordan core. Reaching `r\asymp T^{1/3}` is equivalent to the source transfer operating at the square-root interval scale. Thus square-root short-interval cancellation is the exact direct-transfer threshold for reaching the cube-root boundary where the earlier Jordan control changes regime.

The durable separation is now sharper. **Local packet capacity, host entropy, and normalized occupation are different currencies.** Direct endpoint transfer can create polynomially many source-bearing rows without changing the optimized global exponent. Improving packet size inside the same host/horizon budget is therefore not enough. Progress must alter a load-bearing ingredient: the same-horizon denominator, the source theorem/quantifier surface (especially toward or below square-root intervals), or a different arithmetic relation among rows that avoids the direct-transfer normalization ledger.

**Boundary.** FD-064 classifies the current direct all-short-interval transfer combined with the generic zero-frontier denominator envelope. It does not rule out source-coupled denominator estimates, almost-all/maximal interval theorems usable on the adaptive host corridor, cancellation below the square-root interval scale, or other row interactions. No new zero-free region or positive global occupation theorem follows.