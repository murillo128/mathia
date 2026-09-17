# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-051-normalized-euler-band-access-costs-inverse-source-mass-in-scalar-translate-variation`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band.

NB-191 closes the simplest fixed-resolution locality escape. At every fixed `a` and fixed positive accuracy, compactly truncated sharp synthesizers can be translated into every sufficiently high dyadic block `[T,2T]` with no extra asymptotic variation cost. Finite-frequency Bohr recurrence supplies a common near-return for the active frequencies, so high height alone does not add a universal surcharge.

NB-192 quantifies the hidden nonuniformity. A single fixed log-width Euler band contains `m_a~a exp(r_0/a)` rationally independent prime-log phases. Coordinatewise common recurrence at fixed accuracy therefore has worst-gap inclusion length with `log L_a >> a exp(r_0/a)`, giving a log-log lower floor on `a` if the return must be guaranteed inside a block of length `T`.

NB-193 now closes the most direct aggregate-weighted escape from that entropy barrier. Replace coordinatewise phase recurrence by the true-source-weighted coefficient mismatch

`A_a(t) = theta_(0,a)^(-1) sum_(n in S_(0,a)) alpha_(n,a) |e^(-it log n)-1|`.

For a rationally independent positive phase family, the Haar volume of the weighted target is exponentially small in the effective dimension `D_eff=1/sum_j w_j^2`. The true prime weights in one fixed log-width Euler band remain diffuse enough that `D_eff asymp m_a`, while higher prime powers carry vanishing relative mass. Hence for every fixed `0<eta<1`, any **syndetic** inclusion length for `{t:A_a(t)<=eta}` still satisfies

`log L_a^avg(eta) >> a exp(r_0/a)`.

The same log-log block-width floor survives. Thus replacing max-phase recurrence by the natural positive `ell^1` aggregate used by the NB-190 coefficient topology does not make the NB-191 transplant uniformly cheap in the coupled limit.

The live discriminator is now narrower. A successful high-block synthesis below that floor must exploit something not captured by positive syndetic recurrence of the target coefficient mask: an exceptionally early return in the specific block `[T,2T]`, signed cancellation after aggregation, a different response topology, or a genuinely different source-native synthesis architecture. The next theorem should price one of those mechanisms directly rather than weakening the recurrence target while retaining the same worst-gap paradigm.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-193 are acquisition theorems in coefficient topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all `K` normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but NB-192--NB-193 show that both coordinatewise and natural positive weighted recurrence become double-exponentially nonuniform as `a->0`.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, filling time and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and then test that bound against a matched control on the realized approximation range.