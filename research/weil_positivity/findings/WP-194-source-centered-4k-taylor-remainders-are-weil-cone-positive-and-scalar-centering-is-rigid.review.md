---
type: adversarial-review
target: research/weil_positivity/findings/WP-194-source-centered-4k-taylor-remainders-are-weil-cone-positive-and-scalar-centering-is-rigid.md
---

# Adversarial review

## Adversary

Section 2 overstates the centered scalar Fourier-positivity claim by asserting it for every order `n>=3` and both signs of the scalar perturbation. For a negative scalar shift this fails at odd order. For example, take `c=0`, `n=3`, and `v=-a<0`. Taylor's integral remainder, written with increasing integration limits on `[-a,0]`, has density

\[
\eta_{3,0,-a}(\lambda)=-\frac{(-a-\lambda)^2}{2}\,\mathbf 1_{[-a,0]}(\lambda),
\]

so its evenization is

\[
-\frac{(a-|x|)_+^2}{4},
\]

not the positive kernel displayed in equation (5). Its Fourier transform is therefore strictly negative at `0` and is the negative of the triangle-mixture transform used in (10), contradicting the statement that every centered scalar density of order at least three has strictly positive Fourier transform after evenization.

This does not appear to damage the advertised `4k` theorem: for even `n` the sign reversal from the reversed integration limits is canceled by the odd power `r=n-1`, so the positive centered kernel used for `4k` (and `4k+2`) remains valid. The objection is resolved by restricting the general scalar positivity statement and equations (5)--(10) to the applicable parity/sign regime, or by carrying the missing sign factor explicitly. The canonical finding should not claim all `n>=3` until that distinction is made.
