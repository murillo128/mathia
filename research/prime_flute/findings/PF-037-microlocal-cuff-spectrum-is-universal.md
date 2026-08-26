# PF-037 — microlocalizing a distinguished cuff recovers only its length, not additional prime-gap data

**Status:** `DECISIVE-NEGATIVE` for the branch that tries to rescue the distinguished cuff lengths from the globally divergent wave/Selberg trace by spatial or phase-space localization.

PF-036 shows that the global Selberg orbital measure has infinite mass on every positive length window, so a time cutoff cannot isolate a distinguished cuff. A natural remaining escape is to microlocalize the wave group near the closed geodesic itself. This does isolate that orbit in phase space, but on a constant-curvature hyperbolic surface its complete local spectral germ is universal and depends only on the cuff length already known from the prime geometry.

## 1. Exact local model around every cuff

Let \(\gamma\) be any simple closed geodesic of length \(\ell\) on a hyperbolic surface of curvature \(-1\). In Fermi coordinates around \(\gamma\), before the collar self-overlaps,

\[
\boxed{
 ds^2=dr^2+\ell^2\cosh^2 r\,d\theta^2,
 \qquad \theta\in\mathbb R/\mathbb Z.
}
\]

Thus the metric germ around \(\gamma\) is isometric to the corresponding germ of the standard hyperbolic cylinder

\[
C_\ell=\langle z\mapsto e^\ell z\rangle\backslash\mathbb H.
\]

The maximal standard embedded collar has half-width

\[
w(\ell)=\operatorname{arsinh}\!\frac1{\sinh(\ell/2)}.
\]

For the distinguished prime-flute cuff \(\gamma_n\), PF-032 gives the exact identity

\[
\boxed{
w(\ell_n)=\frac{h_n}{2},
\qquad
h_n=\log\frac{u_n}{u_{n-1}},
\qquad
u_n=\cot\frac{\pi}{p_n},
}
\]

or equivalently

\[
\boxed{
e^{-\ell_n/2}=\tanh(h_n/4),
\qquad
\ell_n=2\log\coth(h_n/4).
}
\]

Hence even the canonical collar width and the cuff length are not independent prime-derived moduli; they are the two standard coordinates of one universal hyperbolic cylinder.

The two-sided/interior-exterior symmetry also becomes locally universal: the Fermi reflection

\[
r\mapsto-r
\]

is an exact isometry because the metric coefficient is \(\cosh^2r\). Thus preserving the two sides of the original orthogonal-circle construction does not add a second local invariant at a single cuff.

## 2. Local Laplacian and transfer data depend only on \(\ell\)

On this cylinder the nonnegative Laplacian is

\[
\Delta_\ell
=-\partial_r^2-\tanh r\,\partial_r
-\frac{1}{\ell^2\cosh^2r}\,\partial_\theta^2.
\]

After Fourier decomposition in \(\theta\), every angular channel is a one-dimensional radial equation whose only cuff-dependent parameter is

\[
\frac{2\pi m}{\ell}.
\]

Therefore all spectral objects built solely from the canonical cuff collar — Dirichlet-to-Neumann maps on its boundary, local resolvents, cylinder scattering/transfer matrices, separated radial Jost data, or determinants of a truncated canonical collar — are universal functions of \(\ell\). Re-expressing them through \(h_n\), \(p_n\), or \(g_n\) does not create an additional arithmetic invariant.

## 3. The microlocal wave trace also contains only \(\ell\)

The transverse Jacobi equation along a closed geodesic in curvature \(-1\) is

\[
J''-J=0.
\]

Hence the linear Poincare return map of a primitive orbit of length \(\ell\) has multipliers

\[
\boxed{e^{\ell},\ e^{-\ell}.}
\]

In particular,

\[
\boxed{
|\det(I-P_\gamma)|^{1/2}=2\sinh(\ell/2).
}
\]

The standard local wave-trace coefficient of the primitive orbit is therefore, up to the universal phase/convention,

\[
\boxed{
A(\ell)=\frac{\ell}{2\sinh(\ell/2)}.
}
\]

For the \(k\)-th iterate the same local geometry gives the standard coefficient with \(k\ell\) in the Poincare denominator. More generally, the full microlocal wave-invariant germ near the orbit is determined by the metric jet along \(\gamma\); in constant curvature that jet is the universal Fermi metric above, so no independent local geometric data remain once \(\ell\) is fixed.

This is exactly why phase-space localization can evade the contamination found in PF-036 but cannot generate a new prime-specific relation. It recovers the already-known cuff length from a universal hyperbolic orbit model.

For example, using

\[
e^{-\ell_n/2}\sim \frac{g_n}{4p_n},
\]

the leading local wave amplitude has the asymptotic

\[
\boxed{
A(\ell_n)
\sim
\frac{g_n}{2p_n}\log\frac{4p_n}{g_n}.
}
\]

This is a genuine consequence of the prime-flute construction, but it is only the composition of the universal function \(A(\ell)\) with the already-known arithmetic formula for \(\ell_n\). It should therefore **not** be counted as a new spectral law of prime gaps.

## 4. What this rules out

PF-020/PF-036 ruled out isolating the distinguished cuffs in a global time trace because infinitely many iterated short orbits contaminate every positive time window. PF-037 closes the obvious microlocal escape:

\[
\boxed{
\text{distinguished cuff}
\to
\text{spatial/microlocal wave trace or collar transfer}
\to
\text{new prime-gap spectral invariant}
}
\]

does not work.

Microlocalization can isolate \(\gamma_n\), but every local spectral coefficient is a universal function of \(\ell_n\). Thus it contains no information about the surrounding prime configuration beyond what was already encoded in that one cuff.

This applies equally to the local hyperbolic-cylinder model used in resolvent/scattering constructions. To obtain genuinely new prime-sensitive spectral information, the observable must involve geometry outside a single constant-curvature collar: several cuffs/cusps at once, a nonlocal separating geodesic, a pointed tangent such as PF-034, or another spatially relative construction whose metric germ is not determined by one length.

## 5. Literature / novelty check

No novelty is claimed for the local facts:

- the hyperbolic cylinder \(C_\ell\) with metric \(dr^2+\ell^2\cosh^2r\,d\theta^2\) is the standard model used in the spectral geometry of geometrically finite hyperbolic surfaces;
- Duistermaat-Guillemin wave trace theory and later work of Guillemin/Zelditch express the local closed-orbit invariants through the Poincare map and the metric jet along the orbit;
- microlocal phase-space localization of individual closed geodesic contributions is standard and is explicitly used to separate near-multiple lengths in work such as Jakobson-Polterovich-Toth;
- in curvature \(-1\), the Jacobi equation fixes the Poincare multipliers to \(e^{\pm\ell}\).

The substantive point here is the negative specialization to the prime-flute: after PF-036 destroys global time localization, the strongest natural local repair still cannot expose anything beyond the scalar cuff length. This rules out an important remaining branch without imposing any extra assumptions on the rest of the infinite surface.
