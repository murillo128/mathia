# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros.

The live broader question is to identify justified source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator. Every proposal must state both the source category and the retained analytic layer.

## Distinguish gauge elimination from a target-faithful positivity certificate

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`.

AF-371 separates source richness from target-faithful positivity: complete reciprocal Taylor data may determine the source while Hankel PSD remains target-mixed, whereas Schoenberg translation total positivity uses the correct ordered relation. AF-372 shows that no fixed determinant order is enough on the unrestricted translation-kernel class. AF-373 then shows that location sampling is an independent resource: on an exponentially decaying class some thin sets are determining, while the integer lattice is not.

AF-374 identifies the fixed-lattice multiplicative quotient. AF-375 classifies its entire continuous separable gauge by the difference subgroup `H_E=<E-E>`. If `H_E=aZ`, exponential tilts times positive periodic factors remain invisible; if `H_E` is dense, only the universal exponential tilt survives. An incommensurate second lattice phase therefore kills every nonconstant periodic separable gauge.

AF-376 closes the obvious finite-phase repair on Ganzburg's broad class `L`. If the actual row set is uniformly discrete with separation `Delta_E>0`, any bounded nonnegative kernel supported in an interval shorter than `Delta_E` is `E`-Pólya-frequency at every order, while no nonzero compactly supported integrable kernel is globally Pólya-frequency. Thus `E=aZ union (tau+aZ)` with irrational `tau/a` can have dense generated difference subgroup and still retain an infinite-dimensional non-separable false-positive fibre because the **actual sampled rows** remain separated.

AF-377 removes the converse shortcut. Vanishing minimum spacing is not enough either. For a compact/local source of support width `w`, form the support-interaction graph `G_w(E)` joining sampled rows whose translates can interact. If every connected component has size at most `r`, every sampled Toeplitz determinant factorizes into blocks of order at most `r`; any compactly supported `PF_r` kernel that is not globally PF is then an all-order sampled false positive. The explicit shrinking-pair construction has `inf |u-v|=0` but interaction components of size two, so a `PF_2` non-`PF_3` kernel already defeats the nominal all-order certificate.

AF-378 closes the coordinate-only repair. An order isomorphism preserves all sampled determinant values when the kernel is transported with it, so the false-positive fibre survives even if the new coordinate picture has arbitrarily small gaps. For the full translation-kernel class, a common reparameterization preserves difference geometry exactly only when it is positive affine. Reimposing a fresh translation kernel after a nonlinear change is therefore a new source model, not evidence that the old observation became determining.

The live question is no longer whether more finite lattice phases remove the known gauge, whether the sampling set merely has points arbitrarily close together, or whether nonlinear coordinates can manufacture such spacing. A successful sampled positivity reduction must prove genuinely unbounded **intrinsic** support-scale interaction complexity together with a determining theorem, or derive a source-specific class rigid enough to exclude compact/local aliases. Dense `H_E`, vanishing displayed spacing, nominally unbounded determinant order and nonlinear coordinate densification are each insufficient by themselves.

## Separate source identification from the RH zero-selection mechanism

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Couple preserved discriminators to a stably usable destination

A destination theorem must declare separately the finite data observed, the admissible source/tail class, retained analytic layer, relation type and arity, intrinsic versus displayed sampling geometry, generated difference subgroup, residual gauge, and topology/modulus in which the conclusion is inferred. Exact injectivity without usable conditioning, or gauge elimination without a determining theorem, is not a destination result.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

The RH root-rate endpoint tolerates large output error but is highly sensitive to breaking its binomial cancellation orbit upstream. A viable bridge must assemble the required cancellation coherently before taking the root-rate quotient; ordinary prefix accuracy is the wrong resource.

## Replace the conditional Schanuel codimension budget by an unconditional joint-dependence obstruction

**Linked intuitions:** `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density` through `MI-040-unitary-zero-incidence-spends-two-algebraic-codimensions`.

AF-320--AF-336 separate exact recovery, conditioning, support-union geometry and exact incidence. The unconditional target remains to rule out the required independent polynomial relations on the common prime-phase tuple without Schanuel, or find another prime-source theorem strong enough to exclude the middle-singular fibre.

## Keep fidelity currencies separate until a theorem connects them

Observation horizon, admissible source category, tail class, transform fidelity, inverse conditioning, positivity relation, nominal relational arity, **intrinsic support-scale interaction-component size**, displayed coordinate geometry, source-category covariance under reparameterization, generated difference subgroup, residual observation gauge and destination slack are distinct resources. AF-375 makes the separable gauge currency exact; AF-376 makes positive row separation an independent obstruction; AF-377 shows that even zero minimum spacing can leave the effective interaction arity uniformly bounded; AF-378 shows that coordinate densification is not a new resource when the source experiment is transported faithfully. Future work should state which fibre has actually been removed, which source category is being preserved, and which target-changing fibres remain.
