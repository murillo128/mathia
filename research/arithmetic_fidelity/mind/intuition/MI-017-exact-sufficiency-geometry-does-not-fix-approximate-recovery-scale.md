# MI-017 — Exact sufficiency does not fix the stable recovery scale

**Evidence level:** proved on the finite Blaschke control families through AF-175

## Core intuition

Endpoint-faithful information has several distinct layers: exact identifiability, the maximal output quotient, quantitative inversion on the admissible source class, and the asymptotic scale at which the endpoint is observed. AF-167--AF-174 show that an exactly sufficient complete representation can be singular through collisions, exponentially contract a regular source direction, or have only a sharp `1/n` worst-case inverse on unrestricted degree-`n` divisors. AF-175 supplies the positive counterpart: a uniform interpolation constant restores degree-independent local Lipschitz recovery.

Stable fidelity is therefore a property of the **representation metric + output quotient + source regularity class + endpoint normalization**, not of abstract completeness or degree alone.

## Strongest justified principle

AF-169--AF-170 remove collisions from one negative example: simple regular radial divisors at fixed radii remain macroscopically apart while their complete finite Blaschke inner factors converge in `H^infinity`. AF-171 identifies the matching positive scale through the compressed coordinate `r^n` and its boundary-layer normalization.

AF-172 extends that geometry to a complex cyclic parameter, showing that the compressed coordinate can carry orientation as well as radius. AF-173 then removes the arbitrary output phase exactly: on the cyclic stratum the quotient `H^infinity` distance is `2 rho(a,b)`. AF-174 proves a general fixed-degree divisor bound with sharp exponent `1/n`, diagnosing the cost of unrestricted multiplicity splitting and clustering.

AF-175 isolates the missing source modulus. If the reference divisor has interpolation constant bounded below independently of degree, sufficiently small quotient `H^infinity` error places exactly one target zero in each disjoint pseudohyperbolic neighborhood and gives a degree-independent locally linear inverse. The earlier fixed-radius cyclic controls lose this interpolation constant, while the compact boundary-layer family retains it.

## Counterevidence / boundary

Uniform interpolation is a strong source-class assumption, not a generic consequence of degree or pairwise separation. Multiple zeros and increasingly clustered families exit the class and legitimately fall back to weaker recovery. The boundary-layer and cyclic comparisons are special control families; they do not prescribe a universal rescaling for arbitrary divisors.

A larger output gauge than the one unimodular scalar treated by AF-173 could identify distinct divisors and would require a separate quotient audit.

## Epistemic status

**Proved on the declared finite Blaschke families; supported as a general fidelity principle.** No claim is made that every complete representation admits a useful regular source stratum.

## Falsification criterion

Produce degree-uniform recovery on the unrestricted degree-`n` class despite AF-174's sharp root-splitting controls, or exhibit a uniformly interpolating family satisfying AF-175's small-error hypotheses whose divisor distance violates its modulus. More generally, a downstream theorem that remains uniformly stable after the declared quotient while the source regularity modulus degenerates would narrow this principle.