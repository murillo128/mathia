# WI-406 — canonical superzeta continuation at the critical Widder weight is fixed and cannot itself carry positive defect mass

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

**Parent finding:** [WI-405](./WI-405-signed-widder-mellin-averages-collapse-to-superzeta-and-require-renormalization.md).

## Claim

WI-405 identified an exact height-uniform finite-pair defect at the signed Widder Mellin weight `a=1`, equivalently at the second-kind superzeta exponent

\[
\sigma=-\frac{a+1}{2}=-1,
\]

but left open whether Voros's meromorphic continuation could provide a canonical global renormalization of the divergent zero sum. The classical special-value formula answers the naive version of that question decisively.

For Voros's second-kind superzeta

\[
\mathcal Z(\sigma\mid t)
=
\sum_{k\ge 1}(\tau_k^2+t^2)^{-\sigma},
\qquad \Re\sigma>\frac12,
\]

where the Riemann zeros are written as

\[
\rho=\frac12\pm i\tau_k,
\qquad \Re\tau_k>0,
\]

Voros proves meromorphic continuation in `sigma` and gives, for every integer `m>=1`, the explicit negative-integer value

\[
\boxed{
\mathcal Z(-m\mid t)
=
\left(t^2-\frac14\right)^m
-
2^{-2m-3}
\sum_{j=0}^m
{m\choose j}(-1)^jE_{2j}(2t)^{2(m-j)}.
}
\tag{1}
\]

At the critical Widder exponent `sigma=-1`, `m=1` and `E_2=-1`, so

\[
\boxed{
\mathcal Z(-1\mid t)
=
\frac78 t^2-\frac9{32},
\qquad
\mathcal Z(-1\mid0)=-\frac9{32}.
}
\tag{2}
\]

Thus the **canonical analytic-continuation value of the actual zero superzeta at exactly the WI-405 critical scale is a fixed explicit constant**. It is not a positive additive sum of horizontal off-critical defects. In particular, simply declaring the divergent critical signed Widder sum to equal Voros's continued value cannot turn the finite-pair `d^2` charge of WI-405 into a global defect-to-zero theorem.

This closes only the naive canonical-continuation route. A matched renormalization of the **difference** between the actual zero sum and a same-ordinate criticalized baseline could still retain horizontal defect, but that baseline is an additional object and Voros's continuation does not supply its required counterterm automatically.

No improved simple-critical-zero proportion and no proof of RH is claimed.

## 1. Exact identification with the WI-405 critical scale

WI-405 parametrizes an upper-half-plane zero by

\[
\rho=\frac12+\delta+i\gamma
=\frac12+i\tau,
\qquad
\tau=\gamma-i\delta,
\]

and writes

\[
w_\rho=(\gamma-i\delta)^2=\tau^2.
\tag{3}
\]

Its absolutely convergent signed Mellin family is a beta multiple of

\[
\mathcal Z(\sigma\mid0)=\sum_k\tau_k^{-2\sigma},
\tag{4}
\]

which is exactly Voros's second-kind superzeta at `t=0`. The height-uniform finite-pair charge found there occurs at `a=1`, hence at `sigma=-1`. Formally, this is the divergent sum of the `w_rho=\tau_k^2` themselves.

Voros's continuation is therefore not merely adjacent prior art: equation (2) evaluates the exact regularized scalar left open by WI-405.

## 2. Voros's negative-integer formula fixes the continuation value

Voros defines the second-kind family in the half-plane `Re sigma>1/2` and continues it meromorphically to the full `sigma`-plane. His Table 6 gives equation (1), with the negative-integer values explicitly computable from Euler numbers.

For `m=1`,

\[
\begin{aligned}
\mathcal Z(-1\mid t)
&=
\left(t^2-\frac14\right)
-
\frac1{32}
\left[(2t)^2-E_2\right]\\
&=
\left(t^2-\frac14\right)
-
\frac{4t^2+1}{32}\\
&=
\frac78t^2-\frac9{32},
\end{aligned}
\]

because `E_2=-1`. At `t=0` this gives `-9/32` exactly.

The point is structural, not the numerical value. The continuation has already absorbed the divergent high-zero asymptotics into its analytic prescription. At negative integers the result collapses to explicit polynomial/rational data; it is not a manifestly nonnegative statistic that grows with off-critical mass.

## 3. Why this does not globalize the finite-pair `d^2` tariff

Take a same-ordinate off-line pair in the upper half-plane,

\[
\rho_\pm=\frac12\pm d+i\gamma,
\qquad d>0.
\]

The corresponding Voros parameters are

\[
\tau_\pm=\gamma\mp id,
\qquad
w_\pm=\tau_\pm^2.
\]

For a finite pair,

\[
w_++w_-=2(\gamma^2-d^2),
\tag{5}
\]

whereas projecting both zeros to the critical line at the same ordinate gives `2 gamma^2`. Hence the finite comparison is exactly

\[
\boxed{
2\gamma^2-(w_++w_-)=2d^2.
}
\tag{6}
\]

Equation (6) is the local charge underlying WI-405. On a finite truncation it gives

\[
\sum_{\text{criticalized}}\gamma^2-
\sum_{\text{actual}}w
=
2\sum_{\text{off-line pairs}}d^2.
\tag{7}
\]

But both scalar sums in (7) diverge as the height cutoff tends to infinity. Voros canonically continues the **actual** superzeta and assigns its `sigma=-1` value `-9/32`. That operation alone gives no separately defined regularized value for the fictitious same-ordinate criticalized sequence, and therefore no theorem identifying a difference of two matched finite parts with the nonnegative right side of (7).

This distinction is essential. The conclusion is not that analytic continuation erases all zero information, nor that superzetas cannot participate in an RH criterion. Voros himself uses superzeta machinery in RH-sensitive asymptotic criteria. The narrower conclusion is:

\[
\boxed{
\text{the single canonical value }\mathcal Z(-1\mid0)=-9/32
\text{ cannot by itself be the desired positive off-line defect budget.}
}
\tag{8}
\]

Any successful use of (7) must control the **renormalized comparison**, not just the actual spectral sum.

## 4. The remaining renormalization problem is now sharply specified

The viable escape is a matched subtraction performed before, or compatibly with, the infinite-height limit. One would need a zeta-specific theorem defining a common counterterm `C(H)` such that the two limits

\[
\operatorname*{FP}_{H\to\infty}
\left(\sum_{\gamma\le H}w_\rho-C(H)\right),
\qquad
\operatorname*{FP}_{H\to\infty}
\left(\sum_{\gamma\le H}\gamma^2-C(H)\right)
\tag{9}
\]

exist in a compatible sense and their difference preserves the finite-truncation identity (7), ideally with no uncontrolled signed boundary term. Equivalently, one can seek an explicit-formula identity in which the common divergent baseline is cancelled **before** summation and the residual prime/gamma terms have a finite one-sided budget.

The obstruction is that the criticalized ordinates are not themselves the zero set of the original `Xi`; Voros's continuation is tied to the actual spectral sequence. Therefore the second finite part in (9), or any replacement for it, requires genuinely additional structure. It cannot be inferred merely by evaluating the already-continued actual superzeta at `sigma=-1`.

This yields a clean falsifiable fork:

- if a source-exact matched finite-part formula can be derived and the residual counterterm is independent of the horizontal displacements, then (7) can in principle globalize the WI-405 `d^2` tariff;
- if every admissible matched subtraction necessarily contains an uncontrolled horizontal-displacement term of the same order, this renormalized route also closes.

Parameter derivatives or noninteger combinations remain logically open as well, because the present barrier is specifically the negative-integer value of the raw second-kind superzeta.

## 5. Prior-art audit and novelty boundary

The primary source is:

- André Voros, *Zeta functions over zeros of Zeta functions and an exponential-asymptotic view of the Riemann Hypothesis*, arXiv:`1403.4558`, version 2 (2014): <https://arxiv.org/abs/1403.4558>. Section 2.2 defines the second-kind superzeta; Table 6 gives equation (1) and states that the negative-integer values are explicitly computable.

The earlier foundational source is:

- André Voros, *Zeta functions for the Riemann zeros*, Annales de l'Institut Fourier **53** (2003), 665--699, DOI `10.5802/aif.1955`: <https://www.numdam.org/articles/10.5802/aif.1955/>.
- André Voros, *Erratum - Zeta functions for the Riemann zeros*, Annales de l'Institut Fourier **54** (2004), 1139, DOI `10.5802/aif.2046`: <https://www.numdam.org/articles/10.5802/aif.2046/>.

A targeted audit around Voros superzetas, negative-integer special values, zeta regularization over Riemann zeros, and RH criteria found the special-value formula as established prior art but did not locate the specific proposal of using `mathcal Z(-1|0)` itself as a nonnegative horizontal-defect mass. That negative search is **not** used as a priority claim.

The novelty boundary is therefore strict:

- `CLASSICAL-IDENTITY`: equation (1), its meromorphic-continuation context, and the special value (2) are Voros prior art.
- `LITERATURE+DERIVED`: WI-405 identifies the signed Widder critical scale with `sigma=-1`; substituting that scale into Voros's formula is the bridge.
- `EXACT-DERIVED`: equations (5)--(7) give the finite-pair comparison algebraically.
- `DECISIVE-NEGATIVE`: canonical continuation of the actual superzeta alone cannot be promoted to the desired positive global defect budget.
- `PRIOR-ART-REDIRECT`: the next admissible target is a **matched renormalization/difference identity**, not another evaluation of the raw continued superzeta.

No priority claim is made for the superzeta identities or zeta regularization.

## Consequence

WI-405's open renormalization question is now narrower. The simplest interpretation

\[
\text{``regularize }\sum w_\rho\text{ by }\mathcal Z(-1\mid0)\text{ and read off off-line mass''}
\]

is impossible: the canonical value is already the explicit constant `-9/32`. The finite-pair geometry has not disappeared; it survives exactly in a **difference** between the actual and same-ordinate criticalized sums. What is missing is a canonical, source-compatible renormalization of that difference.

The next serious target is therefore a matched finite-part or explicit-formula subtraction that cancels the common cubic-in-height divergence while proving that the remainder preserves a one-sided quantity comparable to

\[
\sum d_\rho^2.
\]

That is a genuinely stronger requirement than meromorphic continuation of the actual superzeta and is the point at which new zeta-specific arithmetic or spectral information must enter.