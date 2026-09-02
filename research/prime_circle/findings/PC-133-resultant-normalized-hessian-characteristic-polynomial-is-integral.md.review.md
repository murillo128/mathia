---
type: adversarial-review
target: research/prime_circle/findings/PC-133-resultant-normalized-hessian-characteristic-polynomial-is-integral.md
---

# Adversarial review

## Adversary

The exceptional `(m,n)=(3,6)` exact control in §4 is internally inconsistent with its own displayed polynomial and with canonical `PC-129`.

From the displayed factorization

\[
\det(tI+H_{3,6})
=\frac14\,t(t+2)(2t+1)(2t+5),
\]

the coefficient of `t` is

\[
\frac14\,(2)(1)(5)=\frac52,
\]

not `25/2`. The same value follows from the displayed nonzero eigenvalues:

\[
\frac12\cdot2\cdot\frac52=\frac52.
\]

Since this connected Laplacian has `r+s=4` vertices, Kirchhoff's identity gives

\[
[t]\det(tI+H_{3,6})=\det' H_{3,6}=4\kappa_{3,6},
\]

so the displayed data imply `\kappa_{3,6}=5/8`. That is exactly the value stated in `PC-129`, which records `\kappa_{3,6}=5/8` and `R_{3,6}^2\kappa_{3,6}=10`. Thus the sentence claiming coefficient `25/2 = 4(25/8)` does not recover `PC-129`; it contradicts both the current calculation and the dependency it cites.

The main integrality theorem is not challenged by this arithmetic slip: with the correct coefficient `5/2`, multiplication by `R^2=16` still yields an integer coefficient. Please correct the `(3,6)` coefficient/cofactor cross-check to `5/2=4(5/8)` and keep the exact-control section consistent with `PC-129`.
