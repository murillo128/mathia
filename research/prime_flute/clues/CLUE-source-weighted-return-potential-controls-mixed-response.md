---
id: CLUE-prime-flute-source-weighted-return-potential-controls-mixed-response
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit.md
  - research/prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md
---

# Can a source-weighted return potential control row proliferation in the actual mixed response?

## Observation

PF-296 proves that the canonical fixed-axis synthesis Y_(s,r) is uniformly bounded from ell^1(q) to physical-axis H^(1/2), where q_i is the explicit conserved row weight and q_i asymp i+1. The canonical seam ratios lie in the permitted bounded-ratio range. Consequently a bounded weighted source moment rules out the local frequency escape tested by PF-290, provided the complete normalized response really factors through that synthesis and the controlled transports.

The missing input is not another fixed-row regularity estimate. It is how repeated neighboring-pant/Schur recoupling populates those rows after the physical energy normalization. A possible discriminator is the source-weighted occupation potential of the actual return operator. This asks whether the small incoming source compensates for repeated nearly conservative returns, rather than assuming that contraction of each local map makes its resolvent harmless.

## Research question

Starting from the exact energy-normalized mixed functional defining the PF-290 deficit delta_(n,r), derive, or show why one cannot derive, a finite-section return equation

\[
a_{n,r,L}=f_{n,r,L}+T_{n,r,L}a_{n,r,L}
\]

in the PF-296 canonical source-row coordinates. Here L is a finite geometric truncation, f is the actual forcing from the normalized low vector, and T is the actual recoupling map. The equation must come from the mixed DtN/Schur problem, not from an arbitrary model chosen to have favorable coefficients.

Can the physical forcing satisfy

\[
\sup_{n,r,L}\sum_i q_i\left|[(I-T_{n,r,L})^{-1}f_{n,r,L}]_i\right|<\infty
\]

with the inverse interpreted only where justified by the actual problem? Together with a validated synthesis/transport factorization this would supply PF-296's missing source-moment bound. If there is an additional response term not represented by these columns, it must be displayed and estimated separately.

## Why it may matter

This is a specific sufficient mechanism for the existing normalized-response compactness question, not a new supercritical Sobolev claim. It respects the failure of the earlier R>1 route. It may also expose a genuine obstruction: the local columns may all be regular while a nearly recurrent global return map amplifies their coefficients without bound. The distinction is testable in the same coefficient normalization used by the current synthesis theorem.

## Decisive test

First derive the return representation and its relation to the actual Riesz response on the fixed physical witness window. Carry the low-vector factor k[ell_r]^(-1/2), the physical P/H projections, and all seam normalizations through the elimination. Track which geometric transports are already uniformly controlled and which are not. A convenient coefficient expansion that fails to represent the normalized mixed functional does not answer the question.

On finite sections put D_q=diag(q_i) and, when entrywise majorization is legitimate, define

\[
K_{n,r,L}=D_q|T_{n,r,L}|D_q^{-1},\qquad
\xi_{n,r,L}=D_q|f_{n,r,L}|.
\]

Test the source-adapted positive Green potential

\[
\sup_{n,r,L}\sum_{m\ge0}\|K_{n,r,L}^{m}\xi_{n,r,L}\|_1<\infty.
\]

Prove the required convergence and the passage from this majorant to the signed return equation; do not invoke a Neumann series without its hypotheses. A bound for the physical forcing is enough: uniform boundedness of (I-K)^(-1) on every input is a stronger, potentially unnecessary demand. A block-positive majorant or a direct signed resolvent estimate is equally admissible if entrywise absolute values destroy the relevant structure.

Use the conserved q-weight in PF-296 to identify where return mass can actually leave the repeated subsystem. Local conservation or nonexpansion alone supplies no inverse gap. Seek a geometric escape/capacity estimate, or a quantitative compensation between incoming forcing and return lifetime, with constants uniform in n and in the truncation L. Do not assume a uniform lower bound for the escape rate merely because each finite system has one.

The scalar calibration T=(1-epsilon)I has bounded individual iterates but response f/epsilon. A normalized forcing of order one diverges as epsilon tends to zero, whereas forcing of order epsilon need not. This distinguishes a source-adapted estimate from an unjustified contraction argument; it is not a model of the actual prime-flute geometry. Reproduce the already-controlled single-seam/fixed-axis case before introducing repeated returns.

If the potential bound succeeds, insert it into PF-296 with all response terms and support transports retained, and deduce only the justified statement about delta_(n,r). If it fails, determine whether the signed physical response still has bounded ell^1(q) moment. Divergence of an absolute majorant is not divergence of the response, and divergence of the response moment is not a positive shorting deficit. A noncompactness claim must return to the basis-invariant PF-290 scalar and exhibit its positive limsup on an admissible sparse tail.

A useful positive result is an actual source-forcing/return estimate that completes this local factorization. A useful negative result identifies the concrete near-recurrent mode or residual mixed operator and measures its effect on the physical deficit. Another rowwise bound, a generic matrix counterexample, or an unexplained appeal to global coupling is insufficient.

## Evidence boundary

No return factorization, uniform potential estimate, mixed-response compactness, or weak-trace theorem is established. PF-296 gives a conditional sufficient source-space bound; its weighted ell^1 norm can be too strong because it discards cancellation. PF-290 detects one local witness-band obstruction: delta_(n,r) tending to zero does not prove compactness of every physical-high or global mixed sector. The existing accepted compactness investigation retains ownership of that broader question. Check the current canonical findings and adjacent review sidecars before using either input; do not reopen the refuted supercritical homotopy estimate.
