# VIS-419 — fixed Wang shell translation orbit is its prime-torus Haar pushforward

## Claim

Fix one finite strict near-band Wang dyadic shell from `VIS-313`,

`F_M(T)=sum_(lambda in Lambda_M) B_lambda exp(-i lambda T)`,

where every frequency has the form

`lambda=log(q/r)`

for prime powers `q=p^k`, `r=s^l` occurring in the shell. Let `P_M` be the finite set of base primes appearing in those prime powers.

Then there is a finite Laurent polynomial `Phi_M` on the prime torus `T^(P_M)` such that

`F_M(T)=Phi_M((p^(-iT))_(p in P_M))`.

Consequently, for every fixed starting height `T_0`, every fixed finite list of offsets `u_1,...,u_d`, and every bounded continuous `Psi : R^d -> C`,

`lim_(V->infinity) (1/V) integral_0^V`
`  Psi(F_M(T_0-s+u_1),...,F_M(T_0-s+u_d)) ds`

is exactly the Haar expectation of the same observable under one independent uniform phase per **base prime**, with all ratio-mode phases kept as the induced prime characters. The limit is independent of `T_0`.

In particular, the translation-orbit control proposed by `CLUE-wang-phase-anchored-small-values` has an exact asymptotic calibration for every fixed shell. Normalized amplitude

`a_M(T)=|F_M(T)|/||F_M||_infinity`

and every fixed-radius persistence observable built continuously from finitely many samples, or from `sup_(|u|<=rho)|F_M(T+u)|`, have the same long-translation law as their prime-torus Haar pushforwards.

This does **not** show that a distinguished arithmetic height is typical. It shows that the appropriate fixed-shell self-null is mathematically canonical: long translation of the actual shell and Haar randomization of its base-prime phase point are the same limiting experiment. Independent randomization of each ratio frequency is a different, generally invalid null.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KRONECKER/BOHR SPECIALIZATION + CONTROL CALIBRATION + NO-NOVELTY-CLAIM`.

No quantitative finite-window equidistribution rate, uniform growing-shell theorem, small-value anomaly at arithmetic heights, or RH consequence is claimed.

## 1. A Wang shell is a finite character polynomial on the prime torus

For a shell frequency from an oriented pair `q=p^k`, `r=s^l`,

`exp(-iT log(q/r))`
` = p^(-ikT) s^(ilT)`.

Put

`z_p(T)=p^(-iT)`.

The corresponding mode is the torus character

`z_p^k conjugate(z_s)^l`.

Because a fixed dyadic shell contains only finitely many prime powers, only finitely many base primes and finitely many characters occur. Therefore

`Phi_M(z)=sum_(q=p^k,r=s^l in shell) B_(log(q/r)) z_p^k conjugate(z_s)^l`

is a finite continuous Laurent polynomial and

`F_M(T)=Phi_M(z(T))`.

The conjugate-pair symmetry established in `VIS-413` makes the restriction to the vertical orbit real-valued, but real-valuedness is not needed for the equidistribution argument.

## 2. Vertical translation equidistributes on the complete base-prime torus

Suppose an integer character `m=(m_p)_(p in P_M)` satisfies

`sum_p m_p log p=0`.

Exponentiating gives

`prod_p p^(m_p)=1`,

so unique factorization forces every `m_p=0`. Hence the prime-log frequency vector has no nontrivial integer relation.

The continuous orbit

`s -> (p^(is))_(p in P_M)`

is therefore Haar-equidistributed on `T^(P_M)` by the Kronecker-Weyl/Weyl-character criterion. Multiplication by the fixed phase point `(p^(-iT_0))_p` is a torus translation and preserves Haar measure, so

`s -> (p^(-i(T_0-s)))_p`

has the same limiting Haar law for every `T_0`.

For offsets `u_j`, define the fixed torus rotation

`tau(u_j)=(p^(-iu_j))_p`.

Then

`F_M(T_0-s+u_j)=Phi_M(z(T_0-s) tau(u_j))`.

The map from the base torus to the finite vector of shell values is continuous. Applying equidistribution to `Psi` composed with this map proves the claimed joint translation-orbit law.

## 3. The amplitude and fixed-radius quiet-region controls are covered

Because the vertical orbit is dense and `Phi_M` is continuous on a compact torus,

`||F_M||_infinity = max_(z in T^(P_M)) |Phi_M(z)|`.

Thus, provided the shell is nonzero, normalized amplitude is the continuous torus observable

`z -> |Phi_M(z)|/max|Phi_M|`.

For a fixed persistence radius `rho`, the continuous-time local envelope

`Q_(M,rho)(T)=sup_(|u|<=rho) |F_M(T+u)|/||F_M||_infinity`

is also a continuous function of the base torus phase. Indeed `(z,u) -> |Phi_M(z tau(u))|` is jointly continuous on the compact product `T^(P_M) x [-rho,rho]`, and taking the supremum over the compact `u` interval preserves continuity in `z`.

Therefore both `a_M(T)` and `Q_(M,rho)(T)`, and any bounded continuous function of finitely many such fixed-radius statistics, are calibrated exactly by the same Haar pushforward in the long-translation limit.

This is stronger than matching only bandwidth, coefficient magnitudes, beat gaps, or energy. The null keeps the complete shell character polynomial and changes only the global prime-torus phase origin.

## 4. What remains genuinely source-sensitive

The theorem removes the calibration ambiguity in the current clue but does not answer its source question.

For a pre-specified distinguished height `T_*`, the observed value `a_M(T_*)` may still lie unusually deep in the lower tail of the Haar/translation distribution. Likewise, a fixed-radius envelope `Q_(M,rho)(T_*)` may be unusually small. Such an effect would be a statement about where the arithmetic source places `T_*` inside the otherwise completely calibrated shell orbit.

The baseline distribution itself is independent of `T_*`. What can be exceptional is only the **source-selected phase point** represented by that height.

This separation is useful because `VIS-417` and `VIS-418` show that coarse spectral controls cannot distinguish phase anchoring. Here the exact character structure supplies the stronger matched self-null without destroying the shell's beat geometry.

## 5. Prior art and novelty boundary

The dynamical input is classical Kronecker-Weyl equidistribution on a finite torus. `VIS-071` already proves the corresponding fixed-finite prime-phase Haar law for additive within-prime harmonic fields, and `VIS-309` applies the same Bohr principle to the full Wang quadratic remainder at the level of its first two moments.

Håkan Hedenmalm, Peter Lindqvist, and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)**, *Duke Mathematical Journal* 86:1 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, use the classical prime-torus/vertical-limit correspondence and Kronecker's theorem in the Dirichlet-series setting. Andreas Defant, Domingo García, Manuel Maestre, and Pablo Sevilla-Peris, **Dirichlet Series and Holomorphic Functions in High Dimensions**, Cambridge University Press (2019), Chapter 3, develops the same Bohr prime-coordinate viewpoint.

No novelty is claimed for Kronecker-Weyl, torus characters, or Bohr vertical limits. The Mathia-specific content is the exact specialization to the mixed ratio characters of a canonical finite Wang shell and the resulting calibration of the phase-anchored small-value control left open by `VIS-418`.

## Boundaries and falsification

The result is fixed-shell and asymptotic in translation length. It gives no useful rate as `V` grows. Near-resonant integer combinations of the participating prime logarithms can make a finite translation window converge slowly.

It does not justify replacing the shell by a family whose prime support, dyadic scale `M`, bandwidth, persistence radius, or statistic grows with the arithmetic height unless a uniform quantitative equidistribution theorem is supplied.

It also does not justify independently randomizing every ratio-mode phase. The valid Haar coordinates are the base-prime phases; ratio modes are their integer characters and retain all algebraic dependencies.

A threshold indicator is not continuous at its boundary, so direct convergence of a tail probability requires the threshold to be a continuity point of the pushforward distribution, or a standard continuous approximation argument. The continuous observables stated above require no such qualification.

Falsify the result by finding a shell mode that is not an integer character of the finite base-prime torus, a nontrivial integer relation among the participating prime logarithms, or a bounded continuous finite-offset observable whose long translation average differs from its stated Haar pushforward.

## Dependencies

- `VIS-071`: finite prime vertical-flow/shared-phase Haar law.
- `VIS-309`: Bohr-time/Haar equivalence for the Wang remainder moments.
- `VIS-313`: finite dyadic Wang ratio shells.
- `VIS-413`: canonical shell real-valuedness and conjugate frequency pairing.
- `VIS-416`: bandwidth-normalized amplitude control.
- `VIS-417`: beat-scale obstruction to coarse controls.
- `VIS-418`: global-translation obstruction and phase-anchored clue.

## Research consequence

`CLUE-wang-phase-anchored-small-values` now has a canonical asymptotic fixed-shell null. For each fixed shell, the correct translation-orbit calibration can equivalently be computed on the base-prime Haar torus while preserving every ratio-frequency dependency.

The remaining experiment is narrower: pre-register a genuinely source-defined height panel and shell family, evaluate normalized amplitude and fixed-radius persistence there, and ask whether those source-selected phase points are atypical under this exact self-null. Any move to growing shells or finite translation windows must pay a separate quantitative equidistribution cost rather than treating asymptotic Haar calibration as uniform.