# WI-160 — the corrected BGSTB proof splits the prefix form-factor error but not the dyadic error

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-RIGIDITY`.

The current author correction to Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh materially changes the provenance of the pointwise Montgomery input used in WI-157--WI-159. The published 2024 Theorem 1 stated a multiplicative error for the sum over `0 < gamma,gamma' <= T`; in the current `arXiv:2501.14545v3` the same authors explicitly say that statement is incorrect and repair the proof. Crucially, the repaired **prefix** calculation proves a stronger split estimate before they deliberately degrade it, and that stronger first line is exactly the arithmetic shape used in WI-157. The corresponding **dyadic** sum over `T < gamma,gamma' <= 2T`, however, is only proved with the degraded first-term error.

Thus the changing-test gate of WI-157 survives, but its load-bearing primary-source anchor is the corrected prefix equation (3.5) in the 2026 paper, not the published 2024 theorem statement. One must not silently transfer the same `O(1)e^{-2L alpha}` spike error to the dyadic form factor.

No new zero proportion follows from this provenance repair.

## 1. What the 2024 statement got wrong

Write

\[
L:=\log T.
\]

The 2024 Acta Arithmetica theorem stated, in its normalization, a formula equivalent to

\[
\mathcal F_{(0,T]}(x)
=
\left(
\frac{T}{2\pi x^2}L^2
+
\frac{T}{2\pi}\log x
\right)
\left(1+O(L^{-1/2})\right)
\qquad (1\le x\le T).
\tag{1}
\]

In Section 3 of `arXiv:2501.14545v3` the same authors explicitly identify this as incorrect. They note that taking `x=c log T` would create an incorrect `c`-dependent term of order `T`, thank Ramūnas Garunkštis and Julija Paliulionytė for pointing out the issue, and then give a corrected proof.

This matters for WI-157--WI-159 because the multiplicative form (1) does **not** by itself imply the split spike error used there. After normalization it only allows an error of size `O(sqrt(L) e^{-2L alpha})` near the support edge.

## 2. The corrected prefix proof proves the stronger split estimate that WI-157 needs

For the original prefix sum, the corrected proof obtains its equation (3.5):

\[
\boxed{
\mathcal F_{(0,T]}(x)
=
\frac{T}{2\pi x^2}\bigl(L^2+O(L)\bigr)
+
\frac{T}{2\pi}\log x
+
O(T\sqrt L)
}
\qquad (1\le x\le T).
\tag{2}
\]

The paper then deliberately degrades the first error term to obtain a simpler displayed Montgomery theorem. For the changing-test question that degradation is not harmless: the first line (2) is the stronger information.

Put `x=T^alpha` and normalize by `(T/(2 pi))L`. Then (2) gives, uniformly for `0<=alpha<=1`,

\[
\boxed{
F_T^{\mathrm{pre}}(\alpha)
=
L e^{-2L\alpha}
+\alpha
+O(e^{-2L\alpha})
+O(L^{-1/2}).
}
\tag{3}
\]

Equivalently,

\[
F_T^{\mathrm{pre}}(\alpha)
=e^{-2L\alpha}(L+O(1))
+\alpha+O(L^{-1/2}),
\tag{4}
\]

which is exactly the pointwise split used in WI-157 and in the countermodels of WI-158--WI-159.

The source of the `O(L)` error in the first coefficient is visible in the repaired proof itself: its `M_1` term is

\[
M_1=\frac{T}{x^2}(L^2+O(L)),
\]

while the prime-side `M_2` term contributes `T log x+O(T sqrt L)`. The mixed and `A_3` terms are then absorbed without enlarging the prefix spike error beyond `O(TL/x^2)`.

## 3. The WI-157 changing-test norm gate therefore remains valid for the prefix sum

Let `r_L` be a real support-one changing test. Pairing the two errors in (3) gives the deterministic bound

\[
\begin{aligned}
\left|2\int_0^1 O(e^{-2L\alpha})r_L(\alpha)\,d\alpha\right|
&\ll \frac{\|r_L\|_\infty}{L},\\
\left|2\int_0^1 O(L^{-1/2})r_L(\alpha)\,d\alpha\right|
&\ll \frac{\|r_L\|_1}{\sqrt L}.
\end{aligned}
\tag{5}
\]

Hence the sufficient uniformity gate recorded in WI-157 is still justified:

\[
\boxed{
\|r_L\|_\infty=o(L),
\qquad
\|r_L\|_1=o(\sqrt L)
\Longrightarrow
\text{integrated arithmetic error}=o(1).
}
\tag{6}
\]

This is a source-provenance repair, not a new improvement of the gate. The split estimate required to prove (6) is genuinely present in the corrected argument; it simply is not the theorem statement that WI-157 previously named as its source.

WI-158 and WI-159 also survive this correction. Their adversarial model errors are only `O(L^{-1/2})` pointwise and therefore satisfy the stronger split envelope (3), not merely the weaker degraded theorem. Their logical conclusion — generic pointwise size, nonnegativity, analyticity, and square structure do not control a singular changing test — is unchanged.

## 4. The dyadic form factor has a strictly weaker source-level gate

The current 2026 paper defines its main dyadic form factor using zeros with

\[
T<\gamma,\gamma'\le2T.
\]

For this dyadic sum it proves

\[
\mathcal F_{(T,2T]}(x)
=
\frac{TL^2}{2\pi x^2}
\left(1+O(L^{-1/2})\right)
+
\frac{T}{2\pi}\log x
+O(T\sqrt L),
\tag{7}
\]

uniformly for `1<=x<=T`. After normalization,

\[
F_T^{\mathrm{dyad}}(\alpha)
=
L e^{-2L\alpha}+\alpha
+O(\sqrt L\,e^{-2L\alpha})
+O(L^{-1/2}).
\tag{8}
\]

The same crude dual-norm argument now gives only

\[
\boxed{
\text{dyadic integrated error}
\ll
\frac{\|r_L\|_\infty}{\sqrt L}
+
\frac{\|r_L\|_1}{\sqrt L}.
}
\tag{9}
\]

Thus the source-level sufficient gate for a changing dyadic test is

\[
\|r_L\|_\infty=o(\sqrt L),
\qquad
\|r_L\|_1=o(\sqrt L),
\tag{10}
\]

unless one proves additional cancellation or recovers a split dyadic spike estimate by another argument.

This distinction is load-bearing for future work because the canonical `weil_inertia` line often works on dyadic height windows. A prefix changing-test argument may use (3); a dyadic argument may not cite (3) without an explicit transfer theorem.

## 5. Independent contemporary check from Lamzouri's proof

Lamzouri's current `arXiv:2609.02882v1` quotes the **fixed-test** pair-correlation formula as Lemma 3.1 (Lemma 5 of BGSTB24), then explicitly observes that the deweighting identity would require a `T`-dependent test and therefore cannot be inserted into that fixed-test lemma without an additional uniformity argument. His proof avoids this issue by expressing the desired kernel as a linear combination of two fixed test functions.

This independently confirms the logical boundary relevant here: changing-test uniformity is an extra quantitative question, not an automatic consequence of the fixed-test pair-correlation lemma. WI-157 answers that question for families satisfying (6) by using the corrected pointwise prefix estimate (3); WI-158--WI-159 show why the boundary cannot be removed from pointwise information alone.

## 6. Prior-art and novelty audit

Primary correction: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, arXiv:2501.14545v3, last revised 1 Sep 2026. Section 3 explicitly corrects the proof and statement inherited from BGSTB24; equation (3.5) is the repaired prefix estimate (2), while the paper's Montgomery theorem and the subsequent dyadic calculation use the degraded error (7).

Original source being corrected: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376, arXiv:2306.04799.

Contemporary independent use: Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 Sep 2026), especially Lemma 3.1 and the discussion immediately following it.

No novelty claim is made for the corrected Montgomery estimate; it is the authors' own repair. The Mathia contribution recorded here is the exact normalization and scope audit showing which part of the corrected source validates WI-157--WI-159 and which dyadic transfer remains unavailable.

## Evidence boundary

Equations (2), (7), and the statement that the 2024 theorem is incorrect are literature-backed by the current author correction. Equations (3)--(6) and (8)--(10) are exact normalizations and elementary dual-norm consequences. No claim is made that the dyadic spike error in (7) is sharp, only that the current cited source does not provide the stronger prefix split there. No new unconditional proportion is claimed.