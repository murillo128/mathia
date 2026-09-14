# MI-017 — Finite source-native pole cancellation is RH-complete and irreducibly signed at every order

**Evidence level:** supported by [WP-290](../../findings/WP-290-critical-mangoldt-dilation-coboundary-is-rh-equivalent-and-jordan-parts-remain-nontempered.md)--[WP-291](../../findings/WP-291-finite-dilation-coboundary-products-remain-rh-equivalent-and-sign-indivisible.md), together with the positive-completion obstructions of WP-288--WP-289. No Weil-positivity proof is claimed.

For the critical Mangoldt half-density

`mu=sum_(n>=2) Lambda(n)/sqrt(n) delta_(log n)`,

WP-290 introduces the intrinsic dilation coboundary `Delta_q=I-sqrt(q)S_(log q)`. Its transform multiplier `1-q^(1/2-s)` cancels the zeta-pole tangent exactly, and `Delta_q mu` is tempered if and only if RH. Both Jordan parts remain individually non-tempered, so the category descent exists only through signed cancellation.

WP-291 closes the obvious finite-order escape. For any finite nonempty list `q_1,...,q_r`, the product

`D_q=Delta_(q_1)...Delta_(q_r)`

remains tempered exactly under RH. Every factor vanishes at the pole location, so repeated differencing can annihilate the pole tangent to arbitrarily high finite order. But no factor vanishes at a nontrivial zeta-zero pole because `q^(1-rho)=1` would force `Re rho=1`. Hence the complete nontrivial zero divisor survives every finite product.

The sign obstruction is equally rigid. The positive Jordan channel retains the original coefficient `log p/sqrt(p)` on every prime, while a universal negative prime ray survives at `d p`, where `d=min q_j`. Both Jordan parts therefore have `e^(x/2)` mass growth and are non-tempered for every finite hierarchy, unconditionally.

The matched counting half-density becomes tempered after the same finite coboundary hierarchy. Finite dilation differencing is therefore generic homogeneous pole removal; the RH-sensitive content is precisely the residual Mangoldt zero structure.

The reusable conclusion is stronger than “one pole-killing difference is insufficient.” **No finite iteration of the canonical source-native dilation ideal changes the admissibility gate or separates the signed cancellation into positive channels.** More finite pole annihilation is mathematically irrelevant to the remaining obstruction.

The live Weil problem must therefore leave this finite hierarchy in a substantive way: prove unconditional admissibility through a different signed/global coupling, or use the hierarchy only diagnostically while constructing an exact Weil quadratic object by another mechanism. Treating any `D_q mu` as already admissible is circular because that admissibility is RH-equivalent.

**Boundary.** WP-291 closes products of the canonical elementary dilation coboundaries, not every finite signed translation filter. Zero-selected filters are outside the mandate, and an arbitrary source-native filter with genuinely different structure would require its own analysis.