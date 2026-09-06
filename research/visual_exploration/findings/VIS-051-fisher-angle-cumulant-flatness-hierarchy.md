# VIS-051 — two-ratio Fisher gauge flatness is exactly a class-cumulant hierarchy

## Claim

Assume the nondegenerate two-ratio Fisher configuration of `VIS-049` and the one-coordinate finite-gauge reduction of `VIS-050`. Thus `0<|kappa|<1`, the active cells split into reciprocal ratio classes `P,M`, and for a fixed real cell function `h` the gauge path

`G_x(s)=H_x exp(-s h_x)/Z(s)`

has Fisher cosine

`kappa_h(s)=F(q_h(s))`,

where

`F(q)=kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)`

and

`q_h(s)=log E_(pi_P)[exp(s h)]-log E_(pi_M)[exp(s h)]`.

Here

`pi_P(x)=v_x^2/p` on `P`,
`pi_M(x)=v_x^2/m` on `M`

are the normalized classwise `v^2` weights from `VIS-050`.

Let `c_j(P)` and `c_j(M)` denote the `j`th cumulants of the finite weighted distributions of the scalar values `h_x` under `pi_P` and `pi_M`, and write

`Delta_j=c_j(P)-c_j(M)`.

Then the full higher-order flatness along the fixed gauge direction `h` is classified exactly as follows.

If

`r=min{j>=1: Delta_j != 0}`

exists, then

`kappa_h(s)-kappa
 = [kappa(1-kappa^2)/(8(r!)^2)] Delta_r^2 s^(2r)
   + O(s^(2r+1))`.

Consequently every derivative through order `2r-1` vanishes, while

`kappa_h^(2r)(0)
 = [(2r)!/(8(r!)^2)] kappa(1-kappa^2) Delta_r^2`

is nonzero. The first detectable change in the Fisher cosine occurs at **twice the order of the first unmatched class cumulant**.

If no such `r` exists, then the two finite weighted distributions of `h` are identical. Equivalently,

`q_h(s)=0`

for every real `s`, and hence

`kappa_h(s)=kappa`

exactly along the entire positive gauge path. Thus a nonconstant gauge direction can preserve the angle exactly when its `h`-value distribution is the same in the two ratio classes, even though `VIS-048` rules out exact invariance on an open neighborhood of arbitrary gauges.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + CUMULANT/FINITE-GAUGE CLASSIFICATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that empirical zeta/CUE residuals satisfy the two-ratio hypothesis, that high-order flatness is common, or that the underlying cumulant/MGF uniqueness facts are new.

## 1. The gauge coordinate is a difference of cumulant generators

For the two classwise probability laws induced by `h`, define

`M_P(s)=E_(pi_P)[exp(s h)]`,
`M_M(s)=E_(pi_M)[exp(s h)]`.

Because the support is finite, both moment-generating functions are finite and real-analytic for every real `s`. Their logarithms are therefore analytic near `s=0`, and

`q_h(s)=log M_P(s)-log M_M(s)`.

By the standard definition of cumulants through derivatives of the log moment-generating function,

`q_h(s)=sum_(j>=1) Delta_j s^j/j!`

in a neighborhood of zero.

If the first nonzero cumulant difference is `Delta_r`, then

`q_h(s)=Delta_r s^r/r!+O(s^(r+1))`.

This converts the vague question “how flat is the Fisher angle under this gauge perturbation?” into a precise comparison of the two classwise scalar distributions seen by the perturbation.

## 2. The angle response squares the first unmatched cumulant

The exact outer function from `VIS-050` is even in `q`. Expanding at the balanced point gives

`F(q)=kappa+[kappa(1-kappa^2)/8]q^2+O(q^4)`.

Substituting the first nonzero term of `q_h(s)` yields

`F(q_h(s))-kappa
 = [kappa(1-kappa^2)/8]
   [Delta_r^2/(r!)^2] s^(2r)
   + O(s^(2r+1))`.

The `O(q^4)` term starts only at order `4r`; the `O(s^(2r+1))` remainder comes from the next term in `q_h(s)^2`. Hence no lower-order contribution has been omitted.

This immediately gives the displayed `2r`th derivative. Since `0<|kappa|<1` and `Delta_r != 0`, it cannot vanish.

Three simple cases show the hierarchy:

- if the class means differ (`Delta_1 != 0`), the Fisher cosine moves first at order `s^2`, reproducing the rank-one Hessian of `VIS-050`;
- if the means agree but the class variances differ (`Delta_1=0`, `Delta_2 != 0`), the cosine is flat through cubic order and first moves at order `s^4`;
- if mean and variance agree but the third cumulants differ, the first response is order `s^6`.

Thus a high-order flat numerical response can be forced by low-order moment matching between the two ratio classes without providing any new gauge invariant.

## 3. Exact invariance along one direction is distribution matching

`VIS-050` proves that exact angle preservation along the fixed path is equivalent to

`q_h(s)=0`.

If the weighted `h`-distributions under `pi_P` and `pi_M` are identical, their moment-generating functions agree, so `q_h(s)=0` for all real `s` and the Fisher cosine is exactly constant.

Conversely, if `kappa_h(s)=kappa` for all `s` in any open interval around zero, `VIS-050` forces `q_h(s)=0` there. Therefore `M_P(s)=M_M(s)` on that interval. The classical uniqueness theorem for moment-generating functions then gives equality of the two probability laws. In the present finite-support setting this can also be seen elementarily: the MGFs are finite sums of exponentials, and equality on an interval forces equality of the aggregate weights at every distinct `h` value.

The same conclusion follows if all cumulants agree. Then every derivative of `q_h` at zero vanishes; analyticity gives `q_h=0` near zero, hence equality of the MGFs and of the finite weighted distributions.

This is compatible with `VIS-048`. Exact constancy along one specially balanced one-dimensional path is not constancy on an open set of all positive gauges. The two-ratio geometry can contain many such balanced directions while remaining globally gauge-dependent.

## 4. Prior art and novelty boundary

Moment-generating functions, cumulant-generating functions, and their uniqueness properties are classical probability theory. A direct classical anchor is J. H. Curtiss, **A Note on the Theory of Moment Generating Functions**, *The Annals of Mathematical Statistics* 13:4 (1942), 430–433, DOI `10.1214/aoms/1177731541`, which underlies the standard uniqueness theorem used above. Modern probability texts likewise define cumulants as derivatives of the log MGF and use equality of an MGF on a neighborhood of zero to identify the law.

A targeted search for weighted-cosine perturbation, diagonal metric reweighting, cosine gauge freedom, and cumulant-generating-function angle expansions found the neighboring weighted-angle/gauge literature already bounded in `VIS-045`--`VIS-050`, but no source needed for the present argument beyond those classical ingredients. No novelty is claimed for the cumulant expansion or MGF uniqueness.

The durable Mathia contribution is the representation-control consequence obtained by composing those standard facts with the exact one-coordinate Fisher reduction of `VIS-050`: **the apparent order of gauge robustness is not a free geometric property; it is exactly determined by how many class cumulants the chosen perturbation fails to distinguish, and the angle doubles that first distinguishing order.**

## 5. Boundary conditions and falsification

The finite support, positive baseline gauge, residual tensors, reciprocal ratio partition, and class weights from `VIS-050` must remain fixed. Rebinning cells, moving cells between `P` and `M`, refitting residual tensors, recomputing a Markov closure, or changing support while `s` varies is outside the claim.

The result concerns one fixed real perturbation field `h`. Exact invariance for that field does not imply invariance for nearby or arbitrary fields. Conversely, a nonconstant `h` is allowed to be exactly invisible if its weighted value distribution agrees between the two ratio classes.

The finite-support assumption removes moment-indeterminacy issues: both class MGFs exist everywhere and their equality determines the weighted value distribution. The statement should not be transferred unchanged to infinite-support perturbation laws without restoring the appropriate existence/uniqueness hypotheses.

Falsify the claim by giving a valid `VIS-050` two-ratio configuration and a fixed `h` for which the first unmatched class cumulant has order `r` but the Fisher cosine changes at an order different from `2r`; by finding all class cumulants equal while the finite weighted `h`-distributions differ; or by producing exact angle preservation along the path with unequal class MGFs.

## Research consequence

The exceptional first-order-flat family is now fully classified along each fixed positive gauge direction. A small gradient, Hessian, or even several vanishing higher derivatives can be manufactured by matching progressively more low-order class cumulants. Such flatness is therefore a **representation diagnostic**, not evidence that a residual orientation carries arithmetic information.

For empirical residual work, sensitivity tests should not stop after a numerically tiny first or second derivative. If a pair is near the two-ratio locus, compare the classwise distribution of the proposed log-gauge perturbation itself. Exact distribution matching identifies a genuinely invisible direction; the first cumulant mismatch predicts the order at which a local finite-difference test can begin to respond.

This closes the higher-cumulant flatness hierarchy left open by `VIS-050`. Applying the criterion to a frozen empirical zeta/CUE residual table is a separate question because it requires a predeclared primary gauge, a concrete perturbation family, and sampling-error controls rather than further exact finite-gauge algebra.