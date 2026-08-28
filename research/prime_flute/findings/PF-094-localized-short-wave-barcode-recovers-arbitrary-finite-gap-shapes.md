# PF-094 — a localized short-wave barcode recovers arbitrary finite prime-gap shapes

**Status:** `POSITIVE / EXACT-HYPERBOLIC-BARCODE + LOCAL-WAVE-COROLLARY + CANDIDATE-NEW-COMPOSITION`. No RH claim.

PF-064 showed that, for a recurring isolated three-prime pattern, the first positive singularity of a spatially localized wave trace of the **single infinite prime-flute Laplacian** recovers one adjacent-gap ratio. The higher-punctured case had been left open because a scalar wave trace is unmarked and because repeats of very short geodesics can occur before the next primitive length.

For the strongly hierarchical tangents of PF-054 there is nevertheless an exact finite window in which the entire primitive length spectrum is forced to be the prime-derived pants cuffs. The standard hyperbolic wave-trace coefficients then permit primitive/repeat separation recursively. Consequently one geometrically selected localized scalar wave trace recovers an arbitrarily long finite projective gap vector.

The key new observation is the exact threshold `log 2`, obtained by combining the collar lemma with Yamada's universal lower bound for self-intersecting geodesics.

## 1. Exact tangent geometry

Let

\[
H=\{\eta_1<\cdots<\eta_r\},
\qquad
d_j=\eta_{j+1}-\eta_j,
\qquad j=1,\ldots,r-1,
\]

be an isolated prime pattern as in PF-034/PF-046. Its cusp-side tangent is the genus-zero finite-area surface

\[
Y_H\simeq S_{0,r+1}.
\]

The exact orthogonal-circle construction gives the nested separating geodesics

\[
\gamma_k,
\qquad k=2,\ldots,r-1,
\]

whose lengths satisfy

\[
\boxed{
\sinh^2\frac{L_k}{4}
=R_k
:=\frac{d_1+\cdots+d_{k-1}}{d_k}.
}
\tag{1}
\]

These `r-2` curves are the internal cuffs of the canonical zero-twist pants decomposition of `Y_H`.

The formula is Möbius invariant: it is the same cross-ratio formula obtained from the exact prime-circle endpoints before taking the tangent. Ambient inversion exchanging the interior/exterior pictures preserves every `L_k`, so the argument below does not choose one side of the prime-circle duality as a second intrinsic surface.

## 2. Exact short-primitive barcode lemma

Put

\[
c_*:=4\operatorname{arsinh}1
=2\operatorname{arccosh}3.
\]

Yamada's universal theorem says that every self-intersecting closed geodesic on an orientable hyperbolic surface has length at least `c_*`, with equality only for the figure-eight on the thrice-punctured sphere. Hence every primitive closed geodesic of length `<c_*` on `Y_H` is simple.

Now let

\[
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}
\]

be the standard half-width of the embedded collar about a simple geodesic of length `L`. There is an exact identity

\[
\boxed{
2w(\log 2)=4\operatorname{arsinh}1=c_*.
}
\tag{2}
\]

Indeed

\[
\sinh\frac{\log2}{2}=\frac1{2\sqrt2},
\qquad
2\sqrt2=\sinh(2\operatorname{arsinh}1).
\]

Assume now that every internal cuff satisfies

\[
\boxed{L_k<\log2.}
\tag{3}
\]

Any essential simple closed geodesic which is not one of the pants cuffs must intersect at least one cuff. By the collar lemma its length is at least

\[
2w(L_k)>2w(\log2)=c_*.
\]

Combining this with Yamada's bound gives the exact statement

\[
\boxed{
\mathcal L_{\rm prim}(Y_H)\cap(0,c_*)
=\{L_2,\ldots,L_{r-1}\}
}
\tag{4}
\]

with multiplicity.

Thus, below the fixed universal number `c_*`, the primitive length spectrum is not merely approximated by the prime-derived cuffs: **it is exactly the cuff set**.

PF-054 constructs recurrent patterns with

\[
L_2\gg L_3\gg\cdots\gg L_{r-1}\to0
\]

as the hierarchy parameter tends to infinity, so (3) eventually holds for every cuff and the ordering of the primitive barcode itself labels the indices `k`.

## 3. The barcode exactly determines the projective gap vector

Once the ordered lengths `L_k` are known, put

\[
R_k=\sinh^2(L_k/4).
\]

Equation (1) is triangular. Fix the irrelevant overall scale by setting `d_1=1`; then recursively

\[
\boxed{
 d_k=\frac{d_1+\cdots+d_{k-1}}{R_k},
 \qquad k=2,\ldots,r-1.
}
\tag{5}
\]

Therefore

\[
\boxed{
\{\text{ordered primitive lengths below }c_*\}
\Longleftrightarrow
[d_1:\cdots:d_{r-1}]
}
\tag{6}
\]

on the hierarchical prime-tangent family.

This is exact on each finite tangent; no Burger approximation, graph limit, determinant, or inverse-scattering theorem is needed for (6).

For a large-prime occurrence of the same pattern, the distinguished prime-flute cuffs satisfy

\[
\ell_j(P)=2\log\frac{4P}{d_j}+o(1),
\]

so the same recovered projective vector is equivalently the full finite vector of cuff contrasts

\[
\boxed{
\frac{d_j}{d_1}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_j(P)-\ell_1(P)}2\right].
}
\tag{7}
\]

Thus the short primitive barcode is a spectral-geometric encoding of the **relative**, not absolute, distinguished-cuff data.

## 4. One localized wave observable of the global infinite flute sees the barcode

Let `X_prime` be the complete infinite prime-flute. For a recurring isolated occurrence of `H`, let `Omega_m` be the corresponding embedded block and choose a smooth cutoff `chi_m` which is identically one on a fixed compact core containing all internal cuffs and which dies inside the two exterior collars. The cutoff can be chosen from a fixed profile of the signed collar-distance functions, so it is selected by the exact orthogonal-circle block geometry, not by selecting an individual spectral orbit.

As in PF-064, the exterior isolation makes

\[
\operatorname{dist}(\operatorname{supp}\chi_m,\partial\Omega_m)\to\infty.
\]

Define

\[
\Theta_m(t)
=
\operatorname{Tr}\!\left(
\chi_m\cos(t\sqrt{\Delta_{X_{\rm prime}}})\chi_m
\right)
\]

as a compactly supported distributional wave trace. Finite propagation and pointed smooth convergence give, for every fixed bounded time interval,

\[
\boxed{
\Theta_m\longrightarrow\Theta_{Y_H,\chi}
\quad\text{in }\mathcal D'.
}
\tag{8}
\]

No global trace formula or global scattering determinant is invoked.

For an isolated hyperbolic closed geodesic `gamma` of primitive length `L`, the standard local wave-trace singularity at its `q`-th repetition has nonzero leading coefficient proportional, in the constant-curvature normalization, to

\[
\boxed{
A_{\gamma,q}
=\frac{L}{2\sinh(qL/2)}.
}
\tag{9}
\]

Because `chi=1` near every internal cuff, localization leaves these leading orbital coefficients unchanged. If a repetition `qL_i` collides with another primitive cuff length, the corresponding leading coefficients add; after the already-known repeat contribution is subtracted, the extra primitive contribution remains nonzero. Starting from the smallest positive singular time and proceeding upward therefore recovers recursively the primitive closed-geodesic lengths below `c_*`, even though the strong hierarchy places many repetitions of the shortest cuff before the next cuff.

By (4), that recovered primitive support is exactly

\[
\{L_2,\ldots,L_{r-1}\}.
\]

Combining (5), (8), and (9) yields the global-Laplacian statement:

\[
\boxed{
\text{one block-localized wave trace on }X_{\rm prime}
\quad\Longrightarrow\quad
[d_1:\cdots:d_{r-1}]
}
\tag{10}
\]

in the pointed tangent limit.

Since PF-054 allows `r` to be arbitrarily large, the single infinite prime-flute contains recurring isolated blocks for which **arbitrarily long finite projective consecutive-gap vectors are recoverable from scalar localized wave data**.

## 5. Why this is stronger than the earlier spectral encodings

This result sits between several previous findings but is not their restatement.

- PF-054: unmarked **small Laplace eigenvalues** recover hierarchical gap ratios only asymptotically through Burger's graph limit.
- PF-051/PF-052/PF-078: marked scattering residues or Weyl data recover the ordered graph weights, but retain channel/eigenvector marking and use degeneration analysis.
- PF-064: the first positive localized wave singularity recovers one ratio on a four-punctured tangent.
- PF-094: the **full short primitive singularity barcode of one scalar spatially localized wave trace** recovers the entire finite projective gap vector, exactly at tangent level, with no channel marking and no low-energy graph approximation.

The result also explains why global wave/Selberg traces fail while local wave data succeed. PF-069 shows that the whole infinite surface has continuum-like positive-length accumulation and infinite primitive orbital mass on finite windows. Formula (4) says that after spatial isolation of one prime block, a universal finite time window becomes maximally rigid instead: its primitive spectrum is exactly the finite prime-derived pants decomposition.

## 6. Serious novelty audit

The analytic and hyperbolic ingredients are classical and no novelty is claimed for them:

1. Yamada's lower bound for self-intersecting geodesics (`4 asinh 1`) is classical; see Akira Yamada, *On Marden's universal constant of Fuchsian groups II*, J. Analyse Math. 41 (1982), together with the standard Buser formulation of the shortest non-simple geodesic theorem.
2. The collar lemma and the fact that a simple curve not belonging to a maximal pants decomposition intersects a pants cuff are standard.
3. Duistermaat--Guillemin/Chazarain local wave-trace theory gives the closed-orbit singularities and the Poincare-map coefficient; in curvature `-1`, `|det(I-P_gamma^q)|^{1/2}=2 sinh(qL/2)`.
4. Huber/Selberg theory classically recovers hyperbolic length data from spectral/trace data on finite-type surfaces.
5. Spatially localized wave traces and finite propagation on noncompact manifolds are standard; PF-064 already used exactly this analytic mechanism for one ratio.

Directed searches for combinations of `wave trace + pants decomposition + pinching parameters`, `localized wave trace + hyperbolic short geodesics`, `prime gaps + wave trace + hyperbolic surface`, and `prime gaps + length spectrum + pants decomposition` found the adjacent classical theories but not the composition (10).

The potentially new content is therefore deliberately narrow:

\[
\boxed{
\text{recurrent isolated consecutive-prime hierarchy}
\to
\text{exact orthogonal-circle tangent}
\to
\text{universal short-primitive barcode}
\to
\text{one localized global wave observable}
\to
\text{arbitrary finite projective prime-gap shape}.
}
\]

It should not be advertised as a new wave-trace theorem or a new pants-decomposition theorem.

## 7. Limitations and falsification checks

- The localization is geometrically marked by a selected prime-derived block. This is not an unmarked invariant of the global Laplace spectrum.
- The recovery is exact on the finite tangent and asymptotic for occurrences in the original prime-flute as the pointed tangent is formed.
- The ordering needed to turn the unlabelled barcode into the triangular recursion (5) uses the strong hierarchy of PF-054. Without that hierarchy, the same set of cuff lengths need not label the nested cuffs uniquely.
- If a primitive non-cuff closed geodesic of length `<c_*` existed under assumption (3), PF-094 would be false. Yamada + the collar lemma rule this out exactly.
- If the local wave singular coefficient of an internal cuff could vanish after a cutoff equal to one on that orbit, wave recovery would fail. The standard nondegenerate closed-orbit trace formula rules this out; curvature `-1` gives the explicit nonzero denominator in (9).

The most useful next mathematical move is not another scalar determinant. It is to determine whether the block localization in (10) can be replaced by a canonical operator-valued partition associated to the exact orthogonal-circle decomposition, so that the collection of local barcodes becomes an intrinsic decomposition of the global spectral measure rather than externally selected observations.
