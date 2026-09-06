# VIS-063 — a frozen quadratic Markov-residual witness has dimension-free whole-replicate calibration

## Claim

Fix one finite three-gap representation on a declared alphabet `X x Y x Z`. For any probability law `P` on that alphabet define the **denominator-free Markov residual tensor**

`C(P)_(ijk) = P_Y(j) P_(ijk) - P_XY(i,j) P_YZ(j,k)`.

Whenever `P_Y(j)>0`, the adjacent-pair-preserving Markov residual `Delta(P)` of `VIS-057` satisfies

`C(P)_(ijk) = P_Y(j) Delta(P)_(ijk)`.

Thus `C` records the same conditional-independence defect fiberwise, but without dividing by a possibly small middle-state mass.

Now freeze a real weight tensor `w` on the declared support with

`||w||_infty <= 1`,

and define the scalar quadratic witness

`tau_w(P) = sum_(i,j,k) w_(ijk) C(P)_(ijk)`.

Let `X_1,...,X_B` be independent identically distributed random probability tables produced by complete control replicates, with

`E[X_b]=P`.

Each `X_b` may contain arbitrary dependence internally. In the intended finite-size CUE application, one `X_b` may be the empirical three-gap table formed from all eligible overlapping triples inside one independently generated control matrix.

For two probability tables `x,y`, define the symmetric cross-replicate kernel

`h_w(x,y)`
` = (1/2) sum_(i,j,k) w_(ijk) [`
`     x_Y(j) y_(ijk) + y_Y(j) x_(ijk)`
`     - x_XY(i,j) y_YZ(j,k) - y_XY(i,j) x_YZ(j,k)]`.

Then

`E[h_w(X_1,X_2)] = tau_w(P)`

and, solely from `||w||_infty<=1` and simplex geometry,

`|h_w(x,y)| <= 2`.

Put `m=floor(B/2)` and assume `B>=2`. Pair independent control replicates disjointly and form

`T_hat_w = (1/m) sum_(r=1)^m h_w(X_(2r-1), X_(2r))`.

Then `T_hat_w` is unbiased for `tau_w(P)`, and Hoeffding's bounded-variable inequality gives, for every `0<rho<1`,

`Pr(|T_hat_w-tau_w(P)| <= r_B(rho)) >= 1-rho`,

where the safe radius is

`r_B(rho) = min(4, sqrt(8 log(2/rho)/m))`.

The radius contains **no support-size factor `K` and no Fisher-reference floor `h_min`**.

Consequently, for any frozen zeta table `Z` on the same declared representation,

`| [tau_w(Z)-tau_w(P)] - [tau_w(Z)-T_hat_w] | <= r_B(rho)`

on the same control-only event. In particular,

`|tau_w(Z)-T_hat_w| > r_B(rho)`

certifies that the frozen zeta table and the control population differ in this predeclared quadratic Markov-residual contrast, with probability at least `1-rho` over the independent control replicates only.

**Evidence/status:** `EXACT-DERIVED + CONTROL-CONCENTRATION INTERFACE + LOWER-DIMENSIONAL REPRESENTATION CONTROL + CLASSICAL HOEFFDING/U-STATISTIC PRIOR ART + NO-NOVELTY-CLAIM`.

This does not contradict `VIS-062`. That finding rules out eliminating the `sqrt(K/B)` scale while retaining distribution-free **full-law `L^1` control** over arbitrary simplex-valued replicates. The present result deliberately gives up omnidirectional full-law coverage and estimates one frozen scalar quadratic contrast instead.

## 1. The polynomial residual removes the middle-state denominator

Recall from `VIS-057` that, on a positive middle state,

`Delta(P)_(ijk)`
` = P_(ijk) - P_XY(i,j) P_YZ(j,k)/P_Y(j)`.

Multiplying by `P_Y(j)` gives exactly

`P_Y(j) Delta(P)_(ijk)`
` = P_Y(j)P_(ijk) - P_XY(i,j)P_YZ(j,k)`
` = C(P)_(ijk)`.

If `P_Y(j)=0`, every cell and both adjacent marginals on that middle-state fiber are zero, so `C(P)` vanishes there automatically. Hence `C` is a denominator-free version of the same conditional-independence obstruction, with zero-mass middle fibers contributing nothing.

This changes the error geometry rather than merely tightening a constant. `VIS-057` first controls the full raw law in `L^1` and then propagates that ball through a nonlinear Markov completion and a Fisher norm. Here the target itself is a polynomial scalar functional of the population law, so it can be estimated directly without first reconstructing the complete population table to `L^1` accuracy.

For later comparison it is also useful that

`||C(Z)-C(P)||_1`
` = sup_(||w||_infty<=1) |tau_w(Z)-tau_w(P)|`.

Thus a single frozen `w` is one dual direction of the full denominator-free residual difference. Recovering the whole `L^1` norm would require optimizing over all such directions and would reintroduce the complexity that this one-witness certificate intentionally avoids.

## 2. Cross-replicate multiplication is unbiased for the quadratic functional

The obstacle to estimating `tau_w(P)` from one empirical table is the quadratic product of population marginals. Using two independent whole-replicate tables removes that plug-in bias exactly.

Because `X_1` and `X_2` are independent and each has mean `P`,

`E[X_1,Y(j) X_2,(ijk)] = P_Y(j) P_(ijk)`,

`E[X_1,XY(i,j) X_2,YZ(j,k)] = P_XY(i,j) P_YZ(j,k)`.

The same identities hold after swapping the two replicates. Linearity of expectation therefore gives

`E[h_w(X_1,X_2)]`
` = sum_(i,j,k) w_(ijk) [`
`     P_Y(j)P_(ijk) - P_XY(i,j)P_YZ(j,k)]`
` = tau_w(P)`.

No statement about the triples inside a control replicate enters this calculation. The independent units are the complete control tables `X_b`, exactly as in `VIS-061`.

This is the classical quadratic-functional/U-statistic idea specialized to the Markov-residual tensor. The Mathia-specific content is not the unbiasedness principle itself, but the choice of a denominator-free conditional-dependence functional that matches the active three-gap residual experiment and can be calibrated at the whole-control-replicate level.

## 3. One frozen witness has a dimension-free bounded range

For probability tables `x,y`,

`sum_(i,j,k) x_Y(j) y_(ijk)`
` = sum_j x_Y(j)y_Y(j) <= 1`.

Similarly,

`sum_(i,j,k) x_XY(i,j)y_YZ(j,k)`
` = sum_j x_Y(j)y_Y(j) <= 1`.

Therefore each of the four weighted terms entering `h_w` has absolute value at most `1` when `||w||_infty<=1`. The factor `1/2` gives

`|h_w(x,y)| <= 2`.

The `m` disjoint-pair kernels in `T_hat_w` are independent, each lies in `[-2,2]`, and each has mean `tau_w(P)`. Hoeffding's inequality for an average of `m` independent variables with range length `4` gives

`Pr(|T_hat_w-tau_w(P)| >= t)`
` <= 2 exp(-m t^2/8)`.

Setting the right-hand side to `rho` yields

`t = sqrt(8 log(2/rho)/m)`.

Both `T_hat_w` and `tau_w(P)` lie in `[-2,2]`, so their difference is deterministically at most `4`; taking the minimum gives the displayed safe radius.

The price of the clean proof is that an odd final replicate is discarded and the estimator uses only disjoint pairs. The all-pairs order-two U-statistic with the same kernel is also unbiased and can use the controls more efficiently; classical U-statistic concentration theory applies. The disjoint-pair form is retained here because its independence and confidence semantics are immediate and require no within-replicate assumptions.

## 4. Fixed-zeta confirmation needs no zeta process model

`VIS-060` separated two questions that had been conflated: comparison of one frozen arithmetic table with a random control population, and generalization across the zeta-zero process. The same distinction applies here.

Once `Z`, the representation, and `w` are frozen, `tau_w(Z)` is an exact deterministic number. The only random quantity is `T_hat_w`. Hence on the control event,

`|tau_w(Z)-tau_w(P)|`
` >= |tau_w(Z)-T_hat_w| - r_B(rho)`.

A gap larger than `r_B` therefore proves a nonzero population contrast for that fixed table and frozen witness with control-side probability only. No i.i.d. model, stationarity assumption, or resampling semantics for the Riemann zeros is introduced.

This certificate can be materially cheaper than the full `VIS-061` route when the declared three-gap support is fine. It removes the generic `sqrt(K/B)` law-estimation cost precisely by asking a smaller question. It does **not** establish separation of the complete residual vector, Fisher orientation, CMI, or every possible visual direction.

## 5. The witness must be frozen before confirmation

The dimension-free statement is for one fixed `w`. A useful visual workflow may choose `w` from exploratory information, but the confirmation sample must not be reused to optimize that direction.

It is valid, for example, to choose `w` from the frozen zeta table alone, because the theorem conditions on that table as deterministic. It is also valid to use an independent pilot control ensemble to construct a direction such as an approximate sign pattern of `C(Z)-C(P_pilot)`, freeze that `w`, and then evaluate it on fresh independent confirmation controls.

It is not valid to search many weight tensors on the same confirmation controls and then attach the single-witness radius to the most favorable one. A finite predeclared family can be covered with an ordinary multiplicity correction; a rich adaptive family requires an appropriate simultaneous-complexity argument. In the limit, optimizing over the entire `L^infty` unit ball recovers the full `L^1` residual difference and therefore gives up the low-dimensional advantage.

The same gate applies to zeta windows, partitions, support edits, unfolding choices, and any arithmetic correction in the control construction. Selection may happen during exploration, but the advertised confirmation guarantee belongs only to a frozen view or to a confidence construction that explicitly covers the selection.

## 6. Prior art and novelty boundary

The conditional-independence/Markov-completion identity is classical information theory; `VIS-020` already anchors it to Thomas Cover and Joy Thomas, **Elements of Information Theory**, 2nd ed., Wiley (2006), DOI `10.1002/047174882X`.

The use of independent copies to estimate a quadratic population functional is classical U-statistic territory. Wassily Hoeffding, **A Class of Statistics with Asymptotically Normal Distribution**, *Annals of Mathematical Statistics* 19:3 (1948), 293–325, DOI `10.1214/aoms/1177730196`, is the foundational reference for U-statistics and unbiased estimators built from symmetric kernels of independent observations.

The confidence step is also classical. Wassily Hoeffding, **Probability Inequalities for Sums of Bounded Random Variables**, *Journal of the American Statistical Association* 58:301 (1963), 13–30, DOI `10.1080/01621459.1963.10500830`, supplies the bounded-independent-sum inequality used directly for the disjoint-pair estimator and also treats related U-statistic bounds.

No new concentration theorem, U-statistic theorem, conditional-independence criterion, or minimax result is claimed. The durable contribution is the assembled interface forced by the current Mathia control problem: `VIS-062` says the generic full-law route must pay support dimension, while the denominator-free tensor `C(P)` exposes a predeclared quadratic residual direction that can instead be estimated from independent whole control replicates with a support-dimension-free scalar confidence radius.

## 7. Falsification and boundaries

Falsify the exact result by producing finite probability laws for which `C(P)=P_Y Delta(P)` fails on a positive middle-state fiber; by finding probability tables `x,y` and a weight tensor with `||w||_infty<=1` for which `|h_w(x,y)|>2`; by showing that the cross-replicate kernel is biased under the stated independent-identically-distributed replicate hypothesis; or by producing independent whole-replicate controls for which the displayed Hoeffding radius fails.

The theorem assumes independence across complete control replicates. Dependence between nominally separate CUE matrices, shared random seeds that induce coupling, adaptive simulation stopping tied to the witness, or reuse of the confirmation controls to choose `w` invalidates the stated confidence semantics.

The witness `C(P)` weights each conditional-dependence fiber by its middle-state mass. Rare middle states are therefore intentionally downweighted rather than magnified by a Fisher denominator. This is a different geometry from the normalized Fisher residual orientation of `VIS-041`/`VIS-057`, not a sharper estimate of the same object.

A nonzero certified witness difference is also not automatically arithmetic-specific. Finite-size CUE corrections, finite-height arithmetic corrections, unfolding choices, and other matched baselines remain mandatory. Conversely, failure to clear the radius for one `w` does not prove equality of the residual tensors; it only says that the chosen direction did not certify a difference at the declared confidence level.

## Research consequence

`VIS-062` left three honest escape routes from an impractical generic whole-law calibration: exploit control-specific structure, reduce the representation, or change the propagated error geometry. This finding instantiates the third route without pretending to solve the full distribution-estimation problem.

The accepted three-gap clue can now be tested at two different claim strengths. The conservative full-vector route remains `VIS-061` followed by `VIS-057`/`VIS-060`. When that ball is too loose, a lower-dimensional confirmation can instead freeze one mathematically interpretable `w`, use independent whole control replicates in the paired estimator above, and test the fixed zeta/control contrast directly with a radius of order `B^(-1/2)` independent of the table support size.

If a predeclared witness survives matched finite-size and arithmetic controls, that is a genuine finite-object separation worth replicating at fresh heights. If it does not, the line should not recover significance by optimizing a new direction on the same confirmation ensemble. A broader zeta-process claim still requires independent across-height evidence and a separately justified source-side model.