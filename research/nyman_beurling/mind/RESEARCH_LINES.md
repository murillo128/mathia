# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-052-brun-titchmarsh-occupancy-pushes-positive-return-obstruction-to-the-mellin-endpoint`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band. NB-191 then shows that at fixed `a` and fixed positive accuracy, finite-frequency Bohr recurrence can transplant compact sharp synthesizers into arbitrarily high blocks without an extra asymptotic variation surcharge.

NB-192--NB-197 expose the coupled-limit nonuniformity. Prime-log phase dimension forces enormous recurrence scales; Vinogradov--Korobov, mean-square and short-interval source resolution give progressively stronger return-free corridors, but the intermediate exponents measure source-resolution technology rather than a natural endpoint constant.

NB-198 replaces cellwise source approximation by positive occupancy. A sufficiently accurate positive return forces most von-Mangoldt mass into favorable phase windows, and Brun--Titchmarsh bounds how much those windows can carry. NB-199 follows their width diagonally and proves a quantitative gap through the final logarithmic layer below `x_a/X_a`. NB-200--NB-201 then show that local density hands off to atomic carrying capacity at endpoint height and quantify the approach to the resulting one-sided capacity edge.

NB-202 makes the next transition from counting favorable phase cells to counting which cells actually meet the integer carrier. Erdős--Turán plus the second-derivative van der Corput test yields `A_a(t)>>1/X_a` through `|t|<<x_a^2/X_a^3`. NB-203 extends the same carrier argument with every fixed derivative order and thereby removes every fixed polynomial shell height. NB-204 uses a uniform all-orders derivative estimate with order growing with `a` to push the obstruction to quasi-polynomial height,

`log |t| >= (1/log 2-o(1)) X_a log X_a`

for any high-ordinate positive-return sequence with `X_a A_a(t)->0`.

NB-205 replaces the derivative hierarchy by Ford's Vinogradov--Korobov exponential-sum estimate for `sum n^(-it)`. Coupled to the same angular-resolution Erdős--Turán count and the Euler atom cap `w_(n,a)<<X_a/x_a`, it proves that for every fixed `kappa<1/sqrt(133.66)`,

`X_a^2 <= |t| <= exp(kappa X_a^(3/2)/sqrt(log X_a))`

implies `A_a(t)>>_kappa 1/X_a`. Hence an `o(1/X_a)` positive return must satisfy

`liminf log|t| sqrt(log X_a)/X_a^(3/2) >= 1/sqrt(133.66)`.

In a physical block `[T,2T]`, the resulting necessary positive-source acquisition width is

`a >= r_0 (3/(2*133.66)+o(1))^(1/3) / ((log T)^(2/3)(log log T)^(1/3))`.

This is a source-acquisition obstruction, not a Nyman distance theorem. The positive-source frontier is now to test whether stronger logarithmic exponential-sum bounds or genuinely von-Mangoldt-weighted carrier cancellation can improve Ford's all-integers law. A separate destination question remains load-bearing: prove that a Nyman approximant resolving the target must realize such an `o(a)` positive Euler-shell return, or identify the correct destination-coupled source condition if it does not.

A different continuation must leave positivity and control signed/complex synthesis, where occupancy, integer carrying capacity and positive chord mass cease to be monotone because cancellation can move between phase sectors.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-205 are acquisition theorems in coefficient/phase topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but the coupled source-height limit successively exposes target volume, dephasing, source resolution, occupancy, atomic capacity, endpoint stability, integer-carrier discrepancy, derivative-order uniformity and now **Vinogradov--Korobov logarithmic-sum cancellation**.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, long-time prevalence, first-hit/return-free scale, source-specific pointwise dephasing, uniform versus almost-all source resolution, interval occupancy, atomic cell capacity, integer-cell occupancy, endpoint deficit, requested return tolerance and destination conditioning are distinct currencies. A successful continuation must identify which are actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and test that bound against a matched control on the realized approximation range.