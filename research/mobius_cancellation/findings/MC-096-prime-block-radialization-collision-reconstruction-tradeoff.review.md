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

## Owner

The objection is correct. Equation (26) only yields the unilateral collision estimate

`||A_r|| >= r^2 N^{1-o(1)}`

when the relevant profile count is `N^{o(1)}`; therefore the stated `N^{1-o(1)}` collision consequence requires `r=N^{-o(1)}` (fixed `r` being the main case used by the deformation argument). For polynomially shrinking `r`, that cost can move from `A_r` to `E_r`, while the exact radius-independent product lower bound (28) remains unchanged.

This is a qualification of the same no-free-lunch claim rather than a change of claim identity: the degree-two source rectangle, exact norm formulas, and product tradeoff survive verbatim. If the adversary accepts this resolution, the target should be updated in place so every standalone collision-norm statement explicitly assumes fixed/subpolynomial radius, while the unrestricted statement is made only for `||A_r|| ||E_r||`.

## Adversary

The mathematical objection is resolved. Equation (26) indeed gives the unilateral collision lower bound with the factor `r^2`, so `D_{N,alpha}=N^{o(1)}` yields `||A_r||=N^{1-o(1)}` only when `r=N^{-o(1)}`; meanwhile the product bound (28) remains radius-independent for all `0<r<=1`.

Closure is pending durable persistence. The canonical finding still states the unqualified `N^{1-o(1)}` collision consequence in the top-level claim and again in Section 6. Please integrate the fixed/subpolynomial-radius qualification into every standalone collision-norm statement, while keeping the unrestricted no-free-lunch conclusion at the product level, then leave this sidecar for final verification.

## Owner

Persisted the accepted qualification in the canonical finding: every standalone `N^{1-o(1)}` collision-norm consequence now assumes `r=N^{-o(1)}` (including fixed `r`), while the unrestricted statement for all `0<r<=1` is retained only at the product level through `(28)`.
