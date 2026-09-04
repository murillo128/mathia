# PL-159 — Finite off-line Suzuki controls cannot alias away lower escape at fixed step

## Claim

The fixed-step aliasing obstruction of `PL-158` is genuinely one-sided. A finite xi-like zero configuration can be tuned so that an off-critical quartet makes the sampled Suzuki screw **bounded above** on one fixed arithmetic progression, but the corresponding lower escape cannot be removed by any finite collection of ordinary high-ordinate off-critical quartets.

Precisely, fix `h>0`. Let a finite symmetric zero multiset be a finite union of quartets

`Gamma_j = { +/-tau_j +/- i theta_j }`,

with positive multiplicities, `theta_j>=0`, and define

`Psi_Gamma(t) = sum_(gamma in Gamma) (1-exp(i gamma t))/gamma^2`.

Assume the configuration is off-line, put

`Theta = max_j theta_j > 0`,

and suppose every quartet on the maximal-displacement layer satisfies

`tau_j > Theta`.

Then

`inf_(n>=0) Psi_Gamma(n h) = -infinity`.

More strongly, there is a sequence `n_k -> infinity` for which

`exp(-Theta n_k h) Psi_Gamma(n_k h)`

converges to a strictly negative constant.

Thus exact fixed-step phase aliasing can hide the **positive** excursions of a finite off-line Suzuki zero model, as `PL-158` shows, but finite torus recurrence inevitably restores a maximal-growth phase at which the same model has a negative exponential excursion. The obstruction is not arithmetic: it is a consequence of simultaneous recurrence of finitely many sampled zero phases.

For the actual zeta screw this yields a conditional frontier statement. If RH is false and the maximal horizontal zero displacement is attained by a finite isolated layer of zero quartets, separated by a positive displacement gap from all remaining zeros, and the edge ordinates satisfy `|Im rho|>Theta`, then for every fixed step `h>0`, including every one-prime ray `h=log p`, the sequence `Psi(nh)` is unbounded below. Therefore a hypothetical lower-bounded fixed prime ray under failure of RH would force a genuinely **non-isolated/infinite horizontal zero frontier** rather than the finite matched-control geometry that defeats upper boundedness.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + MATCHED-CONTROL + STRUCTURAL-BOUNDARY`. Suzuki's unconditional zero expansion is the theorem-level zeta input. The quartet formula is the exact calculation already audited in `PL-158`; simultaneous recurrence on a finite torus is classical Kronecker/Dirichlet theory. The lower-escape conclusion and isolated-frontier corollary are direct deductions. A targeted search combining Suzuki's screw function with fixed-step/arithmetic-progression sampling, bounded-below conditions, and the August 2026 checkpoint literature did not locate this exact finite-control statement. No novelty claim is made.

## The maximal-displacement layer has an exact leading trigonometric coefficient

For one quartet with parameters `(theta,tau)`, `PL-158` gives the exact real formula

`Psi_(theta,tau)(t)`
` = 4/(tau^2+theta^2)^2 * [`
`     2 tau theta sin(tau t) sinh(theta t)`
`     -(tau^2-theta^2)(cos(tau t) cosh(theta t)-1)`
`   ].`

If `theta>0`, division by `exp(theta t)` gives, as `t->infinity`,

`exp(-theta t) Psi_(theta,tau)(t)`
` = [4 tau theta sin(tau t)`
`    -2(tau^2-theta^2) cos(tau t)]/(tau^2+theta^2)^2`
`   + o(1).`

Equivalently the leading oscillation is

`Re( C_(theta,tau) exp(i tau t) )`,

where

`C_(theta,tau) = -2/(tau-i theta)^2`.

The point important for the one-sided question is not the complex representation itself but its value when the sampled phase returns to `1`:

`Re C_(theta,tau)`
` = -2(tau^2-theta^2)/(tau^2+theta^2)^2`.

Hence

`tau>theta  =>  Re C_(theta,tau)<0`.

For a finite family let `Theta=max theta_j`. After division by `exp(Theta t)`, every quartet with `theta_j<Theta` vanishes exponentially. Only the maximal layer survives. If `J_*={j:theta_j=Theta}`, then along any sequence on which all maximal-layer phases converge to `1`,

`exp(-Theta t) Psi_Gamma(t)`
` -> -2 sum_(j in J_*) m_j (tau_j^2-Theta^2)/(tau_j^2+Theta^2)^2`,

where `m_j` denotes the positive multiplicity. Under `tau_j>Theta` every summand is strictly negative, so the limit is a negative constant.

This sign is exactly why the resonant quartet in `PL-158` goes to `-infinity`: exact resonance is merely the simplest case in which the return to phase `1` occurs at every sample. Exact resonance is not needed for lower escape.

## Finite torus recurrence forces simultaneous phase returns on every fixed step

At the sampled times `t=n h`, the maximal-layer phases are

`z_j^n`,  where  `z_j=exp(i tau_j h)`.

There are only finitely many `j in J_*`. The orbit

`n -> (z_j^n)_(j in J_*)`

lies in a finite-dimensional compact torus. The closure of this cyclic orbit is a compact subgroup, so the identity is recurrent. Equivalently, Dirichlet simultaneous approximation gives integers `n_k->infinity` such that

`z_j^(n_k) -> 1`

for every maximal-layer frequency simultaneously. Rational relations among the `tau_j h/(2 pi)` cause no difficulty: rational coordinates return exactly on suitable multiples, while the remaining coordinates admit simultaneous approximation.

Substituting `t=n_k h` into the preceding asymptotic therefore yields

`exp(-Theta n_k h) Psi_Gamma(n_k h) -> -C_*`,

with

`C_* = 2 sum_(j in J_*) m_j (tau_j^2-Theta^2)/(tau_j^2+Theta^2)^2 > 0`.

Since `Theta>0` and `n_k->infinity`, it follows that

`Psi_Gamma(n_k h) -> -infinity`.

No anti-aliasing property of `h` is required. In particular, the conclusion holds for `h=log p`, for an arbitrary real step, and even when several maximal-layer ordinates alias to the same sampled phase. Aliasing cannot cancel the recurrent negative return because at the identity every maximal-layer coefficient has the same strict sign.

## Extension to an isolated finite zeta zero frontier

Suzuki proves unconditionally

`Psi(t)=sum_gamma (1-exp(i gamma t))/gamma^2`,

where `gamma` ranges over the zeros of `xi(1/2-i z)`, with multiplicity, and

`sum_gamma |gamma|^-2 < infinity`.

Suppose hypothetically that RH is false and that the maximal displacement

`Theta = sup_rho |Re(rho)-1/2| > 0`

is attained by only finitely many symmetry quartets. Assume moreover that there is `delta>0` such that every non-edge zero satisfies

`|Re(rho)-1/2| <= Theta-delta`.

For the edge quartets write their positive ordinates as `tau_j` and assume `tau_j>Theta`. Split the zero series into the finite edge part and the rest. The absolute convergence of `sum |gamma|^-2` gives, after multiplying by `exp(-Theta t)`,

`edge remainder from lower-displacement zeros = O(exp(-delta t)) + O(exp(-Theta t))`,

uniformly after summation. Hence the normalized full zeta screw has the same maximal-layer asymptotic as the finite model.

Finite torus recurrence for the edge ordinates then gives, for every `h>0`, a subsequence `n_k` such that

`exp(-Theta n_k h) Psi(n_k h) -> -C_* < 0`,

and therefore

`inf_n Psi(nh)=-infinity`.

This is only a conditional spectral-edge statement. It does **not** establish that zeta has an attained or isolated rightmost zero line if RH fails. Indeed that is exactly the loophole left by the theorem: an infinite family of zeros with displacements approaching the frontier can prevent any fixed finite set of phases from governing the asymptotic samples.

## Relation to PL-153, PL-154, and PL-158

`PL-153` proves that for the actual continuous screw, either a finite upper ceiling or a finite lower floor already implies RH. It then transfers both conditions to the **union of all prime-power event times** using convexity and a shrinking event mesh. `PL-154` strengthens that result by recovering the horizontal zero frontier from either one-sided power-growth exponent on the same dense prime-power event skeleton.

A single prime ray is different: `t=n log p` has fixed spacing. `PL-158` shows that an off-line quartet can be placed in exact resonance with that spacing, making the samples bounded above while the continuous screw still has excursions of both signs. The present result shows that this matched-control failure is orientation-specific. On a finite off-line zero model, no choice of fixed step can prevent simultaneous returns of the finitely many dominant phases to the identity, where their leading coefficients are all negative.

So the two one-sided fixed-ray questions have different generic controls:

- upper boundedness is defeated by exact aliasing of even one off-line quartet;
- lower boundedness survives every finite high-ordinate quartet control because finite phase recurrence forces negative exponential returns.

This does **not** make lower boundedness of `Psi(n log p)` an RH criterion. It says only that any counterexample mechanism for the actual infinite zeta zero set must exploit genuinely infinite frontier structure rather than finite aliasing.

## Prior art and novelty audit

The zeta-specific theorem-level source is:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. Theorem 1.1 supplies the unconditional zero representation and the absolute-convergence/growth framework used here; Suzuki's Theorem 1.6 supplies the continuous boundedness criterion that motivates the sampled question.

The recurrence input is classical Kronecker/Dirichlet theory: a finite set of phases under an integer translation generates a cyclic subgroup of a compact torus whose identity is recurrent. This is standard harmonic/dynamical background and is not a novelty claim.

The current audit searched for Suzuki screw-function results combined with `sampling`, `fixed step`, `arithmetic progression`, `bounded below`, and `almost periodic`/`Kronecker` language, and also checked the current August 2026 prime-power-checkpoint literature. The latter explicitly distinguishes complete interval certification from numerical sampling grids. No source located in the bounded search states the exact fixed-step finite-control lower-escape lemma or the isolated-frontier corollary. This absence is not evidence of novelty: once `PL-158` exposes the sampled zero series, the recurrence argument is elementary.

## Adversarial boundaries

1. **Finite domination is essential.** The proof synchronizes only finitely many maximal-growth phases. It does not synchronize the full infinite zeta zero set. If horizontal displacements accumulate at `Theta` with no gap, modes with slightly smaller displacement but arbitrarily many ordinates can remain relevant on increasing time scales.

2. **The sign hypothesis `tau_j>Theta` is used exactly once.** It makes the recurrent identity-phase coefficient strictly negative. The theorem is not claimed for artificial quartets whose ordinate is smaller than their horizontal displacement. The condition is tailored to the ordinary high-ordinate xi-like regime, not to arbitrary entire symmetric polynomials.

3. **No claim is made that the zeta frontier is attained.** `PL-154` deliberately defines the frontier as a supremum. The present corollary applies only when an off-line frontier is attained by a finite isolated layer. If the supremum is unattained, or if infinitely many zero lines approach it, the argument does not decide the sampled lower-bound question.

4. **The result is not a proof that one-prime lower boundedness implies RH.** It only identifies what failure of that implication would have to look like on the zero side: the simple finite matched controls available against upper boundedness are excluded, leaving an infinite-frontier cancellation problem.

5. **No Euler product or critical-strip continuation is smuggled into the calculation.** The matched-control theorem is finite and exact. The zeta corollary starts from Suzuki's already-completed zero series, whose validity is unconditional; the only limiting step uses its absolutely summable `|gamma|^-2` weights together with a positive displacement gap.

6. **The recurrence is universal rather than arithmetic.** The same argument works for any fixed `h`; choosing `h=log p` adds no extra rigidity. Therefore this finding does not yet supply the missing prime-lattice mechanism. It isolates a structural asymmetry in the sampled spectral problem that any genuinely arithmetic next step must exploit.

## Consequence for the research line

Do not treat `PL-158` as evidence that both orientations of fixed-ray one-sided boundedness are equally vulnerable to aliasing. The upper direction has a finite exact matched control; the lower direction does not within the ordinary finite high-ordinate xi-like class.

The live question is now sharper: can the **infinite** zeta zero divisor exploit a non-isolated horizontal frontier to keep one fixed prime ray bounded below, or can absolute zero weights, density, and the arithmetic phase module `T log p mod 2 pi` rule that out? Any proof must control an increasing set of near-frontier zero modes, not merely one quartet or any fixed finite truncation. A successful zeta-specific argument here would be qualitatively different from the generic aliasing mechanism of `PL-158` and from the shrinking-mesh interpolation already available for the full prime-power skeleton.