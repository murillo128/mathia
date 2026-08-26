# PF-049 — canonical endpoint spectral measure recovers the relative gap path; static two-end DtN does not

**Status:** `POSITIVE-CANDIDATE + DECISIVE-NEGATIVE`.

PF-048 showed that the unordered small eigenvalues of the hierarchical tangent do not determine the ordered vector of pinching lengths: distinct positive weighted paths can be exactly Laplace-isospectral. This note tests the next object that is still forced by the prime-flute geometry rather than added to repair the inverse problem: the spectral measure seen from the **first component of the canonical ordered pants chain**.

The outcome is sharply different from the unordered spectrum. At the effective graph level the endpoint spectral measure determines every edge weight uniquely, hence every relative prime-gap/cuff ratio. Burger's surface-to-graph degeneration also supplies the natural surface version of this marked measure through component averages of the small eigenfunctions. By contrast, the static Dirichlet-to-Neumann map on the two ends of the path collapses all interior weights to one total resistance and cannot recover the gap hierarchy.

The exact graph inverse statement is unconditional. Passing from the finite hyperbolic tangent to the graph endpoint measure is an asymptotic statement; Burger's proof gives the required componentwise-constant decomposition of low eigenfunctions, but a uniform quantitative stability statement for arbitrarily multi-scale hierarchical families remains a separate analytic gate.

## 1. Canonical ordered path from the prime tangent

Use the notation of PF-047/PF-048. For a recurrent isolated prime pattern

\[
H=\{\eta_1<\cdots<\eta_r\},\qquad d_i=\eta_{i+1}-\eta_i,
\]

the cusp-side tangent `Y_H` has the nested separating geodesics

\[
\boxed{
L_k=4\,\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}},
\qquad k=2,\ldots,r-1.
}
\]

In the hierarchical regime all `L_k -> 0`, and cutting along them produces a canonical ordered chain of

\[
N=r-1
\]

three-punctured / limiting pants components

\[
P_1,P_2,\ldots,P_N.
\]

The order is not an external marking: it is inherited from the cyclic order of the prime vertices and from the exact orthogonal-circle construction. The dual graph is the path `P_N` with conductances

\[
w_i=L_{i+1},\qquad i=1,\ldots,N-1.
\]

Every pants component has hyperbolic area exactly `2 pi`, so after the common mass normalization the effective graph operator is the ordinary symmetric weighted path Laplacian

\[
G=
\begin{pmatrix}
w_1&-w_1&&&\\
-w_1&w_1+w_2&-w_2&&\\
&\ddots&\ddots&\ddots&\\
&&-w_{N-2}&w_{N-2}+w_{N-1}&-w_{N-1}\\
&&&-w_{N-1}&w_{N-1}
\end{pmatrix}.
\]

PF-047 records Burger's asymptotic

\[
\lambda_j(Y_H)=\frac{1}{2\pi^2}\mu_j(G)(1+o(1)),
\qquad j=1,\ldots,N-1,
\]

for the small eigenvalues in the pinching regime.

## 2. The endpoint spectral measure uniquely determines every path weight

Let

\[
0=\mu_0<\mu_1<\cdots<\mu_{N-1}
\]

be the eigenvalues of `G`, and let `v_j` be an orthonormal eigenbasis. Because all `w_i>0`, the path matrix is irreducible and its spectrum is simple.

At the first vertex define the spectral measure

\[
\boxed{
\nu_1
=\sum_{j=0}^{N-1}|v_j(1)|^2\,\delta_{\mu_j}.
}
\]

Equivalently its Stieltjes/Weyl transform is

\[
\boxed{
m_1(z)
=\langle e_1,(G-z)^{-1}e_1\rangle
=\int\frac{d\nu_1(x)}{x-z}.
}
\]

Conjugate `G` by the alternating-sign diagonal matrix

\[
D=\operatorname{diag}(1,-1,1,-1,\ldots).
\]

Then

\[
J=DGD
\]

is a finite Jacobi matrix with positive off-diagonal coefficients

\[
a_i=w_i>0
\]

and diagonal coefficients

\[
b_1=w_1,\qquad
b_i=w_{i-1}+w_i\ (2\le i\le N-1),\qquad
b_N=w_{N-1}.
\]

Since `De_1=e_1`, `J` has exactly the same endpoint spectral measure `nu_1`.

A classical finite-Jacobi inverse theorem now applies: the spectral measure at a cyclic endpoint determines the Jacobi matrix uniquely. One can reconstruct it by applying Gram--Schmidt to `1,x,x^2,...` in `L^2(nu_1)`, or equivalently from the Stieltjes continued fraction of `m_1(z)`. Thus

\[
\boxed{
\nu_1\quad\Longrightarrow\quad
(a_1,\ldots,a_{N-1};b_1,\ldots,b_N)
\quad\Longrightarrow\quad
(w_1,\ldots,w_{N-1})
}
\]

uniquely and in the correct order.

This immediately separates the exact isospectral pair of PF-048: if `(1,4,6,4)` and `(2,3,2,8)` had the same endpoint spectral weights as well as the same eigenvalues, Jacobi uniqueness would force the matrices, hence their edge vectors, to coincide. Their unordered eigenvalues agree, but their endpoint norming constants cannot.

## 3. Exact reconstruction of relative prime gaps from the recovered weights

Once the ordered pinching lengths are known, set

\[
R_k=\sinh^2(L_k/4),\qquad k=2,\ldots,r-1.
\]

The exact prime tangent geometry says

\[
R_k=\frac{d_1+\cdots+d_{k-1}}{d_k}.
\]

Fix the irrelevant common Euclidean scale by setting `d_1=1`. Then recursively

\[
\boxed{
d_k=\frac{d_1+\cdots+d_{k-1}}{R_k},
\qquad k=2,\ldots,r-1.
}
\]

Therefore the endpoint spectral measure of the effective path determines the complete relative gap vector

\[
\boxed{(d_1:\cdots:d_{r-1})}
\]

rather than only symmetric combinations such as the PF-048 pseudodeterminant.

For occurrences near prime scale `P`, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so the same reconstruction determines all relative cuff contrasts:

\[
\boxed{
\frac{d_i}{d_j}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_i(P)-\ell_j(P)}2\right].
}
\]

Thus the full ordered relative-cuff profile is recoverable from **marked spectral data**, even though PF-048 proves that the unordered eigenvalue list alone is not enough.

## 4. Canonical surface endpoint measure

The graph marking has a direct hyperbolic origin. Let

\[
\phi_0,\phi_1,\ldots,\phi_{N-1}
\]

be `L^2`-normalized eigenfunctions spanning the constant mode and the `N-1` small eigenmodes of a pinching tangent, with eigenvalues

\[
0=\lambda_0<\lambda_1\le\cdots\le\lambda_{N-1}.
\]

Define the first-pants average

\[
\boxed{
\beta_j
=\frac{1}{\sqrt{2\pi}}
\int_{P_1}\phi_j\,dA.
}
\]

The factor `sqrt(2 pi)` is forced by the exact area of a hyperbolic pair of pants. The sign of an eigenfunction is irrelevant; use `|beta_j|^2`.

The corresponding rescaled small endpoint spectral measure is

\[
\boxed{
\nu_{Y,1}^{\rm small}
=
\sum_{j=0}^{N-1}
|\beta_j|^2\,
\delta_{\,2\pi^2\lambda_j}.
}
\]

Burger's degeneration proof does more than compare eigenvalues: it writes a low eigenfunction as

\[
f=h+g,
\]

where `h` is constant on each component cut apart by the short separating geodesics and `g` has mean zero there, and shows that the small spectral problem converges to the weighted graph quadratic form. Consequently, for pinching families with a nondegenerate normalized graph shape, the component averages converge to the graph eigenvectors and

\[
\boxed{
\nu_{Y,1}^{\rm small}\ \Longrightarrow\ \nu_1.
}
\]

Hence in that regime the **surface** small eigenvalues plus the canonically marked first-pants norming constants asymptotically recover the complete ordered vector of gap/cuff ratios.

For the very strongly multi-scale patterns available from PF-046, the graph itself can approach further singular limits. The qualitative componentwise-constant reduction remains correct, but a quantitative uniform inverse theorem would require stability estimates for the Jacobi reconstruction as graph spectral gaps coalesce. This is the main remaining analytic gate before claiming a uniform reconstruction theorem over every hierarchical family.

## 5. Decisive negative: static two-end DtN collapses to total resistance

A tempting alternative is to mark only the two ends of the pants chain and use the zero-energy Dirichlet-to-Neumann map of the effective graph. That does **not** retain the gap hierarchy.

For boundary values `u_1,u_N`, harmonicity at every interior vertex forces the same current `I` through every edge. The total voltage drop is

\[
u_1-u_N=I\sum_{i=1}^{N-1}\frac1{w_i}.
\]

Therefore the effective conductance is

\[
C_{\rm eff}
=\left(\sum_{i=1}^{N-1}w_i^{-1}\right)^{-1}
\]

and the complete two-end DtN matrix is only

\[
\boxed{
\Lambda_{\rm DtN}(0)
=C_{\rm eff}
\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
}
\]

All interior weights have collapsed to one harmonic sum.

This is exactly the degree-two invisibility familiar in inverse problems on weighted trees: fixed-energy DtN data on all leaves determine a tree only **up to removal of degree-two vertices**. A path has only two leaves, so its entire internal subdivision is invisible to this static boundary datum.

Thus the branch

\[
\boxed{
\text{prime tangent}
\to
\text{two-end static DtN}
\to
\text{full gap recovery}
}
\]

is decisively closed.

The successful object is instead the **frequency/spectral measure at one canonical endpoint**, which sees the internal masses and resonances of the path and is precisely the classical data that reconstruct a Jacobi matrix.

## 6. Literature / novelty audit

Known ingredients:

- Marc Burger, *Small eigenvalues of Riemann surfaces and graphs* (Math. Z. 205, 1990), and his 1988 announcement, give the surface-to-weighted-graph small-spectrum asymptotic. The proof explicitly decomposes low eigenfunctions into componentwise constants plus mean-zero remainders. Burger notes that the method extends to geometrically finite surfaces.
- The fact that a finite Jacobi matrix with positive off-diagonal entries is uniquely determined by its endpoint spectral measure / Weyl `m`-function is classical inverse Jacobi theory; de Boor--Golub (1978) give a reconstruction from spectral data via orthogonal polynomials.
- Gernandt--Rohleder, *A Calderon type inverse problem for tree graphs* (Linear Algebra Appl. 646, 2022), recover weighted trees from fixed-energy DtN data on all leaves only up to degree-two vertices and give explicit counterexamples for insufficient boundary data. This matches the static-path collapse above.
- Jin--Wang, *The Steklov Determinant and Compactness of Isospectral Planar Domains* (arXiv:2608.22330, 23 Aug 2026), is nearby recent prior art: it studies degenerating hyperbolic surfaces and compares small Dirichlet/Neumann eigenvalues with weighted graph Laplacians in a Steklov-determinant problem. It does not appear to address the prime-derived tangent construction or endpoint Jacobi spectral measures as inverse data for the pinching weights.

Directed searches for combinations of degenerating hyperbolic surfaces, weighted path inverse spectral measures, endpoint norming constants, and prime/cyclotomic tangents did not locate the composition used here.

No novelty is claimed for the inverse Jacobi theorem or Burger degeneration separately. The candidate new content is the exact chain forced by the prime-flute geometry:

\[
\boxed{
\text{relative prime cuffs}
\to
\text{nested exact orthogonal-circle necks}
\to
\text{ordered weighted path}
\to
\text{canonical first-pants spectral measure}
\to
\text{full relative gap vector}.
}
\]

Unlike a generating function of the gaps, every intermediate object is a standard geometric/spectral object attached to the finite tangent.

## 7. Relation to the infinite prime-flute

PF-034 shows that the tangent small eigenvalues produce genuine Weyl sequences for the infinite prime-flute. The **norming constants** in this finding are marked tangent data, not unmarked global invariants of the infinite surface, so one should not claim that the global spectrum alone reconstructs the gaps.

A natural global formulation is local spectral convergence: take the canonically normalized function supported/approximately constant on the first pants of successive isolated occurrences of the same tangent pattern and consider its local spectral measure for the global Laplacian. Pointed geometric convergence should make the low-energy part converge to the tangent measure above. Establishing this with an explicit cutoff error would turn the candidate into a direct local spectral statement for `X_prime`.

## 8. Research consequence

PF-048's inverse ambiguity is therefore not a dead end. It identifies exactly the missing data:

\[
\text{eigenvalues alone} \quad\text{lose ordering information,}
\]

while

\[
\boxed{
\text{eigenvalues + one canonically forced endpoint spectral weight per mode}
}
\]

recover the entire effective path and hence all relative prime-gap/cuff ratios.

The next rigorous gate is not another global determinant. It is a quantitative **surface-to-Jacobi spectral-measure convergence theorem** for the canonical first-pants probe, preferably uniform enough to handle the multi-scale PF-046 families, followed by the corresponding local-spectral-measure statement inside the infinite prime-flute.
