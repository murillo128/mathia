# MI-051 — Normalized Euler-band access costs inverse source mass in scalar-translate variation

**Evidence level:** exact/derived synthesis from [NB-189](../../findings/NB-189-positive-mass-euler-band-routing-saturates-source-fidelity-tariffs-on-poisson-packed-controls.md) and [NB-190](../../findings/NB-190-normalized-euler-bands-have-a-sharp-inverse-source-mass-scalar-translate-synthesis-cost.md). Sharpness is within the unrestricted Fourier--Stieltjes scalar-translate class at fixed positive accuracy; this is not yet a theorem about the realized Nyman approximation range.

NB-189 shows that independently normalized true-amplitude Euler bands can pay the representation-level source-mass and fanout tariffs and still generate a full Fourier code on a Poisson-packed matched control. NB-190 prices the missing operation: obtaining those normalized bands from the genuine scalar Euler translate family.

If a target probe is concentrated on source mass `Theta`, every Fourier--Stieltjes mixture of scalar translates that approximates it with coefficient `ell^1` error at most `epsilon<1` must have total variation at least

`(1-epsilon)/Theta`.

This follows directly from the uniform Fourier--Stieltjes amplitude bound. Renormalizing a source subset of mass `Theta` to unit coefficient mass requires multiplier amplitude of order `1/Theta`; scalar vertical mixing cannot create that normalization for free.

For the balanced NB-189 partition, each of the `K asymp 1/a` bands has `Theta asymp 1/K`. **Each normalized band therefore costs `Theta(K)` scalar-translate total variation.** A smooth Fourier cutoff attains the same order at every fixed positive accuracy, so the tariff is sharp in the unrestricted mixing class. The independent band oracle hides an additional acquisition cost: the representation theorem charges only `sqrt(K)` RMS source-density gain, while scalar synthesis charges linear `K` variation per normalized coordinate.

The high-ordinate normalization makes the same distinction sharper. When one source-safe scalar sample has gain `~1/(a H_T)`, approximating one normalized `Theta(a)` band requires mixture variation `Omega(H_T)`. Bounded-variation high-ordinate mixing cannot supply even one such coordinate when `H_T` diverges.

The reusable lesson is that **representation complexity and acquisition complexity are different currencies**. A coefficient decomposition may satisfy true amplitudes, positive mass and bounded fanout and still presuppose an expensive normalization operation that the physical scalar source exposes only through large variation. Conversely, large variation is a cost, not an impossibility: unrestricted scalar mixtures can still synthesize the matched-control band code if that cost is allowed.

**Boundary.** NB-190 does not identify the physically admissible total-variation budget of the Nyman architecture, prove that the realized Nyman range needs the full band code, or make a large scalar mixture arithmetic. The live discriminator is whether the actual acquisition mechanism supplies or forbids the required inverse-mass variation at the same destination scale.