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