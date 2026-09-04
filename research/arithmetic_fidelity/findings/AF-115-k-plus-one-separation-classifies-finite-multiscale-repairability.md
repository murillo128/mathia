# AF-115 — `(k+1)`-sample separation classifies finite multiscale repairability

**Status:** `EXACT-DERIVED`, `STRUCTURAL-CLASSIFICATION`, `PROBABILISTIC-PACKING-COVERING`, `MULTISCALE-HIERARCHY`, `SCALE-FREE-FIDELITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-114 exactly classified whether a probability mass profile on logarithmic scale can be made tight by **one** translating center, equivalently whether one scalar spectral blow-up can retain asymptotically all normalized resource mass. Its genuine two-cloud control then showed that one scale may fail while two scales are plainly enough.

There is an exact finite hierarchy behind that example.

Let `(X,d)` be a metric space, let `(\mu_i)` be a net of Borel probability measures on `X`, and fix an integer `k\ge1`. For `R>0`, define the optimal `k`-center uncovered mass

\[
c_{i,k}(R)
:=
\inf_{a_1,\ldots,a_k\in X}
\mu_i\!\left(
X\setminus\bigcup_{r=1}^k \overline B(a_r,R)
\right).
\tag{1}
\]

Also let `X_{i,0},\ldots,X_{i,k}` be independent samples with law `\mu_i` and define the `(k+1)`-sample separation probability

\[
q_{i,k+1}(R)
:=
\mathbb P\!\left(
 d(X_{i,r},X_{i,s})>R
 \text{ for every }0\le r<s\le k
\right).
\tag{2}
\]

Then for every `i` and every `R>0`,

\[
\boxed{
 c_{i,k}(R)^k
 \le
 q_{i,k+1}(R)
 \le
 (k+1)c_{i,k}(R/2).
}
\tag{3}
\]

Equivalently,

\[
\boxed{
 c_{i,k}(R)
 \le
 q_{i,k+1}(R)^{1/k},
\qquad
 q_{i,k+1}(2R)
 \le
 (k+1)c_{i,k}(R).
}
\tag{4}
\]

Consequently the following are equivalent.

**(a) `k`-center tightness.** For every `\varepsilon>0` there are `R>0` and `i_0` such that

\[
 c_{i,k}(R)\le\varepsilon
 \qquad(i\ge i_0).
\tag{5}
\]

Thus all but `\varepsilon` of the mass can eventually be retained in `k` bounded-radius clusters whose centers may move with `i`.

**(b) Scale-free `(k+1)`-sample non-separation.** For every `\varepsilon>0` there are `R>0` and `i_0` such that

\[
 q_{i,k+1}(R)\le\varepsilon
 \qquad(i\ge i_0).
\tag{6}
\]

Thus a family is repairable by at most `k` moving centers exactly when, at sufficiently coarse resolution, `k+1` independent resource samples cannot retain a uniformly positive probability of occupying `k+1` mutually separated regions.

The criterion does **not choose the centers first**. It detects from an intrinsic `(k+1)`-point relation whether a `k`-center lift exists at all.

### Spectral specialization

For the positive Schatten profiles of AF-114, take

\[
\rho_i
=
\frac1{M_i}
\sum_j\lambda_{ij}^p\,\delta_{\log\lambda_{ij}}
\qquad
\left(M_i=\sum_j\lambda_{ij}^p\right).
\tag{7}
\]

Choosing logarithmic centers `a_{i,1},\ldots,a_{i,k}` is equivalent to choosing scalar spectral scales

\[
s_{i,r}=e^{a_{i,r}}>0.
\tag{8}
\]

Condition (5) becomes

\[
\boxed{
\frac1{M_i}
\sum_{j:\ \lambda_{ij}\in
\bigcup_{r=1}^k[e^{-R}s_{i,r},e^R s_{i,r}]}
\lambda_{ij}^p
\ge1-\varepsilon
\quad\text{eventually}.
}
\tag{9}
\]

Meanwhile (6) is determined without selecting any `s_{i,r}`: for `k+1` independent eigenvalue samples drawn with probabilities proportional to `\lambda^p`, the probability that **every pairwise log-ratio** satisfies

\[
\left|\log\frac{\Lambda_{i,r}}{\Lambda_{i,s}}\right|>R
\tag{10}
\]

must become uniformly small at large `R`.

Hence

\[
\boxed{
\text{at most }k\text{ scalar scales can retain the normalized }p\text{-mass}
\iff
\text{the }(k+1)\text{-sample logarithmic packing probability vanishes at large scale.}
}
\tag{11}
\]

For `k=1`, this recovers AF-114's one-scale classification and also gives the sharper elementary estimate

\[
 c_{i,1}(R)\le q_{i,2}(R),
\tag{12}
\]

where AF-114 used a weighted-median construction to obtain a convenient explicit center and the weaker bound `c_{i,1}(R)\le2q_{i,2}(R)`. The median remains useful because it provides a canonical benchmark center; (12) is only an existence bound.

## Derivation

The lower bound in (3) is a sequential packing argument.

Write `c=c_{i,k}(R)`. Suppose `X_{i,0},\ldots,X_{i,j-1}` have already been sampled with pairwise distances greater than `R`, where `1\le j\le k`. Conditional on those samples,

\[
\mathbb P\!\left(
 d(X_{i,j},X_{i,r})>R
 \text{ for all }r<j
 \mid X_{i,0},\ldots,X_{i,j-1}
\right)
=
\mu_i\!\left(
 X\setminus\bigcup_{r<j}\overline B(X_{i,r},R)
\right).
\tag{13}
\]

Any family of fewer than `k` balls can be padded by repeated centers without changing its union. Therefore the right-hand side of (13) is at least `c`. Multiplying the `k` successive conditional lower bounds gives

\[
 q_{i,k+1}(R)\ge c^k,
\tag{14}
\]

which is the left inequality in (3).

For the upper bound, fix arbitrary centers `a_1,\ldots,a_k` and write

\[
G=\bigcup_{r=1}^k\overline B(a_r,R/2).
\tag{15}
\]

If all `k+1` samples lie in `G`, the pigeonhole principle puts two samples in the same radius-`R/2` ball. Their distance is then at most `R`, so the event in (2) cannot occur. Thus that event forces at least one sample outside `G`, and the union bound gives

\[
q_{i,k+1}(R)
\le
(k+1)\mu_i(X\setminus G).
\tag{16}
\]

Taking the infimum over the centers proves the right inequality in (3).

Equations (5) and (6) are now equivalent directly from (3)--(4): one implication uses the radius doubling in the upper estimate; the other uses the `k`th-root lower estimate. No compactness theorem, selected subsequence, or preferred center is required for this equivalence.

## Exact controls and hierarchy

### AF-114's two-cloud obstruction has scale number exactly two

For the AF-114 family whose logarithmic `p`-mass is supported at `-n` and `-2n` with asymptotic weights `1/2,1/2`, one-center tightness fails because the two order-one clouds separate by distance `n`.

But two centers placed at the two support points give

\[
 c_{n,2}(0)=0
\tag{17}
\]

exactly. Equivalently, three independent samples from a two-point support can never be pairwise separated: two must coincide. Hence

\[
 q_{n,3}(R)=0
\qquad(R\ge0).
\tag{18}
\]

So the earlier statement that a “second scale is necessary” can now be read literally: the family fails the `k=1` gate and passes the `k=2` gate.

### `m` persistent clouds calibrate every finite level

Fix `m\ge2`. For each `n`, let a positive finite-rank operator have, for `1\le\ell\le m`,

\[
N_{n,\ell}:=\lfloor e^{p\ell n}\rfloor
\tag{19}
\]

eigenvalues equal to

\[
\lambda_{n,\ell}:=e^{-\ell n}.
\tag{20}
\]

Each level contributes

\[
N_{n,\ell}\lambda_{n,\ell}^p\longrightarrow1,
\tag{21}
\]

so the normalized logarithmic `p`-mass tends to equal weight `1/m` on the `m` locations

\[
-n,-2n,\ldots,-mn.
\tag{22}
\]

For every fixed `R`, these locations are mutually more than `R` apart once `n>R`. Therefore, for `k<m`,

\[
\boxed{
 c_{n,k}(R)\longrightarrow1-\frac{k}{m}>0,
}
\tag{23}
\]

while the separation probability converges to the probability that `k+1` independent uniform labels in `{1,\ldots,m}` are all distinct:

\[
\boxed{
 q_{n,k+1}(R)
\longrightarrow
\frac{m(m-1)\cdots(m-k)}{m^{k+1}}>0.
}
\tag{24}
\]

For `k\ge m`, centering every cloud gives zero uncovered mass. Thus the hierarchy detects the exact number of persistent logarithmic levels in this matched family.

### A growing cloud count defeats every finite multiscale lift

Let the same construction use `m=m_n\to\infty` levels. For every fixed `k` and fixed `R`, eventually the levels are mutually `R`-separated and

\[
 c_{n,k}(R)\longrightarrow1,
\tag{25}
\]

whereas

\[
 q_{n,k+1}(R)\longrightarrow1.
\tag{26}
\]

Hence **no fixed finite number of scalar scales can retain the normalized mass**. A proposed repair for such a family needs a genuinely variable-complexity object: for example a profile measure, a growing marked scale set, a tree/hierarchy, or an independent source theorem that excludes this regime.

This separates “multiscale” into two mathematically different cases: finite scale multiplicity, where some fixed `k` passes the gate, and unbounded scale complexity, where every finite `k` fails.

## Exact controls and failure modes

### The criterion measures resource clustering, not object reconstruction

Just as AF-114's pairwise difference law does not recover a centered spectral profile, the `(k+1)`-sample separation probabilities do not determine `\mu_i`, the cluster centers, or the internal distribution inside each cluster. They certify only the existence or impossibility of a bounded-complexity center lift.

Two very different measures can have the same entire family of separation probabilities. Any downstream claim needing phase, provenance, multiplicity labels, eigenvectors, arithmetic orientation, or the exact within-scale profile requires additional retained structure.

### `k` is a complexity budget, not an intrinsic label unless the category permits `k` free centers

The centers in (1) may be chosen after inspecting the whole measure. Therefore (5) is an **existence** criterion. An intended RH construction may permit only scales forced by geometry, arithmetic, an operator, or a functorial rule. Passing the `k`-center gate does not prove that those admissible scales exist.

Conversely, failing the unrestricted gate is decisive: if even arbitrary moving centers cannot retain the mass with `k` clusters, no more constrained family of `k` scalar scales can do so.

### Vanishing satellites are ignored for the correct reason

A family may contain arbitrarily many distant spectral levels whose total normalized mass tends to zero. They do not force the finite-scale number upward because both `c_{i,k}` and `q_{i,k+1}` are resource-weighted. Persistent separated mass, rather than support cardinality or condition number, is the obstruction.

### The metric matters

The theorem is metric rather than specifically one-dimensional. In the spectral application the logarithmic metric is forced by multiplicative rescaling: translation of `\log\lambda` is scalar dilation of `\lambda`. Replacing it with an unrelated metric changes which structures count as one scale and therefore changes the fidelity question.

### Signed or nonnormal spectral data remain outside the probability model

As in AF-113--AF-114, the `\lambda^p` weights are positive. Cancellative signed spectral measures and nonnormal operators may require a different resource measure plus phase/eigenvector markings. The theorem applies once a positive probability measure and a justified metric have been identified; it does not manufacture that reduction.

### Finite multiscale fidelity is still weaker than arithmetic fidelity

A rational-prime-derived operator and a matched Beurling/generalized-prime control may have the same finite scale complexity. Passing (11) says only that a bounded number of scalar coordinates can prevent resource escape. It does not show that the retained clusters distinguish rational primes from controls at the same information layer.

## Prior art and novelty assessment

The mechanisms used here are classical, and **no theorem-level novelty is claimed**.

The deterministic geometry is the familiar packing-versus-covering principle behind metric `k`-center clustering: `k+1` mutually separated points obstruct a cover by `k` sufficiently small balls, while a `k`-ball cover forces a pigeonhole collision among `k+1` points. Teofilo F. Gonzalez's 1985 `k`-center work is a standard algorithmic landmark for this packing/covering geometry. The present inequalities add only the elementary probability weighting needed for the Arithmetic Fidelity resource measure.

P.-L. Lions's concentration-compactness framework is the broader classical language for loss of compactness by translation and for mass splitting into separated components. AF-114 already records the relevant Lions and probability-tightness references. AF-115 should be read as a finite-cluster bookkeeping theorem at that existing frontier, not as a new concentration-compactness principle.

The durable Arithmetic Fidelity content is the **audit hierarchy**: instead of saying vaguely that a failed one-scale normalization “needs multiscale structure,” equation (11) supplies a falsifiable scale-free test for each finite complexity budget `k`, and (25)--(26) exhibit a regime in which every fixed finite budget is impossible.

## Consequences for Arithmetic Fidelity

AF-113 identified boundary escape after an operator-norm blow-up. AF-114 removed dependence on the chosen scalar and separated a bad normalization from genuine failure of every one-scale repair. AF-115 now resolves the next ambiguity: when one scale genuinely fails, it decides whether a fixed finite number of scales is enough or whether the required scale complexity itself diverges.

The resulting audit order is sharper. First test `k=1`. If it fails, do not immediately introduce an unrestricted profile or renormalization tree; test `k=2,3,\ldots` through the intrinsic separation probabilities. The smallest finite `k` that passes is the least unrestricted scalar-center budget capable of preventing resource escape. If every finite `k` fails, no finite list of scalar normalizations can be faithful to the mass cloud.

For later arithmetic applications, this means that a proposed compression can be assigned a precise **scale-complexity lower bound** before choosing a repair. A mechanism using only finitely many global scales must prove that its arithmetic resource law passes the corresponding `(k+1)`-sample separation gate; otherwise the missing cross-scale relations have already been discarded before any later trace, determinant, positivity, or zero-selection step can recover them.