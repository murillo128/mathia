# PC-197 — the global Cauchy–Poisson character packet is classical Dirichlet-L data

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for using the source-native vertexwise angular/radial Cauchy–Poisson field of one primitive shell, followed by multiplicative-character decomposition and Mellinization in the intrinsic radial depth, as a new RH/GRH mechanism.

PC-025 showed that inserting a polylogarithmic order into the anchored chord profile manufactures `L(s,chi)` directly, so that route is not an independent spectral explanation. PC-179 later showed something stronger on the scalar radial side: the Mellin parameter can be genuinely source-native — dual to the actual radial depth — yet the aggregate signed flux still gives only the classical `Gamma(s) zeta(s)` packet. A natural remaining escape is therefore to avoid the scalar aggregate and retain the full vertexwise two-dimensional Cauchy/Poisson field before Mellinization.

That escape is exact but classical. The multiplicative Fourier transform of the full vertexwise field at a prime level is the complete family of nonprincipal Dirichlet characters, and its radial Mellin transform is exactly `Gamma(s)L(s,chi)` times the standard Gauss sum. The principal mode is precisely the signed radial flux of PC-179. Moreover the same formula holds for primitive characters of composite conductor, so the construction is not prime-specific.

## 1. The source-native complex radial field

Let `n>1`,

\[
\zeta_n=e^{2\pi i/n},
\qquad
U(n)=(\mathbb Z/n\mathbb Z)^\times,
\]

and put

\[
r=e^{-x},\qquad x>0.
\]

Resolve the cyclotomic logarithm into its primitive vertex factors,

\[
\ell_{n,a}(x):=\Log(1-r\zeta_n^a),
\qquad a\in U(n).
\]

Because the inverse primitive roots are the same set,

\[
\sum_{a\in U(n)}\ell_{n,a}(x)
=\log\Phi_n(e^{-x}).
\]

The first complex radial jet of one factor gives the canonical Cayley/Cauchy kernel

\[
\boxed{
K_{n,a}(x)
:=1+2\ell_{n,a}'(x)
=\frac{1+r\zeta_n^a}{1-r\zeta_n^a}.
}
\tag{1}
\]

This is not an externally chosen spectral family. It is the actual vertexwise derivative of the same logarithmic potential already intrinsic to Prime Circle. Its real and imaginary parts are the ordinary Poisson and conjugate-Poisson kernels:

\[
\boxed{
\operatorname{Re}K_{n,a}(x)
=\frac{1-r^2}{|1-r\zeta_n^a|^2},
}
\tag{2}
\]

\[
\boxed{
\operatorname{Im}K_{n,a}(x)
=\frac{2r\sin(2\pi a/n)}
{1-2r\cos(2\pi a/n)+r^2}.
}
\tag{3}
\]

Thus (1) retains both harmonic components that are lost by evaluating only the scalar radial potential. At the circle boundary,

\[
\boxed{
K_{n,a}(0+)=i\cot\frac{\pi a}{n},
}
\tag{4}
\]

so the field also interpolates continuously to the oriented cotangent/chord data already encountered elsewhere in the line.

For `x>0`, the absolutely convergent positive-frequency expansion is

\[
\boxed{
K_{n,a}(x)
=1+2\sum_{k\ge1}e^{-kx}\zeta_n^{ak}.
}
\tag{5}
\]

The radial variable has therefore produced a genuine Laplace semigroup on the additive angular modes before any arithmetic transform is applied.

## 2. Primitive multiplicative characters diagonalize the whole angular packet

Let `chi` be a primitive nonprincipal Dirichlet character modulo `n`, and define the multiplicative character mode

\[
\mathcal K_{n,\chi}(x)
:=\sum_{a\in U(n)}\overline{\chi(a)}K_{n,a}(x).
\tag{6}
\]

The constant term in (5) vanishes because `chi` is nonprincipal. The standard primitive Gauss identity gives, for every integer `k>=1`,

\[
\sum_{a\in U(n)}\overline{\chi(a)}\zeta_n^{ak}
=\chi(k)\tau(\overline\chi),
\tag{7}
\]

where

\[
\tau(\overline\chi)
=\sum_{a\bmod n}\overline{\chi(a)}e^{2\pi ia/n}.
\]

Substitution into (5) yields the exact radial character packet

\[
\boxed{
\mathcal K_{n,\chi}(x)
=2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)e^{-kx}.
}
\tag{8}
\]

At a prime level `p`, every nonprincipal character modulo `p` is primitive. Hence (8), together with the principal mode below, classifies the **entire multiplicative Fourier transform** of the vertexwise Cauchy–Poisson field on the primitive `p`-shell.

The parity split is geometric rather than additional arithmetic. The Poisson part (2) is even under `a -> -a`, while the conjugate-Poisson part (3) is odd. Consequently even characters live entirely in the Poisson component and odd characters entirely in the conjugate-Poisson component. Keeping the complex field (1) simply retains both parity sectors at once.

## 3. Intrinsic radial Mellinization gives `Gamma(s)L(s,chi)` exactly

The key difference from the polylogarithmic control in PC-025 is that no complex order has been inserted into the vertex kernel. The only continuous parameter in (8) is the actual radial depth `x`. Mellin-transforming that intrinsic scale gives, initially for `Re(s)>1`,

\[
\begin{aligned}
\mathcal M\mathcal K_{n,\chi}(s)
&:=\int_0^\infty
x^{s-1}\mathcal K_{n,\chi}(x)\,dx\\
&=2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)
\int_0^\infty x^{s-1}e^{-kx}\,dx.
\end{aligned}
\]

Since

\[
\int_0^\infty x^{s-1}e^{-kx}\,dx
=\Gamma(s)k^{-s},
\]

one obtains

\[
\boxed{
\mathcal M\mathcal K_{n,\chi}(s)
=2\tau(\overline\chi)\Gamma(s)L(s,\chi).
}
\tag{9}
\]

Thus a source-native two-dimensional Prime-Circle field really does reach a standard `L`-function with a source-native Mellin variable. But the result is exactly the classical Dirichlet `L`-family, not a new spectral divisor.

For prime `p`, equation (9) applies to every nonprincipal multiplicative mode. The zeros seen after Mellinization are therefore precisely the classical zeros of the corresponding `L(s,chi)`, with no additional prime-circle zero condition. The Gauss factor is also the familiar finite Fourier factor entering the classical Dirichlet functional equation; its appearance is not independent evidence for a new functional equation.

## 4. The principal character is exactly PC-179, not a second carrier

For the principal character, summing (5) over the primitive shell gives Ramanujan sums rather than a primitive Gauss transform:

\[
\begin{aligned}
\mathcal K_{n,1}(x)
&:=\sum_{a\in U(n)}K_{n,a}(x)\\
&=\varphi(n)
+2\sum_{k\ge1}c_n(k)e^{-kx}.
\end{aligned}
\tag{10}
\]

PC-179 defined

\[
\rho_n(x)
=-\frac{d}{dx}\log\Phi_n(e^{-x})
=-\sum_{k\ge1}c_n(k)e^{-kx}.
\]

Therefore

\[
\boxed{
\mathcal K_{n,1}(x)-\varphi(n)
=-2\rho_n(x).
}
\tag{11}
\]

The scalar signed radial flux is not merely analogous to the principal angular mode: it is **exactly** the centered principal multiplicative component of the full vertexwise Cauchy–Poisson field.

Using the PC-179 factorization gives

\[
\boxed{
\int_0^\infty
x^{s-1}
\bigl(\mathcal K_{n,1}(x)-\varphi(n)\bigr)\,dx
=2\Gamma(s)\zeta(s)
 n^{1-s}\prod_{q\mid n}(1-q^{s-1}).
}
\tag{12}
\]

For a prime `p`, the complete multiplicative packet is consequently

\[
\boxed{
\text{principal mode}
\;\longleftrightarrow\;
\Gamma(s)\zeta(s)(p^{1-s}-1),
}
\tag{13}
\]

and

\[
\boxed{
\chi\ne1
\;\longleftrightarrow\;
\tau(\overline\chi)\Gamma(s)L(s,\chi).
}
\tag{14}
\]

Up to the explicit elementary factors displayed above, the global angular/radial field is therefore the classical Dirichlet `L` packet.

## 5. Composite conductors are a decisive matched control

Nothing in (7)--(9) uses primality. For every modulus `n` and every primitive nonprincipal Dirichlet character of conductor `n`, the same primitive-root shell and the same Cauchy–Poisson field satisfy (8)--(9).

Thus prime levels do not uniquely generate the `L`-packet. Composite conductors supporting primitive characters produce the identical mechanism with their own classical conductor. At a prime level the only simplification is representation-theoretic: every nonprincipal character happens to be primitive, so the full multiplicative Fourier basis is exhausted by (9) plus the principal mode.

Imprimitive character modes do not create an escape. Their additive Fourier transforms factor through their primitive conductor with the usual finite local corrections, so they remain inside standard induced-character Dirichlet `L` theory. No new analytic species appears when the shell conductor is composite.

This matched control rules out interpreting either the appearance of `L(s,chi)` or the conductor `p` in a prime shell as a new prime-specific RH/GRH mechanism.

## 6. Boundary values connect back to the classical anchored spectrum

Equation (4) shows that the same radial packet has a finite boundary limit because no primitive `n`-th root equals the common vertex `1`. For nonprincipal primitive `chi`,

\[
\mathcal K_{n,\chi}(0+)
=i\sum_{a\in U(n)}
\overline{\chi(a)}\cot\frac{\pi a}{n}.
\tag{15}
\]

Parity now becomes explicit: the boundary cotangent is odd, so even characters vanish there while odd characters retain the familiar cotangent/Gauss special-value data. This is the boundary counterpart of the log-sine/Dirichlet-`L(1,chi)` package already classicalized in PC-025 and of the cotangent character transforms used elsewhere in Prime Circle.

At the opposite radial endpoint `x -> infinity`, every nonprincipal mode decays exponentially. The interior family therefore interpolates between classical finite cyclotomic character data at the circle and the ordinary Dirichlet Laplace series in depth; Mellinization does not introduce a second arithmetic carrier between those endpoints.

## 7. Functional-equation and critical-line audit

Equation (9) is a real bridge from the original two-dimensional geometry to standard analytic number theory, but it fails the novelty/RH gate for three separate reasons.

First, `L(s,chi)` is obtained coefficient-for-coefficient from the classical Gauss transform of the primitive roots and the Mellin transform of `e^{-kx}`. No unexplained spectral eigenvalue condition remains after the derivation.

Second, the completed Dirichlet functional equation is classical data of exactly this character/Gauss-sum package. The standard completion introduces the parity-dependent archimedean factor

\[
\Gamma\!\left(\frac{s+\varepsilon_\chi}{2}\right)
\]

and the conductor normalization required for `s <-> 1-s`. The raw disk-depth Mellin transform (9) instead supplies `Gamma(s)`. Recovering the standard completion by further classical analytic continuation or transform theory would recover the known Dirichlet functional equation, not derive a new Prime-Circle zero-confining principle.

Third, neither the pointwise positivity of each Poisson kernel (2) nor the harmonic-conjugate pairing supplies positivity after projection onto nonprincipal characters and analytic continuation. In particular, (9) gives no self-adjoint operator, de Branges structure, Weil positivity form, total-positivity theorem, or other mechanism forcing the zeros onto `Re(s)=1/2`.

Therefore the fact that the full field naturally contains the Dirichlet `L`-family is mathematically useful but not itself progress toward proving RH/GRH.

## 8. Prior-art and novelty audit

The ingredients are classical and already lie inside the line's recorded prior-art surface.

- The disk Poisson/Cauchy kernel and its Fourier series (5) are standard harmonic analysis.
- The primitive-character identity (7) is the classical Gauss-sum finite Fourier transform. PC-025 already records Montgomery--Vaughan as a modern source for the corresponding Gauss/Dirichlet-`L` special-value formulas.
- The Mellin identity `int_0^infinity x^{s-1}e^{-kx} dx = Gamma(s)k^{-s}` and the defining Dirichlet series for `L(s,chi)` are classical.
- PC-025 already classicalizes the same multiplicative shell coefficients when an external polylogarithmic order is used; PC-179 classicalizes the principal radial Mellin mode. The present result identifies the exact **source-native vertexwise completion connecting those two boundaries**.

Directed prior-art checks around Poisson kernels, Gauss sums, Dirichlet characters and Mellin transforms found the expected classical ingredients rather than a distinct Prime-Circle mechanism. No theorem-level historical novelty is claimed. The durable content is a scope theorem for this research program: retaining all vertexwise angular information before radial Mellinization does not escape into a new `L`-object; it fills out the standard Dirichlet character packet.

## 9. Research consequence

The natural repair

\[
\boxed{
\text{primitive vertexwise log field}
\to
\text{complex Cauchy/Poisson radial jet}
\to
\text{multiplicative character modes}
\to
\text{radial Mellin transform}
}
\]

is now classified. It is strictly richer than the scalar PC-179 transform and uses a source-native scale parameter rather than the inserted polylog order of PC-025, but its complete prime-level output is still only the classical principal zeta mode plus nonprincipal Dirichlet `L(s,chi)` modes.

This does **not** close the current hard frontier. It leaves untouched geometry-forced nonseparable couplings between distinct shells before character/Mellin diagonalization, couplings between this field and genuinely different old/new or chord operators with noncommuting eigenspaces, nonlinear global uniformization/monodromy data, and any construction that produces an independent positivity or functional-equation mechanism rather than merely realizing an already-known `L`-function.

The practical boundary is sharper: adding the full harmonic-conjugate/angular information to one radial primitive shell is not enough. A surviving mechanism must couple independent source-native structures **before** the abelian multiplicative character transform or the scalar Mellin transform turns them into standard Dirichlet `L` data.
