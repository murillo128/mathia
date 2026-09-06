# VIS-065 — hybrid modulus contrast is a single-factor coordinate modulo the residual

## Claim

Let `P_X(s)`, `Z_X(s)`, and `E_X(s)=zeta(s)/(P_X(s)Z_X(s))` be the nonzero hybrid Euler–Hadamard channels from `VIS-064`. For two admissible scales `X<Y`, define the real log-modulus increments

`A_XY = log|P_Y/P_X|`,

`B_XY = log|Z_Y/Z_X|`,

and the residual increment

`R_XY = log|E_X/E_Y|`.

`VIS-064` gives the exact relation

`A_XY + B_XY = R_XY`.

For the proposed orthogonal contrast

`C_XY = A_XY - B_XY`,

one therefore has the exact coordinate identities

`C_XY = 2 A_XY - R_XY = R_XY - 2 B_XY`,

and conversely

`A_XY = (R_XY + C_XY)/2`,

`B_XY = (R_XY - C_XY)/2`.

Thus `(R_XY,C_XY)` is merely an invertible linear reparameterization of `(A_XY,B_XY)`. Once the residual channel is treated as known or controlled, the contrast contains exactly the same remaining pointwise scalar information as either one factor increment. It does **not** by itself define an additional prime/zero interaction coordinate.

If the relative hybrid errors satisfy the hypotheses of `VIS-064`, so that

`|R_XY| <= delta_XY`

with

`delta_XY = -log(1-eta_X)-log(1-eta_Y)`,

then pointwise

`|C_XY - 2 A_XY| <= delta_XY`,

`|C_XY + 2 B_XY| <= delta_XY`.

Hence in an accurate-hybrid regime the proposed contrast is quantitatively close to twice the prime increment and to minus twice the zero increment. A visually strong contrast can therefore be inherited almost entirely from one factor rather than from a new cross-factor mechanism.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

The hybrid factorization is established prior art. The coordinate identities above are elementary consequences of `VIS-064`; no new theorem about the hybrid product, statistical independence, zeta, its zeros, or RH is claimed.

## 1. The sum/contrast coordinates do not add a degree of freedom

At every nonzero evaluation point, the hybrid identity gives

`R=A+B`.

Introducing `C=A-B` produces the linear change of variables

`(A,B) <-> (R,C)`

with inverse

`A=(R+C)/2`, `B=(R-C)/2`.

Calling `C` the direction orthogonal to the product-direction sum is geometrically correct in the Euclidean `(A,B)` plane, but it does not quotient out the product relation by itself. It simply chooses a complementary coordinate while retaining the residual coordinate `R`.

If the analysis conditions on, subtracts, or otherwise treats `R` as a known nuisance channel, only one scalar degree remains. That degree may be represented by `A`, by `B`, or by `C`; changing among them cannot create independent evidence.

## 2. Small residual makes the contrast a near-copy of either factor

From

`C=2A-R`

and

`C=R-2B`,

the pointwise deviations are exactly

`C-2A=-R`,

`C+2B=R`.

Therefore any deterministic or empirical control on `R` transfers immediately to the contrast. Under the `VIS-064` relative-error bound,

`|C-2A|, |C+2B| <= delta_XY`.

The same statement holds in any `L^p` norm over a height window for which the quantities are defined:

`||C-2A||_p = ||R||_p`,

`||C+2B||_p = ||R||_p`.

Thus a contrast heatmap, return map, or scale profile in a regime where the hybrid residual is small should be expected to resemble a rescaled single-factor picture. That resemblance is a coordinate consequence, not evidence of a new prime/zero transfer law.

## 3. Even covariance between the two factors has a forced component

For any sampling law over evaluation points with finite second moments, `B=R-A` implies

`Cov(A,B) = Cov(A,R) - Var(A)`

and

`Var(B) = Var(R) + Var(A) - 2 Cov(A,R)`.

Therefore strong negative covariance between `A` and `B` can arise simply because the sum residual `R` varies less than either factor. In the idealized limit `R=0`, one has `B=-A` exactly and the contrast is `C=2A`; perfect anticorrelation then carries no additional coupling information.

This does not prove that all joint statistics are forced. It identifies the part that must be removed before interpreting any empirical prime/zero dependence.

## 4. Visual falsification rule

A test based on `C=A-B` remains legitimate only with a narrower interpretation.

If the question is whether the **prime factor itself** has stable scale geometry that separates arithmetic data from randomized-prime controls, `C` can serve as a residual-corrected representation of that one-factor observable. Equivalent statements can be made from the zero factor.

If the question is instead whether there is a new **prime/zero interaction**, a large or structured `C` is not sufficient. The test must demonstrate structure not reconstructible from one factor together with the measured residual. Examples could involve a predeclared non-pointwise dependence between the prime increment and the residual field, or another statistic whose null is explicitly calibrated from the individual-factor and residual laws. Such a test is a new thread and is not established here.

In particular, do not count any of the following as independent evidence:

- a large magnitude of `C` when `A` itself is large;
- visual similarity between `C` and `2A` or `-2B` when `R` is small;
- strong negative covariance of `A` and `B` without comparing it with the exact `B=R-A` baseline.

## 5. Prior art and novelty boundary

Gonek, Hughes, and Keating's hybrid Euler–Hadamard model is the prior-art source for the independently defined prime and zero factors and the approximation error already recorded in `SOURCES.md`. Their framework also motivates statistical separation of prime and zero contributions in moment calculations.

Winston Heap, **On the splitting conjecture in the hybrid model for the Riemann zeta function**, *Forum Mathematicum* 35:2 (2023), 329–362, DOI `10.1515/forum-2022-0020`, proves substantial cases/bounds for that splitting program. This is a different question from the pointwise coordinate identity above, but it is an important boundary: statistical factorization or approximate independence of hybrid contributions is established prior-art territory, not a novelty claim available to this visual route.

`VIS-065` neither proves nor refutes the splitting conjecture. It says only that at fixed points and scales, once the exact hybrid residual is retained, the proposed linear contrast is algebraically equivalent to one factor plus that residual.

## 6. Boundaries and falsification

The log-modulus formulation requires all displayed factors and `zeta` to be nonzero at the evaluation point. Near zeros, one must use a separately justified regularization or a branch-free multiplicative formulation; divergent logarithms are not a visual signal.

The result does not make `A`, `B`, or `C` arithmetically uninteresting. A single factor may carry highly nontrivial arithmetic structure. It also does not eliminate non-pointwise statistics involving several scales or evaluation points. It only prevents a pointwise linear contrast from being interpreted as an extra cross-factor degree of freedom after the residual relation is known.

Falsify the exact claim by producing real numbers `A,B,R` arising from the stated nonzero hybrid increments with `A+B=R` but for which any of `C=2A-R`, `C=R-2B`, `A=(R+C)/2`, or `B=(R-C)/2` fails. The quantitative bounds fail only if the `VIS-064` residual bound itself fails under its stated hypotheses.

## Research consequence

The accepted prime-phase recursive-geometry clue should be narrowed again. The simple modulus contrast is still a usable predeclared observable, but its first honest interpretation is **within-factor scale geometry after explicit residual accounting**, not independent prime/zero coupling.

A subsequent visual experiment may test that within-factor question against matched controls. If the aim remains a genuinely joint hybrid mechanism, the next experiment must predeclare a statistic that survives reconstruction from one factor plus the residual and must calibrate it against the established hybrid/splitting baselines. That is a separate coherent research thread.