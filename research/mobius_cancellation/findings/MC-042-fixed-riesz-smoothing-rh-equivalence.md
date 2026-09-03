# MC-042 — Every fixed-order Möbius Riesz smoothing retains the full RH zero-free burden

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

For a fixed real parameter `tau >= 0`, define the normalized Möbius Riesz mean

\[
M_\tau(x)
=
\frac{1}{\Gamma(\tau+1)}
\sum_{n\le x}\mu(n)\left(1-\frac{n}{x}\right)^\tau,
\qquad x\ge1.
\tag{1}
\]

Then, for every fixed `tau >= 0`,

\[
\boxed{
\mathrm{RH}
\iff
M_\tau(x)=O_{\tau,\varepsilon}(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
}
\tag{2}
\]

The exact Mellin transform behind this equivalence is

\[
\boxed{
\int_1^\infty M_\tau(x)x^{-s-1}\,dx
=
\frac{\Gamma(s)}{\Gamma(s+\tau+1)}\frac1{\zeta(s)},
\qquad \Re(s)>1.
}
\tag{3}
\]

For fixed `tau >= 0`, the Gamma quotient in `(3)` is holomorphic and nonzero throughout `Re(s)>1/2`. Thus fixed-order Riesz smoothing does not mask any zeta zero in the critical half-plane: it only multiplies `1/zeta(s)` by a fixed zero-free analytic factor.

Consequently the active Tauberian escape after `MC-041` cannot be obtained merely by replacing the ordinary Mertens sum, the order-one Riesz mode of `MC-019`, or another coarse observable by a **fixed higher-order** Riesz/Cesàro smoothing and then proving the same square-root exponent for that smoothed quantity. At the critical exponent every fixed order remains in the same RH information class.

This does not rule out scale-dependent smoothing `tau=tau(x)`, nonlinear multiscale carriers, or an independently proved quantitative inverse theorem. It isolates why those would be genuine carrier changes whereas a finite fixed-order smoothing hierarchy is not.

## 1. Exact Mellin factorization

For `Re(s)>1`, absolute convergence permits interchange of the sum and integral in `(1)`. For each `n`, substitute `u=1-n/x`:

\[
\begin{aligned}
\frac1{\Gamma(\tau+1)}
\int_n^\infty
\left(1-\frac nx\right)^\tau x^{-s-1}\,dx
&=
\frac{n^{-s}}{\Gamma(\tau+1)}
\int_0^1 u^\tau(1-u)^{s-1}\,du \\
&=
 n^{-s}\frac{\Gamma(s)}{\Gamma(s+\tau+1)}.
\end{aligned}
\tag{4}
\]

Summing `(4)` against `mu(n)` gives `(3)` because

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}
\qquad (\Re(s)>1).
\tag{5}
\]

No zero information has been used in deriving `(3)`; it is an identity in the half-plane of absolute convergence.

## 2. A critical Riesz bound forces RH

Assume that for the fixed `tau` and every `epsilon>0`,

\[
M_\tau(x)=O_{\tau,\varepsilon}(x^{1/2+\varepsilon}).
\tag{6}
\]

On every compact subset of `Re(s)>1/2`, choose `epsilon` smaller than the compact set's distance from the critical line. Then the integral

\[
F_\tau(s)=\int_1^\infty M_\tau(x)x^{-s-1}\,dx
\tag{7}
\]

converges absolutely and locally uniformly, hence defines a holomorphic function throughout `Re(s)>1/2`.

For fixed `tau>=0`, both `Gamma(s)` and `Gamma(s+tau+1)` are finite and nonzero in this half-plane. Therefore

\[
G_\tau(s)=\frac{\Gamma(s+\tau+1)}{\Gamma(s)}F_\tau(s)
\tag{8}
\]

is holomorphic on `Re(s)>1/2`. On `Re(s)>1`, equations `(3)` and `(8)` give

\[
G_\tau(s)=\frac1{\zeta(s)}.
\tag{9}
\]

Thus `(8)` supplies a holomorphic continuation of the reciprocal zeta function to the whole half-plane `Re(s)>1/2`. The zeta function therefore has no nontrivial zero there. The functional equation and conjugation symmetry then place every nontrivial zero on `Re(s)=1/2`, proving RH.

The important structural point is the **nonmasking** property: unlike a transform whose multiplier could vanish exactly where `zeta` vanishes, the fixed Gamma quotient cannot cancel an off-critical zero divisor.

## 3. RH gives the fixed-order Riesz bound

For `tau=0`, `(1)` is simply the ordinary Mertens function, so the implication is the classical Mertens criterion.

Let `tau>0`. Write

\[
M(u)=\sum_{n\le u}\mu(n).
\]

Stieltjes summation by parts applied to `(1)` gives the exact identity

\[
M_\tau(x)
=
\frac{\tau}{\Gamma(\tau+1)x}
\int_1^x
M(u)\left(1-\frac ux\right)^{\tau-1}\,du.
\tag{10}
\]

Under RH, the classical criterion gives, for every `delta>0`,

\[
M(u)=O_\delta(u^{1/2+\delta}).
\tag{11}
\]

Insert `(11)` into `(10)` and set `v=u/x`. The remaining integral is bounded by the finite beta integral

\[
\int_0^1 v^{1/2+\delta}(1-v)^{\tau-1}\,dv<\infty
\qquad (\tau>0),
\tag{12}
\]

so

\[
M_\tau(x)=O_{\tau,\delta}(x^{1/2+\delta}).
\tag{13}
\]

This proves the reverse implication in `(2)` for every fixed positive order.

## 4. Prior art and novelty boundary

Generalized Riesz means of the Möbius function are established prior art. Shōta Inoue, *Riesz mean of Möbius function*, RIMS Kôkyûroku 2203 (2021), 31–40, defines the same family `(1)` for nonnegative real order, develops explicit formulas in terms of zeta zeros, and studies both fixed and growing smoothing order under RH. The bibliographic record is independently indexed by the National Diet Library as RIMS Kôkyûroku 2203 (November 2021), pages 31–40.

`MC-019` already used the order-one member of this family, where `x M_1(x)` is the first Möbius Riesz sum, and derived its RH equivalence by an elementary Mellin argument. The present result extends that information audit uniformly across **every fixed order** using the general beta-kernel factorization `(3)`.

No novelty is claimed for Riesz means, beta integrals, Mellin transforms, the reciprocal-zeta Dirichlet series, summation by parts, or the general principle that nonvanishing transform factors preserve zero divisors. A targeted search also finds a broader literature of reciprocal-zeta/Riesz criteria. The durable line-specific result is the closure of a current escape route: increasing the smoothing order while keeping it fixed does not change the critical zero-information class.

## 5. Consequences and falsification boundary

The finding is a negative classification, not a proof that smoothing is useless. A smoothed carrier can still be valuable if arithmetic input controls it in a way that is genuinely easier than controlling `M(x)` and a separate theorem transfers that control back to the ordinary scale.

What `(2)` rules out is the claim that the **endpoint itself** becomes softer merely because the Riesz order is increased to another fixed constant. A finite collection of fixed orders likewise cannot evade the obstruction: each member separately has a zero-free Mellin multiplier and its critical square-root bound already implies RH.

The first mathematically distinct escape begins when the smoothing law changes with scale. Inoue's work is relevant here because it also studies growing order `tau=tau(x)` under RH; once `tau` depends on `x`, there is no single fixed Mellin multiplier to which the argument above applies. That difference is only a research opening, not evidence of a converse or a useful Tauberian gain.

A viable continuation must therefore establish both sides of a new quantitative bridge: independently weaker arithmetic information must control a variable-order, nonlinear, or otherwise carrier-changing statistic, and an inverse/Tauberian estimate must recover polynomial ordinary cancellation without importing zero location. If the recovery step itself is equivalent to the fixed-order critical estimate, the route has merely moved the RH burden again.

## Consequence for the active transfer clue

The accepted mean-absolute/coarse-mode transfer clue had already narrowed after `MC-019` to producing the first Riesz coarse mode from independently weaker arithmetic information. This finding closes the obvious fixed-order smoothing relaxation of that target. Replacing the order-one mode by order `2`, order `3`, or any other fixed real order does not reduce the zero-free burden.

Accordingly, further work on that clue should treat **scale-dependent carrier change plus quantitative inverse transfer** as the live smoothing question, not another fixed-order Riesz hierarchy.