# AF-431 — Constant rational supercritical sources hit the first saddle window

## Status

`EXACT-DERIVED` · `LITERATURE-AUDITED` · `ARITHMETIC-FIDELITY` · `SUPERCRITICAL` · `SOURCE-LATTICE` · `SHRINKING-TARGET` · `POSITIVE-REALIZABILITY` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-429--AF-430 in the supercritical full-column branch. Fix `a>0` and a rational derivative-density

\[
q=\frac uv>2,
\qquad (u,v)=1,
\qquad
\alpha:=1-\frac2q=\frac{q-2}{q}\in(0,1).
\]

On the exact source lattice

\[
n=vk,
\qquad
s=uk=qn,
\]

put

\[
R(n)=a^{1/q}n^\alpha.
\]

Let `tau(n)` denote the real zero of AF-429's exact adjacent full-column log-ratio after extending `n` to a real variable while keeping the ratio `s/n=q` fixed. Then for all sufficiently large real `n`, `tau(n)` is `C^1`, strictly increasing, and

\[
\boxed{
\tau(n)\sim R(n),
\qquad
\tau'(n)
=\alpha\frac{R(n)}{n}(1+o(1)).
}
\tag{1}
\]

Consequently, on any fixed arithmetic progression of admissible source indices with step `h`,

\[
\boxed{
\tau(n+h)-\tau(n)
=h\alpha\frac{R(n)}{n}(1+o(1)).
}
\tag{2}
\]

Since `tau(n)->infinity` while the right-hand side tends to zero, the sampled saddle crosses the integer lattice with exactly the same scale as AF-429's first comparability window. In particular, along `n=vk`,

\[
\boxed{
\operatorname{dist}(\tau_n,\mathbb Z)
\le
(v\alpha+o(1))\frac{R_n}{n}
}
\tag{3}
\]

for infinitely many admissible source indices. More strongly, every sufficiently large integer level crossed by the monotone sampled saddle supplies such an index.

For the sign-alternating branch used by AF-429--AF-430, require odd `n`. If the reduced denominator `v` is odd, use

\[
n_k=v(2k+1),
\qquad
s_k=u(2k+1).
\]

Then consecutive admissible odd indices are separated by `2v`, and

\[
\boxed{
\operatorname{dist}(\tau_{n_k},\mathbb Z)
\le
(2v\alpha+o(1))\frac{R_{n_k}}{n_k}
}
\tag{4}
\]

for infinitely many `k`.

Thus AF-429's `O(R_n/n)` integer window is **not a universal source-lattice obstruction**. Every fixed rational supercritical density has an exact source progression on which the first window is reached automatically; when the denominator is odd, this remains true on an odd-`n` progression where adjacent rectangle/packet signs alternate. Taking the nearest integer `r_n` at those crossings meets AF-430's hypothesis, so the two complete residual packets are order-one comparable infinitely often inside the exceptional-`1` sector.

The theorem does **not** reach AF-430's finer packet-corrected center. The inter-index source spacing in `(2)` is `Theta(R_n/n)`, whereas the first packet correction is only `Theta(R_n/n^2)`. Hence the rational constant-density crossing mechanism closes the first-scale realizability question positively but leaves the factor-`n` finer balance as a genuine arithmetic target.

## 1. Exact continuous adjacent-ratio equation

For fixed real `q>2`, set `s=qn` and

\[
R(n)=a^{1/q}n^{1-2/q}.
\]

AF-429's exact adjacent full-column ratio can be written for real `n,r` in the large positive region as

\[
\begin{aligned}
\Phi(n,r)
&:=\log F_{n,r}\\
&=qn\log\!\left(\frac{R(n)(n+r)}{nr}\right)+E(n,r),
\end{aligned}
\tag{5}
\]

where

\[
E(n,r)
=-\log\frac{n+r}{r}
+\log\frac{\zeta(2(n+r))}{\zeta(2r)}
+2\log\frac{2(n+r)-1}{2r-1}.
\tag{6}
\]

Indeed `R(n)^q=a n^{q-2}`, so the first factor in the original ratio obeys

\[
\left(\frac{a}{n^2}\right)^n
=\left(\frac{R(n)}n\right)^{qn}.
\]

The remaining `-1` in the exponent `s-1=qn-1` is exactly the first term of `E`.

AF-429's localization and strict decrease in `r` use estimates uniform in the same moving region `r\asymp R(n)` and therefore apply to the real extension `(5)`: for all sufficiently large `n`, there is a unique zero `tau(n)` with

\[
\tau(n)\sim R(n).
\tag{7}
\]

Moreover `\partial_r\Phi` is nonzero there, so the implicit-function theorem makes `tau` continuously differentiable.

## 2. The saddle moves by one AF-429 window per unit source scale

Write

\[
A(n,r)=\log\!\left(\frac{R(n)(n+r)}{nr}\right).
\]

Since `R'(n)/R(n)=alpha/n`, differentiation at fixed `r` gives

\[
\partial_n A
=\frac\alpha n+\frac1{n+r}-\frac1n
=\frac\alpha n-\frac{r}{n(n+r)}.
\tag{8}
\]

Hence

\[
\partial_n(qnA)
=qA+(q-2)-q\frac{r}{n+r}.
\tag{9}
\]

At the root `r=tau(n)`, equation `(5)` gives `qnA=-E`. Because `r\sim R=o(n)`,

\[
E(n,r)=O(\log(n/R)),
\qquad
\partial_nE(n,r)=O(n^{-1}),
\tag{10}
\]

while `r/(n+r)=o(1)`. Therefore

\[
\boxed{
\partial_n\Phi(n,\tau(n))
=q-2+o(1).
}
\tag{11}
\]

For the `r` derivative,

\[
\partial_r(qnA)
=qn\left(\frac1{n+r}-\frac1r\right)
=-\frac{qn^2}{r(n+r)}.
\]

The derivative of `E` is only `O(1/r)` in the same region; the logarithmic derivative of zeta is exponentially smaller as `r->infinity`. Thus

\[
\boxed{
\partial_r\Phi(n,\tau(n))
=-q\frac{n}{R(n)}(1+o(1)).
}
\tag{12}
\]

Implicit differentiation of `Phi(n,tau(n))=0` now yields

\[
\tau'(n)
=-\frac{\partial_n\Phi}{\partial_r\Phi}
=\frac{q-2}{q}\frac{R(n)}n(1+o(1)),
\]

which is `(1)`. Because the coefficient is positive, `tau` is eventually strictly increasing. Since `R(n)->infinity`, `(7)` gives `tau(n)->infinity`; because `R(n)/n=a^{1/q}n^{-2/q}->0`, the derivative tends to zero.

For fixed `h>0`, the mean-value theorem and regular variation of `R` over bounded increments give `(2)`.

## 3. A monotone crossing lemma turns source spacing into integer hits

The remaining argument is elementary but is the exact arithmetic-fidelity point. Let `x_k` be any eventually strictly increasing sequence with

\[
x_k\to\infty,
\qquad
x_{k+1}-x_k\to0.
\]

For each sufficiently large integer `M`, choose the first `k=k(M)` with `x_k>=M`. Then

\[
x_{k-1}<M\le x_k,
\]

so

\[
\operatorname{dist}(x_k,\mathbb Z)
\le x_k-M
\le x_k-x_{k-1}.
\tag{13}
\]

Apply `(13)` to the sampled saddle `x_k=tau(vk)`. Equation `(2)` with `h=v` gives `(3)`. If `v` is odd, sampling only `n_k=v(2k+1)` keeps every `n_k` odd, and `(2)` with `h=2v` gives `(4)`.

This also isolates a general sufficient condition for future source audits: **if an allowed source subsequence makes the real saddle eventually monotone and divergent with inter-index spacing `O(R_n/n)`, then AF-429's first integer window is automatic.** A genuine first-scale obstruction must therefore come from coarser source spacing, nonmonotone/source-induced jumps, or an additional compatibility condition not present in the bare integer lattice.

## 4. Why the finer AF-430 target does not follow

At a first-window hit choose `r_n` to be the integer level crossed by `tau_n`. Equations `(3)` or `(4)` give

\[
|r_n-\tau_n|=O(R_n/n),
\]

so AF-430 applies and makes the adjacent complete residual packets comparable.

But AF-430's first inverse-`n` balance requires the refined center

\[
\widehat\tau_n-\tau_n
=a e^q\frac{R_n}{n^2}(1+o(1)).
\tag{14}
\]

The allowed-source saddle increment from `(2)` is larger by a factor asymptotic to `n`:

\[
\frac{R_n/n}{R_n/n^2}=n.
\]

The crossing lemma therefore gives no control at the corrected `R_n/n^2` scale and does not even force `o(R_n/n)`. That distinction is essential: AF-429's first window is a coarse comparability gate, while cancellation of exponentially large neighboring packets can demand much finer alignment.

## Prior-art and novelty audit

The modulo-one behavior of sublinear power sequences belongs to classical uniform-distribution theory. A modern primary source, Technau and Yesha, *On the correlations of `n^alpha` mod 1*, Journal of the European Mathematical Society 25 (2023), 4123--4154, DOI `10.4171/JEMS/1281`, recalls the Fejer--Csillag theorem that `{n^beta}` is uniformly distributed modulo one for positive nonintegral `beta` and studies much finer correlation statistics. This places power-law fractional-part questions firmly in established prior art.

The present result does **not** use uniform distribution or any local-statistics theorem. Its `O(R_n/n)` hit follows from the much weaker deterministic fact that an increasing divergent real sequence whose increments tend to zero must cross every sufficiently large integer within one increment. The implicit differentiation of a moving saddle and this crossing lemma are elementary classical tools. A targeted search did not locate the exact Euler-log derivative-Hankel saddle specialization `(1)`--`(4)`, but no novelty claim is made for the underlying asymptotic, implicit-function, regular-variation, or modulo-one principles.

The durable Mathia content is the source-interface consequence: after AF-429 and AF-430 converted packet comparability into a shrinking integer target, the exact constant-rational source lattice has mesh **of the same asymptotic order as that target**. Therefore this source class cannot be excluded at the first lattice gate.

## Boundaries and falsification checks

- The positive realization theorem is for fixed rational `q=u/v>2` sampled on indices where `s=qn` is exactly integral. It does not prove the same statement for an arbitrary prescribed sequence `q_n->sigma`.
- Exact constant density and odd `n` coexist on an infinite progression precisely in the stated construction when the reduced denominator `v` is odd. If `v` is even, the exact constant-density progression contains only even `n`; a nearby varying-depth odd source needs a separate audit.
- The result proves only an `O(R_n/n)` hit. It does not imply `o(R_n/n)`, `F_{n,r}->1`, the packet-corrected `R_n/n^2` alignment, or cancellation to the precision required by the exponentially large saddle.
- AF-430 still concerns the exceptional-`1` Cauchy--Binet sector. Omitted-`1` and singular-block determinant sectors remain uncontrolled here.
- The argument assumes fixed finite `q>2` and fixed `a>0`; it does not cover `q_n->infinity` or an amplitude varying with `n`.
- The theorem supplies no rational-prime discriminator and has no implication for zeta zeros or RH.

## Consequence for the research line

AF-429's first supercritical shrinking window is now known to be **source-sensitive rather than intrinsically prohibitive**. In the exact rational constant-density class, the moving saddle itself advances through the integer lattice in steps of order `R_n/n`, so infinitely many first-window hits are forced; with odd denominator the same is true on the odd-`n` sign-alternating branch.

The supercritical frontier should therefore split cleanly. For a distinguished source sequence not covered by this class, first determine whether its allowed saddle samples satisfy the same monotone `O(R_n/n)` mesh criterion or instead introduce genuinely coarser jumps. For constant rational sources that already pass, do not spend further work reproving first-window membership: move directly to the finer packet-corrected `R_n/n^2` target and to the omitted determinant sectors. The factor-`n` separation between source-step scale and refined balance scale is now the next potentially arithmetic obstruction.