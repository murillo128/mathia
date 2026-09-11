# AF-275 — Finite right-half-plane samples leave exact far-prime Euler fibers

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `ARITHMETIC-FIDELITY`, `EULER-GLOBAL`, `FINITE-SAMPLING`, `PRIME-BREADTH`, `POINT-FIBER`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-274 shows that bounded local Euler degree removes the unbounded prime-power-depth escape: in degree one, one exact coefficient at each prime determines the whole local ray. The remaining bill is prime breadth. A finite list of exact global values does **not** compress that infinite breadth away, even when every prime location stays equal to an ordinary rational prime and every changed local factor remains degree one.

Fix distinct real sample points

\[
1<\sigma_1<\cdots<\sigma_m,
\qquad m\ge1,
\tag{1}
\]

and an arbitrary prime cutoff `P_0`. Then there exist `N=m+1` distinct rational primes

\[
q_1,\ldots,q_N>P_0
\tag{2}
\]

with the following property. For real parameters `a=(a_1,\ldots,a_N)` in a sufficiently small neighborhood of

\[
\mathbf 1=(1,\ldots,1),
\tag{3}
\]

define

\[
Z_a(s)
:=\zeta(s)
\prod_{\ell=1}^{N}
\frac{1-q_\ell^{-s}}
{1-a_\ell q_\ell^{-s}}.
\tag{4}
\]

Equivalently, `Z_a` has the degree-one Euler product

\[
Z_a(s)
=\prod_p(1-\alpha_p(a)p^{-s})^{-1},
\tag{5}
\]

where

\[
\alpha_p(a)=1
\quad(p\notin\{q_1,\ldots,q_N\}),
\qquad
\alpha_{q_\ell}(a)=a_\ell.
\tag{6}
\]

After shrinking the parameter neighborhood so that every `a_\ell>0` and `a_\ell<q_\ell`, the products are holomorphic and nonzero on `Re(s)>1`. Then:

1. **The exact finite-sample fiber through `zeta` is nontrivial.** There is a smooth one-dimensional manifold through `\mathbf1` on which
   \[
   \boxed{
   Z_a(\sigma_j)=\zeta(\sigma_j)
   \qquad(1\le j\le m).
   }
   \tag{7}
   \]
   Hence every neighborhood of `\mathbf1` contains `a\ne\mathbf1` satisfying all `m` exact equalities.

2. **The collision can be pushed arbitrarily far into the prime tail.** The cutoff `P_0` is arbitrary. Thus the competing Euler product can agree with `zeta` at every local factor below any prescribed prime bound while still matching all retained global sample values exactly.

3. **The controls preserve rational-prime locations and local degree one.** No Beurling prime is moved and no higher-degree local polynomial is introduced. The only changed data are finitely many degree-one local parameters attached to ordinary rational primes beyond `P_0`.

4. **The colliding source is genuinely different.** If `a\ne\mathbf1`, then `Z_a` is not the same analytic function as `zeta`; at least one local coefficient has changed. The equalities in `(7)` are finite-sampling collisions, not a reparameterization of one Euler product.

5. More generally, after choosing any `N>m` primes containing an `m`-prime full-rank block constructed below, the same level set through `\mathbf1` has local dimension `N-m`.

Therefore bounded local Euler degree plus exact rational-prime support does not turn finitely many global right-half-plane values into a faithful certificate. **Finite scalar sampling can mix information from all primes and still leave an exact positive-dimensional tail fiber through the Riemann-zeta source point.**

## Exact derivation

### 1. Use the positive real logarithm of the finite Euler-factor ratio

For `\sigma>1`, `\zeta(\sigma)>0`. In a sufficiently small positive neighborhood of `\mathbf1`, every factor in `(4)` is also positive at each `\sigma_j`. Equality of sampled values is therefore equivalent to equality of their real logarithms.

Define

\[
F:\mathbb R^N\supset U\longrightarrow\mathbb R^m
\tag{8}
\]

by

\[
F_j(a)
:=\log\frac{Z_a(\sigma_j)}{\zeta(\sigma_j)}
=\sum_{\ell=1}^{N}
\left[
\log(1-q_\ell^{-\sigma_j})
-\log(1-a_\ell q_\ell^{-\sigma_j})
\right].
\tag{9}
\]

Then

\[
F(\mathbf1)=0,
\tag{10}
\]

and direct differentiation gives

\[
\frac{\partial F_j}{\partial a_\ell}(\mathbf1)
=
\frac{q_\ell^{-\sigma_j}}
{1-q_\ell^{-\sigma_j}}
=
\boxed{
\frac1{q_\ell^{\sigma_j}-1}
}.
\tag{11}
\]

Thus exact pointwise fidelity is governed by the real `m\times N` matrix

\[
J_{j\ell}
=\frac1{q_\ell^{\sigma_j}-1}.
\tag{12}
\]

The only remaining question is whether one can force full row rank using primes arbitrarily far out.

### 2. The Euler-sampling response functions are linearly independent on every prime tail

For the ordered samples `(1)`, define on primes

\[
f_j(q):=\frac1{q^{\sigma_j}-1}.
\tag{13}
\]

Fix any cutoff `P_0`. We claim that the restrictions of

\[
f_1,\ldots,f_m
\tag{14}
\]

to the infinite set of primes `q>P_0` are linearly independent over `\mathbb R`.

Suppose instead that

\[
\sum_{j=1}^{m}c_j f_j(q)=0
\tag{15}
\]

for every prime `q>P_0`, with some coefficients not all zero. Let `j_*` be the smallest index for which `c_{j_*}\ne0`. Since the `\sigma_j` are strictly increasing, multiplication by `q^{\sigma_{j_*}}` gives, along primes tending to infinity,

\[
q^{\sigma_{j_*}}
\sum_{j=1}^{m}
\frac{c_j}{q^{\sigma_j}-1}
\longrightarrow c_{j_*}.
\tag{16}
\]

Indeed the `j_*` term tends to `c_{j_*}`, every earlier coefficient is zero by definition, and every later term tends to zero because `\sigma_j>\sigma_{j_*}`. But the left side of `(16)` is identically zero on all sufficiently large primes by `(15)`, so its limit must be zero. This contradicts `c_{j_*}\ne0`.

Hence the response functions are linearly independent on **every** prime tail.

A standard evaluation lemma now finishes the rank step: if `m` functions are linearly independent on a set `S`, their evaluation vectors span `\mathbb R^m`; otherwise a nonzero vector orthogonal to that span would give a nontrivial linear relation among the functions on all of `S`. Therefore there exist distinct primes

\[
q_1,\ldots,q_m>P_0
\tag{17}
\]

for which

\[
\det
\left[
\frac1{q_\ell^{\sigma_j}-1}
\right]_{1\le j,\ell\le m}
\ne0.
\tag{18}
\]

Choose any additional prime `q_{m+1}>P_0` distinct from these. The full Jacobian `(12)` then has rank exactly `m`.

This argument needs no prime-distribution estimate beyond the infinitude of primes. The asymptotic hierarchy `q^{-\sigma_1}\gg\cdots\gg q^{-\sigma_m}` is already enough to prevent a common linear dependence on an unbounded prime tail.

### 3. Full row rank forces an exact same-sample curve through `zeta`

Because the `m\times m` minor `(18)` is nonzero at `\mathbf1`, it remains nonzero in a sufficiently small parameter neighborhood. Thus `F` is a submersion near `\mathbf1`.

The regular-level-set / implicit-function theorem gives

\[
F^{-1}(0)
\tag{19}
\]

as a smooth submanifold near `\mathbf1` of dimension

\[
N-m=(m+1)-m=1.
\tag{20}
\]

Consequently there is a nonconstant smooth curve

\[
a(t),
\qquad
a(0)=\mathbf1,
\tag{21}
\]

with

\[
F(a(t))=0
\tag{22}
\]

for all sufficiently small `t`. Equations `(9)` and `(22)` are exactly the sample equalities `(7)`.

Shrinking the curve if necessary keeps every coordinate positive and below its prime `q_\ell`. Hence each modified factor remains a valid degree-one geometric Euler factor with no pole in `Re(s)>1`, and the product differs from `zeta` at only finitely many factors.

For `N>m`, the same argument yields a local fiber dimension `N-m` as soon as the selected prime block contains the full-rank `m\times m` minor from `(18)`.

### 4. Nontrivial parameters really change the Euler source

Suppose `a\ne\mathbf1`. Let `q_*` be the smallest selected prime with

\[
a_{q_*}\ne1.
\tag{23}
\]

The Euler product `(5)` is the Dirichlet series of the completely multiplicative coefficient law determined by

\[
\alpha_p(a).
\tag{24}
\]

At the prime index `q_*`, the coefficient of `q_*^{-s}` is exactly `a_{q_*}` rather than `1`. Thus `Z_a` and `\zeta` have different Dirichlet coefficients in their common absolute-convergence half-plane and cannot be the same analytic function.

Equivalently, in the finite ratio in `(4)`, the first changed prime supplies the leading nonzero exponential term as real `s\to+\infty`; it cannot be cancelled identically by factors at distinct larger primes.

So the point-fiber consists of genuine distinct arithmetic sources that coincide only after the declared finite sampling compression.

## Relation to AF-274: finite local depth does not imply finite global sample complexity

AF-274 identifies a sharp positive result. In a degree-`d` local Euler category, the first `d` prime-power moments determine one local factor. For `zeta`, `d=1`, so one coefficient at each prime determines the whole local ray.

The unresolved issue was whether a small number of **global** analytic observations might combine infinitely many local coordinates so efficiently that the separate prime-breadth bill disappears.

AF-275 gives a negative answer for finite real value sampling in `Re(s)>1`. Even with:

- exact rational-prime locations;
- degree-one local factors at every prime;
- all local factors below an arbitrary cutoff fixed exactly to the zeta factors;
- exact infinite-precision values at every retained sample point;

the sample map still has a nontrivial smooth fiber through `zeta`.

Thus the information boundary after AF-274 is sharper than merely

\[
\text{finite inspected prime set}
\not\Rightarrow
\text{global Euler fidelity}.
\tag{25}
\]

It is already

\[
\boxed{
\text{finite exact global value samples}
\not\Rightarrow
\text{global degree-one Euler fidelity}.
}
\tag{26}
\]

The destination can mix contributions from every prime and still fail to identify the infinitely many local coordinates.

## Relation to AF-023: the regular-fiber obstruction is now source-specific and unconditional

AF-023 proved a general regular-point statement for finite Weil-test maps on continuously deformable Beurling generator norms. Its point-fiber conclusion required a Jacobian full-rank hypothesis, and the source deformation moved generalized-prime locations.

Here the same classical differential mechanism is specialized more tightly:

- the prime locations remain the ordinary rational primes;
- the varying coordinates are degree-one local Euler parameters;
- the retained outputs are actual values of the resulting Euler product at prescribed real points `\sigma_j>1`;
- the full-rank block is **proved to exist for every finite distinct sample set and beyond every prime cutoff**.

So no generic-test assumption remains in this finite-sampling category. The zeta point itself is regular after selecting a suitable far-prime block, and therefore lies on an exact collision fiber.

This does not subsume AF-023, whose source category and retained tests are different. It supplies the missing concrete cross-prime breadth audit suggested by AF-274.

## Relation to AF-017: full analytic data and finite samples are different fidelity layers

AF-017 shows that an exact Euler-product function on its convergence half-plane is a highly faithful object: in its generator-norm model, the full function recovers the prime sum and hence the generator multiset. The present result shows that **finitely many values of such a function are categorically weaker than the function itself**.

There is no contradiction. Equality on an open set, or on an infinite set with an accumulation point inside a common analytic domain, invokes analytic rigidity and can determine the whole function. Equality at finitely many isolated real points has no such consequence.

Within `(5)`, once the whole Dirichlet series is known in `Re(s)>1`, its coefficients recover each local parameter `\alpha_p`. AF-275 instead proves that any fixed finite sample set leaves coordinated far-prime perturbations exactly invisible.

This gives a useful three-layer distinction:

\[
\text{all local factors}
\longrightarrow
\text{full analytic Euler-product function}
\longrightarrow
\text{finite value samples}.
\tag{27}
\]

The first two layers can be faithful under suitable source assumptions; the last is not faithful on the degree-one coefficient family studied here.

## Prior art and novelty assessment

Every ingredient used in the proof is classical.

- The Euler-product representation for Dirichlet series of completely multiplicative functions is standard; NIST DLMF §27.4 records that in an absolute-convergence region a completely multiplicative coefficient law has geometric local factors `\prod_p(1-f(p)p^{-s})^{-1}`, citing classical sources including Apostol and Titchmarsh.
- The regular-level-set / implicit-function theorem used to turn full Jacobian rank into an exact positive-dimensional fiber is standard differential topology; John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2012), is already the line's source for this mechanism in AF-007 and AF-023.
- Finite-dimensional interpolation and universality theories for Dirichlet series and Euler products are broad established subjects, but the present proof does not need a universality theorem. It is a local finite-dimensional rank argument inside a finitely perturbed Euler-product family.

A targeted literature search did not change this classification: the nearby literature concerns standard Euler-product factorization, finite Euler-product approximation, Dirichlet-series universality/interpolation, and multiplicative-function rigidity, while the theorem above follows directly from the elementary Jacobian `(12)` plus the regular-level-set theorem. No broad novelty is claimed for Euler products, implicit-function methods, or finite-sample non-identifiability.

The Arithmetic Fidelity contribution is the **boundary placement after AF-274**: bounded local degree solves prime-power depth but not prime breadth, and finitely many exact global values do not remove that breadth obstruction even at the `zeta` point and even when all changed factors stay on ordinary rational-prime locations.

## Boundaries and failure modes

- The retained observations are finitely many **real values** at distinct `\sigma_j>1`. Complex samples contribute two real constraints each in general; an analogous complex-parameter statement is plausible but is not proved here.
- The theorem varies real positive local parameters `a_\ell` near `1`. It preserves rational-prime locations and local degree one, but it does **not** preserve the stricter condition `|a_\ell|=1`, the exact zeta coefficient law `a_\ell=1`, automorphy, a functional equation, analytic continuation to the critical strip, or another global `L`-function axiom system.
- In particular, a route that independently proves a rigid cross-prime relation among local parameters may evade this deformation family. Such a relation is precisely the additional information that must be exhibited rather than assumed.
- Only finitely many local factors are changed in each control. The theorem does not construct an infinite-tail perturbation.
- The changed primes can lie beyond every prescribed cutoff, but the corresponding Jacobian entries become small. The result is **exact fidelity failure**, not a uniform conditioning statement. As the perturbation block moves outward, maintaining a useful finite-precision deformation may become increasingly ill-conditioned.
- Equality at finitely many points must not be conflated with equality of the analytic function. An infinite sample set with an interior accumulation point is subject to the identity theorem and lies in a different destination category.
- The theorem does not say that a finite collection of zeros, spectral invariants, explicit-formula tests, or nonlinear global constraints behaves identically to value sampling. Each destination requires its own Jacobian/fiber audit.
- The construction has no direct implication for the truth or falsity of RH.

## Decisive audit test

For any proposed RH-facing compression that replaces Euler/local-factor data by finitely many scalar analytic observations, first identify the actual admissible local-parameter class. If that class contains independent degree-one perturbations at arbitrarily large rational primes, then:

1. write the exact finite observation map on a finite block of prime-local parameters;
2. compute its Jacobian at the zeta source point;
3. include more perturbable prime coordinates than effective real outputs;
4. test whether a full-row-rank block exists arbitrarily far in the prime tail;
5. if it does, the regular-level-set theorem produces an exact same-destination manifold through the source point;
6. if the route claims fidelity anyway, identify the extra global constraint that forbids those local directions and prove that it is retained by the compression;
7. audit exact fidelity and finite-precision conditioning separately.

For ordinary real value sampling in `Re(s)>1`, steps 1–5 are settled by `(9)`–`(20)`: the necessary full-rank block exists beyond every prime cutoff.

## Consequence for the research line

AF-273 and AF-274 separated **local depth** from **global breadth**. AF-275 now rules out the most direct finite-dimensional shortcut for the breadth side: replacing infinitely many degree-one local coordinates by finitely many exact right-half-plane function values does not identify the zeta source, even locally.

The live gate therefore moves to genuinely **cross-prime rigidity**. A finite-dimensional RH-facing object can overcome the prime-breadth obstruction only if its admissible source category couples the prime-local parameters strongly enough that the independent tail directions used here are not available, or if the retained destination carries richer-than-finite-sample analytic structure that reconstructs those directions.

Useful next targets are consequently not more isolated value samples. They are theorem-level audits of which natural zeta/L-function structures — functional equation, Euler-category constraints, growth/order, positivity, automorphic or cohomological coupling, or another intrinsic global law — actually reduce the independent prime-breadth degrees of freedom rather than merely evaluate them at finitely many points.