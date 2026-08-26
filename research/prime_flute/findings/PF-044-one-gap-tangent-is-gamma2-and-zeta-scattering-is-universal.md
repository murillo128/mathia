# PF-044 — the one-gap tangent is Gamma(2), so its Riemann-zeta scattering is universal and gap-blind

**Status:** `DECISIVE-NEGATIVE` for any RH mechanism based on the scattering/resonance data of a two-prime / one-gap cusp-side tangent.

## 1. The minimal cusp-side tangent has no modulus

In the cusp-side tangent construction, retain only two consecutive prime offsets

\[
H=\{\eta_1<\eta_2\},\qquad d=\eta_2-\eta_1.
\]

The limiting ideal polygon is an ideal triangle. Its double is a complete finite-area hyperbolic sphere with three cusps. All ideal triangles are related by a Mobius isometry, equivalently the Teichmuller space of the thrice-punctured sphere is a point. Therefore

\[
\boxed{Y_H\cong S_{0,3}}
\]

independently of the numerical gap \(d\).

This is the exact hyperbolic expression of a fact already visible in the orthogonal-circle geometry: with only one relative spacing, an allowed Mobius normalization removes that spacing completely. The first cusp-side tangent with a genuine modulus requires at least three prime offsets, hence four punctures.

## 2. The surface is the classical congruence surface H/Gamma(2)

The unique complete thrice-punctured hyperbolic sphere is

\[
\boxed{S_{0,3}\cong \Gamma(2)\backslash\mathbb H,}
\]

where \(\Gamma(2)\) is the principal congruence subgroup of level two. It has index six in \(PSL_2(\mathbb Z)\), three cusp classes, each of width two.

Thus the minimal prime-flute tangent is not merely a generic finite-area surface: it is a classical arithmetic congruence surface before any prime gap has been specified.

## 3. Its scattering matrix already contains the Riemann zeta function

For the modular surface, the scalar scattering coefficient can be written

\[
\phi_{\rm mod}(s)
=
\sqrt\pi\,\frac{\Gamma(s-\tfrac12)}{\Gamma(s)}
\frac{\zeta(2s-1)}{\zeta(2s)}.
\]

Equivalently, by the zeta functional equation,

\[
\phi_{\rm mod}(s)
=
\pi^{2s-1}\frac{\Gamma(1-s)\zeta(2-2s)}
{\Gamma(s)\zeta(2s)}.
\]

Wolpert's explicit computation for \(\Gamma(2)\) gives a symmetric three-by-three scattering matrix whose entries are the same modular scalar factor multiplied by elementary rational functions of \(2^{2s}\) coming only from the width-two cusps. Schematically,

\[
\boxed{
\Phi_{\Gamma(2)}(s)
=\phi_{\rm mod}(s)\,M_2(s),
}
\]

where \(M_2(s)\) is explicit and contains no prime-gap datum.

Therefore the Riemann-zeta quotient, its functional equation, and its zero/pole divisor occur in the scattering theory of the one-gap tangent **universally**.

No use has been made of \(d\), of \(p_n\), or of the distinguished cuff asymptotic

\[
\ell_n\sim 2\log(4p_n/g_n).
\]

## 4. Why this is a decisive RH negative control

The tempting chain

\[
\text{one prime gap}
\longrightarrow
\text{finite cusp-side tangent}
\longrightarrow
\text{scattering matrix}
\longrightarrow
\zeta(s)
\]

is therefore misleading. The last arrow is present for every thrice-punctured sphere because that surface is \(\Gamma(2)\backslash\mathbb H\); the prime gap has already disappeared before scattering is formed.

In particular, under RH a nontrivial zeta zero

\[
\rho=\frac12+i\gamma
\]

enters the modular scattering quotient through

\[
\zeta(2s)=0
\quad\Longrightarrow\quad
s=\frac14+\frac{i\gamma}{2},
\]

and through

\[
\zeta(2s-1)=0
\quad\Longrightarrow\quad
s=\frac34+\frac{i\gamma}{2}.
\]

Thus the zeta-induced divisor is mirrored around the scattering symmetry line \(\Re s=1/2\), but it lies on the two lines \(\Re s=1/4\) and \(\Re s=3/4\) under RH, not on the Laplace continuous-spectrum parametrization line itself. This further rules out identifying the mere appearance of zeta in this scattering matrix with a Hilbert-Polya realization of the Riemann zeros.

The exact assignment of a particular zero to a zero or pole of an individual scattering eigenvalue can be affected by the elementary Gamma/level-two factors and should not be overstated. The robust statement is that the classical modular zeta quotient is a gap-independent factor of the full \(\Gamma(2)\) scattering data.

## 5. Relation to previous prime-flute findings

This strengthens the earlier negative that the generic cusp-scattering symmetry

\[
s\leftrightarrow1-s
\]

is universal. Here even the much more striking appearance of the **Riemann zeta function itself** is shown to be universal in the minimal tangent.

It also clarifies why the first potentially gap-sensitive tangent requires at least three prime offsets. For a four-punctured sphere the cross-ratio / shear is a genuine modulus; earlier work showed that direct marked sojourn times merely recover that classical modulus. Any genuinely spectral prime signal must therefore occur one level deeper, for example in moduli-dependent small eigenvalues, resonance locations, scattering eigenphases, or nontrivial Selberg data of four-or-more-punctured tangents.

## 6. Novelty check

The mathematical ingredients are classical:

- \(S_{0,3}\cong\Gamma(2)\backslash\mathbb H\);
- the explicit \(\Gamma(2)\) scattering matrix;
- the modular scattering coefficient involving \(\zeta(2s-1)/\zeta(2s)\);
- the scattering functional equation.

No novelty is claimed for any of these facts. The project-specific contribution is the negative control: the minimal cusp-side blow-up of the exact prime-flute geometry lands exactly on this arithmetic congruence surface, so any Riemann-zeta signature seen there is necessarily inherited from universal \(\Gamma(2)\) uniformization rather than from prime-gap fluctuations.

Directed searches found no prior discussion of this exact prime-gap/tangent comparison, but the conclusion follows rigorously from the uniqueness of the thrice-punctured sphere and the classical \(\Gamma(2)\) scattering formula.

## Research consequence

Do not count any occurrence of \(\zeta\), its functional equation, or its zero/pole pattern in the two-prime tangent scattering theory as evidence for a new RH mechanism. The first legitimate tangent-level spectral test is at fixed topology with at least four punctures, comparing **unmarked genuinely spectral data** for distinct prime-derived moduli rather than marked cross-ratios or sojourn times.
