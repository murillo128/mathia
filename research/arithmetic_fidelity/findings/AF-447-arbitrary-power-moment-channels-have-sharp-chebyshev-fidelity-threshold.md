# AF-447 — Arbitrary power-moment channels have a sharp Chebyshev fidelity threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `GENERALIZED-MOMENTS`, `CHEBYSHEV-SYSTEM`, `SHARP-THRESHOLD`, `LOCAL-CONDITIONING`, `NO-NOVELTY-CLAIM`

## Claim

AF-445 and AF-446 use consecutive ordinary moments and Hankel determinants. Their threshold is more structural than that special coordinate choice suggests.

For distinct real exponents

\[
\Lambda=\{\lambda_0<\lambda_1<\cdots<\lambda_{m-1}\}
\]

and a finite positive atomic measure on `(0,\infty)`,

\[
\mu=\sum_{i=1}^{r}a_i\delta_{x_i},
\qquad a_i>0,\quad x_i>0,
\]

define

\[
T_\Lambda(\mu)
=\left(M_\lambda(\mu)\right)_{\lambda\in\Lambda},
\qquad
M_\lambda(\mu)=\int x^\lambda\,d\mu(x)
=\sum_i a_i x_i^\lambda.
\]

Fix `K>=1`.

### Sharp exact-fidelity threshold

If `|\Lambda|=2K+1`, every at-most-`K`-atomic source is separated from every exactly-`K+1`-atomic source with distinct positive support:

\[
\boxed{T_\Lambda(\mu)\ne T_\Lambda(\nu).}
\]

Conversely, if `|\Lambda|=2K`, fix any positive `K`-atomic base source

\[
\mu_0=\sum_{i=1}^{K}a_i^0\delta_{x_i^0}
\]

with distinct supports and any `y>0` different from them. For all sufficiently small `c>0` there is another positive `K`-atomic source `\widetilde\mu_c`, arbitrarily close to `\mu_0`, such that

\[
\boxed{
T_\Lambda(\mu_0)
=
T_\Lambda(\widetilde\mu_c+c\delta_y).
}
\]

Thus, within generalized power-moment channels,

\[
\boxed{
2K\text{ distinct coordinates can fail locally, whereas }2K+1\text{ always separate globally.}
}
\]

No consecutiveness, Hankel structure, or zeroth moment is required for exact separation. The threshold is a Chebyshev-system cardinality threshold.

### Source laws trade one-for-one against transmitted coordinates

Choose any `2K+1` distinct exponents. Suppose `q<=2K` corresponding generalized moments are fixed by an independently justified source law and are therefore known without transmission, with the same prescribed values on every admissible source being compared. Retaining the other

\[
2K+1-q
\]

moments still gives exact separation.

This count is locally sharp. With only `2K-q` retained coordinates, the `q` source constraints plus the retained coordinates impose only `2K` generalized moment equations, and the small-extra-atom construction above can satisfy all of them simultaneously. Source laws therefore do not create free information; they substitute genuine prior coordinates one-for-one for transmitted coordinates.

### The smallest exponent controls the zero-boundary visibility

Now let `|\Lambda|=2K+1` and

\[
0\le\lambda_0<\lambda_1<\cdots<\lambda_{2K}.
\]

At a fixed regular `K`-atomic nuisance source, the nuisance observation image is locally `2K`-dimensional in `\mathbb R^{2K+1}`. Let `n` span its one-dimensional normal space and put

\[
v(y)=\left(y^{\lambda_0},\ldots,y^{\lambda_{2K}}\right),
\qquad
\tau(y)=\frac{|n\cdot v(y)|}{\|n\|}.
\]

Then

\[
\boxed{
\tau(y)=\Theta\!\left(y^{\lambda_0}\right)
\qquad(y\downarrow0).
}
\]

Hence exact identifiability and robustness are controlled by different channel features: the **number** of Chebyshev coordinates controls exact separation, whereas the **smallest exponent** controls first-order visibility of a target approaching `x=0`. If `\lambda_0=0`, the transverse signal stays `\Theta(1)`; if `\lambda_0>0`, it collapses as `y^{\lambda_0}`.

This recovers the structural distinction between AF-445 and AF-446. The positive-moment channel beginning at exponent `1` loses one power of target location near zero. Making the zeroth moment available, either by observing it or through a genuine conservation law, changes that boundary exponent to `0`.

## Global separation from generalized Vandermonde total positivity

Assume two sources with the declared cardinalities have the same `2K+1` generalized moments. Subtract them and combine common support points:

\[
\sigma=\sum_{j=1}^{r}d_j\delta_{z_j},
\qquad r\le 2K+1,
\]

where the `z_j>0` are distinct and the nonzero coefficients `d_j` are real. Equality of the generalized moments gives

\[
\sum_{j=1}^{r}d_j z_j^{\lambda_i}=0
\qquad(i=0,\ldots,2K).
\]

Choose any `r` rows. The square matrix `V=(z_j^{\lambda_i})` is a generalized Vandermonde matrix. With `z_j=e^{t_j}` its entries are `e^{\lambda_i t_j}`; the exponential kernel is strictly totally positive for strictly ordered arguments. Hence `V` is nonsingular and every `d_j=0`, contradiction.

This proves the global statement. Positivity of the original weights is not needed for this linear-independence step; it is used below to keep the local collision inside the positive source class.

## Local collision from the confluent Chebyshev Jacobian

For the `2K`-coordinate case, write the exponents as

\[
\rho_1<\rho_2<\cdots<\rho_{2K}.
\]

Parameterize a labeled `K`-atomic source by

\[
\theta=(a_1,\ldots,a_K,x_1,\ldots,x_K)\in\mathbb R^{2K}.
\]

The generalized moment map has Jacobian columns

\[
\frac{\partial M_{\rho_j}}{\partial a_i}=x_i^{\rho_j},
\qquad
\frac{\partial M_{\rho_j}}{\partial x_i}
=a_i\rho_jx_i^{\rho_j-1}.
\]

This square Jacobian is nonsingular at every source with nonzero weights and distinct positive supports. If a row vector annihilated it, the generalized polynomial

\[
p(x)=\sum_{j=1}^{2K}c_jx^{\rho_j}
\]

would satisfy `p(x_i)=p'(x_i)=0` at all `K` support points. The functions `x^{\rho_j}` form an extended Chebyshev system on `(0,\infty)`: their Wronskian is a nonzero Vandermonde in the exponents times a nonvanishing power of `x`. A nonzero combination cannot therefore have `2K` zeros counted with multiplicity. So the Jacobian is invertible.

The inverse-function theorem now applies. A target atom contributes

\[
c\,v_\rho(y)
=c\,(y^{\rho_1},\ldots,y^{\rho_{2K}}),
\]

which tends to zero with `c` for fixed `y`. For sufficiently small `c`, a unique nearby nuisance parameter vector absorbs the perturbation. Shrinking the neighborhood preserves positive weights, distinct supports, and separation from `y`.

The same argument proves the source-law sharpness statement because any selected `q` fixed moments plus `2K-q` observed moments are again `2K` distinct Chebyshev coordinates.

## The lowest exponent is the infinitesimal conditioning exponent

For the `2K+1`-coordinate map let `J` denote the `(2K+1) x 2K` nuisance Jacobian at the fixed `K`-atomic source and choose nonzero `n` with `n^T J=0`. Define

\[
\phi(x)=n\cdot v(x)=\sum_{j=0}^{2K}n_jx^{\lambda_j}.
\]

Because `n` annihilates both the weight and support-location columns,

\[
\phi(x_i)=\phi'(x_i)=0
\qquad(i=1,\ldots,K).
\]

The coefficient `n_0` cannot vanish. Otherwise `\phi` would be a combination of only the remaining `2K` Chebyshev functions while still having `K` double zeros, forcing `\phi\equiv0` and contradicting `n\ne0`.

Therefore

\[
\phi(y)=n_0y^{\lambda_0}(1+o(1)),
\qquad y\downarrow0,
\]

which gives the claimed `\Theta(y^{\lambda_0})` normal component. This is an infinitesimal transversality statement, not a global finite-noise decoder theorem.

## Prior art and novelty audit

The ingredients are classical.

- Samuel Karlin and William J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience/Wiley (1966), develop Chebyshev systems, generalized moment spaces, and atomic representations.
- James Demmel and Plamen Koev, **“The Accurate and Efficient Solution of a Totally Positive Generalized Vandermonde Linear System,”** *SIAM Journal on Matrix Analysis and Applications* 27(1), 142–152 (2005), DOI `10.1137/S0895479804440335`, treats total positivity of generalized Vandermonde systems.
- Yohann de Castro and Fabrice Gamboa, **“Exact Reconstruction using Beurling Minimal Extrapolation,”** *Journal of Mathematical Analysis and Applications* 395(1), 336–354 (2012), DOI `10.1016/j.jmaa.2012.05.011`, proves exact recovery of finitely supported nonnegative measures from `2s+1` generalized moments under the corresponding Chebyshev-type hypotheses.
- Dmitry Batenkov, Gil Goldman, Yehonatan Salman, and Yosef Yomdin, **“Algebraic Geometry of Error Amplification: the Prony leaves,”** arXiv:`1702.05338` (2017), studies equi-moment Prony leaves and error amplification.

No novelty is claimed for generalized Vandermonde total positivity, Chebyshev zero counts, generalized-moment recovery, confluent Vandermonde nonsingularity, or Prony-leaf geometry.

The Arithmetic Fidelity contribution is the source-law classification required by the current frontier: **Chebyshev-family cardinality controls exact atomic identifiability; independently known source moments replace transmitted coordinates one-for-one; and the smallest exponent controls first-order visibility at the zero boundary.** AF-445 and AF-446 are two coordinate choices inside this wider structure rather than isolated Hankel effects.

## Boundaries and falsification checks

- Exponents and support points must be distinct. Repeated exponents add no independent coordinate, while coalescing supports changes effective atomic cardinality.
- The local collision requires sufficiently small target weight so the compensating nuisance source remains in the positive distinct-support chart. It is a worst-case sharpness result, not failure for every target mass.
- The source-law tradeoff is valid only when the fixed generalized moments are independently justified properties common to nuisance and target-present sources. A target-coded “known” value would be source-law smuggling.
- `2K+1-q` counts transmitted coordinates only after `q` genuine source coordinates are supplied externally. Total scalar information remains `2K+1`.
- The boundary law is first-order at a fixed regular nuisance source. Colliding nuisance supports, vanishing weights, global folds, or target mass tending to zero can cause additional conditioning loss.
- For negative smallest exponent the target vector grows rather than disappears as `y\downarrow0`; the boundary-visibility interpretation above is restricted to nonnegative exponents.
- Nothing here distinguishes rational primes or proves that prime-derived data form a low-atomic source class.

## Consequence for the line

The moment frontier no longer needs to privilege consecutive moments or Hankel determinants. For sparse positive atomic source models, the gates are now: whether the retained observables form a sufficiently large Chebyshev family, which coordinates are genuinely supplied by source law rather than channel, and whether the lowest-order observable stays sensitive in the target degeneration.

The next useful question is therefore not merely which additional moment to add, but **which arithmetic source laws force low-dimensional Chebyshev-type observation families whose lowest-order observable remains sensitive to the arithmetic discriminator.**
