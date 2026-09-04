# PL-161 — One-sided fixed-step Suzuki boundedness phase-pins any surviving off-line frontier

## Claim

Let `Psi` be Masatoshi Suzuki's completed real even screw potential for the Riemann zeta function, and fix an arbitrary sampling step `h>0`. Write

`Theta = sup { Re(rho) : xi(rho)=0 }`,

`theta = Theta-1/2`.

Assume RH is false, so `theta>0`, and put

`R_h = exp(-theta h) < 1`.

If the fixed-step sample sequence

`a_n = Psi(nh)`,  `n>=0`,

is bounded on **either one side** — bounded above or bounded below — then there exists a sequence of nontrivial zeta zeros

`rho_j = beta_j + i T_j`,  `beta_j>1/2`,

such that

`beta_j -> Theta`

and

`exp(i T_j h) -> 1`.

Equivalently,

`dist(T_j h/(2 pi), Z) -> 0`.

For a one-prime exponent-lattice ray, `h=log p`, this becomes

`beta_j -> Theta`,  `p^(i T_j) -> 1`.

Thus one-sided boundedness on a fixed prime ray cannot coexist with an arbitrary off-line horizontal zero frontier. Any surviving frontier must accumulate at the exact sampled phase identity seen by that ray.

There is a sharper lower-bounded consequence. `PL-160` proves that, under RH failure, an **attained** rightmost zero frontier makes `Psi(nh)` unbounded below for every `h>0`. Hence

`Psi(nh) bounded below`

forces not only that `Theta` is unattained, but that there are **distinct** zeros with

`beta_j -> Theta`,  `|T_j| -> infinity`,  `exp(i T_j h) -> 1`.

So the only fixed-ray lower-bounded loophole left after `PL-160` is an **unattained and phase-pinned** frontier.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRINGSHEIM-BOUNDARY + STRUCTURAL-REDUCTION`. Suzuki's zero expansion is peer-reviewed theorem-level input. The positive-coefficient boundary step is the classical Vivanti--Pringsheim theorem. The grouped sampled Cauchy transform, alias noncancellation on each horizontal-displacement circle, and phase-pinning conclusion are exact deductions. A targeted current-literature search did not locate this fixed-step frontier-pinning statement, but no novelty claim is made: its ingredients are classical once Suzuki's completed zero series is sampled.

## The sampled zero series has a finite-measure Cauchy-transform continuation

Suzuki proves unconditionally, for every real `t>=0`,

`Psi(t) = sum_gamma (1-exp(i gamma t))/gamma^2`,

where `gamma` ranges over the zeros of `z -> xi(1/2-i z)`, with multiplicity, and the zero weights satisfy

`sum_gamma |gamma|^(-2) < infinity`.

If `rho=beta+iT` is a zero of `xi`, then

`gamma = i(rho-1/2) = -T + i(beta-1/2)`.

Consequently the sampled mode is

`exp(i gamma n h)`

and its geometric-series pole location is

`q_gamma = exp(-i gamma h)`.

Its modulus is

`|q_gamma| = exp((beta-1/2)h)`.

In particular, the zeros on the **left** of the critical line, `beta=1/2-eta`, `eta>0`, produce pole locations of radius

`exp(-eta h)<1`,

while their symmetric right-side partners produce reciprocal radii larger than one.

Set

`A_h(z)=sum_(n>=0) Psi(nh) z^n`.

Since every zero displacement satisfies `|beta-1/2|<=theta`, the zero expansion may be summed geometrically and interchanged absolutely for

`|z| < R_h = exp(-theta h)`.

Writing

`S = sum_gamma gamma^(-2)`,

one obtains the exact germ

`A_h(z)`
` = S/(1-z)`
`   - sum_gamma [ gamma^(-2) / (1-z/q_gamma) ].`

Fixed-step aliasing means that distinct zeros may have the same `q_gamma`. Group them exactly by defining

`C_h(q) = sum_(gamma : q_gamma=q) gamma^(-2)`.

Absolute convergence gives

`sum_q |C_h(q)| <= sum_gamma |gamma|^(-2) < infinity`.

Discard the exactly cancelled alias classes and put

`Q_h^* = { q : C_h(q) != 0 }`.

Then

`A_h(z)=S/(1-z)-sum_(q in Q_h^*) C_h(q)/(1-z/q)`

throughout the initial disk. The second term is the Cauchy transform of the finite complex atomic measure

`nu_h = sum_(q in Q_h^*) q C_h(q) delta_q`,

up to the harmless sign convention for the Cauchy kernel. Its total variation is finite because all `|q|` lie in the compact annulus

`exp(-theta h) <= |q| <= exp(theta h)`.

This formulation is useful because it makes exact alias cancellation part of the measure itself rather than an informal pole count. The transform is analytic off `supp(nu_h)`. Conversely, every point of `supp(nu_h)` is a genuine singular point of this Cauchy-transform continuation: distributionally, `bar-partial C(nu_h)` is a nonzero constant multiple of `nu_h`, so a holomorphic continuation through an open neighborhood meeting the support would force `nu_h` to vanish there. This remains valid when pole locations accumulate and avoids assuming that a boundary pole is isolated.

## Every actual off-line displacement circle leaves a noncancelled sampled pole

The main possible loophole is destructive aliasing: perhaps all poles corresponding to zeros at a given horizontal displacement cancel after sampling. For the actual zeta symmetry this cannot happen.

Fix an attained displacement `eta>0`, meaning that zeta has at least one zero with real part `1/2+eta` and hence, by the functional equation, zeros with real part `1/2-eta`. The growing sampled parameters on that left line occur in conjugate ordinate pairs

`gamma_+ = T-i eta`,

`gamma_- = -T-i eta`,

up to ordering. Their combined zero weight is

`1/(T-i eta)^2 + 1/(-T-i eta)^2`
` = 2(T^2-eta^2)/(T^2+eta^2)^2.`

For every hypothetical off-critical zeta zero this quantity is strictly positive. Indeed `eta<=1/2`, while the rigorous Platt--Trudgian verification places every possible off-critical zero above height `3*10^12`, so `|T|>eta` automatically.

Summing over all zeros on the displacement line, with positive multiplicities, therefore gives the absolutely convergent strict inequality

`sum_(Im gamma=-eta) gamma^(-2) > 0`.

But every such `gamma` has

`|q_gamma|=exp(-eta h)`,

and grouping by the sampled phase gives exactly

`sum_(q : |q|=exp(-eta h)) C_h(q)`
` = sum_(Im gamma=-eta) gamma^(-2)`
` > 0`.

Hence **not every alias class on that displacement circle can cancel**. For every horizontal displacement `eta>0` actually realized by a zeta zero, at least one point of `Q_h^*` remains on the circle

`|q|=exp(-eta h)`.

This sign argument is the load-bearing zeta-specific input beyond generic fixed-step aliasing. It does not say that each individual zero survives grouping; it says that complete annihilation of an entire displacement layer is impossible.

## The Taylor radius is exactly the horizontal zero frontier

By definition of `Theta`, every pole location satisfies

`|q| >= R_h=exp(-theta h)`.

On the other hand, because `theta` is the supremum of the actual positive horizontal displacements, there are attained displacement values `eta_j -> theta`. The preceding noncancellation lemma supplies, for each `eta_j`, a nonzero alias class `q_j in Q_h^*` with

`|q_j|=exp(-eta_j h) -> R_h`.

Therefore

`dist(0,supp(nu_h)) = R_h`.

The term `S/(1-z)` is analytic on a neighborhood of the closed disk of radius `R_h`, because RH failure gives `R_h<1`. The Cauchy-transform support statement then shows that the Taylor series of `A_h` at zero has **exactly** the radius

`rad(A_h)=R_h=exp(-(Theta-1/2)h)`.

This equality is stronger than the elementary upper growth estimate. It says that fixed-step phase cancellations may move individual poles or cancel alias classes, but they cannot increase the exponential radius beyond the horizontal zero frontier, because every realized displacement layer leaves some nonzero atomic mass and those layers approach the supremum.

If the frontier is unattained, no atom need lie exactly on `|z|=R_h`; the singular boundary can instead arise from accumulation of noncancelled pole locations. The finite-measure support formulation handles both cases uniformly.

## One-sided boundedness pins the Pringsheim singularity to positive phase

Suppose first that `Psi(nh)` is bounded below. Choose a real constant `M` such that

`b_n = Psi(nh)+M >= 0`

for all `n`. Its generating function is

`B_h(z)=A_h(z)+M/(1-z)`.

Because `R_h<1`, the added geometric term is analytic at every point with modulus `R_h`, so

`rad(B_h)=R_h`.

The Vivanti--Pringsheim theorem now applies: a power series with nonnegative real coefficients and finite radius `R_h` must be singular at the **positive real boundary point**

`z=R_h`.

The same conclusion follows if `Psi(nh)` is bounded above, by taking instead

`b_n=M-Psi(nh)>=0`,

so that `B_h(z)=M/(1-z)-A_h(z)`.

Since the only possible singularities of the Cauchy-transform continuation inside the unit disk lie in `supp(nu_h)`, the Pringsheim singularity forces

`R_h in supp(nu_h)`.

By definition of support, there are noncancelled alias locations

`q_j in Q_h^*`,  `q_j -> R_h`.

For all sufficiently large `j`, `|q_j|<1`, so choose a left-side zero parameter in the corresponding alias class. Writing its displacement and ordinate as `eta_j>0` and `T_j`,

`q_j = exp(-eta_j h) exp(+/- i T_j h)`.

Convergence to the positive real number `R_h` gives simultaneously

`eta_j -> theta`

and

`exp(i T_j h) -> 1`

after changing the ordinate sign if necessary. Reflecting the associated left-side zeros across the functional equation gives right-side zeros

`rho_j=beta_j+iT_j`,

with

`beta_j=1/2+eta_j -> Theta`.

This proves the claim.

## Prime-exponent interpretation

For the fixed prime ray

`0,e_p,2e_p,3e_p,...`,

the exponent-lattice energy is

`E(n e_p)=n log p`,

so the sampling step is canonically

`h=log p`.

The sampled pole coordinate associated with a left-side zero displacement `eta` and ordinate `T` is therefore

`q = p^(-eta) p^(iT)`.

The radial coordinate records the horizontal zero displacement, while the angular coordinate is exactly the prime-torus phase at that zero ordinate. Under RH failure, one-sided boundedness of the ray forces pole support to approach the positive radial frontier:

`p^(-eta_j) p^(iT_j) -> p^(-theta)`.

Equivalently,

`eta_j -> theta`,  `p^(iT_j) -> 1`.

This is a genuine fixed-axis spectral constraint that does not appear in the shrinking-mesh interpolation of `PL-156`/`PL-157`. It also makes precise the aliasing language of `PL-158`: the only way a one-sided sampled sequence can place its dominant singularity where Pringsheim requires it is for near-frontier zero modes to accumulate at the sampled phase identity.

The condition is nevertheless **not intrinsically prime-specific** as a theorem: it holds for every fixed real step `h>0`. The prime lattice supplies canonical steps `log p`; it does not by itself prove that actual zeta ordinates cannot satisfy the resulting resonance condition.

## Relation to PL-158, PL-159, and PL-160

`PL-158` constructs, for every fixed step, a finite symmetric off-line control whose sampled screw is bounded above. In generating-function language that example has an attained frontier pole exactly at the positive point `R_h`: the off-line frequency was deliberately chosen so that `T h in 2 pi Z`. It therefore **saturates** the present necessary phase-pinning condition rather than contradicting it.

`PL-159` shows that finite high-ordinate off-line controls cannot similarly hide lower escape, because recurrence returns the finitely many dominant phases to identity where their leading coefficient has the negative sign. `PL-160` removes the finite/isolation assumptions: if the actual zeta horizontal frontier is attained, every fixed-step sample sequence is unbounded below.

Combining `PL-160` with the present result gives the sharper alternative

`Psi(nh) bounded below`

`=> RH`

`   or [Theta is unattained and there are zeros rho_j with`

`       Re(rho_j)->Theta and exp(i Im(rho_j) h)->1].`

Under the second alternative the zeros are necessarily distinct and their ordinates tend to infinity, because the zero set is discrete and the frontier is unattained.

For upper boundedness there is no corresponding attainment exclusion: `PL-158` demonstrates that an attained exactly resonant quartet can keep the samples bounded above in a matched control. The present theorem supplies only the necessary phase-pinning condition.

## Prior-art and novelty audit

The theorem-level zeta input is:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487. DOI `10.1112/jlms.12785`; arXiv `2206.03682`. Theorem 1.1 supplies the unconditional completed zero expansion and the absolutely summable `gamma^(-2)` framework used here.
- **Dave Platt, Tim Trudgian**, “The Riemann hypothesis is true up to `3*10^12`,” *Bulletin of the London Mathematical Society* **53**(3) (2021), 792--797. DOI `10.1112/blms.12460`. It is used only to make the elementary sign `T^2-eta^2>0` unconditional for every hypothetical off-line zeta zero.

The positive-coefficient boundary theorem is classical:

- **Vivanti--Pringsheim theorem**: if a power series with nonnegative real coefficients has finite radius `R`, then `z=R` is a singularity. A standard modern reference is Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, Theorem IV.6.

The Cauchy-transform support fact is standard complex/harmonic analysis: for a finite complex measure `nu`, its Cauchy transform is holomorphic off `supp(nu)` and distributionally has `bar-partial` equal to a nonzero constant multiple of `nu`. It is used here only to make accumulation and exact alias cancellation rigorous.

A targeted search combined Suzuki's screw function with fixed-step/arithmetic-progression sampling, generating functions, Pringsheim/Landau boundary arguments, and sampled zero phases. It located Suzuki's continuous criteria and generic Pringsheim references but no published statement of the exact frontier phase-pinning consequence above. That absence is not evidence of novelty. The safe classification is exact derived structure built from established ingredients.

## Adversarial boundaries

1. **This does not prove RH from one fixed ray.** The conclusion is necessary, not contradictory: an unattained zero frontier could in principle contain a sequence whose ordinates approach the resonance lattice `2 pi Z/h` while its real parts approach `Theta`.

2. **The lower and upper orientations remain different.** Lower boundedness inherits the non-attainment restriction from `PL-160`; upper boundedness does not. The exact resonant quartet of `PL-158` is a matched control showing why no stronger generic upper conclusion follows.

3. **The result does not produce simultaneous resonance for two prime axes.** If boundedness hypotheses are known separately for `h=log p` and `h=log q`, Pringsheim may select different near-frontier zero subsequences for the two steps. Irrationality of `log p/log q` does not by itself synchronize those subsequences.

4. **Joint two-dimensional sampling is different from separate one-dimensional marginals.** Distinct frequencies can form checkerboard alias patterns whose row and column sums vanish separately even though the joint phase pairs are distinct. Thus one must not infer from this finding that two incommensurable one-prime sequences automatically eliminate all finite aliasing. `PL-155` already handles the genuinely joint two-prime face for the completed screw kernel by a different dense-difference argument.

5. **Complete alias cancellation was ruled out only layerwise for the actual zeta symmetry and weights.** Individual sampled poles can cancel. The proof needs only the strict positivity of the total `gamma^(-2)` weight on each left horizontal displacement line, which guarantees that at least one alias class survives there.

6. **The Cauchy-transform support step is load-bearing.** Normal convergence away from the pole-support closure is not enough by itself when poles accumulate. The finite-measure distribution identity is what prevents an open holomorphic continuation through a support point even in the non-isolated case.

7. **No Euler product is analytically continued.** The argument starts from Suzuki's already-completed zero expansion, valid unconditionally for all real `t`, and then uses ordinary generating functions in the sample index. The radius `R_h` is a spectral growth radius of that sampled completed object, not an Euler-product convergence radius.

A falsification would require failure of Suzuki's zero expansion/absolute zero weights, an error in the sampled geometric-series identity, complete cancellation of an entire off-line displacement circle despite its strictly positive paired total weight, failure of the finite-measure Cauchy-transform support identity, or failure of the Vivanti--Pringsheim theorem.

## Consequence for the research line

The remaining fixed one-prime lower-boundedness problem is now narrower than the unattained-frontier alternative left by `PL-160`. Under RH failure it would require a moving population of zeros that satisfies **two simultaneous asymptotic conditions**:

`Re(rho_j) -> Theta`

and

`p^(i Im(rho_j)) -> 1`.

Future work on that branch should therefore target whether known zero-density/explicit-formula information can exclude or quantitatively constrain this coupled radial-angular concentration. Merely enlarging finite recurrence controls or proving more generic fixed-step aliasing statements will not address the surviving case.

The prime-exponent interpretation is exact but modest: one prime axis converts horizontal zero displacement into radial pole approach and the zero ordinate into a torus phase. One-sided boundedness forces the near-frontier spectral mass toward the identity phase; what remains unknown is whether rational-prime arithmetic can forbid that concentration.