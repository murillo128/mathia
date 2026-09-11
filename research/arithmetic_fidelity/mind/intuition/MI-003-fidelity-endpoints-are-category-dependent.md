# MI-003 — Exact source-category membership and metric fidelity are different mathematical claims

**Evidence level:** supported by exact counterseparations

## Core intuition

There is no single numerical notion of “how much information survives” that can be moved freely among smooth, stochastic, formal, supportwise, and analytic-source settings. Several natural fidelity tests agree at one endpoint and diverge sharply at another. The category of the claim is therefore part of the claim itself.

The newest arithmetic example makes the distinction especially sharp. A source can be arbitrarily close to the genuine zeta logarithmic derivative in a strong vertical sup metric while still lying outside the exact Bohr/Dirichlet source category. Conversely, exact membership in that category is a rigid algebraic-analytic fact but supplies no positive metric margin against nearby signed controls.

## Strongest justified principle

AF-007 measures smooth local loss by vertical differential rank. It gives a sharp first-order lower bound on the dimension of a smooth lift but cannot see disconnected fibers. AF-010 gives the jet analogue: all finite jets may factor while a smooth flat germ still carries hidden variation, so full-jet recovery needs a quasianalytic or analytic category plus the relevant closure theorem.

AF-009 and AF-011 separate probabilistic endpoints. Conditional variance is the exact `L2` prediction defect and may tend to zero under increasingly informative observations. Zero-error recovery is instead a support-confusability statement: one discordant overlap is fatal even if its probability is tiny.

AF-266--AF-268 add the vertical zeta-source separation. Pure off-critical insertion is uniformly detectable on a full vertical line to the right of one by the logarithmic derivative, but count-preserving signed surgery destroys every positive uniform gap while remaining RH-violating. Nevertheless every nontrivial finite surgery leaves the exact Bohr almost-periodic class because its logarithmic-derivative defect is a nonzero `C_0(R)` function, and `AP(R) intersect C_0(R)={0}`. The distance of those controls back to `AP(R)` can still tend to zero.

Thus **exact category exclusion does not imply robust separation, and robust separation for one control family does not survive a more balanced control family**. A fidelity theorem must say whether it needs an exact membership test, a quantitative modulus, average risk, support separation, or finite/infinite-order regularity.

## Synthesis of evidence

The zeta application suggests a useful two-stage discipline. First identify the exact source category consumed by the intended theorem. Then ask for the quantitative topology in which the downstream operation is stable. Treating the first as a substitute for the second leads to brittle proofs; treating the second as a substitute for the first can miss exact source laws that survive arbitrarily small perturbations.

For the current arithmetic-fidelity frontier, Bohr almost periodicity is therefore a real categorical discriminator for finite zero surgery, but not yet a robust RH certificate. The next advance must either extend exact source-category rigidity to a substantially larger RH-violating control class or identify a quantitative source modulus that cannot be driven to zero by count-preserving surgery.

## Counterevidence / boundary cases

AF-268 treats nontrivial **finite** divisor surgery. It does not prove that every infinite zero rearrangement violating RH leaves the almost-periodic/Dirichlet category, nor that exact almost periodicity by itself characterizes zeta among entire functions with the same symmetries.

AF-267 shows why one must not infer a positive distance from categorical exclusion: the finite-surgery controls can approach the genuine vertical profile uniformly. Likewise the earlier differential, jet, stochastic, and supportwise separations remain category-specific rather than one universal no-go.

## Epistemic status

**Supported category-versus-topology boundary:** exact analytic-source membership can exclude every member of a finite RH-violating surgery class even though that class has no positive metric separation from the genuine source. The missing theorem must specify which of those two currencies the downstream RH argument actually needs.

## Novelty/prior-art status

The individual fidelity criteria, Bohr almost-periodic facts, and finite-surgery calculations retain their finding-level prior-art status. This note is a synthesis of their role in the current line.

## Falsification criterion

Construct a nontrivial finite zero surgery satisfying the AF-268 hypotheses whose vertical logarithmic derivative remains Bohr almost periodic, or derive a uniform positive vertical-distance gap for the count-preserving AF-267 controls. Strategically, exhibit an RH-violating infinite/source-preserving control inside the same exact Dirichlet category; that would show the present category gate is too weak and sharpen the required source law.

## Lean-formalizable core

- Vertical-rank lower bounds for smooth lifts.
- Conditional-variance and support-confusability separations.
- The finite-dimensional algebraic part of the finite-surgery cancellation estimates.
