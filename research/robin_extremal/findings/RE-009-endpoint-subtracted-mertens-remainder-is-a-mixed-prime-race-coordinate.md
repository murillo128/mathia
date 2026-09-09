# RE-009 — endpoint-subtracted Mertens remainder is a mixed prime-race coordinate

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-COLLISION + MIXED-ERROR-IDENTIFICATION + GLOBAL-BOUND-OBSTRUCTION + SOURCE-SELECTION-NARROWING`. `RE-008` shows that every unbounded sequence of clean regular self-tangent Robin-counterexample peaks, with consecutive first-layer boundary primes `p<q`, must satisfy

\[
\liminf \sqrt p\log p\,\mathcal M_*(p)\ge 2\sqrt2,
\qquad
\mathcal M_*(p)=E(p)-(\vartheta(p)-p)h(p),
\]

where `E` is the logarithmic Mertens-product error and `h(x)=-log(1-x^{-1})/log x`. A current prior-art audit changes the interpretation of this remaining quantity. After the square-root normalization used by `RE-008`, `mathcal M_*` is, up to an unconditional `o(1)` term, exactly the difference between the normalized logarithmic Mertens-product error and the normalized Chebyshev `theta` error studied by Bhattacharya--Martin--Simpson.

More precisely, for real `x>=2`, define

\[
\mathscr Y(x):=\sqrt x\log x\,\mathcal M_*(x),
\]

with

\[
E(x):=\sum_{r\le x}-\log(1-r^{-1})-\gamma-\log\log x,
\qquad
\mathcal M_*(x):=E(x)-(\vartheta(x)-x)h(x).
\]

Let

\[
\mathcal E_{\vartheta}(x):=\frac{\vartheta(x)-x}{\sqrt x},
\qquad
\mathcal E_{\pi_\ell}(x):=E(x)\sqrt x\log x,
\]

which are exactly the normalized error terms `E^theta` and `E^{pi_l}` in Bhattacharya--Martin--Simpson. Then

\[
\boxed{
\mathscr Y(x)
=\mathcal E_{\pi_\ell}(x)-\lambda(x)\mathcal E_{\vartheta}(x),
\qquad
\lambda(x):=-x\log(1-x^{-1}),
}
\tag{1}
\]

and therefore, unconditionally,

\[
\boxed{
\mathscr Y(x)
=\mathcal E_{\pi_\ell}(x)-\mathcal E_{\vartheta}(x)+o(1).
}
\tag{2}
\]

This identifies the surviving source quantity of `RE-008` with a standard **mixed standard/reciprocal prime race** rather than a new isolated Mertens remainder.

The identification has a sharp strategic consequence. Bhattacharya--Martin--Simpson prove that one-sided boundedness of this mixed normalized difference is itself equivalent to RH. Hence a global unconditional upper or lower bound for `mathscr Y(x)` cannot be a genuinely weaker source theorem: it would already settle RH. The clean Robin route must exploit the additional CA self-tangent **selection of the boundary primes**, not merely control `mathcal M_*` on all inputs.

## 1. Exact normalization dictionary

Bhattacharya--Martin--Simpson define

\[
\pi_\ell(x)
:=\log\prod_{r\le x}(1-r^{-1})^{-1}
=\sum_{r\le x}-\log(1-r^{-1}),
\]

and their normalized reciprocal error is

\[
\mathcal E_{\pi_\ell}(x)
=\bigl(\pi_\ell(x)-\log\log x-\gamma\bigr)\sqrt x\log x.
\tag{3}
\]

Thus the `E(x)` of `RE-008` satisfies exactly

\[
\mathcal E_{\pi_\ell}(x)=E(x)\sqrt x\log x.
\tag{4}
\]

For the endpoint subtraction,

\[
\begin{aligned}
\sqrt x\log x\,(\vartheta(x)-x)h(x)
&=\sqrt x\,(\vartheta(x)-x)\bigl[-\log(1-x^{-1})\bigr]\\
&=\mathcal E_{\vartheta}(x)\,
\underbrace{\bigl[-x\log(1-x^{-1})\bigr]}_{\lambda(x)}.
\end{aligned}
\tag{5}
\]

Equations (4)--(5) prove (1) without asymptotics.

The elementary expansion

\[
\lambda(x)=1+\frac1{2x}+O(x^{-2})
\tag{6}
\]

is enough for the second step. Chebyshev's classical bound `vartheta(x)=O(x)` gives

\[
\mathcal E_{\vartheta}(x)=O(\sqrt x),
\]

so

\[
(\lambda(x)-1)\mathcal E_{\vartheta}(x)=O(x^{-1/2}).
\tag{7}
\]

This proves (2) **unconditionally**. No RH-quality error term for `theta` is being inserted into the dictionary.

## 2. Under RH the entire mixed race lies far below the clean-counterexample threshold

Bhattacharya--Martin--Simpson assign bias constants

\[
\beta_{\vartheta}=-1,
\qquad
\beta_{\pi_\ell}=1.
\tag{8}
\]

Their Theorem 1.4(b) says that under RH, for any reciprocal normalized error minus any standard normalized error,

\[
\beta_f-\beta_g-w
\le\liminf(\mathcal E_f-\mathcal E_g)
\le\limsup(\mathcal E_f-\mathcal E_g)
\le\beta_f-\beta_g+w,
\]

with

\[
w=2+\gamma-\log(4\pi)=0.0461914\ldots.
\tag{9}
\]

Taking `f=pi_l` and `g=theta`, and then using (2), gives

\[
\boxed{
2-w
\le\liminf_{x\to\infty}\mathscr Y(x)
\le\limsup_{x\to\infty}\mathscr Y(x)
\le2+w
\qquad(\mathrm{RH}).
}
\tag{10}
\]

In particular

\[
2+w=2.0461914\ldots<2\sqrt2=2.8284271\ldots.
\tag{11}
\]

Thus the `RE-008` clean-counterexample requirement is not merely a positive Mertens excursion under RH normalization: it lies outside the full RH range of the mixed Mertens--Chebyshev coordinate.

Under RH+LI, their Theorem 1.17(b) strengthens the range statement to a joint limiting logarithmic distribution whose support is exactly the diagonal strip of width `w`. Projecting that strip onto the difference coordinate and using (2), the limiting support of `mathscr Y` is exactly

\[
\boxed{[2-w,\,2+w].}
\tag{12}
\]

No novelty is claimed for this prime-race support theorem; it is current prior art. Its role here is to locate the precise source coordinate selected indirectly by `RE-008`.

## 3. A global one-sided bound for the surviving remainder is RH-equivalent

The more consequential prior-art boundary is Bhattacharya--Martin--Simpson Theorem 1.6(b). For a standard function `g` and reciprocal function `f` with unequal biases, outside a short list of elementary comparison pairs, RH is equivalent to an eventual strict ordering of their normalized errors. More generally, RH is equivalent to their normalized difference being bounded **either above or below**.

The pair `(theta,pi_l)` is not one of the exceptional elementary pairs. Therefore

\[
\boxed{
\mathrm{RH}
\iff
\mathcal E_{\pi_\ell}(x)-\mathcal E_{\vartheta}(x)
\text{ is bounded above or bounded below.}
}
\tag{13}
\]

Since (2) changes this difference by `o(1)`, the same equivalence holds for the exact `RE-008` coordinate:

\[
\boxed{
\mathrm{RH}
\iff
\mathscr Y(x)=\sqrt x\log x\,\mathcal M_*(x)
\text{ is bounded above or bounded below.}
}
\tag{14}
\]

Consequently, if RH is false then `mathscr Y` is unbounded in **both** directions on the real input line. A fixed global threshold such as `2sqrt(2)` is therefore not, by itself, a restrictive phenomenon in an RH-false world. What is restrictive in `RE-008` is that the positive excursion must occur at the boundary primes selected simultaneously by the clean CA self-tangent geometry.

This rules out a specific tempting continuation of the accepted clean-selector clue: proving a universal estimate

\[
\sqrt x\log x\,\mathcal M_*(x)\le C
\quad\text{or}\quad
\sqrt x\log x\,\mathcal M_*(x)\ge-C
\]

for all sufficiently large `x` is not a weaker analytic input waiting to be combined with Robin geometry. By (14), either statement is already an RH theorem in disguise.

## 4. What remains genuinely source-specific

`RE-008` is still stronger than the bare prime-race statement because a clean hypothetical Robin counterexample supplies three simultaneous constraints on the same boundary prime `p`:

1. `p` is selected by the exact CA self-tangent equation of `RE-006`;
2. the neighboring first-layer prime gap and higher-layer mass obey the clean peak geometry of `RE-007`;
3. the mixed error coordinate satisfies `mathscr Y(p)>=2sqrt(2)+o(1)` by `RE-008`.

Equation (14) says that none of these can be replaced by a global one-sided bound on the third coordinate. A useful next theorem has to be a **conditional distribution/correlation statement under the CA selector**, an exclusion of simultaneous selector-and-height alignment, or an argument forcing hypothetical counterexamples into the higher-layer/tied chamber. The difficulty is therefore not ordinary Mertens oscillation, and it is not ordinary `theta` oscillation; it is the arithmetic dependence between the extremal exponent geometry and a mixed prime-race coordinate.

This also changes how matched controls should be designed. A control that merely reproduces the marginal size or sign distribution of `mathscr Y` is too weak. It must preserve the clean CA selection conditions while changing the transported Robin height, or preserve the mixed error coordinate while breaking the self-tangent/event geometry. Otherwise it does not test the remaining implication.

## 5. Prior art, audit, and evidence boundary

The load-bearing new source is Shubhrajit Bhattacharya, Greg Martin, and Reginald M. Simpson, *Correlations of error terms for weighted prime counting functions*, arXiv:2507.13504v2 (6 May 2026). Their Definitions 1.2--1.3 provide the normalized `theta` and logarithmic Mertens-product errors and their biases; Theorem 1.4 gives the RH strip bound; Theorem 1.6 gives the RH equivalence for persistent/one-sided mixed-error bounds; and Theorem 1.17 identifies the joint support under RH+LI. The paper is directly prior art for the mixed error coordinate. The derivation (1)--(7) is the Mathia-specific dictionary showing that `RE-008` had independently arrived at this coordinate through the clean CA selector.

The conclusion does **not** weaken the `RE-008` necessary condition, prove Robin's inequality, or prove RH. In particular, Theorem 1.4 cannot be used inside a hypothetical Robin counterexample argument, because RH already excludes Robin counterexamples. Its value is diagnostic: it shows exactly which global theorem would be circularly strong and leaves only the source-selected correlation as a potentially weaker route.

Nor does the unboundedness consequence of (14) say that excursions above `2sqrt(2)` occur at primes, still less at clean CA boundary primes. It is a statement on the real input line. Transferring it to the sparse extremal selector would itself require new arithmetic information and is precisely the gap this finding isolates.

The recent correlation paper substantially classicalizes the standalone behavior of `mathcal M_*`; no novelty claim is made for its global mixed-race distribution or RH equivalence. The durable contribution here is the exact normalization dictionary and the resulting obstruction: **a successful clean Robin argument must condition on the extremal selector, because every global one-sided control of the surviving remainder is already RH-equivalent.**