# MI-073 — Effective translation geometry counts axes only after positive-closure costs are included

**Evidence level:** exact synthesis from MC-409--[MC-421](../../findings/MC-421-iterated-positive-differencing-creates-source-free-diagonal-faces.md), including the endpoint factorization of MC-414, the multivariable Fejer theorem MC-419 and support-lattice reduction MC-420. No new Möbius cancellation estimate is claimed.

MC-415--MC-418 identify the one-variable positive-kernel cost: after ordinary differencing the zero-shift diagonal re-squares the sieve, and finite-band stationary positivity pays at least the Fejer `1/H` floor even with operator-valued channels. MC-419 shows that genuinely independent translation variables can multiply bandwidth, while MC-420 makes independence algebraic: a symbol supported on an injected rank-`r` integer lattice factors through an `r`-torus. Ambient tensor coordinates and channel multiplicity therefore do not count as extra directions.

MC-421 adds a second audit that matters when new axes are manufactured by iterated positive differencing rather than present before closure. For the multiplicative cube derivative, every coordinate-zero face satisfies

`D_r(...,h_j=0,...)=|D_(r-1)|^2>=0`.

Under Fejer weighting that face has normalized coefficient mass `1/H_j`, not the product-scale mass of the all-zero corner. In the source frame `a_n=w(n)chi(n)`, absolute squaring removes the character phase on every such face. At depth two the whole face is the positive sliding-window energy

`sum_h W_H(h) Q_(h,0) = sum_t (sum_(j=0)^(H-1) |a_(t+j)|^2)^2`.

Thus a genuinely new shift variable can still fail to buy a tensorized diagonal saving if it is created by raising correlation order: the new cube comes with codimension-one, source-phase-free diagonal faces at reciprocal one-axis scale. Counting only integer support rank or the all-zero corner is then incomplete; the mechanism that creates the axes and the degeneracy geometry of the positive closure must also be priced.

Two escapes remain distinct. A genuinely rank-two quadratic arithmetic lift derived before squaring is still governed by MC-419--MC-420 and is not ruled out by MC-421. A higher-order/Gowers or dispersion argument may also survive if it controls the full cube collectively and proves structured off-face cancellation strong enough to pay the degenerate faces. What is closed is the shortcut of iterating generic positive differencing and crediting each new formal shift as an independent Fejer factor.

**Boundary.** MC-421 is not a lower bound for the complete higher-order energy; off-face terms can cancel inside the exact positive expression. The result concerns ordinary positive repeated-differencing closure, not signed/indefinite or nonstationary architectures, and it yields no RH-scale cancellation by itself.