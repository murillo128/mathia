---
type: adversarial-review
target: research/weil_inertia/findings/WI-188-count-saturating-bows-force-self-dual-twisted-prime-covariance.md
---

# Adversarial review

## Adversary

The passage from count saturation `c=4π+o(1)` to the square-root scale used in Section 4 needs a stronger rate. From `α_*=2π/c=1/2+o(1)` one gets only `x_*=T^{1/2+o(1)}=√T·T^{o(1)}`, not `x_*=√T(1+o(1))`. Consequently

\[
\frac{U}{x_*^2}=\frac{\theta T}{T^{2\alpha_*}}=\theta T^{1-2\alpha_*}
\]

need not stay bounded above and below by positive constants. For example, `α_*=1/2+1/√log T` still satisfies `α_*=1/2+o(1)` but makes `U/x_*^2→0`, while the opposite sign makes it diverge. Thus (23)--(24), and hence the claim of `Θ(h)` lattice aliases per shift at the count-saturating scale, do not follow from WI-184's stated `c=4π+o(1)` asymptotic alone.

Resolve the objection either by proving quantitative saturation strong enough that `(α_*-1/2)log T→0` (for example a sufficient rate `c-4π=o(1/log T)`), or by retaining the factor `U/x_*^2` throughout the derivative/alias analysis and weakening the self-dual stationary-lattice conclusion to the regime actually justified by its asymptotics. The earlier polynomial resolution-barrier calculation using `x_*=T^{1/2+o(1)}` is not the issue; the objection is specifically to upgrading that exponent-level statement to the multiplicative square-root normalization required by Section 4.