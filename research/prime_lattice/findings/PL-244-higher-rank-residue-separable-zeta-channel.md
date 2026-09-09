# PL-244 — Higher-rank quadratic WMDS residues retain reciprocity only as a separable factor from the rank-one zeta channel

## Claim

`PL-243` deliberately left higher-rank Weyl-group multiple Dirichlet series open because a residue can retain a genuinely nontrivial lower-rank multiple Dirichlet series instead of collapsing completely to a scalar. Diaconu–Ion–Paşol–Popa (2025) prove exactly that phenomenon for finite quadratic Weyl-group multiple Dirichlet series: at a simple-short-root polar divisor, the residue factors as the WMDS attached to the root subsystem orthogonal to that root times an explicit product of rank-one zeta factors.

This confirms that the higher-rank caveat in `PL-243` is real, but it also supplies a sharper obstruction for the current `prime_lattice` target. The surviving mixed-prime reciprocity object and the rank-one factor carrying the Riemann-zeta divisor are **multiplicatively separable**. In particular, an explicit `A_4` endpoint residue over the Gaussian field retains a nontrivial `A_2` quadratic WMDS while the Riemann-sensitive zeros remain in independent Dedekind-zeta factors. Mere survival of a lower-rank reciprocity subsystem therefore does not couple that subsystem to the localization of Riemann zeros.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. The residue factorization is theorem-level prior art; the `A_4` specialization and its use as an RH-facing separability control are exact derived consequences. This is decisive against the hypothesis that a nontrivial higher-rank residue is useful merely because it retains mixed-prime data alongside a zeta divisor. It does not rule out non-polar periods or quotients, affine/imaginary-root corrections, higher-order WMDS, iterated operations that create a genuinely nonseparable object, or an independent operator/positivity mechanism acting across the factors.

## The theorem-level higher-rank residue

Let `Phi` be a finite irreducible root system other than `G_2`, let `alpha_i` be a short simple root, and let `Phi_0` be the root subsystem orthogonal to `alpha_i`. For a root

`alpha = sum_j n_j alpha_j`,

write

`s_alpha = sum_j n_j s_j`.

Diaconu–Ion–Paşol–Popa prove first at the Chinta–Gunnells local level that the residue at `x_i=1/u` equals the zeta average for `Phi_0` multiplied by rank-one `A_1` factors. Their global Gaussian-field theorem then gives, for `K=Q(i)`,

`lim_(s_i -> 1/2) (s_i-1/2) Z_Phi(s)`

`= (pi/8) Z_(Phi_0)(s)|_(s_i=1/2) product_(alpha in Phi_+, <alpha,alpha_i>=1) zeta_K^(2)(2 s_alpha)|_(s_i=1/2)`.

Here `zeta_K^(2)` is the Dedekind zeta function of `K` with the Euler factor at the prime above `2` removed. This is a meromorphic residue formula obtained from the established WMDS continuation and the Chinta–Gunnells residue theorem; it is not a formal continuation of an Euler product.

The structural point is already visible in the formula: the nontrivial residual WMDS is one multiplicative factor, while every additional factor is rank one. The authors explicitly interpret the local factors as evaluations of the rank-one `A_1` zeta average and describe the theorem as relating a higher-rank residue to the object for the orthogonal lower-rank subsystem.

## Exact `A_4` endpoint control

Take `Phi=A_4` with simple roots `alpha_j=e_j-e_(j+1)` and take the endpoint residue `i=1`. Positive roots are intervals

`alpha_a+...+alpha_b`.

With the standard simply-laced inner product, the roots orthogonal to `alpha_1` are exactly those supported on `alpha_3,alpha_4`. Thus

`Phi_0 = A_2`.

The positive roots satisfying `<alpha,alpha_1>=1` are exactly

`alpha_1+alpha_2`,

`alpha_1+alpha_2+alpha_3`,

`alpha_1+alpha_2+alpha_3+alpha_4`.

Therefore Theorem C specializes exactly to

`Res_(s_1=1/2) Z_(A_4)(s_1,s_2,s_3,s_4)`

`= (pi/8) Z_(A_2)(s_3,s_4)`

`  * zeta_K^(2)(1+2s_2)`

`  * zeta_K^(2)(1+2s_2+2s_3)`

`  * zeta_K^(2)(1+2s_2+2s_3+2s_4)`.

This is the missing higher-rank control after `PL-243`: the residue **does not scalarize completely**. It genuinely preserves the `A_2` multiple Dirichlet series, whose coefficients still carry the quadratic-character/reciprocity structure of the lower-rank WMDS.

But it preserves that object as a product factor. Fix a generic pair `(s_3,s_4)` at which `Z_(A_2)(s_3,s_4)` is finite and nonzero. The entire residual reciprocity factor is then a nonzero constant as `s_2` varies. Zeros in `s_2` contributed by any one of the displayed rank-one zeta factors occur independently of the value of the `A_2` factor; the latter supplies no equation capable of moving or localizing those zeros.

## Where the Riemann divisor sits

For the Gaussian field the standard quadratic-field factorization is

`zeta_(Q(i))(z) = zeta(z) L(z,chi_(-4))`.

Removing the ramified Euler factor at `2` gives

`zeta_K^(2)(z) = (1-2^(-z)) zeta(z) L(z,chi_(-4))`.

The nonprincipal Dirichlet `L(z,chi_(-4))` is entire, and the removed local factor is nonzero at every nontrivial Riemann zero. Hence every nontrivial zero `rho` of `zeta` is also a zero of each Gaussian Dedekind factor when its argument equals `rho`.

For example, in the first rank-one factor of the `A_4` residue the Riemann divisor appears on

`1+2s_2 = rho`,

so

`s_2=(rho-1)/2`.

At any generic fixed `(s_3,s_4)` the `A_2` reciprocity factor is unchanged as this divisor moves. The other two rank-one factors give the translated hyperplanes

`1+2s_2+2s_3=rho`,

`1+2s_2+2s_3+2s_4=rho`.

Thus the higher-rank residue can contain both a nontrivial reciprocity subsystem and the Riemann zero divisor in the same meromorphic expression while still providing no coupling between them. If `Re(rho)=1/2`, the corresponding affine hyperplanes are simply the images of the Riemann critical line under the displayed linear arguments; the root-system factorization supplies no independent positivity or self-adjointness statement forcing that real part.

## Adversarial controls

**This corrects an overstrong extrapolation of the rank-two collapse.** `PL-242`–`PL-243` showed complete loss of the varying quadratic family on all polar faces of Blomer's rank-two model. The higher-rank theorem shows that this is not the general residue pattern: a nontrivial lower-rank WMDS can survive. The valid obstruction is separability, not universal scalarization.

**Product separation is weaker than absence of arithmetic structure.** `Z_(A_2)` is genuinely arithmetic and can have its own zeros, poles, and Weyl symmetries. The claim is only that, in the theorem's residue formula, it is a multiplicative factor distinct from the rank-one Dedekind factors. At generic residual parameters where it is finite and nonzero, it cannot constrain the Riemann zeros carried by those rank-one factors.

**Exceptional parameter coincidences do not create a localization law.** At special `(s_3,s_4)` the `A_2` factor could vanish or have a pole, and divisors of different factors can intersect. Such intersections are consequences of multiplying meromorphic factors. They do not by themselves establish a source-derived relation forcing the Riemann divisor to a symmetry line. The generic fixed-parameter slice above is a matched control that removes this accidental possibility.

**The theorem's scope is finite quadratic WMDS, not every multiple Dirichlet series.** The published number-field statement is made concretely over `Q(i)`; the authors explicitly say that the precise general number-field/higher-order phenomenon is not settled there. They also note affine cases where imaginary-root correction factors enter. This finding therefore does not close affine WMDS, cubic/higher-order series, or non-polar constructions.

**The Dedekind factor is not identical to Riemann zeta.** Over `Q(i)` it also contains `L(s,chi_(-4))`, so its complete divisor is richer. It is used here only because the ordinary Riemann divisor is an unconditional factor of it; no claim is made that a statement about the full Dedekind divisor is equivalent to RH for `zeta`.

## Prior-art and novelty audit

The residue decomposition itself is direct prior art: Adrian Diaconu, Bogdan Ion, Vicenţiu Paşol, and Alexandru A. Popa, “Residues of quadratic Weyl group multiple Dirichlet series,” *Advances in Mathematics* **476** (2025), 110359, DOI `10.1016/j.aim.2025.110359`, arXiv `2307.06223`. Their Theorems A–C state the orthogonal-subsystem times rank-one-factor decomposition at local, function-field, and Gaussian number-field levels.

The exact `A_4 -> A_2` specialization above is a direct root-system calculation from their theorem and is not claimed as a new theorem. A current literature audit found the 2025 finite-root-system result itself and the separate 2025 affine `D_4^(1)` program, but no source that turns this multiplicative residue factorization into an RH localization mechanism for the ordinary Riemann factor. The line-level contribution here is therefore a **negative routing result**, not a novelty claim about WMDS residues.

## Research implication

The higher-rank escape left open by `PL-243` should no longer be phrased as “retain a nontrivial lower-rank subsystem.” Established finite quadratic WMDS already do that. The target must be stricter:

> the source-forced mixed-prime relation must remain **nonseparably coupled** to the same variable/divisor whose Riemann zeros are to be localized, or an independent operator/positivity principle must act across the residual and rank-one factors so that the arithmetic subsystem can constrain that divisor.

A direct-product coexistence `R(s') * zeta(linear form in s)` fails this test even when `R` is a rich reciprocity object. This narrows the surviving higher-rank search toward non-polar periods/quotients, affine corrections that genuinely mix variables, iterated constructions with provable cross-factor coupling, or operator realizations before the residue factorization loses that interaction.
