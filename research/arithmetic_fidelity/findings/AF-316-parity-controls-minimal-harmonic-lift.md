# AF-316 — Parity controls the minimal harmonic lift of centered unit-circle configurations

**Status:** `EXACT-DERIVED`, `STRUCTURAL-RECOVERY`, `DIMENSION-TIGHT`, `CLASSICAL-IDENTITY+DERIVED`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
Z=\{z_1,\ldots,z_n\}\subset \mathbb S^1
\]

be an unordered multiset, allowing multiplicity, with power sums

\[
s_r(Z)=\sum_{j=1}^n z_j^r
\]

and assume the centered condition

\[
s_1(Z)=0.
\tag{1}
\]

Write

\[
P_Z(w)=\prod_{j=1}^n(w-z_j)
      =\sum_{k=0}^n(-1)^k e_k w^{n-k},
\qquad
E=e_n=\prod_{j=1}^n z_j\in\mathbb S^1.
\tag{2}
\]

Then the amount of low-harmonic data needed for exact recovery obeys a parity law.

### Odd support: one real phase lift is exactly the missing generic degree

Let `n=2m+1`, `m>=2`. Then

\[
\boxed{
\bigl(s_2,\ldots,s_m,E\bigr)
}
\tag{3}
\]

determines the complete unordered multiset `Z` for **every** centered unit-circle configuration.

The representation `(3)` has

\[
2(m-1)+1=2m-1=n-2
\tag{4}
\]

real coordinates. The smooth noncollinear centered configuration space has generic real dimension `n-2`, so no continuous faithful representation into fewer real coordinates can exist on a generic open patch. In particular, the lower-harmonic block

\[
(s_2,\ldots,s_m)
\tag{5}
\]

is generically short by exactly one real degree, and the product phase `E in S^1` is a dimension-minimal lift.

There is also a purely harmonic version. On the stratum `e_m ne 0`,

\[
\boxed{
\bigl(s_2,\ldots,s_{m+1}\bigr)
}
\tag{6}
\]

recovers `Z`, because the last harmonic supplies the missing product phase. Its apparent `2m` real coordinates contain one exact redundancy,

\[
|e_{m+1}|=|e_m|,
\tag{7}
\]

so its realized image again has generic dimension `2m-1=n-2`.

### Even support: the middle harmonic generically carries the phase itself

Let `n=2m`, `m>=2`. On the stratum

\[
e_m\ne0,
\tag{8}
\]

the low-harmonic block

\[
\boxed{
\bigl(s_2,\ldots,s_m\bigr)
}
\tag{9}
\]

determines the complete unordered multiset `Z`.

It has

\[
2(m-1)=2m-2=n-2
\tag{10}
\]

real coordinates, exactly the generic dimension of the centered configuration space. Thus `(9)` is dimension-tight on its faithful stratum.

The exceptional set `e_m=0` is structurally different: the middle self-inversive relation becomes `0=E\overline 0` and no longer determines the product phase. Adding `E` always restores exact recovery, but no claim is made here that this extra phase is minimal on every singular stratum.

### Shape modulo common phase

Common rotation `Z -> rho Z`, `|rho|=1`, acts by

\[
s_r\mapsto \rho^r s_r,
\qquad
E\mapsto \rho^n E.
\tag{11}
\]

Therefore the exact representations above descend to complete weighted-orbit representations of the unordered shape modulo common phase. On the generic free locus the shape space has real dimension

\[
n-3,
\tag{12}
\]

and the corresponding quotient of `(3)` or `(9)` has exactly that dimension. Hence the earlier five- and six-point thresholds are the first cases of a general parity-controlled information law rather than isolated coincidences.

## Derivation

### 1. Unit-circle roots halve the polynomial coefficients

For every `0<=k<=n`, complementing a `k`-element subset in the product of all roots gives

\[
\boxed{
e_{n-k}=E\,\overline{e_k}.
}
\tag{13}
\]

This is the standard coefficient symmetry of a monic polynomial whose roots all lie on the unit circle. The centering condition `(1)` gives

\[
e_1=s_1=0,
\qquad
e_{n-1}=E\overline{e_1}=0.
\tag{14}
\]

Newton's identities recursively recover `e_k` from the first `k` power sums:

\[
k e_k
=\sum_{r=1}^k(-1)^{r-1}e_{k-r}s_r,
\qquad e_0=1.
\tag{15}
\]

Since `s_1=0`, the block `s_2,...,s_q` determines `e_2,...,e_q` exactly.

### 2. Odd degree has no self-paired middle coefficient

Take `n=2m+1`. From `(15)`, `s_2,...,s_m` determine

\[
e_2,\ldots,e_m.
\tag{16}
\]

If `E` is retained, `(13)` immediately gives

\[
e_{2m+1-k}=E\overline{e_k}
\qquad(0\le k\le m),
\tag{17}
\]

which supplies every coefficient from `e_{m+1}` through `e_{2m+1}`. Together with `e_1=0`, all coefficients of `P_Z` are known, so its unordered root multiset is known. This proves global exact recovery by `(3)` without any nondegeneracy assumption.

If one insists on harmonics only, Newton's identities also recover `e_{m+1}` from `s_2,...,s_{m+1}`. Equation `(13)` at the central pair says

\[
e_{m+1}=E\overline{e_m}.
\tag{18}
\]

When `e_m ne0`,

\[
\boxed{
E=\frac{e_{m+1}}{\overline{e_m}},
}
\tag{19}
\]

and `(17)` again reconstructs the polynomial. Taking moduli in `(18)` gives the exact real consistency relation `(7)`.

Thus odd support has a genuine one-real-degree phase deficit if only harmonics through order `m` are retained. The next harmonic can encode that phase, but it necessarily carries one redundant magnitude relation on the unit-circle image.

### 3. Even degree has a self-paired middle coefficient

Take `n=2m`. Newton's identities recover

\[
e_2,\ldots,e_m
\tag{20}
\]

from `s_2,...,s_m`. The central self-inversive relation is now

\[
e_m=E\overline{e_m}.
\tag{21}
\]

When `e_m ne0`, the product phase is already encoded by that single middle coefficient:

\[
\boxed{
E=\frac{e_m}{\overline{e_m}}.
}
\tag{22}
\]

Equation `(13)` then gives every upper coefficient, so `(9)` reconstructs `P_Z` and therefore `Z`.

When `e_m=0`, equation `(21)` becomes vacuous with respect to `E`. This is exactly the singular mechanism already visible at six points in AF-315: low harmonics can remain highly informative while the self-inversive phase closure loses one constraint on the exceptional middle-coefficient zero set.

### 4. The coordinate counts are sharp on generic patches

Write `z_j=e^{i\theta_j}` and consider

\[
\Sigma:(S^1)^n\to\mathbb C,
\qquad
\Sigma(z)=\sum_j z_j.
\tag{23}
\]

At a centered configuration,

\[
D\Sigma(\dot\theta_1,\ldots,\dot\theta_n)
=i\sum_j z_j\dot\theta_j.
\tag{24}
\]

Its real rank is `2` unless all `z_j` lie on one real line through the origin. Hence away from the collinear locus the centered ordered configuration space is a smooth real manifold of dimension

\[
n-2.
\tag{25}
\]

Passing to unordered configurations is only a finite quotient on a generic patch and does not change local dimension. A continuous injection from an open subset of an `(n-2)`-manifold into `R^q` with `q<n-2` is impossible by invariance of domain after composing with the standard inclusion `R^q -> R^{n-2}`.

For odd `n=2m+1`, `(s_2,...,s_m)` has only `2m-2=n-3` real coordinates, so it cannot be generically faithful; one additional real coordinate is necessary. The lift `E in S^1` attains that lower bound exactly.

For even `n=2m`, `(s_2,...,s_m)` has `2m-2=n-2` real coordinates and is already exactly faithful on `e_m ne0`, so it attains the generic lower bound.

Quotienting the free common-rotation action removes one further real dimension, giving `(12)` and the corresponding sharp lower bound for continuous shape summaries.

## Arithmetic specialization

Let `p_1,...,p_n` be distinct rational primes and

\[
F_P(t)=\sum_{j=1}^n p_j^{-it}.
\tag{26}
\]

At a hypothetical nonzero exact hit `F_P(t)=0`, set `z_j=p_j^{-it}`. Then

\[
s_r=F_P(rt),
\qquad
E=\left(\prod_{j=1}^n p_j\right)^{-it}.
\tag{27}
\]

For **odd** support `n=2m+1`, the exact global recovery statement becomes

\[
\boxed{
\left(
F_P(2t),\ldots,F_P(mt),
\left(\prod_{j=1}^n p_j\right)^{-it}
\right)
}
\tag{28}
\]

which recovers the complete unordered phase multiset for every hypothetical hit, with no torsion or middle-coefficient exception. Generically the product phase is exactly the one real lift missing from the lower harmonic block.

For **even** support `n=2m`,

\[
\boxed{
\bigl(F_P(2t),\ldots,F_P(mt)\bigr)
}
\tag{29}
\]

recovers the phase multiset whenever the associated middle coefficient `e_m` is nonzero. AF-315 proves this nondegeneracy automatically for the six-prime case by excluding both relevant torsion geometries. No corresponding all-even-support prime theorem is proved here; for `n>=8`, the possibility `e_m=0` remains a separate arithmetic incidence question.

The specialization therefore identifies an exact representation cost **conditional on incidence**. It does not decide whether any such prime-log orbit meets the centered zero fiber.

## Fidelity interpretation

AF-313 and AF-315 could look like unrelated low-dimensional accidents: five points needed two harmonics with one real redundancy, while six points needed the same two harmonics but a three-real shape quotient. The parity theorem explains both from the same self-inversive closure mechanism.

For odd support there is no coefficient paired with itself under `k -> n-k`. The lower half of the polynomial therefore misses one circle-valued global phase, and `E` is a minimal exact lift. For even support the middle coefficient is self-paired; away from its zero set, its phase closes the polynomial automatically. **The information bill is controlled not by “number of harmonics” alone but by whether the involutive coefficient pairing has a fixed point.**

This is a reusable Arithmetic Fidelity mechanism: a symmetry can cut the apparent reconstruction budget roughly in half, but parity determines whether the symmetry itself leaves a residual global gauge variable. The result also separates exact recovery from conditioning; nothing here gives a uniform modulus near the singular middle-coefficient set.

## Prior art and novelty assessment

The mathematical ingredients are classical and no novelty claim is made. Newton identities are the standard bridge from power sums to elementary symmetric coefficients. The coefficient relation `(13)` is the standard self-inversive symmetry for unit-circle root polynomials; direct references include Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, Cambridge University Press (2010), pp. 312–321, DOI `10.1017/CBO9780511721274.020`, and Andrzej Schinzel, **“Self-Inversive Polynomials with All Zeros on the Unit Circle,”** *The Ramanujan Journal* 9 (2005), 19–23, DOI `10.1007/s11139-005-0821-9`.

Finite reconstruction from moments is classical Prony/trigonometric-moment theory; Stefan Kunis, Thomas Peter, Tim Roemer, and Ulrich von der Ohe, **“A multivariate generalization of Prony's method,”** *Linear Algebra and its Applications* 490 (2016), 31–47, DOI `10.1016/j.laa.2015.10.023`, is a modern reference for finite-support moment reconstruction.

A targeted literature search found the classical ingredients and broader finite-moment reconstruction theory, but not a named result packaging the centered equal-weight unit-circle case into this exact odd/even minimal-lift statement. The present result should therefore be read as an elementary synthesis and specialization of classical structures, not as a claim of a new general theorem.

## Boundaries and falsification checks

- Recovery is of the **unordered multiset** of phases, not a labeling that identifies which recovered phase belongs to which prime.
- The theorem assumes exact unit modulus and exact centering `s_1=0`. Unequal weights, off-circle roots, approximate cancellation, and noisy harmonics require a separate stability analysis.
- The odd representation `(s_2,...,s_m,E)` is globally sufficient and generically dimension-minimal; this does not say that `E` is the only possible one-real lift.
- The purely harmonic odd representation `(s_2,...,s_{m+1})` is asserted only on `e_m ne0`. On `e_m=0`, equation `(18)` cannot recover `E`.
- The even representation `(s_2,...,s_m)` is asserted only on `e_m ne0`. Adding `E` always repairs exact recovery, but minimality on singular strata is not classified here.
- Dimension lower bounds concern continuous representations on generic smooth patches. They do not rule out discontinuous encodings into fewer coordinates or exploit special lower-dimensional arithmetic subfamilies.
- Exact identifiability does not imply stable recovery. Root collisions or approach to `e_m=0` can make inversion badly conditioned.
- The arithmetic specialization is conditional on a prime-phase exact hit. It provides no first-incidence theorem, zero-selection theorem, critical-line statement, or RH implication.

## Consequences for the line

The five-to-six-point transition now extends to every support size: centered unit-circle reconstruction has a deterministic parity law, and the generic continuous information budget is exactly `n-2` real coordinates before quotienting common phase and `n-3` after quotienting it.

For the current prime-incidence frontier this removes a broad class of post-incidence ambiguity questions. Once a centered hit is given, low harmonics plus at most one explicit product-phase lift reconstruct the complete phase multiset at every support size. The unresolved arithmetic content is therefore pushed more cleanly toward **first incidence, conditioning, and prime-specific accessibility of the required lift**, rather than generic loss of phase geometry after exact cancellation.

For larger odd supports, `(28)` supplies a canonical minimal-lift benchmark against which any purportedly smaller arithmetic summary can be tested. For larger even supports, the next structural question is the arithmetic size and geometry of the singular set `e_m=0`; that question should not be conflated with the generic reconstruction theorem proved here.
