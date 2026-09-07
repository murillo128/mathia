# MI-008 — Stable transport is relative to the destination scale and admissible source class

**Evidence level:** supported by exact asymptotic fidelity controls through AF-171 and exact Xi dictionary controls through XF-083

## Core intuition

Exact recovery and tiny forward error remain insufficient by themselves, but the recent evidence makes the correction more precise. Stability is not a single condition number attached to an abstract representation. It depends on the **destination metric and scale actually consumed** and on the **source class in which inversion is performed**.

Arithmetic Fidelity shows a complete analytic representation that collapses a regular endpoint direction at fixed interior scale yet becomes uniformly informative after passing to its natural boundary-layer coordinate. Xi Flow shows an unrestricted local surrogate class with a huge Vieta nullspace, yet the same center-local logarithmic data becomes exponentially Vieta-stable once the admissible divisor is constrained to be real. The correct bridge theorem must therefore identify both the scale and the class that remove its null directions for source-derived reasons.

## Strongest justified principle

AF-167--AF-168 separate exact finite sufficiency from collision conditioning. AF-169--AF-170 then show that collisions are not the only instability: simple regular radial divisors at fixed radii remain a fixed bottleneck distance apart while their complete finite Blaschke inner factors converge in `H^infinity`. The forward map itself contracts the radial coordinate exponentially with degree.

AF-171 identifies the exact positive scale. The inner-function distance is the pseudohyperbolic distance of `r^n` and `s^n`; on the boundary layer `u=-n log r`, this is uniformly bi-Lipschitz to the correspondingly rescaled divisor distance. Stable recovery is restored because the downstream coordinate is matched to what the representation actually retains, not because exactness changed.

Xi Flow gives the admissible-class analogue. XF-081--XF-082 construct exponentially invisible center-local perturbations, preserved under the exact periodic heat equation, that arbitrarily change a growing Vieta prefix. In the unrestricted carrier class, even dynamical compatibility does not identify the destination state. XF-083 then proves that for same-degree **real-divisor** carriers, the center-half-line logarithmic derivative is a one-sided Hardy generating function whose low power sums are exponentially stable throughout the guarded source range. The nullspace disappears after a mathematically meaningful source constraint is imposed.

Together these lines give a sharper rule: **forward fidelity is useful only after the destination quotient/scale and the admissible inverse class have been specified, and both choices must be source- or theorem-forced rather than chosen to rescue a failing representation.**

## Program consequence

For every source-to-destination bridge, declare the destination equivalence relation, norm, and asymptotic normalization; expose the exact compressed coordinate when one exists; characterize the source class on which inversion is attempted; and identify the singular/null directions outside that class. Then prove a recovery modulus on the actual asymptotic family.

A collapsing unscaled metric does not prove total information loss if the theorem consumes a canonical rescaling. Conversely, imposing an artificial narrow class merely to make inversion stable is not progress unless the source itself is known to lie there. Stability is a theorem about the whole source--representation--destination triple.

## Counterevidence / boundary

AF-171's boundary-layer rescue is family-specific, and XF-083's real-divisor stability is conditional on existence of an admissible real-rooted carrier. These examples do not imply that every ill-conditioned bridge has a canonical rescaling or source class that repairs it.

## Epistemic status

The component statements are persisted exact mathematics built from classical conditioning, pseudohyperbolic, Hardy, and harmonic-measure mechanisms. The cross-line principle is supported synthesis, not a theorem about RH.

## Falsification criterion

Produce a Mathia bridge whose declared destination metric collapses and whose inverse remains ill-conditioned on the source-forced admissible class, yet whose final theorem stays uniformly coercive without another quotient/scale theorem; or show that one of the AF-171/XF-083 stability restorations is not actually matched to its claimed destination resource. Either outcome would narrow this synthesis.