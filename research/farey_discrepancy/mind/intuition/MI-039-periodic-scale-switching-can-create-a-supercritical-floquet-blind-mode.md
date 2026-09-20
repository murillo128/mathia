# MI-039 — Switched-block blindness survives exact full-divisor repair, but smooth capacity growth is visible

**Evidence level:** exact/literature-backed synthesis from FD-212--[FD-227](../../findings/FD-227-power-law-divisor-cushions-are-asymptotically-visible-to-switched-root-rows.md), interpreted against the fixed-family source-identification dichotomy of FD-210--FD-224.

The periodic schedule `q_j=(0,3,3)` has a physical super-square-root Floquet blind mode even though each instantaneous annihilator has only the harmless root `1`. FD-212--FD-223 show that exact Möbius Euler laws, bounded scheduled observations and a macroscopic earlier-prefix defect can coexist across long fixed blocks when the source law is anchored to one absolute cutoff below the original horizon. FD-224 fixes the quantifier boundary: horizon-relative exact Euler windows eventually cover the original prefix, and exhaustive cofinal exact compatibility identifies the permanent source as `mu`.

FD-225 removes switched-matrix conditioning from the non-exhaustive construction. The complete divisor-reservoir response

`(A c)(m)=sum_(d<=m) c_d M(floor(m/d))`

has the exact integer inverse `c(n)=sum_(d|n)(y(d)-y(d-1))`. Using all divisor reservoirs, every sampled prefix through depth `D` can be flattened to one common value up to unit rounding error while retaining an `N^(1-o(1))` defect at the original horizon. The earlier exponential triangular-conditioning factor was therefore a repair artifact.

FD-226 then separates prime-resolution geometry from physical positive capacity. Exact floor cells with width proportional to the divisor remove one power of `D` from the prime-resolution error, but a common positive cushion still has to absorb the physical Mertens correction. The smallest reservoir fixes that common level, so the overall certified depth retains the quadratic capacity pressure even after inversion and prime-resolution artifacts are cleaned up.

FD-227 shows that the obvious attempt to use the larger cells more aggressively is not switched-null. If `b_d=c d^sigma+o(d^sigma)` with `sigma>0`, then

`(A b)(m)=c m^(sigma+1)/((sigma+1) zeta(sigma+1))+o(m^(sigma+1))`.

Every fixed root row `(T-I)^r` multiplies the leading term by the nonzero factor `(2^(sigma+1)-1)^r`. At the natural cell-capacity exponent `sigma=1`, a fixed positive fraction of every reservoir therefore creates a quadratic switched signal. By contrast the constant profile is exactly exceptional: `A 1=1`, so every positive-order root difference annihilates it.

The reusable distinction is now between **source coverage**, **algebraic repair**, **prime resolution**, and **nullspace-compatible positive capacity**. Exact inversion can make the observation equations easy while positivity makes their physical realization hard. More importantly, extra reservoir capacity is useful only if its occupancy profile lies near the switched nullspace: smooth scale growth is converted by the Möbius divisor response into a Jordan-totient main mode that every fixed root row sees.

The remaining blind-route question is therefore sharply oscillatory. A successful nonconstant target must redistribute occupancy by order one across divisor scales while staying nonnegative, within each local prime capacity, and with enough lower slack to absorb the Mertens correction. If every such switched-null profile repeatedly depletes the small-capacity scales, the remaining capacity loss is structural; if one admits proportional positive slack across the full relevant range, the current depth barrier is still a construction artifact.

**Boundary.** FD-227 does not prove that the smallest-cell cushion is intrinsic and does not rule out oscillatory Floquet/divisor-scale null profiles. FD-224 uses exact global prime relations; averaged, local-in-`n`, probabilistic or approximate source fidelity can have different identification behavior. None of these findings gives a counterexample to Möbius cancellation or RH.