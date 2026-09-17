# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-051-normalized-euler-band-access-costs-inverse-source-mass-in-scalar-translate-variation`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band.

NB-191 closes the simplest locality escape from that tariff. At every fixed `a` and fixed positive accuracy, the compactly truncated sharp synthesizers can be translated into every sufficiently high dyadic block `[T,2T]` with no extra asymptotic variation cost. Finite-frequency Bohr recurrence supplies a common near-return for the union of all `K` active band frequencies, so the high-block infimum remains `Theta(H_T)` once `T` exceeds the recurrence threshold. Merely forcing acquisition far from height zero therefore does not add a universal surcharge.

The live discriminator is the **coupled scaling** of source resolution and height. As `a=a_T->0`, the active prime-log frequency set grows and the common Bohr-recurrence inclusion length may grow much faster than the arithmetic height available. A genuine locality obstruction must quantify that competition, or derive another source-native bound on the scalar-mixing/operator budget. Fixed-`a` high-block locality by itself is now a closed negative route.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-191 are acquisition theorems in coefficient topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all `K` normalized bands. Conversely, the fact that unrestricted mixtures can synthesize the bands, and can transplant them to high blocks at fixed `a`, does not make their `Theta(K)`/`Theta(H_T)` variation cost irrelevant.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence length and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and then test that bound against a matched control on the realized approximation range.