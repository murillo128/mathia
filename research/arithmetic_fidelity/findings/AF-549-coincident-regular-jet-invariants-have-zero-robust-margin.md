# AF-549 — Coincident regular jet invariants have zero robust margin under unrestricted calibration

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `CALIBRATION` · `JET-LIFT` · `COMPLETE-INVARIANT` · `ZERO-MARGIN` · `NO-NOVELTY-CLAIM`

## Claim

AF-548 proved that finitely many finite-order regular jets at distinct output values are pure gauge under unrestricted orientation-preserving smooth recalibration. The coincident case is genuinely different, but only on the exact collision stratum.

Let `k >= 1` and let `q_1,...,q_m` be `C^k` regular germs from `(R,0)` to an interval `I`, all with the same base value `q_i(0)=x` and all with `q_i'(0) != 0`. The orientation-preserving target pseudogroup acts diagonally by postcomposition: `q_i -> phi o q_i`, with `phi'(x) > 0`.

Choose `q_1` as reference and define the relative transition germs

`H_i = q_1^{-1} o q_i`, for `i=2,...,m`.

Then the finite jets `j^k H_i` are exact invariants of common target recalibration. Together with the discrete sign `sgn q_1'(0)`, they are a complete set of invariants for the diagonal action on common-base regular `k`-jet tuples. The collision stratum therefore carries `k(m-1)` continuous jet invariants, unlike the separated stratum of AF-548, where only discrete order/sign data survive.

These collision invariants nevertheless have zero robust margin under the unrestricted calibration class. For every nonzero base separation, however small, AF-548 restores independent programmability of the target jets at the distinct output values. Therefore no nonconstant collision-jet invariant admits a continuous invariant extension through nearby separated configurations.

Already at first order this failure is quantitative. For two coincident branches the exact invariant is the relative slope `R = q_2'(0)/q_1'(0)`. Once their base values are separated by any `epsilon > 0`, an orientation-preserving analytic recalibration can change the observed slope ratio by any prescribed fixed factor `M > 0`, even as `epsilon -> 0`. Nearness alone therefore supplies no source-independent stability modulus.

A nonzero margin appears only after additional cross-value regularity is imposed on the nuisance. If `|d/dx log phi'(x)| <= L` between two observed values `x_1,x_2`, then `exp(-L|x_2-x_1|) <= phi'(x_2)/phi'(x_1) <= exp(L|x_2-x_1|)`. The missing resource is not another finite derivative of the source branches; it is a condition that couples calibration jets across different output values.

## Complete orbit classification on the collision stratum

Because `q_1` is regular, its `k`-jet is invertible under jet composition. If `tilde q_i = phi o q_i`, then

`tilde q_1^{-1} o tilde q_i = q_1^{-1} o phi^{-1} o phi o q_i = q_1^{-1} o q_i`.

So every `j^k H_i` is invariant.

Conversely, suppose another common-base tuple `tilde q_1,...,tilde q_m` has the same relative transition `k`-jets and the same sign of the reference derivative. Define the target jet

`j^k phi = j^k tilde q_1 o (j^k q_1)^{-1}`.

Its first derivative is `tilde q_1'(0)/q_1'(0) > 0`, so it is orientation preserving. It maps the reference jet exactly, and for every `i` the equality of transition jets gives

`j^k(phi o q_i) = j^k tilde q_1 o j^k(q_1^{-1} o q_i) = j^k tilde q_i`.

Hence the relative transition jets plus one reference orientation sign classify the orbit completely.

The dimension count is consistent but is not used as proof. A common-base `m`-tuple has one base coordinate plus `m k` derivative coordinates. The target `k`-jet has one value plus `k` derivative coordinates. The continuous quotient dimension is therefore `k(m-1)`, exactly the number of coefficients carried by the `m-1` transition jets.

## First- and second-order invariants

For two branches write `v_i=q_i'(0)` and `a_i=q_i''(0)`. With `H=q_1^{-1} o q_2`, differentiating `q_1(H(t))=q_2(t)` gives

`H'(0) = v_2/v_1`

and

`H''(0) = (a_2 v_1^2 - a_1 v_2^2)/v_1^3`.

Under a target recalibration with `alpha=phi'(x)>0` and `beta=phi''(x)`, the branch jets transform as `v_i -> alpha v_i` and `a_i -> beta v_i^2 + alpha a_i`. Substitution cancels both `alpha` and `beta` exactly. Higher orders are the corresponding coefficients of the complete relative transition jet.

## Why the margin collapses immediately off the collision stratum

Let `F` be an invariant of finite `k`-jet tuples under unrestricted orientation-preserving smooth target recalibration, defined both on a collision stratum and on nearby separated tuples. Fix one separated order/sign chamber. AF-548 proves that the pseudogroup action is transitive on that chamber, so `F` is constant there.

Now take any two common-base regular jet tuples with the same branch-sign pattern but different relative transition jets. Perturb only their base values by arbitrarily small distinct offsets while leaving the derivative jets fixed. The perturbed tuples lie in the same separated order/sign chamber and converge back to the respective collision tuples.

If `F` were continuous through the collision, both collision values would have to equal the same constant from the separated chamber. Therefore every invariant that extends continuously through separated configurations is constant on the collision jet stratum.

So the nontrivial transition-jet invariants are genuine exact-stratum invariants but have no continuous invariant extension under the unrestricted nuisance. The quotient changes orbit type at coincidence: several branches are forced to sample one target jet at the collision, while any nonzero separation lets the pseudogroup choose the target jets independently.

## Explicit analytic zero-margin control

Take `q_1,epsilon(t)=t` and `q_2,epsilon(t)=epsilon+t` with `epsilon>0`. Both source slopes are `1`. Fix any `M>0`. For `M != 1`, put

`b = log(M)/epsilon`

and

`phi_epsilon,M(x) = (exp(b x)-1)/b`.

For `M=1`, take the identity. In all cases `phi' > 0`, `phi'(0)=1`, and `phi'(epsilon)=M`. Therefore postcomposition changes the observed slope ratio from `1` to `M` for every positive `epsilon`, however small.

The transformed base separation remains of order `epsilon`:

`phi(epsilon)-phi(0) = epsilon (M-1)/log(M)`.

Thus there is no modulus `omega(epsilon) -> 0` controlling distortion of the collision slope invariant from base separation alone. The analytic recalibrations achieving fixed `M != 1` have

`d/dx log phi'(x) = log(M)/epsilon`.

This identifies the exact missing hypothesis: cross-value regularity of the calibration must be controlled if near-coincidence is to approximate true coincidence.

## Quantitative regularity restores a margin

Assume instead that admissible calibrations satisfy `|d/dx log phi'(x)| <= L` on the interval joining `x_1` and `x_2`. The fundamental theorem of calculus gives

`|log(phi'(x_2)/phi'(x_1))| <= L |x_2-x_1|`.

For source slopes `v_1,v_2`, the observed ratio is

`tilde R = R phi'(x_2)/phi'(x_1)`.

Hence, with `epsilon=|x_2-x_1|`,

`exp(-L epsilon) <= |tilde R/R| <= exp(L epsilon)`.

For small `L epsilon`, the multiplicative distortion is `1+O(L epsilon)`. Higher-order transition coefficients require corresponding control of higher target-jet variation; no higher-order stability claim is made here.

## Full-profile boundary

There is one important escape not covered by the finite-jet no-go. If entire regular branch profiles are retained on overlapping ranges, then a transition map such as `q_1^{-1} o q_2` can remain well defined even when `q_1(0) != q_2(0)`. Whenever the composition exists,

`(phi o q_1)^{-1} o (phi o q_2) = q_1^{-1} o q_2`

exactly.

This does not contradict AF-548 or the zero-extension result: separated finite jets at their own base points do not determine the cross-evaluation needed to form that transition map. Retaining an overlapping profile is a genuinely more nonlocal representation than retaining any fixed finite jet at each separated branch.

Whether an arithmetic source naturally supplies overlapping profiles, recurrent value incidence, or a calibrated cross-value regularity bound is a separate source-specific question.

## Prior-art / novelty audit

No novelty is claimed for the underlying left-equivalence or differential-invariant mathematics.

- J. W. Bruce, T. Gaffney, and A. A. du Plessis, On Left Equivalence of Map Germs, Bulletin of the London Mathematical Society 16(3), 303-306 (1984), DOI `10.1112/blms/16.3.303`, is the classical target-diffeomorphism/left-equivalence setting used already by AF-548.
- Francis Valiquette, Solving Local Equivalence Problems with the Equivariant Moving Frame Method, SIGMA 9 (2013), 029, DOI `10.3842/SIGMA.2013.029`, gives the modern prolonged-pseudogroup and differential-invariant framework for local equivalence.
- Boris Kruglikov and Valentin Lychagin, Global Lie-Tresse theorem, Selecta Mathematica 22(3), 1357-1411 (2016), DOI `10.1007/s00029-015-0220-z`, is broader differential-invariant prior art for pseudogroup actions.

The complete invariant by relative transition is elementary cancellation in the regular left-equivalence problem, not a new singularity-theory theorem. The Arithmetic Fidelity contribution is the exact boundary produced by combining that collision classification with AF-548's separated transitivity and the explicit analytic family above: finite coincident jets do carry relational information, but under unrestricted calibration the information has zero robust margin as soon as the sampled target values separate.

The literature anchors above are already recorded in `research/arithmetic_fidelity/SOURCES.md`; no source-ledger change is needed.

## Boundaries and failure modes

- The classification concerns regular branch germs. Singular contact strata have additional invariants and remain outside this theorem.
- The branches are labelled. Quotienting branch permutations would add a separate discrete symmetry.
- The target nuisance is the full orientation-preserving local pseudogroup. Restricted finite-dimensional or regularity-bounded calibration families can retain more information.
- The no-extension result concerns invariants determined by finitely many finite-order jets at their own base points. Nonlocal overlapping profiles can retain transition maps.
- Exact collision may still be source-natural in a specific application. This finding says only that coincidence itself supplies no robustness to perturbations under unrestricted calibration.
- The quantitative bound controls only the first-order slope invariant. Higher-order robust recovery requires corresponding bounds on higher calibration-jet variation.
- No rational-prime discriminator is identified, and no RH consequence follows.

## Decisive audit tests

1. Verify the cancellation of the relative transition jet and the converse orbit construction.
2. Differentiate `q_1(H(t))=q_2(t)` and verify the first- and second-order invariants under common postcomposition.
3. Apply AF-548 to every nonzero base separation and check the continuity argument across the collision stratum.
4. Substitute the explicit analytic calibration and verify arbitrary fixed slope-ratio distortion at arbitrarily small separation.
5. Impose the logarithmic-derivative bound and verify the multiplicative stability estimate.

## Consequence for the research line

The coincident-branch escape is now classified. At the same output value, relative transition jets survive exactly. At any nonzero separation, all continuous finite-jet invariants disappear under unrestricted calibration. Exact shared-value incidence is therefore a singular fidelity resource, not a robust generic lift.

Adding finite jet depth does not repair the obstruction unless the source also forces a mechanism that couples calibration information across output values. The live escape routes are narrower: a restricted nuisance law, explicit calibration anchors, quantitative cross-value regularity, singular/contact structure forced by the source, or a nonlocal overlapping-profile representation. Any arithmetic application must still show that such coupling is source-natural and that the surviving transition quantity has nonzero margin in the destination seminorm.