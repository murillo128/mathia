---
type: adversarial-review
target: research/mobius_cancellation/findings/MC-096-prime-block-radialization-collision-reconstruction-tradeoff.md
---

# Adversarial review

## Adversary

The exact product bound (1)/(28) is sound for every `0<r<=1`, but the finding overstates one of its unilateral consequences when the noise radius may depend on `N`. The top-level claim says that if the quotient has only `N^{o(1)}` relevant profiles, then the collision step is already `N^{1-o(1)}`, and Section 6 repeats that such block families force a generic collision norm `N^{1-o(1)}`. Equation (26), however, gives only

`||A_r|| >= r^2 sqrt(|T_{N,alpha}|/D_{N,alpha})`.

Thus `D_{N,alpha}=N^{o(1)}` implies `||A_r||=N^{1-o(1)}` only with an additional lower-scale hypothesis such as fixed `r` (as Section 5 later states explicitly), or more generally `r=N^{-o(1)}`. For example, a polynomially shrinking `r` can make the collision norm polynomially smaller while the endpoint norm grows correspondingly; the radius-independent no-free-lunch statement survives only at the product level.

Please either add the missing fixed/subpolynomial-radius hypothesis wherever the collision norm alone is claimed to be `N^{1-o(1)}`, or reformulate those sentences purely in terms of the radius-independent product tradeoff. This objection does not challenge the degree-two positive rectangle, the exact norms (11)/(13), or the product lower bound itself.
