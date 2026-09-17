# MI-051 — Normalized Euler-band access costs inverse source mass, while positive recurrence pays effective dimension and source dephasing

**Evidence level:** exact/derived synthesis from [NB-189](../../findings/NB-189-positive-mass-euler-band-routing-saturates-source-fidelity-tariffs-on-poisson-packed-controls.md) through [NB-196](../../findings/NB-196-short-interval-prime-density-forbids-positive-euler-returns-through-the-13-30-mellin-corridor.md). Sharpness of the variation tariff is within the unrestricted Fourier--Stieltjes scalar-translate class at fixed positive accuracy; the recurrence and dephasing results price specific positive transplant mechanisms rather than all possible high-block synthesis.

NB-189 shows that independently normalized true-amplitude Euler bands can pay the representation-level source-mass and fanout tariffs and still generate a full Fourier code on a Poisson-packed matched control. NB-190 prices the missing operation: obtaining those normalized bands from the genuine scalar Euler translate family.

If a target probe is concentrated on source mass `Theta`, every Fourier--Stieltjes mixture of scalar translates that approximates it with coefficient `ell^1` error at most `epsilon<1` must have total variation at least `(1-epsilon)/Theta`. For the balanced partition with `K asymp 1/a`, each band has `Theta asymp 1/K`, so each normalized coordinate costs `Theta(K)` variation. Smooth cutoffs attain the same order at fixed accuracy. Under source-safe high-ordinate normalization, the corresponding lower tariff is `Omega(H_T)` per normalized band.

NB-191 shows that high-block support does not increase this order at fixed source width. The sharp finite-height synthesizers can be compactly truncated and translated into every sufficiently high dyadic block; finite-frequency Bohr recurrence supplies a common phase return. The coupled limit is different: NB-192 shows that one fixed log-width Euler band already contains `m_a asymp a exp(r_0/a)` rationally independent prime-log phases, so coordinatewise syndetic recurrence has `log L_a >> a exp(r_0/a)`.

NB-193 proves that this scale is not an artifact of demanding every phase separately. For the normalized true-source weights, the weighted return set has Haar volume exponentially small in effective dimension `D_eff asymp m_a`. Thus the natural positive coefficient defect

`A_a(t)=theta_(0,a)^(-1) sum alpha_(n,a)|e^(-it log n)-1|`

still has any fixed-accuracy syndetic inclusion length satisfying `log L_a^avg(eta) >> a exp(r_0/a)`.

NB-194 then uses actual rational-prime dephasing rather than torus-volume entropy. For the normalized full prime-power barycenter `C_a(t)`, Vinogradov--Korobov PNT remainder yields a deterministic return-free corridor reaching `exp(c_eta V(e^(r_0/a)))`. NB-195 extends the specific-block obstruction beyond that pointwise corridor in measure: the true shell has squared coefficient mass `O((a exp(r_0/a))^-1)`, so Montgomery--Vaughan mean square implies that positive returns occupy vanishing relative measure on `[T,2T]` whenever `a_T T->infinity`. The only positive-recurrence escape left there is an isolated exceptional near-return.

NB-196 pushes pointwise exclusion much farther by resolving the actual Euler shell with uniform primes in short intervals. Using the current `17/30+epsilon` short-interval prime-density exponent, a local Mellin Riemann sum approximates the continuum response uniformly for

`|t| <= x_a^(13/30-epsilon)`,  where `x_a=exp(r_0/a)`.

Hence every fixed positive return tolerance is excluded pointwise from a fixed height through that corridor. In the coupled physical block, `[T,2T]` is eventually return-free whenever

`limsup_(T->infinity) a_T log(2T)/r_0 < 13/30`.

The constant `13/30` is therefore a **current theorem-uniformity boundary**, the complement of the available `17/30` short-interval exponent, not an intrinsic Nyman phase transition. Beyond `x_a^(13/30-o(1))`, NB-195 still gives vanishing-density positive returns but not emptiness; the remaining positive route is genuinely an isolated-large-value problem for the source Dirichlet polynomial.

The reusable lesson is that **representation complexity, acquisition variation, recurrence entropy, mean-square dephasing and pointwise source resolution are separate currencies**. Inverse source mass is the sharp scalar-mixture tariff. Fixed-width locality is free by almost periodicity. In the shrinking-width limit, positive recurrence is first made nonuniform by effective dimension, then sparse on the actual block by mean square, and now excluded pointwise through the range where short-interval prime density resolves the Mellin oscillation.

**Boundary.** NB-196 excludes only positive `ell^1` recurrence of the normalized true Euler shell inside the current short-interval Mellin corridor. It does not make `13/30` intrinsic, settle isolated near-maximal values beyond that corridor, lower-bound every scalar acquisition mechanism, or exclude signed/complex aggregation and non-recurrence constructions. NB-190--NB-196 also do not identify the actual variation/operator budget of the Nyman approximation class or prove that its realized range requires independent recovery of all normalized bands. A useful continuation must either extend pointwise source resolution beyond the current short-interval exponent, control isolated large values there, or leave the positive topology for a source-safe signed response norm.
