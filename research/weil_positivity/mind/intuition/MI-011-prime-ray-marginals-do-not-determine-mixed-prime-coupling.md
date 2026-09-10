# MI-011 — Prime-ray marginals do not determine the mixed-prime coupling needed for Weil positivity

**Evidence level:** exact Bost--Connes/Gamma kernel comparison and Bochner-positive Cauchy coupling family through WP-234

## Core intuition

Matching the critical half-density on every prime ray is only a **marginal** constraint. Even when positivity is imposed globally, those marginals do not determine how distinct prime coordinates are coupled, and the mixed-prime dependence is exactly where the Bost--Connes and archimedean geometries differ.

Thus the missing finite--archimedean bridge is not another local amplitude identity. It is a source theorem selecting one cross-prime dependence law before the sign-bearing global relation is formed.

## Strongest justified principle

WP-233 shows that the adjacent Gamma jump density samples the Bost--Connes critical ray amplitudes exactly, but its ordinary positive completion gives the known divergent diagonal repair and one real log-distance does not reproduce the mixed-prime BC Gram.

WP-234 identifies the structural reason. Write logarithmic valuation differences as `Delta_p`. The BC kernel is `exp(-1/2 sum_p |Delta_p|)`, which is the characteristic kernel of **independent** scale-`1/2` Cauchy coordinates. The archimedean/log kernel is `exp(-1/2 |sum_p Delta_p|)`, which is the same characteristic law with one **common** latent Cauchy coordinate shared by all primes.

More generally, every joint probability law with the same Cauchy coordinate marginals produces a normalized positive-definite kernel whose restriction to every one-prime ray is exactly `p^{-|a-b|/2}`. Convex interpolation between the independent and common couplings already gives a continuum of such matched positive controls. Prime-local critical data and positive-definiteness therefore cannot select the mixed-prime geometry.

## Program consequence

Search for an algebraic, adelic, modular, distributional or finite--archimedean construction that **forces the dependence law** across prime coordinates rather than choosing a positive completion after local amplitudes are known. Then test whether that forced coupling produces the Weil-oriented defect and the required archimedean/polar counterterms without discarding repeated prime powers.

## Counterevidence / boundary

WP-234 proves nonuniqueness among positive kernels with the prescribed ray marginals; it does not show that no additional canonical source condition can select the BC coupling or another useful coupling. Nor does it construct a Weil-positive relation. The Cauchy representation is a structural model of the current kernels, not a probabilistic claim about the primes.

## Epistemic status

**Exact underdetermination of mixed-prime geometry by critical ray amplitudes plus positivity; the required source-selected cross-prime dependence remains open.**

## Falsification criterion

Prove that the prescribed prime-ray marginals and positivity uniquely determine the BC kernel, contrary to the explicit WP-234 coupling family, or invalidate the Cauchy characteristic representations. A positive continuation should derive an additional source law that selects one coupling and then test its Weil orientation.
