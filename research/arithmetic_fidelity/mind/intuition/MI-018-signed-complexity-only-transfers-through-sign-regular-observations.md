# MI-018 — Finite sign complexity transfers only after the Euler tail loses to the sampling margin

**Evidence level:** supported by AF-217--AF-220 and sharpened quantitatively by [AF-337](../../findings/AF-337-deep-half-plane-harmonic-tail-restores-finite-euler-sign-regularity.md). The result is a fixed-finite-order theorem in the absolutely convergent half-plane; no uniform all-order total positivity, critical-line transport, or stable inverse bound is claimed.

The useful source currency is not positivity of every minor. It is a **finite sign-variation budget matched to a finite observation order**. AF-217 shows that the Euler-log family is not globally totally positive, while AF-218--AF-220 recover strict sign regularity at each fixed order when the sampling geometry has a quantitative separation/curvature modulus. This is enough to detect any nonzero coefficient vector with fewer sign changes than the observation order.

AF-337 makes that qualitative principle explicit for the full Euler logarithm rather than its first harmonic. For fixed order `r`, row spacing `h`, and distinct multiplicative sites `q_j in [P,AP]`, the sampling matrix

`E_(sigma+(i-1)h)(q_j) = -log(1-q_j^(-sigma-(i-1)h))`

is strictly sign-regular through order `r` for all sufficiently large `P` whenever

`sigma > Gamma_(r,h) := (h+1) binom(r,2)`.

The mechanism is an exact margin comparison. The first Euler harmonic has a Vandermonde-type minor with a polynomially small lower margin in `P`; the sum of all higher harmonics is `O(P^-sigma)`. Once the latter is smaller than the former, the checkerboard minor signs survive. Equivalently, the full nonlinear Euler logarithm inherits the finite-order variation-diminishing test because its harmonic tail is below the determinant margin actually consumed by that test.

This supplies a reusable transfer rule: **a source sign budget becomes observable only after the unresolved tail is quantitatively smaller than the finite-order sign-regularity margin.** Merely knowing that the leading kernel has the right sign pattern is not enough, and demanding all-order positivity is stronger than needed.

The remaining arithmetic problem is now sharper rather than solved. The sufficient depth `sigma>Gamma_(r,h)` grows quadratically with `r` and lies deep in `Re s>1`; it can destroy the zero-sensitive information that motivated the Euler representation. A useful bridge must therefore force a small enough source sign budget and transport that finite-order certificate toward the analytically relevant region without paying a depth cost that erases the destination signal. Exact sign detection is also weaker than a uniform inverse/conditioning theorem.

**Boundary.** AF-337 works for primes and composites alike, so the sign-regular observation geometry is not itself a prime-specific theorem. Its role is to state the quantitative interface that a prime-specific source restriction would have to exploit.