---
type: adversarial-review
target: research/xi_flow/findings/XF-152-initial-off-circle-maximal-contact-trace-has-an-exact-one-sided-visibility-threshold.md
---

# Adversarial review

## Adversary

The stated quantifier “for every \(D>0\)” is false as written. Taking \(D=\pi\) gives \(\cos^2 D=1\), so
\[
F_+(H,\pi)=H+\log\cosh H,
\]
which vanishes only at \(H=0\) and is strictly positive for every \(H>0\). The displayed formula likewise gives \(H_*(\pi)=0\), not a unique positive zero. More generally the positive threshold exists when \(|\cos D|<1\); the exceptional values \(D\in\pi\mathbb Z\) have only the zero threshold.

The intended physical near-antipodal regime appears to be \(0<D\le\pi/2\) (equivalently a distance \(0<d\le L/2\)), where the claim is correct. Please make that physical domain explicit wherever the positive-root and threshold statements are quantified, or otherwise state the exact mathematical domain and handle the exceptional values separately.

## Owner

Accepted. The literal quantifier `for every D>0` is too broad; the intended statement uses the fundamental physical distance from the antipodal point, so one chooses `0<=d<=L/2` and hence `0<=D<=pi/2`.

On the nondegenerate physical range `0<D<=pi/2`,
\[
F_+(0,D)=\log|\cos D|<0,
\qquad
\partial_HF_+(H,D)
=1+\frac{\sinh H\cosh H}{\cos^2D+\sinh^2H}>0
\]
for `H>0`, while `F_+(H,D)->+infinity` as `H->infinity`. Thus there is exactly one positive zero, and solving its quadratic gives the displayed formula for `H_*(D)`. At `D=0` the threshold is instead `H_*(0)=0` and should be stated separately. If one extends `D` outside the fundamental physical range, the exact mathematical statement is periodic: a positive zero exists precisely when `D notin pi Z`, whereas for `D in pi Z` the only zero is `H=0`.

The near-antipodal expansion and the downstream XF-153 theorem are unaffected: XF-153 already works in the stricter sector `0<=D<=pi/4`. I therefore regard this as a domain correction to the same physical threshold claim, not a new claim identity. If accepted, I will persist the corrected physical domain and the `D=0` boundary case naturally in XF-152 before closure.