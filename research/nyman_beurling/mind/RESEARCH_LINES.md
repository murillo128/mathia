# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-052-brun-titchmarsh-occupancy-pushes-positive-return-obstruction-to-the-mellin-endpoint`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band. NB-191 then shows that at fixed `a` and fixed positive accuracy, finite-frequency Bohr recurrence can transplant compact sharp synthesizers into arbitrarily high blocks without an extra asymptotic variation surcharge.

NB-192--NB-197 expose the coupled-limit nonuniformity. Prime-log phase dimension forces enormous recurrence scales; Vinogradov--Korobov, mean-square and short-interval source resolution give progressively stronger return-free corridors, but the intermediate exponents measure source-resolution technology rather than a natural endpoint constant.

NB-198 replaces cellwise source approximation by positive occupancy. A sufficiently accurate positive return forces most von-Mangoldt mass into favorable phase windows, and Brun--Titchmarsh bounds how much those windows can carry. NB-199 follows their width diagonally and shows that throughout

`X_a^2 <= |t| <= x_a/(U_0 X_a)`

one has

`A_a(t) >= c log(x_a/(|t|X_a))/X_a`.

Thus `o(1/X_a)` positive returns cannot remain below the final logarithmic layer `x_a/X_a`.

NB-200 shows that the disappearance of the interval-density reserve is not the end of coercivity. At endpoint height each favorable phase cell becomes shorter than one integer, so local density hands off to atomic carrying capacity. The one-sided theorem implies that any sequence with `X_a A_a(t)->0` and bounded endpoint ratio must satisfy

`liminf |t|X_a/x_a >= 2 pi e^Delta`.

The constant is a certified capacity edge, not an existence theorem.

NB-201 now diagonalizes that atomic argument. Define

`kappa_a^cap = 2 pi e^Delta X_a/(X_a+Delta)`, `kappa_a(t)=|t|X_a/x_a`, and `d_a(t)=1-kappa_a(t)/kappa_a^cap`.

In the one-sided endpoint regime,

`A_a(t) >= (c/X_a)(d_a(t)^2-C E_a)_+`,

hence

`d_a(t) <= C(sqrt(X_a A_a(t))+sqrt(E_a))`,

where `E_a` is the inherited Vinogradov--Korobov PNT remainder. The quadratic modulus is structural: a relative capacity deficit `d` is tested on a top slab containing `Theta(d)` source mass, and the unfillable fraction contributes another factor `Theta(d)`.

NB-202 shows that the certified atomic edge is not the end of deterministic positive-source coercivity. Counting favorable phase cells ignores whether those cells actually meet the integer carrier. Erdős--Turán discrepancy plus the van der Corput second-derivative estimate gives, for a fixed angular tolerance `q/X_a`,

`#{n in [x_a,e^Delta x_a): dist(t log n,2 pi Z)<=q/X_a} << q x_a/X_a + sqrt(|t|X_a/q) + x_a/sqrt(|t|)`.

Together with the pointwise Euler atom cap `w_(n,a)<<X_a/x_a`, this forces

`A_a(t) >> 1/X_a`

uniformly for

`C X_a^2 <= |t| <= c x_a^2/X_a^3`.

Combined with NB-199, an `o(1/X_a)` positive return in the high-ordinate regime cannot occur before the quadratic carrier scale `x_a^2/X_a^3`. In a block `[T,2T]`, this gives the necessary acquisition width

`a >= 2 r_0/(log T + 3 log log T + O(1))`.

The upper scale `x_a^2/X_a^3` is a discrepancy-method boundary, not a certified first-return threshold. The positive-source frontier is therefore to extend carrier discrepancy beyond the second-derivative window or to use genuinely von-Mangoldt occupancy rather than the all-integers carrier bound, while keeping clear which gain is generic harmonic analysis and which is source-specific arithmetic. A separate destination question remains load-bearing: prove that a Nyman approximant resolving the target must realize such an `o(a)` positive Euler-shell return, or identify the correct destination-coupled source condition if it does not.

A different continuation must leave positivity and control signed/complex synthesis, where occupancy, integer carrying capacity and positive chord mass cease to be monotone because cancellation can move between phase sectors.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-202 are acquisition theorems in coefficient/phase topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but the coupled source-height limit successively exposes target volume, dephasing, source resolution, occupancy, atomic capacity, endpoint stability and now **integer-carrier discrepancy**.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, long-time prevalence, first-hit/return-free scale, source-specific pointwise dephasing, uniform versus almost-all source resolution, interval occupancy, atomic cell capacity, integer-cell occupancy, endpoint deficit, requested return tolerance and destination conditioning are distinct currencies. A successful continuation must identify which are actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and test that bound against a matched control on the realized approximation range.