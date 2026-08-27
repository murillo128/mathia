# PF-067 — generalized cusp scattering already solves the full inverse tangent problem

**Status:** `DECISIVE-NOVELTY-DOWNGRADE` for any claim whose substance is only that a full operator-valued cusp response / generalized scattering datum determines the prime-derived tangent and hence its relative gap profile.

## 1. Setup

For every finite prime-derived tangent `Y_H` produced in PF-029/PF-034, we have a geometrically finite finite-area hyperbolic surface with finitely many cusps. The exact orthogonal-circle construction determines its moduli from the relative prime-gap data. In the simplest nontrivial case,

\[
H=\{\eta_1<\eta_2<\eta_3\},\qquad
r=\frac{d_1}{d_2},
\]

and one separating geodesic satisfies

\[
\sinh^2\frac{L}{4}=r.
\]

More generally the nested separating lengths recover the ordered relative gap vector recursively.

PF-066 showed that the long prime-derived collar can be stripped exactly from the full Dirichlet-to-Neumann operator by a Schur-complement identity. It was tempting to regard

\[
\text{one canonical boundary response}
\Longrightarrow
Y_H
\Longrightarrow
\text{relative gaps}
\]

as a new inverse-spectral mechanism particular to the prime flute.

## 2. Prior art is substantially stronger

Isozaki–Kurylev–Lassas, *Conic singularities, generalized scattering matrix, and inverse scattering on asymptotically hyperbolic surfaces* (arXiv:1108.1577; later Crelle), define an operator-valued **generalized scattering matrix at a cusp** by allowing all Fourier modes, including exponentially growing incoming modes.

Their main inverse theorem states that for geometrically finite hyperbolic orbifolds, equality of the `(1,1)` component of the generalized S-matrix at isometric cusp ends determines the whole orbifold up to isometry/orbifold isomorphism.

Our tangents `Y_H` are a special nonsingular case, and after the standard cusp normalization their selected cusp ends are isometric. Therefore, directly from their theorem,

\[
\boxed{
\mathbf S^{\mathrm{gen}}_{11}(Y_H)
\quad\Longrightarrow\quad
Y_H\text{ up to isometry}.
}
\]

Since the exact prime geometry already gives

\[
Y_H\quad\Longrightarrow\quad
(d_1:\cdots:d_{r-1}),
\]

we obtain only the classical corollary

\[
\boxed{
\mathbf S^{\mathrm{gen}}_{11}(Y_H)
\quad\Longrightarrow\quad
(d_1:\cdots:d_{r-1}).
}
\]

Thus **unique recovery of the prime-gap profile from the full generalized cusp scattering operator is not a new inverse-scattering phenomenon**.

## 3. The overlap with PF-066 is especially direct

The same paper proves the inverse theorem by cutting the cusp at an artificial boundary and recovering the interior Neumann-to-Dirichlet map.

In their Lemma 4.7, equality of the generalized cusp S-matrix component implies equality of the N-D maps on the truncating boundary. Their Corollary 4.8 then analytically continues that boundary map and identifies the boundary spectral data / Green kernel needed by the boundary-control reconstruction.

Schematically,

\[
\boxed{
\mathbf S^{\mathrm{gen}}_{11}
\Longrightarrow
\Lambda_{\mathrm{interior}}(z)
\Longrightarrow
\text{boundary spectral data}
\Longrightarrow
\text{surface}.
}
\]

This is conceptually the same layer-stripping / boundary-response route that PF-066 had reached from the exact maximal prime collar.

PF-066 still contributes a useful **prime-flute-specific canonical de-embedding**: the orthogonal-circle neck chooses the collar and its limiting horocycle automatically. But the inverse uniqueness after the collar is removed is classical.

## 4. Important distinction: this does NOT kill the physical-scattering branch

Isozaki–Kurylev–Lassas explicitly explain why the ordinary physical cusp S-matrix is weaker. For a cusp, the continuous spectral channel is one-dimensional; the ordinary physical `(1,1)` cusp scattering coefficient is therefore only a scalar and, in their words, does not contain enough information to determine the whole manifold. Their generalized S-matrix adds all nonzero Fourier modes precisely to overcome this loss.

Therefore this finding does **not** invalidate the narrower candidates that use less data:

- PF-051: residues of the ordinary finite-dimensional physical scattering matrix near residual poles;
- PF-052: the conjectural / partially proved Jacobi Weyl scaling limit of one marked physical channel;
- PF-063: recovery of a hierarchical four-punctured gap ratio from unmarked resonance data through the unique systole;
- any future claim that a *finite-dimensional physical* scattering block, or only its poles/residues, recovers more geometry than generic inverse-scattering theory guarantees.

Those remain genuinely more restrictive inverse problems.

## 5. Consequence for novelty policy

From now on, the following chain should **not** count as a new prime-flute spectral discovery:

\[
\boxed{
\text{full generalized cusp S-matrix / full boundary response}
\to
\text{recover tangent geometry}
\to
\text{recover relative gaps}.
}
\]

That is already covered by general inverse scattering / Calderón theory once the tangent is known to be geometrically finite.

A substantive new result must instead use materially weaker spectral data or produce a new scaling law. Examples that still clear this gate include:

1. a single ordinary physical scattering coefficient;
2. only poles, residues, or resonance sets;
3. an explicit singular limit converting physical scattering into the weighted prime-gap graph operator;
4. a statement intrinsic to the infinite flute rather than the finite tangent;
5. a quantitative formula linking cuff contrasts to spectral quantities, not merely abstract uniqueness.

## 6. Literature check

Primary prior art:

- H. Isozaki, Y. Kurylev, M. Lassas, *Conic singularities, generalized scattering matrix, and inverse scattering on asymptotically hyperbolic surfaces*, arXiv:1108.1577; their Theorem 1.3 treats geometrically finite hyperbolic orbifolds.
- In the same paper, Lemma 4.7 and Corollary 4.8 explicitly recover the interior N-D map and boundary spectral data from one generalized cusp scattering component.
- Classical Calderón results on Riemann surfaces separately show that full Dirichlet-to-Neumann data determines the conformal structure of a compact bordered surface; for curvature `-1`, the conformal class fixes the complete hyperbolic metric once the puncture/boundary data are fixed.

The novelty downgrade is therefore decisive at the level of **full operator-valued boundary/scattering data**.

## Research consequence

Do not spend further effort proving abstract inverse uniqueness from the collar-stripped full DtN operator or from the generalized cusp S-matrix of `Y_H`. The useful remaining questions are whether much smaller physical data — especially ordinary scattering poles/residues or one marked scalar channel — still recover the weighted gap path, and whether that recovery survives as a localized statement on the infinite prime flute.
