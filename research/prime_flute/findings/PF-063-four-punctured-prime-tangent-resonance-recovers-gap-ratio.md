# PF-063 — in the hierarchical four-punctured tangent, unmarked resonance data recovers the adjacent-gap ratio exactly

**Status:** `POSITIVE-CANDIDATE` + `EXACT-INVERSE-STATEMENT` for the finite tangent; no claim that these resonances are poles of a global scattering matrix for the infinite flute.

## Setup

Take the first nontrivial cusp-side tangent from PF-029/PF-034, determined by three prime offsets

\[
\eta_1<\eta_2<\eta_3,
\qquad
d_1=\eta_2-\eta_1,
\qquad
d_2=\eta_3-\eta_2,
\]

and write

\[
r:=\frac{d_1}{d_2}>0.
\]

The tangent \(Y_r\) is a finite-area four-punctured sphere. The exact orthogonal-circle / parabolic trace computation gives a distinguished simple separating geodesic \(\gamma_r\) with

\[
\boxed{
\sinh^2\frac{L_r}{4}=r,
\qquad
L_r=4\operatorname{arsinh}\sqrt r.
}
\]

For actual occurrences of the pattern at prime scale \(P\), the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so

\[
\boxed{
r=\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_1(P)-\ell_2(P)}2\right].
}
\]

Thus the tangent modulus is exactly the surviving contrast between two distinguished cuffs after their common divergent part is removed.

## 1. A quantitative regime in which \(\gamma_r\) is the unique systole

A shortest closed geodesic on a complete hyperbolic surface is simple. On a four-punctured sphere, any two distinct essential nonperipheral simple closed curves must intersect unless they are isotopic; the geodesic representative in a free homotopy class is unique.

The collar lemma says that if a simple closed geodesic \(\delta\) intersects \(\gamma_r\), then

\[
\ell(\delta)>2w(L_r),
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}.
\]

Hence \(\ell(\delta)>L_r\) whenever

\[
w(L_r)>\frac{L_r}{2}.
\]

This is equivalent to

\[
\sinh\frac{L_r}{2}<1,
\qquad
L_r<2\operatorname{arsinh}1.
\]

Using \(L_r=4\operatorname{arsinh}\sqrt r\), the condition is exactly

\[
\boxed{
0<r<r_*:=\sinh^2\!\left(\frac12\operatorname{arsinh}1\right)
=\frac{\sqrt2-1}{2}.
}
\]

Therefore, for

\[
0<r<\frac{\sqrt2-1}{2}\approx0.20710678,
\]

we have

\[
\boxed{
\operatorname{sys}(Y_r)=L_r
}
\]

and the systolic geodesic is unique.

This regime is automatically reached by the hierarchical prime patterns used in PF-045/PF-054, where \(d_1/d_2\to0\).

## 2. The resonance set recovers the gap ratio without any marking

For geometrically finite hyperbolic surfaces, Borthwick–Judge–Perry prove that the resonance set determines the primitive length spectrum (and conversely, up to the standard topological data). In particular, for the finite-area tangent \(Y_r\), the resonance set determines its systole length.

In the regime above, the systole is uniquely \(L_r\), so the unmarked resonance data determines

\[
\boxed{
r=\sinh^2\left(\frac{\operatorname{sys}(Y_r)}{4}\right).
}
\]

Combining with the prime-cuff asymptotics gives the exact inverse relation

\[
\boxed{
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_1(P)-\ell_2(P)}2\right]
=
\sinh^2\left(\frac{\operatorname{sys}(Y_r)}4\right),
}
\]

where \(\operatorname{sys}(Y_r)\) is determined by the unmarked resonance/length data of the tangent.

Equivalently, if \(\mathcal R(Y_r)\) denotes the full resolvent resonance set, then in this hierarchical regime

\[
\boxed{
\mathcal R(Y_r)
\Longrightarrow
\operatorname{sys}(Y_r)
\Longrightarrow
\frac{d_1}{d_2}
\Longrightarrow
\lim_{P\to\infty}(\ell_1-\ell_2).
}
\]

No cusp labels, eigenfunction norming constants, marked scattering residues, or preselected geodesic are required.

## 3. Relation to earlier findings

This does not contradict PF-048, which showed that the *small Laplace eigenvalues alone* of a longer weighted path need not determine all weights. PF-063 uses the full finite-tangent resonance/length data and a special complexity-one fact: once \(r\) is sufficiently small, the prime-derived curve is the unique systole.

It also does not contradict PF-062. The near-\(s=1\) renormalized Selberg-zeta germ collapses to the already-known small-spectrum polynomial. PF-063 instead uses the full resonance divisor / primitive length spectrum, not merely the near-one germ.

Nor does it repair the global Selberg/scattering theory of the infinite flute. The ordinary global zeta and trace constructions remain obstructed by the infinite accumulation of short primitive orbits. The rigorous statement here is attached to the finite pointed tangent \(Y_r\). Via PF-034/PF-050, repeated isolated occurrences of the prime pattern realize this finite geometry as a genuine spatial tangent of the infinite prime-flute.

## 4. Why this is spectrally stronger than the marked sojourn-time identity

PF-030 recovered \(d_1/d_2\) from a *marked* difference of scattering sojourn times; PF-031 correctly downgraded that to the classical shear/cross-ratio coordinate.

PF-063 is different. The input is an **unmarked spectral invariant**: the resonance set determines the length spectrum, whose least positive primitive length is singled out intrinsically. The geometric identification of that least length with \(L_r\) is forced by the collar lemma and the topology of \(S_{0,4}\).

Thus the inverse map does not presuppose which geodesic carries the gap ratio.

## 5. Novelty check

Known ingredients:

- the collar lemma and the fact that systoles are simple are classical;
- the topology of the four-punctured sphere is classical;
- Borthwick–Judge–Perry prove that resonance data determines the length spectrum for geometrically finite hyperbolic surfaces;
- systoles and their multiplicities on four-punctured spheres have been studied extensively.

Directed searches for combinations of prime gaps / consecutive prime gaps with four-punctured hyperbolic tangents, systoles, resonance sets, or inverse scattering did not reveal this specialization.

No priority claim is made for any individual ingredient. The candidate-specific statement is the composition

\[
\boxed{
\text{adjacent prime-gap ratio}
\to
\text{exact four-punctured tangent modulus}
\to
\text{unique systole}
\to
\text{unmarked resonance invariant}.
}
\]

## Research consequence

For hierarchical three-prime tangents, the full finite-tangent resonance data already distinguishes the prime-derived modulus exactly. The next useful question is not whether a spectral invariant sees \(d_1/d_2\) — it does — but whether a **spatially localized spectral observable of the infinite flute itself** converges strongly enough to this unique-systole resonance/length datum without importing the tangent as external information.
