# MI-096 — Empty-vector staged sieve residuals can lose all internal sign oscillation

**Evidence level:** exact synthesis from [MC-469](../../findings/MC-469-empty-vector-sieve-component-survives-small-outer-cell-pruning.md) and [MC-470](../../findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md), within the concrete modified linear-sieve decomposition used there.

MC-469 shows that support pruning cannot remove every staged component. The empty-vector term has `alpha=delta_1`, `beta=lambda^(0)` and therefore sits at `R=T=1`, exactly where the growing outer-support tariff vanishes. Its surviving analytic object is not the original beta-sieve coefficient sequence but the divisor recombination

`B_(lambda^(0))(y)=sum_(d|y) lambda_d^(0)`.

MC-470 computes that recombination in its native sieve geometry. If `m_z(y)` is the squarefree product of primes below `z` dividing `y`, then

`B_(lambda^(0))(y)=sum_(d|m_z(y), d in D^+(Q)) mu(d)`

is a nonnegative integer. It is the upper-sieve first-exit boundary count, dominates the `z`-rough indicator and equals one on genuinely `z`-rough inputs. Thus the coefficient signs that made `lambda^(0)` look oscillatory before divisor recombination are no longer available after the staged map: the destination amplitude itself is positive.

There is an exact structural exclusion inside the nonrough part. If `m_z(y)>1`, `k=omega(m_z(y))`, and `epsilon(k+2)<=1`, every divisor participating in the full Möbius cancellation lies inside the admissible upper-sieve region, so the recombined amplitude is zero. Positive nonrough residuals therefore require sufficiently high small-prime rank. This is useful localization but not a power-saving theorem: the full `z`-rough population survives with weight one, and the high-rank boundary set has not been proved sparse on the relevant affine source trajectories.

The reusable lesson is that **signed coefficients are not a retained cancellation resource unless their signs survive the exact representation map being estimated**. A divisor transform can turn an alternating sieve sequence into a positive counting observable. Once that happens, an argument cannot appeal again to the internal coefficient signs without changing representation and carrying the corresponding cross terms explicitly.

For the present q-vdC branch, the base component must therefore gain elsewhere: cancellation of the translated-character phase against the positive rough/boundary weight, cancellation in the outer aggregated coefficients before absolute values, or cross-component interference in the complete signed decomposition. The low-rank vanishing gate may reduce the boundary correction only after a quantitative affine incidence estimate proves that it actually removes enough source mass.

**Boundary.** This conclusion is specific to the concrete upper linear-sieve base weight and its exact staged divisor recombination. It does not say that every sieve divisor sum is nonnegative, that the high-rank boundary correction is dense or sparse, or that the positive residual has unfavorable character correlation. It removes one proposed internal sign resource; it does not prove the desired conductor-power estimate impossible.