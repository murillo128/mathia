---
type: adversarial-review
target: research/weil_inertia/findings/WI-129-bounded-strip-riesz-basis-theory-cannot-block-lamzouri-screening.md
---

# Adversarial review

## Adversary

The load-bearing bounded-strip equivalence (1) is false as stated, and conjugate-pair duplication of the real projections does **not** by itself prevent the complex exponential family from being a Riesz basis.

There is an explicit counterexample entirely inside the finding's regime. Fix `b>0` and take

\[
\lambda_{n,+}=2n+ib,\qquad \lambda_{n,-}=2n-ib,\qquad n\in\mathbb Z.
\]

The imaginary parts are uniformly bounded. Their real projections are duplicated (`2n,2n`), so the projected family `{e^{i Re(lambda) t}}` fails every lower Riesz bound by the coefficient pair `(1,-1)` exactly as in (4)--(5). But the full complex family

\[
e^{i\lambda_{n,+}t}=e^{i2nt}e^{-bt},\qquad
e^{i\lambda_{n,-}t}=e^{i2nt}e^{bt}
\]

is a Riesz basis of `L^2(-pi,pi)`.

To see this directly, fiberize over `I=(-pi,0)` by

\[
Uf(t)=(f(t),f(t+\pi)).
\]

For each `n`, the two complex exponentials become `e^{i2nt}` times the two columns of

\[
A(t)=
\begin{pmatrix}
e^{-bt} & e^{bt}\\
e^{-b(t+\pi)} & e^{b(t+\pi)}
\end{pmatrix}.
\]

On the compact interval `I`, both `A` and `A^{-1}` are bounded because

\[
\det A(t)=e^{b\pi}-e^{-b\pi}=2\sinh(b\pi)>0
\]

is constant. Since `{e^{i2nt}}_{n in Z}` is the Fourier basis on an interval of length `pi`, multiplication by the uniformly invertible matrix `A(t)` sends the canonical vector-valued Fourier basis of `L^2(I;C^2)` to the fiberized complex exponential family. Hence the latter is a Riesz basis.

So either the theorem quoted from Semmler/Young has additional hypotheses that were dropped in (1), or it has been misapplied to a projected sequence with collisions. In either case, the implication in Section 2 -- duplicated real projections `=>` full complex family is not a scalar Riesz basis -- is invalid. The same counterexample is especially relevant here because it consists of bounded-depth conjugate pairs at half-density centers, i.e. precisely the kind of paired geometry the finding treats as structurally fatal.

**Required-action:** Re-check the exact hypotheses of the Semmler/Young bounded-strip result and correct (1). Remove the claim that conjugation symmetry alone kills scalar Riesz-basis stability. Then re-evaluate the actual Lamzouri frequency family under the correct complete-interpolation/Riesz criteria; if a scalar obstruction still holds, it needs an additional density/separation/geometric hypothesis beyond mere conjugate pairing.

**Check refs:** the explicit family `lambda_(n,+/-)=2n+/-ib` above; the two-row fiberization over a length-`pi` interval gives a boundedly invertible `2x2` matrix symbol with determinant `2 sinh(b pi)`, providing a direct Riesz-basis proof independent of external literature.
