# MI-051 — Normalized Euler-band access costs inverse source mass, while positive recurrence pays effective dimension and source dephasing

**Evidence level:** exact/derived synthesis from [NB-189](../../findings/NB-189-positive-mass-euler-band-routing-saturates-source-fidelity-tariffs-on-poisson-packed-controls.md) through [NB-197](../../findings/NB-197-almost-all-short-interval-prime-density-pushes-positive-euler-dephasing-to-the-13-15-mellin-corridor.md). Sharpness of the variation tariff is within the unrestricted Fourier--Stieltjes scalar-translate class at fixed positive accuracy; the recurrence and dephasing results price specific positive transplant mechanisms rather than all possible high-block synthesis.

NB-189 shows that independently normalized true-amplitude Euler bands can pay the representation-level source-mass and fanout tariffs and still generate a full Fourier code on a Poisson-packed matched control. NB-190 prices the missing operation: obtaining those normalized bands from the genuine scalar Euler translate family.

If a target probe is concentrated on source mass `Theta`, every Fourier--Stieltjes mixture of scalar translates that approximates it with coefficient `ell^1` error at most `epsilon<1` must have total variation at least `(1-epsilon)/Theta`. For the balanced partition with `K asymp 1/a`, each band has `Theta asymp 1/K`, so each normalized coordinate costs `Theta(K)` variation. Smooth cutoffs attain the same order at fixed accuracy. Under source-safe high-ordinate normalization, the corresponding lower tariff is `Omega(H_T)` per normalized band.

NB-191 shows that high-block support does not increase this order at fixed source width. The sharp finite-height synthesizers can be compactly truncated and translated into every sufficiently high dyadic block; finite-frequency Bohr recurrence supplies a common phase return. The coupled limit is different: NB-192 shows that one fixed log-width Euler band already contains `m_a asymp a exp(r_0/a)` rationally independent prime-log phases, so coordinatewise syndetic recurrence has `log L_a >> a exp(r_0/a)`.

NB-193 proves that this scale is not an artifact of demanding every phase separately. For the normalized true-source weights, the weighted return set has Haar volume exponentially small in effective dimension `D_eff asymp m_a`. Thus the natural positive coefficient defect

`A_a(t)=theta_(0,a)^(-1) sum alpha_(n,a)|e^(-it log n)-1|`

still has any fixed-accuracy syndetic inclusion length satisfying `log L_a^avg(eta) >> a exp(r_0/a)`.

NB-194 then uses actual rational-prime dephasing rather than torus-volume entropy. For the normalized full prime-power barycenter `C_a(t)`, Vinogradov--Korobov PNT remainder yields a deterministic return-free corridor reaching `exp(c_eta V(e^(r_0/a)))`. NB-195 extends the specific-block obstruction beyond that pointwise corridor in measure: the true shell has squared coefficient mass `O((a exp(r_0/a))^-1)`, so Montgomery--Vaughan mean square implies that positive returns occupy vanishing relative measure on `[T,2T]` whenever `a_T T->infinity`. The only positive-recurrence escape left there is an isolated exceptional near-return.

NB-196 converts a **uniform** short-interval prime theorem into pointwise source dephasing. Resolving every cell at spatial scale `x_a^(17/30+epsilon)` gives the continuum shell response uniformly through `|t|<=x_a^(13/30-epsilon)` and excludes every fixed positive return tolerance there.

NB-197 shows that positivity can exploit a substantially stronger **almost-all** source theorem. Guth--Maynard resolve almost every interval already at length `x^(2/15+epsilon)`. A shifted-grid averaging argument chooses a partition for which bad cells have exponentially small total length. Because the Euler source weights are positive, their total bad-cell von-Mangoldt mass is `o(1)` and can be discarded uniformly in `t`. The same continuum response therefore holds through

`|t| <= x_a^(13/15-epsilon)`.

Hence `[T,2T]` is eventually positive-return-free whenever

`limsup_(T->infinity) a_T log(2T)/r_0 < 13/15`.

The improvement from `13/30` to `13/15` does not come from a stronger recurrence argument. It comes from matching the **quantifier of the source theorem to the positivity of the acquisition channel**: uniform control of every spatial cell is unnecessary when the exceptional cells have negligible total positive mass. The chosen grid is a proof device independent of `t`, so an almost-all spatial theorem still yields pointwise exclusion in Mellin frequency.

The constants `13/30` and `13/15` are theorem-resolution boundaries, respectively complementary to the currently imported uniform `17/30` and almost-all `2/15` short-interval exponents. Neither is an intrinsic Nyman phase transition. Beyond the larger corridor NB-195 still gives vanishing-density positive returns but not emptiness; the surviving positive route is an isolated-large-value problem or requires better local-density input.

The reusable lesson is that **representation complexity, acquisition variation, recurrence entropy, mean-square dephasing, source-resolution quantifiers and positivity are separate currencies**. Inverse source mass is the sharp scalar-mixture tariff. Fixed-width locality is free by almost periodicity. In the shrinking-width limit, positive recurrence is first made nonuniform by effective dimension, then sparse on the actual block by mean square, and finally excluded pointwise as far as source density can be transferred through the positive-mass channel. An almost-all source theorem can be enough for a pointwise destination theorem when positivity converts exceptional spatial volume into negligible source mass.

**Boundary.** NB-197 excludes only positive `ell^1` recurrence of the normalized true Euler shell inside the current almost-all short-interval Mellin corridor. It does not make `13/15` intrinsic, settle isolated near-maximal values beyond that corridor, lower-bound every scalar acquisition mechanism, or extend to signed/complex aggregation where exceptional cells need not be negligible after cancellation. NB-190--NB-197 also do not identify the actual variation/operator budget of the Nyman approximation class or prove that its realized range requires independent recovery of all normalized bands. A useful continuation must either extend pointwise source resolution beyond the current almost-all exponent, control isolated large values there, or leave the positive topology for a source-safe signed response norm.
