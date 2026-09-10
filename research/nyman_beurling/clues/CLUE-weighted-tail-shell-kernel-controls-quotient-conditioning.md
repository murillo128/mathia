---
id: CLUE-weighted-tail-shell-kernel-controls-quotient-conditioning
type: research-clue
status: proposed
origin: independent-review
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-033-polylogarithmic-tail-skeleton-preserves-relative-distance-and-mobius-core.md
  - research/nyman_beurling/formalization/NB033TailQuotient.lean
  - research/nyman_beurling/findings/NB-031-moving-tail-adjacent-sectors-are-gram-whitened-target-poor.md
  - research/nyman_beurling/findings/NB-020-early-shell-mobius-inversion-forces-an-inverse-distance-coefficient-core.md
  - research/nyman_beurling/findings/NB-029-adjacent-differences-have-the-full-nyman-closure.md
---

# Can the early-shell kernel give a uniformly conditioned, source-faithful tail quotient?

## Observation

The approved [NB-033 Lean artifact](https://github.com/murillo128/mathia/blob/59e38a8da8f1d076c87bd315c0a93592fb4913cd/research/nyman_beurling/formalization/NB033TailQuotient.lean) proves a generic path quotient through `tailSpace_eq_ker`, `coefficientQuotientEquiv`, `skeletonEquiv`, and `coefficient_pushforward`. It forgets the relation that generates the actual arithmetic family. Canonical findings were inspected at `167d82a451f71a4024cca5eec5b9d2bd30d3dd66`; no adjacent review sidecars were present for these sources.

NB-031 supplies that lost relation: on the harmonic shell

\[
I_t=(1/(t+1),1/t],\qquad g_n|_{I_t}=t/n\quad(t<M\le n).
\]

Ordinary tail differences retain a rank-one early-shell profile. Rescaling the tail generators to \(f_n=ng_n\) instead suggests differences

\[
\widehat h_n=ng_n-(n+1)g_{n+1},\qquad
\widehat W_{M,N}=\operatorname{span}(\widehat h_M,\ldots,\widehat h_{N-1}),
\]

which vanish on every shell with \(t<M\). This changes the discarded subspace; it is not merely a basis change inside NB-033's original tail space.

## Research question

For \(2\le M\le N\), put \(V_N=\operatorname{span}(g_2,\ldots,g_N)\), \(\widehat Q=I-P_{\widehat W_{M,N}}\), and

\[
\widehat K_{M,N}=V_N\cap\widehat W_{M,N}^{\perp},\qquad
\widehat k_j=\widehat Qg_j\quad(2\le j\le M).
\]

Can one establish the following combined source-to-quotient theorem, including a quantitative lower Gram bound uniform in the upper endpoint \(N\)? The proposed normal form is

\[
\widehat W_{M,N}
=\ker(R_M|_{V_N}),\qquad
R_Mv=(v|_{I_t})_{1\le t<M},
\]

with quotient coordinates

\[
\widehat Q\sum_{n=2}^N a_ng_n
=\sum_{n=2}^{M-1}a_n\widehat k_n
+\left(M\sum_{n=M}^N\frac{a_n}{n}\right)\widehat k_M.
\tag{1}
\]

Thus the proposed basis preserves every head coefficient but retains a harmonic weighted tail sum. If \(\widehat H_{M,N}\) is its Gram matrix, define the explicit matrix

\[
(B_M)_{ij}=\sum_{t=1}^{M-1}
\frac{\{t/i\}\{t/j\}}{t(t+1)}
\quad(2\le i,j\le M).
\]

The decisive metric candidate is

\[
B_M\preceq\widehat H_{M,N}\preceq G_M,
\qquad \lambda_{\min}(B_M)\ge cM^{-4}
\tag{2}
\]

for an absolute \(c>0\), where \(G_M\) is the full Hilbert Gram matrix of \(g_2,\ldots,g_M\). This would give \(\operatorname{cond}_2(\widehat H_{M,N})=O(M^4\log M)\) in these specified, unnormalized source coordinates, independently of \(N\).

## Why it may matter

Early-shell vanishing suggests \(\|P_{\widehat W_{M,N}}e\|^2\le1/M\) for \(e=1\). With the usual orthogonal distance identity and NB-033's Burnol floor, a predeclared cutoff \(M_N/\log N\to\infty\), \(M_N\le N\), would suffice for relative distance preservation. The unchanged head would still contain the forced Möbius core. Equation (2) would additionally replace the original quotient's uncontrolled dependence on the full tail by an explicit conditioning bound in the retained dimension. Forming the projected basis may still require the full section; neither claim supplies a faster construction or a better Nyman approximation rate.

## Decisive test

First prove the kernel equality, including \(M=2\) and \(M=N\). Weighted edges have zero early restriction. Conversely, NB-020's triangular divisor inversion should force every head coefficient of an early-shell-null vector to vanish; its first shell should then force \(\sum_{n=M}^N a_n/n=0\). Apply the generic checked quotient to the family with unchanged head and rescaled tail, carefully converting its final basis vector \(Mg_M\) back to \(g_M\) in (1).

Next verify (2) in the full Hilbert norm. The early restriction of \(\widehat Qg_j\) should equal that of \(g_j\), giving the lower inequality, while orthogonal contraction gives the upper one. For the quantitative step, let \(v_t=\sum_{j=2}^M c_j\{t/j\}\), set \(v_0=0\), and put

\[
\delta^2=\sum_{t<M}\frac{|v_t|^2}{t(t+1)}.
\]

Test the inversion bounds

\[
|c_n|\le2\delta\sigma(n)\quad(2\le n<M),\qquad
c_M=M\left(v_1-\sum_{n=2}^{M-1}c_n/n\right).
\]

The elementary sums \(\sum_{n<M}\sigma(n)\le M^2\) and \(\sum_{n<M}\sigma(n)/n\le2M\) suggest \(\|c\|_2\le C M^2\delta\), which would establish the claimed bound. Check all constants and the complex case. An exact counterexample to the kernel, coordinate, or Gram comparison kills the corresponding claim; numerical conditioning alone cannot establish uniformity.

Finally identify the construction with \(\widehat K_{M,N}=P_{V_N}E_M\), where \(E_M\) is the span of the first \(M-1\) shell indicators. This tests the classical finite-observation projection explanation rather than treating an abstract quotient as new mathematics. The residual contribution to assess is the explicit arithmetic kernel, preserved coordinates, and uniform quantitative Gram bound together. Compare them with existing finite Nyman conditioning results before accepting a substantive extension. Keep the target pairings and full tail norm when translating these statements into a distance certificate.

## Evidence boundary

This remains a proposed source specialization and metric extension. The generic field quotient, independent-family basis, and projection identities are covered by Lean; applying them after nonzero rescaling is algebraically legitimate. Lean does not formalize fractional-part generators, their early-shell relation, the kernel identification with shell observations, (2), Burnol's bound, or any resulting asymptotic estimate. The displayed derivation leads require the owning Research Watch's independent verification and prior-art audit before becoming a finding.

Exact rational finite checks for all \(2\le M\le N\le24\) confirmed early-shell annihilation, the required matrix ranks, retained-matrix invertibility, and the factor \(M/n\) in (1). They do not verify the infinite Hilbert Gram matrix or asymptotic claims. The bounded neighborhood and local/global clue checks did not identify this combined question. [Bagchi's primary paper](https://arxiv.org/abs/math/0607733) supplies the weighted sequence realization and classical totality/Gram context; the bounded comparison did not locate this specific weighted-tail conditioning statement. No priority claim follows from that search.

NB-029 already explains the disappearance of the original unweighted endpoint in Hilbert closure, so that observation is not a separate clue. Its vanishing-generator telescope cannot simply be applied to the rescaled sequence \(ng_n\). The proposed quotient uses a different nuisance sector, and no improvement of \(d_N\), Gram-whitened Möbius occupation theorem, efficient projector algorithm, or evidence for RH is asserted.
