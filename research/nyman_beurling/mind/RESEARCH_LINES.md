# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-051-normalized-euler-band-access-costs-inverse-source-mass-in-scalar-translate-variation`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band.

NB-191 closes the simplest fixed-resolution locality escape. At every fixed `a` and fixed positive accuracy, compactly truncated sharp synthesizers can be translated into every sufficiently high dyadic block `[T,2T]` with no extra asymptotic variation cost. Finite-frequency Bohr recurrence supplies a common near-return for the active frequencies, so high height alone does not add a universal surcharge.

NB-192 quantifies the hidden nonuniformity. A single fixed log-width Euler band contains `m_a~a exp(r_0/a)` rationally independent prime-log phases. Coordinatewise common recurrence at fixed accuracy therefore has worst-gap inclusion length with `log L_a >> a exp(r_0/a)`, giving a log-log lower floor on `a` if the return must be guaranteed inside a block of length `T`.

NB-193 closes the most direct aggregate-weighted escape from that entropy barrier. Replace coordinatewise phase recurrence by the true-source-weighted coefficient mismatch

`A_a(t) = theta_(0,a)^(-1) sum_(n in S_(0,a)) alpha_(n,a) |e^(-it log n)-1|`.

For a rationally independent positive phase family, the Haar volume of the weighted target is exponentially small in the effective dimension `D_eff=1/sum_j w_j^2`. The true prime weights in one fixed log-width Euler band remain diffuse enough that `D_eff asymp m_a`, while higher prime powers carry vanishing relative mass. Hence for every fixed `0<eta<1`, any **syndetic** inclusion length for `{t:A_a(t)<=eta}` still satisfies

`log L_a^avg(eta) >> a exp(r_0/a)`.

NB-194 now closes a genuine part of the specific-block loophole left by those worst-gap theorems. For the actual normalized full von-Mangoldt shell, a positive chord return forces a large complex barycenter, while Vinogradov--Korobov PNT dephasing gives

`|C_a(t)| << (1+|t|)^(-1) + (1+|t|) exp(-c V(e^(r_0/a)))`.

Therefore for every fixed positive accuracy there is a deterministic return-free corridor from a fixed height up to `exp(c_eta V(e^(r_0/a)))`. In particular the physical block `[T,2T]` cannot contain an exceptionally early positive return when

`log T=o(V(e^(r_0/a_T)))`,

with inversion scale roughly `a_T~(log T)^(-5/3)(loglog T)^(-1/3)` up to constants. This is a source-dephasing theorem for the particular block, not another syndetic entropy estimate.

The ranges still leave a substantial intermediate regime. The NB-193 guaranteed-block obstruction becomes relevant near the much larger log-log source-width scale, while NB-194 excludes actual positive returns only in the narrower Vinogradov--Korobov corridor. The next theorem should attack this gap directly: strengthen blockwise cancellation for the oscillatory von-Mangoldt shell, price signed/complex aggregate synthesis in a source-safe response norm, or identify a genuinely different high-block construction not obtained by positive recurrence. Weakening the positive recurrence target again is no longer enough.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-194 are acquisition theorems in coefficient/phase topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all `K` normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but NB-192--NB-193 show that positive recurrence becomes double-exponentially nonuniform as `a->0`, while NB-194 shows that the actual rational-prime shell is uniformly dephased on a narrower high-block corridor.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, filling time, source-specific dephasing and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and then test that bound against a matched control on the realized approximation range.
