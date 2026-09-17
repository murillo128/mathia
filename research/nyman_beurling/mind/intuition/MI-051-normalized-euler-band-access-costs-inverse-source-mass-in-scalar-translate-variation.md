# MI-051 — Normalized Euler-band access costs inverse source mass, while positive recurrence pays effective dimension

**Evidence level:** exact/derived synthesis from [NB-189](../../findings/NB-189-positive-mass-euler-band-routing-saturates-source-fidelity-tariffs-on-poisson-packed-controls.md), [NB-190](../../findings/NB-190-normalized-euler-bands-have-a-sharp-inverse-source-mass-scalar-translate-synthesis-cost.md), [NB-191](../../findings/NB-191-bohr-recurrence-removes-a-universal-high-block-locality-surcharge.md), [NB-192](../../findings/NB-192-prime-log-entropy-forces-double-exponential-bohr-inclusion-length.md), and [NB-193](../../findings/NB-193-weighted-euler-band-recurrence-still-has-double-exponential-inclusion-length.md). Sharpness of the variation tariff is within the unrestricted Fourier--Stieltjes scalar-translate class at fixed positive accuracy; the recurrence results price specific syndetic transplant mechanisms rather than all possible high-block synthesis.

NB-189 shows that independently normalized true-amplitude Euler bands can pay the representation-level source-mass and fanout tariffs and still generate a full Fourier code on a Poisson-packed matched control. NB-190 prices the missing operation: obtaining those normalized bands from the genuine scalar Euler translate family.

If a target probe is concentrated on source mass `Theta`, every Fourier--Stieltjes mixture of scalar translates that approximates it with coefficient `ell^1` error at most `epsilon<1` must have total variation at least `(1-epsilon)/Theta`. For the balanced partition with `K asymp 1/a`, each band has `Theta asymp 1/K`, so each normalized coordinate costs `Theta(K)` variation. Smooth cutoffs attain the same order at fixed accuracy. Under source-safe high-ordinate normalization, the corresponding lower tariff is `Omega(H_T)` per normalized band.

NB-191 shows that **high-block support does not increase this order at fixed source width**. The sharp finite-height synthesizers can be compactly truncated and translated into every sufficiently high dyadic block `[T,2T]`; finite-frequency Bohr recurrence supplies a single common shift whose active phases are simultaneously close to one. At fixed `a`, the localized upper bound therefore stays `O(H_T)`.

The coupled limit is different. NB-192 shows that one fixed log-width Euler band already contains

`m_a asymp a exp(r_0/a)`

rationally independent prime-log phases, so coordinatewise syndetic recurrence has inclusion length satisfying

`log L_a >> a exp(r_0/a)`.

NB-193 proves that the same scale is not an artifact of requiring every phase separately. For positive weights `w_j`, a weighted chord-return set below the Haar mean has measure exponentially small in the effective dimension

`D_eff(w)=1/sum_j w_j^2`.

The normalized true prime weights in the first Euler band have `D_eff asymp m_a`, and higher prime powers carry vanishing relative mass. Consequently the natural true-source-weighted coefficient defect

`A_a(t)=theta_(0,a)^(-1) sum alpha_(n,a)|e^(-it log n)-1|`

still has any fixed-accuracy **syndetic** inclusion length obeying

`log L_a^avg(eta) >> a exp(r_0/a)`.

Both recurrence mechanisms therefore impose the same guaranteed-block log-log floor

`a >= r_0/(log log T + log log log T + O(1))`

when their return must occur inside an available block of length `T`.

The reusable lesson is that **representation complexity, acquisition variation and recurrence entropy are separate currencies**. Inverse source mass is the sharp scalar-mixture tariff. Fixed-height locality is free by almost periodicity, but in the shrinking-width limit the positive recurrence target itself occupies exponentially small phase volume because the true source has exponentially large effective dimension. Replacing a max-phase requirement by its most natural positive weighted `ell^1` relaxation does not remove that cost.

**Boundary.** NB-192--NB-193 do not prove that every high-block Fourier--Stieltjes synthesis must pay the double-exponential scale. They price worst-gap/syndetic recurrence of positive phase mismatch. A specific block may contain an unusually early return; signed coefficient cancellation, a different response topology, or a non-recurrence synthesis may evade the bound. NB-190--NB-193 also do not identify the actual variation/operator budget of the Nyman approximation class or prove that the realized range requires independent recovery of all normalized bands. The live question is now whether one of the surviving non-positive/non-syndetic mechanisms exists in the physical `a_T`--`T` regime and remains compatible with the destination conditioning.