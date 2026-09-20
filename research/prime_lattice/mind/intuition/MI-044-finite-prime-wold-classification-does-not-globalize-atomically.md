# MI-044 — Zero-faithful analytic continuation can lie entirely in the kernel of the native almost-periodic quotient

**Evidence level:** exact/literature-aware synthesis from PL-379--[PL-392](../../findings/PL-392-euler-maclaurin-renormalization-besicovitch-null.md), including the finite Jessen-density audit of [PL-391](../../findings/PL-391-finite-jessen-half-line-density-is-not-rh.md). No RH conclusion is claimed.

Prime-lattice representations face two different losses. Keeping the numerical prime frequencies in a strong operator or energy category does not automatically provide analytic continuation, while weakening to vertical Besicovitch `B^2` can carry the Dirichlet series deeper into the strip but identifies functions that differ by height-decaying terms.

PL-391 shows why a half-line zero-density statement does not repair this by itself. The finite Dirichlet-polynomial Jessen mechanism selects `Re(s)=1/2` through an `L^2` coefficient-energy threshold, but the normalized density can ignore any fixed or zero-density family of off-line zeros. The order of limits does not turn it into the divisor of the analytically continued zeta function.

PL-392 gives an exact matched pair. Adding the Euler--Maclaurin tail `N^(1-s)/(s-1)` produces local-uniform convergence to zeta on `Re(s)>0` away from the pole and hence recovers fixed zeros by ordinary analytic continuation. Yet the same tail is Besicovitch-null on each fixed interior vertical line, so the corrected and uncorrected cutoffs are identical in the native `B^2` quotient. A representation can therefore carry the right mean-square source while erasing precisely the term that makes the finite approximants zero-faithful.

The durable requirement is to keep **numerical frequency data, a distinguished continuation representative and the target divisor** in one category. Mean-square equivalence is too coarse if the target is an isolated zero; local-uniform continuation alone is too weak if the arithmetic energy/index is lost. Any nonlinear or Fredholm repair must demonstrate both properties rather than infer one from the other.

**Boundary.** PL-391 does not say Jessen theory is irrelevant, and PL-392 does not rule out nonlinear functionals of the corrected representative. They show that normalized finite zero density and linear/quadratic `B^2` invariants do not by themselves transport the actual zeta divisor.
