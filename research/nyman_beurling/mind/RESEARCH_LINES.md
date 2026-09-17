# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-051-normalized-euler-band-access-costs-inverse-source-mass-in-scalar-translate-variation`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 now prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. The independent band oracle therefore hides a linear acquisition tariff beyond the square-root representation tariff.

This resolves the former binary question “can scalar translates synthesize the bands?” in a more useful way: **yes, in the unrestricted Fourier--Stieltjes class, but only by paying inverse source mass**. At high ordinate, the source-safe normalization strengthens the tariff to `Omega(H_T)` per band, so bounded-variation mixing cannot provide even one normalized coordinate when `H_T` grows.

The live discriminator is now the admissible acquisition budget of the actual Nyman architecture. A positive route should derive a source-native bound on scalar-mixing variation or another operator constraint that the matched-control Fourier code violates. A negative route could show that the realized Nyman range or its allowed scalar acquisition already supplies the required growing variation, in which case the tariff is only bookkeeping and a different selector is needed.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190 is an acquisition theorem in coefficient topology. It does not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all `K` normalized bands. Conversely, the fact that unrestricted mixtures can synthesize the bands does not make their `Theta(K)` variation cost irrelevant.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction and then test that bound against a matched control on the realized approximation range, not merely against an abstract coefficient code.