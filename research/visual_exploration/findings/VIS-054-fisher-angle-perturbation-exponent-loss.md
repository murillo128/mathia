# VIS-054 — Fisher normalization halves the perturbation exponent of balance-return localization

## Claim

Assume the nondegenerate two-ratio Fisher configuration of `VIS-049` and the exact one-coordinate finite-gauge reduction of `VIS-050`, with `0<|kappa|<1`. Along one fixed real log-gauge direction `h`, write

`A(s)=kappa_h(s)=F(q(s))`,

where

`F(q)=kappa cosh(q/2)/sqrt(1+kappa^2 sinh(q/2)^2)`

and `q=q_h` is the class log-moment contrast. Let

`D(s)=M_P(s)-M_M(s)`

be the signed balance coordinate of `VIS-052`, so `D` and `q` have exactly the same real zeros and the same multiplicities.

Let `s_0` be an isolated balance return at which `D`, equivalently `q`, has multiplicity `m>=1`. Then the signed balance coordinate and the rendered Fisher angle have different perturbation scales.

1. There are nonzero constants `a` and `b` such that locally

   `q(s)=a(s-s_0)^m+O(|s-s_0|^(m+1))`,

   `A(s)-kappa=b(s-s_0)^(2m)+O(|s-s_0|^(2m+1))`,

   with

   `b=[kappa(1-kappa^2)/8] a^2`.

   Thus Fisher normalization doubles the contact multiplicity of every exact balance return, as in `VIS-052`, and therefore halves the exponent with which return location can be recovered from a vertically perturbed angle curve.

2. If a perturbed signed balance coordinate `D_tilde=D+E` has a zero `s_tilde` near `s_0` and `||E||_infinity<=eta`, then necessarily

   `|s_tilde-s_0|=O(eta^(1/m))`.

   For a **simple** return (`m=1`) this becomes a quantitative structural-stability statement. If on

   `I=[s_0-rho,s_0+rho]`

   one has `|D'(s)|>=gamma>0`, together with

   `||E||_infinity<gamma rho`,
   `||E'||_infinity<gamma`,

   then `D_tilde` has exactly one zero in `I` and

   `|s_tilde-s_0| <= ||E||_infinity/gamma`.

3. This linear bound converts directly into a finite class-law perturbation bound. Suppose the fixed gauge values satisfy `|a_j|<=H`, the comparison is restricted to `|s|<=S`, and

   `D(s)=sum_j c_j exp(a_j s)`,
   `D_tilde(s)=sum_j c_tilde_j exp(a_j s)`

   with

   `sum_j |c_tilde_j-c_j| <= epsilon`.

   Then

   `||D_tilde-D||_infinity <= epsilon exp(H S)`,

   `||D_tilde'-D'||_infinity <= H epsilon exp(H S)`

   on that gauge window. Hence any simple remote return satisfying the margin above survives uniquely whenever

   `epsilon exp(H S)<gamma rho`,
   `H epsilon exp(H S)<gamma`,

   and its displacement is at most

   `epsilon exp(H S)/gamma`.

4. Angle-only observation is intrinsically weaker. Let a perturbed experiment supply an angle defect

   `R_tilde(s)=A_tilde(s)-A_tilde(0)`

   satisfying

   `||R_tilde-(A-kappa)||_infinity <= delta`

   on a small neighborhood of `s_0`. If `R_tilde(s_tilde)=0`, then

   `|s_tilde-s_0|=O(delta^(1/(2m)))`.

   For a simple return this is only `O(sqrt(delta))`, even though the underlying signed balance return is linearly stable under a comparable signed-coordinate perturbation.

5. The exponent loss is sharp for angle-only sup-norm information. A constant perturbation of the angle defect with the sign of `b` produces apparent returns satisfying

   `|s_tilde-s_0| ~ (delta/|b|)^(1/(2m))`.

   No uniformly better localization exponent can therefore be recovered from the Fisher-angle curve alone without additional signed information.

6. Multiple balance roots are qualitatively less stable than simple ones. The localization exponents above remain valid for nearby roots when they exist, but arbitrary small signed perturbations can split or remove a real even-multiplicity balance root. For example, the local model `(s-s_0)^2` becomes root-free after adding a positive constant and splits into two roots after subtracting one. The corresponding Fisher-angle contact has order four and hides this signed bifurcation even more strongly.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-ROOT-PERTURBATION + REPRESENTATION CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

The result does not show that an empirical zeta/CUE residual comparison lies near the exact two-ratio locus, does not give a global perturbation theorem for changing ratio classes or support, and does not make a new general claim about root conditioning. It isolates the quantitative information loss introduced by the exact Fisher normalization used in this visual branch.

## 1. The outer Fisher map squares every balance coordinate

`VIS-050` gives the exact identity

`A(s)=F(q(s))`

with

`F(q)-kappa=[kappa(1-kappa^2)/8] q^2+O(q^4)`.

At a balance return `s_0`, `VIS-052` gives equality of the zero multiplicities of `D` and `q`. Hence for some `a!=0`,

`q(s)=a(s-s_0)^m+O(|s-s_0|^(m+1))`.

Substitution into the exact Fisher expansion yields

`A(s)-kappa
 = [kappa(1-kappa^2)/8] a^2 (s-s_0)^(2m)
   + O(|s-s_0|^(2m+1))`.

The leading coefficient is nonzero because `0<|kappa|<1`. Thus the doubled contact order is not merely a formal Taylor cancellation at the baseline: it governs the conditioning of every exact return along the one-coordinate gauge path.

There is also an exact non-asymptotic way to see the quadratic information loss. Put

`y=sinh(q/2)^2`.

Then

`A(s)^2-kappa^2
 = [kappa^2(1-kappa^2) y]/[1+kappa^2 y]`.

Since `A` and `kappa` have the same sign and `|A|>=|kappa|`, on every bounded `|q|<=Q` there are positive constants `C_Q,c_Q` depending only on `kappa,Q` such that

`c_Q q^2 <= |A-kappa| <= C_Q q^2`.

For example one may take

`c_Q = |kappa|^2(1-kappa^2)
       / [4(1+|kappa|)(1+kappa^2 sinh(Q/2)^2)]`.

Thus any vertical uncertainty in the angle becomes square-root uncertainty in the hidden signed coordinate near a balance point.

## 2. Signed simple returns are linearly stable

Assume first that `m=1` and choose an interval

`I=[s_0-rho,s_0+rho]`

on which `|D'|>=gamma>0`. Because `D'` is continuous and never vanishes on the connected interval, it has one sign throughout `I`. The mean-value theorem therefore gives

`|D(s_0+-rho)| >= gamma rho`

with opposite signs at the two endpoints.

Let `D_tilde=D+E`, with

`||E||_infinity<gamma rho`,
`||E'||_infinity<gamma`.

The first inequality preserves the opposite endpoint signs, so the intermediate value theorem gives a perturbed zero in `I`. The second inequality preserves the sign of the derivative, so `D_tilde` is strictly monotone there and the zero is unique.

At that zero,

`|D(s_tilde)|=|E(s_tilde)|<=||E||_infinity`.

Applying the mean-value theorem between `s_0` and `s_tilde` gives

`gamma |s_tilde-s_0| <= |D(s_tilde)-D(s_0)|`,

hence

`|s_tilde-s_0| <= ||E||_infinity/gamma`.

This is the elementary real-variable form of ordinary simple-root/implicit-function stability. No special property of exponential polynomials is needed beyond the availability of the signed balance coordinate.

## 3. Class-law error gives an explicit balance-error budget

The finite-support form from `VIS-052` makes the preceding bound directly auditable. If

`E(s)=sum_j (c_tilde_j-c_j) exp(a_j s)`

and `|a_j|<=H`, then for `|s|<=S`,

`|E(s)|
 <= sum_j |c_tilde_j-c_j| exp(|a_j||s|)
 <= epsilon exp(H S)`.

Differentiating gives

`|E'(s)|
 <= sum_j |a_j| |c_tilde_j-c_j| exp(|a_j||s|)
 <= H epsilon exp(H S)`.

This supplies a concrete robustness certificate for a simple **remote** balance return when the two classwise `h`-value laws are perturbed while the gauge values themselves are fixed. If `c_tilde` again comes from two probability laws, the compulsory baseline root at `s=0` remains exact because both perturbed moment sums still equal one there.

The conclusion is deliberately local. Large changes of support, class assignment, gauge values, or the reciprocal-ratio geometry may change the outer Fisher reduction itself; those changes require an additional model-error bound rather than being hidden inside `epsilon`.

## 4. Angle-only returns lose a factor two in the perturbation exponent

Now suppose only the rendered/observed angle defect is controlled. Let

`R(s)=A(s)-kappa`.

Near an isolated multiplicity-`m` return, the nonzero leading coefficient above implies that for some `c>0` and sufficiently small neighborhood,

`|R(s)| >= c |s-s_0|^(2m)`.

If the perturbed defect satisfies

`||R_tilde-R||_infinity<=delta`

and `R_tilde(s_tilde)=0`, then

`|R(s_tilde)|<=delta`,

so

`|s_tilde-s_0| <= (delta/c)^(1/(2m))`.

For the simple remote return forced in the minimal odd-budget case `V(c)=r+1` of `VIS-053`, the signed balance equation therefore gives linear displacement under a signed `C^1` perturbation, while the Fisher-angle view alone gives only square-root localization under vertical angle error.

This distinction matters because the visual angle never crosses its baseline at an exact nondegenerate balance return: the outer normalization has squared away the sign of the class imbalance. The apparent smoothness or tangency of the angle curve is therefore exactly the feature that destroys first-order return-location information.

## 5. The exponent loss is not an artifact of the proof

Write locally

`R(s)=b(s-s_0)^(2m)+o(|s-s_0|^(2m))`,

with `b!=0`. Consider the admissible angle-defect perturbation

`R_tilde(s)=R(s)-sign(b) delta`.

For sufficiently small `delta>0`, the equation `R_tilde=0` has nearby solutions whose distance from `s_0` is asymptotic to

`(delta/|b|)^(1/(2m))`.

Thus the `1/(2m)` exponent is attained by a perturbation of sup norm exactly `delta`. A method that sees only an angle curve known to that vertical accuracy cannot in general infer the underlying return location with a better power of `delta`.

By contrast, the signed local model `q(s)=a(s-s_0)^m+...` has the ordinary `eta^(1/m)` root scale. The Fisher normalization has therefore not merely made the plotted contact visually flatter; it has quantitatively halved the root-localization exponent available from the scalar display.

## 6. Prior art and novelty boundary

Simple-root stability, multiple-root ill-conditioning, and fractional-power root displacement under perturbation are classical numerical-analysis and implicit-function phenomena. A canonical historical source for polynomial root conditioning is J. H. Wilkinson, **The evaluation of the zeros of ill-conditioned polynomials. Part I**, *Numerische Mathematik* 1 (1959), 150–166, DOI `10.1007/BF01386381`. Wilkinson's work is much broader than the elementary local argument needed here and already makes clear that multiple roots are fundamentally ill-conditioned under coefficient perturbation.

The real-variable simple-root estimate above is proved directly from monotonicity, the intermediate value theorem, and the mean-value theorem; the `eta^(1/m)` and `delta^(1/(2m))` scales follow from the displayed local normal forms. No novelty is claimed for root perturbation theory, implicit-function stability, or multiple-root sensitivity.

The durable Mathia contribution is only the specialization to the exact Fisher-gauge representation classified in `VIS-048`–`VIS-053`: the balance coordinate can remain linearly informative while the normalized visual statistic necessarily loses the sign and degrades the observable perturbation exponent by a factor of two.

## 7. Boundary conditions and falsification

All exact identities inherited from `VIS-050` remain conditional on the finite fixed support, fixed residual tensors, nondegenerate reciprocal two-ratio geometry, fixed real gauge direction, and `0<|kappa|<1`. The coefficient-law corollary additionally keeps the distinct gauge values `a_j` fixed and compares their signed class masses on a bounded gauge window.

The simple-root existence/uniqueness statement requires both the derivative margin and the `C^1` perturbation bound. A sup-norm bound alone can create oscillatory extra roots even when the function values are close. For `m>1`, this finding gives local displacement scales for nearby roots but **does not** assert persistence of the number of real roots.

The angle-only statement concerns error in the angle **defect relative to the perturbed experiment's own baseline**. This avoids confusing a baseline calibration shift with return-location error. An approximate two-ratio empirical model must separately bound how far its actual angle defect is from the exact `F(q)-kappa` model before the square-root localization statement can be used quantitatively.

Falsify the result by producing a valid `VIS-050` configuration whose balance root has multiplicity `m` but whose Fisher-angle defect has a different local order; by violating the simple-root displacement bound under the stated derivative and `C^1` margins; by finding a fixed-support class-law perturbation whose `D` or `D'` error exceeds the elementary exponential bounds above; or by constructing angle-defect perturbations of size `delta` for which an apparent nearby return escapes every `O(delta^(1/(2m)))` neighborhood.

## Research consequence

The quantitative-stability question left open by `VIS-053` should be attacked in the **signed balance coordinate before the Fisher angle**. For exact two-ratio geometry, a simple remote return comes with an explicit derivative margin `gamma`; perturbations of the classwise value laws can then be converted into a linear location-error certificate through their `L^1` coefficient error.

If only the Fisher angle is retained, the same return is inherently less identifiable: vertical angle error produces square-root location uncertainty even in the simple case, and higher-order balance returns are worse. Therefore a visually stable Fisher tangency should not be promoted as arithmetic robustness unless the analysis also preserves a signed source-sensitive coordinate or proves an independent model-error bound strong enough to overcome this exponent loss.

The next independent question is no longer another exact return-count identity. It is whether a frozen empirical zeta/CUE residual construction admits a source-sensitive signed coordinate whose deviation from the ideal `D` or `q` can be bounded under the actual sampling, binning, closure, and ratio-class errors.