# Weil-inertia research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Keep optimization loss separate from information loss

**Linked intuitions:** `MI-002-global-fenchel-dual-separates-losses`.

Global Fenchel coupling can remove artificial blockwise optimization loss, but no optimizer can reconstruct a discriminator already erased by the represented Gram/pressure data. Continue to audit the exact represented object before strengthening inequalities on it.

## Treat screening as an information-bandwidth obstruction

**Linked intuitions:** `MI-001-screening-is-an-information-bandwidth-obstruction`.

When the represented test family cannot resolve the coordinates needed by an off-line witness, sharper optimization of the same screened object cannot recover them. A decisive advance must enlarge the source-faithful information channel or prove that the existing channel already determines the missing witness variable.

## Work inside the exact finite-window alias quotient, but move beyond pairwise residual rank

**Linked intuitions:** `MI-003-coupled-welding-uniformity-is-the-fourth-moment-gate` and `MI-004-w-conditioning-is-l2-compressible-but-l1-expensive`.

The scalar finite-window representation is exactly `N`-dimensional in divisor/tail coordinates. The residual pairwise branch is now closed much further than a rank ceiling: WI-094 proves positive-density defect edges contribute only `O(1/log P)` of dyadic diagonal Frobenius energy even with adversarial signs; WI-095--WI-096 identify defect as low-denominator free-cycle resonance and give the exact cycle-count formula; WI-099 makes each pair phase-pure with one common rotation resonance. WI-097--WI-098 show the sharp Loewner mechanism is cyclotomic and extends to coprime composite moduli.

The surviving fourth-moment route must therefore use information that pairwise residual rank cannot supply: actual centered source coefficients across many weak/full-rank blocks, cross-scale coupling, a source-specific restriction inside the exact alias quotient, a direct non-Cartesian incidence estimate, or a genuinely non-scalar object formed before Ramanujan reduction.

A decisive result is a source-specific many-body theorem in one of those retained structures. Generic pairwise rank saving, low-denominator resonance, or positive-density defect aggregation is no longer a distinct escape route.
