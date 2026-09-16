# PC-316 — pointwise cross-level Poisson product is a Mordell–Tornheim L-bundle

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most canonical nonlinear mixed-conductor route that multiplies two oriented prime-level harmonic fields before scalar angular compression and then propagates the product by the same Poisson semigroup.

PC-311 showed that the direct sesquilinear pairing of two prime-level Poisson fields is too rigid: angular Haar pairing first forces the same Fourier index on both legs, collapses the two radial depths to their sum, and after Mellinization produces only a finite bundle of ordinary Dirichlet `L(s+t,chi)` functions. PC-312--PC-315 then close the scalar finite-Fourier repairs of the resulting periodic packet, including its full even/odd orientation orbit.

The current live boundary therefore asks whether a source-forced **nonlinear coupling before scalar cyclic compression** can retain the two Fourier indices. Pointwise multiplication is the coefficient-free canonical test. It does retain them. If the product is then propagated inward by the same Poisson semigroup and observed at the common anchor, the third propagation depth supplies the additive factor `k+l`, and triple Mellinization produces a genuinely three-variable double Dirichlet series.

However, that series is exactly a finite bundle of classical character-weighted Mordell–Tornheim double `L`-functions. Thus this route really escapes the one-variable collapse of PC-311, but it does not create a new analytic species. The extra variables and their functional relations are inherited from established Mordell–Tornheim theory. Any RH-facing continuation of this route must therefore prove an additional **source-specific zero-selection property** of the particular Prime-Circle bundle, rather than count the multiple-`L` structure itself as progress.

## 1. The oriented Hardy component is intrinsic source data

Let `q` be prime and let

\[
f:\mathbb Z/q\mathbb Z\to\mathbb C,
\qquad
\sum_{a\bmod q}f(a)=0.
\]

Write its unnormalized finite Fourier transform as

\[
\widehat f(k)=\sum_{a\bmod q}f(a)e^{-2\pi i k a/q}.
\]

The centered Poisson field has no zero Fourier mode. Its positive-frequency Hardy component is therefore canonically determined by the field:

\[
\boxed{
A_{q,f}(x,\theta)
:=\sum_{k\ge1}\widehat f(k\bmod q)e^{-kx}e^{ik\theta},
\qquad x>0.
}
\tag{1}
\]

No new phase or coefficient sequence is introduced in (1); this is simply the oriented half of the same harmonic field whose chirality is retained in PC-315. For a second prime `r` and centered source `g`, put

\[
B_{r,g}(y,\theta)
:=\sum_{l\ge1}\widehat g(l\bmod r)e^{-ly}e^{il\theta}.
\tag{2}
\]

For brevity define

\[
a(k):=\widehat f(k\bmod q),
\qquad
b(l):=\widehat g(l\bmod r).
\tag{3}
\]

Centering gives

\[
a(k)=0\quad(q\mid k),
\qquad
b(l)=0\quad(r\mid l).
\tag{4}
\]

Thus each coefficient sequence is periodic and supported on the units of its prime conductor.

## 2. Multiply first, then propagate the product

Let `P_z^+` denote the positive-frequency Poisson/Hardy semigroup, so that it multiplies angular mode `n>=1` by `e^{-nz}`. Define the nonlinear cross-level field

\[
\mathcal H_{q,r}^{f,g}(x,y,z;\theta)
:=P_z^+\!\left(A_{q,f}(x,\cdot)B_{r,g}(y,\cdot)\right)(\theta),
\qquad z>0.
\tag{5}
\]

Pointwise multiplication occurs **before** any angular scalarization. Since both inputs have only positive frequencies, their product has output frequency `k+l`, hence absolute convergence gives

\[
\boxed{
\mathcal H_{q,r}^{f,g}(x,y,z;\theta)
=\sum_{k,l\ge1}
 a(k)b(l)e^{-kx-ly-(k+l)z}e^{i(k+l)\theta}.
}
\tag{6}
\]

Equivalently, the semigroup law makes the geometry especially transparent:

\[
\boxed{
\mathcal H_{q,r}^{f,g}(x,y,z;\theta)
=A_{q,f}(x+z,\theta)B_{r,g}(y+z,\theta).
}
\tag{7}
\]

At the common anchored vertex `theta=0`,

\[
\boxed{
H_{q,r}^{f,g}(x,y,z)
:=\mathcal H_{q,r}^{f,g}(x,y,z;0)
=\sum_{k,l\ge1}a(k)b(l)e^{-kx-ly-(k+l)z}.
}
\tag{8}
\]

This is the simplest canonical operation that avoids PC-311's diagonalization `k=l`: the two source indices remain independent, while the downstream geometry remembers their sum. The new additive coupling is not inserted by hand; it is exactly the eigenvalue of the output Fourier mode under further Poisson propagation.

Equation (7) also gives the first falsification warning. The nonlinearity has not created an autonomous interaction dynamics: the downstream propagation is only a common radial translation of the two original analytic fields. Any arithmetic novelty must therefore come from the resulting coupled Mellin transform, not from a hidden new semigroup.

## 3. Triple Mellinization gives the Mordell–Tornheim denominator exactly

For the safe absolute-convergence region

\[
\Re s>1,\qquad \Re t>1,\qquad \Re u>1,
\]

termwise Mellin integration of (8) is immediate from

\[
\int_0^\infty x^{s-1}e^{-kx}\,dx=\Gamma(s)k^{-s}.
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal M_3H_{q,r}^{f,g}(s,t,u)
&:=\int_0^\infty\!\int_0^\infty\!\int_0^\infty
x^{s-1}y^{t-1}z^{u-1}
H_{q,r}^{f,g}(x,y,z)\,dx\,dy\,dz\\
&=\Gamma(s)\Gamma(t)\Gamma(u)
Z_{q,r}^{f,g}(s,t,u),
\end{aligned}}
\tag{9}
\]

where

\[
\boxed{
Z_{q,r}^{f,g}(s,t,u)
:=\sum_{k,l\ge1}
\frac{a(k)b(l)}{k^s l^t(k+l)^u}.
}
\tag{10}
\]

This is a real structural difference from PC-311. The direct Haar pairing there forced one Fourier integer and one analytic variable `s+t`; multiplying before scalar compression leaves the pair `(k,l)` and produces the additive output coordinate `k+l`.

The extra variable is nevertheless generated by the standard Laplace identity

\[
(k+l)^{-u}
=\frac1{\Gamma(u)}
\int_0^\infty z^{u-1}e^{-(k+l)z}\,dz.
\tag{11}
\]

Thus the apparent three-variable spectralization is exactly the Mellin image of the common downstream Poisson depth.

## 4. Character decomposition is a finite classical Mordell–Tornheim bundle

Because `q` is prime, (4) says that `a` is an arbitrary function on `U(q)` extended by zero to nonunits. Dirichlet characters are its Fourier basis. Hence

\[
\boxed{
a(k)=\sum_{\chi\bmod q}A_f(\chi)\chi(k),}
\qquad
A_f(\chi)
=\frac1{q-1}\sum_{h\in U(q)}a(h)\overline{\chi(h)}.
\tag{12}
\]

Similarly,

\[
\boxed{
b(l)=\sum_{\psi\bmod r}B_g(\psi)\psi(l).}
\tag{13}
\]

Substitution into (10) gives the exact finite decomposition

\[
\boxed{
Z_{q,r}^{f,g}(s,t,u)
=\sum_{\chi\bmod q}\sum_{\psi\bmod r}
A_f(\chi)B_g(\psi)
L_{MT,2}(s,t,u;\chi,\psi,\mathbf1),
}
\tag{14}
\]

with

\[
\boxed{
L_{MT,2}(s,t,u;\chi,\psi,\omega)
:=\sum_{k,l\ge1}
\frac{\chi(k)\psi(l)\omega(k+l)}
{k^s l^t(k+l)^u}.
}
\tag{15}
\]

Here `omega=1` is the trivial character. Equation (15) is precisely the standard character-weighted Mordell–Tornheim double `L`-function. The canonical Prime-Circle prime-support sources merely select a finite coefficient vector `A_f(chi)B_g(psi)` inside this established family. As in PC-311, those one-level coefficients reduce to finite character transforms of the prime-support source (equivalently Gauss factors times finite prime-character sums for nonprincipal characters); the nonlinear operation does not alter that source packet before inserting it into the classical double-`L` basis.

There is therefore no hidden infinite character expansion or conductor limit in (14): for fixed `q,r` it is a finite bundle of `(q-1)(r-1)` classical components, with some coefficients possibly zero.

## 5. Exact controls locate where the apparent new structure enters

The first control is `u=0`, initially interpreted by analytic continuation from an absolute-convergence region where the separated sums converge. Directly from (10), whenever the two one-variable Dirichlet series converge absolutely,

\[
\boxed{
Z_{q,r}^{f,g}(s,t,0)
=\left(\sum_{k\ge1}\frac{a(k)}{k^s}\right)
 \left(\sum_{l\ge1}\frac{b(l)}{l^t}\right).
}
\tag{16}
\]

Each factor is already a finite ordinary Dirichlet-`L` bundle. Thus the only new coupling in (10) is exactly the source-independent additive propagator `(k+l)^{-u}`.

The second control is the order of operations. If one replaces pointwise multiplication by the angular Haar pairing of PC-311 before Mellinization, orthogonality enforces a single shared Fourier index and returns the ordinary finite `L(s+t,chi)` bundle. Hence the present extra variables are not an inconsistency with PC-311; they record precisely the information preserved by delaying scalar angular compression.

The third control is source replacement. Equations (12)--(15) hold for **every** centered source at prime levels, not only for the prime-support source. Prime-Circle arithmetic enters through the finite coefficient vector, while the analytic kernel and its multiple-`L` continuation are universal.

## 6. Prior art and novelty audit

The analytic class in (15) is established. Hirofumi Tsumura, **On some functional relations between Mordell–Tornheim double L-functions and Dirichlet L-functions**, *Journal of Number Theory* 120:1 (2006), 161--178, DOI `10.1016/j.jnt.2005.11.006`, develops analytic functional relations for character-weighted Mordell–Tornheim double `L`-functions and ordinary Dirichlet `L`-functions. Kohji Matsumoto, Takashi Nakamura and Hirofumi Tsumura, **Functional relations and special values of Mordell-Tornheim triple zeta and L-functions**, *Proceedings of the American Mathematical Society* 136:6 (2008), 2135--2145, DOI `10.1090/S0002-9939-08-09192-2`, explicitly uses the general character-weighted Mordell–Tornheim `L`-function framework and identifies the double functions as its lower-rank predecessors.

Yuichiro Toma, **A relation between the Mordell–Tornheim multiple Dirichlet series and the confluent hypergeometric function**, *International Journal of Number Theory* 21:9 (2025), 2171--2183, DOI `10.1142/S1793042125501052`, arXiv:`2210.13033`, gives a modern analytic treatment of Mordell–Tornheim multiple Dirichlet series and obtains functional equations for double `L`-functions. The already-audited Jianqiang Zhao, **A Note on Colored Tornheim's Double Series**, *Integers* 10:6 (2010), 879--882, DOI `10.1515/integ.2010.059`, arXiv:`0907.5106`, supplies neighboring root-of-unity/colored Tornheim prior art.

A directed search did not locate the exact Prime-Circle formulation “multiply the two oriented Poisson fields, propagate their product by a third Poisson depth, then evaluate at the common anchor.” That absence is **not** a novelty claim. Once (9)--(15) are derived, the analytic object is visibly in the classical Mordell–Tornheim family.

There is also a strong zero-geometry warning against overinterpreting multiple-zeta functional structure. Takashi Nakamura, **The universality for linear combinations of Lerch zeta functions and the Tornheim–Hurwitz type of double zeta functions**, *Monatshefte für Mathematik* 162 (2011), 167--178, DOI `10.1007/s00605-009-0164-5`, proves universality and nontrivial zeros in a region of absolute convergence for a neighboring Tornheim–Hurwitz family. That theorem is **not** asserted here for the character-weighted bundle (14); it only reinforces the methodological boundary already exposed by PC-314/PC-315: a multiple-zeta functional equation or symmetry is not by itself a zero-selection theorem.

Accordingly no historical novelty is claimed for Mordell–Tornheim series, character-weighted multiple `L`-functions, their functional relations, or the Mellin/Laplace representation. The Mathia-specific content is the exact identification of the most canonical pre-compression nonlinear Prime-Circle Poisson product with this classical family.

## 7. Research consequence

This result is deliberately more nuanced than another scalar no-go. **Nonlinear cross-level coupling before angular compression really can preserve more information than PC-311:** the separate Fourier indices survive, and the downstream field supplies a genuine additive coordinate. The route therefore escapes the narrow one-variable `L(s+t,chi)` classification.

But the escape lands exactly in established Mordell–Tornheim multiple-`L` theory. Consequently the chain

\[
\text{two oriented prime-level Poisson fields}
\longrightarrow
\text{pointwise product}
\longrightarrow
\text{shared downstream Poisson propagation}
\longrightarrow
\text{triple Mellin transform}
\]

cannot be counted as a new RH mechanism merely because it produces more variables, a nonseparable denominator, meromorphic continuation, or functional relations. Those features are already native to the classical destination family.

A viable continuation must add a mathematically independent ingredient. The cleanest surviving question is whether the **specific canonical coefficient vector** selected by Prime-Circle prime-support sources forces a property of the finite Mordell–Tornheim bundle that is absent generically and is tied by an independent theorem to Riemann-zeta zero confinement. Failing that, a different nonlinear geometry would have to produce a kernel not reducible to the additive convolution coordinate `k+l` or to another established multiple-Dirichlet normal form.

This does not close arbitrary nonlinear cross-level operators, pointed matrix-valued states, shell-dependent tensors, or growing-level limits. It closes only the canonical pointwise-product plus common-Poisson-propagation route as a claim to a new analytic species.

## 8. Audit tests

The classification is exact and can be falsified locally:

1. Expand the two centered Hardy/Poisson fields and verify (6) by Cauchy multiplication.
2. Apply the positive-frequency Poisson semigroup and verify the exact translation identity (7).
3. At the anchor, Mellin-transform the three radial depths independently and recover the denominator `k^s l^t(k+l)^u` in (9)--(10).
4. Verify from centering that the coefficient sequences vanish on multiples of their prime conductors, then reconstruct them exactly from Dirichlet characters as in (12)--(13).
5. Substitute those expansions and compare term by term with the standard definition (15).
6. Set `u=0` in an absolute-convergence region and verify the separated product (16).
7. Replace multiplication by PC-311's angular Haar pairing and check that the two-index state collapses back to its one-index finite ordinary-`L` bundle.

Any extra source-dependent dependence on `(k,l)` that cannot be absorbed into the finite character coefficients, or any failure of the downstream semigroup to act through `k+l`, would invalidate the Mordell–Tornheim classification for this construction.
