# PF-051 — marked tangent scattering residues recover the weighted gap path

**Status:** `POSITIVE-CANDIDATE / EXACT-SCATTERING-IDENTITY + CLASSICAL-DEGENERATION`; the pole-location law is rigorous once PF-047 applies. The residue-to-graph-eigenvector identification is rigorous for simple, spectrally separated small modes and remains a quantitative stability gate for arbitrarily multi-scale families.

PF-047--PF-050 show that hierarchical prime-gap tangents carry a canonical weighted-path small spectrum and that a local endpoint spectral measure recovers the ordered relative gap vector. This note asks whether the finite tangent itself already contains the missing norming data in a standard spectral object, without choosing a first-pants test function.

For genus-zero finite-area tangents the answer is yes at the level of **marked scattering residues**. The small eigenvalues are residual rather than cuspidal, hence are poles of the cusp scattering matrix. Maaß--Selberg identifies the residue matrix at each pole with the Gram matrix of the corresponding residual eigenfunctions. In the simple-eigenvalue regime this matrix is rank one and its vector factor records the cusp zero-mode amplitudes of the residual eigenfunction. Under the same pinching degeneration used in PF-047, those amplitudes converge to the component constants / graph eigenvector entries. Therefore pole positions plus marked residue matrices asymptotically supply the full Jacobi spectral data, and hence recover the ordered relative gap/cuff path.

The scattering **determinant or pole set alone does not have this inverse power**: at leading graph order it inherits the isospectral-path ambiguity of PF-048. The residue matrices are the essential additional data.

## 1. Prime tangent and weighted path

Let

\[
H=\{\eta_1<\cdots<\eta_r\},\qquad d_i=\eta_{i+1}-\eta_i,
\]

be a recurrent isolated hierarchical prime pattern and let `Y_H` be its finite cusp-side tangent. The nested separating curves have exact lengths

\[
\boxed{
L_k=4\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}},
\qquad k=2,\ldots,r-1.
}
\]

In the hierarchical degeneration all `L_k -> 0`; cutting along them gives a chain of `N=r-1` pants components of equal area `2 pi`. Let `G_H` be the ordinary weighted path Laplacian with edge weights

\[
w_i=L_{i+1},\qquad i=1,\ldots,N-1,
\]

and eigenvalues

\[
0=\mu_0<\mu_1<\cdots<\mu_{N-1}.
\]

PF-047 records Burger's asymptotic

\[
\boxed{
\lambda_j(Y_H)=\frac{1}{2\pi^2}\mu_j(G_H)(1+o(1)),
\qquad j=1,\ldots,N-1.
}
\]

The weighted path has simple spectrum because all edge weights are positive.

## 2. In genus zero every small eigenvalue is residual

Every tangent `Y_H` has genus zero and finite area. A theorem of Huxley, reproved/topologically generalized by Otal, says that finite-area hyperbolic surfaces of genus zero or one have no cuspidal eigenfunction with eigenvalue at most `1/4`.

Hence every positive tangent eigenvalue

\[
0<\lambda_j<\frac14
\]

is residual. There is therefore a pole

\[
\frac12<s_j<1
\]

of the Eisenstein/scattering theory such that

\[
\boxed{
\lambda_j=s_j(1-s_j).
}
\]

Since the PF-047 modes satisfy `lambda_j -> 0`, necessarily `s_j -> 1`, and

\[
1-s_j=\lambda_j+O(\lambda_j^2).
\]

Combining with Burger gives the first scattering law

\[
\boxed{
1-s_j
=\frac{1}{2\pi^2}\mu_j(G_H)(1+o(1)).
}
\]

Thus the complete vector of small weighted-path eigenvalues reappears as the first-order distances of the tangent scattering poles from `s=1`.

For a four-punctured tangent (`r=3`), the path has one edge `L_2`, hence `mu_1=2L_2`. Therefore

\[
\boxed{
1-s_1\sim\frac{L_2}{\pi^2}
\sim\frac4{\pi^2}\sqrt{\frac{d_1}{d_2}}
\sim\frac4{\pi^2}e^{-(\ell_1-\ell_2)/4}
}
\]

in the pinching regime `d_1/d_2 -> 0`. This is a genuine cuff-contrast-to-scattering-pole asymptotic inside a fixed topological type.

## 3. Maaß--Selberg turns scattering residues into norming data

Let the cusps of `Y_H` be marked by their canonical order inherited from the prime vertices, together with the final cusp at infinity. Normalize each cusp by its primitive parabolic so that its translation width is one. This normalization is intrinsic up to horocyclic translation, which does not alter the constant Fourier coefficient.

Let

\[
\Phi_H(s)=(\phi_{ab}(s))
\]

be the corresponding marked scattering matrix, and let

\[
R_j:=\operatorname*{Res}_{s=s_j}\Phi_H(s).
\]

For each cusp `a`, write

\[
\rho_{a,j}(z):=\operatorname*{Res}_{s=s_j}E_a(z,s).
\]

The Maaß--Selberg relation gives the exact identity

\[
\boxed{
(R_j)_{ab}
=\langle \rho_{a,j},\rho_{b,j}\rangle_{L^2(Y_H)}.
}
\]

In particular `R_j` is positive semidefinite.

If the residual eigenspace at `lambda_j` is one-dimensional, choose a normalized eigenfunction `u_j`. Then

\[
\rho_{a,j}=c_a^{(j)}u_j
\]

for some cusp-amplitude vector `c^{(j)}`, and therefore

\[
\boxed{
R_j=c^{(j)}(c^{(j)})^*.
}
\]

So the residue matrix is rank one and determines `c^{(j)}` up to one irrelevant global phase/sign. Ratios are read directly, for example

\[
\frac{c_a^{(j)}}{c_b^{(j)}}
=\frac{(R_j)_{ab}}{(R_j)_{bb}}
\]

whenever the denominator is nonzero.

The zero Fourier coefficient of `rho_{a,j}` at cusp `b` is exactly

\[
\boxed{
(R_j)_{ab}\,y^{1-s_j}.
}
\]

Equivalently, the zero-mode coefficient vector of the normalized residual eigenfunction `u_j` is proportional to the rank-one factor `c^{(j)}`.

## 4. Pinching identifies residue vectors with graph eigenvectors

In the PF-047 degeneration, a normalized small eigenfunction becomes asymptotically constant on each pants component. Burger's reduction writes the low mode as a componentwise constant part plus a mean-zero remainder whose low-energy contribution vanishes.

Choose one original cusp canonically in each limiting pants component:

- on the first endpoint pants use its first prime cusp;
- on each interior pants use its unique original prime cusp;
- on the final endpoint pants use the final prime cusp (or, equivalently, the distinguished infinity cusp with a fixed convention).

No new boundary labels are introduced: every selected cusp is already marked by the cyclic prime order of the exact orthogonal-circle tangent.

For the residual eigenfunction with parameter `s_j -> 1`, its zero mode in a selected cusp is

\[
A_i^{(j)}y^{1-s_j}.
\]

On every fixed truncation height,

\[
y^{1-s_j}\to1.
\]

Local convergence of the low eigenfunction to its componentwise constant graph mode therefore gives

\[
\boxed{
A_i^{(j)}\to v_j(i)
}
\]

up to the common normalization forced by the equal component area `2 pi`, where `v_j` is the normalized eigenvector of `G_H`.

By the previous section the vector `A^{(j)}` is obtained, up to one scalar phase, from the rank-one scattering residue matrix `R_j`. Hence the marked pole-residue data recover asymptotically the complete eigenpair data

\[
\boxed{
(\mu_j,v_j),\qquad j=1,\ldots,N-1.
}
\]

The constant graph mode is known a priori because all vertex masses are equal.

For fixed normalized graph shape, or more generally whenever the small graph eigenvalues remain spectrally separated at the scale at which the degeneration is taken, this matching is mode-by-mode. For arbitrarily multiscale PF-046 sequences a uniform quantitative version should be stated in terms of clustered spectral projectors / residue subspaces; proving that stability estimate remains an analytic gate.

## 5. Scattering residues recover the ordered gap/cuff vector

Once the graph eigenpairs are known, one may form the endpoint spectral measure

\[
\nu_1=\sum_j |v_j(1)|^2\delta_{\mu_j}.
\]

PF-049 applies the classical finite-Jacobi inverse theorem to show that `nu_1` determines all ordered path weights uniquely:

\[
\boxed{
\nu_1\Longrightarrow(w_1,\ldots,w_{N-1}).
}
\]

The exact tangent geometry then gives

\[
R_k^{\rm geom}=\sinh^2(L_k/4)
=\frac{d_1+\cdots+d_{k-1}}{d_k}.
\]

Fixing the irrelevant Euclidean scale by `d_1=1`, one reconstructs recursively

\[
\boxed{
d_k=\frac{d_1+\cdots+d_{k-1}}{R_k^{\rm geom}}.}
\]

Thus

\[
\boxed{
\{(s_j,R_j)\}_{j=1}^{N-1}
\Longrightarrow
(d_1:\cdots:d_{r-1})
}
\]

asymptotically in the pinching regime, with the cusp labels supplied canonically by the prime tangent.

Equivalently, for large-prime realizations,

\[
\boxed{
\frac{d_i}{d_k}
=\lim
\exp\!\left[-\frac{\ell_i-\ell_k}{2}\right].
}
\]

So the marked scattering residues recover the ordered **relative distinguished-cuff profile**, not merely a symmetric statistic.

## 6. Decisive negative inside the same branch: pole positions / determinant alone are insufficient at graph order

PF-048 gives explicit distinct positive weighted paths with exactly the same unordered graph Laplace spectrum. Therefore the vector of leading pole positions

\[
1-s_j\sim\mu_j/(2\pi^2)
\]

cannot by itself recover the ordered gap path.

Consequently a scalar scattering determinant, or an unmarked list of the small residual poles, loses at leading degeneration order exactly the norming information that PF-048 showed to be missing from the small eigenvalue list.

This does **not** prove exact isoscattering of the corresponding finite hyperbolic tangents: higher-order corrections can separate them. It proves the narrower and relevant statement that the graph-limit inverse problem cannot be solved from pole locations alone. The marked residue matrices are not decorative; they are the first standard scattering datum that restores the missing eigenvector information.

## 7. Relation to the infinite prime-flute

This finding concerns the standard scattering matrix of the finite tangent `Y_H`. It does **not** assert the existence of a well-behaved global infinite-cusp scattering matrix for the prime-flute; PF-019 and the later determinant/trace obstructions make such a claim unjustified.

PF-050 nevertheless gives the correct global bridge on the Laplacian side: tangent spectral measures occur as local spectral limits of the single infinite prime-flute. Thus PF-051 supplies a second, finite-tangent representation of the same inverse data:

\[
\text{local global-Laplacian norming data}
\longleftrightarrow
\text{tangent residual scattering residues}
\longrightarrow
\text{weighted gap path}.
\]

The two descriptions are compatible because both encode the low eigenfunction amplitudes on the canonical pants components.

## 8. Literature and novelty audit

Known ingredients:

- Huxley/Otal: finite-area genus-zero and genus-one hyperbolic surfaces have no small cuspidal eigenpairs, so small eigenvalues are residual.
- Classical Eisenstein/Maaß--Selberg theory: poles in `1/2<s<1` are simple residual poles; residues are `L^2` eigenfunctions, and
  `Res Phi_ab = <Res E_a, Res E_b>`.
- Burger: pinching small eigenfunctions reduce to componentwise constants governed by the weighted dual graph.
- Finite inverse Jacobi theory: an endpoint spectral measure determines the weighted path.
- Schulze studies resolvent degeneration and defines approximate Eisenstein functions/scattering matrices for degenerating finite-geometry hyperbolic surfaces, so scattering under pinching is not a new subject.
- General scattering data are not globally rigid: classical isoscattering constructions include non-isometric finite-area cusped hyperbolic surfaces. Therefore no unrestricted inverse-scattering theorem is claimed.

Directed searches for combinations of `prime gaps`, `scattering residue matrix`, `degenerating hyperbolic surface`, `weighted graph eigenvectors`, and `inverse Jacobi` did not locate the composition above. Searches for scattering residues plus graph degeneration returned the general degeneration literature but not a residue-to-weighted-path reconstruction of this type.

The candidate new content is therefore the **specific forced chain**

\[
\boxed{
\text{relative prime cuffs}
\to
\text{prime tangent pinching}
\to
\text{residual scattering poles + marked residue matrices}
\to
\text{weighted-path eigenpairs}
\to
\text{ordered relative gap vector}.
}
\]

No novelty is claimed for any individual scattering, degeneration, or Jacobi theorem.

## 9. Research consequence

PF-051 identifies a natural scattering object that survives the earlier novelty filters. The scalar scattering determinant is too compressed, just as the unmarked small spectrum is. The **marked residue matrices at the residual poles** retain exactly the norming information needed by the inverse problem.

The next rigorous gate is quantitative: formulate and prove convergence of the residue subspaces/matrices to the weighted-graph spectral projectors uniformly through the strongly multiscale PF-046 degeneration. If that succeeds, the prime-derived scattering statement would no longer require mode-separation qualifications.
