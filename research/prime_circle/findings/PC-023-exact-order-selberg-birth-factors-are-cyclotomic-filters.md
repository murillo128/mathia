# PC-023 — exact-order Selberg birth factors are cyclotomic filters of one fixed length-winding spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for treating the canonical exact-order Selberg birth factor of the full cyclic-cover tower as a new arithmetic mechanism. This does **not** rule out exceptional information in an individually distinguished twisted sector or in the nonlinear composite birth-surface defect of PC-017.

PC-022 isolated the exact-order deck-character layer

\[
\mathcal H_n^{\rm birth}
=\bigoplus_{(a,n)=1}L^2(B,\chi_{a/n})
\]

and its canonical Selberg factor

\[
Z_n^{\rm birth}(s)
=\prod_{(a,n)=1}Z_B(s,\chi_{a/n}).
\]

The open question was whether the **twisted spectral data inside this exact-order package** introduced arithmetic structure beyond the Ramanujan projector that selects the package. On the half-plane where the twisted Selberg Euler products converge absolutely, the answer for the canonical product is exact: its dependence on the level `n` is again purely cyclotomic/Ramanujan. The nontrivial geometry is a fixed marked length spectrum of the base thrice-punctured sphere.

## 1. One universal marked geodesic spectrum

Keep the notation of PC-022:

\[
B=\widehat{\mathbb C}\setminus\{0,1,\infty\},
\]

and let

\[
\omega:\pi_1(B)\to\mathbb Z
\]

record winding around `0`. For

\[
\chi_{a/n}(\gamma)
=\exp\!\left(2\pi i\frac{a}{n}\omega(\gamma)\right),
\]

the scalar twisted Selberg zeta has, for `Re(s)` sufficiently large, the standard Euler product

\[
Z_B(s,\chi_{a/n})
=\prod_{\widehat\gamma}\prod_{k\ge0}
\left(1-\chi_{a/n}(g_{\widehat\gamma})
 e^{-(s+k)\ell(\widehat\gamma)}\right),
\]

where `hat gamma` runs over primitive periodic geodesics of the fixed base `B`.

Thus every level samples the same marked data

\[
\boxed{
\bigl(\ell(\widehat\gamma),\omega(g_{\widehat\gamma})\bigr)
}
\]

with different roots-of-unity phases. No level-dependent geodesic geometry is created on the base.

## 2. Grouping exact-order characters gives an explicit cyclotomic local factor

Fix a primitive periodic geodesic and write

\[
r=\omega(g_{\widehat\gamma})\in\mathbb Z,
\qquad
q=e^{-(s+k)\ell(\widehat\gamma)}.
\]

The local contribution to the exact-order birth product is

\[
C_{n,r}(q)
:=\prod_{\substack{0\le a<n\\(a,n)=1}}
\left(1-e^{2\pi i ar/n}q\right).
\]

Let

\[
m=\frac{n}{\gcd(n,r)}.
\]

If `m>1`, multiplication by `r` sends the primitive `n`-th characters onto the primitive `m`-th roots, each with multiplicity

\[
\frac{\varphi(n)}{\varphi(m)}.
\]

Therefore

\[
\boxed{
C_{n,r}(q)
=\Phi_m(q)^{\varphi(n)/\varphi(m)},
\qquad
m=\frac{n}{\gcd(n,r)}>1.
}
\]

If `n|r`, all phases are `1`, so instead

\[
\boxed{
C_{n,r}(q)=(1-q)^{\varphi(n)}.
}
\]

Hence the complete canonical birth factor is

\[
\boxed{
Z_n^{\rm birth}(s)
=\prod_{\widehat\gamma}\prod_{k\ge0}
C_{n,\omega(g_{\widehat\gamma})}
\!\left(e^{-(s+k)\ell(\widehat\gamma)}\right)
}
\]

on the absolute-convergence half-plane.

This is stronger than saying the projector is a Ramanujan projector: **the Euler factor of the entire exact-order Selberg determinant is literally a cyclotomic polynomial determined by the gcd of the level with the geodesic winding.**

## 3. Logarithmic form: Ramanujan sums are the only level weights

Using

\[
\log(1-z)=-\sum_{j\ge1}\frac{z^j}{j}
\]

and summing over primitive characters gives

\[
\sum_{(a,n)=1}e^{2\pi i a j r/n}=c_n(jr).
\]

Therefore

\[
\boxed{
\log Z_n^{\rm birth}(s)
=-\sum_{\widehat\gamma}\sum_{j\ge1}
\frac{c_n(j\,\omega(g_{\widehat\gamma}))}{j}
\frac{e^{-js\ell(\widehat\gamma)}}
{1-e^{-j\ell(\widehat\gamma)}}.
}
\]

This separates the two inputs exactly:

```text
fixed hyperbolic base geometry
    -> lengths ell(gamma) and integer winding omega(gamma)

level n
    -> classical Ramanujan weight c_n(j omega(gamma))
```

No other `n`-dependence is present in the canonical exact-order product before meromorphic continuation.

For a prime `p`, this becomes especially transparent:

\[
c_p(r)=
\begin{cases}
p-1,&p\mid r,\\-1,&p\nmid r.
\end{cases}
\]

Equivalently, every local birth factor is either

\[
(1-q)^{p-1}
\]

when `p|r`, or

\[
\Phi_p(q)=\frac{1-q^p}{1-q}
\]

when `p` does not divide `r`.

## 4. Consequence: the canonical full-cover birth determinant is classicalized

PC-022 left alive the possibility that the exact-order twisted family might itself carry a forced prime-specific spectral mechanism. PC-023 closes the most canonical scalar version of that route.

The exact-order **product/determinant package** contains no new arithmetic weighting beyond:

- the fixed length-winding spectrum of `B`;
- gcd with `n`;
- cyclotomic polynomials;
- Ramanujan sums.

These are all structures already present elsewhere in the prime-circle program. Meromorphic continuation can reveal nontrivial spectral zeros/resonances of this weighted base-geodesic product, but it does not change where the level dependence entered. Therefore a zero pattern of `Z_n^{birth}` cannot be interpreted as new arithmetic evidence merely because `n` is prime or because the factor was extracted as a spectral birth layer.

This is analogous in spirit to PC-015 and PC-021: a sophisticated analytic package can still inherit its arithmetic dependence from an elementary primitive-root transform.

## 5. What this does not rule out

The negative result is deliberately scoped.

It does **not** prove that every individual function

\[
Z_B(s,\chi_{a/n})
\]

is analytically trivial, nor that no particular character sector can have exceptional spectral behavior. The canonical product over all exact-order characters forgets distinctions among primitive `a` by taking their norm-like product.

It also does not touch the nonlinear comparison

\[
Q_n^{\rm birth}-Q_n^{\rm full}
\]

of PC-017 for composite levels. That object is absent from the full-cover Artin package entirely.

Thus a surviving spectral route must demonstrate at least one of:

1. a **canonically distinguished individual character/combination** whose choice is forced by the original anchored circle geometry and whose behavior is not reproduced by generic rational holonomy;
2. exceptional analytic behavior of the fixed length-winding spectrum under the Ramanujan/cyclotomic weights, with composite and non-arithmetic controls showing that the effect is not generic cyclic-cover representation theory;
3. a mechanism involving the nonlinear birth-vs-full uniformization defect, rather than only the full cyclic-cover spectrum.

Without one of these extra ingredients, the exact-order Selberg factor is a classical cyclotomic filter of a fixed dynamical spectrum.

## 6. Prior art and novelty audit

The ingredients are standard:

- Venkov-Zograf Artin formalism gives factorization of Selberg zeta under finite covers/induced representations.
- Fedosova-Pohl give the standard twisted Selberg Euler product for finite-dimensional twists with non-expanding cusp monodromy, a class containing all unitary characters, and restate/generalize the factorization formalism.
- Ramanujan sums are exactly sums over primitive roots of unity.
- The product over primitive roots is the cyclotomic polynomial.

Directed searches for `Selberg zeta + Ramanujan sum + cyclic cover`, `twisted Selberg zeta + Ramanujan sum`, and products over primitive cyclic characters did not identify this exact prime-circle specialization. No historical novelty is claimed: once PC-022 has identified the exact-order character package, the cyclotomic/Ramanujan reduction is an elementary consequence of the standard Euler product.

The durable contribution is the **research boundary**: the canonical exact-order Selberg determinant is not an unexplained new arithmetic object; its level dependence is explicitly classical.

Primary anchors:

- A. B. Venkov and P. G. Zograf, *On analogues of the Artin factorization formulas in the spectral theory of automorphic functions connected with induced representations of Fuchsian groups*, Math. USSR-Izv. 21 (1983), 435-443.
- K. Fedosova and A. Pohl, *Meromorphic continuation of Selberg zeta functions with twists having non-expanding cusp monodromy*, Selecta Math. 26, 9 (2020), DOI 10.1007/s00029-019-0534-3.
- S. Ramanujan, *On certain trigonometrical sums and their applications in the theory of numbers* (1918), for the classical primitive-root sums.

## 7. Audit tests

The exact reduction can be falsified directly:

1. for arbitrary `n,r`, verify the multiset of phases `exp(2 pi i a r/n)` over `(a,n)=1` and the stated cyclotomic multiplicity;
2. expand the logarithm and recover `c_n(jr)` coefficient-by-coefficient;
3. substitute the standard twisted Selberg Euler product and check absolute convergence justifies regrouping on a right half-plane;
4. at prime `p`, verify the two local cases `p|r` and `p∤r` above.

No claim is made that the individual twisted spectra are known explicitly, that the meromorphic zeros of the birth factor are trivial, or that this calculation by itself resolves any part of RH.
