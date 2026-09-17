# MI-051 — Normalized Euler-band access costs inverse source mass, while positive recurrence pays effective dimension and source dephasing

**Evidence level:** exact/derived synthesis from [NB-189](../../findings/NB-189-positive-mass-euler-band-routing-saturates-source-fidelity-tariffs-on-poisson-packed-controls.md), [NB-190](../../findings/NB-190-normalized-euler-bands-have-a-sharp-inverse-source-mass-scalar-translate-synthesis-cost.md), [NB-191](../../findings/NB-191-bohr-recurrence-removes-a-universal-high-block-locality-surcharge.md), [NB-192](../../findings/NB-192-prime-log-entropy-forces-double-exponential-bohr-inclusion-length.md), [NB-193](../../findings/NB-193-weighted-euler-band-recurrence-still-has-double-exponential-inclusion-length.md), and [NB-194](../../findings/NB-194-vinogradov-korobov-dephasing-excludes-positive-euler-band-returns-on-specific-high-blocks.md). Sharpness of the variation tariff is within the unrestricted Fourier--Stieltjes scalar-translate class at fixed positive accuracy; the recurrence and dephasing results price specific positive transplant mechanisms rather than all possible high-block synthesis.

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

Both recurrence mechanisms therefore impose the same guaranteed-block log-log floor when their return must occur inside every available block of length `T`.

NB-194 closes part of the remaining “lucky specific block” escape by using the actual von-Mangoldt source rather than phase-volume entropy. For the normalized full prime-power barycenter

`C_a(t)=sum_n w_(n,a)e^(-it log n)`

on a fixed logarithmic Euler shell, Vinogradov--Korobov PNT remainder plus Stieltjes partial summation gives

`|C_a(t)| << (1+|t|)^(-1) + (1+|t|) exp(-c V(e^(r_0/a)))`,

where `V(x)=(log x)^(3/5)/(loglog x)^(1/5)`. A positive weighted chord return `A_a(t)<=eta<1` would force `|C_a(t)|>=1-eta`, so such a return is impossible throughout a deterministic high-frequency corridor extending to `exp(c_eta V(e^(r_0/a)))`. In particular a physical block `[T,2T]` is return-free whenever `log T=o(V(e^(r_0/a_T)))`, whose inversion scale is roughly

`a_T asymp (log T)^(-5/3)(loglog T)^(-1/3)`

up to constants.

This separates two different locality prices. NB-192--NB-193 say positive recurrence cannot be guaranteed cheaply in **every** block once the source width shrinks. NB-194 says that, in a narrower unconditional coupled regime, the actual block cannot be exceptionally lucky either: rational-prime dephasing rules out the positive return pointwise throughout the whole corridor. The large intermediate regime between this Vinogradov--Korobov scale and the syndetic log-log frontier remains open.

The reusable lesson is that **representation complexity, acquisition variation, recurrence entropy and source dephasing are separate currencies**. Inverse source mass is the sharp scalar-mixture tariff. Fixed-height locality is free by almost periodicity. In the shrinking-width limit, positive recurrence is first made nonuniform by effective dimension and then, on a narrower actual-source corridor, excluded outright by the PNT cancellation of the von-Mangoldt shell.

**Boundary.** NB-194 excludes only positive `ell^1` recurrence of the normalized Euler coefficient mask in its explicit corridor. It does not lower-bound every scalar acquisition mechanism. Signed or complex aggregation, a different response topology, a direct high-block Fourier--Stieltjes construction not obtained by recurrence, or stronger cancellation for the oscillatory von-Mangoldt shell may behave differently. NB-190--NB-194 also do not identify the actual variation/operator budget of the Nyman approximation class or prove that the realized range requires independent recovery of all normalized bands. The live question is now the intermediate coupled regime and any genuinely non-positive/non-recurrence acquisition mechanism that survives destination conditioning.
