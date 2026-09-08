# MC-156 — One signed prime semigroup commutator cubically reconstructs Möbius

**Status:** `EXACT-DERIVED`, `DECISIVE-NEGATIVE`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation used in `MC-149`–`MC-155`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_k=\varepsilon_{pk},
\qquad
D_\mu\varepsilon_k=\mu(k)\varepsilon_k,
\]

and fix **any one prime** `p`. Put

\[
C_p=[D_\mu,S_p],
\qquad
B_p=S_p^*C_p
     =S_p^*D_\mu S_p-D_\mu.
\tag{1}
\]

Then `B_p` is diagonal and

\[
B_p\varepsilon_k
=b_p(k)\varepsilon_k,
\qquad
b_p(k)=\mu(pk)-\mu(k).
\tag{2}
\]

The signed coefficient alphabet already contains the complete Möbius target. More precisely,

\[
\boxed{
D_\mu
= P(B_p),
\qquad
P(t)=\frac{t^3-7t}{6}.
}
\tag{3}
\]

Equivalently, for every `k`,

\[
\boxed{
\mu(k)=P\!\left(\mu(pk)-\mu(k)\right).
}
\tag{4}
\]

Thus the **exact signed matrix coefficients of a single fixed-prime raw semigroup commutator reconstruct the entire Möbius sequence pointwise**, with no anchor, no all-prime family, no unbounded mixed-commutator depth, and no limiting procedure.

This closes a precise loophole left by `MC-155`. That finding showed that magnitude rows and continuous one-state signed cluster data remain cancellation-blind, and therefore listed relational matrix coefficients among the information types not covered by its no-go. The present result shows that the most literal escape — retain the complete state-labelled signed coefficient field of `[D_\mu,S_p]` — overshoots in the opposite direction: it is target-complete already at one prime and first commutator depth.

A surviving semigroup/Bost–Connes mechanism must therefore **compress, aggregate, quotient, or otherwise reduce** these signed coefficients before using them, and must prove that the reduced object still transfers quantitatively to anchored Mertens excursion. Merely keeping the exact signed operator cannot count as an intermediate explanation of cancellation.

## 1. The pulled-back commutator is exactly a multiplicative first difference

From the canonical action,

\[
[D_\mu,S_p]\varepsilon_k
=\bigl(\mu(pk)-\mu(k)\bigr)\varepsilon_{pk}.
\tag{5}
\]

Because `S_p` is an isometry,

\[
S_p^*\varepsilon_{pk}=\varepsilon_k,
\]

so `(5)` gives `(2)` immediately. In particular `B_p` is a bounded self-adjoint diagonal operator with

\[
\sigma(B_p)\subseteq\{-2,-1,0,1,2\}.
\tag{6}
\]

The important distinction from the scalar regularity readouts in `MC-149`–`MC-155` is that `(2)` retains both the **sign** and the **state label** `k` of each multiplicative difference.

## 2. Möbius multiplicativity leaves only five possible signed differences

There are three exhaustive cases.

If `k` is not squarefree, then `pk` is also not squarefree, hence

\[
\mu(k)=\mu(pk)=0,
\qquad
b_p(k)=0.
\tag{7}
\]

If `k` is squarefree and `p\nmid k`, multiplicativity gives

\[
\mu(pk)=\mu(p)\mu(k)=-\mu(k),
\]

and therefore

\[
b_p(k)=-2\mu(k)\in\{-2,2\}.
\tag{8}
\]

Finally, if `k` is squarefree and `p\mid k`, then `pk` contains `p^2`, so

\[
\mu(pk)=0,
\qquad
b_p(k)=-\mu(k)\in\{-1,1\}.
\tag{9}
\]

Consequently

\[
b_p(k)=
\begin{cases}
0,&\mu(k)=0,\\
-2\mu(k),&\mu(k)\ne0\text{ and }p\nmid k,\\
-\mu(k),&\mu(k)\ne0\text{ and }p\mid k.
\end{cases}
\tag{10}
\]

In particular the sign alone already decodes the nonzero value:

\[
\mu(k)=-\operatorname{sgn}(b_p(k)),
\qquad
\operatorname{sgn}(0)=0.
\tag{11}
\]

The cubic in `(3)` is simply a polynomial version of this finite-alphabet decoder.

## 3. A cubic polynomial gives an exact operator decoder

The odd cubic

\[
P(t)=\frac{t^3-7t}{6}
\tag{12}
\]

satisfies

\[
P(0)=0,
\qquad
P(1)=P(2)=-1,
\qquad
P(-1)=P(-2)=1.
\tag{13}
\]

Combining `(10)` with `(13)` yields `(4)` for every positive integer `k`. Since both `D_\mu` and `P(B_p)` are diagonal in the same orthonormal basis, pointwise equality of their diagonal entries proves the operator identity `(3)`.

Hence

\[
D_\mu\in C^*(B_p)
=C^*\!\left(S_p^*[D_\mu,S_p]\right),
\tag{14}
\]

and the inclusion is not merely abstract: the target is obtained by a degree-three polynomial.

There is no hidden infinite-depth limit in `(14)`. One canonical prime direction suffices. Nor does the reconstruction require knowledge of whether `p` divides `k`: the magnitude of `b_p(k)` distinguishes the two squarefree cases automatically, while its sign supplies `\mu(k)`.

## 4. This identifies the exact information boundary behind the previous commutator no-gos

`MC-149` already computes the local values in `(10)` while classifying **operator norm, essential norm, compactness, and Schatten behavior** of the raw commutator. Those scalar regularity summaries discard the coefficient signs and state labels. As a result, boundedness is universal for bounded diagonals while compact/Schatten decay rejects Möbius.

`MC-150`–`MC-154` then show that scalar weighting, divisibility splits, fixed mixed depth, and direction-by-direction all-depth norm data do not recover the missing cancellation information. `MC-155` strengthens this to simultaneous weighted row magnitudes and to continuous one-state signed cluster data: a support-matched sequence with positive linear mean can share the relevant extremal rows and signed cluster point with Möbius.

Equation `(3)` shows why simply undoing all of those quotients is not the answer. Once one retains the **complete exact signed coefficient table** of even one prime commutator, there is no longer an information deficit to solve: the original target diagonal is already present by polynomial functional calculus.

Thus the current semigroup frontier has a sharp two-sided boundary:

- scalar/topological summaries studied through `MC-155` discard enough structure to admit linearly biased controls;
- exact state-labelled signed coefficients retain so much structure that they reconstruct `D_\mu` itself.

The mathematically live question is therefore an **intermediate quotient**: a source-forced relation among commutator coefficients that is strictly weaker than the exact table, still excludes the known biased controls, and has an independently controlled transfer to additive Mertens excursion.

## 5. Quantitative stability of the literal coefficient decoder

The exact result is already decisive for exact retention, but the polynomial decoder is also locally stable at the coefficient level. On `[-2,2]`,

\[
P'(t)=\frac{3t^2-7}{6},
\qquad
\sup_{|t|\le2}|P'(t)|=\frac76.
\tag{15}
\]

Therefore if a scalar approximation `\widetilde b(k)\in[-2,2]` satisfies

\[
|\widetilde b(k)-b_p(k)|\le\eta,
\]

then

\[
\left|P(\widetilde b(k))-\mu(k)\right|
\le\frac76\eta.
\tag{16}
\]

This does **not** classify noisy aggregate statistics or prove an operator-Lipschitz theorem for arbitrary noncommuting perturbations. It only emphasizes that a proposal retaining the state-labelled scalar coefficient field with uniformly small error remains a near-pointwise encoding of the target rather than a qualitatively cheaper cancellation observable.

## Prior art and novelty assessment

The Bost–Connes system, its canonical semigroup isometries, and the number-state representation are established prior art, already audited in `MC-138`–`MC-149`. In particular, `MC-149` cites Bost–Connes (1995), Laca–Raeburn (1999), and the twisted-spectral-triple boundary of Greenfield–Marcolli–Teh (2014). The weighted-shift/diagonal calculation `(5)` is also already part of `MC-149`.

The new line-level delta is the **information classification of the signed coefficient object itself**: the case split from `MC-149` implies the exact decoder `(3)`, so the literal signed-operator escape left after the later scalarization no-gos is target-complete. Polynomial interpolation on the finite spectrum `(6)` is elementary functional calculus, and Möbius multiplicativity is classical.

A targeted literature search for Bost–Connes semigroup commutators together with Möbius arithmetic did not locate this cubic identity as a named theorem. No novelty inference is drawn from that absence. The result is an immediate exact specialization of standard commutator calculus plus the classical local Möbius rules, so it is recorded as `EXACT-DERIVED` with **no novelty claim**.

## Boundaries and falsification tests

- **Exact signed coefficients are load-bearing.** Norms, absolute values, spectra without state labels, coefficient distributions, cluster sets, moments, and other quotients need separate analysis. `MC-149`–`MC-155` already show that several natural such quotients are cancellation-blind.
- **The result is Möbius-specific.** It does not say that one prime commutator reconstructs an arbitrary bounded diagonal. The decoder works because Möbius has squarefree support and the exact multiplicative transition law in `(10)`.
- **This is an information no-go, not a source construction.** The identity does not construct `[D_\mu,S_p]` independently of `D_\mu`. It says that a proposed carrier which assumes access to that exact signed commutator has already retained the target it was meant to explain.
- **No Mertens estimate follows.** Summing the reconstructed diagonal merely recovers `M(x)`. Equation `(3)` supplies no independent bound on the resulting partial sums and therefore no progress toward RH by itself.
- **Compressed relational statistics remain open.** A statistic coupling different states or scales can evade this result if it does not permit recovery of the exact coefficient table. It must then be tested against the support-matched linearly biased controls and against target-equivalence.
- **Alternative representations/twists remain open.** The theorem uses the canonical number-state `S_p` and diagonal `D_\mu`. A genuinely different representation, twisted commutator, unbounded correspondence, or source-defined observable requires its own reconstruction audit.
- **The cubic is directly falsifiable.** A single integer `k` and prime `p` for which `(10)` holds but `P(b_p(k))\ne\mu(k)` would refute `(3)`; the five possible values in `(7)`–`(9)` exhaust all cases.

## Consequence for the line

The residual Bost–Connes/semigroup frontier after `MC-155` should no longer list **exact signed relational matrix coefficients of the raw prime commutator** as an unexplored intermediate carrier. At that resolution, even one prime direction is already Möbius-complete by the cubic identity `(3)`.

Future work in this route must instead identify a mathematically natural **lossy but cancellation-preserving quotient** of signed semigroup data: weak enough that `D_\mu` cannot be recovered pointwise by a fixed decoder, strong enough to distinguish the explicit biased controls, and equipped with a source-to-Mertens estimate that is genuinely cheaper than controlling `M(x)` itself.