# WI-230 — Lamzouri v2 charges repeated off-line mass but not simple off-line mass

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

Lamzouri's arXiv:2609.02882v2, revised 8 September 2026, adds two unconditional inequalities that were absent from v1: Proposition 2.1(2.6)--(2.7), yielding Theorem 1.1's `88.76%` lower bound for zeros that are simple or on the critical line and the `83.62%` lower bound for the average of the simple-zero and critical-line proportions. These additions have an exact interpretation that is more useful for the Weil-inertia defect program than the headline percentages.

Let `N` be the cardinality of Lamzouri's finite conjugation-invariant multiset counted with multiplicity, let `s` be its number of simple real elements, let

\[
Q:=\sum_{z,w\in\mathcal Z}K(z-w)^2,
\]

and let

\[
E_{\rm nr}^{\ge2}
:=\sum_{\substack{z\in\mathcal Z\\z\notin\mathbb R,\ m_z\ge2}}1
\]

count, with multiplicity, the non-real elements whose multiplicity is at least two. Then Lamzouri's new inequality (2.6) is equivalent to

\[
\boxed{
E_{\rm nr}^{\ge2}
\le
\Delta_{\rm sr}
:=Q-(2N-s).
}
\tag{A}
\]

Here `Delta_sr>=0` is exactly the slack in his original simple-real inequality (2.4), `s>=2N-Q`. Thus **near equality in the simple-real Montgomery--Taylor bound forces repeated off-line mass to disappear**. The new union inequality (2.7) gives, whenever `Q<=AN` with `1<=A<2`, the independent global estimate

\[
\boxed{
E_{\rm nr}^{\ge2}
\le
\frac{2(A-1)}{3+2\sqrt2}\,N.
}
\tag{B}
\]

At the unconditional Montgomery--Taylor limit `A=C_MT=2-C_0`, this is

\[
\limsup_{T\to\infty}
\frac{E_{\rm off}^{\ge2}(T)}{N(T)}
\le 1-C_2
=0.112379991826\ldots,
\tag{C}
\]

where

\[
C_0=\frac32-\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right),
\qquad
C_2=\frac{1+2\sqrt2+2C_0}{3+2\sqrt2}
=0.887620008173\ldots.
\]

The load-bearing limitation is equally exact: **simple non-real elements cancel from both (A) and (B)**. Consequently the new v2 rigidity cannot by itself rule out the live confluence/sparse-screen escape, because those screens may be made from simple off-line conjugate pairs. WI-140 already supplies a finite admissible control in which a simple non-real conjugate pair approaches the real axis and the original simple-real deficit tends to zero while every point remains off-real. Lamzouri v2 does not change that control: `E_nr^{>=2}=0` identically. The new theorem therefore removes multiplicity as a possible hiding place near saturation, but it leaves the genuinely RH-facing obstruction concentrated in **simple off-line mass**.

No unconditional simple-critical-zero proportion is improved here.

## 1. Primary-source contract and provenance

The primary source is Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v2, revised 8 September 2026:

- https://arxiv.org/abs/2609.02882
- https://arxiv.org/html/2609.02882v2

The v2 abstract and Theorem 1.1 state four unconditional asymptotic conclusions. The two inherited from v1 are

\[
\liminf\frac{N_0^s(T)}{N(T)}\ge C_0=0.6725007\ldots,
\qquad
\liminf\frac{N_d(T)}{N(T)}\ge C_1=\frac{1+C_0}{2}=0.83625\ldots.
\]

The two additions are

\[
\boxed{
\liminf\frac{N_{s\cup0}(T)}{N(T)}\ge C_2=0.88762\ldots
}
\tag{1}
\]

and

\[
\boxed{
\liminf\frac{N_s(T)+N_0(T)}{2N(T)}\ge C_1=0.83625\ldots.
}
\tag{2}
\]

Here `N_s` counts simple zeros, `N_0` critical-line zeros with multiplicity, and `N_{s union 0}` zeros that are simple or lie on the critical line, counted with multiplicity.

The finite source is Proposition 2.1. For `lambda>0`, a real even `eta in L^2(R)` supported in `(-lambda,lambda)` with `widehat(eta^2)(0)=1`, and a nonempty finite conjugation-invariant multiset `Z`, put `K=widehat(eta^2)` and `Q=sum K(z-w)^2`. In addition to the v1 inequalities for simple real and distinct elements, v2 proves

\[
N_s(\mathcal Z)+N_{\mathbb R}(\mathcal Z)\ge3N-Q,
\tag{3}
\]

and, if `Q<=AN`, `1<=A<2`,

\[
N_{s\cup\mathbb R}(\mathcal Z)
\ge
\frac{5+2\sqrt2-2A}{3+2\sqrt2}N.
\tag{4}
\]

The proof remains Lamzouri's nested-subspace/Bessel argument. For (3), v2 splits non-real distinct elements into simple and repeated pairs and combines the resulting lower bound on the `U`-sector mass with the three spectral ranges of the Bessel coefficients. For (4), it introduces `t>2`, balances the three coefficient weights, and the exact balance equation `t^2-4t+2=0` selects `t=2+sqrt(2)`.

The zeta specialization still uses the unconditional pair-correlation formula of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (Lamzouri's Lemma 3.1, cited there as Lemma 5 of their paper), followed by the Montgomery--Taylor extremal family. Thus (1)--(2) are unconditional modulo no RH or narrow-box assumption.

As of this audit, the public `AxiomMath/ZetaZeros` README and challenge still advertise/formalize the v1-level simple-critical and distinct-zero conclusions, not the two new v2 additions. The new claims are therefore treated here as primary-preprint mathematics independently checked at the algebraic interface, not as already Lean-certified artifacts.

## 2. Exact category bookkeeping gives the slack identity

Partition the labels of `Z` into four disjoint populations:

\[
s=\#\{\text{simple real labels}\},
\quad
a=\#\{\text{simple non-real labels}\},
\]

\[
r=\#\{\text{repeated real labels}\},
\quad
e=\#\{\text{repeated non-real labels}\},
\tag{5}
\]

where `r` and `e` count with multiplicity. Then

\[
N=s+a+r+e,
\qquad
N_s=s+a,
\qquad
N_{\mathbb R}=s+r.
\tag{6}
\]

Therefore

\[
\boxed{N_s+N_{\mathbb R}=N+s-e.}
\tag{7}
\]

Substitute (7) into Lamzouri's new finite inequality (3):

\[
N+s-e\ge3N-Q.
\]

Rearranging gives exactly

\[
e\le Q-2N+s=\Delta_{\rm sr},
\tag{8}
\]

which is (A). No asymptotic, optimization, or inequality beyond Lamzouri's (3) has been added. His old simple-real inequality gives `s>=2N-Q`, so the right side in (8) is manifestly nonnegative.

The same conclusion is independently compatible with the older Mathia slack reconstruction. WI-137 writes `Delta_sr` as a sum of nonnegative operator/source terms including `4 E_C`, where `E_C=sum(m_z-1)` over non-real conjugate pairs. For every repeated non-real pair of multiplicity `m>=2`, its `2m` labels obey `2m<=4(m-1)`. Hence the previously reconstructed exact slack already implies `e<=4E_C<=Delta_sr`. Lamzouri v2 now exposes the same multiplicity rigidity directly at the published finite-inequality level; this finding does not claim priority for (8).

## 3. The union theorem is exactly a repeated-off-line bound

The complement of the simple-or-real population is not an unspecified exceptional set. By (5)--(6),

\[
N_{s\cup\mathbb R}=N-e.
\tag{9}
\]

Consequently (4) is algebraically equivalent to

\[
\boxed{
e\le
\frac{2(A-1)}{3+2\sqrt2}N,}
\tag{10}
\]

which is (B). After zeta specialization, `e` becomes exactly the number of zeros that are simultaneously off the critical line and of multiplicity at least two, counted with multiplicity. This is Lamzouri's interpretation in Remark 1.2; the exact finite rewrite (10) simply makes the controlled population explicit.

At the Montgomery--Taylor source value

\[
\frac{Q_T}{N(T)}\to C_{\rm MT}=2-C_0
=1.327499296320\ldots,
\tag{11}
\]

(10) yields

\[
\frac{e}{N}
\le
\frac{2(1-C_0)}{3+2\sqrt2}+o(1)
=1-C_2+o(1),
\tag{12}
\]

which is (C). Numerically the unconditional ceiling is `0.112379991826...`.

This is genuinely stronger for repeated off-line mass than what follows by discarding all other populations from WI-170's v1 joint budget `O+2M<=Q-N`: a double off-line pair pays at least two units of that budget per repeated off-line label, giving only the coarser marginal ceiling `(C_MT-1)/2=(1-C_0)/2=0.163749648160...`. The v2 union inequality therefore contributes new finite Hilbert-space information; it is not merely a restatement of the v1 distinctness estimate.

## 4. Near extremality removes repeated off-line mass

The strongest RH-facing content is not the fixed `11.24%` ceiling but (8). Under the Montgomery--Taylor family, suppose a sequence of zeta windows is near-extremal for the simple-critical inequality in the precise sense

\[
\frac{Q_T}{N(T)}=2-C_0+o(1),
\qquad
\frac{N_0^s(T)}{N(T)}=C_0+\varepsilon_T.
\tag{13}
\]

Then (8) gives

\[
\boxed{
\frac{E_{\rm off}^{\ge2}(T)}{N(T)}
\le\varepsilon_T+o(1).
}
\tag{14}
\]

In particular, if the simple-critical lower bound is asymptotically sharp (`epsilon_T->0`), the multiplicity-weighted population of repeated off-line zeros has density zero. Any macroscopic off-line population surviving in such a near-extremizer must therefore consist asymptotically of **simple** off-line pairs.

This is exactly the separation requested by the Weil-inertia mandate. Multiple critical-line zeros are not being relabeled as off-line defect; repeated off-line zeros are isolated as `E_off^{>=2}`; and the remaining simple off-line population is left explicit rather than absorbed into proof slack.

## 5. Decisive control: simple off-line confluence survives unchanged

The new inequalities do not charge simple non-real labels `a`. This is not merely a bookkeeping concern. WI-140 gives the canonical finite Lamzouri control: an isolated simple non-real conjugate pair approaching the real axis. With its notation `t(y)=||h_y||^2`, one has

\[
N=2,
\qquad
s=0,
\qquad
Q-4=8t+8t^2,
\qquad
t(y)\to0.
\tag{15}
\]

Both elements are non-real and simple, so

\[
e=0,
\qquad
N_s=2,
\qquad
N_{\mathbb R}=0.
\tag{16}
\]

For the original inequality (2.4), the deficit is

\[
\Delta_{\rm sr}=Q-4=8t+8t^2\to0.
\tag{17}
\]

For the new (2.6), the right side is

\[
3N-Q=2-8t-8t^2,
\tag{18}
\]

while the left side is `N_s+N_R=2`. Thus (2.6) also tends to equality as the entire population remains simple and off-real. The new rigidity correctly sees no contradiction because its charged population `e` vanishes identically.

The union inequality (2.7) is structurally blind for the same reason: every simple off-line zero belongs to the union `simple or real`. In any configuration with no repeated off-line zeros, `N_{s union R}=N` regardless of how much simple off-line mass is present. Hence even where the `Q<2N` hypothesis of (2.7) is available globally, its left side cannot distinguish a simple off-line pair from a simple critical zero.

This closes a tempting reaction to the v2 headline: the `88.76%` theorem is **not** an `88.76%` near-RH statement. Its `11.24%` complement is precisely repeated off-line mass, not all off-line mass. The live WI-211/WI-212 sparse-screen mechanisms may use simple off-line conjugate pairs and therefore evade both new inequalities.

## 6. Prior-art and novelty audit

Lamzouri v2 is the primary source for (3)--(4), their zeta consequences, and the interpretation that zeros simultaneously off-line and multiple have proportion at most `1-C2`. The paper explicitly compares its two new estimates with the earlier narrow-box horizontal-multiplicity results of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh; in the `b->0` conditional narrow-box regime those authors obtain the same `C1` average bound and the slightly stronger union value `(2+C0)/3=0.89083...`. Those conditional estimates are not used as unconditional evidence here.

Mathia's pre-v2 WI-137 already reconstructed the complete nonnegative slack in Lamzouri's simple-real inequality, and WI-170 extracted the exact v1 joint budget separating off-line labels and multiplicity excess. Equation (8) is therefore best viewed as a newly published direct route to a rigidity that was already latent in the local exact slack, not as a new theorem claim. What is genuinely new in the prior-art landscape is Lamzouri's finite inequality (2.7) and its stronger unconditional `11.24%` repeated-off-line ceiling.

The novelty in this finding is the line-specific audit: identifying the exact population controlled by each new v2 inequality, comparing that control to WI-137/WI-170, and testing it against the already established simple off-line confluence countermodel. No priority claim is made for elementary rewrites (7)--(10).

A search of the current public `AxiomMath/ZetaZeros` challenge found only the original simple-critical and distinct-zero theorem surface. If that formalization is updated to include v2 (2.6)--(2.7), it would upgrade the mechanical evidence tier for the source theorem but would not alter the structural conclusion here.

## 7. Consequence for the research line

Lamzouri v2 materially narrows the exceptional geometry: **repeated off-line zeros cannot carry a near-extremal simple-real deficit, and unconditionally they occupy at most `11.238...%` of the Montgomery--Taylor population.** This removes repeated off-line multiplicity as a plausible dominant explanation for sharpness.

It does not supply the missing defect-to-zero bootstrap. The remaining hard branch is sharper than before: one must charge or exclude **simple off-line conjugate pairs** by source-sensitive information, nonlocal screen complexity, a statistic not invariant under confluence, or genuinely stronger correlation/support input. The current source-fixed bow/covariance program remains aimed at exactly that population.

A future result claiming that Lamzouri v2 alone forces RH, density-one criticality, or vanishing total off-line mass is falsified by the category identity (9) and the WI-140 simple-pair confluence control unless it introduces an additional hypothesis that independently charges simple non-real points.