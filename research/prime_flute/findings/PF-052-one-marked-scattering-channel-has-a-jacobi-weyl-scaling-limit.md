# PF-052 — one marked scattering channel has a Jacobi Weyl scaling limit

**Status:** `POSITIVE-CANDIDATE / EXACT-ALGEBRA-GIVEN-PF-051 + ONE-ANALYTIC-SCALING-GATE`.

PF-051 showed that the full marked residue matrices at the residual poles recover the weighted path, hence the ordered relative prime-gap/cuff profile, in the hierarchical tangent degeneration. This note compresses that statement much further: in a fixed-shape pinching regime, the **polar part of a single canonically marked diagonal scattering coefficient**, after the forced blow-up at `s=1`, converges to the endpoint Weyl--Titchmarsh `m`-function of the weighted Jacobi/path operator.

Thus the prime-gap path is not merely encoded in a collection of scattering residues. It appears as the coefficients of a standard one-variable Herglotz/Stieltjes function arising from one cusp channel.

The conclusion is asymptotic and concerns the finite prime tangent, not a global infinite-cusp scattering matrix for the entire flute.

## 1. Fixed-shape hierarchical tangent degeneration

Let `Y_epsilon` be a genus-zero finite-area prime-tangent family whose `N-1` separating geodesics pinch with a common first-order scale

\[
L_i(\varepsilon)=\varepsilon a_i+o(\varepsilon),
\qquad a_i>0,
\qquad i=1,\ldots,N-1.
\]

The limiting stable surface is a chain of `N` thrice-punctured spheres. The dual weighted path has ordinary Laplacian

\[
G_a=
\begin{pmatrix}
a_1&-a_1&&\\
-a_1&a_1+a_2&-a_2&\\
&\ddots&\ddots&\ddots\\
&&-a_{N-1}&a_{N-1}
\end{pmatrix}
\]

with simple eigenpairs

\[
G_a v_j=\mu_j v_j,
\qquad
0=\mu_0<\mu_1<\cdots<\mu_{N-1},
\qquad
\|v_j\|_{\ell^2}=1.
\]

Burger's theorem for degenerating finite-geometry hyperbolic surfaces gives, with each pants component having area `2 pi`,

\[
\boxed{
\lambda_{j,\varepsilon}
=\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon),
\qquad j=1,\ldots,N-1.
}
\]

For genus zero these small positive eigenvalues are residual. Write

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
=\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon).
}
\]

Include the constant mode as `j=0`, with `s_{0,epsilon}=1` and `mu_0=0`.

## 2. One canonical cusp channel

Choose the original prime cusp lying in the first endpoint pair of pants. This cusp is canonically marked by the order inherited from the exact orthogonal-circle construction; no auxiliary test function or artificial graph endpoint is selected.

Normalize the primitive parabolic at this cusp to translation width one and denote the corresponding diagonal scattering entry by

\[
\phi_\varepsilon(s)
:=\Phi_{aa,\varepsilon}(s).
\]

Let

\[
r_{j,\varepsilon}
:=\operatorname*{Res}_{s=s_{j,\varepsilon}}\phi_\varepsilon(s).
\]

Maaß--Selberg gives exactly

\[
r_{j,\varepsilon}
=\left\|
\operatorname*{Res}_{s=s_{j,\varepsilon}}E_a(\cdot,s)
\right\|_{L^2(Y_\varepsilon)}^2
\ge0.
\]

For a simple residual eigenvalue, if `u_{j,epsilon}` is normalized in `L^2`, then `r_{j,epsilon}` is the squared zero-mode amplitude of `u_{j,epsilon}` in this marked cusp.

PF-051 identifies the pinching limit of these amplitudes with the first component of the graph eigenvector. Since a normalized graph vector `v_j` corresponds to a componentwise-constant surface eigenfunction with value `v_j(i)/sqrt(2 pi)` on the `i`-th pants component, the expected/standard fixed-shape residue limit is

\[
\boxed{
2\pi\,r_{j,\varepsilon}
\longrightarrow
|v_j(1)|^2.
}
\]

This normalization is consistent with the universal pole at `s=1`: the tangent has area `2 pi N`, hence

\[
r_{0,\varepsilon}=\frac1{2\pi N},
\]

while the constant graph eigenvector satisfies `|v_0(1)|^2=1/N`.

## 3. The near-one polar blow-up is the Jacobi Weyl function

Let the polar cluster of the chosen scattering entry at the residual poles converging to `1` be

\[
\phi_\varepsilon^{\mathrm{pol}}(s)
:=
\sum_{j=0}^{N-1}
\frac{r_{j,\varepsilon}}{s-s_{j,\varepsilon}}.
\]

This is canonical once one chooses a small neighbourhood of `s=1` containing precisely the residual cluster; it is the principal polar part of the meromorphic scattering coefficient, not an independently invented generating function.

Blow up the spectral coordinate at the rate forced by Burger:

\[
\boxed{
s=1-\frac{\varepsilon z}{2\pi^2}.}
\]

For every `z` off the graph spectrum,

\[
s-s_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}(\mu_j-z)+o(\varepsilon).
\]

Together with the residue limit above this yields term by term

\[
\frac{\varepsilon}{\pi}
\frac{r_{j,\varepsilon}}
{s-s_{j,\varepsilon}}
\longrightarrow
\frac{|v_j(1)|^2}{\mu_j-z}.
\]

Because the cluster is finite, summation gives the central candidate identity

\[
\boxed{
\frac{\varepsilon}{\pi}\,
\phi_\varepsilon^{\mathrm{pol}}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\longrightarrow
m_{G_a}(z),
}
\]

where

\[
\boxed{
m_{G_a}(z)
:=\langle e_1,(G_a-z)^{-1}e_1\rangle
=\sum_{j=0}^{N-1}
\frac{|v_j(1)|^2}{\mu_j-z}
}
\]

is the endpoint Weyl--Titchmarsh / Stieltjes `m`-function of the weighted path.

The constants are forced. In particular, the `j=0` term tends to

\[
-\frac1{Nz},
\]

exactly the constant-mode contribution to `m_{G_a}`.

## 4. Why this is stronger than PF-051

PF-051 used the collection

\[
\{s_j,\operatorname{Res}_{s_j}\Phi(s)\}
\]

of marked matrix residues. PF-052 says that, asymptotically, one scalar cusp channel already packages the required pole positions and endpoint norming constants into one standard analytic object.

For a finite Jacobi matrix, the endpoint `m`-function is cyclic and determines the full ordered tridiagonal matrix via its Stieltjes continued fraction. Since `G_a` is a weighted path Laplacian,

\[
\boxed{
m_{G_a}\Longrightarrow(a_1,\ldots,a_{N-1})}
\]

uniquely.

Therefore the near-one scattering blow-up determines the normalized separating-length profile.

## 5. Return to exact prime gaps and distinguished cuffs

For a prime tangent arising from

\[
H=\{\eta_1<\cdots<\eta_r\},
\qquad
d_i=\eta_{i+1}-\eta_i,
\]

the exact orthogonal-circle geometry gives

\[
\boxed{
L_k
=4\operatorname{arsinh}
\sqrt{\frac{d_1+\cdots+d_{k-1}}{d_k}},
\qquad k=2,\ldots,r-1.
}
\]

Thus recovering the ordered `L_k` recovers the ordered relative gap vector recursively, up to the irrelevant common Euclidean scale.

For large-prime realizations, the distinguished cuffs satisfy

\[
\ell_i(P)
=2\log\frac{4P}{d_i}+o(1),
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

The common divergent cuff scale disappears, while the relative cuff profile survives as the coefficients of the limiting Jacobi `m`-function.

The resulting chain is

\[
\boxed{
\text{relative prime cuffs/gaps}
\to
\text{exact tangent necks}
\to
\text{near-}1\text{ residual scattering cluster}
\to
m_{G_a}(z)
\to
\text{ordered gap path}.
}
\]

## 6. Relation to known scattering/Weyl theory

There is important prior art close to the *form* of this result.

1. Abstract scattering theory expresses scattering matrices in terms of operator-valued Weyl functions (boundary triples, Krein theory). Thus `scattering <-> Weyl function` is not new.
2. Inverse scattering on asymptotically hyperbolic surfaces can be extremely rigid when one uses a **generalized** scattering matrix; Isozaki--Kurylev--Lassas show that such data can determine the metric and singularity structure.
3. In separable asymptotically hyperbolic Liouville surfaces, reflection coefficients are generalized Weyl--Titchmarsh functions for a radial ODE.
4. Schulze studies degenerating hyperbolic surfaces, proves local resolvent convergence, and constructs approximate Eisenstein functions and scattering matrices converging under pinching.
5. Burger identifies the small surface spectrum with a weighted graph spectrum.

These facts substantially lower the novelty level of the slogan "scattering becomes a Weyl function." They do **not**, however, appear to contain the specific singular scaling limit above: a physical cusp scattering coefficient of a pinching finite-area hyperbolic surface, blown up around the coalescing residual poles at `s=1`, yielding the endpoint `m`-function of Burger's weighted dual graph with the explicit `epsilon/pi` and `epsilon/(2 pi^2)` normalizations.

Directed searches for combinations of `degenerating hyperbolic surface`, `scattering`, `weighted graph`, `Weyl m-function`, `Jacobi`, `Eisenstein residue`, and `pinching` found the separate degeneration and abstract Weyl/scattering literatures, but not this graph `m`-function scaling statement.

No historical-priority claim is made.

## 7. Important analytic gate

The algebra of the scaling limit is exact once the two first-order asymptotics

\[
1-s_{j,\varepsilon}
=\frac{\varepsilon\mu_j}{2\pi^2}+o(\varepsilon),
\qquad
2\pi r_{j,\varepsilon}\to|v_j(1)|^2
\]

are available.

The first is Burger plus `lambda=s(1-s)`.

The second is the only substantive analytic gate. PF-051 derives it from Maaß--Selberg and convergence of normalized small eigenfunctions to componentwise constants. A paper-level proof should make explicit that this convergence controls the zero Fourier coefficient at a fixed normalized horocycle in the selected cusp, and should treat clusters by spectral projectors if several small modes approach on parametrically different scales.

For a fixed graph shape with simple separated `mu_j`, this is the cleanest regime and no infinite-dimensional uniformity is required.

One should also distinguish the **polar part** from the full scattering entry. The regular holomorphic part may have its own scaling. PF-052 only claims the canonical principal-pole cluster unless a separate bound shows that

\[
\frac{\varepsilon}{\pi}
\phi_\varepsilon^{\rm reg}
\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
\to0.
\]

Proving or disproving that stronger full-entry limit is the next natural test.

## 8. Research consequence

This candidate identifies a highly compressed but still information-complete standard spectral observable: **one marked cusp scattering channel near `s=1`**.

It avoids the global infinite-flute scattering obstructions because it lives on the finite tangent. It avoids the isospectral ambiguity of PF-048 because residues supply the endpoint norming constants. It avoids an arbitrary local probe because the cusp is canonically marked by the original prime/orthogonal-circle ordering.

If the remaining residue-asymptotic lemma and the regular-part bound can both be proved, the full rescaled physical scattering coefficient would converge directly to the Jacobi `m`-function of the prime-gap path. That would be a natural transfer/scattering law derived from the exact hyperbolic geometry rather than an imposed generating function.
