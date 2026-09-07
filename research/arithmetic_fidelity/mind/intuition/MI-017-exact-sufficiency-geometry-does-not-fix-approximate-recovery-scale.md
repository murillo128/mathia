# MI-017 — Exact sufficiency does not fix the stable recovery scale

**Evidence level:** proved on the finite Blaschke control families through AF-177, with the local conditioning scale pinned within a universal factor two on the simple stratum

## Core intuition

Endpoint-faithful information has several distinct layers: exact identifiability, the maximal output quotient, quantitative inversion on the admissible source class, and the asymptotic scale at which the endpoint is observed. AF-167--AF-174 show that an exactly sufficient complete representation can be singular through collisions, exponentially contract a regular source direction, or have only a sharp `1/n` worst-case inverse on unrestricted degree-`n` divisors. AF-175 supplies the positive counterpart: a uniform interpolation constant restores degree-independent local Lipschitz recovery.

AF-176--AF-177 now show that this interpolation modulus is not merely sufficient. On the cyclic family and then at every finite simple Blaschke divisor, a canonical perturbation forces inverse slope `1/(2 delta(B))`, while AF-175 gives upper slope at most `1/delta(B)`. Stable fidelity is therefore controlled, up to a universal constant in these metrics, by the **representation metric + output quotient + source regularity modulus + endpoint normalization**, not by abstract completeness, simplicity, or degree alone.

## Strongest justified principle

AF-169--AF-170 remove collisions from one negative example: simple regular radial divisors at fixed radii remain macroscopically apart while their complete finite Blaschke inner factors converge in `H^infinity`. AF-171 identifies the matching positive scale through the compressed coordinate `r^n` and its boundary-layer normalization.

AF-172 extends that geometry to a complex cyclic parameter, showing that the compressed coordinate can carry orientation as well as radius. AF-173 removes the arbitrary output phase exactly: on the cyclic stratum the quotient `H^infinity` distance is `2 rho(a,b)`. AF-174 proves a general fixed-degree divisor bound with sharp exponent `1/n`, diagnosing unrestricted multiplicity splitting and clustering.

AF-175 isolates the source modulus: if the reference divisor has interpolation constant bounded below, sufficiently small quotient `H^infinity` error gives degree-independent local Lipschitz recovery. AF-176 shows on regular cyclic divisors that every local inverse estimate must pay at least `1/(2 delta)`. AF-177 then uses Frostman shifts to produce the same lower-bound direction at an arbitrary finite simple Blaschke product, yielding

`1/(2 delta(B)) <= kappa_loc(B) <= 1/delta(B)`.

The reciprocal interpolation constant is therefore an intrinsic local conditioning scale for the declared quotient and divisor metrics, up to factor two. The earlier fixed-radius controls lose it; compact boundary-layer families can retain it.

## Counterevidence / boundary

The factor-two enclosure is local and specific to the quotient `H^infinity` output metric and pseudohyperbolic divisor bottleneck metric. It does not prove that `1/(2 delta)` is the exact condition number in every perturbation direction, and multiple zeros exit the simple stratum into the Hölder regime of AF-174.

Uniform interpolation is still a strong source-class condition. The point is not that every representation has such a modulus, but that any stable inversion claim must identify its analogous nondegeneracy quantity and show that the source actually preserves it.

## Epistemic status

**Proved on the declared finite Blaschke families; supported as a general fidelity principle.** No claim is made that every complete representation admits a useful regular source stratum or a factor-two conditioning classification.

## Falsification criterion

Produce a simple finite Blaschke divisor for which the AF-177 Frostman direction fails to have local quotient/divisor ratio `1/(2 delta(B))`, or violate AF-175's local upper modulus on a uniformly interpolating family. More generally, a downstream theorem that remains uniformly stable after the declared quotient while every plausible source regularity modulus degenerates would narrow this principle.