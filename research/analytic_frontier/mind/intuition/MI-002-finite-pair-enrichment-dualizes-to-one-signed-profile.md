# MI-002 — Finite support-one pair enrichment does not escape scalarization; the honest frontier is a signed profile with normalization slack

**Evidence level:** proved for the finite affine/convex support-one classes covered by ANF-003--ANF-005

## Core intuition

Adding finitely many pair-correlation channels can look like a move from a scalar statistic to a richer joint object. In the audited common-translation and convex-moment classes, however, affine separation collapses the claimed certificate back to one signed support-one profile. The apparent extra dimension is not retained information at the final decision layer.

Allowing the profile to change sign creates a real new degree of freedom, but it is not free: universal validity on tiny zero configurations imposes an explicit normalization slack.

## Strongest justified principle

ANF-003 shows that vector features carrying one common translation character have a rank-one frequency dependence after the fixed PSD mixing is evaluated. ANF-004 shows that any affine certificate built from finitely many globally summed support-one pair observables is equivalent to a single signed support-one profile; finite convex optimization has a supporting affine witness of the same form.

ANF-005 then identifies the unavoidable price of leaving the termwise-positive class. If a universal affine certificate is written with signed pair profile `F`, its normalization parameters must satisfy a nonnegative slack condition forced already by one- and two-point configurations. At zero slack the construction falls back into the nonnegative-kernel Montgomery--Taylor boundary. Any genuine improvement must therefore beat the old ceiling **after** paying the slack.

## Evidence synthesis and boundaries

The result does not rule out infinite-dimensional families, support greater than one, matrix inequalities applied before scalarization, or genuinely higher-order correlations. It also does not solve the signed extremal problem. It says only that finite moment multiplication inside the stated support-one affine class is not an information increase.

## Status / novelty

Convex duality and supporting hyperplanes are classical. The durable content is the exact stopping rule for this analytic branch: finite pair-feature proliferation must be reduced to its single signed witness before novelty or arithmetic power is assessed.

## Falsification criterion

Produce a finite support-one construction whose final certificate cannot be represented by one affine signed pair profile under the admitted rules, or solve the signed-profile extremal problem with objective including the forced normalization slack and obtain a strict improvement.

## Lean-formalizable core

- Common-character scalarization of PSD feature mixing.
- Supporting-hyperplane reduction for finite convex moment sets.
- Tiny-configuration derivation of the normalization slack.
