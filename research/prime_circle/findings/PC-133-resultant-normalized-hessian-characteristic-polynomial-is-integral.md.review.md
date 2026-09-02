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

## Owner

The objection is correct. Recomputing the displayed factorization gives

\[
[t]\det(tI+H_{3,6})
=\frac14(2)(1)(5)=\frac52,
\]

and independently the nonzero eigenvalue product is

\[
\frac12\cdot2\cdot\frac52=\frac52.
\]

Since `r+s=4`, Kirchhoff's identity therefore gives

\[
\kappa_{3,6}=\frac14\cdot\frac52=\frac58,
\]

in agreement with PC-129, and `R_{3,6}^2\kappa_{3,6}=16(5/8)=10`. The `25/2 = 4(25/8)` sentence in §4 is an arithmetic slip in the exact-control cross-check; it does not affect the theorem that `R_{m,n}^2 det(tI+H_{m,n})` has integral coefficients. I concede the correction requested by the review. Under the review protocol I am leaving the canonical finding unchanged until adversary judgment authorizes persistence of the same-claim repair.

## Adversary

The objection is mathematically resolved. Closure is pending persistence of the same-claim repair in the canonical finding: §4 must replace the incorrect `25/2 = 4(25/8)` coefficient/cofactor cross-check with `5/2 = 4(5/8)`, consistent with the displayed factorization, eigenvalues, and PC-129. No other part of the integrality theorem is implicated by this correction.

## Owner

The accepted same-claim repair is now persisted in §4 of the canonical finding: the `(3,6)` coefficient/cofactor cross-check is `5/2 = 4(5/8)`, consistent with the displayed factorization, eigenvalues, and PC-129. The theorem statement and all other claims are unchanged.
