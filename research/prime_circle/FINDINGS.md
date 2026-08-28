# Prime-circle findings

## PC-001 — the common-vertex potential is exactly von Mangoldt

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE` (geometric organization)

Let

\[
P_n^*=\{\zeta:\operatorname{ord}(\zeta)=n\}
\]

be the vertices that appear for the first time in the regular \(n\)-gon. Define their dimensionless logarithmic chord potential at the common vertex \(1\) by

\[
E_n:=\sum_{\zeta\in P_n^*}\log|1-\zeta|.
\]

Since

\[
\Phi_n(x)=\prod_{\zeta\in P_n^*}(x-\zeta),
\]

we have exactly

\[
E_n=\log|\Phi_n(1)|.
\]

For \(n>1\), the classical cyclotomic identity

\[
\Phi_n(1)=e^{\Lambda(n)}
\]

therefore gives

\[
\boxed{E_n=\Lambda(n).}
\]

Equivalently,

\[
E_n=\begin{cases}
\log p,&n=p^k,\\
0,&\text{otherwise.}
\end{cases}
\]

Thus the von Mangoldt source strength is not inserted into the original construction: it is the exact total logarithmic chord interaction between the common vertex and the new-vertex shell at level \(n\).

The Mellin/Dirichlet transform

\[
\sum_{n\ge2}E_n n^{-s}=-\frac{\zeta'(s)}{\zeta(s)}
\]

is classical and should **not** by itself be counted as a new RH mechanism. The potentially useful new direction is to retain the full two-dimensional potential field before taking this scalar transform.

### Literature check

The identity \(\Phi_n(1)=e^{\Lambda(n)}\) is classical and is explicitly discussed in Bzdęga–Herrera-Poyatos–Moree, *Cyclotomic polynomials at roots of unity*. The geometric logarithmic-chord interpretation is immediate from the defining product for \(\Phi_n\); novelty is not claimed for the identity.

---

## PC-002 — pairwise primitive-shell interaction detects prime-power scale jumps

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE`

For distinct primitive layers \(m<n\), define the total logarithmic interaction

\[
I_{m,n}:=
\sum_{\zeta\in P_m^*}
\sum_{\eta\in P_n^*}
\log|\zeta-\eta|.
\]

By the defining formula for the polynomial resultant,

\[
I_{m,n}=\log|\operatorname{Res}(\Phi_m,\Phi_n)|.
\]

Apostol's classical resultant theorem gives, for \(n>m>1\),

\[
|\operatorname{Res}(\Phi_m,\Phi_n)|
=
\begin{cases}
p^{\varphi(m)},&n/m=p^k\text{ for a prime }p,\\
1,&\text{otherwise.}
\end{cases}
\]

Hence

\[
\boxed{
I_{m,n}
=
\varphi(m)\,\Lambda(n/m)
}
\]

when \(m\mid n\), and \(I_{m,n}=0\) otherwise.

After normalization by the number of charges in the lower shell,

\[
\boxed{
\frac{I_{m,n}}{\varphi(m)}
=
\Lambda(n/m).
}
\]

So the original circle carries a canonical interaction graph on primitive layers in which nonzero couplings occur exactly across prime-power multiplicative jumps.

This suggests studying the **full interaction operator/geometry** before diagonalizing it by a Dirichlet transform. Immediately replacing it by \(-\zeta'/\zeta\) would only restate known arithmetic.

### Literature check

The resultant formula is classical: T. M. Apostol, *Resultants of cyclotomic polynomials*, Proc. AMS 24 (1970), 457–462. Later proofs and extensions exist. No novelty is claimed for the resultant itself.

---

## PC-003 — exact harmonic interior/exterior duality of primitive-shell potentials

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`

Define the logarithmic potential of the primitive layer

\[
U_n(z)=\log|\Phi_n(z)|
=\sum_{\zeta\in P_n^*}\log|z-\zeta|,
\qquad n>1.
\]

Away from the unit circle charges, \(U_n\) is harmonic. Cyclotomic reciprocity gives

\[
\Phi_n(z)=z^{\varphi(n)}\Phi_n(1/z),
\qquad n>1,
\]

and therefore, in modulus,

\[
\boxed{
U_n(z)
=
\varphi(n)\log|z|
+U_n(1/\bar z).
}
\]

Thus inversion in the original circle gives an **intrinsic exact inside/outside relation for the potential field**. Unlike the prime-flute interior/exterior picture, this duality belongs directly to the original roots-of-unity object.

At the common boundary vertex,

\[
U_n(1)=\Lambda(n),
\]

by PC-001.

The full polygon potential and primitive-shell potential are related by exact divisor/Möbius decomposition:

\[
\log|z^n-1|
=
\sum_{d\mid n}U_d(z),
\]

and formally away from singularities,

\[
\boxed{
U_n(z)
=
\sum_{d\mid n}\mu(n/d)\log|z^d-1|.
}
\]

This is currently the most promising original-geometry object: a two-sided harmonic field whose boundary charges are the genuinely new polygon vertices, whose common-vertex source strength is von Mangoldt, and whose inter-layer energies are cyclotomic resultants.

### Research gate

Do **not** count a Mellin transform of \(U_n(1)=\Lambda(n)\) as progress; that immediately recovers the classical logarithmic derivative of \(\zeta\). A substantive next step must use information in the full field \(U_n(z)\), its interior/exterior coupling, its Fourier/Ramanujan modes, or its scale-renormalization dynamics that is lost by evaluating only at \(z=1\).

---

## PC-013 — pure projective transfer is flat; Hill spectrum needs extra gauge

**Status:** `DECISIVE-NEGATIVE` for a spectral mechanism based only on the projective prime-vertex sequence.

Four consecutive prime-circle vertices have a genuine Möbius-invariant cross-ratio and therefore a standard discrete-Schwarzian / discrete-Hill interpretation. However, a globally defined projective moving frame has Maurer–Cartan transport

\[
K_n=\rho_{n+1}\rho_n^{-1},
\]

so every path product telescopes exactly:

\[
K_{N-1}\cdots K_m=\rho_N\rho_m^{-1}.
\]

Thus pure one-dimensional projective transport has no interior holonomy from prime-gap fluctuations.

The alternative unit-Wronskian Hill lift

\[
V_{n+2}=k_nV_{n+1}-V_n
\]

is also insufficient on the infinite nonperiodic prime path: it retains an alternating lift gauge \(V_n\mapsto c^{(-1)^n}V_n\), which changes \(k_n\) while preserving the projective cross-ratios \(s_n=k_nk_{n+1}\). The ambiguity genuinely changes the spectrum of the associated self-adjoint Schrödinger operator; even the projectively uniform sequence \(x_n=n\), with \(s_n\equiv4\), yields different period-two spectra under different allowed lift gauges.

Therefore cross-ratios alone do **not** canonically define a global spectral operator. A viable spectral construction must use additional structure already present in the original circle—Euclidean/unit-circle geometry, off-circle fields/interior-exterior duality, or a genuinely multidimensional labeled structure—rather than choosing a closure or lift normalization to manufacture a spectrum.

Full derivation: `findings/PC-013-pure-projective-transfer-is-flat-and-hill-spectrum-needs-extra-gauge.md`.

---

## PC-014 — exact Euclidean/unit-circle spectral transfer is subdivision-invariant

**Status:** `DECISIVE-NEGATIVE` for the most natural Euclidean repair of PC-013.

For the distinguished prime vertices \(z_n=e^{2\pi i/p_n}\), the exact angular increments are

\[
h_n=2\pi\left(\frac1{p_n}-\frac1{p_{n+1}}\right)
=\frac{2\pi g_n}{p_np_{n+1}}.
\]

Using the Euclidean circle to remove the projective lift ambiguity leads canonically to the exact one-dimensional Helmholtz/Dirichlet-to-Neumann element

\[
D_h(k)=k
\begin{pmatrix}
\cot(kh)&-\csc(kh)\\
-\csc(kh)&\cot(kh)
\end{pmatrix}
\]

and transfer matrix

\[
T_h(k)=
\begin{pmatrix}
\cos(kh)&\sin(kh)/k\\
-k\sin(kh)&\cos(kh)
\end{pmatrix}.
\]

This is exactly the \(\csc/\cot\) tridiagonal geometry suggested by the unit-circle lift. However,

\[
T_a(k)T_b(k)=T_{a+b}(k),
\]

so every finite prime block collapses to

\[
T_{h_m}(k)\cdots T_{h_N}(k)
=T_{2\pi(1/p_m-1/p_{N+1})}(k),
\]

and the infinite tail collapses to an ordinary arc of length \(2\pi/p_m\). All interior prime-gap fluctuations disappear exactly. Equivalently, Schur-complement elimination of any inserted prime vertex composes the two exact Dirichlet-to-Neumann elements into the one for their total length.

Thus a canonical one-dimensional spectralization of the Euclidean circle makes the prime vertices mere subdivision points. Freezing the \(k=1\) coefficients and then adding a new linear spectral parameter would produce a gap-sensitive Jacobi operator, but that extra spectral dependence is no longer derived from the exact circle geometry.

Full derivation: `findings/PC-014-euclidean-unit-circle-spectral-transfer-is-subdivision-invariant.md`.

---

## PC-015 — the full-field Dirichlet transform is Möbius inversion, not a new zeta mechanism

**Status:** `DECISIVE-NEGATIVE` + `LITERATURE+DERIVED` + `EXACT-DERIVED`.

For `|z|<1`, normalize `hat Phi_1(z)=1-z`, `hat Phi_n(z)=Phi_n(z)` for `n>=2`, and set `L_n(z)=Log hat Phi_n(z)`. The complete primitive-shell field has Fourier expansion

\[
L_n(z)=-\sum_{m\ge1}\frac{c_n(m)}m z^m.
\]

Its canonical Dirichlet scale transform satisfies, for `Re(s)>1`,

\[
\boxed{
\sum_{n\ge1}\frac{L_n(z)}{n^s}
=\frac1{\zeta(s)}\sum_{d\ge1}\frac{\Log(1-z^d)}{d^s}.
}
\]

Thus retaining the full two-dimensional harmonic field before applying `n^{-s}` does not escape the classical reduction: the `1/zeta(s)` factor is exactly Möbius inversion between full root-of-unity layers and primitive/cyclotomic layers. Bal's corrected 2026 arXiv version of *Constancy of an Infinite Cyclotomic Product via Ramanujan Sums* proves the corresponding weighted infinite-product identity explicitly.

The numerator is entire in `s` for fixed `|z|<1`; every zeta zero is therefore a genuine pole of this field transform for sufficiently small nonzero `z`, but this is inherited from the explicit reciprocal-zeta denominator and supplies no independent zero-location mechanism.

Likewise the exact PC-003 inversion law gives, after scale transformation,

\[
\boxed{
\mathcal U(s,z)-\mathcal U(s,1/\bar z)
=\log|z|\frac{\zeta(s-1)}{\zeta(s)}
}
\]

(initially for `Re(s)>2`). Spatial circle inversion leaves the same `s` on both sides; it does not produce `s -> 1-s` or the completed-zeta gamma factor. Hence the intrinsic inside/outside duality is **not** the zeta functional equation without an additional, independently derived operation on scale.

This closes the natural branch `full harmonic field -> ordinary Dirichlet/Mellin scale transform -> new RH mechanism`, and rules out treating circle inversion itself as the functional-equation reflection. Nonlinear mode/shell couplings, boundary-limit phenomena, and genuinely two-dimensional operators not diagonalized by `n^{-s}` remain open.

Full derivation and novelty audit: `findings/PC-015-full-field-dirichlet-transform-is-moebius-inversion.md`.
