# PL-160 — Attainment of the horizontal zero frontier forces fixed-step Suzuki lower escape

## Claim

Let `Psi` be Suzuki's completed zeta screw potential and write

`Theta = sup { Re(rho) : xi(rho)=0 }`,

`theta = Theta-1/2`.

Assume RH is false, so `theta>0`, and assume the rightmost horizontal zero frontier is **attained**: at least one nontrivial zero satisfies `Re(rho)=Theta`. Then for every fixed sampling step `h>0` there is a sequence `n_k->infinity` such that

`exp(-theta n_k h) Psi(n_k h) -> -C_edge < 0`.

Consequently

`inf_(n>=0) Psi(nh) = -infinity`.

The constant is determined by all zero quartets on the attained edge. If the edge quartets have positive ordinates `tau_j`, multiplicities `m_j`, and common horizontal displacement `theta`, then

`C_edge = 2 sum_(j in edge) m_j (tau_j^2-theta^2)/(tau_j^2+theta^2)^2 > 0`.

For the actual zeta function the sign condition `tau_j>theta` is automatic: `theta<=1/2`, while the rigorous Platt--Trudgian verification puts every off-critical zero, if any exists, above height `3*10^12`.

Thus the finite-isolated-frontier hypothesis in `PL-159` is unnecessary. A fixed one-prime ray `h=log p` can stay bounded below under failure of RH only if the rightmost zero abscissa is **not attained at all**. Infinitely many edge zeros and the absence of a positive displacement gap do not provide an escape.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + ALMOST-PERIODIC-EDGE + STRUCTURAL-REDUCTION`. Suzuki's absolutely convergent zero expansion is theorem-level input; the quartet calculation is inherited from `PL-158`; the new step is an `ell^1` dominated-convergence separation of subedge zeros followed by uniform almost-periodic recurrence of the possibly infinite attained edge. No novelty claim is made.

## Quartet decomposition and a uniform summable majorant

Suzuki proves unconditionally

`Psi(t)=sum_gamma (1-exp(i gamma t))/gamma^2`,

with multiplicity and

`sum_gamma |gamma|^-2 < infinity`.

Using the functional equation and Schwarz symmetry, group the nonreal zero parameters into quartets with horizontal displacement `eta_j>=0` and positive ordinate `tau_j>0`. For one quartet, `PL-158` gives the exact real contribution

`Psi_(eta,tau)(t)`
` = 4/(tau^2+eta^2)^2 * [`
`     2 tau eta sin(tau t) sinh(eta t)`
`     -(tau^2-eta^2)(cos(tau t) cosh(eta t)-1)`
`   ].`

Every displacement satisfies `eta<=theta`. Multiplying by `exp(-theta t)` gives a uniform bound of the form

`exp(-theta t) |Psi_(eta,tau)(t)| <= C/(tau^2+eta^2)`

for all `t>=0`, with an absolute constant `C`. Indeed `exp(-theta t)sinh(eta t)` and `exp(-theta t)cosh(eta t)` are bounded by constants when `eta<=theta`, while

`tau eta <= (tau^2+eta^2)/2`,

`|tau^2-eta^2| <= tau^2+eta^2`.

The resulting majorant is summable over all quartets because it is comparable to the quartet contribution to Suzuki's `sum |gamma|^-2`.

If `eta<theta`, then for each fixed quartet

`exp(-theta t) Psi_(eta,tau)(t) -> 0`

as `t->infinity`. Dominated convergence therefore removes **all** subedge zeros at once, even if there are infinitely many displacements tending upward to `theta` and no positive gap:

`exp(-theta t) Psi(t) = F_edge(t) + o(1)`.

This is the point at which the isolation hypothesis of `PL-159` disappears. A displacement gap is convenient for an elementary exponential estimate, but absolute summability of the completed zero weights already supplies the required global tail control at the exact frontier normalization.

## The attained edge is an absolutely convergent almost-periodic series

For an edge quartet `eta=theta`, expanding `sinh(theta t)` and `cosh(theta t)` after the frontier normalization gives

`exp(-theta t) Psi_(theta,tau)(t)`
` = [4 tau theta sin(tau t)`
`    -2(tau^2-theta^2) cos(tau t)]/(tau^2+theta^2)^2`
`   + o_tau(1)`.

Summing the leading terms over every attained-edge quartet defines

`F_edge(t)`
` = sum_(j in edge) m_j [`
`     4 tau_j theta sin(tau_j t)`
`     -2(tau_j^2-theta^2) cos(tau_j t)`
`   ]/(tau_j^2+theta^2)^2.`

The coefficient series is absolutely summable. The cosine coefficients are `O(tau_j^-2)` and the sine coefficients are even smaller, while Suzuki's zero weights are summable. Hence the Fourier series for `F_edge` converges absolutely and uniformly on the real line. In particular `F_edge` is a uniformly almost-periodic function, and the termwise edge asymptotics combine with the preceding dominated-convergence argument to give the single global formula

`exp(-theta t) Psi(t) = F_edge(t) + o(1)`.

At phase identity,

`F_edge(0)`
` = -2 sum_(j in edge) m_j (tau_j^2-theta^2)/(tau_j^2+theta^2)^2.`

Because the frontier is attained, the edge set is nonempty. For zeta, every member of that edge is off the critical line. Platt and Trudgian rigorously verified that every nontrivial zero with `0<Im(rho)<=3*10^12` lies on `Re(rho)=1/2`; therefore every hypothetical off-line edge zero has `tau_j>3*10^12`. Since `0<theta<=1/2`, each summand above is strictly positive before the minus sign. Thus

`F_edge(0)=-C_edge<0`.

The use of the computational verification is only to make the sign automatic for the actual zeta divisor. The abstract statement remains valid for any symmetric completed zero set whose attained-edge ordinates satisfy `tau_j>theta`.

## Every fixed sampling step recurrently returns the whole infinite edge to phase identity

Fix `h>0`. At the samples `t=nh`, the edge phases are

`z_j^n`,  where  `z_j=exp(i tau_j h)`.

The edge can now be infinite, so finite-dimensional recurrence cannot simply be applied to all phases at once. Absolute convergence supplies the missing step. Given `epsilon>0`, choose a finite edge subset `J` so that the uniform tail of the Fourier series contributes less than `epsilon`. On the finite torus generated by `(z_j)_(j in J)`, the cyclic orbit recurrently approaches the identity. Hence there are arbitrarily large integers `n` for which every `z_j^n`, `j in J`, is as close to `1` as desired.

For such `n`, the finite part of `F_edge(nh)` is arbitrarily close to its value at zero, while the omitted tail changes the comparison by at most `2 epsilon`. Taking `epsilon->0` and choosing the recurrence integers increasingly gives a sequence `n_k->infinity` with

`F_edge(n_k h) -> F_edge(0)=-C_edge`.

Combining this with the frontier asymptotic yields

`exp(-theta n_k h) Psi(n_k h) -> -C_edge<0`.

Since `theta>0`, the unnormalized values satisfy

`Psi(n_k h) -> -infinity`.

No Diophantine property of `h` is required. Rational relations among the edge ordinates merely make some coordinates periodic; the compact-torus recurrence of every finite truncation remains valid. The argument therefore holds for an arbitrary fixed real step and in particular for every one-prime exponent-lattice ray `h=log p`.

## Why the unattained frontier is the exact remaining loophole for this method

If the supremal displacement `theta` is **not** attained, every quartet satisfies `eta_j<theta`. The same summable-majorant argument then gives

`exp(-theta t) Psi(t) -> 0`.

So there is no nonzero frontier Fourier series to recur. This does not imply boundedness on a fixed ray; it shows only that the attained-edge recurrence mechanism has genuinely exhausted its information. To go further one would have to control an increasing collection of zeros with displacements approaching `theta` while their exponential growth rates and very high ordinates change simultaneously.

This distinction is sharper than the boundary left in `PL-159`. There the possible escape was described as a non-isolated or infinite horizontal frontier because the proof synchronized only finitely many maximal phases and used a positive displacement gap. The present `ell^1` argument shows that **infinite multiplicity of an attained edge is harmless**, and that arbitrarily close subedge lines are harmless as well. Only non-attainment of the supremum survives.

## Prior art and novelty audit

The theorem-level zeta input is:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487, DOI `10.1112/jlms.12785`. Suzuki supplies the unconditional zero expansion, absolute `|gamma|^-2` summability, and the completed transform framework used throughout `PL-153`--`PL-160`.
- **Dave Platt, Tim Trudgian**, “The Riemann hypothesis is true up to `3*10^12`,” *Bulletin of the London Mathematical Society* **53**(3) (2021), 792--797, DOI `10.1112/blms.12460`. Their interval-arithmetic verification makes `tau_j>theta` automatic for every hypothetical off-line zeta edge zero.

The recurrence input is classical Bohr/Kronecker theory. The proof here needs only the elementary finite-dimensional statement that a cyclic orbit in a compact torus recurrently approaches the identity, together with uniform approximation of an absolutely convergent trigonometric series by finite sums.

A targeted current search combined Suzuki's screw function with fixed-step sampling, arithmetic progressions, bounded-below conditions, almost periodicity, and the recent prime-power-checkpoint literature. The search located Suzuki's continuous screw criteria and the 2026 checkpoint work, whose interval certificates explicitly differ from a fixed sampling grid, but did not locate this exact attained-frontier extension of the fixed-step lower argument. This absence is not evidence of novelty. Once `PL-159` isolates the finite recurrence mechanism, replacing finite-edge domination by `ell^1` dominated convergence and uniform almost periodicity is a natural classical completion.

## Adversarial boundaries

1. **Attainment remains essential.** The proof gives no lower escape when `theta` is a strict supremum. In fact the same dominated-convergence calculation proves that the `exp(-theta t)`-normalized zero series tends to zero in that case, so the leading almost-periodic edge used here literally does not exist.

2. **This is not yet a fixed-prime RH criterion.** It proves the conditional alternative

   `Psi(n log p) bounded below  =>  RH or the rightmost zero frontier is unattained`.

   Ruling out the unattained alternative would be new zero-distribution information of a different kind.

3. **The result is orientation-specific.** `PL-158` gives an exact finite off-line control that keeps fixed-step samples bounded above. The present theorem does not repair that upper direction; it strengthens only the lower-escape side identified in `PL-159`.

4. **The recurrence is universal, not rational-prime rigidity.** The theorem holds for every `h>0`. Choosing `h=log p` uses the exponent-lattice interpretation but contributes no anti-aliasing theorem. The mathematical advance is a sharper obstruction classification, not a new prime-specific RH mechanism.

5. **Absolute zero weights are load-bearing.** The passage from finitely many edge phases to an infinite attained edge uses Suzuki's absolute `|gamma|^-2` summability twice: to remove arbitrarily near subedge zeros by dominated convergence and to make the edge Fourier series uniformly approximable by finite phase systems.

6. **No Euler product is transported into the critical strip.** All zeta information enters through Suzuki's completed zero expansion, valid unconditionally. The proof never continues a prime Euler product beyond its convergence domain.

7. **The Platt--Trudgian input is not being used as evidence for RH at unverified heights.** It serves only the elementary sign check `tau_j>theta` for a hypothetical off-line edge zero: any such zero must lie above the verified range, while `theta<=1/2`.

A falsification would require failure of the quartet asymptotic inherited from `PL-158`, failure of the summable uniform majorant, failure of dominated convergence over the zero quartets, or failure of finite-torus recurrence after uniformly truncating the edge Fourier series.

## Consequence for the research line

The fixed one-prime lower-boundedness question is now reduced to a much narrower zero-side pathology. Under failure of RH, **an attained rightmost zero line is incompatible with lower boundedness on every fixed ray**, even if that line contains infinitely many zeros and even if other zero lines accumulate arbitrarily close to it.

Therefore future work on the remaining fixed-ray lower question should not spend effort on larger finite controls, infinite collections sitting exactly on one maximal line, or restoring a displacement gap. The only surviving zero geometry for a counterexample is an **unattained horizontal frontier**: a sequence of off-line zeros whose real parts approach `Theta` strictly from below. Any further progress must control that moving near-frontier population and its sampled phases simultaneously, or import genuinely arithmetic information capable of excluding such a frontier. That is a qualitatively different problem from the finite aliasing mechanism of `PL-158` and the finite-edge recurrence of `PL-159`.