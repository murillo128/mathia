# PC-015 — spherical compactification is exact, but round-sphere linear spectralization collapses to Ramanujan data

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for any RH mechanism that uses only a fixed round sphere and a rotationally invariant linear operator.

## 1. Exact stereographic realization of the original geometry

Use inverse stereographic projection

\[
\Sigma(z)=\frac{(2\Re z,2\Im z,|z|^2-1)}{1+|z|^2}\in S^2.
\]

Then the original unit circle is the equator,

\[
|z|=1\iff Z=0,
\]

while

\[
z=0\mapsto(0,0,-1),\qquad z=\infty\mapsto(0,0,1).
\]

The original inside/outside inversion

\[
I(z)=\frac1{\bar z}
\]

becomes exactly reflection across the equatorial plane:

\[
\boxed{\Sigma(Iz)=(X,Y,-Z).}
\]

Thus the interior/exterior duality is an honest spherical involution, not merely a visual analogy.

## 2. Orthogonal circles become canonical spherical caps

Consider the Euclidean circle orthogonal to the unit circle through equatorial endpoints with midpoint angle \(m\) and half-separation \(\alpha\). Its center and radius are

\[
c=\sec\alpha\,e^{im},\qquad r=\tan\alpha.
\]

Its planar equation reduces to

\[
1+|z|^2=2\sec\alpha\,\Re(e^{-im}z).
\]

Under \(\Sigma\), this becomes the plane section

\[
\boxed{X\cos m+Y\sin m=\cos\alpha.}
\]

Hence the orthogonal circle is the boundary of a spherical cap of geodesic radius exactly \(\alpha\), centered at the equatorial point \((\cos m,\sin m,0)\). The cap boundary is invariant under equatorial reflection, and its northern/southern halves are the stereographic exterior/interior pieces.

This preserves the exact orthogonal-circle geometry while placing it in a compact two-sided object.

## 3. Primitive-shell logarithmic potential on the sphere

For the primitive shell

\[
\mu_n^*=\{e^{2\pi i a/n}:(a,n)=1\},
\]

define the spherical logarithmic chord potential

\[
G_n(\Sigma(z))=
\sum_{\zeta\in\mu_n^*}
\log|\Sigma(z)-\Sigma(\zeta)|.
\]

Using the stereographic chord-distance identity and \(|\zeta|=1\),

\[
\boxed{
G_n(\Sigma(z))
=
U_n(z)-\frac{\varphi(n)}2\log(1+|z|^2)
+\frac{\varphi(n)}2\log2,
}
\]

where \(U_n(z)=\log|\Phi_n(z)|\) is the planar primitive-shell potential of PC-003.

Consequently \(G_n\) is exactly invariant under equatorial reflection / inversion:

\[
\boxed{G_n(\Sigma(Iz))=G_n(\Sigma(z)).}
\]

Distributionally on the unit round sphere,

\[
\boxed{
\Delta_{S^2}G_n
=2\pi\sum_{\zeta\in\mu_n^*}\delta_{\Sigma(\zeta)}
-\frac{\varphi(n)}2.
}
\]

Thus every primitive shell is a neutral spherical charge distribution: cyclotomic point charges on the equator plus the canonical uniform background forced by compactness.

## 4. Decisive obstruction for linear round-sphere spectral methods

Let

\[
\nu_n=\sum_{(a,n)=1}\delta_{(\theta,\phi)=(\pi/2,2\pi a/n)}.
\]

Its spherical-harmonic coefficient is

\[
\widehat\nu_n(\ell,m)
=
\overline{N_{\ell m}P_\ell^{|m|}(0)}
\sum_{(a,n)=1}e^{-2\pi i ma/n}.
\]

The final sum is exactly the Ramanujan sum \(c_n(m)\). Hence

\[
\boxed{
\widehat\nu_n(\ell,m)
=
\overline{N_{\ell m}P_\ell^{|m|}(0)}\,c_n(m).
}
\]

Now let \(T\) be any linear rotationally invariant operator on the round sphere: for example a function of \(-\Delta_{S^2}\), a Green operator, heat/wave propagator, resolvent, or any zonal convolution. Then

\[
T Y_{\ell m}=\tau_\ell Y_{\ell m}
\]

for universal multipliers \(\tau_\ell\). Therefore

\[
\widehat{T\nu_n}(\ell,m)
=
\tau_\ell\overline{N_{\ell m}P_\ell^{|m|}(0)}\,c_n(m).
\]

So the entire output is determined by the classical Ramanujan sums of the primitive roots, passed through a universal spherical filter.

This rules out the broad branch

\[
\boxed{
\text{primitive vertices on a fixed round sphere}
\to
\text{linear SO(3)-equivariant spectral/PDE operator}
\to
\text{new RH-sensitive data}.
}
\]

The spherical projection is still geometrically useful, but novelty must come from something that the fixed linear sphere does not retain: nonlinear metric dependence, topology/puncture changes between levels, labeled multi-level interactions, or a genuinely non-equivariant construction already forced by the original geometry.

## Literature / novelty check

- The fact that the Fourier sums of primitive roots are Ramanujan sums is classical.
- Linear rotationally invariant operators on the round sphere diagonalize in spherical harmonics; therefore the collapse above is structural, not a literature gap.
- The exact stereographic realization of inversion and of the orthogonal circles is elementary inversive geometry; novelty is not claimed for those facts individually.
- Directed searches did not reveal a prior formulation of this particular prime-circle spherical package, but the negative conclusion itself follows from standard harmonic analysis once the construction is written down.

## Research consequence

Keep the spherical compactification and its exact hemisphere duality as part of the base geometry, but do not spend further effort on Laplacian/Green/heat/wave spectra of the **unchanged round sphere**. The next legitimate spherical objects must let the primitive shell change the surface or the metric itself.
