# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price the physically admissible scalar acquisition budget in the coupled source-height limit

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-052-brun-titchmarsh-occupancy-pushes-positive-return-obstruction-to-the-mellin-endpoint`.

The source-side program has separated raw phase accessibility, representation complexity and physical Euler acquisition. The natural scalar Euler functional escapes the bounded Hilbert dual but is priced by an absolute Wiener/Dirichlet budget `W(a)~1/a`. NB-188 shows that compressing positive source mass into a Hadamard-scale code forces square-root source-density amplification and bounded effective fanout. NB-189 proves those representation tariffs are sharp but nonselective: independently normalized true-amplitude bands still generate a DFT-scale code on a Poisson-packed matched control.

NB-190 prices the missing normalization step for the genuine scalar Euler translate family. A normalized probe supported on source mass `Theta` requires Fourier--Stieltjes mixing variation at least `(1-epsilon)/Theta` at coefficient error `epsilon<1`. For the `K~1/a` balanced bands of NB-189, `Theta~1/K`, so each coordinate costs `Theta(K)` scalar-translate variation; smooth cutoffs attain that order at fixed accuracy. Under source-safe high-ordinate normalization the same lower bound becomes `Omega(H_T)` per band.

NB-191 closes the simplest fixed-resolution locality escape. At every fixed `a` and fixed positive accuracy, compactly truncated sharp synthesizers can be translated into every sufficiently high dyadic block `[T,2T]` with no extra asymptotic variation cost. Finite-frequency Bohr recurrence supplies a common near-return for the active frequencies, so high height alone does not add a universal surcharge.

NB-192--NB-193 quantify the hidden nonuniformity. A single fixed log-width Euler band contains `m_a~a exp(r_0/a)` rationally independent prime-log phases. Coordinatewise common recurrence has double-exponential worst-gap scale in `1/a`, and even the true-source-weighted positive target has exponentially small Haar volume in effective dimension `D_eff asymp m_a`. Positive recurrence is therefore cheap at fixed `a` but catastrophically nonuniform in the coupled `a->0` limit.

NB-194--NB-197 move from recurrence volume to the actual physical block. Vinogradov--Korobov dephasing gives an initial pointwise return-free corridor; Montgomery--Vaughan mean square gives vanishing return density when `a_T T->infinity`; uniform short-interval source resolution gives a `13/30` pointwise Mellin corridor; and positivity plus Guth--Maynard almost-all source resolution extends fixed-tolerance exclusion to exponent `13/15`. Those exponents measure available source-resolution technology rather than an intrinsic recurrence threshold.

NB-198 removes the need to approximate every spatial cell. If a positive return is sufficiently accurate, most von-Mangoldt source mass must lie in the short multiplicative phase windows where `t log n` is near `2 pi Z`. Brun--Titchmarsh bounds how much positive source mass those favorable windows can carry. Consequently no fixed subunit Mellin exponent can contain arbitrarily accurate positive returns.

NB-199 follows the actual window width diagonally toward the endpoint. Put `X_a=log x_a=r_0/a`. In the range

`X_a^2 <= |t| <= x_a/(U_0 X_a)`

one has

`A_a(t) >= c * log(x_a/(|t|X_a))/X_a`.

Thus `A_a(t)<=eta` forces `|t|>=x_a^(1-C eta)/log x_a`; in particular `eta_a=o(1/X_a)` cannot occur below a constant multiple of the final logarithmic layer `x_a/X_a`.

NB-200 shows that the disappearance of the Brun--Titchmarsh logarithmic reserve is **not** the end of positive coercivity. At endpoint height the favorable phase cells become physically shorter than one integer. Then interval-density technology hands off to atomic capacity: each phase cell can carry at most one von-Mangoldt atom. A fixed top logarithmic slab carries a fixed fraction of normalized source mass, while the number of favorable cells available there is only `t h/(2 pi)+O(1)` and each atom has mass at most order `X_a/x_a`.

The resulting one-sided endpoint theorem is explicit. For every fixed

`0 < K < 2 pi e^Delta`

there is `c_K>0` such that, for small `a`,

`inf_(X_a^2 <= |t| <= K x_a/X_a) A_a(t) >= c_K/X_a`.

Equivalently, any sequence with `X_a A_a(t)->0` and bounded endpoint ratio must satisfy

`liminf |t| X_a/x_a >= 2 pi e^Delta`.

The constant is a **capacity threshold**, not an existence theorem. `2 pi` comes from phase periodicity and `e^Delta` from the physical upper edge of the fixed log-width shell. The proof uses only macroscopic PNT mass plus one lattice atom per sub-unit favorable cell; it does not require primes in bounded intervals.

The positive-source frontier is therefore sharper than “inside the final logarithmic layer.” An `o(a)` positive return at endpoint scale must lie at or beyond `(2 pi e^Delta-o(1))x_a/log x_a`. The remaining acquisition question is what happens at and beyond that atomic-capacity threshold, where enough cells exist in principle but their occupation by the actual von-Mangoldt source is still constrained. A separate destination question remains load-bearing: prove that a Nyman approximant capable of resolving the target must realize a positive Euler-shell return with `o(a)` accuracy, or identify the correct destination-coupled source condition if it does not.

A different continuation must leave positivity and control signed/complex synthesis, where both interval occupancy and atomic mass packing cease to be monotone because cancellation can move between phase cells.

## Keep source persistence, acquisition cost and destination conditioning separate

NB-190--NB-200 are acquisition theorems in coefficient/phase topology. They do not establish that the true Nyman realized range contains the Poisson-packed dipoles, nor that the approximation problem demands independent recovery of all normalized bands. Conversely, unrestricted mixtures can synthesize those bands, and fixed-`a` recurrence can eventually transplant them to high blocks, but the coupled source-height limit successively exposes target-volume, pointwise-dephasing, source-resolution, occupancy and finally atomic-capacity obstructions.

Frequency membership, true amplitudes, positive source mass, fanout, representation gain, scalar-mixture total variation, recurrence target volume/effective dimension, long-time prevalence, first-hit/return-free scale, source-specific pointwise dephasing, source-specific mean-square dephasing, **uniform versus almost-all source resolution versus interval occupancy versus atomic cell capacity**, requested return tolerance and destination conditioning are distinct currencies. A successful continuation must identify which of them is actually bounded by the Nyman construction in the simultaneous `a_T`--`T` regime and then test that bound against a matched control on the realized approximation range. The positive occupancy/capacity gains cannot be imported unchanged into a signed synthesis architecture where exceptional cells may cancel rather than carry a monotone mass tariff.