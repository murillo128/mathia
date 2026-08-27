# PF-062 — the near-one renormalized Selberg zeta collapses to the already-known small-spectrum polynomial

**Status:** `DECISIVE-NEGATIVE` for a new prime-specific zeta channel near `s=1`; `EXACT-COROLLARY` of classical pinching-zeta factorization plus Burger's graph limit.

## 1. Question

PF-035/PF-036 show that the infinite prime-flute has no ordinary Selberg/Ruelle Euler-product starting half-plane, so any useful Selberg zeta must live on a finite prime-derived tangent rather than on the whole flute.

PF-047/PF-054, on the other hand, show that a prime-derived tangent with `N-1` short separating necks has a weighted-path small spectrum. A natural remaining possibility was therefore:

> Does the Selberg zeta of the finite tangent, after the standard pinching factors are removed, contain some additional prime-gap-sensitive analytic structure beyond the small eigenvalues already detected by Burger's graph limit?

The answer near `s=1` is **no**. The classical degeneration theory already isolates exactly the small-eigenvalue polynomial, and a double scaling at `s=1` produces nothing beyond the characteristic polynomial of the Burger graph.

## 2. Fixed-shape prime-tangent degeneration

Let `Y_epsilon` be a fixed-topology finite-area hyperbolic tangent whose `N-1` separating geodesics have lengths

\[
L_i(\varepsilon)=\varepsilon a_i+o(\varepsilon),
\qquad a_i>0,
\qquad i=1,\ldots,N-1.
\]

In the prime-flute construction these necks are not arbitrary. For a tangent pattern

\[
H=\{\eta_1<\cdots<\eta_r\},
\qquad d_i=\eta_{i+1}-\eta_i,
\]

PF-047 gives the exact nested-separator formula

\[
\sinh^2\frac{L_k}{4}
=
\frac{d_1+\cdots+d_{k-1}}{d_k}.
\]

The original distinguished cuffs at prime scale `P` satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

hence

\[
\frac{d_i}{d_j}
=
\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_i(P)-\ell_j(P)}2\right].
\]

Thus the fixed shape `(a_i)` is ultimately a function of relative cuff/gap data.

Let `G_a` be the weighted dual-path Laplacian with edge weights `a_i`, and write

\[
0=\mu_0<\mu_1\le\cdots\le\mu_{N-1}
\]

for its eigenvalues.

Burger's degeneration theorem gives, with the normalization used in PF-047,

\[
\boxed{
\lambda_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}\mu_j+o(\varepsilon),
\qquad j=0,\ldots,N-1,
}
\]

where `lambda_0,epsilon=0` and the other `N-1` eigenvalues are the small eigenvalues created by the separating pinches.

## 3. The classical zeta factorization already removes exactly those modes

Let

\[
Z_\varepsilon(s)=Z(Y_\varepsilon,s)
\]

be the Selberg zeta function and let

\[
Z_{{\rm pin},\varepsilon}(s)
\]

be the product of the standard local Selberg factors belonging to the `N-1` pinching geodesics.

Schulze's theorem (extending Wolpert/Hejhal) gives

\[
\frac{Z_\varepsilon(s)}{Z_{{\rm pin},\varepsilon}(s)}
\longrightarrow
Z_0(s)
\]

locally uniformly for `Re s > 1/2`, where `Z_0` is the product of the Selberg zeta functions of the components of the nodal limit.

More importantly for the present question, the local analysis around `s=1` used by Wolpert and recorded explicitly by Freixas i Montplet factors the degenerating zeta as

\[
\boxed{
Q_\varepsilon(s)
:=
\frac{Z_\varepsilon(s)}
{Z_{{\rm pin},\varepsilon}(s)
 \prod_{j=0}^{N-1}(s^2-s+\lambda_{j,\varepsilon})}
}
\]

and proves that `Q_epsilon` extends holomorphically to a fixed disk around `s=1` and is locally uniformly bounded there. Subsequential limits are the corresponding product of component zetas with their simple `s=1` zeros divided out.

For our stable limit, every component is a thrice-punctured sphere. Writing

\[
C_*:=Z'_{S_{0,3}}(1),
\]

we therefore have

\[
\boxed{
Q_\varepsilon(s)\longrightarrow Q_0(s),
\qquad
Q_0(1)=C_*^N\ne0,
}
\]

along the degeneration (or along any subsequence needed in the standard Montel formulation; the value of the limit at `1` is unique).

This is the crucial point: **the known theorem already identifies the only singularly moving near-one factor as the polynomial in the small Laplace eigenvalues.**

## 4. Double scaling gives the graph characteristic polynomial

Set

\[
s_\varepsilon(z)
=
1-\frac{\varepsilon z}{2\pi^2}.
\]

Then

\[
s_\varepsilon(z)^2-s_\varepsilon(z)
=
-\frac{\varepsilon z}{2\pi^2}+O(\varepsilon^2),
\]

and Burger's asymptotics give

\[
\boxed{
s_\varepsilon(z)^2-s_\varepsilon(z)+\lambda_{j,\varepsilon}
=
\frac{\varepsilon}{2\pi^2}(\mu_j-z)+o(\varepsilon).
}
\]

Multiplying over all `N` small modes, including `mu_0=0`, yields locally uniformly in `z`

\[
\prod_{j=0}^{N-1}
\bigl(s_\varepsilon(z)^2-s_\varepsilon(z)+\lambda_{j,\varepsilon}\bigr)
=
\left(\frac{\varepsilon}{2\pi^2}\right)^N
\det(G_a-zI)
\,(1+o(1)).
\]

Therefore the standard pinching-renormalized Selberg zeta has the scaling limit

\[
\boxed{
\left(\frac{2\pi^2}{\varepsilon}\right)^N
\frac{1}{C_*^N}
\frac{
Z_\varepsilon\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
}{
Z_{{\rm pin},\varepsilon}\!\left(1-\frac{\varepsilon z}{2\pi^2}\right)
}
\longrightarrow
\det(G_a-zI).
}
\]

The sign convention is fixed by

\[
\det(G_a-zI)=\prod_j(\mu_j-z).
\]

This is a useful exact corollary, but **not a new independent zeta invariant**. The right-hand side is precisely the characteristic polynomial of the weighted graph whose eigenvalues PF-047 already obtained from the Laplacian.

## 5. Why this closes the near-one zeta branch as a source of new information

At `z=0`, after removing the permanent zero mode, derivatives recover the product of nonzero small eigenvalues. That is the determinant/pseudodeterminant information already visible in PF-048 and in classical determinant-degeneration formulas.

Allowing `z` to vary recovers all elementary symmetric functions of the small eigenvalues at once, but still nothing beyond them:

\[
\boxed{
\text{near-one renormalized tangent Selberg zeta}
\quad\Longleftrightarrow\quad
\text{Burger small-spectrum characteristic polynomial}.
}
\]

Consequently the chain

\[
\text{relative prime cuffs/gaps}
\to
\text{finite tangent}
\to
\text{renormalized Selberg zeta near }1
\to
\text{new prime-specific analytic data}
\]

fails at the last arrow. The zeta germ packages the same small spectral data already supplied by the Laplacian/weighted path.

This does **not** invalidate the prime-specific spectral relation itself. In particular, in the hierarchical regime PF-054 still gives

\[
\lambda_{N-j}
\sim
\frac{2(j+1)}{\pi^2j}
\exp\!\left[-\frac{\ell_j-\ell_{j+1}}4\right].
\]

It only says that passing from those small eigenvalues to the tangent Selberg zeta near `s=1` does not create an additional layer of arithmetic structure.

## 6. Novelty audit

The relevant prior art is unusually close:

1. **Schulze**, *On the resolvent of the Laplacian on functions for degenerating surfaces of finite geometry* (JFA 2006), proves convergence of `Z/Z_pin` to the zeta of the limit for `Re s>1/2`.
2. **Wolpert's degeneration results**, as quoted and used by **Freixas i Montplet**, give a uniform local bound after dividing additionally by
   \[
   \prod_j(s^2-s+\lambda_j),
   \]
   and identify the holomorphic limit near `s=1`.
3. **Burger**, *Small eigenvalues of Riemann surfaces and graphs* (Math. Z. 1990), identifies the collapsing small eigenvalues with the weighted dual-graph spectrum, with the `1/(2 pi^2)` normalization used here.
4. Freixas i Montplet already evaluates the above factorization at `s=1` to obtain product-of-small-eigenvalue asymptotics. The displayed double-scaling polynomial is essentially the same classical factorization without setting the spectral variable to `s=1` first.

Directed searches did not locate the exact displayed double-scaling formula written as a graph characteristic polynomial. Nevertheless, because the Wolpert/Freixas factorization already removes precisely the factors `s^2-s+lambda_j`, this should **not** be advertised as a new Selberg-zeta mechanism. It is best regarded as a transparent corollary that closes the branch.

Recent work of Li–Matheus–Pan–Tao does obtain genuinely new graph-zeta scaling limits from degenerating Schottky groups, where Selberg zeta tends to an Ihara zeta of a non-Archimedean limiting graph. That mechanism is topologically different: our genus-zero tangent dual graphs are trees (PF-057), so their Ihara zeta is trivial. The only nontrivial graph object surviving here is the weighted Laplacian characteristic polynomial above.

## 7. Research consequence

For the prime-flute program, do not spend further effort trying to obtain extra information from the **standard pinching-renormalized Selberg zeta germ near `s=1`** of finite tangents. It is spectrally equivalent, at the singular scale, to the already-known small-eigenvalue polynomial.

The still-live objects are those that retain information not determined by the unmarked small eigenvalues: marked spectral measures, scattering residue matrices, or genuinely new two-scale/localization constructions. The global infinite-flute Selberg zeta remains obstructed independently by PF-035/PF-036.
