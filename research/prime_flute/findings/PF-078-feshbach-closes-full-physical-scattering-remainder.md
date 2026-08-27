# PF-078 — a low/high resolvent split closes the physical-scattering remainder gate

**Status:** `POSITIVE / PROOF-LEVEL ANALYTIC CLOSURE IN THE FIXED-SHAPE FINITE-TANGENT REGIME`.

This finding closes the analytic gap isolated in PF-061.  PF-052 had established the graph-resolvent scaling for the extracted cluster of residual poles of a marked physical cusp-scattering coefficient.  PF-053 claimed the same limit for the full physical scattering block, but PF-061 correctly downgraded that step because the cited degeneration theory did not itself prove that the pole-subtracted holomorphic remainder stays uniformly `O(1)` in the singular double scaling `s=1-O(epsilon)`.

The missing estimate can be obtained directly from the Laplacian by a finite-dimensional Feshbach / low-high spectral decomposition.  The key point is that the only spectral subspace approaching zero is Burger's componentwise-constant graph sector.  Persistent cusp source and observation maps live in geometrically fixed cusp annuli, so they are uniformly bounded on the orthogonal complement.  Consequently every possible `1/epsilon` singularity of the physical scattering block comes from the finite-dimensional small-mode sector; after its actual principal parts are removed, the remainder is uniformly bounded.

The conclusion is restricted to **finite prime tangents with fixed positive graph shape**.  It does not construct a scattering matrix for the infinite prime flute, and it does not solve the separate arithmetic problem of realizing an arbitrary prescribed fixed shape by recurrent consecutive-prime patterns.

## 1. Fixed-shape prime-tangent degeneration

Let `Y_epsilon` be a finite-area genus-zero hyperbolic tangent in which `N-1` disjoint separating geodesics pinch as

\[
L_i(\varepsilon)=\varepsilon a_i+o(\varepsilon),
\qquad a_i>0,
\qquad i=1,\ldots,N-1.
\]

The stable limit is a chain of `N` thrice-punctured spheres.  Let

\[
G_a=
\begin{pmatrix}
a_1&-a_1&&\\
-a_1&a_1+a_2&-a_2&\\
&\ddots&\ddots&\ddots\\
&&-a_{N-1}&a_{N-1}
\end{pmatrix}
\]

be the weighted path Laplacian, with orthonormal eigenpairs

\[
G_a v_j=\mu_jv_j,
\qquad
0=\mu_0<\mu_1<\cdots<\mu_{N-1}.
\]

Burger's graph-degeneration theorem gives

\[
\boxed{
\lambda_{j,\varepsilon}
=\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon),
\qquad j=0,\ldots,N-1,
}
\]

where `lambda_0=0`.  Since the vertex pieces are fixed thrice-punctured spheres and all non-pinched geometry remains nondegenerate, the orthogonal complement of these `N` modes has a uniform spectral gap: there is `c>0` such that, for small `epsilon`,

\[
\sigma(\Delta_\varepsilon|_{Q_\varepsilon L^2})\cap[0,c)=\varnothing,
\]

where `P_epsilon` projects onto the `N` small modes and `Q_epsilon=I-P_epsilon`.

For `|lambda|<c/2`, spectral calculus therefore gives the exact split

\[
\boxed{
(\Delta_\varepsilon-\lambda)^{-1}
=
\sum_{j=0}^{N-1}
\frac{P_{j,\varepsilon}}
{\lambda_{j,\varepsilon}-\lambda}
+
R^\perp_\varepsilon(\lambda),
\qquad
\|R^\perp_\varepsilon(\lambda)\|\le \frac{2}{c}.
}
\]

This is the finite-dimensional Feshbach decomposition needed below.

## 2. Persistent-cusp scattering is a bounded boundary functional of the resolvent

Choose one original cusp on each limiting pants component.  These cusps persist through the pinching and can be normalized to width one.  In each such cusp choose a cutoff `chi_a` whose transition region lies in a fixed standard cusp annulus, independent of `epsilon`.

For `s` near `1`, put

\[
F_{a,\varepsilon}(s)
:=
(\Delta_\varepsilon-s(1-s))(\chi_a y^s).
\]

Because the cusp geometry and the cutoff are fixed, `F_{a,epsilon}(s)` is compactly supported in that fixed annulus, holomorphic in `s`, and uniformly bounded in `L^2` on a fixed neighbourhood of `s=1`.

The standard cutoff-resolvent construction of the Eisenstein series is

\[
E_{a,\varepsilon}(s)
=
\chi_a y^s
-
(\Delta_\varepsilon-s(1-s))^{-1}
F_{a,\varepsilon}(s),
\]

up to the harmless sign convention used for the Laplacian/resolvent.

The outgoing zero-mode coefficient in another persistent cusp is determined by the Cauchy data on a fixed normalized horocycle.  Boundary trace plus local elliptic regularity therefore gives a uniformly bounded observation map from a local `H^2` norm to that coefficient.  Equivalently, the standard compact-core formulation expresses the physical scattering matrix as a fractional-linear functional of the Neumann-to-Dirichlet map.  Thus, on the persistent marked cusp block, one may write

\[
\boxed{
\Phi_\varepsilon^{\rm mark}(s)
=
D_\varepsilon(s)
+
\mathcal B_\varepsilon(s)
(\Delta_\varepsilon-s(1-s))^{-1}
\mathcal F_\varepsilon(s),
}
\]

where `D_epsilon`, `B_epsilon`, and `F_epsilon` are holomorphic near `1` and uniformly bounded in the fixed-shape family.  No global infinite-flute scattering object is used.

## 3. All singular `1/epsilon` behaviour lies in the small-mode sector

Insert the resolvent decomposition with

\[
\lambda(s)=s(1-s).
\]

The complement term is uniformly bounded:

\[
\left\|
\mathcal B_\varepsilon(s)
R^\perp_\varepsilon(\lambda(s))
\mathcal F_\varepsilon(s)
\right\|
=O(1)
\]

uniformly for `s` in a fixed sufficiently small disk about `1`.

Hence any growth on the scale `1/epsilon` can only come from

\[
\sum_{j=0}^{N-1}
\frac{
\mathcal B_\varepsilon(s)P_{j,\varepsilon}
\mathcal F_\varepsilon(s)
}
{\lambda_{j,\varepsilon}-s(1-s)}.
\]

Let `s_{j,epsilon}` be the solution near `1` of

\[
s_{j,\varepsilon}(1-s_{j,\varepsilon})
=\lambda_{j,\varepsilon}.
\]

Then

\[
1-s_{j,\varepsilon}
=\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon).
\]

Since

\[
\lambda'(s)=1-2s,
\qquad
\lambda'(s_{j,\varepsilon})\to-1,
\]

each scalar denominator has a simple pole in the `s` variable with uniformly nonzero derivative.  Subtracting its actual principal part leaves a holomorphic term whose size is uniformly `O(1)`: this follows from Taylor expansion of `lambda(s)` and of the uniformly holomorphic finite-rank numerator.  There are only `N` such terms.

Therefore, if

\[
R_{j,\varepsilon}
:=
\operatorname*{Res}_{s=s_{j,\varepsilon}}
\Phi_\varepsilon^{\rm mark}(s),
\]

then for every smaller fixed disk about `1`,

\[
\boxed{
H_\varepsilon(s)
:=
\Phi_\varepsilon^{\rm mark}(s)
-
\sum_{j=0}^{N-1}
\frac{R_{j,\varepsilon}}
{s-s_{j,\varepsilon}}
=O(1)
}
\]

uniformly as `epsilon -> 0`.

This is exactly the estimate that PF-061 identified as missing.  It does not follow merely from meromorphic convergence of scattering; it follows from the uniform complement gap plus the bounded persistent-cusp source/observation maps.

## 4. Residues converge to graph spectral projectors

Burger's eigenfunction reduction gives, after normalization, convergence of every small eigenfunction to a function that is constant on each limiting pants component.  If `v_j` is the normalized graph eigenvector, the limiting value on the `i`-th pants is

\[
\frac{v_j(i)}{\sqrt{2\pi}},
\]

because every thrice-punctured sphere has area `2 pi`.

On a fixed persistent cusp annulus, elliptic regularity upgrades the `L^2/H^1` convergence used in the graph reduction to convergence of the zero Fourier coefficient on a fixed horocycle.  A residual eigenfunction has zero mode

\[
A_{j,i,\varepsilon}\,y^{1-s_{j,\varepsilon}}.
\]

Since `s_{j,epsilon}->1`, the fixed-horocycle factor tends to one, and therefore

\[
A_{j,i,\varepsilon}
\longrightarrow
\frac{v_j(i)}{\sqrt{2\pi}}.
\]

The standard Maaß--Selberg residual identity identifies the scattering residue matrix with the Gram/rank-one matrix of these residual cusp amplitudes.  Consequently

\[
\boxed{
2\pi R_{j,\varepsilon}
\longrightarrow
v_jv_j^*.
}
\]

For `j=0` this agrees with the universal pole at `s=1`: `Area(Y_epsilon)=2 pi N` and the constant graph eigenvector has entries `1/sqrt(N)`.

## 5. The full physical scattering block has the graph-resolvent blow-up

Set

\[
\boxed{
s_\varepsilon(z)
=1-\frac{\varepsilon z}{2\pi^2}.}
\]

For `z` outside `Spec(G_a)`,

\[
s_\varepsilon(z)-s_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}(\mu_j-z)+o(\varepsilon).
\]

The residue limit therefore gives

\[
\frac{\varepsilon}{\pi}
\frac{R_{j,\varepsilon}}
{s_\varepsilon(z)-s_{j,\varepsilon}}
\longrightarrow
\frac{v_jv_j^*}{\mu_j-z}.
\]

The bound from Section 3 implies

\[
\frac{\varepsilon}{\pi}
H_\varepsilon(s_\varepsilon(z))
\longrightarrow0.
\]

Summing the finite small-mode cluster yields

\[
\boxed{
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1}
}
\]

locally uniformly on compact subsets of

\[
\mathbb C\setminus\operatorname{Spec}(G_a).
\]

Thus the conclusion originally sought in PF-053 is recovered, but now by a direct low/high resolvent argument rather than by the continuity claim rejected in PF-061.

Taking the first diagonal entry gives

\[
\boxed{
\frac{\varepsilon}{\pi}
\Phi_{c_1c_1,\varepsilon}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
\langle e_1,(G_a-zI)^{-1}e_1\rangle.
}
\]

The right side is the endpoint Jacobi/Weyl `m`-function.  Since the endpoint is cyclic for a path with positive weights, it determines the ordered weights by Stieltjes/Jacobi inversion.

## 6. Prime-gap / distinguished-cuff meaning

For a tangent arising from ordered prime offsets with consecutive gaps `d_i`, the exact orthogonal-circle geometry gives

\[
\boxed{
L_k
=4\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}}.
}
\]

For large-prime realizations of the same bounded pattern, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

hence

\[
\boxed{
\frac{d_i}{d_j}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_i(P)-\ell_j(P)}2\right].
}
\]

Therefore the common divergent cuff scale disappears, while the **relative** cuff/gap profile survives as the weighted graph seen by the singularly rescaled physical scattering matrix of the finite tangent.

The construction preserves the original orthogonal-circle ordering and uses persistent cusps selected by that geometry.  The ambient interior/exterior inversion does not create an additional intrinsic scattering channel for the two-dimensional flute; the present result concerns the intrinsic finite-tangent cusp scattering already compatible with the earlier interior/exterior audit.

## 7. Serious novelty / prior-art audit

Known ingredients include:

- Burger's reduction of small eigenvalues/eigenfunctions of pinching hyperbolic surfaces to a weighted graph;
- the cutoff-resolvent construction of Eisenstein series and Maaß--Selberg residue identities;
- Schulze's resolvent convergence and approximate scattering theory for degenerating finite-geometry hyperbolic surfaces;
- the expression of physical cusp scattering through a compact-core Neumann-to-Dirichlet map (Levitin--Strohmaier);
- abstract Feshbach/Schur-complement and Weyl-function methods.

The point is therefore **not** that scattering, graph limits, or Feshbach reduction are new separately.  Directed searches for combinations of `degenerating hyperbolic surface`, `physical cusp scattering`, `weighted graph resolvent`, `Feshbach`, `Jacobi/Weyl function`, and `pinching` located these neighbouring theories but did not locate the specific singular limit

\[
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\to(G_a-zI)^{-1}
\]

or the low/high-resolvent proof that the pole-subtracted **physical** scattering remainder is uniformly bounded in the coalescing `s=1-O(epsilon)` regime.

No historical-priority claim is made.  The candidate novelty is narrow: a physical cusp-scattering scaling limit to Burger's weighted graph resolvent, with explicit normalization, specialized here to the exact prime-derived tangent geometry.

## 8. Boundaries and falsification criteria

This finding would be invalidated if any of the following fails in the fixed-shape family:

1. the complement of the `N` graph modes does not admit a uniform spectral gap near zero;
2. persistent-cusp source or outgoing-zero-mode observation maps acquire an unaccounted `epsilon^{-1}` amplification despite being supported on fixed normalized cusp annuli;
3. the residual scattering residue matrix has a normalization different from the Maaß--Selberg amplitude Gram matrix used above;
4. small eigenfunction convergence fails to control the zero Fourier amplitude on a fixed persistent cusp horocycle.

Items 1 and the componentwise eigenfunction convergence are part of the standard Burger/Buser degeneration mechanism.  Item 2 is precisely what the resolvent factorization controls.  Item 3 was separately audited in PF-061.  Item 4 is a local elliptic-regularity upgrade on nondegenerating cusp geometry and is the most useful place for a paper-level lemma with all Sobolev norms written explicitly.

A numerical check on a four- or five-cusp pinching family would also be highly informative: after removing no poles at all, the rescaled physical marked scattering block should approach the explicit finite matrix resolvent uniformly on compact `z`-sets away from graph eigenvalues.

## 9. Remaining limitations

- The result is **fixed-shape**: `a_i>0` are fixed as `epsilon->0`.  Hierarchical/multiscale patterns require iterated blow-ups or Schur complements.
- The result concerns **finite tangents**, not a global scattering matrix of the infinite prime flute.
- Existing prime-cluster results force strong multiscale patterns but do not automatically realize an arbitrary prescribed fixed positive shape.  Thus this analytic theorem and the strongest unconditional arithmetic constructions do not yet overlap in their most general forms.
- The limit proves a natural spectral encoding of relative gaps/cuffs; it is not by itself a mechanism for the Riemann zeros or RH.
