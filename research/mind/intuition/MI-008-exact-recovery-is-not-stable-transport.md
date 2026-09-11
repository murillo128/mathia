# MI-008 — Exact recovery and good local coordinates do not imply stable target transport

**Evidence level:** supported cross-line synthesis

## Core intuition

A representation can be exactly identifying, admit a perfectly conditioned local inverse, or expose the relevant source signal at a very small scale and still fail to transport the final target stably. The irreducible cost often moves to another stage: acquisition of adaptive observables, global recurrence, target projection, relative angle, or cancellation across the actual composed map.

The right question is therefore not “can the hidden state be recovered in principle?” but **what quantitative modulus survives the full map from source data to the target statistic?**

## Strongest justified principle

Arithmetic Fidelity gives an exact category/topology separation. AF-267 constructs RH-violating count-preserving zero surgeries whose full vertical logarithmic-derivative profiles approach the genuine one uniformly, eliminating a positive metric gap. AF-268 nevertheless excludes every nontrivial finite surgery from the exact Bohr almost-periodic source category. Exact membership does not provide robust separation.

Visual Exploration gives the representation version. VIS-161 shows that two exact prime phases identify every real height, but their inverse on the dense torus orbit is nowhere continuous. VIS-162 proves that the optimal Lipschitz decoder constant for any observable is exactly its worst phase-collision quotient. Set-theoretic recovery can therefore be maximally ill-conditioned.

Xi Flow shows that even bad finite-dimensional conditioning may be a coordinate artifact. XF-179 requires depth `m` to identify `m` moved atom pairs; XF-180's monomial inverse is exponentially ill-conditioned in `m`, but XF-181 constructs adapted cusp coordinates with an orthogonal Jacobian and remote-index-uniform local bi-Lipschitz control. What remains expensive is adaptive depth, support knowledge, nonlinear radius, and extraction of those observables from source/heat data.

Nyman--Beurling supplies the target-projection analogue. NB-047 localizes the Burnol-scale directional signal to a tiny deterministic prefix, while NB-048 approximates the unique target repair by a smaller-section projection with exact slack. Small source witness scale does not yet imply cheap geometric target repair.

Prime Flute closes another possible shortcut. The physical outer extension-strength factors are noncompact and infinitely heavy, so weak-trace decay cannot come from their population decay. It must be supplied by relative angle on the common heavy sectors.

## Program consequence

For every proposed compression or recovery theorem, separate four questions: what is exactly identifiable, in which topology is the inverse stable, which adaptive observables must be acquired, and how does the recovered quantity enter the final target projection/sign. A theorem at one layer should not be promoted across the next layer without an explicit modulus.

This also changes how conditioning evidence should be interpreted. A large condition number may be removable by better coordinates; a small condition number may still be irrelevant if computing those coordinates already requires the target oracle. The invariant cost is the whole source-to-target composition.

## Counterevidence / boundary

The cited lines do not imply that stable transport is impossible. XF-181 positively removes one local conditioning barrier; NB-048 provides a recursive approximation; VIS-162 gives an exact stability criterion; and Prime Flute leaves an angular route open. These advances sharpen where a successful theorem must act.

Nor is one topology universally privileged. The relevant metric or regularity class is part of the downstream mathematical claim.

## Epistemic status

**Supported cross-line separation of identifiability, conditioning, acquisition, and target transport.** Recent findings strengthen the principle by showing both directions: exact recovery can be unstable, while apparently severe local ill-conditioning can disappear after adapted preconditioning without solving the global source problem.

## Falsification criterion

In one cited setting, derive the final target theorem from exact identifiability or local conditioning alone while bypassing the identified acquisition/projection/recurrence modulus, under the same hypotheses. Alternatively, invalidate a load-bearing exact separation such as the VIS-162 collision criterion, XF-181 local isometry, or NB-048 repair identity.
