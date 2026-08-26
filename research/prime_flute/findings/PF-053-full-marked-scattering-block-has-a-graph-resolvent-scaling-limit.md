# PF-053 — the full marked scattering block has a weighted-graph resolvent scaling limit

**Status:** `POSITIVE-CANDIDATE / ANALYTIC-GATE-OF-PF-052-CLOSED-IN-FIXED-SHAPE-REGIME`.

PF-052 proved the scaling limit for the principal polar part of one marked scattering coefficient and left two analytic gates: (i) convergence of residual cusp amplitudes to the weighted-path eigenvectors, and (ii) proving that the holomorphic remainder is negligible after the `epsilon` blow-up. In a standard fixed-shape pinching family both gates can be closed by combining Burger's eigenfunction reduction with meromorphic continuity of scattering under degeneration (Schulze). The natural statement is actually matrix-valued and stronger than PF-052.

The result concerns finite prime tangents and their canonical persistent cusp channels. It does **not** assert existence of a global scattering matrix for the infinite prime flute.

## 1. Geometric setting

Let `Y_epsilon` be a genus-zero finite-area hyperbolic tangent family obtained by pinching `N-1` disjoint separating geodesics so that

\[
L_i(\varepsilon)=\varepsilon a_i+o(\varepsilon),
\qquad a_i>0,
\qquad i=1,\ldots,N-1.
\]

Assume all non-pinched Fenchel--Nielsen data stay non-degenerate. In the prime-tangent case the stable limit is a chain of `N` thrice-punctured spheres, so there are no residual moduli in the vertex pieces.

Let

\[
G_a=
\begin{pmatrix}
a_1&-a_1&&\\
-a_1&a_1+a_2&-a_2&\\
&\ddots&\ddots&\ddots\\
&&-a_{N-1}&a_{N-1}
\end{pmatrix}
\]

be the ordinary weighted path Laplacian, with orthonormal eigenpairs

\[
G_av_j=\mu_jv_j,
\qquad
0=\mu_0<\mu_1<\cdots<\mu_{N-1}.
\]

Choose one **persistent original cusp** `c_i` on each limiting pants component, in the canonical order inherited from the prime vertices / orthogonal-circle construction. Normalize each primitive parabolic to width one. Let

\[
\Phi_\varepsilon^{\rm mark}(s)
:=
(\Phi_{c_i c_k,\varepsilon}(s))_{1\le i,k\le N}
\]

be the corresponding `N x N` principal submatrix of the physical scattering matrix.

## 2. Low spectrum and a uniform complement gap

Burger's graph-degeneration theorem, with each limiting pants component of area `2 pi`, gives

\[
\boxed{
\lambda_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon),
\qquad j=1,\ldots,N-1.
}
\]

The constant mode is `lambda_0=0`. Moreover the non-degeneracy of the complementary pieces gives a uniform spectral gap above these `N` modes: there is `C_0>0`, independent of `epsilon`, such that the rest of the small-energy spectrum is bounded below by `C_0`.

This uniform complement gap is explicit in the Burger/Buser degeneration framework and is restated, for example, in Theorem 3.1 of Mukherjee (arXiv:2603.21240, 2026).

Since the tangents have genus zero, the positive eigenvalues below `1/4` are residual rather than cuspidal. Write

\[
\lambda_{j,\varepsilon}
=s_{j,\varepsilon}(1-s_{j,\varepsilon}),
\qquad
\frac12<s_{j,\varepsilon}<1.
\]

Then

\[
\boxed{
1-s_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon).
}
\]

Include `j=0` with `s_{0,epsilon}=1`, `mu_0=0`.

## 3. Residue matrices converge to graph spectral projectors

Let

\[
R_{j,\varepsilon}
:=
\operatorname*{Res}_{s=s_{j,\varepsilon}}
\Phi_\varepsilon^{\rm mark}(s).
\]

Maaß--Selberg gives, for persistent cusp indices,

\[
(R_{j,\varepsilon})_{ik}
=
\left\langle
\operatorname*{Res}_{s_j}E_{c_i}(\cdot,s),
\operatorname*{Res}_{s_j}E_{c_k}(\cdot,s)
\right\rangle.
\]

For a simple residual eigenvalue this matrix is positive semidefinite of rank one. Burger's proof decomposes every normalized small eigenfunction into a componentwise-constant part plus a mean-zero error on the vertex pieces. In a fixed-shape family the error tends to zero, and elliptic regularity on a fixed normalized cusp collar upgrades this to convergence of the zero Fourier coefficient at a fixed horocycle.

A normalized graph eigenvector `v_j` corresponds to a limiting surface eigenfunction with constant value

\[
\frac{v_j(i)}{\sqrt{2\pi}}
\]

on the `i`-th pants component. Hence the full marked residue matrix satisfies

\[
\boxed{
2\pi R_{j,\varepsilon}
\longrightarrow
v_jv_j^{*}.
}
\]

This includes the universal pole at `s=1`: since `Area(Y_epsilon)=2 pi N`,

\[
R_{0,\varepsilon}
=
\frac{1}{2\pi N}\mathbf 1\mathbf 1^{*}
=
\frac1{2\pi}v_0v_0^{*}.
\]

Thus the residue-normalization gate left by PF-052 is closed in the fixed-shape regime.

## 4. The holomorphic remainder is uniformly bounded

Choose a small fixed disk `D` around `s=1`, contained in `Re(s)>1/2`, such that the limiting family has no spectral/scattering singularities in `D` other than the cluster above.

The uniform complement gap implies that, for sufficiently small `epsilon`, the only poles of the physical persistent-cusp scattering block in `D` are

\[
s_{0,\varepsilon},\ldots,s_{N-1,\varepsilon}.
\]

Define

\[
H_\varepsilon(s)
:=
\Phi_\varepsilon^{\rm mark}(s)
-
\sum_{j=0}^{N-1}
\frac{R_{j,\varepsilon}}{s-s_{j,\varepsilon}}.
\]

Schulze's degeneration theory proves meromorphic continuity of the (renormalized approximate) scattering matrix on the augmented Fenchel--Nielsen space away from `Re(s)=1/2`; on the channels corresponding to cusps that persist in the limit this is the ordinary physical scattering block. In particular, on a circle `partial D` avoiding `s=1`, the marked scattering block converges and is uniformly bounded.

The pole locations and residue matrices above converge to the `N` rank-one pieces of the pole of the disconnected limiting scattering problem at `s=1`. Therefore the principal-parts-subtracted family `H_epsilon` is uniformly bounded on `partial D`, and the maximum principle / Cauchy formula gives

\[
\boxed{
\sup_{s\in D'}\|H_\varepsilon(s)\|=O(1)
}
\]

for every smaller disk `D' compactly contained in D`.

Consequently, under the Burger blow-up, the regular part is killed automatically:

\[
\boxed{
\varepsilon
H_\varepsilon\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow0
}
\]

locally uniformly in `z` on compact sets.

This closes the second gate left by PF-052; no additional counterterm or ad hoc subtraction is required.

## 5. Full scattering-block scaling limit

Set

\[
s_\varepsilon(z)
:=
1-\frac{\varepsilon z}{2\pi^2}.
\]

For `z` off `Spec(G_a)`,

\[
s_\varepsilon(z)-s_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}(\mu_j-z)+o(\varepsilon).
\]

Using the residue limit,

\[
\frac{\varepsilon}{\pi}
\frac{R_{j,\varepsilon}}
{s_\varepsilon(z)-s_{j,\varepsilon}}
\longrightarrow
\frac{v_jv_j^*}{\mu_j-z}.
\]

Summing the finite cluster and using the bounded remainder gives the central result:

\[
\boxed{
\frac{\varepsilon}{\pi}
\Phi_\varepsilon^{\rm mark}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
(G_a-zI)^{-1}.
}
\]

The convergence is locally uniform on compact subsets of

\[
\mathbb C\setminus\operatorname{Spec}(G_a).
\]

Thus the **full physical marked scattering block**, not merely its extracted polar part, becomes the resolvent of the weighted dual graph.

The one-channel statement of PF-052 follows by taking the `(1,1)` entry:

\[
\boxed{
\frac{\varepsilon}{\pi}
\Phi_{c_1c_1,\varepsilon}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
\langle e_1,(G_a-zI)^{-1}e_1\rangle.
}
\]

Because `e_1` is cyclic for a positive weighted path, this single limiting channel determines the ordered weights `a_i` uniquely by Jacobi/Stieltjes inversion.

## 6. Prime-gap / cuff content

For a prime tangent with ordered gaps

\[
d_i=\eta_{i+1}-\eta_i,
\]

the exact orthogonal-circle geometry gives the separating lengths

\[
\boxed{
L_k
=4\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}}.
}
\]

In a fixed-shape pinching family, the normalized edge weights `a_i` are the first-order profile of these exact lengths. Recovering `G_a` therefore recovers the normalized ordered neck profile and, recursively, the ordered relative gap profile.

For large-prime realizations the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so

\[
\boxed{
\frac{d_i}{d_j}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_i(P)-\ell_j(P)}2\right].
}
\]

Hence the common divergent cuff scale disappears and the relative cuff/gap profile survives as the coefficients of the graph resolvent seen by physical tangent scattering.

## 7. Serious novelty check

The following ingredients are **not new**:

- Burger/Buser: low spectrum of a pinching hyperbolic surface converges to a weighted graph Laplacian.
- Mukherjee (arXiv:2603.21240, submitted 22 March 2026): a recent inverse-spectral construction explicitly uses Burger's weighted-graph limit for constant-curvature surfaces and records the uniform gap above the graph modes. This substantially downgrades any novelty claim based merely on `surface small spectrum -> weighted graph`.
- Maaß--Selberg: residues of Eisenstein/scattering data encode residual eigenfunctions.
- Schulze: resolvents and scattering data vary meromorphically through hyperbolic pinching; pinching-to-cusp scattering convergence is classical degeneration theory.
- Levitin--Strohmaier: the physical scattering matrix of a finite-area cusped hyperbolic surface is an explicit fractional-linear functional of the compact-core Neumann-to-Dirichlet map.
- Abstract scattering/boundary-triple theory contains many `scattering <-> Weyl function` formulas.
- Grieser's graph-neighborhood scattering work and the broader graph-like-manifold literature already show that graph operators can arise as scattering/spectral limits in other geometric regimes.

Directed searches for

- `degenerating hyperbolic surface scattering matrix weighted graph resolvent`,
- `pinching scattering graph Laplacian`,
- `Eisenstein residue graph Laplacian degeneration`,
- `Weyl function degenerating hyperbolic scattering graph`

found these adjacent theories but not the displayed near-`s=1` scaling law for the physical cusp scattering block of a pinching finite-area hyperbolic surface.

Therefore no novelty is claimed for graph degeneration or for scattering/Weyl theory separately. The candidate-new statement is narrowly:

\[
\boxed{
\text{persistent cusp scattering near the coalescing residual pole at }s=1
\xrightarrow{\text{forced blow-up}}
\text{resolvent of Burger's weighted dual graph},
}
\]

with the explicit constants `epsilon/pi` and `epsilon/(2 pi^2)`, specialized here to the prime-derived tangent geometry.

No historical-priority claim is made.

## 8. Limitations and next gate

1. The proof above is for a **fixed graph shape** `a_i>0`. Extremely multi-scale prime hierarchies, in which some normalized weights themselves tend to zero, require an iterated/multi-scale version. The matrix formula strongly suggests that the correct object is a nested Schur-complement / resolvent scaling, but that is not proved here.
2. The result is on finite tangents. It does not construct a global scattering theory for the infinite flute, whose infinite-cusp and short-orbit obstructions remain.
3. The arithmetic existence of prime-pattern sequences realizing a prescribed fixed positive shape is a separate sieve problem and is not claimed here.
4. This is not an RH mechanism. It establishes a natural spectral transfer law from relative prime-derived geometry to scattering data. A further global law across the naturally occurring tangent family would be needed before any RH relevance could be claimed.

The next mathematically clean test is the multi-scale version: determine whether repeated blow-ups / Schur complements of the same physical scattering block recover the hierarchy of edges when `L_{i+1}/L_i -> 0` at different rates. That would match the strongest prime patterns already available without imposing an unproved fixed-shape distribution theorem for consecutive prime gaps.
