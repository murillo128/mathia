# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-368 separate exact discriminator survival from finite observation, source freedom and conditioning. Global eventual Riesz-profile control can preserve principal parts, while finite prefixes and even arbitrarily tight fixed logarithmic generalized-integer counting still admit target-mixed completions.

AF-369 and AF-370 now give two complementary positive rigidity boundaries. In the integer-supported Delone Beurling class, the zero divisor remains universal but the pole residue becomes a complete binary discriminator: `Res_(s=1) zeta_Q(s)=1` iff `Q=P`. In Hamburger's ordinary-Dirichlet finite-order class, the exact completed Riemann functional equation collapses the admissible fibre to `{c zeta}`, and the normalization `a(1)=1` fixes the remaining scalar gauge. The lesson is not that residues or functional equations are intrinsically faithful. **A retained datum becomes discriminating only relative to a source category rigid enough to make its fibre target-pure.**

The live broader question is to identify other justified source-class/data couplings that are substantially weaker than full reconstruction but still preserve the exact discriminator needed downstream. Any such claim must state both the source category and the retained analytic layer; neither can be priced independently.

## Distinguish source-rich data from target-faithful positivity certificates

**Linked intuition:** `MI-002-canonical-relational-lifts-can-restore-gauge`.

AF-371 gives an exact classical separation. The full reciprocal Taylor sequence of an entire function can determine the analytic source, yet compressing it to the infinite verdict “all Hankel moment matrices are positive” is still not faithful for Laguerre--Pólya membership: Hamburger supplies false positives. Schoenberg's translation total positivity is qualitatively different because the ordered minors `det(Lambda(x_j-y_k))` characterize the Laguerre--Pólya target through the Pólya-frequency transform.

The live question is therefore not how many positivity inequalities survive, but **which relational geometry their minors test**. For an RH-sensitive positivity proposal, first identify the target property and ask whether it factors through the proposed positivity signature. When ordinary PSD/Hankel data remain target-mixed, either derive a source-specific restriction that makes that fibre target-pure or move to a stronger relational family whose target faithfulness can be proved. AF-371 does not establish that Schoenberg total positivity is minimal, so any smaller proposed family still needs its own exact false-positive or sufficiency analysis.

## Separate source identification from the RH zero-selection mechanism

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not constrain its nontrivial zeros to `Re s=1/2`. The functional equation fixes the reflection axis and, together with the source hypotheses, the analytic function; RH still requires an additional sign, positivity, unitarity, localization or equivalent zero-selecting theorem.

This distinction should be enforced in future fidelity arguments. Recovering the correct source/function is a necessary success when the destination needs that identity, but it must not be counted as progress on zero confinement unless the retained structure also supplies a theorem about the divisor.

## Couple preserved discriminators to a stably usable destination

A destination theorem must declare separately the finite data actually observed, the admissible source/tail class, the analytic layer retained, and the topology or modulus in which the conclusion is inferred. If the destination factors through a linear Hilbert target, derive its representer and Picard profile and price the inverse cost. If it uses Mellin continuation or principal parts, prove the global source-tail hypothesis that makes continuation unique and quantitatively usable. If it uses a functional equation or normalization, prove injectivity inside the actual source class rather than treating symmetry as a free label.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. The remaining bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep source class, transform fidelity, finite observation and target conditioning as different currencies

Observation horizon, admissible source category, tail class, scalar counting fidelity, smoothing order, principal-part fidelity, functional-equation rigidity, pole residue/normalization, inverse conditioning, destination topology, positivity-signature geometry and destination slack are distinct resources. AF-369--AF-370 show positively that small retained data can become complete after the admissible fibre is narrowed; AF-366--AF-368 show negatively that apparently accurate observations remain useless while the completion class is too broad; AF-371 shows that even an infinite positivity hierarchy can remain target-poor when it tests the wrong relations. Future work must keep these layers separate until a theorem explicitly connects them.
