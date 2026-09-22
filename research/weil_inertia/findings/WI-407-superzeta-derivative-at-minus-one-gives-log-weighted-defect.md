# WI-407 — the superzeta derivative at minus one gives a positive log-weighted local defect, but a finite budget cannot force RH

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + BOOTSTRAP-INTERFACE`.

**Parent findings:** [WI-405](./WI-405-signed-widder-mellin-averages-collapse-to-superzeta-and-require-renormalization.md), [WI-406](./WI-406-canonical-superzeta-continuation-at-critical-widder-weight-is-fixed.md).

## Claim

WI-405 showed that the signed Widder Mellin family becomes Voros's second-kind superzeta, and that the critical Mellin weight corresponds to `sigma=-1`. WI-406 then showed that the raw analytically continued value at `sigma=-1` is a fixed explicit scalar, so the canonical continuation of the actual zero superzeta cannot itself be read as positive off-critical mass. The first derivative in the superzeta exponent behaves differently at the **finite-pair** level.

For a same-ordinate functional-equation pair in the upper half-plane,

\[
\rho_\pm=\frac12\pm d+i\gamma,
\qquad d>0,
\]

set

\[
\tau_\pm=\gamma\mp id,
\qquad
w_\pm=\tau_\pm^2.
\]

The second-kind superzeta summand is `w^{-sigma}`, so

\[
\frac{\partial}{\partial\sigma}w^{-\sigma}
=-(\Log w)w^{-\sigma}.
\]

At `sigma=-1`, compare the actual pair with the fictitious pair obtained by projecting both zeros to the critical line at the same ordinate. The exact actual-minus-criticalized derivative defect is

\[
\boxed{
\Delta_1(\gamma,d)
:=
2\gamma^2\log(\gamma^2)
-
\left[w_+\Log w_+ + w_-\Log w_-\right].
}
\tag{1}
\]

It has the closed form

\[
\boxed{
\Delta_1(\gamma,d)
=
2\gamma^2\log(\gamma^2)
-2(\gamma^2-d^2)\log(\gamma^2+d^2)
+8\gamma d\arctan\!\frac d\gamma.
}
\tag{2}
\]

Writing `x=d/gamma`,

\[
\boxed{
\Delta_1(\gamma,d)
=
2d^2\log(\gamma^2)+\gamma^2 h(x),
}
\tag{3}
\]

where

\[
h(x)=-2(1-x^2)\log(1+x^2)+8x\arctan x.
\tag{4}
\]

For `x>0`,

\[
h'(x)=4x\log(1+x^2)+4x+8\arctan x>0,
\qquad h(0)=0.
\tag{5}
\]

Hence every high off-line pair pays a strictly positive logarithmically amplified charge; in particular, for `gamma>1`,

\[
\boxed{
\Delta_1(\gamma,d)>2d^2\log(\gamma^2)=4d^2\log\gamma.
}
\tag{6}
\]

Moreover,

\[
h(x)=6x^2+\frac13x^4-\frac1{15}x^6+O(x^8),
\]

so for fixed `d` and `gamma -> infinity`,

\[
\boxed{
\Delta_1(\gamma,d)
=4d^2\log\gamma+6d^2+O\!\left(\frac{d^4}{\gamma^2}\right).
}
\tag{7}
\]

Thus differentiating in the superzeta exponent upgrades the WI-405 finite-pair `d^2` tariff to a `d^2 log gamma` tariff. This is a genuine structural gain, but it still does **not** globalize automatically. If a source-exact matched renormalization preserved the finite-cutoff derivative difference and produced only a finite total budget, it would imply

\[
\boxed{
\sum_{\text{off-line pairs}} d_\rho^2\log\gamma_\rho<\infty,
}
\tag{8}
\]

up to irrelevant finitely many low zeros. That conclusion is stronger than the unweighted square-depth summability suggested by the raw `sigma=-1` comparison, but it still cannot by itself prove RH: finitely many off-line zeros have finite cost, and infinitely many zeros with sufficiently rapidly shrinking horizontal depths can also satisfy (8).

Therefore a derivative renormalization is useful only if its source side gives more than mere finiteness — for example an exactly zero defect budget, a tail budget tending to zero, or another coercive statement incompatible with even one positive local charge. No global matched renormalization, improved simple-critical-zero proportion, or proof of RH is claimed here.

## 1. Exact finite-pair derivative charge

For the pair above, write

\[
a=\gamma^2-d^2,
\qquad
b=2\gamma d,
\qquad
\theta=\arctan(d/\gamma).
\]

Then

\[
w_+=a-ib,
\qquad
w_-=a+ib.
\]

In the zeta application `gamma>d>0`, so the principal logarithm is branch-safe and

\[
\Log w_+=\log(\gamma^2+d^2)-2i\theta,
\qquad
\Log w_-=\log(\gamma^2+d^2)+2i\theta.
\tag{9}
\]

Consequently

\[
\begin{aligned}
w_+\Log w_+ + w_-\Log w_-
&=2\Re\!\left[(a-ib)\left(\log(\gamma^2+d^2)-2i\theta\right)\right]\\
&=2a\log(\gamma^2+d^2)-4b\theta\\
&=2(\gamma^2-d^2)\log(\gamma^2+d^2)
-8\gamma d\arctan(d/\gamma).
\end{aligned}
\tag{10}
\]

Substituting (10) into (1) proves (2).

The sign convention in (1) is the natural one for the superzeta derivative. At `sigma=-1`,

\[
\mathcal Z'( -1\mid0)
=-\sum_\rho w_\rho\Log w_\rho
\]

formally, whereas the criticalized pair contributes `-2 gamma^2 log(gamma^2)`. Therefore actual derivative minus criticalized derivative is exactly `Delta_1` for each finite pair.

## 2. Positivity and logarithmic amplification

Put `x=d/gamma`. Expanding (2) only algebraically gives (3)--(4). Differentiation gives

\[
\begin{aligned}
h'(x)
&=4x\log(1+x^2)
-\frac{4x(1-x^2)}{1+x^2}
+8\arctan x+\frac{8x}{1+x^2}\\
&=4x\log(1+x^2)+4x+8\arctan x.
\end{aligned}
\tag{11}
\]

Every term in the last expression is positive for `x>0`, while `h(0)=0`. Hence `h(x)>0` and (6) follows whenever `gamma>1`.

The Taylor series at zero is

\[
-2(1-x^2)\log(1+x^2)+8x\arctan x
=6x^2+\frac13x^4-\frac1{15}x^6+O(x^8),
\tag{12}
\]

which proves (7). In particular, fixed horizontal depth is not washed out at large height: the derivative charge grows like `4 d^2 log gamma`.

This should be contrasted with the absolutely convergent raw superzeta regime of WI-405, where the fixed-depth signal decays faster than `gamma^-3`. The derivative at the analytically continued critical exponent recovers and amplifies the horizontal signal, but only after leaving the raw absolutely convergent zero sum.

## 3. What a matched derivative renormalization would imply

For a finite height cutoff containing complete functional-equation pairs, define the actual and same-ordinate criticalized derivative sums by

\[
D_{\rm act}(H)
=-\sum_{\gamma\le H}w_\rho\Log w_\rho,
\qquad
D_{\rm crit}(H)
=-\sum_{\gamma\le H}\gamma_\rho^2\log(\gamma_\rho^2),
\tag{13}
\]

with the criticalized term repeated with the same multiplicity as the actual upper-half-plane zero. Critical-line zeros contribute no horizontal pair defect, while an off-line pair contributes exactly (1). Thus, at every finite cutoff,

\[
D_{\rm act}(H)-D_{\rm crit}(H)
=
\sum_{\substack{\text{off-line pairs}\\\gamma\le H}}
\Delta_1(\gamma,d),
\tag{14}
\]

counting multiplicity.

Both sums in (13) diverge. Suppose, conditionally, that one can derive from the explicit formula or another source-exact identity a **matched** counterterm `C(H)` for which the two finite parts

\[
D_{\rm act}(H)-C(H),
\qquad
D_{\rm crit}(H)-C(H)
\tag{15}
\]

have compatible finite limits, with no extra horizontal-displacement term inserted by the renormalization. Then (14) survives the limit. Because all sufficiently high summands are positive and obey (6), a finite resulting defect implies (8).

The conclusion is conditional on the matched subtraction. Voros's meromorphic continuation of the actual superzeta supplies a canonical value for the actual spectral object, but it does not independently define the fictitious criticalized baseline or prove that a common counterterm cancels both sides. This is exactly the distinction already isolated in WI-406, now applied to the exponent derivative.

## 4. Finite derivative budget is still insufficient for RH

The logarithmic factor is a real strengthening, but it does not produce a defect-to-zero theorem by itself. If there are only finitely many off-line pairs, then the right side of (8) is finite regardless of their depths. More generally, an infinite sequence can satisfy (8) whenever its horizontal depths shrink fast enough; for example a hypothetical sequence with

\[
d_n^2\log\gamma_n\le 2^{-n}
\]

has finite derivative cost.

Therefore the implication

\[
\text{matched derivative finite part exists and is finite}
\Longrightarrow
\sum d_\rho^2\log\gamma_\rho<\infty
\]

cannot alone exclude even one off-line zero. This closes the weak version of the derivative-renormalization route: **finiteness is not enough**.

A successful bootstrap would need a stronger source-side conclusion. Three falsifiable possibilities remain:

1. the matched derivative defect is forced to be exactly zero;
2. a source-exact tail identity forces the remaining derivative budget above height `H` to tend to zero in a way incompatible with any positive local charge;
3. a second independent invariant converts log-weighted square-depth summability into a contradiction for every off-line pair.

Conversely, if every admissible matched subtraction necessarily acquires an uncontrolled horizontal counterterm of order `d^2 log gamma`, then even this strengthened route closes at the renormalization gate.

## 5. Prior-art audit and novelty boundary

The primary classical framework is André Voros's superzeta theory:

- André Voros, *Zeta functions over zeros of Zeta functions and an exponential-asymptotic view of the Riemann Hypothesis*, arXiv:`1403.4558`, version 2 (2014): <https://arxiv.org/abs/1403.4558>.
- André Voros, *Zeta functions for the Riemann zeros*, *Annales de l'Institut Fourier* **53** (2003), 665--699, DOI `10.5802/aif.1955`: <https://www.numdam.org/articles/10.5802/aif.1955/>.
- André Voros, *Erratum - Zeta functions for the Riemann zeros*, *Annales de l'Institut Fourier* **54** (2004), 1139, DOI `10.5802/aif.2046`: <https://www.numdam.org/articles/10.5802/aif.2046/>.

Voros supplies the second-kind superzeta, its meromorphic continuation, and the zeta-regularization setting. The differentiation identity `partial_sigma w^{-sigma}=-(Log w)w^{-sigma}` is elementary. WI-406 already records that the raw negative-integer value at `sigma=-1` is classical explicit data rather than a positive defect mass.

A targeted prior-art search around second-kind superzeta derivatives, derivatives at negative integers, and Riemann-zero zeta regularization did not locate the specific finite same-ordinate comparison (1)--(7). That negative search is **not** used as a priority claim. The novelty boundary here is deliberately narrow:

- `CLASSICAL-IDENTITY`: the superzeta framework, meromorphic continuation, and exponent differentiation are classical;
- `LITERATURE+DERIVED`: `sigma=-1` is the exact critical Widder exponent identified by WI-405--WI-406;
- `EXACT-DERIVED`: equations (1)--(7) and the finite-cutoff identity (14) are direct algebraic consequences;
- `BOOTSTRAP-INTERFACE`: a matched derivative finite part would force log-weighted square-depth summability;
- `DECISIVE-NEGATIVE`: mere finiteness of that stronger budget still cannot imply RH.

No priority claim is made for superzeta derivatives or zeta regularization.

## Consequence

Differentiating the critical second-kind superzeta exponent does not solve the renormalization problem from WI-406, but it changes what would be gained if that problem were solved. A defect-preserving matched finite part at `sigma=-1` would no longer see only `d^2`; it would see a strictly positive charge asymptotic to

\[
4d^2\log\gamma.
\]

This is the first exact logarithmic height amplification in the signed Widder/superzeta branch. It remains insufficient as a finite scalar budget, so the next serious target is not simply to prove that `mathcal Z'(-1|0)` exists — meromorphic continuation already gives an actual-spectrum value — but to derive a **source-compatible matched difference identity** whose defect side is either forced to vanish or whose tail budget contracts to zero. That is the point at which the derivative mechanism could become a genuine defect-to-zero bootstrap rather than only a stronger summability statement.