---
id: CLUE-analytic-frontier-odd-dilation-two-sided-return-and-physical-activation
type: research-clue
status: resolved
origin: master-researcher
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-143-odd-dilations-make-positive-annihilator-slack-and-span-budgets-summable.md
  - research/analytic_frontier/clues/CLUE-odd-dilated-annihilators-summable-slack.md
---

# Does the actual first-return density have a two-sided dilation law that makes finite-scale activation explicit?

## Observation

ANF-143 establishes theta_ell<=C_G*ell^(-2) for the actual first positive pressure return of an odd-dilated annihilator at each frozen stage. This is enough for its existential summable slack/span construction, because a slow physical diagonal can absorb every finite stage constant. The upper bound, however, does not by itself say how large A must be before floor(theta_ell*A) is nonzero. The same exact annihilation geometry may supply a matching lower bound and expose the physical clock of this positive construction.

The resolved odd-dilation clue owns existence of a positive-slack, linear-span cascade. This clue asks a different quantitative question and leaves that disposition unchanged.

## Research question

Freeze one admissible ANF-143 stage with pressure G<=0, finite interior nondegenerate zero maxima xi_1,...,xi_J, and its actual binomial product

Q_ell(alpha)=product_(j=1)^J (1+exp(-2*pi*i*ell*tau_j*alpha)),
 tau_j=1/(2*xi_j), ell odd.

Let theta_ell be the first strictly positive return of sup_alpha[G(alpha)+2*theta*log|Q_ell(alpha)|] to zero, with zeros of Q treated in the extended-real pressure sense. Can one prove, for every sufficiently large odd ell,

0<c_G*ell^(-2)<=theta_ell<=C_G*ell^(-2),

and express c_G,C_G and the onset in terms of explicit frozen-stage curvature, chamber, frequency and phase-return data? Can those data then give certified physical activation and source-resolution thresholds for a prescribed finite prefix of the actual cascade, rather than an unspecified 'sufficiently large A'?

## Why it may matter

A two-sided law would identify when the cheap ideal layer actually exists after integer flooring: the scale theta_ell^(-1) would be comparable to ell^2 at each frozen stage. Coupled with explicit Laplace and chamber controls, this could make the positive construction usable in finite-scale arguments and distinguish a genuine rate theorem from a non-effective diagonal existence statement. It would not by itself produce a fatal near-extremizer or improve a zero proportion.

## Decisive test

Reconstruct the exact variational formula for the first positive return as an infimum of -G(alpha)/(2*log|Q_ell(alpha)|) over |Q_ell(alpha)|>1. Prove that no point omitted from this set can create the positive return, and retain the origin and the alpha->1 boundary. Do not confuse the trivial theta=0 equality with the first positive return.

For the candidate lower bound, use the actual product rather than an arbitrary positive trigonometric polynomial. Every factor has modulus at most two. Thus |Q_ell(alpha)|>1 forces each factor to have modulus greater than 2^(1-J). The factor attached to xi_j vanishes exactly there for odd ell and obeys the elementary upper estimate

|1+exp(-2*pi*i*ell*tau_j*alpha)|
 <=2*pi*ell*tau_j*|alpha-xi_j|.

Test whether this forces alpha to stay at least c_(J,tau)/ell from every old maximum. Combine the stage's quadratic pressure loss near its maxima with a strictly negative gap elsewhere and log|Q_ell|<=J*log 2. All constants must be justified on the actual chamber decomposition, including inherited logarithmic zeros. This is a proposed proof route, not an established lower-return theorem.

For the upper bound, retain ANF-143's actual phase-orbit recurrence: a fixed q_0>1 and a correction radius L_G such that every phase starting point reaches |Q|>q_0 within distance L_G. Preserve rational dependencies among the tau_j; the orbit closure need not be the full torus. A quantitative statement conditional on a certified L_G is legitimate, but it must not be advertised as an effective unconditional cascade until those phase-return certificates are constructed for the generated stages.

At physical scale A use exactly m_(ell,A)=floor(theta_ell*A). Derive both an inactivity range from the upper return bound and a guaranteed-activation range from the lower bound, then distinguish activation from asymptotic source accuracy. A nonzero exponent is not enough: the saddle width, distances to annihilator zeros, Hessians, floor errors and the phase crest scale must be resolved. State the further inequalities on A explicitly and preserve the two-sided source normalization, not just the copy count.

For a finite prescribed depth, seek certified bounds on all retained stages without replacing actual first-return densities by freely chosen small densities. Any growing-depth law must follow from quantitative stage data; choosing larger and larger unnamed thresholds only reproduces the existing diagonal argument. In particular the implicit constants can depend badly on J, near-degenerate curvature and arithmetic relations of the shifts, so no depth-uniform rate is assumed.

Calibrate with a single old maximum and then with a genuine two-frequency stage. Approximate shifts must not be treated as exact annihilators. A useful outcome is the two-sided fixed-stage theorem plus a finite physical-scale certificate, or an admissible pressure/product example showing which additional stage hypothesis the lower bound needs. Classical almost periodicity and local quadratic optimization remain prior-art mechanisms; isolate any specialized quantitative conclusion without claiming priority from an unsuccessful literature search.

## Evidence boundary

The upper bound and the existential positive-slack construction are already supplied by ANF-143. This clue supplies neither the lower bound nor computable global stage constants, an efficient construction, a universal depth rate, or the downstream affine completion. Failure to obtain an effective rate does not refute the existing existence theorem. Check the current finding and adjacent review sidecar before using the stage assumptions; a correctness objection belongs in the normal review workflow.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-184-odd-dilation-return-has-a-sharp-ell-squared-physical-threshold.md]]

The exact first-return variational formula and the binomial product bound give the missing lower estimate `theta_ell>=c_G ell^-2`, while ANF-143 supplies the matching upper estimate. Hence `theta_ell=Theta_G(ell^-2)` at every frozen stage for sufficiently large odd `ell`. Integer flooring then makes `A~ell^2` the activation crossover, and the first-return saddle lies `Theta_G(ell^-1)` from the old skeleton and annihilator walls, so `A>>ell^2` is also the natural chamber-resolution regime for the fixed-stage Laplace source. The constants remain stage-dependent; no depth-uniform effective cascade rate or downstream near-extremizer conclusion is claimed.