# PC-025 — the anchored multiplicative spectrum is classical Dirichlet-L data

**Status:** `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the branch that applies multiplicative-character harmonic analysis, group-convolution determinants, or the obvious polylogarithmic spectral parameter to the anchored prime-level chord profile.

## 1. Exact anchored profile at a prime level

Let `p` be prime, let

\[
\zeta_p=e^{2\pi i/p},
\qquad
G_p=(\mathbb Z/p\mathbb Z)^\times,
\]

and retain the common vertex `1`. The oriented complex logarithmic profile of the chords from the anchor to the other vertices is

\[
\ell_p(a):=\Log(1-\zeta_p^a),
\qquad a\in G_p,
\]

with the principal/radial branch. Its real part is the literal logarithmic chord length

\[
\Re\ell_p(a)=\log|1-\zeta_p^a|
=\log\!\left(2\sin\frac{\pi a}{p}\right).
\]

The multiplicative group `G_p` acts by the canonical cyclotomic relabellings `a -> ha`. A natural attempt to retain more structure than the scalar common-vertex potential of PC-001 is therefore to analyze the entire anchored profile under multiplicative rather than additive Fourier modes.

## 2. The full multiplicative convolution spectrum

Define the convolution operator on functions `f:G_p -> C` by

\[
(T_pf)(x)
=
\sum_{a\in G_p}\ell_p(a)f(a^{-1}x).
\]

Every Dirichlet character `chi mod p` is an eigenvector. With

\[
\tau(\bar\chi)=\sum_{a\in G_p}\bar\chi(a)\zeta_p^a,
\]

the corresponding eigenvalue is

\[
\lambda_\chi
=
\sum_{a\in G_p}\bar\chi(a)\Log(1-\zeta_p^a).
\]

For every nonprincipal character modulo the prime `p`, expand radially

\[
-\Log(1-r\zeta_p^a)
=
\sum_{m\ge1}\frac{r^m\zeta_p^{am}}m,
\qquad 0<r<1,
\]

and use the standard Gauss-sum identity

\[
\sum_{a\in G_p}\bar\chi(a)\zeta_p^{am}
=
\chi(m)\tau(\bar\chi).
\]

Taking the Abel limit `r -> 1-` gives the exact identity

\[
\boxed{
\lambda_\chi
=-\tau(\bar\chi)L(1,\chi).
}
\]

The principal mode is equally explicit. Since

\[
\prod_{a=1}^{p-1}(1-\zeta_p^a)=p
\]

and the principal arguments cancel pairwise,

\[
\boxed{
\lambda_{\chi_0}=\log p.
}
\]

Thus PC-001 is the trivial multiplicative mode, while every nontrivial multiplicative mode is a Gauss-normalized Dirichlet `L(1,chi)` value.

## 3. What the real chord-length field retains

Let

\[
r_p(a)=\log|1-\zeta_p^a|.
\]

Because `r_p(-a)=r_p(a)`, all odd characters vanish:

\[
\boxed{
\sum_{a\in G_p}\bar\chi(a)r_p(a)=0
\qquad(\chi(-1)=-1).
}
\]

For every nonprincipal even character,

\[
\boxed{
\sum_{a\in G_p}\bar\chi(a)
\log|1-\zeta_p^a|
=-\tau(\bar\chi)L(1,\chi).
}
\]

This is the standard log-sine formula for `L(1,chi)` in prime-circle notation. The principal coefficient is again `log p`.

Consequently the complete multiplicative harmonic content of the **real** anchored chord fan at a prime level is already the classical package

\[
\boxed{
\log p
\quad+\quad
\{L(1,\chi):\chi\ne\chi_0,\ \chi(-1)=1\}
}
\]

up to explicit Gauss factors; the oriented complex logarithm also retains the odd-character data through its phase.

## 4. The obvious spectral parameter reconstructs Dirichlet L-functions by design

A particularly tempting escape is to replace the logarithm by a one-parameter fractional/polylogarithmic kernel. Define

\[
K_{p,s}(a):=\operatorname{Li}_s(\zeta_p^a).
\]

For `Re(s)>1` and nonprincipal `chi`, absolute convergence permits interchange of the finite character sum and the polylogarithm series:

\[
\begin{aligned}
\sum_{a\in G_p}\bar\chi(a)K_{p,s}(a)
&=\sum_{m\ge1}\frac1{m^s}
  \sum_{a\in G_p}\bar\chi(a)\zeta_p^{am}\\
&=\boxed{\tau(\bar\chi)L(s,\chi)}.
\end{aligned}
\]

At `s=1`, `Li_1(z)=-Log(1-z)`, recovering the anchored complex chord-log identity above.

Therefore a construction of the form

\[
\text{anchored chord profile}
\to
\text{multiplicative characters}
\to
\text{polylog/fractional order }s
\]

cannot count the zeros of the resulting `L(s,chi)` as a new spectral explanation. The `L`-function is already the exact multiplicative Fourier transform of the chosen polylogarithmic kernel.

This does **not** say that every conceivable shell-dependent operator is tautological. It rules out this canonical and very natural way of turning the anchored multiplicative profile into an `s`-dependent spectrum.

## 5. Determinants and class-number packages are classical too

For a finite abelian group, a convolution matrix is diagonalized by its group characters, and its determinant is the product of the character eigenvalues. Applying this to the anchored log-sine kernel means that determinant constructions from the multiplicative chord-relabelling matrix multiply the same `L(1,chi)` eigenvalues.

This is not a literature gap. Dedekind group determinants, log-sine matrices, cyclotomic class numbers, and the corresponding `L(1,chi)` character decomposition are classical and remain an active explicit-computation framework. In particular, modern work of Yang–Wang–Kanemitsu explicitly organizes log-sine class-number determinants through finite-abelian-group characters and convolution maps.

So the branch

\[
\boxed{
\text{anchored chord fan}
+G_p\text{ multiplicative relabelling}
\to
\text{character spectrum/determinant}
\to
\text{new RH mechanism}
}
\]

is closed as a novelty route.

## 6. Relation to the earlier prime-circle no-go results

This finding closes an escape hatch not covered by PC-021. That theorem assumes a **fixed** regular linear ambient probe before the scale transform; here the harmonic-analysis space and convolution operator depend on the level `p` through `G_p` itself.

It is also distinct from PC-024. There the relevant coordinates are the additive Fourier/Ramanujan modes of the primitive shell and finite same-index nonlinearities thereof. Here the coordinates are multiplicative characters of the unit labels.

PC-011 had already shown that low-order multiplicative relabelling statistics of the common-vertex chord fan produce Dedekind/Vasyunin sums. PC-025 upgrades that warning from selected moments to the full multiplicative harmonic decomposition of the anchored logarithmic chord profile: the eigenmodes are Dirichlet characters and the eigenvalues are classical Dirichlet `L`-values.

## 7. Prior art and novelty audit

No novelty is claimed for the character identities themselves.

- The Gauss-sum transform and the log-sine formulas for `L(1,chi)` are standard. Montgomery and Vaughan give an explicit modern statement for primitive even and odd characters, referring to the classical treatment in *Multiplicative Number Theory I*.
- Finite-abelian convolution, Dedekind determinants, log-sine entries, and their relation to cyclotomic class numbers are explicitly treated by Yang, Wang, and Kanemitsu.
- The polylogarithmic identity above is an immediate consequence of the defining series for `Li_s` and the standard Gauss-sum identity; it is recorded here as a falsifier of an obvious spectralization, not as a new theorem.

The prime-circle-specific contribution is the **scope classification**: once the common-vertex chord profile is decomposed under the natural multiplicative relabellings of a prime shell, its complete linear spectrum is already the standard Dirichlet-character package.

## 8. Research consequence

Do not spend further effort treating any of the following as an independent RH mechanism:

- the multiplicative Fourier transform of `a -> log|1-zeta_p^a|`;
- the oriented complex-log version of the same profile;
- convolution determinants built only from multiplicative relabellings of that profile;
- the polylogarithmic family `Li_s(zeta_p^a)` used to manufacture a spectral parameter.

The surviving anchored/nonlocal region must retain structure that is **not diagonalized away by the abelian character group of one level**. Examples include genuinely cross-level geometric interactions with nonseparable composition and, most notably, the nonlinear uniformization/accessory-parameter defect of PC-017, whose metric and projective connection depend globally on the puncture configuration rather than on a fixed group convolution kernel.
