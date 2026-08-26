# PF-041 — the reflection quotient orthospectrum accumulates at zero, so the natural orthogeodesic zeta/trace route also collapses

**Status:** `DECISIVE-NEGATIVE` for the branch that passes to the intrinsic zero-twist reflection quotient and tries to read the distinguished cuffs through its orthospectrum, Basmajian-type identities, orthogeodesic Poincare series, or billiard/wave trace.

## 1. The distinguished cuffs become canonical orthogeodesics

Let \(X\) be the zero-twist prime flute and let \(\tau\) be its intrinsic orientation-reversing reflection. In the standard zero-twist construction, the fixed set of \(\tau\) contains the geodesics \(\gamma_n\) joining consecutive punctures and the geodesic ray \(\beta\) orthogonal to every distinguished cuff \(\alpha_n\). Cutting by the fixed set gives a half-flute \(H=X/\langle\tau\rangle\) with totally geodesic boundary.

Each cuff \(\alpha_n\) is setwise invariant under \(\tau\) and intersects the fixed set orthogonally in two points. Hence its quotient is an orthogeodesic \(a_n\subset H\) and

\[
\boxed{\ell(a_n)=\ell_n/2.}
\]

Thus the original prime cuff law becomes an honest orthospectral law

\[
\boxed{
\ell(a_n)\sim \log\frac{4p_n}{g_n}.
}
\]

This is a natural embedding of the cuff sequence into a standard hyperbolic length datum; no new zeta has yet been defined.

## 2. But the same quotient contains orthogeodesics tending to zero

Previous prime-flute geometry established infinitely many simple primitive separating geodesics \(\sigma_j\subset X\), each enclosing a finite consecutive block of cusps, with

\[
L_j:=\ell(\sigma_j)\longrightarrow0.
\]

The zero-twist reflection preserves every cusp and therefore preserves the homotopy class of a separator around such a consecutive block. The geodesic representative is unique, so

\[
\tau(\sigma_j)=\sigma_j.
\]

These separators are not components of the fixed set. Their restriction under the reflection is therefore a reflection of the closed geodesic with two fixed points, and the quotient is an orthogeodesic \(b_j\subset H\). Doubling \(b_j\) recovers \(\sigma_j\), hence

\[
\boxed{
\ell(b_j)=L_j/2\longrightarrow0.
}
\]

Consequently the orthospectrum of the reflection quotient has zero as an accumulation point:

\[
\boxed{0\in\overline{\operatorname{Orth}(H)}.}
\]

This is compatible with the general fact that orthospectra are discrete for hyperbolic surfaces with **compact** geodesic boundary: the prime half-flute has a noncompact, infinite-length fixed boundary (PF-040), so that compact-boundary theorem does not apply.

## 3. The natural orthogeodesic Poincare series has no initial convergence half-plane

A standard dynamical series associated with an orthospectrum is

\[
\eta_H(s)=\sum_{a\in\mathcal O(H)}e^{-s\ell(a)}.
\]

For compact negatively curved surfaces with totally geodesic boundary, orthogeodesic Poincare series of this type are well defined for large \(\Re s\) and admit meromorphic continuation by microlocal/dynamical methods.

For the prime half-flute, the subsequence \(b_j\) already prevents the initial definition. For every fixed \(s\) with \(\Re s>0\),

\[
e^{-s\ell(b_j)}\longrightarrow1.
\]

Therefore the terms do not even tend to zero and

\[
\boxed{
\eta_H(s)\text{ diverges for every }\Re s>0.
}
\]

Likewise any ordinary Euler product built from the full orthospectrum,

\[
\prod_{a\in\mathcal O(H)}(1-e^{-s\ell(a)}),
\]

has factors tending to zero along \(b_j\), so it has no nonzero right-half-plane product regime.

This is the exact orthogeodesic analogue of PF-035 for closed geodesics.

Selecting only the special orthogeodesics \(a_n=\alpha_n/\tau\) avoids the short subsequence, but then one has simply relabeled the distinguished cuffs and returned to the cuff-only products already downgraded in PF-022/PF-037. Such a selected generating function is not the intrinsic orthospectral zeta of the quotient.

## 4. Basmajian-type identities do not rescue the branch

For a compact hyperbolic surface with geodesic boundary, Basmajian's identity uses the positive summands

\[
B(x)=2\log\coth(x/2)
\]

and reads

\[
\ell(\partial H)=\sum_{a\in\mathcal O(H)}B(\ell(a)).
\]

Extensions to complete infinite-type bordered surfaces are known under hypotheses such as one-dimensional-measure-zero limit set.

Along the prime short orthogeodesics,

\[
B(\ell(b_j))
=2\log\coth(L_j/4)
\sim2\log\frac{4}{L_j}
\longrightarrow+\infty.
\]

Hence the formal Basmajian sum is already divergent term-by-term along this subsequence. Moreover PF-040 showed that the fixed geodesic boundary itself has infinite length. Thus in the prime quotient the standard positive orthospectrum identity cannot produce a finite renormalized invariant: at best it degenerates to an infinite-equals-infinite statement, and any subtraction would require new noncanonical input.

The usual infinite-type extension does not automatically cure this. The zero-twist prime flute lies in the first-kind/parabolic regime established earlier in the project, whereas the Chen--Liu extension invokes the measure-zero-limit-set setting. More fundamentally, the explicit sequence \(b_j\to0\) already forces the divergence independently of that theorem's hypotheses.

## 5. Boundary billiard/wave trace is contaminated by the same short family

An orthogeodesic in \(H\) doubles across the totally geodesic boundary to a closed geodesic in \(X\). Equivalently it is a two-bounce periodic reflecting trajectory in the doubled billiard picture. Thus each \(b_j\) gives a periodic reflecting orbit of period

\[
2\ell(b_j)=L_j\to0.
\]

Its repetitions have periods \(kL_j\). For every \(t>0\), choosing \(k_j\sim t/L_j\) gives

\[
k_jL_j\to t.
\]

Therefore the periodic reflecting lengths generated by these short orthogeodesics are dense in \((0,\infty)\). This is the boundary counterpart of PF-036. Standard boundary Poisson/wave-trace theory relates possible singularities to periodic reflecting rays, but here no positive time window isolates the distinguished trajectories corresponding to \(a_n=\ell_n/2\).

Microlocal localization at one distinguished cuff/orthogeodesic does not restore prime-specific information: PF-037 already showed that the local constant-curvature germ is the universal hyperbolic cylinder determined by \(\ell_n\) alone.

## 6. Relation to the exact orthogonal-circle geometry and the two dualities

This argument uses the **intrinsic** zero-twist reflection \(\tau\), whose fixed geodesics are part of the exact orthogonal-circle realization of the flute. It should not be confused with the original ambient prime-circle inversion

\[
z\mapsto1/\bar z,
\]

which exchanges the planar interior/exterior and becomes equatorial reflection under the spherical compactification. The present negative result does not discard that ambient duality; it closes only the route in which the intrinsic reflection quotient is spectralized through its full orthospectrum.

## 7. Novelty check

Known ingredients:

- The reflection and fixed geodesics of a zero-twist tight flute are explicit in Arredondo--Morales--Ramirez, *Parabolicity of zero-twist tight flute surfaces and uniformization of the Loch Ness monster*.
- Basmajian's orthospectrum identity and its positive summand \(2\log\coth(\ell/2)\) are classical.
- Chen--Liu extend Basmajian/McShane-type identities to classes of complete infinite-type bordered surfaces with measure-zero limit set.
- Orthospectra are known to be discrete for hyperbolic surfaces with compact boundary; the prime half-flute is outside that compact-boundary regime.
- Chaubet proves meromorphic continuation of orthogeodesic Poincare series in the standard negatively curved surface-with-boundary setting, starting from a series convergent for large \(\Re s\).
- Guillemin--Melrose/Zelditch boundary wave-trace theory associates periodic reflecting rays with the boundary length spectrum.

No novelty is claimed for any of these general facts. The project-specific substantive negative is their conjunction with the exact prime-flute geometry:

\[
\boxed{
\text{distinguished cuffs become genuine orthogeodesics,}
\quad\text{but other prime-derived separators give orthogeodesics }\to0.
}
\]

That forces failure of every ordinary full-orthospectrum exponential series/product before analytic continuation can begin and makes positive-time billiard localization globally non-discrete.

## 8. Research consequence

The branch

\[
\boxed{
\text{zero-twist reflection quotient}
\to
\text{full orthospectrum / Basmajian / orthogeodesic Poincare series}
\to
\text{prime-sensitive zeta or wave trace}
}
\]

is closed in its standard form.

A surviving boundary construction would have to renormalize the infinite family \(b_j\to0\) **canonically before** forming an orthospectral series or trace. Merely deleting those arcs because they are inconvenient would leave a marked cuff generating function already covered by the earlier negative results.
