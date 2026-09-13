# AF-315 — Six-point zero shapes need three real harmonic coordinates

**Status:** `EXACT-DERIVED`, `STRUCTURAL-RECOVERY`, `ARITHMETIC-CONTROL`, `DIMENSION-OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-313 and AF-314 show that on the five-point unit-circle zero fiber, two low harmonics recover the full unordered phase multiset and, after quotienting common phase, one complex invariant is enough to recover the shape. The next support size changes the information dimension sharply.

Let

\[
Z=\{z_1,\ldots,z_6\}\subset \mathbb S^1,
\qquad
s_m(Z)=\sum_{j=1}^6 z_j^m,
\]

and restrict to the centered fiber

\[
s_1(Z)=0.
\tag{1}
\]

Then the following hold.

1. **Exact two-harmonic recovery on the open stratum `s_3\ne0`.** The pair `(s_2,s_3)` uniquely determines the unordered multiset `Z`. More explicitly, `Z` is the root multiset of

\[
\boxed{
P_{s_2,s_3}(w)
=
w^6-
\frac{s_2}{2}w^4-
\frac{s_3}{3}w^3-
\frac{s_3\overline{s_2}}{2\overline{s_3}}w^2+
\frac{s_3}{\overline{s_3}}.
}
\tag{2}
\]

2. **A sharp common-phase quotient.** On the same stratum define

\[
\kappa(Z)=\frac{s_2(Z)^3}{s_3(Z)^2},
\qquad
R(Z)=\left(|s_3(Z)|,\kappa(Z)\right)
\in \mathbb R_{>0}\times\mathbb C.
\tag{3}
\]

The map `R` is invariant under common rotation `Z\mapsto\rho Z`, and it is complete: two centered six-point multisets with nonzero `s_3` have the same `R` exactly when they differ by one common rotation.

3. **Three real coordinates are generically necessary.** The smooth noncollinear part of the centered six-point configuration space has real dimension `4`; quotienting common rotation leaves a generic unordered shape space of real dimension `3`. Consequently no continuous invariant with values in one complex scalar can be faithful on any generic open shape patch. The target of `(3)` has exactly three real coordinates, so `R` is dimension-tight on its stratum.

Thus six points are the first centered unit support for which the generic shape quotient cannot be continuously compressed to one complex number. The sharp repair is weaker than “two complex invariants”: **one complex invariant plus one real modulus already suffices.**

4. **Rational-prime exact hits automatically avoid both low-harmonic singularities.** Let `p_1,...,p_6` be distinct rational primes and

\[
F_P(t)=\sum_{j=1}^6p_j^{-it}.
\tag{4}
\]

If `t\ne0` and `F_P(t)=0`, then

\[
\boxed{F_P(2t)\ne0,\qquad F_P(3t)\ne0.}
\tag{5}
\]

Hence every hypothetical six-prime exact hit lies in the faithful stratum of `(2)` and in fact has `\kappa\ne0`. The raw pair

\[
\bigl(F_P(2t),F_P(3t)\bigr)
\tag{6}
\]

recovers the complete unordered phase multiset, while the three-real summary

\[
\boxed{
\left(
|F_P(3t)|,
\frac{F_P(2t)^3}{F_P(3t)^2}
\right)
}
\tag{7}
\]

recovers its unordered shape modulo common phase.

This is a post-incidence recovery theorem, not a first-incidence theorem. It does not decide whether a six-prime zero `(4)` exists.

## Derivation

### 1. Self-inversive coefficients collapse the six-point fiber

Let `e_k=e_k(z_1,...,z_6)` be the elementary symmetric functions and

\[
E=e_6=\prod_{j=1}^6 z_j.
\tag{8}
\]

The monic root polynomial is

\[
P(w)=\prod_{j=1}^6(w-z_j)
=w^6-e_1w^5+e_2w^4-e_3w^3+e_4w^2-e_5w+E.
\tag{9}
\]

Because every root has unit modulus, complementing subsets gives

\[
\boxed{e_{6-k}=E\,\overline{e_k}}
\qquad(0\le k\le6).
\tag{10}
\]

The centered condition gives `e_1=s_1=0`, hence `e_5=0`. Newton's identities give

\[
\boxed{e_2=-\frac{s_2}{2},
\qquad e_3=\frac{s_3}{3}.}
\tag{11}
\]

For `k=3`, equation `(10)` becomes

\[
e_3=E\overline{e_3}.
\tag{12}
\]

If `s_3\ne0`, then `e_3\ne0`, so

\[
\boxed{E=\frac{e_3}{\overline{e_3}}
=\frac{s_3}{\overline{s_3}}.}
\tag{13}
\]

Equation `(10)` with `k=2` then yields

\[
e_4=E\overline{e_2}
=-\frac{s_3\overline{s_2}}{2\overline{s_3}}.
\tag{14}
\]

Substituting `(11)`, `(13)`, and `(14)` into `(9)` gives `(2)`. A monic polynomial determines its root multiset, so `(s_2,s_3)` is exactly faithful on `s_3\ne0`.

This is the six-point analogue of AF-313, but the coefficient geometry is different: for five points unit-circle reciprocity forced an additional modulus relation between `s_2` and `s_3`; for six points the two magnitudes remain independent on the generic zero fiber.

### 2. The weighted quotient has one complex coordinate plus one real modulus

Under common rotation `Z\mapsto\rho Z`, `|\rho|=1`,

\[
s_2\mapsto\rho^2s_2,
\qquad
s_3\mapsto\rho^3s_3.
\tag{15}
\]

Therefore `(3)` is rotation invariant.

To prove completeness, let two configurations `Z,Z'` in the `s_3\ne0` stratum have the same `R`. Write

\[
a=s_2(Z),\quad b=s_3(Z),
\qquad
a'=s_2(Z'),\quad b'=s_3(Z').
\tag{16}
\]

First suppose `a\ne0`. Set

\[
A=\frac{a'}a,
\qquad
B=\frac{b'}b.
\tag{17}
\]

Equality of `|s_3|` gives `|B|=1`, while equality of `\kappa` gives

\[
A^3=B^2.
\tag{18}
\]

Taking moduli in `(18)` gives `|A|=1`. Define

\[
\rho=\frac BA.
\tag{19}
\]

Then `(18)` implies

\[
\rho^2=A,
\qquad
\rho^3=B.
\tag{20}
\]

Hence `(a',b')=(\rho^2a,\rho^3b)`. Formula `(2)` is covariant under the same rotation, so `Z'=\rho Z` as unordered multisets.

If `a=0`, equality of `\kappa` forces `a'=0`. Equality of `|b|` gives `B=b'/b\in S^1`; choose any `\rho\in S^1` with `\rho^3=B`. Then again `(a',b')=(\rho^2a,\rho^3b)`, because both second-harmonic terms vanish, and `(2)` gives `Z'=\rho Z`.

Thus `R` is complete on the entire `s_3\ne0` stratum, including `s_2=0`.

### 3. Why one complex scalar stops being enough at six points

Consider the ordered centered configuration space

\[
\mathcal M_6
=
\left\{(z_1,\ldots,z_6)\in(S^1)^6:
\sum_{j=1}^6z_j=0\right\}.
\tag{21}
\]

Write `z_j=e^{i\theta_j}` and let

\[
\Sigma:(S^1)^6\to\mathbb C,
\qquad
\Sigma(z)=\sum_j z_j.
\tag{22}
\]

At a point of `\mathcal M_6`, the differential is

\[
D\Sigma(\dot\theta_1,\ldots,\dot\theta_6)
=
 i\sum_{j=1}^6 z_j\dot\theta_j.
\tag{23}
\]

Its real rank is less than `2` exactly when all vectors `z_j` lie on one real line through the origin, i.e. when the configuration is supported on one antipodal pair. Away from that collinear locus, `0` is a regular value locally, so `\mathcal M_6` is a smooth real `4`-manifold.

The diagonal common-rotation action of `S^1` on ordered tuples is free, reducing the local dimension to `3`. Passing from labeled to unordered configurations is only a finite permutation quotient. On the generic locus with trivial finite stabilizer, the unordered rotation quotient is therefore locally a real `3`-manifold.

The `s_3\ne0` part contains such generic points. For example, the union of two differently rotated equilateral triples is centered and can be chosen with `s_3\ne0`; nearby points in the regular four-dimensional centered manifold break the finite rotational symmetry while preserving `s_3\ne0`.

Now suppose one complex-valued continuous invariant were injective on a generic open shape patch `U`. Choosing local coordinates would give a continuous injection

\[
f:V\subset\mathbb R^3\longrightarrow\mathbb C\cong\mathbb R^2.
\tag{24}
\]

Composing with the standard inclusion `\mathbb R^2\hookrightarrow\mathbb R^3` would give a continuous injection from an open subset of `\mathbb R^3` into `\mathbb R^3` whose image lies in a plane. Brouwer invariance of domain says the image of such an injection must be open in `\mathbb R^3`, a contradiction.

Therefore a single continuous complex scalar cannot be generically complete. The invariant `(3)` takes values in `\mathbb R_{>0}\times\mathbb C`, exactly three real coordinates, and is already complete on `s_3\ne0`. The lower bound is attained.

This identifies the exact information threshold missed by a simple extrapolation of AF-314: the six-point quotient does not require two full complex invariants, but it does require one more real degree of retained information beyond a single complex number.

### 4. A second-harmonic zero forces cubic torsion

Now specialize to six distinct rational primes at a hypothetical nonzero exact hit and set

\[
z_j=p_j^{-it}.
\tag{25}
\]

Assume first that `s_2=F_P(2t)=0`. Then `(11)` gives `e_2=0`, and `(10)` gives `e_4=E\overline{e_2}=0`. We already have `e_1=e_5=0`, so `(9)` reduces to

\[
P(w)=w^6-e_3w^3+E.
\tag{26}
\]

Thus `P(w)` is a polynomial in `w^3`. Its six roots form two three-element orbits under multiplication by a primitive cube root of unity. In particular, some three of the prime phases have the form

\[
\rho,\ \rho\omega,\ \rho\omega^2,
\qquad \omega^3=1,
\quad\omega\ne1.
\tag{27}
\]

For three corresponding distinct primes `q_1,q_2,q_3`, two phase ratios are nontrivial cube roots of unity. Hence

\[
(q_1/q_3)^{-3it}=1,
\qquad
(q_2/q_3)^{-3it}=1.
\tag{28}
\]

Eliminating `t` gives a nontrivial rational relation between `\log(q_1/q_3)` and `\log(q_2/q_3)`, equivalently a nontrivial multiplicative relation among three distinct rational primes. Unique factorization forbids this. Therefore

\[
F_P(2t)\ne0.
\tag{29}
\]

### 5. A third-harmonic zero forces antipodal pairing

Assume instead that `s_3=F_P(3t)=0`. Equation `(11)` gives `e_3=0`; together with `e_1=e_5=0`, the root polynomial `(9)` contains only even powers:

\[
P(w)=w^6+e_2w^4+e_4w^2+E.
\tag{30}
\]

Therefore its root multiset is invariant under `w\mapsto-w`: the six phases split into three antipodal pairs.

Take two disjoint pairs `(p_a,p_b)` and `(p_c,p_d)`. Their phase ratios are `-1`, so for odd integers `m,n`,

\[
t\log(p_a/p_b)=m\pi,
\qquad
t\log(p_c/p_d)=n\pi.
\tag{31}
\]

Eliminating `t` yields

\[
n\log(p_a/p_b)-m\log(p_c/p_d)=0,
\tag{32}
\]

hence

\[
(p_a/p_b)^n=(p_c/p_d)^m.
\tag{33}
\]

Because the two pairs use four distinct rational primes, `(33)` contradicts unique factorization. Therefore

\[
F_P(3t)\ne0.
\tag{34}
\]

Equations `(29)` and `(34)` prove `(5)`. Substituting the surviving harmonics into `(2)` proves exact raw recovery, and `(3)` proves the quotient statement `(7)`.

## Fidelity interpretation

The first-harmonic scalar `s_1` erases the whole centered six-point fiber. The next two harmonics restore exact information on the source-relevant stratum, but the amount of information needed after quotienting common phase has increased relative to five points.

For five points, AF-314 found a single complex complete coordinate because the generic unordered shape quotient has two real degrees of freedom. At six points the quotient has three. Arithmetic does not make the extra ambient degree disappear merely by excluding the obvious torsion strata: the natural exact quotient record is one complex relative-phase invariant together with one real harmonic magnitude.

This gives a concrete instance of the line's central distinction between **exact recoverability** and **compression budget**. The same low harmonic pair `(s_2,s_3)` remains enough for exact recovery, while a further quotient audit reveals that the minimal continuous shape representation has grown from two to three real coordinates.

The rational-prime control adds a separate fact: the two singular harmonic geometries have explicit cyclotomic forms (`\mu_3` or antipodal pairing), and a common nonzero prime-log time cannot realize them. Thus prime arithmetic removes the bad strata without providing any theorem that the prime orbit meets the centered six-point fiber in the first place.

## Prior art and novelty assessment

The ingredients are classical and no novelty claim is made.

- Newton's identities and elementary-symmetric reconstruction are standard; I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), is a standard reference.
- Unit-circle root polynomials are self-inversive. Christopher D. Sinclair and Jeffrey D. Vaaler, **“Self-inversive polynomials with all zeros on the unit circle,”** in *Number Theory and Polynomials*, London Mathematical Society Lecture Note Series 352, Cambridge University Press (2010), pp. 312–321, DOI `10.1017/CBO9780511721274.020`, is direct prior art for that coefficient structure.
- Planar polygon/linkage spaces are classical. Navnath Daundkar, Priyavrat Deshpande, Shuchita Goyal, and Anurag Singh, **“The Borsuk-Ulam theorem for planar polygon spaces,”** *Topology and its Applications* 318 (2022), 108204, DOI `10.1016/j.topol.2022.108204`, records the standard `n-3` dimension for generic planar polygon moduli. Equilateral even-sided spaces can have singular strata, so the dimension claim here is instead proved directly on the regular noncollinear locus by `(23)`.
- The impossibility of continuously injecting an open `3`-manifold patch into `\mathbb R^2` is the classical Brouwer invariance-of-domain obstruction.

A targeted search found extensive prior art for self-inversive polynomials, power-sum reconstruction, and polygon-space topology, but did not identify this exact six-point centered harmonic specialization or the prime-phase exclusion `(5)` as a named theorem. They are elementary consequences of classical structures, and **no mathematical novelty is asserted**. Their durable value here is the exact fidelity threshold: six is where the centered shape quotient first exceeds one complex degree of continuous storage, while the same two low harmonics still recover a hypothetical rational-prime hit.

## Boundaries and falsification checks

- The recovery theorem `(2)` assumes exactly six unit-modulus points, `s_1=0`, and `s_3\ne0`. When `s_3=0`, `(s_2,s_3)` need not determine the root polynomial because `E` is no longer recovered from `(12)`.
- The quotient invariant `(3)` is complete only on `s_3\ne0`. It is not claimed to extend as a globally faithful continuous coordinate across the antipodal-pair stratum.
- The three-real lower bound is a **continuous generic ambient-shape** statement. Arbitrary discontinuous set-theoretic encodings can evade Euclidean dimension counting, and a restricted arithmetic source subset can have lower intrinsic dimension than the ambient zero fiber.
- The prime specialization is conditional on a hypothetical `F_P(t)=0`. It does not prove such a time exists, and it does not transfer the ambient three-dimensional lower bound to the unknown set of prime hits.
- Exact exclusion of `F_P(2t)=0` and `F_P(3t)=0` does not provide a positive lower bound for their magnitudes. Recovery through `(2)` becomes ill-conditioned as `|s_3|\to0`, and no uniform prime-specific conditioning margin is established.
- Recovery is of the unordered phase multiset. It does not label recovered phases by their originating primes, recover `t`, or identify the absolute common-phase gauge from `(7)`.
- The cubic and antipodal contradictions use distinct rational primes and one common nonzero time. They should not be generalized to arbitrary generalized-prime, Beurling, or freely assigned phase systems.
- No zeta zero count, explicit-formula sign theorem, critical-line statement, or RH implication follows.

## Consequence for the research line

AF-314 left open where a larger centered zero fiber first outruns one complex quotient invariant. The threshold is already the next case: **six points require three real continuous coordinates on the generic unordered common-phase quotient**, and `( |s_3|,s_2^3/s_3^2 )` attains that lower bound on `s_3\ne0`.

At the same time, the arithmetic specialization remains unexpectedly rigid: a hypothetical six-prime exact hit cannot fall onto either the cubic-torsion `s_2=0` stratum or the antipodal `s_3=0` stratum, so the same second and third harmonics recover its entire phase multiset. This closes the immediate post-incidence compression question at support six while leaving the central unresolved problem unchanged: proving or excluding the **first nontorsion prime-log incidence** with the polygon-zero cone requires information beyond these recovery and dimension arguments.