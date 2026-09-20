# MI-073 — The translated character survives as thin endpoint geometry, while positive differencing re-squares the sieve on the diagonal

**Evidence level:** exact synthesis from MC-409--[MC-415](../../findings/MC-415-vdc-diagonal-resquares-linear-sieve.md), with the endpoint factorization of [MC-414](../../findings/MC-414-shift-position-kernel-is-endpoint-separable.md). No Möbius cancellation beyond the cited estimates is claimed.

The well-factorable frame creates a real translated character before completion. MC-414 shows, however, that the joint shift-position phase is not a new irreducible character object: after passing to endpoints `x=m+j`, `y=m`, it factorizes as `chi(x) conjugate(chi(y))`. What remains arithmetic is the thin divisor-dependent domain on which the two endpoints are allowed to range. Full conductor completion still destroys that geometry and returns standard scalar character information.

This representation change clarifies where a gain could live. It must be a bilinear or incomplete character estimate that uses the endpoint domain before the domain is filled out. The generic two-dimensional Fourier transform of the phase is already controlled by Gauss-sum geometry; simply exposing two variables does not supply cancellation. Any stronger result has to exploit the arithmetic weights or the particular thin/convex support.

MC-415 adds a load-bearing cost that appears even earlier. Standard positive van der Corput/Cauchy differencing necessarily carries a zero-shift energy. For the linear-sieve weights that energy is quadratic in the weights and therefore recreates the lcm/squared-sieve structure the frame was designed to postpone. Off-diagonal character cancellation is useful only if it beats this diagonal cost before another positivity step erases the advantage.

The reusable audit is consequently **thin-domain off-diagonal gain versus re-quadratized diagonal cost**. Completion, Cauchy and absolute values are not neutral bookkeeping operations here: each can remove the source coupling one hoped to exploit.

**Boundary.** MC-414--MC-415 do not prove that no useful bilinear estimate exists, nor that a signed or modulus-factorized differencing scheme cannot alter the balance. They show only that ordinary phase counting and a first-moment sieve estimate do not cross the present gate.
