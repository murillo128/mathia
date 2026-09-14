# MI-018 — Finite sign complexity transfers once harmonic tail cost beats collision loss

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), which improves the sufficient depth in AF-337. The result is a fixed-finite-order theorem in the absolutely convergent half-plane; no uniform all-order total positivity, critical-line transport or stable inverse bound is claimed.

The useful source currency is not positivity of every minor. It is a **finite sign-variation budget matched to a finite observation order**. AF-217 shows that the Euler-log family is not globally totally positive, while AF-218--AF-220 recover strict sign regularity at fixed order under quantitative sampling geometry.

AF-337 made the full-Euler tail comparison explicit but paid a quadratic sufficient depth by comparing higher harmonics to the first-harmonic determinant after discarding their inherited source collisions. AF-338 keeps those collisions. For a `k x k` minor, let `m_j` be the column harmonic labels, `S(m)=sum_j(m_j-1)` their total excess order, and `X(m)` the number of column pairs carrying unequal labels. Then exactly at the exponent-budget level

`X(m) <= (k-1) S(m)`.

Equal harmonic labels preserve the first-harmonic Vandermonde zero; only unequal labels can spend an inverse source-gap factor. The generalized Schur row-shape factor creates no positive power of the source scale. Consequently, for fixed order `r`, row spacing `h`, and `q_j in [P,AP]`, the full Euler-log sampling matrix is eventually strictly sign-regular through order `r` whenever

`sigma > r-1`,

with every full-Euler minor differing relatively from its first-harmonic minor by `O(P^-(sigma-(r-1)))`.

The reusable principle is more precise than “tail below margin”: **price how much of the leading determinant's collision geometry each tail component actually destroys.** Treating every tail determinant independently can invent a much larger transport cost than the nonlinear expansion really pays.

The remaining arithmetic problem is still a destination problem. The depth budget is now linear rather than quadratic, but it grows with the desired sign order and remains in `Re s>1`; moreover the theorem is equally valid for primes, composites and mixed integer controls. A useful RH-facing bridge must force a small source sign budget and transport or consume the resulting finite-order certificate before the required half-plane depth erases the zero-sensitive signal.

**Boundary.** AF-338 is an exact finite-order sign theorem, not a prime discriminator or uniform inverse theorem. The exponent threshold is independent of `h`, but constants and the onset scale still depend on `r,h,A,sigma`.
