# AF-182 — Euler-generator clusters have arbitrary-order finite-difference flatness

**Status:** `EXACT-DERIVED`, `LITERATURE-CONTEXT`, `ARITHMETIC-CONTROL`, `QUANTITATIVE-RECOVERY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-180 and AF-181 showed that a **single** nearby Euler-generator replacement can remain exactly identifiable while becoming badly conditioned under right-half-plane observation. The one-generator control leaves an obvious escape: perhaps instability is only first order, and a stronger source geometry or moderate bandwidth restores a uniform power-law inverse once several local factors are observed together.

There is a stronger obstruction. Positive generalized-prime clusters can be arranged so that their first `m-1` log-coordinate moments agree while their Euler-log observations differ only at **order `m`** in the cluster spacing. The source separation in one-dimensional Wasserstein geometry remains exactly first order. Since `m` is arbitrary, no positive uniform inverse Hölder exponent survives on a class allowing arbitrarily high cluster order.

Fix

\[
x>0,
\qquad
\delta>0,
\qquad
m\ge1,
\qquad
s=\sigma+it,
\qquad
\sigma>0,
\tag{1}
\]

and define the Euler logarithm of one log-generator by

\[
F_s(x)
=-\log(1-e^{-sx})
=\sum_{k\ge1}\frac{e^{-ksx}}{k}.
\tag{2}
\]

For arithmetic Euler products one may restrict throughout to `sigma>1`; the stronger `sigma>0` statement in `(2)` is only the local-factor analytic domain.

Let

\[
\Delta_\delta^m F_s(x)
=
\sum_{j=0}^{m}(-1)^{m-j}\binom mj F_s(x+j\delta)
\tag{3}
\]

be the forward `m`-th finite difference. Then

\[
\boxed{
\Delta_\delta^m F_s(x)
=
\int_{[0,\delta]^m}
F_s^{(m)}(x+u_1+\cdots+u_m)
\,du_1\cdots du_m,
}
\tag{4}
\]

and

\[
F_s^{(m)}(y)
=(-s)^m\sum_{k\ge1}k^{m-1}e^{-ksy}.
\tag{5}
\]

Consequently, for fixed vertical bandwidth `T<infinity`, with

\[
S_T=\sqrt{\sigma^2+T^2},
\tag{6}
\]

one has the uniform bound

\[
\boxed{
\sup_{|t|\le T}
|\Delta_\delta^m F_{\sigma+it}(x)|
\le
\delta^m S_T^m (m-1)!
\frac{e^{-\sigma x}}{(1-e^{-\sigma x})^m}.
}
\tag{7}
\]

The finite difference is therefore `O(\delta^m)` on every fixed right-half-plane bandwidth window.

### 1. The cancellation is realized by two positive matched controls

Put

\[
M=2^{m-1}.
\tag{8}
\]

Split the binomial row by the sign of `(-1)^{m-j}` and form two probability measures

\[
\mu_+
=
\frac1M
\sum_{(-1)^{m-j}=+1}
\binom mj\,\delta_{x+j\delta},
\tag{9}
\]

\[
\mu_-
=
\frac1M
\sum_{(-1)^{m-j}=-1}
\binom mj\,\delta_{x+j\delta}.
\tag{10}
\]

They are distinct positive measures with the same total mass. Moreover, for every integer `0<=r<m`,

\[
\boxed{
\int u^r\,d\mu_+(u)
=
\int u^r\,d\mu_-(u).
}
\tag{11}
\]

Thus the two controls agree on every polynomial statistic in log-coordinate of degree below `m`.

Their Euler-log observation difference is exactly

\[
\int F_s(u)\,d(\mu_+-\mu_-)(u)
=
\frac1M\Delta_\delta^m F_s(x).
\tag{12}
\]

For

\[
D_T(\mu,\nu)
=
\sup_{|t|\le T}
\left|
\int F_{\sigma+it}(u)\,d(\mu-\nu)(u)
\right|,
\tag{13}
\]

`(7)` gives

\[
\boxed{
D_T(\mu_+,\mu_-)
\le
2^{1-m}\delta^m S_T^m(m-1)!
\frac{e^{-\sigma x}}{(1-e^{-\sigma x})^m}.
}
\tag{14}
\]

### 2. Their source separation is exactly first order

In one-dimensional Wasserstein-1 distance,

\[
\boxed{
W_1(\mu_+,\mu_-)=\delta.
}
\tag{15}
\]

Hence, for every fixed `m>=2`, `x>0`, `sigma>0`, and finite `T`,

\[
\boxed{
\frac{D_T(\mu_+,\mu_-)}
{W_1(\mu_+,\mu_-)}
\le
C_{m,x,\sigma,T}\,\delta^{m-1}
\longrightarrow0
\qquad(\delta\downarrow0).
}
\tag{16}
\]

Therefore no positive uniform local lower-Lipschitz constant can hold for this bounded-band Euler-log observation on any source class containing these coalescing matched clusters.

This is a **conditioning obstruction, not an exact-collapse theorem**: for every fixed `delta>0` the two finite Euler-generator multisets need not have identical complete observations.

### 3. Arbitrary cluster order destroys every positive uniform inverse Hölder exponent

Suppose a source class containing the parity-split controls for arbitrarily large `m` admitted, in a neighborhood of collision, a uniform inverse Hölder estimate

\[
W_1(\mu,\nu)
\le
C\,D_T(\mu,\nu)^\alpha
\tag{17}
\]

for some `alpha>0`. Along the order-`m` family, `(14)`--`(15)` would imply

\[
\delta
\le
C'\delta^{m\alpha}.
\tag{18}
\]

For any fixed `alpha>0`, choose `m>1/alpha`. Then `(18)` fails as `delta downarrow0`. Thus

\[
\boxed{
\text{no uniform positive inverse Hölder exponent exists on an unrestricted cluster-order class.}
}
\tag{19}
\]

This does **not** rule out every possible modulus of continuity. It rules out all uniform power-law inverse moduli on a class that permits arbitrarily high finite-difference cancellation order.

### 4. Bandwidth must grow with both separation and cluster order

The bound `(14)` remains valid when the bandwidth depends on `delta`. Since

\[
\frac{D_T}{W_1}
=O\!\left(\delta^{m-1}S_T^m\right),
\tag{20}
\]

this matched family continues to force the lower-Lipschitz ratio to zero whenever

\[
T(\delta)
=o\!\left(\delta^{-(m-1)/m}\right).
\tag{21}
\]

Therefore avoiding **this** order-`m` obstruction requires at least the one-way necessary scaling

\[
\boxed{
T(\delta)=\Omega\!\left(\delta^{-(m-1)/m}\right).
}
\tag{22}
\]

As `m->infinity`, the exponent `(m-1)/m` approaches `1`. Arbitrarily high matched-cluster order therefore pushes the necessary bandwidth scale toward the reciprocal-separation scale `1/delta` already familiar from super-resolution.

Equation `(22)` is not sufficient for stable inversion. It only states when this explicit family stops certifying vanishing lower-Lipschitz ratio by `(14)`.

### 5. The construction is a genuine positive generalized-prime control

Set

\[
q_j=e^{x+j\delta}>1.
\tag{23}
\]

Before normalization, `(9)`--`(10)` are two equal-mass finite multisets of positive generalized-prime generators: generator `q_j` occurs with integer multiplicity `\binom mj` on the corresponding parity side. Their Euler-log difference is exactly `\Delta_\delta^m F_s(x)`.

To embed either finite block into an infinite Beurling generalized-prime system, append the same sufficiently rapidly increasing common tail to both sides. The common tail cancels identically in the log-zeta difference, while absolute convergence can be arranged in any prescribed right half-plane. Thus the obstruction is not an artifact of signed prime multiplicities: **the signed finite difference arises as the difference of two ordinary positive generalized-prime multisets.**

The normalized measures `(9)`--`(10)` are used only to put source geometry on a fixed probability-mass scale. In the unnormalized multiset geometry, both the observation discrepancy and transport distance acquire the same factor `M`, so the conditioning ratio `(16)` is unchanged.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{exact local-factor identifiability does not control recovery regularity;}\\
\text{positive matched Euler clusters can annihilate arbitrarily many low-order log-coordinate moments;}\\
\text{bounded-band Euler-log contrast can then vanish to arbitrary algebraic order in cluster spacing;}\\
\text{without a cluster-order/separation restriction, no uniform positive inverse Hölder exponent survives.}
\end{array}}
\tag{24}
\]

## Derivation

### Exact finite-difference identity

For a differentiable function,

\[
\Delta_\delta f(x)
=f(x+\delta)-f(x)
=\int_0^\delta f'(x+u)\,du.
\tag{25}
\]

Iterating `(25)` `m` times gives `(4)` exactly. On `Re(s)=sigma>0`, the expansion `(2)` converges absolutely and locally uniformly, so termwise differentiation yields `(5)`.

For `y>=x`,

\[
|F_s^{(m)}(y)|
\le
|s|^m
\sum_{k\ge1}k^{m-1}e^{-k\sigma x}.
\tag{26}
\]

Writing `r=e^{-sigma x}`, the standard Eulerian-polynomial identity gives

\[
\sum_{k\ge1}k^{m-1}r^k
=
\frac{rA_{m-1}(r)}{(1-r)^m},
\tag{27}
\]

where the Eulerian polynomial `A_{m-1}` has nonnegative coefficients summing to `(m-1)!`. Since `0<r<1`,

\[
\sum_{k\ge1}k^{m-1}r^k
\le
(m-1)!\frac{r}{(1-r)^m}.
\tag{28}
\]

Combining `(4)`, `(26)`, `(28)`, and `|s|<=S_T` proves `(7)`.

There is also the exact Fourier-Laplace form

\[
\boxed{
\Delta_\delta^m F_s(x)
=
\sum_{k\ge1}
\frac{e^{-ksx}}k
\left(e^{-ks\delta}-1\right)^m,
}
\tag{29}
\]

which makes the order-`m` cancellation transparent: every Euler harmonic acquires the same `m`-th finite-difference zero as `delta->0` at fixed `s`.

### Moment matching

The signed difference of `(9)` and `(10)` is

\[
\mu_+-\mu_-
=
\frac1M
\sum_{j=0}^{m}(-1)^{m-j}\binom mj\delta_{x+j\delta}.
\tag{30}
\]

For every polynomial `P` of degree `<m`, the `m`-th finite difference vanishes:

\[
\sum_{j=0}^{m}(-1)^{m-j}\binom mj P(x+j\delta)=0.
\tag{31}
\]

Taking `P(u)=u^r` gives `(11)`. Taking `P=F_s` gives `(12)` rather than zero because `F_s` is analytic but not a polynomial of degree below `m`.

### Exact Wasserstein distance

For probability measures on the real line,

\[
W_1(\mu_+,\mu_-)
=
\int_{\mathbb R}|G_+(u)-G_-(u)|\,du,
\tag{32}
\]

where `G_+`, `G_-` are their cumulative distribution functions. Between consecutive nodes `x+jdelta` and `x+(j+1)delta`, the magnitude of the cumulative signed mass is

\[
\frac1M
\left|
\sum_{k=0}^{j}(-1)^k\binom mk
\right|
=
\frac1M\binom{m-1}{j},
\qquad 0\le j<m,
\tag{33}
\]

using the elementary alternating-binomial identity

\[
\sum_{k=0}^{j}(-1)^k\binom mk
=(-1)^j\binom{m-1}{j}.
\tag{34}
\]

Every interval has length `delta`, so

\[
W_1
=
\frac\delta M
\sum_{j=0}^{m-1}\binom{m-1}{j}
=
\frac\delta{2^{m-1}}2^{m-1}
=\delta,
\tag{35}
\]

proving `(15)`.

## Exact controls

### Order one reproduces ordinary nearby-generator conditioning

For `m=1`, the two controls are point masses at `x` and `x+delta`. Equation `(7)` gives an `O(delta)` Euler-log discrepancy against `W1=delta`; no extra conditioning loss is forced. The genuinely stronger effect begins at `m=2`, where matched first moments remove the linear response.

### Every fixed moment budget can be defeated one order later

If a proposed compression retains all log-coordinate polynomial moments through degree `r`, choose `m=r+1`. The controls match every retained moment by `(11)` while remaining source-separated by exactly `delta`. Thus a finite moment ledger does not prevent arbitrarily high local Euler cancellation when cluster order is allowed to increase.

This is not an exact-collapse claim for the full Euler observation: the nonlinear analytic family `F_s` contains information beyond any fixed moment list. The result concerns its **conditioning on bounded frequency windows**.

### Positivity does not remove the cancellation

The signed coefficients in `(3)` could misleadingly suggest an inadmissible signed-prime perturbation. Equations `(9)`--`(10)` show otherwise: each side separately has only positive integer multiplicities before normalization. The sign appears only when comparing two legitimate positive systems.

### Fixed cluster order leaves an order-dependent Hölder possibility open

For one fixed `m`, `(14)` alone rules out inverse Hölder exponents `alpha>1/m`, but does not rule out `alpha<=1/m`. The stronger statement `(19)` requires a source class with **unbounded** cluster order. Any recovery theorem imposing fixed support size, fixed multiplicity, minimum separation, or another complexity bound lies outside that no-go unless the hypotheses still admit the parity-split family.

## Prior art and novelty assessment

No theorem-level novelty is claimed for finite-difference cancellation, moment annihilation, or clustered super-resolution instability.

- The identity that an `m`-th finite difference annihilates polynomials of degree below `m`, together with the alternating-binomial partial-sum formula used in `(33)`, is classical finite-difference/combinatorial analysis.
- David L. Donoho, **“Superresolution via Sparsity Constraints,”** *SIAM Journal on Mathematical Analysis* 23(5) (1992), 1309--1331, DOI `10.1137/0523074`, established the classical sparsity/super-resolution setting in which stable inversion deteriorates as spectral sources approach below the Rayleigh scale.
- Ankur Moitra, **“Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices,”** *Proceedings of STOC 2015*, 821--830, DOI `10.1145/2746539.2746561`, arXiv `1408.1681`, proves sharp separation-dependent conditioning thresholds for Vandermonde/super-resolution recovery. This is direct prior art for treating reciprocal separation as a recovery resource rather than confusing injectivity with stability.
- Laurent Demanet and Nam Nguyen, **“The recoverability limit for superresolution via sparsity,”** arXiv `1502.01385` (2015), derive minimax error scaling polynomially in the super-resolution factor with exponent depending on sparsity. Their result is especially close in spirit to the present arbitrary-order power-law degradation.
- Dmitry Batenkov, Gil Goldman, and Yosef Yomdin, **“Super-resolution of near-colliding point sources,”** *Information and Inference: A Journal of the IMA* 10(2) (2021), 515--572, DOI `10.1093/imaiai/iaaa005`, studies clustered nodes below the Rayleigh limit and obtains cluster-size-dependent minimax recovery rates. It is the natural modern boundary for the claim that collision order controls inverse conditioning.
- Arne Beurling, **“Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. I,”** *Acta Mathematica* 68 (1937), 255--291, DOI `10.1007/BF02546666`, is the foundational generalized-prime framework. Standard Beurling systems are sequences/multisets of real generators greater than one tending to infinity, so repeated generators may carry multiplicity.

The exact residual derived here is deliberately narrower: **the Euler local-factor kernel admits explicit positive parity-split generalized-prime clusters whose log-coordinate moments match through degree `m-1`, whose normalized `W1` distance is exactly `delta`, and whose bounded-band log-zeta discrepancy is `O(delta^m)`.** The literature search found the surrounding finite-difference, Vandermonde, super-resolution, and generalized-prime mechanisms, but this exact specialization is not treated as evidence of novelty and the finding makes no novelty claim.

## Boundaries and failure modes

1. **This is not failure of exact Euler-product injectivity.** Complete exact Euler data can distinguish finite generator multisets. The result is about the modulus of inverse recovery on bounded observation windows as generators collide.

2. **The metric is part of the theorem.** The exact source statement uses normalized one-dimensional `W1` in log-generator coordinate and a sup norm on one vertical Euler-log bandwidth window. Other source or output geometries can change the exponent.

3. **Unbounded cluster order is essential to the no-positive-Hölder conclusion.** Fixed support-size or separation hypotheses can restore an order-dependent inverse modulus and are consistent with classical super-resolution theory.

4. **Equation `(22)` is necessary only against this control.** Matching or exceeding that bandwidth does not prove stable Euler inversion. Conversely, a stronger observation family than one fixed vertical line may expose additional derivatives or global constraints.

5. **The probability normalization is analytical bookkeeping, not a fractional-prime claim.** Literal generalized-prime controls use the unnormalized integer binomial multiplicities. Normalization divides source and observation scales by the same `M` only to compare cluster orders in a common metric.

6. **The common-tail embedding carries no arithmetic conclusion by itself.** It proves admissibility inside the broad Beurling control class, not similarity to the rational primes in counting density, unique arithmetic role, or zeta-zero behavior.

7. **No RH implication is asserted.** The result identifies a pre-compression stability gate: any route that aggregates nearby arithmetic generators through a smooth bounded-band Euler/local-factor observable must control cluster complexity, retain a stronger marking, or supply bandwidth/structure capable of defeating high-order cancellation before claiming stable prime provenance downstream.

## Consequences for Arithmetic Fidelity

AF-180 and AF-181 isolated two first-order resources for one changed generator: Laplace amplitude and Fourier bandwidth. AF-182 shows that **source complexity itself is a third recovery coordinate**. Even at fixed log-scale and with positive sources, matched multi-generator clusters can cancel the first `m-1` responses of the Euler kernel while staying `W1`-separated at order `delta`.

This gives a sharper audit rule for compression chains. It is not enough to ask whether a representation is injective, whether its left edge approaches the convergence boundary, or whether bandwidth resolves one pair of nearby log-frequencies. A stable inverse claim must also state what prevents **high-order matched clusters** from producing arbitrarily flat output directions. Natural gates include minimum separation, bounded cluster cardinality/multiplicity, retained marking or provenance, or an observation family whose effective bandwidth/derivative access scales with cluster complexity.

The line-level lesson is therefore stronger than ordinary pairwise super-resolution: **when a compression kernel is smooth in the source coordinate, positivity alone does not prevent high-order cancellation between two positive matched objects. Complexity restrictions are part of fidelity.**