# AF-447 — Arbitrary power-moment channels have a sharp Chebyshev fidelity threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `GENERALIZED-MOMENTS`, `CHEBYSHEV-SYSTEM`, `SHARP-THRESHOLD`, `LOCAL-CONDITIONING`, `NO-NOVELTY-CLAIM`

## Claim

AF-445 and AF-446 use consecutive ordinary moments and Hankel determinants. The threshold is more structural than that special coordinate choice suggests.

Let

\[
\Lambda=\{\lambda_0<\lambda_1<\cdots<\lambda_{m-1}\}\subset\mathbb R
\]

be distinct real exponents and, for a finite positive atomic measure on `(0,\infty)`,

\[
\mu=\sum_{i=1}^{r}a_i\delta_{x_i},
\qquad a_i>0,\quad x_i>0,
\]

define the generalized power-moment channel

\[
T_\Lambda(\mu)
=\left(M_{\lambda}(\mu)\right)_{\lambda\in\Lambda},
\qquad
M_\lambda(\mu)=\int x^\lambda\,d\mu(x)
=\sum_i a_i x_i^\lambda.
\]

Fix `K>=1`.

### 1. Any `2K+1` distinct power moments separate `K` atoms from `K+1`

If `|\Lambda|=2K+1`, `\mu` has at most `K` distinct support points, and `\nu` has exactly `K+1` distinct support points, then

\[
\boxed{T_\Lambda(\mu)\ne T_\Lambda(\nu).}
\]

No consecutiveness, Hankel structure, or presence of the zeroth moment is required for exact separation.

### 2. Any `2K` distinct power moments can still fail locally

If `|\Lambda|=2K`, fix any positive `K`-atomic base source

\[
\mu_0=\sum_{i=1}^{K}a_i^0\delta_{x_i^0}
\]

with distinct supports, and fix any `y>0` different from those supports. Then for all sufficiently small `c>0` there is another positive `K`-atomic source `\widetilde\mu_c`, arbitrarily close to `\mu_0`, such that

\[
\boxed{
T_\Lambda(\mu_0)
=
T_\Lambda(\widetilde\mu_c+c\delta_y).
}
\]

Hence the worst-case exact-fidelity threshold inside the class of generalized power moments is sharp:

\[
\boxed{
2K\text{ distinct power moments can fail, while }2K+1\text{ always separate.}
}
\]

The `2K+1` threshold is therefore not a peculiarity of the consecutive Prony/Hankel channel in AF-445. It is a Chebyshev-system cardinality threshold.

### 3. Known source moments trade one-for-one against transmitted moments

Choose any `2K+1` distinct exponents. Suppose `q<=2K` of the corresponding generalized moments are fixed by an independently justified source law and therefore known without transmission, with the same prescribed values for every admissible source being compared. Then retaining the other

\[
2K+1-q
\]

moments still gives exact separation between at-most-`K` and exactly-`K+1` atomic sources.

This count is sharp in the same local worst-case sense: if only `2K-q` additional moments are retained, the `q` source constraints plus the retained coordinates form only `2K` generalized moment equations, and a small extra target atom can again be absorbed by moving the `2K` nuisance parameters.

Thus source laws do not create free information. They can replace transmitted coordinates one-for-one when they supply genuine moment information independently of the target.

### 4. Exact identifiability and boundary robustness are controlled by different parts of the channel

Now let `|\Lambda|=2K+1` with

\[
0\le\lambda_0<\lambda_1<\cdots<\lambda_{2K}.
\]

At a fixed regular `K`-atomic nuisance source `\mu_0`, the nuisance observation image is locally a `2K`-dimensional manifold in `\mathbb R^{2K+1}`. Let `n` span its one-dimensional normal space and write

\[
v(y)=\left(y^{\lambda_0},\ldots,y^{\lambda_{2K}}\right).
\]

The first-order transverse visibility of inserting a target atom at `y` is

\[
\tau(y)
:=
\frac{|n\cdot v(y)|}{\|n\|}.
\]

Then

\[
\boxed{
\tau(y)=\Theta\!\left(y^{\lambda_0}\right)
\qquad(y\downarrow0).
}
\]

Consequently the **number** of generalized moments controls exact identifiability, while the **smallest retained exponent** controls how rapidly a target approaching the blind boundary `x=0` loses first-order separation. In particular:

- if `\lambda_0=0`, the transverse target signal stays `\Theta(1)` as `y\downarrow0`;
- if `\lambda_0>0`, it collapses as `y^{\lambda_0}`.

This recovers the structural distinction behind AF-445 and AF-446 without relying on their special Hankel minors. The shifted positive-moment channel begins at exponent `1` and loses one power of the target location; making the zeroth moment available, whether as an observation or an intrinsic conservation law, changes the boundary exponent to `0`.

## Why the generalized Vandermonde gives global separation

Assume two sources with the declared cardinalities have the same `2K+1` generalized moments. Subtract them and combine common support points. Their difference is a signed atomic measure

\[
\sigma=\sum_{j=1}^{r}d_j\delta_{z_j},
\qquad r\le 2K+1,
\]

with distinct positive `z_j` and nonzero real `d_j`, satisfying

\[
\sum_{j=1}^{r}d_j z_j^{\lambda_i}=0
\qquad(i=0,\ldots,2K).
\]

Use any `r` rows. The resulting square matrix

\[
V=(z_j^{\lambda_i})
\]

is a generalized Vandermonde matrix. After the change `z_j=e^{t_j}`, its entries are `e^{\lambda_i t_j}`. The exponential kernel is strictly totally positive for strictly ordered arguments, so `V` is nonsingular. Hence every `d_j=0`, contradicting the assumption that the two sources differ.

This proves global separation. Positivity of the original weights is not actually needed for this linear-independence step; positivity is used below to keep the local collision inside the admissible source class.

## Why `2K` equations still admit a hidden target atom

Parameterize a labeled `K`-atomic source by

\[
\theta=(a_1,\ldots,a_K,x_1,\ldots,x_K)
\in\mathbb R^{2K}
\]

inside the open set of positive weights and distinct positive supports. For `|\Lambda|=2K`, the Jacobian of the generalized moment map has columns

\[
\frac{\partial M_{\lambda_j}}{\partial a_i}=x_i^{\lambda_j},
\qquad
\frac{\partial M_{\lambda_j}}{\partial x_i}
=a_i\lambda_jx_i^{\lambda_j-1}.
\]

It is nonsingular. Indeed, a row vector annihilating all columns would produce a generalized polynomial

\[
p(x)=\sum_{j=1}^{2K}c_jx^{\lambda_j}
\]

with

\[
p(x_i)=p'(x_i)=0
\qquad(i=1,\ldots,K).
\]

The functions `x^{\lambda_j}` form an extended Chebyshev system on `(0,\infty)`: their Wronskian is a nonzero generalized Vandermonde in the exponents times a nonvanishing power of `x`. A nonzero combination therefore cannot have `2K` zeros counted with multiplicity. Thus `p\equiv0` and the Jacobian is invertible.

The inverse-function theorem now applies exactly as in AF-445/AF-446. A target atom contributes

\[
c\,v_\Lambda(y)
=c\,(y^{\lambda_1},\ldots,y^{\lambda_{2K}}),
\]

which tends to zero with `c` for fixed `y`. For small enough `c`, a unique nearby nuisance parameter vector can absorb that perturbation. Shrinking the neighborhood preserves positive weights, distinct supports, and separation from `y`.

The same argument proves the source-law tradeoff: fixing `q` of the moment coordinates and observing only `2K-q` others still imposes only `2K` equations on the `2K` nuisance parameters, and the generalized confluent Vandermonde remains invertible for any choice of distinct exponents.

## The lowest exponent is the local boundary-conditioning exponent

For `2K+1` moment coordinates, let `J` be the ` (2K+1) x 2K` nuisance Jacobian at `\mu_0`, and choose nonzero `n` with

\[
n^T J=0.
\]

Define

\[
\phi(x)=n\cdot v(x)=\sum_{j=0}^{2K}n_jx^{\lambda_j}.
\]

Because `n` annihilates both the weight and support-location columns of `J`,

\[
\phi(x_i^0)=\phi'(x_i^0)=0
\qquad(i=1,\ldots,K).
\]

The coefficient `n_0` of the smallest exponent cannot vanish. If it did, `\phi` would be a combination of only the remaining `2K` Chebyshev functions while still having `K` double zeros, which is impossible unless `\phi\equiv0`; that would contradict `n\ne0`.

Therefore, as `y\downarrow0`,

\[
\phi(y)
=n_0y^{\lambda_0}
\left(1+o(1)\right),
\]

and hence

\[
\tau(y)
=\frac{|\phi(y)|}{\|n\|}
=\Theta(y^{\lambda_0}).
\]

This is an infinitesimal transversality statement, not a uniform finite-noise decoder theorem. Colliding nuisance supports, vanishing nuisance weights, target weight tending to zero, or global folds of the observation manifold can introduce additional conditioning losses.

## Prior art and novelty audit

The mathematical ingredients are classical.

- Samuel Karlin and William J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience/Wiley (1966), develop Chebyshev systems, generalized moment spaces, and their atomic representations. The zero-count and generalized-moment uniqueness mechanisms used here belong to that theory.
- James Demmel and Plamen Koev, **“The Accurate and Efficient Solution of a Totally Positive Generalized Vandermonde Linear System,”** *SIAM Journal on Matrix Analysis and Applications* 27(1), 142–152 (2005), DOI `10.1137/S0895479804440335`, treats total positivity of generalized Vandermonde systems and their numerical structure.
- Yohann de Castro and Fabrice Gamboa, **“Exact Reconstruction using Beurling Minimal Extrapolation,”** *Journal of Mathematical Analysis and Applications* 395(1), 336–354 (2012), DOI `10.1016/j.jmaa.2012.05.011`, proves exact recovery of finitely supported nonnegative measures from `2s+1` generalized moments under the relevant Chebyshev-type framework. This is close prior art for the `2K+1` recovery side and prevents a novelty claim for the threshold itself.
- Dmitry Batenkov, Gil Goldman, Yehonatan Salman, and Yosef Yomdin, **“Algebraic Geometry of Error Amplification: the Prony leaves,”** arXiv:`1702.05338` (2017), studies equi-moment/Prony leaves and the geometry of error amplification, directly neighboring the local collision and conditioning viewpoint.

No novelty is claimed for generalized Vandermonde total positivity, Chebyshev-system zero counts, generalized-moment recovery, confluent Vandermonde nonsingularity, or Prony-leaf geometry.

The Arithmetic Fidelity contribution here is the exact synthesis needed by the current source-law frontier: it separates three resources that consecutive Hankel coordinates had conflated. **Cardinality of an ECT observation family controls exact atomic identifiability; independently known source moments substitute one-for-one for transmitted coordinates; and the smallest exponent controls first-order visibility of a target approaching the zero boundary.** AF-445 and AF-446 become two coordinate choices inside this wider classification rather than isolated moment tricks.

## Boundaries and falsification checks

- The exact global statement assumes distinct exponents and distinct positive support points. Repeated exponents add no independent information, while coalescing support points changes effective atomic cardinality.
- The local collision theorem requires sufficiently small target weight so the compensating nuisance source remains in the positive, distinct-support parameter chart. It is a worst-case sharpness result, not failure for every target mass.
- The source-law tradeoff is legitimate only when the fixed generalized moments are independently justified properties of the admissible source class and are common to the compared nuisance and target-present sources. Declaring a target-coded value to be “known” would be source-law smuggling.
- The `2K+1-q` transmitted count measures coordinates only after `q` genuine moment values have been supplied externally. Total scalar information remains `2K+1`; the theorem does not beat the Chebyshev threshold for free.
- The boundary law `Theta(y^{lambda_0})` is first-order at a fixed regular nuisance source. It does not by itself provide a global minimax noise radius.
- For negative smallest exponent, the target moment vector grows as `y\downarrow0` rather than disappearing; the stated boundary-conditioning interpretation is restricted to nonnegative exponents.
- Nothing here distinguishes rational primes or proves that prime-derived data belong to a low-atomic source class. The result is a reusable compression/source-law theorem to be applied only after an arithmetic representation supplies the corresponding hypotheses.

## Consequence for the line

The moment frontier can now be phrased without privileging consecutive moments or Hankel determinants. For sparse positive atomic source models, the first gate is whether the retained observables form a sufficiently large Chebyshev family; the second is which coordinates are genuinely supplied by the source law rather than the channel; the third is whether the lowest-order observable remains sensitive in the degeneration relevant to the target.

A useful next question is therefore no longer “which additional moment should be added?” but: **which arithmetic source laws force low-dimensional Chebyshev-type observation families with a smallest-order observable that remains uniformly sensitive to the arithmetic discriminator?**