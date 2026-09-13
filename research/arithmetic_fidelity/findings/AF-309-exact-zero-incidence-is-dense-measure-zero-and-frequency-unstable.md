# AF-309 — Exact-zero incidence is dense, measure-zero, and frequency-unstable

**Status:** `EXACT-DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-308 proves that for `k>=3` the exact-zero frequency incidence set

\[
E_k
=\left\{\nu\in\mathbb R^{k-1}:
\frac1k\left(1+\sum_{j=1}^{k-1}e^{-it\nu_j}\right)=0
\text{ for some }t\ne0\right\}
\]

has Hausdorff dimension at most `k-2` and hence Lebesgue measure zero in `\mathbb R^{k-1}`. The same cone description used there gives a complementary topological fact:

\[
\boxed{\overline{E_k}=\mathbb R^{k-1}\qquad(k\ge3).}
\]

Therefore both `E_k` and its complement are dense. Equivalently,

\[
\boxed{\partial E_k=\mathbb R^{k-1}.}
\]

Thus the binary predicate “this frequency vector has an exact imaginary-axis zero” is discontinuous at **every** frequency vector once `k>=3`. In particular, even if a special arithmetic vector is later proved zero-free, no open ambient neighborhood around that vector can inherit the same exact-zero verdict.

For rational-prime supports this strengthens the AF-307--AF-308 audit. Prime-log difference vectors are rationally independent and therefore have zero stable value margin, but exact membership in `E_k` remains an arithmetic incidence question. The present result shows that this question also has **zero ambient frequency margin**: exact-hit and exact-safe frequency systems occur arbitrarily close to every prime-log vector.

This does not decide whether a given prime-log vector belongs to `E_k`. It shows that any such decision must use exact arithmetic structure rather than a perturbatively stable property of the surrounding frequency geometry.

## Density follows from one lifted polygon configuration

Set

\[
d=k-1\ge2.
\]

AF-308 defines the normalized equilateral-polygon zero locus

\[
M_k
=\left\{(z_1,\ldots,z_d)\in(S^1)^d:
1+\sum_{j=1}^d z_j=0\right\}
\]

and its full angle lift

\[
\widetilde M_k
=\left\{x\in\mathbb R^d:
(e^{-ix_1},\ldots,e^{-ix_d})\in M_k\right\}.
\]

It also proves the exact cone representation

\[
E_k
=\{r x:x\in\widetilde M_k,\ r\in\mathbb R\setminus\{0\}\}.
\tag{1}
\]

Choose any one point `theta in \widetilde M_k`; nonemptiness follows, for example, from a regular `k`-gon zero configuration. Periodicity of the covering map gives

\[
\theta+2\pi n\in\widetilde M_k
\qquad\text{for every }n\in\mathbb Z^d.
\tag{2}
\]

Hence `E_k` contains the union of all lines through the affine lattice `theta+2 pi Z^d`.

Fix a unit vector `u in S^{d-1}`. For each positive integer `N`, choose `n_N in Z^d` by coordinatewise rounding so that

\[
\|2\pi n_N-Nu\|_\infty\le\pi.
\tag{3}
\]

Then

\[
\frac{\theta+2\pi n_N}{N}\longrightarrow u,
\]

and consequently

\[
\frac{\theta+2\pi n_N}{\|\theta+2\pi n_N\|}
\longrightarrow u.
\tag{4}
\]

Thus the directions of the lifted affine lattice are dense on `S^{d-1}`. Because (1) contains every nonzero radial rescaling of those lifted points, every nonzero `nu in R^d` is the limit of vectors in `E_k`: choose directions as in (4) and rescale each one to radius `||nu||`. The origin is also in the closure by taking any fixed hit vector and letting the radial factor tend to zero.

Therefore

\[
\overline{E_k}=\mathbb R^d.
\tag{5}
\]

No equidistribution theorem is needed for this density statement. It is already forced by the `2 pi Z^d` deck transformations of the phase covering together with the free hit-time scale.

## Measure zero plus density makes the exact predicate everywhere unstable

AF-308 gives

\[
\operatorname{Leb}_d(E_k)=0
\qquad(k\ge3).
\tag{6}
\]

Every nonempty Euclidean ball has positive `d`-dimensional Lebesgue measure, so no ball can be contained in `E_k`. Hence the complement

\[
\mathbb R^d\setminus E_k
\]

is dense. Combining this with (5), every neighborhood of every frequency vector contains both an exact-hit vector and an exact-safe vector.

If

\[
\chi_k(\nu)=\mathbf 1_{E_k}(\nu),
\]

then `chi_k` is discontinuous everywhere. More quantitatively, both one-sided frequency-space margins vanish:

\[
\operatorname{dist}(\nu,E_k)=0
\qquad\text{for every }\nu,
\tag{7}
\]

and, for `nu in E_k`,

\[
\operatorname{dist}(\nu,\mathbb R^d\setminus E_k)=0.
\tag{8}
\]

For `nu notin E_k`, the second distance is already zero trivially. Thus there is no positive Euclidean conditioning radius for either exact-zero or exact-zero-free classification anywhere in frequency space.

This frequency instability is distinct from AF-306--AF-308's **value margin**

\[
\inf_t |F_\nu(t)|.
\]

A vector can fail to hit zero exactly while having value margin zero because its orbit approaches the phase-zero locus; AF-309 adds that the vector itself is also arbitrarily close to other frequency systems whose orbit does hit zero exactly.

## Consequence for rational-prime frequency vectors

For distinct primes `p_1,...,p_k`, AF-308 uses

\[
\nu^{(p)}_j=\log(p_j/p_k),
\qquad 1\le j<k.
\]

Unique factorization makes these differences linearly independent over `Q`, so Kronecker-Weyl already gives

\[
\inf_t |F_{\nu^{(p)}}(t)|=0.
\]

For `k=3,4`, AF-307 proves the stronger exact arithmetic statement

\[
\nu^{(p)}\notin E_k.
\]

AF-309 shows that this zero-free conclusion has no open extension in the ambient frequency space: for every `epsilon>0` there is a frequency vector `nu'` with

\[
\|\nu'-\nu^{(p)}\|<\epsilon,
\qquad
\nu'\in E_k.
\]

For `k>=5`, where exact prime incidence remains unresolved, the same statement rules out a whole proof style. One cannot prove prime-log nonmembership in `E_k` by establishing any property that merely persists on an ambient open neighborhood and excludes all exact-hit vectors, because no such neighborhood exists. A successful obstruction has to see the exact arithmetic placement of the prime-log vector inside this dense exceptional geometry.

Conversely, near-zero numerics or arbitrarily accurate perturbative models cannot certify membership either: exact-safe vectors are dense as well. The problem is genuinely exact in both directions.

## Prior art and novelty assessment

No novelty claim is made for the general ingredients.

AF-308 already records the classical equilateral-polygon-space description of `M_k`, the covering-space lift `\widetilde M_k`, semialgebraic dimension theory, and the exponential-sum/Kronecker-Weyl literature relevant to exact versus closure-based zero questions. The new step here is an elementary consequence of that representation: one lifted zero configuration produces the affine lattice `theta+2 pi Z^d`, whose directions are dense after radial rescaling.

A targeted literature search found the established exponential-polynomial and Dirichlet-polynomial literature on zero closures and frequency dependence, but no reason to present the affine-lattice density observation as a novel theorem. Its durable role is the Arithmetic Fidelity classification: the exact-zero incidence set is simultaneously negligible in measure and maximally non-separated topologically.

In particular, this should be read as a structural consequence of AF-308 rather than as a new branch of exponential-polynomial theory.

## Boundaries and failure modes

- Density is in the ambient continuous frequency-difference space `R^{k-1}`. The nearby exact-hit vectors constructed above need not themselves be logarithms of rational-prime ratios or belong to any other discrete arithmetic source family.
- Therefore (5) does **not** prove or disprove exact zeros for any fixed prime support, nor does it compare two nearby prime supports in a metric on primes.
- The argument uses the free hit-time scaling in the definition of `E_k`. If time is restricted to a bounded interval or fixed in advance, the incidence geometry changes and the density statement need not hold.
- The conclusion concerns equal weights on the imaginary axis. Unequal coefficients, nonzero real part, repeated frequencies, or vector-valued observations require their own incidence sets.
- Measure zero does not imply category-smallness by itself; density does not imply large measure. The point is precisely that these two notions of genericity disagree here.
- The constructed dense subset may use highly commensurate lifted directions. The theorem does not assert that exact-hit vectors with rationally independent coordinates are dense, or even classify their existence for each `k`.
- Frequency-space instability and value-space instability are separate. Neither one alone decides the arithmetic incidence question.
- Nothing here supplies a zeta zero count, analytic continuation, a Riemann-zero divisor, or an RH implication.

## Consequence for the research line

The saturated exact-zero frontier now has three distinct layers:

1. **value accessibility:** rationally independent prime-log flows approach zero arbitrarily closely;
2. **ambient incidence conditioning:** exact-hit and exact-safe frequency systems are both dense, so the binary exact-zero predicate has zero frequency margin everywhere;
3. **arithmetic incidence:** whether the special prime-log vector itself belongs to the exact-hit set remains a separate exact question.

AF-308 showed that the third layer lies in a measure-zero exceptional set. AF-309 shows that the same exceptional set is dense, so generic measure arguments, perturbative continuity arguments, and numerical proximity all fail in complementary ways. For the unresolved `k>=5` prime-support problem, the next useful theorem must therefore exploit exact arithmetic structure of the logarithmic frequency vector or change the observation class; more ambient topology cannot separate the prime point from the exact-hit set.