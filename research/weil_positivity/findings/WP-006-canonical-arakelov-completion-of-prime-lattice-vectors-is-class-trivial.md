# WP-006 — The canonical Arakelov completion of Prime-Lattice vectors is class-trivial

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. WP-004 showed that Prime Lattice intrinsically recovers the exact finite Weil weights `Lambda(n)/sqrt(n)` from the prime-power axes, but its Beurling control showed that finite-place geometry alone is not enough. The most canonical arithmetic way to break that control is to reinterpret the exponent vector as the finite divisor of an integer and add the real place by the product formula. This does combine finite primes and infinity intrinsically — but it makes every Prime-Lattice integer vector a **principal arithmetic divisor**, hence the zero class in the ordinary Arakelov Picard/Chow group. Any positivity or intersection form that depends only on that class therefore vanishes identically on the very data whose finite part WP-004 needs to retain. The naive route “Prime Lattice + product-formula compactification + class-level Arakelov positivity” is therefore closed.

## 1. Claim

Prime Lattice represents a positive integer

\[
n=\prod_p p^{v_p(n)}
\]

by its exponent vector `(v_p(n))_p`. The same data is exactly the finite divisor on `Spec Z`

\[
D_f(n)=\sum_p v_p(n)[p].
\tag{1}
\]

In the standard arithmetic-divisor convention for `Spec Z`, an arithmetic divisor is written

\[
\widehat D=\left(\sum_p n_p[p],\lambda\right),
\]

with arithmetic degree

\[
\widehat{\deg}(\widehat D)
=\sum_p n_p\log p+\frac{\lambda}{2}.
\tag{2}
\]

The rational function `n in Q^times` has principal arithmetic divisor

\[
\widehat{\operatorname{div}}(n)
=
\left(
\sum_p v_p(n)[p],
-\log |n|^2
\right)
=
\left(D_f(n),-2\log n\right).
\tag{3}
\]

Because

\[
\sum_p v_p(n)\log p=\log n,
\]

its arithmetic degree is exactly zero:

\[
\widehat{\deg}\,\widehat{\operatorname{div}}(n)
=\log n-\log n=0.
\tag{4}
\]

More strongly, (3) is one of the relations by which the arithmetic Chow/Picard group is defined, so

\[
\boxed{
[\widehat{\operatorname{div}}(n)]=0
\quad\text{in}\quad
\widehat{\mathrm{CH}}^1(\operatorname{Spec}\mathbb Z)
}
\tag{5}
\]

for every positive integer `n`. For `Q`, arithmetic degree identifies the ordinary Arakelov divisor class group with `R`; in particular its degree-zero subgroup is trivial.

Consequently, if `q` is any norm, positive form, intersection response, or other invariant that **descends to the ordinary arithmetic divisor class**, then

\[
q([\widehat{\operatorname{div}}(n)])=q(0)
\]

for every `n` (and equals zero for any quadratic/bilinear form normalized at the origin). But WP-004 requires the nonzero finite values

\[
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=
\frac{\log p}{p^{k/2}}>0.
\tag{6}
\]

Thus the canonical product-formula completion destroys, at class level, exactly the prime-power information that WP-004 had recovered:

\[
\boxed{
\text{Prime-Lattice finite divisor}
+\text{canonical product-formula infinity}
\longrightarrow
\text{principal class }0,
}
\tag{7}
\]

so ordinary class-level Arakelov positivity cannot be the missing global Weil mechanism.

---

## 2. Why this is the natural continuation of WP-004

WP-004 has an unusually strong finite success. On the exponent Hilbert space it defines

\[
T=e^{-A/2}QAN^{-1}Q\ge0,
\qquad
T e_n=\frac{\Lambda(n)}{\sqrt n}e_n,
\]

where the axis projection `Q` recognizes exactly the prime powers. The matched Beurling-prime control then shows that this finite structure, including its positivity and its `1/2` Schatten boundary, is not sufficient for a Riemann-type global statement.

The obvious next requirement is therefore a structure that knows that the underlying primes are the places of `Q`, not merely abstract generators. Equation (1) supplies exactly that interpretation: the Prime-Lattice exponent coordinates are the finite valuations of a rational integer. Arakelov compactification is then the canonical classical mechanism for adjoining the real place, and the product formula determines the archimedean coordinate without fitting a parameter.

That makes (3) a particularly strong matched control. Unlike the construction in WP-004, it is genuinely specific to the arithmetic of `Q`; an arbitrary Beurling generalized-prime system does not automatically possess this principal-divisor/product-formula geometry. **The first canonical step that breaks the WP-004 Beurling control therefore does exist — and it immediately collapses the Prime-Lattice integer vectors to zero in the ordinary class group.**

This is why the obstruction is stronger than the statement that “Arakelov theory is already known.” It identifies what happens to the exact Mathia data under the most canonical global completion suggested by that known theory.

## 3. The obstruction is class-level, not a denial of all Arakelov geometry

The scope is deliberately narrow. Arithmetic divisors before quotienting still remember the decomposition in (1), and one can certainly write functions or forms of chosen representatives. What fails is the combination of all three requirements

1. use the product formula to force the archimedean component;
2. descend under principal/rational equivalence to an ordinary Arakelov divisor class;
3. retain a nonzero form on the Prime-Lattice integer vectors.

The first two imply (5), contradicting the third.

This distinction matters. A representative-dependent form on raw divisors could avoid the zero class, but then its value changes when one adds a principal arithmetic divisor. It is not an invariant of the ordinary Arakelov class and therefore needs an additional Mathia-native reason for selecting a representative. Likewise, one can choose an archimedean metric different from `-2 log n`; that avoids (3), but the metric is then extra geometric data that must be forced independently rather than obtained merely from the product formula.

The finding therefore does **not** rule out an Arakelov-flavoured global construction. It rules out the cheapest one: identify the Prime-Lattice vector with a principal divisor, add infinity by the product formula, and hope that an existing class-level norm/Hodge/intersection positivity supplies Weil positivity.

## 4. Why the gamma factor is not hiding in the principal completion

The product-formula correction in (3) contributes one scalar `-2 log n` for each rational integer. It exactly cancels the finite arithmetic degree. This is the correct archimedean datum for making the divisor principal, but it is not the archimedean distribution in the zeta explicit formula, whose test-function contribution is governed by the real gamma factor and its logarithmic derivative.

Therefore one cannot rescue (7) by saying that the missing Weil archimedean term has already appeared as `-2 log n`: that term performs the product-formula cancellation, not the gamma/digamma test-function functional. Producing the latter requires additional global analytic or cohomological structure.

This observation is secondary to the exact class-triviality proof; no impossibility theorem is claimed for every possible Green metric or analytic enhancement.

## 5. Adversarial escape tests

### 5.1 Omit the real-place term

Using only `D_f(n)` keeps the Prime-Lattice data nontrivial. But then finite and archimedean places have **not** been intrinsically assembled. This is exactly the incompleteness already exposed by WP-004 and its Beurling control.

### 5.2 Choose a non-principal metric at infinity

For

\[
\widehat D(n)=\left(D_f(n),\lambda_n\right)
\]

with `lambda_n != -2 log n`, the class need not vanish. This is a real escape, but it moves the burden of proof to the choice of `lambda_n`: a successful route must derive that metric/Green datum from geometry and then show that the same construction yields the gamma and polar terms. Selecting it to fit the explicit formula would be precisely the hand-picked regularization rejected by this research line.

### 5.3 Pair raw divisors before taking classes

This can retain prime support, but it does not descend through principal equivalence. It may still be useful as boundary data, yet it is no longer “positivity of the ordinary Arakelov divisor class.” A canonical gauge fixing or larger space would have to be supplied.

### 5.4 Apply the Prime-Lattice axis projection first

This is already what WP-004 does and is not contradicted. The projection extracts `Lambda(n)` before any Arakelov quotient. WP-006 only says that mapping the resulting integer/prime-power divisor to its **canonical principal arithmetic divisor class** cannot preserve that nonzero signal. Thus Prime Lattice may remain a finite boundary block of a larger object even though it cannot itself become the desired class.

### 5.5 Pass to an enlarged Picard/Jacobian, adele class space, or a higher-dimensional square

This escapes the theorem because it changes the target. It is also very close to existing prior art. Connes--Consani's 2026 arithmetic Jacobian work explicitly interprets the Riemann sector of the adele class space as a monoidal extension of the Picard geometry of the completed arithmetic curve, adding singular strata needed for spectral realization. Their earlier/global program similarly emphasizes that a Weil-style proof needs more than ordinary curve-level divisor classes.

So this is a **prior-art redirect**, not a novelty claim: if Mathia escapes WP-006 by adding exactly such adelic/monoidal/cohomological structure, novelty must lie in a new forced positivity mechanism, not in the idea of enlarging the arithmetic Picard object.

## 6. Relation to the previous Weil-positivity findings

The sequence now separates four increasingly global requirements:

```text
WP-004:
    Prime-Lattice axes
        -> exact positive finite coefficient measure Lambda(n)/sqrt(n)
        -> survives Beurling generalized-prime control

WP-005:
    exact Weil autocorrelation
        -> finite translation operator is indefinite
        -> commuting same-space completion is insufficient

WP-006:
    first canonical Q-specific global completion
        finite valuations + real place via product formula
        -> principal arithmetic divisor
        -> zero ordinary Arakelov class
```

The important new point is that simply “adding the archimedean place geometrically” is not enough. The most canonical such addition either leaves the finite object incomplete (if infinity is omitted), becomes a free fitted metric (if the product formula is not used), or trivializes the object in the ordinary divisor class (if the product formula is used canonically).

A surviving Mathia construction must therefore keep more structure than the ordinary principal divisor class while still making its positivity invariant and intrinsic.

## 7. Prior art and novelty assessment

The arithmetic-divisor definitions, product formula, arithmetic degree, and triviality of principal divisor classes are classical Arakelov theory. No novelty is claimed for them. Freixas i Montplet's Arakelov notes give the definitions in a normalization where a principal relation is

\[
(\operatorname{div}\alpha,(-\log|\sigma\alpha|^2)_\sigma),
\]

and for `Spec Z`

\[
\widehat{\deg}\left(\sum n_p[p],\lambda\right)
=\sum n_p\log p+\lambda/2,
\]

with the arithmetic class group of `Q` identified with `R` by degree. Burgos Gil--Kramer--Kühn provide the broader arithmetic-Chow framework.

Connes--Consani 2026 is close current prior art in the opposite direction: rather than expecting ordinary Picard classes to carry the Riemann geometry, it enlarges the completed arithmetic Picard/Jacobian picture toward the adele class space. This makes it especially important not to relabel an ordinary Arakelov completion of Prime Lattice as a new global geometric mechanism.

The durable Mathia contribution here is only the **bridge-and-failure calculation**: Prime-Lattice exponent vectors are literally the finite divisor coordinates; the canonical product-formula completion is therefore available without fitting; and precisely that completion sends every lattice integer to a principal zero class, so it cannot carry the nonzero WP-004 finite Weil observable.

## 8. Boundary conditions and next target

WP-006 does not exclude:

- a canonical non-principal Green metric forced by a larger Mathia geometry;
- an adelic/semilocal quotient where the Prime-Lattice divisor is boundary data rather than a class;
- an extended Picard/Jacobian monoid with singular strata;
- a correspondence or cycle on a genuine two-dimensional arithmetic object, where an intersection pairing can be nontrivial;
- a relative/cohomological construction in which principal divisors are null only after a compensating boundary term has already produced the Weil functional.

The strongest next question is therefore not “can we append infinity to Prime Lattice?” — ordinary Arakelov theory already answers that. It is:

\[
\boxed{
\text{Can Mathia force a larger global object in which}
\quad
\Lambda(n)/\sqrt n
\quad\text{survives as boundary/cycle data,}
}
\]

while the archimedean and polar sectors arise from the **same** geometry and positivity is a theorem of its global pairing?

That is the smallest surviving target consistent with WP-004 through WP-006.

## 9. Falsification checklist

The exact core can be checked without zeta zeros:

1. identify the Prime-Lattice vector of `n` with `D_f(n)=sum_p v_p(n)[p]`;
2. use the standard principal arithmetic divisor relation to add `lambda=-2 log n`;
3. verify the arithmetic degree is `log n-log n=0`;
4. quotient by principal arithmetic divisors and obtain class zero;
5. compare with WP-004, where the finite observable is nonzero for every `p^k`.

WP-006 is falsified only if one of those standard identifications is wrong, or if a claimed positive form does not in fact descend to the ordinary arithmetic divisor class. A construction on raw divisors, an enlarged Picard monoid, a higher-dimensional cycle space, or another quotient is an **escape by changing the object**, not a counterexample to the stated obstruction.

## 10. Evidence classification

- Prime-Lattice exponent vector equals the finite divisor coefficient vector: `EXACT-DERIVED` from unique factorization and the Prime-Lattice definition.
- Principal arithmetic divisor formula and arithmetic-degree normalization: `LITERATURE`, standard Arakelov geometry.
- Equation (5), class triviality of the canonical completion: `EXACT + LITERATURE` by the defining rational-equivalence relation.
- Incompatibility with the nonzero WP-004 prime-power weight: `EXACT-DERIVED`.
- Claim that a successful route must retain extra boundary/cohomological/adelic structure: `RESEARCH-REDIRECT`; it is a necessary escape from this obstruction, not evidence that such a structure succeeds.

No RH assumption, zeta-zero input, fitted kernel, or numerical experiment is used.