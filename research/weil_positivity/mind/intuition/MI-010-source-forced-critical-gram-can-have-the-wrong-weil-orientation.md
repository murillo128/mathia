# MI-010 — A source-forced critical Gram can have the wrong Weil orientation

**Evidence level:** exact Bost--Connes divisibility/KMS conditioning and local Weil-defect comparison through WP-216

## Core intuition

Matching the critical half-density, the prime logarithmic scale, and a canonical positive geometry is still not enough for Weil positivity. The sign theorem depends on **orientation**, not only on magnitude or source naturality.

Bost--Connes divisibility conditioning supplies a particularly sharp example. At the actual critical inverse temperature, source-defined range projections generate the positive GCD Gram whose prime-axis kernel has coefficients `p^{-|a-b|/2}`. Those are exactly the critical Weil magnitudes. Yet the desired local finite Weil Toeplitz ray is the defect `log p (I-G_p)`, and that defect is indefinite. The source has selected the right scale while positivity points in the opposite direction.

## Strongest justified principle

For the canonical range projections `E_n=mu_n mu_n^*`, the semilattice law `E_mE_n=E_lcm(m,n)` and the KMS identity `phi_beta(E_n)=n^{-beta}` give normalized vectors with Gram

`G_beta(m,n)=(gcd(m,n)/sqrt(mn))^beta`.

At `beta=1`, the prime-axis restriction is the Poisson Toeplitz kernel with radius `p^{-1/2}`, and the Bost--Connes time evolution independently supplies the generator scale `log p`. No scalar `F(H)`, Borel prime-power projector, or inserted zero data is needed.

WP-216 then identifies the exact sign mismatch. In the finite-Weil normalization, the nonzero Fourier coefficients are `-(log p)p^{-|k|/2}`, so the local target is `log p(I-G_p)`. Its symbol changes sign. The minimal scalar diagonal repair is the same local threshold previously isolated in WP-096, and the all-prime compensation diverges. Mixed-prime terms can make a larger kernel positive, but that positivity comes from an additional completion, not from the conditioned Gram itself.

## Counterevidence / boundary

This does not show that Bost--Connes geometry cannot contribute to a Weil proof. It shows only that the canonical critical conditional Gram is not itself the desired sign theorem. A non-scalar global operation, indefinite-to-positive completion, modular relation, or finite--archimedean coupling could still transform the source geometry in a canonical way.

The result is local on prime axes for the orientation comparison. A successful global relation could use mixed-prime and archimedean structure in a way not visible from one axis, but it must derive rather than prescribe the needed sign change.

## Epistemic status

**Exact source-forced critical magnitude and exact negative orientation test; the global sign-producing operation remains open.**

## Falsification criterion

Refute the divisibility/KMS Gram identity or the equality of the local Weil ray with `log p(I-G_p)`, or exhibit a positivity theorem for that defect without adding a source-external compensating structure. A positive continuation should instead identify the extra source-forced operation and prove that its completed form has the Weil orientation while retaining the exact prime and archimedean normalization.
