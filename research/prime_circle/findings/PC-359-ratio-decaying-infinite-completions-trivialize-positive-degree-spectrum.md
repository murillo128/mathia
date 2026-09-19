# PC-359 — ratio-decaying infinite completions trivialize positive-degree multiplier spectra

- **Finding ID:** `PC-359`
- **Status:** `EXACT-DERIVED` + `CLASSICAL-OPERATOR-THEORY` + `DECISIVE-NEGATIVE`
- **Research line:** `prime_circle`
- **Result type:** exact infinite-completion / compact weighted-shift obstruction
- **Scope:** tests the first live escape left by PC-358: a genuine infinite Prime-Circle word completion on which reciprocal parity becomes unbounded. It closes the broad scalar grade-weight regime in which every fixed positive-degree creation block decays to zero at high grade.
- **RH relevance:** high as a boundary result. This regime really escapes the bounded-similarity hypothesis of PC-358, but the same completion compactifies every norm-convergent positive-degree multiplier and forces its ordinary spectrum to collapse. Unbounded reciprocal parity by itself therefore does not produce a nontrivial RH-facing eigenvalue spectrum here.

## Claim

Let `K` be a nonzero finite-dimensional complex Hilbert space with inner product induced by a fixed positive Hermitian form `G`, and let

\[
J:K\to K,
\qquad J^2=I,
\]

be the algebraic reciprocal parity appearing in the Prime-Circle source/control signature construction of PC-355--PC-358. Consider a scalar-weighted full word completion

\[
\mathcal H_w
:=
\bigoplus_{m\ge 0}
\left(K^{\otimes m},\,w_m G^{\otimes m}\right),
\qquad w_m>0,
\tag{1}
\]

with orthogonal tensor grades.

The reciprocal parity on the algebraic finite-word core is

\[
P:=\bigoplus_{m\ge0}J^{\otimes m}.
\tag{2}
\]

Because the same scalar factor `w_m` occurs in the domain and range of grade `m`,

\[
\boxed{
\left\|P\big|_{K^{\otimes m}}\right\|
=
\|J\|_G^m.
}
\tag{3}
\]

Hence whenever `\|J\|_G>1`, `P` is genuinely unbounded on `\mathcal H_w`, independently of the scalar grade weights. This is therefore a real infinite-dimensional escape from PC-358's bounded-parity similarity theorem rather than another finite truncation in disguise.

Now let `d_k\in K^{\otimes k}` be homogeneous of degree `k\ge1`, and let

\[
L_{d_k}:K^{\otimes m}\to K^{\otimes(m+k)},
\qquad
L_{d_k}x=d_k\otimes x,
\tag{4}
\]

be left creation by `d_k`. Its exact block norm in `\mathcal H_w` is

\[
\boxed{
\left\|L_{d_k}\big|_{K^{\otimes m}}\right\|
=
\|d_k\|_{G^{\otimes k}}
\sqrt{\frac{w_{m+k}}{w_m}}.
}
\tag{5}
\]

Assume the grade weights satisfy the fixed-lag ratio-decay condition

\[
\boxed{
\frac{w_{m+k}}{w_m}\longrightarrow0
\quad(m\to\infty)
\quad\text{for every fixed }k\ge1.
}
\tag{6}
\]

Then every homogeneous positive-degree creation operator `L_{d_k}` is compact. Consequently, if

\[
Q:=\sum_{k\ge1}L_{d_k}
\tag{7}
\]

converges in operator norm, then `Q` is compact and strictly grade-raising. It follows exactly that

\[
\boxed{\sigma(Q)=\{0\}.}
\tag{8}
\]

Therefore the corresponding unital multiplier

\[
L=I+Q
\tag{9}
\]

has

\[
\boxed{\sigma(L)=\{1\}.}
\tag{10}
\]

In particular, if the Prime-Circle source multiplier and its matched reciprocal control are both bounded by norm-convergent positive-degree expansions on the same ratio-decaying completion, then each has the singleton spectrum `{1}`. No bounded similarity between them is being asserted: bounded reciprocal parity is precisely what has failed. The obstruction is stronger in a different direction -- each spectrum is already trivial separately.

## Derivation

### 1. Scalar grade weights do not tame reciprocal parity

For `x\in K^{\otimes m}`,

\[
\|x\|_{\mathcal H_w}=\sqrt{w_m}\,\|x\|_{G^{\otimes m}},
\]

while

\[
\|J^{\otimes m}x\|_{\mathcal H_w}
=
\sqrt{w_m}\,\|J^{\otimes m}x\|_{G^{\otimes m}}.
\]

The scalar weight cancels, and the Hilbert tensor norm gives

\[
\|J^{\otimes m}\|=\|J\|_G^m,
\]

proving (3). Since `J` is an involution, `\|J\|_G\ge1`; if it is strictly larger than one, the block norms diverge exponentially and `P` has no bounded extension to `\mathcal H_w`.

Thus scalar grade weighting does not merely preserve the finite obstruction of PC-358. It produces the opposite operator-theoretic regime: the algebraic source/control intertwiner survives on the finite-word core but is unbounded in the completed Hilbert space.

### 2. The same weights can compactify every positive-degree creation block

For `x\in K^{\otimes m}`,

\[
\|d_k\otimes x\|_{\mathcal H_w}^2
=
w_{m+k}\,\|d_k\|_{G^{\otimes k}}^2\|x\|_{G^{\otimes m}}^2,
\]

whereas

\[
\|x\|_{\mathcal H_w}^2
=
w_m\|x\|_{G^{\otimes m}}^2.
\]

This proves (5). Under (6), the block norms tend to zero with `m`; because a convergent scalar sequence is bounded, each `L_{d_k}` is also bounded.

Let `L_{d_k}^{(M)}` agree with `L_{d_k}` on input grades `0,\ldots,M` and vanish above grade `M`. Its range lies in a finite direct sum of finite-dimensional tensor powers, so it has finite rank. Moreover,

\[
\|L_{d_k}-L_{d_k}^{(M)}\|
=
\|d_k\|
\sup_{m>M}
\sqrt{\frac{w_{m+k}}{w_m}}
\longrightarrow0.
\tag{11}
\]

Hence `L_{d_k}` is compact.

A simple concrete completion is

\[
w_m=\frac1{m!},
\tag{12}
\]

for which

\[
\sqrt{\frac{w_{m+k}}{w_m}}
=
\sqrt{\frac{m!}{(m+k)!}}
\longrightarrow0.
\tag{13}
\]

Thus the factorial completion simultaneously leaves reciprocal parity unbounded when `\|J\|_G>1` and makes every fixed positive-degree creation operator compact.

### 3. Compactness plus strict grade raising forces quasinilpotence

If the series (7) converges in operator norm, then `Q` is a norm limit of finite sums of compact operators and is therefore compact.

Strict grade raising alone is not enough to conclude quasinilpotence: the unilateral shift is the standard counterexample. Compactness is the additional load-bearing fact here.

Suppose `Qx=\lambda x` with `x\ne0` and `\lambda\ne0`. Because tensor grades are indexed by the nonnegative integers, `x` has a least occupied grade `m_0`. Every term of `Q` raises degree by at least one, so the grade-`m_0` component of `Qx` is zero. The grade-`m_0` component of `\lambda x` is nonzero, a contradiction. Therefore `Q` has no nonzero eigenvalues.

For a compact operator on an infinite-dimensional complex Hilbert space, every nonzero spectral value is an eigenvalue. Hence `Q` has no nonzero spectral values at all, proving (8). Spectral translation then gives (10).

## What this closes relative to PC-358

PC-358 leaves a genuine infinite-completion escape: if reciprocal parity ceases to be bounded, the finite-dimensional similarity argument no longer controls the completed operators.

The present calculation shows that one broad and natural way of entering exactly that regime does **not** rescue the ordinary spectrum. Scalar grade weights cannot bound parity, and if those weights decay strongly enough that every fixed positive-degree creation block vanishes asymptotically, then all norm-convergent positive-degree multipliers become compact quasinilpotents. Source and matched control can fail to be boundedly similar while still having the same completely uninformative singleton spectrum.

The important distinction is therefore

\[
\text{unbounded reciprocal parity}
\not\Rightarrow
\text{nontrivial spectral separation}.
\tag{14}
\]

A useful infinite completion has to do more than invalidate bounded similarity: it must retain enough high-grade transport that the natural multiplier itself has nontrivial spectral content.

## Prior-art and novelty audit

The abstract ingredients here are classical operator theory: homogeneous creation maps on graded Hilbert spaces are weighted shifts; block weights tending to zero give compact operators; and a compact operator has no nonzero spectral point unless that point is an eigenvalue. Weighted-shift theory has treated these mechanisms for decades. No novelty is claimed for those facts, for compact quasinilpotence, or for the singleton spectrum of `I+Q` once compactness and strict grade raising are established.

The research-specific delta is the exact Prime-Circle tradeoff exposed by combining those classical facts with the reciprocal-parity obstruction of PC-355--PC-358: **the first obvious infinite-dimensional escape from bounded reciprocal similarity can be realized, but a large natural class of completions that regularizes positive-degree multiplication destroys the desired spectrum at the same time.** This is a boundary result for the Prime-Circle representation problem, not a new theorem about weighted shifts.

Prior-art searches were therefore aimed at weighted shifts, compact weighted shifts, graded/Fock multiplication, and compact-operator spectra rather than at wording specific to Prime-Circle. They support the classification `CLASSICAL-OPERATOR-THEORY` for the functional-analytic mechanism and do not reveal an independent RH mechanism hiding in this completion.

## Boundary conditions and surviving frontier

This is not a universal no-go for infinite completions. The proof uses all of the following:

1. a scalar grade-weighted tensor Hilbert structure as in (1);
2. positive-degree **left multiplication** as the spectral operator;
3. fixed-lag ratio decay (6), which compactifies every homogeneous creation block;
4. operator-norm convergence of the full positive-degree expansion.

Accordingly, the following regimes remain open and are not covered by PC-359:

- weights with nonzero asymptotic fixed-lag ratios, where creation can remain bounded but noncompact;
- unbounded or merely closed multipliers whose domains carry source/control information;
- Hilbert structures that couple tensor grades non-scalarly rather than through one number `w_m` per grade;
- operators containing same-grade, backward, or genuinely two-sided couplings rather than pure positive-degree creation;
- naturally forced observables that are not similarity-invariant ordinary spectra, provided they are not introduced as arbitrary spectral wrappers.

The next useful infinite-completion test should therefore target the **borderline noncompact regime**, not stronger decay. For example, geometric weights with `w_{m+1}/w_m\to r>0` preserve a nonzero asymptotic creation scale and evade the compactness proof above while reciprocal parity remains unbounded whenever `\|J\|_G>1`.

## Falsification / audit test

The finding is exact under its stated hypotheses. A counterexample must violate at least one step above. The decisive audit is to produce positive weights satisfying (6) and a norm-convergent positive-degree multiplier `Q` for which either:

- some homogeneous block `L_{d_k}` is noncompact despite (5), or
- `Q` has a nonzero spectral value without a nonzero eigenvalue despite compactness, or
- `Q` has a nonzero eigenvalue despite strict grade raising.

Any such example would contradict standard Hilbert-space operator theory and would refute the finding. In contrast, a noncompact borderline weighting or an unbounded-domain construction is not a counterexample; it lies outside the theorem and is precisely part of the surviving frontier.

## Formalization handoff

No automatic Lean handoff is warranted. The proof is exact but its core is standard infinite-dimensional compact-operator theory, while formalizing the weighted Hilbert direct sum and compact spectral theorem would introduce substantial analytic infrastructure without exposing a presently unclear finite structural boundary. The result is better used as a research boundary than as a bounded formalization target.