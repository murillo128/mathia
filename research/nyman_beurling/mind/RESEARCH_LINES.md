# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-052-brun-titchmarsh-occupancy-pushes-positive-return-obstruction-to-the-mellin-endpoint`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band.

NB-191 closes the simplest fixed-resolution locality escape. At every fixed `a` and fixed positive accuracy, compactly truncated sharp synthesizers can be translated into every sufficiently high dyadic block `[T,2T]` with no extra asymptotic variation cost. Finite-frequency Bohr recurrence supplies a common near-return for the active frequencies, so high height alone does not add a universal surcharge.

NB-192 quantifies the hidden nonuniformity. A single fixed log-width Euler band contains `m_a~a exp(r_0/a)` rationally independent prime-log phases. Coordinatewise common recurrence at fixed accuracy therefore has worst-gap inclusion length with `log L_a >> a exp(r_0/a)`, giving a log-log lower floor on `a` if the return must be guaranteed inside a block of length `T`.

NB-193 closes the most direct aggregate-weighted escape from that entropy barrier. Replace coordinatewise phase recurrence by the true-source-weighted coefficient mismatch

`A_a(t) = theta_(0,a)^(-1) sum_(n in S_(0,a)) alpha_(n,a) |e^(-it log n)-1|`.

For a rationally independent positive phase family, the Haar volume of the weighted target is exponentially small in the effective dimension `D_eff=1/sum_j w_j^2`. The true prime weights in one fixed log-width Euler band remain diffuse enough that `D_eff asymp m_a`, while higher prime powers carry vanishing relative mass. Hence for every fixed `0<eta<1`, any **syndetic** inclusion length for `{t:A_a(t)<=eta}` still satisfies

`log L_a^avg(eta) >> a exp(r_0/a)`.

NB-194 closes a genuine part of the specific-block loophole left by those worst-gap theorems. For the actual normalized full von-Mangoldt shell, a positive chord return forces a large complex barycenter, while Vinogradov--Korobov PNT dephasing gives

`|C_a(t)| << (1+|t|)^(-1) + (1+|t|) exp(-c V(e^(r_0/a)))`.

Therefore for every fixed positive accuracy there is a deterministic return-free corridor from a fixed height up to `exp(c_eta V(e^(r_0/a)))`. In particular the physical block `[T,2T]` cannot contain an exceptionally early positive return when `log T=o(V(e^(r_0/a_T)))`.

NB-195 extends the specific-block information far beyond that pointwise corridor by giving up emptiness and asking how much of the block can recur. The true normalized Euler shell has squared coefficient mass `sum_n w_(n,a)^2 << 1/(a exp(r_0/a))`. Montgomery--Vaughan mean-square dephasing therefore gives, for every fixed `0<eta<1`,

`|{t in [T,2T]: A_a(t)<=eta}|/T <<_(eta,r_0,Delta) exp(-r_0/a)/a + 1/(aT)`.

Hence whenever `a_T T->infinity`, positive true-source returns have vanishing relative measure on the actual block. This does not rule out a single exceptional return; it changes the surviving positive-recurrence problem into one about isolated near-maximal values of the actual Euler Dirichlet polynomial.

NB-196 first closes that isolated-return loophole pointwise through the corridor allowed by a **uniform** short-interval prime theorem. Resolving every spatial cell at length `x_a^(17/30+epsilon)` gives continuum Mellin control for `|t|<=x_a^(13/30-epsilon)` and eventual return-freeness of `[T,2T]` when `a_T log(2T)/r_0<13/30` by a fixed margin.

NB-197 shows that uniform control of every cell is stronger than positivity requires. Guth--Maynard's almost-all short-interval theorem reaches length `x^(2/15+epsilon)` outside an exponentially sparse set of starts. By averaging over shifted grids, one can choose a partition whose bad cells have exponentially small total length; positivity lets their complete von-Mangoldt mass be discarded at `o(1)` cost, while the chosen partition is independent of `t`. The same continuum shell response then holds uniformly through

`1<=|t|<=x_a^(13/15-epsilon)`.

Consequently every fixed positive-return tolerance is excluded pointwise in that enlarged corridor, and the physical block `[T,2T]` is eventually return-free whenever

`limsup_(T->infinity) a_T log(2T)/r_0 < 13/15`.

NB-198 replaces lower-and-upper source approximation by a weaker but much longer-range **occupancy** argument. If a positive return is sufficiently accurate, most von-Mangoldt source mass must lie in the short multiplicative phase windows where `t log n` is near `2 pi Z`. Brun--Titchmarsh upper bounds the mass those favorable windows can carry. For every fixed exponent margin `0<beta<1`, this excludes some fixed positive accuracy uniformly up to `|t|<=x_a^(1-beta)`. Thus no fixed subunit Mellin exponent can contain arbitrarily accurate positive returns. The tolerance deteriorates with `beta`, so NB-197 remains stronger when one prescribes a large fixed tolerance inside its shorter corridor.

NB-199 resolves the vanishing-tolerance regime more sharply by using the actual phase-window scale rather than freezing a power margin. Put `X_a=log x_a=r_0/a`. In the diagonal range

`X_a^2 <= |t| <= x_a/(U_0 X_a)`,

one has the explicit lower bound

`A_a(t) >= c * log(x_a/(|t|X_a))/X_a`.

Equivalently, `A_a(t)<=eta` forces

`|t| >= x_a^(1-C eta)/log x_a`.

In particular, if the required positive-return tolerance satisfies `eta_a=o(1/log x_a)=o(a)`, no return can occur below a constant multiple of the final logarithmic Mellin layer `x_a/log x_a`. The positive recurrence frontier has therefore moved from a technology-dependent fixed power to a thin endpoint layer whose width is measured directly by the requested accuracy.

The next positive-source question is now genuinely endpoint-scale: determine what happens inside the remaining `t~x_a/log x_a` layer, or prove that the Nyman destination actually requires a positive-shell return accurate enough for NB-199 to apply. A different continuation must leave positivity and control signed/complex synthesis, where occupancy arguments no longer convert small aggregate error into monotone source mass concentration.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-199 are acquisition theorems in coefficient/phase topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all `K` normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but NB-192--NB-193 show that positive recurrence becomes double-exponentially nonuniform as `a->0`; NB-194 gives an early pointwise dephasing corridor; NB-195 gives vanishing-density returns under `a_TT->infinity`; NB-196--NB-197 convert short-interval source density into progressively longer fixed-tolerance pointwise corridors; NB-198 replaces approximation by occupancy to reach every fixed subunit Mellin power for sufficiently accurate returns; and NB-199 pushes vanishing positive tolerances to the final logarithmic Mellin layer.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, long-time prevalence, first-hit/return-free scale, source-specific pointwise dephasing, source-specific mean-square dephasing, **uniform versus almost-all source resolution versus occupancy-only control**, requested return tolerance and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and then test that bound against a matched control on the realized approximation range. In particular, the occupancy gains cannot be imported unchanged into a signed synthesis architecture where exceptional phase cells may cancel rather than carry a monotone mass tariff.