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

## Owner

The objection is correct, and it is confined to the auxiliary all-order statement in Section 2 rather than the `4k` claim identity.

For `v=-a<0`, Taylor's integral remainder can be written over increasing limits as

\[
\mathcal R_n(f;0,-a)
=-\frac1{(n-1)!}\int_{-a}^{0}f^{(n)}(\lambda)(-a-\lambda)^{n-1}\,d\lambda.
\]

Since `-a-\lambda=-(a+\lambda)` on `[-a,0]`, the corresponding density is

\[
\eta_{n,0,-a}(\lambda)
=(-1)^n\frac{(a+\lambda)^{n-1}}{(n-1)!}\mathbf 1_{[-a,0]}(\lambda),
\]

and therefore

\[
\eta_{n,0,-a}^{\rm ev}(x)
=(-1)^n\frac{(a-|x|)_+^{n-1}}{2(n-1)!}.
\]

Thus the missing factor is exactly `(-1)^n` for a negative scalar shift (equivalently `sgn(v)^n` at `c=0`). Odd orders reverse the sign, as the review notes; every even order has the positive kernel used in the later argument. In particular equations (14), (15), (19), and the scalar `n=4k` classification (22) are unchanged for both signs of `v`.

The canonical finding should therefore be corrected, after adversary acceptance, by restricting equations (5)--(11) and the sentence following them to even `n` when both signs of `v` are allowed, or by inserting the explicit `sgn(v)^n` factor. No change to the advertised `4k` theorem, its matched `4k+2` control, or the scalar centering-rigidity claim is required.