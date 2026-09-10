# AF-257 — Parity-restricted continued fractions exactly classify two-mode Li cancellation

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DIOPHANTINE-FIDELITY`, `PARITY-RESTRICTED`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-249 identifies the exact two-mode cancellation invariant

\[
\kappa_{1/2}(\alpha)
:=
\limsup_{n\to\infty}
\frac{-\log d_\alpha(n)}{n},
\qquad
 d_\alpha(n)=\operatorname{dist}\!\left(n\alpha,\mathbb Z+\frac12\right),
\tag{1}
\]

for irrational `alpha`, but only bounds it above by the unrestricted Sondow irrationality base. The parity restriction in `(1)` can in fact be resolved exactly by ordinary continued fractions.

Let

\[
\alpha=[a_0;a_1,a_2,\ldots],
\qquad \frac{p_j}{q_j}
\tag{2}
\]

be the simple continued-fraction convergents of `alpha`. Define

\[
L_{\mathrm{oe}}(\alpha)
:=
\limsup_{\substack{j\to\infty\\ q_j\ \mathrm{even}}}
\frac{\log q_{j+1}}{q_j},
\tag{3}
\]

with value `0` when only finitely many convergent denominators `q_j` are even. Then

\[
\boxed{
\kappa_{1/2}(\alpha)=2L_{\mathrm{oe}}(\alpha).
}
\tag{4}
\]

Equivalently,

\[
\boxed{
\kappa_{1/2}(\alpha)
=2\limsup_{\substack{j\to\infty\\ q_j\ \mathrm{even}}}
\frac{\log a_{j+1}}{q_j},
}
\tag{5}
\]

with the same convention.

Thus the half-integer cancellation channel does not see the full exponential rational-approximation profile of `alpha`. It sees exactly the exponential jumps in the continued fraction that occur **after an even-denominator convergent**. Since `p_j` and `q_j` are coprime, every such `q_j` automatically has odd `p_j`, exactly matching the odd-numerator/even-denominator rationals forced by half-integer cancellation.

For the two-mode signal

\[
F_{\alpha,m}(n)=-2m\cos(\pi n\alpha),
\tag{6}
\]

AF-249 therefore gives the exact worst-case root-rate over all unbounded retained sets:

\[
\boxed{
\inf_{S\subset\mathbb N\,\mathrm{unbounded}}
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=
\exp\!\left(-2L_{\mathrm{oe}}(\alpha)\right).
}
\tag{7}
\]

Now specialize to one hypothetical off-critical Keiper pair from AF-255,

\[
a_\rho=1-\frac1\rho=r_\rho e^{i\theta_\rho},
\qquad
q_\rho=r_\rho^{-1}>1,
\qquad
\alpha_\rho=\frac{\theta_\rho}{\pi}.
\tag{8}
\]

Assume `alpha_rho` is irrational and write `p_j/q_j` for its convergents. Then **every unbounded output sampling set** retains that pair as a strictly superunit off-RH root-rate witness if and only if

\[
\boxed{
2\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\frac{\log q_{j+1}}{q_j}
<\log q_\rho.
}
\tag{9}
\]

Full pair-rate fidelity for every unbounded sampling set is equivalent to the left side of `(9)` being zero. By AF-255, at large height the admissible detectability margin satisfies

\[
\log q_\rho
\asymp
\frac{\beta-1/2}{\gamma^2},
\tag{10}
\]

so the remaining source-specific requirement is now an exact parity-filtered continued-fraction growth condition rather than a generic statement about transcendence or irrationality.

## Why it matters

AF-249 deliberately stopped at a one-sided comparison with Sondow's unrestricted irrationality base because cosine cancellation only allows rational approximants of the form `p/(2n)` with `p` odd. Equation `(4)` closes that gap. At exponential scale, the parity-constrained problem becomes simpler than the full best-approximation problem: any approximation good enough to contribute a positive exponent automatically crosses Legendre's `1/(2q^2)` threshold and is therefore an ordinary principal convergent. The parity condition then reduces to selecting the principal convergents whose denominator is even.

This sharpens the source theorem needed after AF-255--AF-256. An unrestricted irrationality-base estimate can be unnecessarily strong because exponential approximation events attached only to odd-denominator convergents are invisible to the half-integer channel. The exact obstruction is the even-denominator subsequence in `(3)`. Conversely, once an even-denominator convergent is followed by an exponentially large next denominator, the corresponding Li mode has an exponentially small cancellation sample at index `n=q_j/2`.

The result also makes the conditioning scale explicit. To hide an off-critical pair from some sparse output set, the continued fraction of its normalized Keiper phase must contain even-denominator convergents followed by denominator growth at exponential rate at least `log(q_rho)/2`. To hide the pair from the **worst** unbounded sampling set, no more complicated sparse-set combinatorics are needed: the limsup of those parity-selected jumps is the complete invariant.

## Exact derivation

### 1. Half-integer cancellation is odd/even rational approximation

For each `n>=1`, choose an odd integer `p_n` attaining the nearest half-integer in `(1)`. Then

\[
d_\alpha(n)
=
\left|n\alpha-\frac{p_n}{2}\right|,
\qquad
\left|\alpha-\frac{p_n}{2n}\right|
=
\frac{d_\alpha(n)}{n}.
\tag{11}
\]

Put

\[
g_n=\gcd(p_n,2n).
\tag{12}
\]

Because `p_n` is odd, `g_n` is odd. Reducing the rational in `(11)` gives

\[
\frac{p_n}{2n}=\frac{r_n}{s_n},
\qquad
r_n=\frac{p_n}{g_n},
\qquad
s_n=\frac{2n}{g_n}.
\tag{13}
\]

Hence `s_n` remains even and `r_n` remains odd. Set

\[
n'_n=\frac{s_n}{2}=\frac{n}{g_n}.
\tag{14}
\]

Using the same reduced odd/even rational as an admissible half-integer target at `n'_n`,

\[
d_\alpha(n'_n)
\le
\frac{d_\alpha(n)}{g_n}.
\tag{15}
\]

Therefore, writing

\[
A(n)=\frac{-\log d_\alpha(n)}{n},
\tag{16}
\]

we have

\[
A(n'_n)
\ge
 g_n A(n)+\frac{g_n\log g_n}{n}
\ge A(n).
\tag{17}
\]

So reduction of a nonprimitive odd/even approximant cannot decrease its exponential cancellation exponent.

### 2. Every positive exponential event is eventually a principal convergent

Suppose along a sequence `n -> infinity` that

\[
A(n)\ge c>0.
\tag{18}
\]

Then `(11)` gives

\[
\left|\alpha-\frac{r_n}{s_n}\right|
=
\frac{d_\alpha(n)}{n}
\le
\frac{e^{-cn}}{n}.
\tag{19}
\]

Since `s_n<=2n`, for all sufficiently large `n`,

\[
\frac{e^{-cn}}{n}
<
\frac1{8n^2}
\le
\frac1{2s_n^2}.
\tag{20}
\]

Legendre's continued-fraction criterion now implies that the reduced rational `r_n/s_n` is a principal convergent of `alpha`. Its denominator `s_n` is even by `(13)`.

Combining this with `(17)` shows that every sequence contributing a positive value to the ambient limsup in `(1)` is dominated by a sequence of even-denominator principal convergents. The reverse inclusion is immediate because each even-denominator convergent itself supplies an allowed index `n=q_j/2`. Hence

\[
\kappa_{1/2}(\alpha)
=
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
A(q_j/2),
\tag{21}
\]

with value zero if the parity-selected convergent set is finite. This also covers the cases `\kappa_{1/2}=0` and `+infinity`: if the right side were positive while the left side were zero, or vice versa, the subset and reduction inequalities above would contradict each other.

### 3. Continued-fraction denominator growth gives the exact exponent

For a principal convergent `p_j/q_j`, the standard consecutive-denominator estimate gives

\[
\frac1{q_j(q_j+q_{j+1})}
<
\left|\alpha-\frac{p_j}{q_j}\right|
<
\frac1{q_j q_{j+1}}.
\tag{22}
\]

When `q_j` is even, `p_j` is odd, and with `n=q_j/2` we have exactly

\[
d_\alpha(q_j/2)
=
\frac{q_j}{2}
\left|\alpha-\frac{p_j}{q_j}\right|.
\tag{23}
\]

Thus

\[
\frac1{2(q_j+q_{j+1})}
<d_\alpha(q_j/2)
<\frac1{2q_{j+1}}.
\tag{24}
\]

Since `q_{j+1}>q_j`, the logarithms of the two bounds in `(24)` differ by at most a fixed constant. Dividing by `q_j/2` yields

\[
A(q_j/2)
=
\frac{2\log q_{j+1}}{q_j}
+O\!\left(\frac1{q_j}\right).
\tag{25}
\]

Taking the parity-restricted limsup in `(21)` proves `(4)`.

Finally,

\[
q_{j+1}=a_{j+1}q_j+q_{j-1},
\tag{26}
\]

with `0<q_{j-1}<q_j`, so

\[
\log q_{j+1}
=
\log a_{j+1}+\log q_j+O(1).
\tag{27}
\]

Because `\log q_j/q_j -> 0`, substituting `(27)` into `(4)` proves `(5)`.

### 4. Worst-case sparse sampling is attained by the limsup subsequence

AF-249 gives, for every unbounded `S`,

\[
\limsup_{\substack{n\to\infty\\n\in S}}
|F_{\alpha,m}(n)|^{1/n}
=
\exp\!\left(-\tau_\alpha(S)\right),
\tag{28}
\]

where

\[
\tau_\alpha(S)
=
\liminf_{\substack{n\to\infty\\n\in S}} A(n).
\tag{29}
\]

For every unbounded `S`, `\tau_\alpha(S)<=\limsup_n A(n)=\kappa_{1/2}(\alpha)`. Conversely, choose a subsequence on which `A(n)` converges to its limsup, in the extended-value sense. Along that set, `\tau_\alpha(S)=\kappa_{1/2}(\alpha)`. Equation `(7)` follows.

Multiplying by the Keiper radial factor `q_\rho^n` from AF-255 shifts every root rate by `log q_rho`. Consequently the worst unbounded sampling set has pair root rate

\[
\exp\!\left(\log q_\rho-2L_{\mathrm{oe}}(\alpha_\rho)\right),
\tag{30}
\]

which is strictly greater than one exactly under `(9)`.

## Prior-art audit

Jonathan Sondow, **“Irrationality Measures, Irrationality Bases, and a Theorem of Jarnik,”** arXiv:`math/0406300` (2004), develops the irrationality base and its continued-fraction characterization. In the present notation the unrestricted exponential scale is classically governed by

\[
\log\beta(\alpha)
=
\limsup_j\frac{\log q_{j+1}}{q_j}
=
\limsup_j\frac{\log a_{j+1}}{q_j}.
\tag{31}
\]

AF-249 already used this as a sufficient upper bound for the half-integer channel.

Dong Han Kim, Seul Bee Lee, and Lingmin Liao, **“Diophantine approximation by rational numbers of certain parity types,”** *Mathematika* 71 (2025), e12285, DOI `10.1112/mtk.12285`, develops best rational approximation under the three primitive parity classes, including odd-numerator/even-denominator approximants, and relates those classes to regular, intermediate, odd, and even continued-fraction algorithms. This is direct prior art for **parity-constrained best approximation** and prevents treating the parity decomposition itself as new.

The present theorem works at a narrower exponential scale. Kim--Lee--Liao show that parity-best approximants need not coincide simply with ordinary principal convergents at the usual Diophantine scale. Here Legendre's classical criterion implies that any parity approximant capable of producing a positive value of `(1)` is eventually much better than `1/q^2` and therefore must be an ordinary principal convergent. That collapses the exponential half-integer problem to the even-denominator subsequence and yields `(4)`.

A targeted literature search for parity-constrained irrationality bases, exponential odd/even approximation, and continued-fraction limsup formulae located the general Sondow theory and the Kim--Lee--Liao parity-best-approximation theory, but did not locate the exact parity-filtered exponential identity `(4)` or its Keiper--Li consequence `(9)`. This is not an exhaustive novelty proof. No novelty is claimed for Legendre's criterion, the convergent error bounds, Sondow's unrestricted formula, or parity continued-fraction algorithms.

## Boundaries

**Irrational phase only.** Rational `alpha` can have exact periodic half-integer hits and belongs to the exact-alias regime already separated in AF-245--AF-248. Equations `(4)`--`(9)` address near-cancellation for irrational phases.

**Two-mode dominant pair only.** The exact parity reduction uses the zero set of one cosine. With several co-dominant Keiper phases, cancellation occurs on the zero set of a multivariable trigonometric polynomial; one-dimensional even-denominator continued fractions no longer classify the fiber norm. AF-246 and AF-253 remain the appropriate general framework there.

**This is a source criterion, not a theorem about zeta zeros.** Nothing here proves that the normalized phase of an actual or hypothetical Riemann zero satisfies `(9)`, has finite irrationality exponent, or avoids exponentially large parity-selected continued-fraction jumps. AF-256 only makes the zero-coordinate resonance geometry explicit; the arithmetic source theorem remains missing.

**The unrestricted irrationality base remains sufficient but is no longer exact for this channel.** Equation `(31)` immediately gives `L_oe(alpha)<=log beta(alpha)` and recovers AF-249's bound `kappa_{1/2}(alpha)<=2 log beta(alpha)`. The new information is that odd-denominator exponential jumps do not enter the exact half-integer cancellation exponent.

## Research consequence

For one hypothetical off-critical conjugate Keiper pair, the source-side fidelity problem is now completely localized to a concrete continued-fraction event. Sparse output sampling can suppress the pair to unit root rate or below only if the normalized phase `theta_rho/pi` has even-denominator convergents whose next denominators grow exponentially fast enough to consume the pair's radial margin.

Using AF-255's high-zero scale, a sufficient and exact all-sampling inequality is

\[
\limsup_{\substack{j\to\infty\\q_j\ \mathrm{even}}}
\frac{\log q_{j+1}}{q_j}
<
\frac12\log q_\rho
\asymp
\frac{\beta-1/2}{2\gamma^2}.
\tag{32}
\]

The remaining arithmetic question is therefore sharper than “prove the Keiper phase is not Liouville.” One must control parity-selected exponential continued-fraction jumps at a zero-dependent threshold that shrinks quadratically with height. Any future source theorem can now be tested against this exact target; generic irrationality, ordinary zero-spacing, or an unrestricted phase heuristic is not enough unless it quantitatively implies `(32)`.