# PL-375 — Two-dimensional nonnormal multiplicative extensions are split or Leibniz-additive character jets

**Evidence:** `EXACT-DERIVED + L-ADDITIVE-PRIOR-ART + DECISIVE-NARROWING`.

**Parent finding:** `PL-374`.

**Related findings:** `PL-201`, `PL-202`, `PL-369`, `PL-373`, `PL-374`.

**Status:** `THE-FIRST-NONNORMAL-FINITE-DIMENSIONAL-ESCAPE-LEFT-BY-PL-374-COLLAPSES-IN-DIMENSION-TWO: DISTINCT-DIAGONAL-CHARACTERS-SPLIT-BY-ONE-FIXED-SHEAR, WHILE-A-NONVANISHING-SELF-EXTENSION-IS-EXACTLY-A-LEIBNIZ-ADDITIVE/COMPLETELY-ADDITIVE-FIRST-ORDER-JET-OF-ONE-SCALAR-CHARACTER; THE-CANONICAL-LOG-N-JET-GIVES-JUST-A-DERIVATIVE-OF-THE-SCALAR-DIRICHLET-SERIES`.

## Claim

Let

\[
\rho:\mathbb N_{>0}\to M_2(\mathbb C)
\]

be unital and completely multiplicative. After the simultaneous triangularization supplied by `PL-374`, write

\[
\rho(n)=
\begin{pmatrix}
\chi_1(n)&b(n)\\
0&\chi_2(n)
\end{pmatrix},
\tag{PL375-1}
\]

where `chi_1,chi_2` are scalar completely multiplicative functions. Then the off-diagonal coefficient satisfies

\[
b(mn)=\chi_1(m)b(n)+b(m)\chi_2(n).
\tag{PL375-2}
\]

Because `rho(m)` and `rho(n)` commute, the same equation with `m,n` interchanged implies

\[
\boxed{
(\chi_1(m)-\chi_2(m))b(n)
=(\chi_1(n)-\chi_2(n))b(m).
}
\tag{PL375-3}
\]

This gives an exact dichotomy.

If `chi_1 != chi_2`, choose `r` with `chi_1(r) != chi_2(r)`. Then

\[
b(n)=c\bigl(\chi_1(n)-\chi_2(n)\bigr),
\qquad
c=\frac{b(r)}{\chi_1(r)-\chi_2(r)}.
\tag{PL375-4}
\]

One fixed upper-triangular shear therefore diagonalizes **every** `rho(n)`. The apparent nonnormal extension between distinct scalar characters is split; it contains no new joint prime coupling.

If instead `chi_1=chi_2=chi`, then (PL375-2) is exactly the classical **Leibniz-additive** rule

\[
b(mn)=\chi(m)b(n)+b(m)\chi(n).
\tag{PL375-5}
\]

Assume now that `chi` is nonzero-valued. Setting

\[
d(n)=\frac{b(n)}{\chi(n)}
\]

gives

\[
\boxed{d(mn)=d(m)+d(n)},
\tag{PL375-6}
\]

so `d` is completely additive and hence

\[
\boxed{
d(n)=\sum_p v_p(n)d(p).
}
\tag{PL375-7}
\]

Writing `N=E_12`, `N^2=0`, every such nonsplit self-extension therefore has the exact form

\[
\boxed{
\rho(n)=\chi(n)\bigl(I+d(n)N\bigr).
}
\tag{PL375-8}
\]

Conversely every completely additive `d` gives a representation of this form. Thus the surviving two-dimensional nonnormal datum is not a new nonlinear interaction among prime directions: it is a freely specified linear functional on the exponent vector,

\[
d(n)=\langle v(n),(d(p))_p\rangle.
\tag{PL375-9}
\]

Equivalently, it is the first-order tangent jet of the scalar character family

\[
\chi_t(n)=\chi(n)e^{t d(n)},
\qquad
\left.\partial_t\chi_t(n)\right|_{t=0}=\chi(n)d(n)=b(n).
\tag{PL375-10}
\]

The most canonical prime-lattice choice `d(p)=log p` gives `d(n)=log n`. If

\[
L_\chi(s)=\sum_{n\ge1}\chi(n)n^{-s},
\]

then, in any half-plane where termwise differentiation is justified,

\[
\boxed{
\sum_{n\ge1}\frac{b(n)}{n^s}
=
\sum_{n\ge1}\frac{\chi(n)\log n}{n^s}
=-L_\chi'(s).
}
\tag{PL375-11}
\]

So the canonical logarithmic Jordan direction does not create an independent analytic object: it produces the first derivative of the underlying scalar Dirichlet series. Analytic continuation of the matrix coefficient beyond its initial convergence region therefore still requires continuation of the scalar channel; it is not supplied by the two-dimensional extension.

## 1. Exact classification of the distinct-character case

Multiplying (PL375-1) gives

\[
\rho(m)\rho(n)=
\begin{pmatrix}
\chi_1(m)\chi_1(n)&
\chi_1(m)b(n)+b(m)\chi_2(n)\\
0&\chi_2(m)\chi_2(n)
\end{pmatrix}.
\]

Complete multiplicativity yields (PL375-2). Since `mn=nm`, the image is commutative, so comparison with `rho(n)rho(m)` gives (PL375-3).

Suppose the diagonal characters are distinct. Fix `r` with

\[
\Delta_r:=\chi_1(r)-\chi_2(r)\ne0.
\]

Putting `m=r` in (PL375-3) gives (PL375-4) for every `n`. For

\[
S=
\begin{pmatrix}
1&-c\\
0&1
\end{pmatrix},
\]

a direct multiplication shows that for any upper-triangular matrix `A=[[a,b],[0,d]]`, the off-diagonal entry of `S^{-1}AS` is `b-c(a-d)`. Applying (PL375-4),

\[
S^{-1}\rho(n)S
=
\begin{pmatrix}
\chi_1(n)&0\\
0&\chi_2(n)
\end{pmatrix}
\qquad\forall n.
\tag{PL375-12}
\]

Thus in dimension two there is no nonsplit extension between two distinct multiplicative characters of the positive-integer monoid. The conclusion is stronger than trace/determinant blindness: the entire matrix representation is globally similar to the direct sum of the two scalar channels.

This calculation uses no nonvanishing hypothesis on the characters. Zeros are harmless as long as the two diagonal characters are not identical.

## 2. Self-extensions are exactly Leibniz-additive arithmetic functions

When `chi_1=chi_2=chi`, equation (PL375-2) becomes (PL375-5). This is precisely the definition of an `L`-additive or Leibniz-additive arithmetic function with multiplier `h=chi` in the number-theory literature.

Haukkanen, Merikoski and Tossavainen introduced and systematically studied this class in 2018, proving in particular that an `L`-additive function is determined by its values and its completely multiplicative multiplier on primes. Later work makes the nonvanishing reduction especially explicit: for nonzero-valued `h`, division `g=f/h` converts Leibniz-additivity to complete additivity and hence to a prime-linear formula. This is exactly (PL375-6)--(PL375-7).

Therefore no novelty is claimed for the abstract twisted Leibniz law or for its reduction to a completely additive function. The line-specific content is the identification that **the first genuinely nonnormal two-dimensional extension left open by `PL-374` is exactly this classical arithmetic-function class**.

In exponent-lattice coordinates the reduction is particularly transparent. Since a completely additive `d` is fixed freely by its values on primes,

\[
d(n)=\sum_p v_p(n)d(p),
\]

its geometry is affine-linear on the positive cone. It does not create curvature, pairwise prime interaction, or a higher-order support invariant. The off-diagonal channel is one linear covector on the same exponent lattice.

## 3. Dual-number / first-jet interpretation

The algebra of matrices

\[
\{aI+bN:N^2=0\}
\]

is the ordinary dual-number algebra. Equation (PL375-8) says that a nonvanishing two-dimensional self-extension is a multiplicative character valued in dual numbers.

The tangent interpretation is exact rather than metaphorical. For any completely additive `d`, define

\[
\chi_t(p)=\chi(p)e^{t d(p)}
\]

and extend completely multiplicatively. Then unique factorization gives

\[
\chi_t(n)
=\chi(n)\exp\left(t\sum_pv_p(n)d(p)\right)
=\chi(n)e^{t d(n)}.
\]

Its first jet at `t=0` is `(chi,b)`. Hence the nilpotent matrix direction stores an infinitesimal deformation of a scalar character, not a new finite-dimensional irreducible prime object.

This is the familiar algebraic role of dual numbers and derivations/tangent vectors. The targeted novelty audit around matrix-valued completely multiplicative arithmetic functions, upper-triangular character extensions, dual-number representations, and derivations found the established Leibniz-additive arithmetic-function theory and the standard dual-number tangent interpretation, but no RH-specific theorem converting this first-order jet into a zero-localization mechanism.

## 4. Dirichlet-series observable of a general additive jet

The logarithmic choice is only one member of the class. Let

\[
d(n)=\sum_pv_p(n)c_p,
\qquad c_p=d(p),
\]

and suppose we are in a half-plane where the relevant sums/products are absolutely convergent. Put

\[
a_p=\chi(p)p^{-s}.
\]

The scalar series has Euler product

\[
L_\chi(s)=\prod_p(1-a_p)^{-1}.
\]

Weighting the exponent at one prime and summing the geometric local series gives

\[
\boxed{
\sum_{n\ge1}\chi(n)d(n)n^{-s}
=
L_\chi(s)
\sum_p c_p\frac{a_p}{1-a_p},
}
\tag{PL375-13}
\]

provided the weighted prime sum is absolutely legitimate. Thus even the matrix coefficient decomposes into the scalar channel times a freely chosen prime-linear logarithmic-direction field.

For `c_p=log p`,

\[
\sum_p(\log p)\frac{a_p}{1-a_p}
=-\frac{L_\chi'(s)}{L_\chi(s)},
\]

and (PL375-13) becomes (PL375-11). This identity is asserted first only in the common absolute-convergence region. If `L_chi` has an independently established meromorphic/holomorphic continuation, then `-L_chi'` continues with it as a derivative; the Euler-product derivation itself is not being transported formally into the critical strip.

For the `log n` Hamiltonian singled out throughout the Prime-Lattice line, the nonnormal first jet therefore supplies no new continuation engine and no independent divisor. It differentiates the scalar source already present.

## 5. RH-facing consequence

`PL-374` left nonnormal extension data as the first finite-dimensional possibility not seen by trace or determinant. In dimension two that escape is now sharply reduced:

- if the two scalar graded channels differ, the extension is a basis artifact and splits globally;
- if they coincide and are nonzero-valued, the only nonsplit extension is a completely additive tangent jet of that one scalar channel;
- the canonical exponent energy `log n=<v(n),(log p)_p>` gives exactly the derivative `-L_chi'(s)`.

For the phase/Liouville/Venturini-type scalar channels relevant to the current frontier, the nonvanishing hypothesis is natural: their prime values are nonzero (often unimodular). In that regime a `2 x 2` Jordan upgrade of a scalar completely multiplicative witness does not escape the scalar analytic problem. It adds first-order differential data whose continuation and singularities depend on the scalar series already being controlled.

This does not mean derivatives are analytically useless. `L_chi'` can have its own zeros and can enter argument-principle or multiplicity information. The negative statement is structural: **the two-dimensional nilpotent layer does not independently derive the scalar continuation or force the Riemann zero divisor onto `Re(s)=1/2`; it is the first tangent derivative of a scalar character family.**

## 6. Prior-art and novelty audit

Primary close anchors:

1. **Pentti Haukkanen, Jorma K. Merikoski, Timo Tossavainen**, “The arithmetic derivative and Leibniz-additive functions,” *Notes on Number Theory and Discrete Mathematics* **24**(3) (2018), 68–76. DOI `10.7546/nntdm.2018.24.3.68-76`.
   - Defines Leibniz-additive functions by exactly the twisted product rule (PL375-5), develops their basic structure, and states that they are determined by prime data together with the completely multiplicative multiplier.
2. **Champak Talukdar, Helen K. Saikia**, “Prime-supported Leibniz-additive functions and integer eigenpoints of generalized arithmetic subderivatives,” *Far East Journal of Mathematical Sciences* (2026). DOI `10.17654/0972087126061`.
   - Current explicit close prior art for the nonvanishing case: records that `g=f/h` converts Leibniz-additivity to complete additivity and yields the prime-linear representation. This directly calibrates (PL375-6)--(PL375-7).
3. **Pentti Haukkanen, Jorma K. Merikoski, Timo Tossavainen**, “Arithmetic subderivatives and Leibniz-additive functions,” *Annales Mathematicae et Informaticae* **50** (2019), 145–157. DOI `10.33039/ami.2019.03.003`.
   - Uses the nonzero-valued completely multiplicative multiplier formulation and develops the prime-supported arithmetic-derivative side of the same class.

The exact `2 x 2` splitting dichotomy and its placement as the next obstruction after `PL-374` are derived here rather than attributed to those papers. They are elementary consequences of commutation and the twisted Leibniz relation, so no theorem-priority claim is made. The literature audit did not find an established RH mechanism extracting critical-line localization from such a finite-dimensional first-order character jet.

A recent 2026 paper on generalized convolutions also continues the established `L`-additive theory, reinforcing that the arithmetic-function class itself is active prior art rather than a new object. It is not needed for the derivation above.

## 7. Adversarial boundaries

**Zero-valued self-characters are not classified by the division argument.** If `chi(p)=0` for some prime, `b/chi` is not defined on multiples of that prime. Distinct-character extensions still split by (PL375-3), but an identical diagonal character with zeros can carry singular support behavior not covered by (PL375-6)--(PL375-8). Such a construction would need an RH-relevant reason for the zero pattern rather than freely inserted support defects.

**Higher-dimensional nonnormal extensions are not classified.** A longer common triangular flag can support several nilpotent levels and extension classes. The present result only kills the first `2 x 2` Jordan escape. Higher-order jets are a plausible analogy but are not asserted without proof; nontrivial compatibility among several repeated characters may survive.

**Unbounded/infinite-dimensional representations remain outside the result.** The argument starts after finite-dimensional simultaneous triangularization and says nothing about infinite-dimensional commutative operator algebras, domains, Fredholm determinants, or target-relative compressions.

**Breaking complete multiplicativity remains a genuine category exit.** The twisted Leibniz classification is forced by `rho(mn)=rho(m)rho(n)`. If a source construction couples primes through addition, reciprocity, explicit-formula constraints, or another nonmultiplicative global relation, (PL375-2) no longer applies.

**The logarithmic derivative identity is domain-sensitive.** Equation (PL375-11) follows by termwise differentiation only where the scalar Dirichlet series converges normally. Beyond that region it survives only through an independently justified analytic continuation of `L_chi`; the matrix representation itself supplies no continuation theorem.

## Consequence for the research line

The finite-dimensional fork left by `PL-374` can no longer treat the smallest nonnormal Jordan block as an unexplored source of cross-prime geometry. In dimension two, complete multiplicativity forces either an actual direct sum of scalar characters or a self-extension whose entire extra datum is

\[
\langle v(n),(c_p)_p\rangle.
\]

With the canonical energy covector `(log p)_p`, that datum is just differentiation in the scalar spectral parameter. The next useful finite-dimensional question, if pursued at all, must therefore begin at **higher nilpotent order or a genuinely non-completely-multiplicative relation**, and it must demonstrate an invariant that is not merely an iterated scalar character jet. Otherwise the more promising exits remain the ones already isolated by the line: infinite-dimensional/global trace structure, target-relative positivity, or a source relation whose arithmetic divisor is not predetermined by a scalar completely multiplicative channel.