# WI-408 — finite superzeta exponent jets only control logarithmic defect moments

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

**Parent findings:** [WI-405](./WI-405-signed-widder-mellin-averages-collapse-to-superzeta-and-require-renormalization.md), [WI-406](./WI-406-canonical-superzeta-continuation-at-critical-widder-weight-is-fixed.md), [WI-407](./WI-407-superzeta-derivative-at-minus-one-gives-log-weighted-defect.md).

## Claim

WI-407 showed that the first exponent derivative of the second-kind superzeta at the critical Widder exponent `sigma=-1` has a positive same-ordinate off-line pair defect asymptotic to `4 d^2 log gamma`. It left open whether a source-exact matched renormalization with a contracting tail budget could turn that positive charge into a defect-to-zero bootstrap.

There is a sharp barrier to that weak formulation. For every fixed derivative order `k`, the finite-pair defect is asymptotically a degree-`k` polynomial in `log gamma` times `d^2`. More precisely, with the natural orientation that makes the high-zero defect positive,

\[
\boxed{
Q_k(\gamma,d)
=
2^{k+1}d^2(\log\gamma)^k
\left(1+O_k\!\left(\frac1{\log\gamma}+\frac{d^2}{\gamma^2}\right)\right)
}
\tag{1}
\]

uniformly for `0 <= d <= 1/2` as `gamma -> infinity`. Thus any finite exponent jet sees only finitely many logarithmic moments of the horizontal square-depth measure.

This limitation does not disappear merely by taking every fixed derivative order separately. The hypothetical quartet sequence

\[
\gamma_n=e^n,
\qquad
 d_n=e^{-n},
\qquad
\rho=\frac12\pm d_n\pm i\gamma_n,
\tag{2}
\]

has infinitely many off-critical quartets, respects the functional-equation/conjugation symmetry, and satisfies

\[
\sum_{n\ge1}|Q_k(\gamma_n,d_n)|<\infty
\qquad
\text{for every fixed }k.
\tag{3}
\]

Consequently, neither a finite superzeta derivative jet nor the statement that **all fixed-order derivative defects are finite, one order at a time**, can force the off-critical defect measure to vanish. Likewise, a merely positive tail envelope tending to zero cannot by itself force RH: positive local charges can shrink arbitrarily fast with `d`, and any finite collection of off-line zeros disappears entirely from a sufficiently high tail.

This is a barrier only for the scalar moment/finite-jet ledger. It does **not** rule out exact source identities giving zero defect, exact values of a sufficiently rich transform family, large-order information that determines the defect measure, or an independent arithmetic lower bound on horizontal depth.

## 1. Exact derivative carrier

For an upper-half-plane functional-equation pair

\[
\rho_\pm=\frac12\pm d+i\gamma,
\qquad 0<d<\frac12,
\]

use WI-407's variables

\[
\tau_\pm=\gamma\mp id,
\qquad
w_\pm=\tau_\pm^2.
\]

For every integer `k >= 0`,

\[
\left.\partial_\sigma^k w^{-\sigma}\right|_{\sigma=-1}
=(-\Log w)^k w.
\tag{4}
\]

Define

\[
f_k(z)=z^2\bigl(\Log z^2\bigr)^k,
\qquad
L=\log(\gamma^2).
\tag{5}
\]

At high `gamma`, with the principal logarithm, the actual pair contribution to the `k`th exponent derivative is

\[
A_k=2(-1)^k\Re f_k(\gamma-id),
\]

while the same-ordinate criticalized pair contributes

\[
C_k=2(-1)^k f_k(\gamma).
\]

Orient the local defect by

\[
\boxed{
Q_k(\gamma,d)
:=(-1)^{k+1}(A_k-C_k)
=2\left[f_k(\gamma)-\Re f_k(\gamma-id)\right].
}
\tag{6}
\]

This convention recovers the earlier exact carriers:

\[
Q_0(\gamma,d)=2d^2,
\qquad
Q_1(\gamma,d)=\Delta_1(\gamma,d)
\]

with `Delta_1` exactly as in WI-407.

The construction is finite-pair algebra. No regularized infinite zero sum is being differentiated termwise here, so the identity does not assume a global matched renormalization.

## 2. Fixed-order asymptotic

Taylor-expand the holomorphic function `f_k` from `gamma` to `gamma-id`. Odd Taylor terms are purely imaginary after evaluation at the positive real point, hence

\[
Q_k(\gamma,d)
=d^2 f_k''(\gamma)
+O_k\!\left(
\frac{d^4}{\gamma^2}(1+L^k)
\right),
\tag{7}
\]

uniformly for `0 <= d <= 1/2` once `gamma` is bounded away from zero. The remainder follows by bounding `f_k^{(4)}` on the vertical segment `gamma-it`, `0 <= t <= d`; for fixed `k`,

\[
f_k^{(4)}(z)
=O_k\!\left(|z|^{-2}(1+|\Log z^2|^k)\right).
\]

A direct differentiation gives the exact second derivative

\[
\boxed{
f_k''(\gamma)
=
2L^k+6kL^{k-1}+4k(k-1)L^{k-2},
}
\tag{8}
\]

where terms with negative powers are absent when their polynomial coefficient vanishes. Combining (7) and (8),

\[
\boxed{
Q_k(\gamma,d)
=
2d^2L^k
+6kd^2L^{k-1}
+4k(k-1)d^2L^{k-2}
+O_k\!\left(
\frac{d^4}{\gamma^2}(1+L^k)
\right).
}
\tag{9}
\]

Since `L=2 log gamma`, equation (1) follows. In particular, for every fixed `k`, sufficiently high off-line pairs have `Q_k>0`, and `Q_k` is comparable to

\[
d^2(\log\gamma)^k.
\]

Therefore a matched source identity that merely proves finiteness of the first `K+1` derivative defects can give, at most, finitely many logarithmic moment constraints of the form

\[
\sum_{\text{off-line pairs}}
 d_\rho^2(\log\gamma_\rho)^k<\infty,
\qquad 0\le k\le K,
\tag{10}
\]

up to finitely many low zeros and the usual requirement that the matched subtraction preserve the finite-pair difference.

## 3. Even all fixed-order moment finiteness does not force zero defect

Consider the hypothetical symmetric zero configuration (2). It contains `O(log T)` exceptional quartets below height `T`, so gross zero-counting scale alone does not forbid this sparse model. It is not asserted to be realizable by the Riemann zeta function; it is only a logical countermodel to conclusions based solely on the derivative-moment ledger.

For every fixed `k`, equation (9) gives

\[
Q_k(e^n,e^{-n})
=O_k(e^{-2n}n^k).
\tag{11}
\]

Hence

\[
\sum_{n\ge1}|Q_k(e^n,e^{-n})|
<\infty
\qquad\text{for every fixed }k,
\tag{12}
\]

because an exponential dominates every fixed polynomial. Equivalently, the positive measure

\[
\mu
=
\sum_{n\ge1} d_n^2\,\delta_{\log\gamma_n}
=
\sum_{n\ge1}e^{-2n}\delta_n
\tag{13}
\]

is nonzero and has every polynomial moment finite.

This separates two logically different statements that should not be conflated:

- knowing that every fixed-order moment **exists/is finite** does not determine `mu` and does not imply `mu=0`;
- knowing sufficiently rich **exact values** of moments or of an analytic transform can, under additional determinacy hypotheses, determine a measure.

The first statement is all that follows from a family of finite matched budgets. The second would require genuinely new source-side information.

## 4. A tail tending to zero is not a defect-to-zero mechanism by itself

The same obstruction already appears at first derivative order. For each fixed `gamma`, WI-407's exact charge `Delta_1(gamma,d)` is continuous in `d` and tends to zero as `d -> 0`. Therefore there is no height-independent positive quantum of defect associated with an off-line pair.

Suppose a source argument produced only a bound

\[
0\le
\sum_{\gamma_\rho>H}\Delta_1(\gamma_\rho,d_\rho)
\le B(H),
\qquad B(H)\to0.
\tag{14}
\]

The convergence `B(H)->0` is not coercive by itself. A finite set of off-line pairs has zero tail once `H` passes its largest ordinate. An infinite sparse set can also have a positive summable charge with a tail tending to zero; by shrinking `d_n` further, its tail can be made to fit any prescribed positive envelope on a chosen increasing sequence of heights.

Thus the weak suggestion left open after WI-407 must be sharpened: **tail contraction alone does not force zero defect**. To exclude every off-line pair, a source-side identity needs additional rigidity, for example an exactly vanishing total defect, a nonzero lower bound/quantization for the charge of any admissible off-line zero, or cross-order/analytic-transform data whose exact values determine the positive defect measure.

This is the decisive negative result of the present finding. It redirects the superzeta branch away from accumulating more fixed derivative budgets and toward source identities that preserve substantially more than moment finiteness.

## 5. Prior-art audit and novelty boundary

The superzeta framework is classical. The primary references used by WI-405--WI-407 remain:

- André Voros, *Zeta functions for the Riemann zeros*, *Annales de l'Institut Fourier* **53** (2003), 665--699, DOI `10.5802/aif.1955`: <https://www.numdam.org/articles/10.5802/aif.1955/>.
- André Voros, *Erratum - Zeta functions for the Riemann zeros*, *Annales de l'Institut Fourier* **54** (2004), 1139, DOI `10.5802/aif.2046`: <https://www.numdam.org/articles/10.5802/aif.2046/>.
- André Voros, *Zeta functions over zeros of Zeta functions and an exponential-asymptotic view of the Riemann Hypothesis*, arXiv:`1403.4558` (2014): <https://arxiv.org/abs/1403.4558>.

Voros's 2014 analysis is especially relevant to the boundary here: its RH-sensitive criterion uses **large-order asymptotics** of Keiper--Li-type data, not mere existence of each fixed coefficient. That is qualitatively consistent with the barrier above.

The general moment-problem distinction is also classical: finiteness of all moments is not the same as knowing a determinate moment sequence. Standard Stieltjes/Hamburger moment theory adds hypotheses such as Carleman-type conditions when exact moment values are used to determine a measure. The countermodel (13) makes that general background unnecessary for the actual no-go proof: it directly exhibits a nonzero positive measure with every polynomial moment finite.

A targeted prior-art search around Riemann-zero superzeta derivatives, negative-integer exponent derivatives, logarithmic moment defects, and classical moment determinacy found the Voros framework and standard moment-problem theory, but no exact formulation of the finite-pair hierarchy (6)--(9) or the specific barrier (11)--(14). That negative search is not used as a priority claim.

The evidence boundary is:

- `CLASSICAL-IDENTITY`: exponent differentiation and the general moment-problem distinction;
- `LITERATURE+DERIVED`: the second-kind superzeta at the critical Widder exponent inherited from WI-405--WI-407 and the comparison with Voros's large-order use of superzeta data;
- `EXACT-DERIVED`: equations (6)--(12), including the uniform fixed-order asymptotic;
- `DECISIVE-NEGATIVE`: finite jets, all-fixed-order finiteness, and a merely vanishing positive tail budget cannot by themselves imply zero off-line defect;
- `PRIOR-ART-REDIRECT`: useful information must come from exact cross-order/source identities, a full transform, large-order structure, or independent horizontal-depth rigidity rather than additional fixed-order budget finiteness.

No claim is made that the model (2) can occur for actual zeta zeros, and no priority claim is made for superzeta differentiation, moment problems, or large-order criteria.

## Consequence

The exponent-derivative direction does not bootstrap from `d^2` to RH by repeatedly adding logarithms. At every fixed order it only replaces the weight by another polynomial in `log gamma`, and even the entire collection of fixed-order **finiteness** statements admits nonzero sparse defect measures.

The viable next target is therefore stronger and more specific than the one left by WI-407: derive a source-exact matched object whose values across the exponent parameter determine the horizontal defect measure, or whose defect is forced to vanish exactly. A scalar finite budget, or a family of such budgets indexed by fixed derivative order, is structurally insufficient.