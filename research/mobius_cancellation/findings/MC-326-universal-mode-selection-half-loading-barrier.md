# MC-326 — Universal mode selection cannot beat the half-loading barrier

**Status:** `EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the common lower-prime source package of `MC-312`, `MC-324`, and `MC-325`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\tag{1}
\]

choose fixed lower-prime product representatives `V_i` for the basis functionals, and for every source prime `p` write its nonzero incidence column as

\[
s_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbf F_2^R\setminus\{0\}.
\tag{2}
\]

For a coefficient vector `a\in\mathbf F_2^R`, the symmetric-difference package representative of

\[
\lambda_a:=\sum_{i=1}^R a_i\lambda_i
\]

contains `p` exactly when

\[
a\cdot s_p=1.
\tag{3}
\]

Now allow an **arbitrary nonempty selected mode family**

\[
\mathcal F\subseteq\mathbf F_2^R\setminus\{0\}
\tag{4}
\]

and arbitrary nonnegative mode weights `w_a`, not all zero. Put

\[
W:=\sum_{a\in\mathcal F}w_a,
\qquad
L_{\mathcal F,w}(s)
:=\sum_{\substack{a\in\mathcal F\\a\cdot s=1}}w_a.
\tag{5}
\]

Then the best source-column loading constant available **uniformly over all possible nonzero incidence columns** satisfies the sharp inequality

\[
\boxed{
\max_{s\ne0}\frac{L_{\mathcal F,w}(s)}W
\ge
\frac{2^{R-1}}{2^R-1}
=\frac12+\frac1{2(2^R-1)}.
}
\tag{6}
\]

The constant is sharp as a purely linear-algebraic statement: equality holds when `\mathcal F=\mathbf F_2^R\setminus\{0\}` with equal weights.

Consequently, **no choice of mode subfamily and no nonnegative reweighting can produce a universal asymptotic source-loading constant below `1/2`**. This closes the unrestricted version of the sub-half-loading escape left after `MC-325`.

More specifically, suppose a proof architecture has individual package-cost lower bounds

\[
\log m_a\ge h\log y
\qquad(a\in\mathcal F),
\tag{7}
\]

for some common `h>0`, and attempts to convert them into a common-radical lower bound only by positive weighted summation plus a source-column incidence ceiling. If

\[
c_{\mathcal F,w}
:=
\max_{s\ne0}\frac{L_{\mathcal F,w}(s)}W,
\tag{8}
\]

then the exact source double count gives

\[
\sum_{a\in\mathcal F}w_a\log m_a
\le
c_{\mathcal F,w}W\log P,
\tag{9}
\]

so this route can force at most the exponent

\[
\frac{h}{c_{\mathcal F,w}}
\le
h\frac{2^R-1}{2^{R-1}}.
\tag{10}
\]

For the current varying-modulus prime Halász--Montgomery input of `MC-323`, one may take `h=2-\delta` on any growing fixed-bias family after discarding its `O_\delta(1)` exceptional modes. Therefore **every universal nonnegative incidence-averaging argument built on that individual-conductor horizon has common-radical exponent ceiling**

\[
\boxed{
(2-\delta)\frac{2^R-1}{2^{R-1}}
<4-2\delta,
}
\tag{11}
\]

and after the legitimate fixed-`\delta` limit, at most quartic asymptotically.

The pair family of `MC-324` already reaches

\[
4-O(R^{-1})
\tag{12}
\]

and the sparse even layers of `MC-325` again approach `4`. Hence those arguments are not merely examples that happened to stop at exponent `4`: **the pair layer is asymptotically optimal among all mode-selection/reweighting strategies whose only source-side information is a universal per-column incidence cap and whose analytic input is a positive sum of independent near-quadratic conductor bills.**

This does not rule out a source-specific sub-half family. It shows what such an escape must contain: an additional arithmetic theorem restricting the incidence patterns `s_p` that actually occur, or a genuinely joint conductor inequality that cannot be written as a nonnegative sum of independent mode costs. Merely choosing a more ingenious family of endpoint modes is insufficient.

No estimate for `M(x)` follows.

## 1. Every nonzero mode sees exactly half of all possible source columns

Fix `a\in\mathbf F_2^R\setminus\{0\}`. The map

\[
s\longmapsto a\cdot s
\]

is a nonzero linear functional on `\mathbf F_2^R`. Its kernel has size `2^{R-1}`, so exactly `2^{R-1}` vectors satisfy

\[
a\cdot s=1.
\tag{13}
\]

The zero vector is not among those solutions. Hence the same count holds when `s` ranges only over the `2^R-1` nonzero possible source columns:

\[
\#\{s\ne0:a\cdot s=1\}=2^{R-1}.
\tag{14}
\]

Average `(5)` over all nonzero `s` and exchange the two finite sums:

\[
\begin{aligned}
\frac1{2^R-1}
\sum_{s\ne0}L_{\mathcal F,w}(s)
&=
\frac1{2^R-1}
\sum_{a\in\mathcal F}w_a
\#\{s\ne0:a\cdot s=1\}\\
&=
\frac{2^{R-1}}{2^R-1}W.
\end{aligned}
\tag{15}
\]

The maximum is at least the average, proving `(6)`.

Nothing about Hamming layers, radiality, parity of `|a|`, or equal weights was used. The argument applies to a `y`-dependent family, to highly irregular subsets of modes, and to arbitrary nonnegative weights.

Sharpness is immediate. If every nonzero `a` is selected with the same weight, then for each fixed nonzero `s` the dual functional `a\mapsto a\cdot s` also takes the value `1` on exactly `2^{R-1}` nonzero vectors. Thus every source column has the common loading ratio in `(6)`.

## 2. The package-cost double count is exact for every selected family

For `a\in\mathcal F`, define the chosen package support

\[
V_a:=\mathop{\triangle}_{i:a_i=1}V_i,
\qquad
m_a:=\prod_{p\in V_a}p.
\tag{16}
\]

By `(3)`,

\[
\mathbf1_{p\in V_a}=\mathbf1_{a\cdot s_p=1}.
\tag{17}
\]

Therefore

\[
\begin{aligned}
\sum_{a\in\mathcal F}w_a\log m_a
&=
\sum_{a\in\mathcal F}w_a
\sum_{p\in U}\mathbf1_{a\cdot s_p=1}\log p\\
&=
\sum_{p\in U}L_{\mathcal F,w}(s_p)\log p.
\end{aligned}
\tag{18}
\]

Since every actual source column is nonzero by definition of

\[
U=\bigcup_iV_i,
\]

one has

\[
L_{\mathcal F,w}(s_p)
\le
c_{\mathcal F,w}W.
\tag{19}
\]

Summing `(19)` in `(18)` gives `(9)`.

If `(7)` holds for every selected mode, then

\[
hW\log y
\le
\sum_{a\in\mathcal F}w_a\log m_a
\le
c_{\mathcal F,w}W\log P,
\tag{20}
\]

and hence

\[
\log P\ge\frac h{c_{\mathcal F,w}}\log y.
\tag{21}
\]

The lower bound `(6)` on `c_{\mathcal F,w}` is therefore an **upper bound on the exponent obtainable from this proof architecture**. Combining `(6)` and `(21)` yields `(10)`.

This distinction is important. Equation `(10)` does not say that the true common radical is at most quartic. It says that a proof which knows only independent positive mode costs and protects itself against arbitrary nonzero source columns cannot certify an exponent larger than the stated ceiling by incidence averaging alone.

## 3. The pair layer already asymptotically attains the universal optimum

Take the unweighted family of all pair modes

\[
\mathcal F_2
=\{e_i+e_j:1\le i<j\le R\}.
\tag{22}
\]

For a source column `s` of Hamming weight `a`, exactly

\[
a(R-a)
\tag{23}
\]

pair modes satisfy `(e_i+e_j)\cdot s=1`. Hence

\[
c_{\mathcal F_2}
=
\frac{\max_{0\le a\le R}a(R-a)}{\binom R2}
=
\frac{\lfloor R^2/4\rfloor}{\binom R2}
=
\frac12+O(R^{-1}).
\tag{24}
\]

This is exactly the weighted Plotkin incidence constant used in `MC-324`. With the individual conductor bill `h=2-\delta`, equations `(21)` and `(24)` give the quartic limit derived there.

`MC-325` showed separately that every full sparse even Hamming layer `r=o(\sqrt R)` also has universal loading constant `1/2+o(1)`. Equation `(6)` now explains why these apparently different layers converge to the same number: `1/2` is not an accident of Krawtchouk asymptotics but the asymptotic floor for **every** universally controlled nonnegative mode family.

The full nonzero mode family attains the exact finite-`R` lower bound `(6)`, although it is not useful with the current fixed-bias analytic input because the reciprocal endpoint profile has weak or vanishing modes near the central Hamming layers. Thus the exact combinatorial optimum and the analytically useful endpoint family are distinct; the pair layer is sufficient to attain the optimum asymptotically while retaining fixed shell bias.

## 4. Weighted selection does not evade the barrier

One possible reaction to `MC-325` is to abandon complete Hamming layers and assign larger importance to especially biased or especially expensive modes. Equation `(15)` closes that generic escape.

The weights `w_a` can encode any nonnegative preference: endpoint bias, a mode-dependent proven conductor lower bound after normalization, multiplicity, or a chosen optimization weight. Because the half-space count `(14)` holds separately for every nonzero `a`, linearity gives exactly the same half-loading average for every such weighting.

The restriction `w_a\ge0` is load-bearing and matches the conductor-summing mechanism. If one knows only lower bounds

\[
\log m_a\ge h_a\log y,
\]

then positive multiplication and summation preserve those inequalities. Signed coefficients do not: subtracting one unknown conductor cost from another requires genuinely new joint information. A future signed or cancellation-based conductor identity is therefore not contradicted by this finding; it lies outside the independent-positive-bill architecture being classified.

Likewise, a proof may select only the modes that actually satisfy a desired analytic estimate. The family in `(4)` is arbitrary, so the barrier applies after such selection. Removing an `O_\delta(1)` exceptional set from the Schlage--Puchta family does not change the argument.

## 5. What remains of the sub-half-loading escape

The maximum in `(6)` ranges over **all possible nonzero source columns**. The actual package uses only the finite set

\[
S_A:=\{s_p:p\in U\}.
\tag{25}
\]

It is logically possible that arithmetic forces

\[
\max_{s\in S_A}
\frac{L_{\mathcal F,w}(s)}W
<\frac12-c
\tag{26}
\]

for some fixed `c>0`, even though another vector `s\notin S_A` has loading at least one half. Such a theorem would immediately evade the universal no-go.

But `(26)` can no longer come from the abstract choice of `\mathcal F` alone. It must use a restriction on the **actual lower-prime incidence patterns** generated by the shell-representation problem. In particular, a future proposal must identify why the high-loading vectors guaranteed by `(15)` cannot occur as `s_p`, or why they carry too little logarithmic prime mass to matter.

This sharpens the post-`MC-325` frontier. The phrase “find a family with sub-half column loading” is insufficient unless “column” explicitly means the arithmetic set `S_A`, not every abstract vector in `\mathbf F_2^R`. Without such source-specific information, pair modes already achieve the best asymptotic loading factor available.

The other genuine escape remains a joint conductor theorem. An inequality coupling several `m_a` or minimum primitive conductors in a way not representable as `(20)` could exploit algebraic relations among characters before taking positive sums. The conductor--discriminant packaging of `MC-303` is an example of a genuinely joint invariant, although generic Chebotarev loses the shell scale there; the present theorem does not rule out a stronger source-specific joint relation.

## 6. Prior art and novelty boundary

The finite-vector-space identity behind `(14)` is elementary: a nonzero linear functional on `\mathbf F_2^R` takes each value on exactly `2^{R-1}` vectors. In coding language, the same half-column count is standard in proofs of the Plotkin bound for binary linear codes: across the complete linear code, every nonzero coordinate functional is `1` on exactly half of the codewords. `MC-324` already audited Morris Plotkin, *Binary codes with specified minimum distance*, IRE Transactions on Information Theory **6** (1960), 445--450, DOI `10.1109/TIT.1960.1057584`, and used its columnwise pair-distance count.

A targeted literature search on 16 September 2026 found the standard half-coordinate/Plotkin mechanism and modern coding-theory uses of affine half-spaces separately. No new coding theorem, weighted Plotkin bound, or finite-field identity is claimed here. **No standalone novelty claim is made.**

The durable line-specific result is the optimization statement obtained by inserting the elementary half-space average into the exact source-package identity `(18)`: among all arbitrary mode families and all nonnegative reweightings, the universal source-loading constant cannot asymptotically fall below one half. Together with the near-quadratic individual conductor horizon of `MC-323`, this proves that the quartic barrier reached by `MC-324` is the asymptotic ceiling of the entire independent-positive-bill/universal-incidence architecture, not merely of pair or sparse-even Hamming layers.

## Boundaries and falsification tests

- **This is a proof-architecture ceiling, not a bound on the true radical.** A particular arithmetic package may have much larger `P`; the theorem limits what can be forced from independent positive mode costs plus a universal incidence maximum.
- **Actual-column restrictions are not ruled out.** Equation `(6)` guarantees a high-loading abstract vector, not that this vector occurs among the actual `s_p`. Any source-specific theorem excluding high-loading columns lies outside the no-go.
- **Nonnegative weights are essential.** They are exactly what allows individual conductor lower bounds to be summed safely. A signed identity or determinant/product relation with genuine cross-mode cancellation is additional information.
- **The individual analytic horizon is separate.** The numerical quartic ceiling in `(11)` uses the near-quadratic per-character conductor bill from `MC-323`. A stronger theorem forcing individual conductors above `y^{2+\eta}` would raise the ceiling proportionally.
- **Fixed bias is needed only for the current analytic specialization.** The combinatorial inequality `(6)` holds for every selected family regardless of endpoint coefficients. Which modes receive the `h=2-\delta` bill is an analytic question.
- **The exact reciprocal endpoint is not needed for `(6)`.** It enters only to supply the large fixed-bias pair family that attains the asymptotic optimum under the current arithmetic theorem.
- **No claim of finite-`R` pair optimality.** The full nonzero family attains the exact abstract constant `(6)`; the pair family is only asymptotically optimal while remaining uniformly biased for the reciprocal endpoint.
- **No estimate for the Mertens function follows.** The result closes one internal source-incidence escape and identifies the additional arithmetic information required by the next one.
