# AF-453 — Weakly collapsing secants force zero total-variation conditioning

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-LAW`, `QUANTITATIVE-FIDELITY`, `TOPOLOGY-MISMATCH`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`

## Claim

AF-452 identifies fixed-source-law conditioning with the minimum observation gain on the normalized carrier of completable source secants, once the physical source metric is fixed. For total variation there is a sharp topological obstruction that is independent of arithmetic: **finite continuous observations cannot have a positive uniform total-variation gain on any source fiber containing weakly collapsing secants whose total-variation size stays nonzero.**

Let `X` be a metric space with its Borel sigma-algebra, let

\[
\Psi:X\to\mathbb R^q,
\qquad
\Phi:X\to\mathbb R^m
\]

be continuous, and assume either that `Phi` is bounded or that all measures below are supported in one compact set. For `r>=1` and a prescribed source law `u`, write

\[
\mathcal P_{r,u}^{\Psi}
=
\left\{\mu:\mu\text{ is a probability measure with finite support},\ |​\operatorname{supp}\mu|​\le r,\ \int\Psi\,d\mu=u\right\}.
\]

Use the signed-measure total-variation norm

\[
\|\sigma\|_{TV}=|\sigma|(X)
\]

and any norm `||.||_Y` on `R^m`. Define

\[
\kappa_{r,u}^{TV}(\Phi)
=
\inf_{\substack{\mu,\nu\in\mathcal P_{r,u}^{\Psi}\\\mu\ne\nu}}
\frac{\left\|\int\Phi\,d(\mu-\nu)\right\|_Y}{\|\mu-\nu\|_{TV}}.
\tag{1}
\]

Then:

1. **Weak-collapse criterion.** If there are pairs `mu_n,nu_n` in the prescribed fiber such that
   \[
   \mu_n-\nu_n\rightharpoonup0
   \tag{2}
   \]
   weakly against bounded continuous tests while
   \[
   \inf_n\|\mu_n-\nu_n\|_{TV}>0,
   \tag{3}
   \]
   then
   \[
   \boxed{\kappa_{r,u}^{TV}(\Phi)=0.}
   \tag{4}
   \]

2. **Moving-atom corollary.** Let
   \[
   L_u=\Psi^{-1}(u).
   \]
   If `L_u` contains a non-isolated point `x`, so that distinct `x_n in L_u` satisfy `x_n->x`, then for every `r>=1`
   \[
   \boxed{\kappa_{r,u}^{TV}(\Phi)=0.}
   \tag{5}
   \]
   Indeed `delta_{x_n}` and `delta_x` are admissible one-atom sources, their total-variation difference has norm `2`, but their finite continuous observations coalesce.

3. **Exact injectivity does not rescue the margin.** If `Phi` is injective on `L_u`, then the observation is exactly injective on the one-atom source fiber while `(5)` still holds whenever `L_u` is non-discrete. Thus exact sparse identifiability and positive total-variation conditioning are genuinely different questions even before multi-atom collisions enter.

4. **Common-background completion preserves the obstruction.** Suppose a moving core `delta_{x_n}-delta_x` with `Psi(x_n)=Psi(x)=v` can be completed into the prescribed source-law fiber by one common probability background `rho` and a fixed `tau in (0,1]`:
   \[
   \mu_n=\tau\delta_{x_n}+(1-\tau)\rho,
   \qquad
   \nu_n=\tau\delta_x+(1-\tau)\rho,
   \tag{6}
   \]
   with both measures obeying the support budget and source law `u`. Then
   \[
   \|\mu_n-\nu_n\|_{TV}=2\tau
   \]
   while
   \[
   \left\|\int\Phi\,d(\mu_n-\nu_n)\right\|_Y
   =
   \tau\|\Phi(x_n)-\Phi(x)\|_Y\to0.
   \]
   Hence completion can move the obstruction between source-law fibers but cannot repair its normalized total-variation margin, exactly as AF-452 predicts.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{a continuous observation topology cannot be uniformly faithful in a strictly finer source metric on any admissible secant family that collapses only in the weaker topology.}
}
\tag{7}
\]

For total variation versus finite continuous measurements, moving atoms are the elementary witness. A positive arithmetic lower bound in total variation therefore requires the admissible source law itself to exclude such motions, for example through a genuinely discrete support class or another rigidity condition. It cannot be obtained merely by adding more continuous coordinates to `Phi` while leaving a non-discrete atomic source fiber available.

## Exact derivation

Let

\[
\sigma_n=\mu_n-\nu_n.
\]

Weak convergence `(2)` means that for every bounded continuous scalar function `f`,

\[
\int f\,d\sigma_n\to0.
\]

Apply this coordinatewise to the finite-dimensional continuous observation `Phi=(phi_1,\ldots,phi_m)`. Under the boundedness/compact-support hypothesis,

\[
\int\Phi\,d\sigma_n\to0
\]

in `R^m`, hence in every norm on `R^m`. Condition `(3)` gives a constant `c>0` such that

\[
\frac{\left\|\int\Phi\,d\sigma_n\right\|_Y}{\|\sigma_n\|_{TV}}
\le
\frac{\left\|\int\Phi\,d\sigma_n\right\|_Y}{c}
\to0.
\]

Since every pair occurs in the infimum `(1)`, equation `(4)` follows.

For the moving-atom corollary, continuity of `Psi` is not by itself enough; the hypothesis is the stronger exact source-law motion `x_n,x in L_u`. The two Dirac measures are mutually singular whenever `x_n!=x`, so

\[
\|\delta_{x_n}-\delta_x\|_{TV}=2.
\tag{8}
\]

On the other hand, continuity of `Phi` gives

\[
\left\|\Phi(x_n)-\Phi(x)\right\|_Y\to0.
\tag{9}
\]

Equations `(8)` and `(9)` prove `(5)` directly. Notice that the argument does not need an exact observation collision: if `Phi` is injective on the level set, every numerator is positive, yet their infimum after total-variation normalization is still zero.

For the completed version `(6)`, subtraction gives

\[
\mu_n-\nu_n
=
\tau(\delta_{x_n}-\delta_x),
\]

so absolute homogeneity of the total-variation norm and linearity of the observation map cancel the same factor `tau` from numerator and denominator. This is the AF-452 completed-secant identity in its simplest topological degeneration.

## Metric control: the same atom motion does not automatically kill `W_1`

The no-go theorem is not a statement that continuous finite observations are intrinsically unstable. It is a statement about a mismatch between the observation topology and the declared physical source metric.

If `X` is metric and the source metric is Wasserstein-1, then for Dirac masses

\[
W_1(\delta_x,\delta_y)=d(x,y).
\tag{10}
\]

Therefore the same one-atom level-set family has lower gain

\[
\inf_{\substack{x,y\in L_u\\x\ne y}}
\frac{\|\Phi(x)-\Phi(y)\|_Y}{d(x,y)}.
\tag{11}
\]

A positive value is possible precisely when the retained feature map is lower-Lipschitz on that admissible source set. For example, if `X` is a compact interval, `Psi` is constant, and `Phi(x)=x`, then the one-atom observation has `W_1` gain exactly `1`, whereas its total-variation gain is `0` by `(5)`.

This gives a matched control with the *same sources and the same observation*. Only the source metric changes. The failure is therefore not arithmetic and not a lack of exact information in `Phi`; it is caused by asking a weakly continuous observation to control a metric that regards arbitrarily nearby distinct atoms as a fixed positive distance apart.

Bounded-Lipschitz and related weak metrics behave like `W_1` in this respect: moving Dirac masses become close in the source metric. Total variation does not. AF-452's statement that all of these are difference-homogeneous is therefore only the algebraic first gate. **Homogeneity makes common-background cancellation exact; topological compatibility determines whether the resulting normalized carrier can have positive gain.**

## Consequence for finite moment and spectral observations

Every finite family of continuous moments, Fourier coefficients, kernel evaluations, or other continuous test functions falls under the theorem. If the admissible source law leaves even one continuous atom-motion direction, no such finite observation family can have a positive uniform lower Lipschitz modulus in total variation.

This places the exact moment/Radon results AF-448--AF-452 on the correct stability side of the boundary. Chebyshev or oriented-matroid structure may prove that two admissible sparse sources never have *identical* finite observations. It does not by itself supply total-variation stability: atoms can approach each other while remaining distinct and exactly identifiable at every finite separation.

The theorem also explains why stable super-resolution results are commonly stated in Wasserstein, localization, or separation-sensitive geometries rather than as a uniform inverse bound in total variation on unrestricted moving point sources. If one insists on a strong source metric, the missing ingredient must enter on the source side -- minimum separation, a discrete support alphabet, quantization, or another condition that removes weakly collapsing secants -- rather than being manufactured by downstream continuous measurements.

## Prior art and novelty audit

The topology behind the theorem is classical, and no novelty is claimed for weak convergence, total variation, Wasserstein geometry, or the instability of near-colliding point-source inversion.

- Patrick Billingsley, ***Convergence of Probability Measures***, 2nd ed., Wiley (1999), is a standard reference for weak convergence of probability measures and the characterization through bounded continuous test functions. The implication used above is elementary: weakly vanishing signed differences are invisible asymptotically to every fixed finite family of bounded continuous tests.
- Cédric Villani, ***Optimal Transport: Old and New***, Grundlehren der mathematischen Wissenschaften 338, Springer (2009), DOI `10.1007/978-3-540-71050-9`, gives the standard Wasserstein and Kantorovich duality framework. In particular, `W_1` reflects displacement of Dirac masses rather than treating distinct atoms as maximally separated.
- Mathias Hockmann and Stefan Kunis, **“Weak Sparse Superresolution Is Well-Conditioned,”** *SIAM Journal on Imaging Sciences* 16(1), SC1--SC13 (2023), DOI `10.1137/22M1521353`, explicitly obtains global Lipschitz conditioning when sparse super-resolution is measured in a Wasserstein metric. This is direct prior art for the principle that a weak source geometry can restore meaningful conditioning even where stronger measure norms are inappropriate.
- Armin Eftekhari, Tamir Bendory, and Gongguo Tang, **“Stable Super-Resolution of Images: A Theoretical Study,”** *Information and Inference* 10(1), 161--193 (2021), DOI `10.1093/imaiai/iaaa029`, proves stable recovery of positive point sources in a generalized Wasserstein metric and places finite continuous measurements, positivity, and source geometry in the same inverse-problem setting.
- Dmitry Batenkov, Gil Goldman, and Yosef Yomdin, **“Super-resolution of near-colliding point sources,”** *Information and Inference* 10(2), 515--572 (2021), arXiv:`1904.09186`, quantifies the severe conditioning deterioration created by clustered nodes in finite-band spectral inversion. Its setting and error metrics differ from `(1)`, but it is strong neighboring evidence that collision geometry, not exact noiseless identifiability alone, governs stable inversion.

The exact no-go `(4)` is a direct topology argument rather than a claimed new theorem. Its durable Arithmetic Fidelity role is to sharpen AF-452's metric warning into a reusable gate: **before seeking an arithmetic lower gain, compare the topology induced by the physical source metric with the topology seen by the retained observations. If admissible secants vanish observationally while staying bounded away from zero in the source metric, the uniform fidelity constant is already forced to vanish.**

## Boundaries and falsification checks

- The theorem concerns a **uniform lower Lipschitz modulus**. It does not deny pointwise continuity of an inverse at specially isolated sources, local conditioning after imposing separation, or recovery under a weaker source metric.
- The moving-atom corollary requires exact motion inside the prescribed source-law level set `Psi^{-1}(u)`. A source law that isolates every admissible atom can eliminate this particular obstruction.
- A finite-dimensional continuous observation is used. Discontinuous point-identifying observables can separate total variation at small spatial scales, but such observables change the observation class and must be justified independently rather than inserted as an arbitrary target encoder.
- Condition `(2)` is sufficient, not necessary, for zero total-variation gain. A sequence can have vanishing observation gain without converging weakly to zero against *all* continuous tests.
- Minimum separation among atoms inside each individual measure does not automatically exclude the one-atom control, because a one-atom source has no internal collision. To obtain a uniform total-variation margin one needs a restriction that also prevents distinct admissible source locations from approaching each other, such as a discrete/quantized location set or a pairwise separation condition across the comparison class.
- The theorem is not arithmetic evidence. If the rational-prime source class is discrete in the physically justified source topology, the moving-atom obstruction may be absent. That absence is only a gate; a positive arithmetic gain still requires an explicit lower bound against matched non-prime controls.

## Research consequence

AF-452 reduced stable fixed-source fidelity to observation gain on the completed secant carrier. AF-453 now removes one large false target from that problem: **total variation cannot be the metric in which a finite continuous observation family exhibits uniform stable fidelity whenever the admissible class contains continuously moving atoms or, more generally, weakly collapsing secants of nonvanishing total variation.**

The next arithmetic test should therefore start by fixing the physically justified source topology. If the rational-prime model is intrinsically discrete, total variation remains viable but must be compared against matched discrete non-prime controls. If the source is allowed continuous perturbations of locations, `W_1`, bounded-Lipschitz, or another weak geometry is the relevant candidate, and the problem becomes a genuine lower-gain estimate on the completed source-law secant carrier rather than an impossible topology mismatch.