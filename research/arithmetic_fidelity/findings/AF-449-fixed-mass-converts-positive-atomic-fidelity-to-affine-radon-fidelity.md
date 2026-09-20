# AF-449 — Fixed mass converts positive atomic fidelity to affine Radon fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `POSITIVE-ATOMS`, `SOURCE-LAW`, `ORIENTED-MATROID`, `CHEBYSHEV-SYSTEM`, `NO-NOVELTY-CLAIM`

## Claim

AF-448 shows that exact recovery of sparse positive atomic sources from a linear feature map is controlled by the **sign balance of kernel relations**, not by ordinary rank alone. A conserved total mass has a sharper interpretation than merely reducing one nuisance parameter: it changes the relevant kernel geometry from **conic dependence** to **affine dependence**.

Let `X` be a set, let

\[
\Phi:X\to\mathbb R^m,
\]

and let

\[
\mathcal M_\Phi(\mu)=\int_X\Phi\,d\mu
\]

for finite atomic measures. For `M>0` and `r\ge1`, write

\[
\mathcal P_{r,M}
=
\left\{
\mu=\sum_{i=1}^k a_i\delta_{x_i}:
1\le k\le r,
\ a_i>0,
\ \sum_i a_i=M
\right\}.
\]

Augment the feature map by the conserved mass coordinate,

\[
\widehat\Phi(x)=(1,\Phi(x))\in\mathbb R^{m+1}.
\]

For a nonzero finite signed atomic measure `sigma`, let `n_+(sigma)` and `n_-(sigma)` be the numbers of atoms in the positive and negative parts of its Jordan decomposition. Define the **affine balanced-kernel index**

\[
 b_{\mathrm{aff}}(\Phi)
 =
 \min_{\substack{0\ne\sigma\\
 \int \widehat\Phi\,d\sigma=0}}
 \max\{n_+(\sigma),n_-(\sigma)\},
\]

with value `+infinity` if no nonzero finite relation exists.

Then

\[
\boxed{
\mathcal M_\Phi\text{ is injective on }\mathcal P_{r,M}
\iff
b_{\mathrm{aff}}(\Phi)>r.
}
\tag{1}
\]

Equivalently, fixed-mass sparse positive fidelity is governed by the oriented circuits of the **affine point configuration** `Phi(X)`, or by the circuits of the augmented dictionary `widehat Phi`, rather than by the conic circuits of `Phi` alone.

If `b(Phi)` denotes AF-448's ordinary positive balanced-kernel index, then

\[
\boxed{
b_{\mathrm{aff}}(\Phi)\ge b(\Phi).}
\tag{2}
\]

Thus a fixed-mass law can only improve exact positive-atomic fidelity. But the gain is not generically "one observation." It is exactly the gain obtained by deleting those offending kernel circuits whose coefficients do **not** sum to zero. Depending on the feature geometry, this may give no improvement, a one-coordinate threshold shift, or remove the entire finite-dimensional ambiguity.

Geometrically, after dividing by `M`, every source in `P_{r,M}` is a probability measure and

\[
\frac1M\mathcal M_\Phi(\mu)
\]

is a convex combination of at most `r` points of `Phi(X)`. Hence `(1)` is equivalently a sparse barycentric-uniqueness theorem:

> fixed-mass `r`-atomic fidelity holds exactly when no point has two distinct convex representations whose two supports both have size at most `r`.

The minimal obstructions are balanced **Radon partitions**. This is the affine counterpart of AF-448's conic sign-balance criterion.

## Exact derivation

Assume first that `M_Phi` is not injective on `P_{r,M}`. Then there are distinct

\[
\mu,\nu\in\mathcal P_{r,M}
\]

with

\[
\mathcal M_\Phi(\mu)=\mathcal M_\Phi(\nu).
\]

Set

\[
\sigma=\mu-\nu.
\]

Because the two sources have equal total mass,

\[
\int 1\,d\sigma=0,
\]

and equality of their observed features gives

\[
\int\Phi\,d\sigma=0.
\]

Therefore

\[
\int\widehat\Phi\,d\sigma=0.
\]

After cancelling any common atoms between `mu` and `nu`, the positive and negative parts of `sigma` use no more atoms than the original sources, so

\[
 n_+(\sigma)\le r,
 \qquad
 n_-(\sigma)\le r.
\]

Hence `b_aff(Phi)<=r`.

Conversely, suppose there is a nonzero atomic relation

\[
\int\widehat\Phi\,d\sigma=0
\]

with

\[
 n_+(\sigma),n_-(\sigma)\le r.
\]

Write the Jordan decomposition

\[
\sigma=\sigma_+-\sigma_-.
\]

The constant coordinate of `widehat Phi` gives

\[
\sigma_+(X)=\sigma_-(X)=:t>0.
\]

The remaining coordinates give

\[
\int\Phi\,d\sigma_+
=
\int\Phi\,d\sigma_-.
\]

Scale both sides by `M/t`:

\[
\mu=\frac Mt\sigma_+,
\qquad
\nu=\frac Mt\sigma_-.
\]

Then `mu` and `nu` are distinct elements of `P_{r,M}` and have the same `Phi`-observation. This proves `(1)`.

Equation `(2)` is immediate because

\[
\ker\mathcal M_{\widehat\Phi}
\subseteq
\ker\mathcal M_\Phi.
\]

Appending the mass coordinate can delete kernel relations but cannot create new ones.

## Radon-partition form

Let a nonzero affine relation be written as

\[
\sum_{i=1}^N c_i\Phi(x_i)=0,
\qquad
\sum_{i=1}^N c_i=0.
\tag{3}
\]

Split the indices according to the sign of `c_i`. Since the coefficient sums on the two sides agree, after normalization `(3)` becomes

\[
\sum_{i\in I_+}\alpha_i\Phi(x_i)
=
\sum_{j\in I_-}\beta_j\Phi(x_j),
\qquad
\sum_{i\in I_+}\alpha_i
=
\sum_{j\in I_-}\beta_j
=1,
\tag{4}
\]

with positive `alpha_i,beta_j`. Thus the convex hulls of the two support sets intersect.

Conversely, every equality of convex combinations gives an affine kernel relation by subtracting the two barycentric representations. Therefore

\[
b_{\mathrm{aff}}(\Phi)
=
\min_{\text{affine Radon relations}}
\max\{|I_+|,|I_-|\}.
\tag{5}
\]

So normalization changes the obstruction class in a precise way:

- without fixed mass, positive collisions are intersections of finitely generated **cones** over feature points;
- with fixed mass, positive collisions are intersections of sparse **convex hulls** of feature points.

This distinction is source-side structure. It is not a downstream repair of information already lost: the mass law removes inadmissible source pairs before the observation map is tested.

## Chebyshev phase diagram: the whole threshold shifts by one coordinate

Suppose `X` is an interval and

\[
1,f_1,\ldots,f_m
\]

is a strict Chebyshev system. Take

\[
\Phi(x)=(f_1(x),\ldots,f_m(x)).
\]

Every minimal affine circuit of `m+2` ordered points has alternating signs. Consequently

\[
\boxed{
 b_{\mathrm{aff}}(\Phi)
 =
 \left\lceil\frac{m+2}{2}\right\rceil.
}
\tag{6}
\]

For `K`-atomic fixed-mass sources this produces a sharp three-stage boundary.

If

\[
m=2K-2,
\]

an alternating circuit on `2K` points has `K` positive and `K` negative coefficients. Hence two distinct fixed-mass `K`-atomic sources can collide.

If

\[
m=2K-1,
\]

minimal circuits have side sizes `K` and `K+1`. Therefore the observation is injective **within the model of at most `K` atoms**, but a `K`-atom source can still collide with a `(K+1)`-atom source.

If

\[
m=2K,
\]

minimal circuits have `K+1` atoms on both sides. Thus every fixed-mass source with at most `K` atoms is separated from every source with at most `K+1` atoms.

For ordinary power moments this says that known mass `m_0=M` shifts the AF-448 moment/Chebyshev phase boundary one transmitted coordinate earlier:

\[
\boxed{
\begin{array}{c|c}
\text{retained positive moments} & \text{fixed-mass fidelity}\
\hline
2K-2 & K\text{-vs-}K\text{ collisions remain}\\
2K-1 & \le K\text{ atoms are internally identifiable}\\
2K & K\text{-vs-}(K+1)\text{ collisions are excluded.}
\end{array}}
\tag{7}
\]

This recovers the observation-count gain in AF-446 but places it inside a general source-law theorem. The one-coordinate shift there is not a generic law of conservation constraints; it is a consequence of the alternating circuit geometry of the augmented Chebyshev system.

## Two controls: mass may buy nothing or everything

### No gain

Suppose two distinct source points `u,v` satisfy

\[
\Phi(u)=\Phi(v).
\]

Then

\[
\delta_u-\delta_v
\]

is already a zero-mass kernel relation. Therefore

\[
b(\Phi)=b_{\mathrm{aff}}(\Phi)=1.
\]

Fixing total mass does nothing: `M delta_u` and `M delta_v` remain indistinguishable.

This is the basic falsification control for any claim that normalization automatically restores a discriminator. It helps only when the bad relation violates the source law.

### A single conserved scalar can remove the entire finite kernel

Let `X={x_1,\ldots,x_5}` and map into `R^4` by

\[
\Phi(x_1)=e_1,
\quad
\Phi(x_2)=2e_1,
\quad
\Phi(x_3)=e_2,
\quad
\Phi(x_4)=e_3,
\quad
\Phi(x_5)=e_4.
\tag{8}
\]

Without a mass constraint,

\[
2\delta_{x_1}
\quad\text{and}\quad
\delta_{x_2}
\]

have the same observation, so `b(Phi)=1`.

But the five augmented columns

\[
(1,\Phi(x_j))\in\mathbb R^5
\]

are linearly independent. Subtracting the first augmented column from the other four leaves the independent vectors

\[
e_1,
\quad -e_1+e_2,
\quad -e_1+e_3,
\quad -e_1+e_4
\]

in the last four coordinates. Hence

\[
 b_{\mathrm{aff}}(\Phi)=+\infty.
\]

For every fixed `M>0`, the observation is therefore injective on **all** positive measures supported on these five points, regardless of sparsity.

So one conserved scalar can, in a finite source model, eliminate an arbitrarily serious conic ambiguity rather than merely increment an observation count by one. The correct currency is circuit elimination, not raw scalar count.

## Prior art and novelty audit

The mathematical ingredients are classical and no novelty is claimed for them.

Radon's theorem and its descendants identify affine dependence with partitions whose convex hulls intersect. In oriented-matroid language, signed circuits record the two sides of minimal affine dependencies. See H. Radon, **“Mengen konvexer Körper, die einen gemeinsamen Punkt enthalten,”** *Mathematische Annalen* 83 (1921), 113–115, and A. Björner, M. Las Vergnas, B. Sturmfels, N. White, G. M. Ziegler, *Oriented Matroids*, 2nd ed., Cambridge University Press (1999), especially the chapters on realizability and convex polytopes.

The sparse nonnegative-recovery literature makes the same convex-geometric passage from nonnegative coefficients to simplices and neighborly polytopes. Donoho and Tanner, **“Sparse nonnegative solution of underdetermined linear equations by linear programming,”** *PNAS* 102(27), 9446–9451 (2005), and **“Neighborliness of randomly projected simplices in high dimensions,”** *PNAS* 102(27), 9452–9457 (2005), connect sparse nonnegative representation to faces and neighborliness of projected simplices. Their discussion also explicitly links moment-curve constructions to moment-space unicity.

For the alternating-sign circuit law of Chebyshev systems, see S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Wiley/Interscience (1966). AF-448 already records the corresponding oriented-circuit interpretation, while AF-446 records the fixed-mass consecutive-moment specialization.

The Arithmetic Fidelity contribution here is therefore an **audit synthesis**, not a new convexity theorem: it identifies exactly what a conserved total mass does to the AF-448 fidelity obstruction. The source law is equivalent to adding a constant feature **before testing collisions**, which replaces conic sign-balance by affine/Radon sign-balance. That distinction gives a reusable test for future arithmetic source laws and explains why the one-coordinate moment gain of AF-446 is structural rather than a generic dimensional rule.

## Boundaries and falsification checks

- The theorem is about **exact** fidelity. `b_aff>r` gives no quantitative lower bound on separation or conditioning. Affine circuits may approach degeneracy arbitrarily closely even when exact collisions are excluded.
- Positivity is essential to the Radon interpretation. Signed source classes revert to ordinary sparse linear dependence with the mass coordinate appended.
- The mass must be known and identical on the compared source class. Merely knowing that masses lie in an interval does not force the difference relation to have zero total coefficient.
- For several affine source constraints, blindly appending all constraint functions is not by itself sufficient to characterize one fixed inhomogeneous level set: a kernel relation only says that its two sides have the same constraint values, not necessarily the prescribed values. Fixed mass is special because every nonzero zero-mass signed relation has positive and negative parts with the same positive total mass, which can be rescaled to the prescribed `M` without changing support counts.
- Equation `(6)` assumes the **augmented** family `1,f_1,...,f_m` is a strict Chebyshev system and that the domain contains enough distinct points to realize the relevant circuits.
- The five-point control is deliberately finite. It demonstrates that a scalar conservation law can have much more than a one-rank effect on the admissible collision set; it does not claim analogous complete recovery for a continuum dictionary.
- A mass law shared equally by rational-prime and matched non-prime controls is universal source structure, not an arithmetic discriminator. Prime-specific value appears only if arithmetic admissibility excludes affine circuits that the matched controls still realize, or if additional arithmetic constraints supply genuinely independent coordinates.
- Nothing here implies RH or identifies a new zeta mechanism.

A direct falsification of `(1)` would require either a fixed-mass collision whose signed difference is not an affine kernel relation, or an affine kernel relation with at most `r` atoms per sign that cannot be rescaled into a fixed-mass collision. The first contradicts subtraction of equal-mass observations; the second contradicts equality of the positive and negative total masses forced by the appended constant coordinate.

## Consequence for the research line

AF-448 turns sparse positive fidelity into an oriented-kernel problem. AF-449 now separates **conic** from **affine** source geometry: a conserved mass does not magically restore information and does not generically purchase one scalar degree of freedom. It filters the obstruction set by imposing zero coefficient sum, so its exact value is measured by which balanced circuits survive that filter.

This gives a sharper rule for later arithmetic applications. Before claiming that a conservation law, normalization, Euler constraint, or source-side identity protects a prime discriminator, identify the offending kernel circuits and ask whether the proposed law actually removes them. If the same affine/Radon circuits remain in a matched non-prime control, the law has preserved generic convex geometry rather than rational-prime provenance.