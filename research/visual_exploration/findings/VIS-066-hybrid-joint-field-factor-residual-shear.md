# VIS-066 — the full hybrid prime/zero increment field is an invertible shear of one factor plus residual

## Claim

Let `P_X(s)`, `Z_X(s)`, and `E_X(s)=zeta(s)/(P_X(s)Z_X(s))` be the nonzero hybrid Euler–Hadamard channels from `VIS-064`. On any common index set `Omega` of evaluation points and admissible scale pairs, define the real log-modulus increment fields

`A = log|P_Y/P_X|`,

`B = log|Z_Y/Z_X|`,

`R = log|E_X/E_Y|`.

Pointwise on `Omega`, `VIS-064` gives

`R = A + B`.

Therefore the complete two-channel prime/zero field is related to the factor/residual field by the invertible linear shear

`(A,B) -> (A,R) = (A,A+B)`

with inverse

`(A,R) -> (A,B) = (A,R-A)`.

Consequently **every deterministic statistic of the complete fields `A` and `B`, including non-pointwise and nonlinear statistics, is exactly reconstructible from one factor field together with the residual field**. Explicitly, for any functional `F` for which the expressions are defined,

`F(A,B) = G(A,R)`

with

`G(a,r) = F(a,r-a)`.

The same statement holds with `B` in place of `A`.

Thus moving from the linear contrast of `VIS-065` to covariance maps, lagged dependence, multiscale summaries, nonlinear embeddings, return maps, topology, or another deterministic joint statistic does not create an additional prime/zero information channel. Such a statistic may still expose nontrivial structure, but after the exact residual is retained its information belongs to the pair `(one factor, residual)`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

The hybrid Euler–Hadamard factorization is established prior art. The shear/reconstruction statement is elementary linear algebra applied to the exact residual identity from `VIS-064`; no new theorem about zeta, hybrid moments, statistical independence, or RH is claimed.

## 1. Field-level reconstruction closes the non-pointwise escape

`VIS-065` showed that the pointwise linear contrast `C=A-B` is only a complementary coordinate to `R=A+B`. It deliberately left open the possibility that a non-pointwise joint statistic might evade that obstruction.

But the residual relation is not merely a constraint on one scalar statistic. It holds at every index `omega in Omega`. Hence the entire field `B` is recovered pointwise from `(A,R)` by

`B(omega)=R(omega)-A(omega)`.

Once the complete arrays/functions are recovered, any deterministic operation applied afterward can also be recovered. If `F` uses several heights, several scale pairs, nonlinear transforms, lagged products, local neighborhoods, singular values, persistent summaries, or any other deterministic construction, substitute `B=R-A` everywhere to obtain an exactly equivalent functional of `(A,R)`.

No amount of post-processing of the same two hybrid increment fields can manufacture a third degree of freedom that was absent before the post-processing.

## 2. The visual coordinate change is a shear, not a new geometry

At one index the coordinate change is

`[A]   [1 0][A]`
`[R] = [1 1][B]`.

Its determinant is `1`, so it is invertible. On a finite collection of indices the full transformation is the corresponding block-diagonal invertible map. The prime/zero point cloud and the factor/residual point cloud therefore contain the same raw information.

This does **not** mean every visual appearance is unchanged. Euclidean lengths, angles, isotropy, and correlation ellipses are not invariant under a shear. A dramatic difference between an `(A,B)` plot and an `(A,R)` plot can therefore be a coordinate effect rather than new arithmetic structure.

Topological or information-presence claims must respect the invertibility: if a feature can be computed from the raw `(A,B)` data, then it can be computed from `(A,R)` data as well. Metric claims need an explicit reason why the chosen metric is canonical rather than merely convenient.

## 3. Dependence statistics become factor/residual questions

The result does not say that dependence statistics are numerically trivial. For example, the covariance identity already recorded in `VIS-065`,

`Cov(A,B)=Cov(A,R)-Var(A)`,

may still vary nontrivially with height, scale, or smoothing because the joint behavior of `A` and `R` may vary.

What changes is the interpretation. A statistic built from both prime and zero increments is not evidence for an **additional** prime/zero coupling merely because both channels appear in its formula. After `B=R-A` is imposed, the same statistic is a property of the factor/residual pair.

Likewise, a probabilistic null is not determined by the marginal laws of `A` and `R` alone; their joint law can remain nontrivial. Testing that joint law is legitimate, but it is a factor-versus-hybrid-error question unless some further independently defined structure is introduced.

This distinction matters for the accepted recursive-geometry clue: replacing a pointwise contrast with a nonlinear or lagged joint statistic does not by itself escape the reconstruction obstruction.

## 4. Visual falsification rule

For any proposed prime/zero scale visualization built only from the same hybrid increment fields:

1. write the statistic as a functional `F(A,B)`;
2. substitute `B=R-A` to obtain `G(A,R)`;
3. determine whether the claimed effect remains meaningful when described entirely in factor/residual coordinates;
4. reject any claim of an extra prime/zero information channel if no independently defined variable or constraint remains after this reconstruction.

This applies equally to a single height window or to a whole family of predeclared windows and scales, provided the same exact residual field is available at every index used by the statistic.

A surviving research question can still ask whether `A` has stable arithmetic scale geometry, whether `R` has unexpected structure beyond the hybrid error theorem, or whether the **joint law of `(A,R)`** separates the arithmetic construction from a matched control. Those are honest questions, but none acquires an extra degree of freedom by being rewritten in terms of `B`.

## 5. Prior art and novelty boundary

S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549, DOI `10.1215/S0012-7094-07-13634-2`, provide the hybrid prime/zero representation that underlies the channels considered here.

The present finding does not claim a new result about that representation. It records the exact information-theoretic boundary induced by retaining the hybrid residual as a field: the constrained prime/zero coordinates and the factor/residual coordinates are related by an elementary invertible change of variables.

Existing hybrid-moment and splitting questions concern probabilistic/statistical behavior of the factors. This finding neither proves nor refutes such results. It only prevents a Mathia visual analysis from treating a deterministic re-expression of the same complete fields as an additional interaction channel.

## 6. Boundaries and falsification

The log-modulus fields require the displayed factors and `zeta` to be nonzero at every index used. Near zeros, use a separately justified regularization or a branch-free formulation; divergent logarithms are not visual evidence.

The result assumes the residual field `R` is retained at the same indices as `A` and `B`. If an experiment deliberately discards `R`, uses an independently observed quantity not recoverable from the hybrid channels, or compares genuinely different factorizations with additional external structure, its information question must be analyzed separately.

Reconstructibility also does not imply that a chosen metric, estimator, or control distribution has identical numerical behavior after the shear. It says only that no deterministic statistic of the complete observed `(A,B)` fields contains information absent from the complete `(A,R)` fields.

Falsify the exact claim by producing fields satisfying `R=A+B` pointwise and a deterministic functional of `(A,B)` that cannot be evaluated after reconstructing `B=R-A` from `(A,R)`.

## Research consequence

The accepted prime-phase recursive-geometry clue should be narrowed once more. The proposed escape through a non-pointwise joint prime/zero statistic is closed at the level of deterministic information: the entire zero-increment field is reconstructible from the prime-increment and residual fields, and vice versa.

The next coherent visual experiment should therefore test a predeclared **within-factor** scale statistic against matched arithmetic controls, or explicitly study factor/residual dependence with a calibrated joint null. It should not present a nonlinear, lagged, or multiscale recombination of `A` and `B` as a new prime/zero coupling merely because the formula uses both factors.