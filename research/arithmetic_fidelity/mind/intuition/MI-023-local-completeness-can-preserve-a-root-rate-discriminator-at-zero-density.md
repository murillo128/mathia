# MI-023 — Sparse root-rate observability is an affine shrinking-target problem

**Evidence level:** exact finite-mode classifications, transcendental counterexamples, Haar/Hausdorff genericity, and affine fiber-collapse reduction through AF-253

## Core intuition

Sparse output sampling preserves a finite-exponential root-rate discriminator according to the exponential rate at which the relevant phase dynamics approach the cancellation geometry. Density and periodic completeness are only proxies in special classes. After affine source constraints are admitted, the correct object is not merely a point orbit approaching one scalar zero set: it is the decay of the entire restricted fiber polynomial along the quotient orbit.

This separates ordinary lower-dimensional phase relations from genuinely destructive source locking. Homogeneous relations and nondegenerate affine motion leave bad phases thin; a positive-measure failure requires exponential collapse of the whole fiber coefficient vector.

## Strongest justified principle

AF-244--AF-250 establish the finite-mode shrinking-target criterion, the algebraic periodic-completeness special case, transcendental counterexamples, and Haar-generic faithfulness. AF-251 sharpens the exceptional set to Hausdorff codimension at least one, and the same bound holds intrinsically on every connected homogeneous subtorus on which the mode is nonzero.

AF-252 classifies torsion affine cosets. The orbit visits finitely many components: if one entire component lies in the cancellation variety, every starting point suffers periodic exact collapse; otherwise the bad set retains codimension at least one. AF-253 gives the general affine criterion. If `R_n(P,C)` is the `L^2` norm of the restricted fiber polynomial, then positive exponential decay exponent `chi(P,C)` forces cancellation for every point of `C`, while `chi=0` makes exponential cancellation Haar-null. Parseval rewrites `R_n` as the norm of a finite vector trigonometric polynomial on the quotient, so `chi>0` is exactly exponential recurrence of the quotient orbit to its simultaneous coefficient-annihilator set.

## Program consequence

Treat the actual zeta/Li phase relations as a quotient-dynamical Diophantine problem. Determine the affine phase locus forced by the source and prove that the corresponding fiber norm decays only subexponentially, uniformly enough as the relevant finite mode family grows. Exact integer relations alone are no longer a plausible explanation for generic loss; a dangerous relation must force exponential approach to a simultaneous coefficient kernel or an exact periodically visited collapsed component.

Keep source cost separate: output faithfulness does not make the retained Li coefficients cheaper to construct.

## Counterevidence / boundary

All current results are finite-mode and mostly measure/dimension statements. A distinguished arithmetic point can lie in a Hausdorff-null set, so genericity does not establish the zeta case. AF-253 gives a zero-one Haar boundary, not a quantitative theorem for the actual quotient orbit, and uniformity as the mode family grows remains open.

Affine constraints outside the finite-dimensional toral model or source relations coupling the sampling set to the coefficients may introduce additional structure.

## Epistemic status

**Exact finite-mode reduction of sparse root-rate failure to exponential shrinking-target recurrence, sharpened for arbitrary affine phase constraints by the fiber-collapse exponent; source-specific control of the zeta/Li quotient orbit remains open.**

## Falsification criterion

Exhibit an actual finite zeta/Li affine phase family with positive fiber-collapse exponent, or produce an affine coset with `chi=0` on which exponential cancellation has positive Haar measure contrary to AF-253.
