---
id: CLUE-prime-flute-source-weighted-return-potential-controls-mixed-response
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-290-optimized-local-low-high-correlation-is-an-exact-high-band-shorting-deficit.md
  - research/prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions.md
  - research/prime_flute/findings/PF-297-robin-finite-sections-are-q-submarkov-but-lose-their-contraction-gap.md
  - research/prime_flute/findings/PF-298-tight-pant-constant-response-is-an-asymptotically-conservative-killed-conductance-edge.md
---

# Can a source-weighted return potential control row proliferation in the actual mixed response?

## Observation

PF-296 proves that the canonical fixed-axis synthesis Y_(s,r) is uniformly bounded from ell^1(q) to physical-axis H^(1/2), where q_i is the explicit conserved row weight and q_i asymp i+1. The canonical seam ratios lie in the permitted bounded-ratio range. Consequently a bounded weighted source moment rules out the local frequency escape tested by PF-290, provided the complete normalized response really factors through that synthesis and the controlled transports.

The missing input is not another fixed-row regularity estimate. It is how repeated neighboring-pant/Schur recoupling populates those rows after the physical energy normalization. A possible discriminator is the source-weighted occupation potential of the actual return operator. This asks whether the small incoming source compensates for repeated nearly conservative returns, rather than assuming that contraction of each local map makes its resolvent harmless.

PF-282 supplies an important compatibility check on this question. Same-sector reservoir mass by itself is not the surviving mixed-frequency obstruction after energy normalization: the normalized cross form factors through extension strength and the physical low/high extension angle. Any return-coordinate model used here must therefore represent the actual PF-290 mixed Riesz functional after the physical `P/H` split, rather than repackage an unprojected same-sector reservoir that PF-282 already separates from the mixed gate.

PF-297 fixes the local Robin part of this bookkeeping. In the PF-296 weight, every fixed-axis Robin inverse is `ell^1(q)`-nonexpansive; its finite Galerkin compressions are strictly `q`-sub-Markov because mass can leak only into omitted source rows. But the finite contraction constants converge to one, and the complete inverse preserves `q`-mass on nonnegative inputs. Robin normalization therefore cannot amplify the source budget, yet it cannot be the depth-uniform discount that sums the global return potential.

PF-298 now fixes a second local candidate for such a discount. The constant-boundary compression of each narrow one-cusp pant core is exactly a conductance edge of strength `c_n \gtrsim s_n^{-1}` plus nonnegative shifted killing whose **total** strength is at most `2\pi`. Hence its relative killing is `O(s_n)` and the corresponding isolated constant-mode Schur transmission tends to one. The neighboring pant can therefore be nearly conservative on its lowest symmetric channel even though the positive shift makes every finite local problem coercive.

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

For the positive-majorant route there is a sharper source-adapted certificate that avoids asking for any uniform inverse gap. If `K>=0` on `ell^1` and `xi>=0`, it is enough to construct a nonnegative `h` with uniformly bounded `ell^1` norm such that

\[
Kh\le h,\qquad \xi\le h-Kh.
\]

Then positivity gives, for every `N`,

\[
\sum_{m=0}^{N}K^m\xi\le h-K^{N+1}h\le h,
\]

so the full Green potential is bounded by `||h||_1` without a spectral-gap estimate. Conversely, whenever the positive Green potential converges in `ell^1`, its sum is such an `h` with equality `h-Kh=xi`. Thus the useful geometric target is an actual uniformly summable superharmonic/excessive majorant for the physical forcing, not a global contraction constant for all inputs. This equivalence is classical positive-operator/Markov potential theory; no novelty is claimed for it.

PF-297 makes the Robin contribution to this test exact. If a factor in `T` is one of the canonical fixed-axis Robin inverses, conjugation by `D_q` makes that factor column-substochastic, with finite-section lost mass given explicitly by the omitted-tail flux. Do not replace that exact loss by a uniform spectral gap: PF-297 proves the corresponding contraction constants tend to one. Instead track whether the actual physical forcing is compensated by this escape, or whether a later `P/H`-split reassembly/support factor supplies additional loss or changes the `q` currency.

PF-298 imposes the analogous constraint on any scalar low-symmetric pant factor. Its exact constant compression has local transmission `theta_n=1-O(s_n)` rather than a fixed `theta<1`. Do not assign a depth-uniform absorption constant to the one-cusp pant merely because `\Delta+1` is coercive. If accumulated pant killing is used as the escape mechanism, derive it across the actual chain and in the coefficient currency of the mixed response; PF-298 does not make the scalar constant compression an invariant subspace of the complete `P/H` problem.

Use the conserved q-weight in PF-296 to identify where return mass can actually leave the repeated subsystem. Local conservation or nonexpansion alone supplies no inverse gap. Seek a geometric escape/capacity estimate, or a quantitative compensation between incoming forcing and return lifetime, with constants uniform in n and in the truncation L. Do not assume a uniform lower bound for the escape rate merely because each finite system has one.

The scalar calibration T=(1-epsilon)I has bounded individual iterates but response f/epsilon. A normalized forcing of order one diverges as epsilon tends to zero, whereas forcing of order epsilon need not. This distinguishes a source-adapted estimate from an unjustified contraction argument; it is not a model of the actual prime-flute geometry. Reproduce the already-controlled single-seam/fixed-axis case before introducing repeated returns.

Cross-check any proposed return equation against PF-282 before treating it as a new obstruction. If its large occupation merely records same-sector extension mass while the physical low/high extension angle remains controlled, it has not identified the PF-290 mixed response. The return formulation is useful only if the coefficient potential reconstructs the actual normalized mixed Riesz representative, or isolates an explicit residual term whose physical-high projection can be estimated separately.

If the potential bound succeeds, insert it into PF-296 with all response terms and support transports retained, and deduce only the justified statement about delta_(n,r). If it fails, determine whether the signed physical response still has bounded ell^1(q) moment. Divergence of an absolute majorant is not divergence of the response, and divergence of the response moment is not a positive shorting deficit. A noncompactness claim must return to the basis-invariant PF-290 scalar and exhibit its positive limsup on an admissible sparse tail.

A useful positive result is an actual source-forcing/return estimate that completes this local factorization. A useful negative result identifies the concrete near-recurrent mode or residual mixed operator and measures its effect on the physical deficit. Another rowwise bound, a generic matrix counterexample, or an unexplained appeal to global coupling is insufficient.

## Evidence boundary

No complete return factorization, uniform source-adapted potential estimate, mixed-response compactness, or weak-trace theorem is established. PF-297 proves only that the canonical fixed-axis Robin normalization is `q`-nonamplifying and that its finite-section strict contraction has no depth-uniform gap. PF-298 proves only that the **constant-boundary compression** of the neighboring pant has relative shifted killing `O(s_n)`; it does not identify that scalar compression with the complete mixed return operator or decide whether accumulated nonuniform killing is sufficient. PF-296 gives a conditional sufficient source-space bound; its weighted ell^1 norm can be too strong because it discards cancellation. PF-290 detects one local witness-band obstruction: delta_(n,r) tending to zero does not prove compactness of every physical-high or global mixed sector. PF-282 additionally shows that unprojected reservoir occupation is not by itself the normalized mixed-frequency obstruction. The existing accepted compactness investigation retains ownership of the broader question. Check the current canonical findings and adjacent review sidecars before using either input; do not reopen the refuted supercritical homotopy estimate.

## Research disposition

The clue remains accepted as a line-local investigation because it attacks the exact missing quantity left by PF-296: the `q`-weighted coefficient budget of the complete normalized PF-290 response. PF-297 and PF-298 now resolve two local sub-gates in the same direction: neither the complete fixed-axis Robin normalization nor the low symmetric one-pant constant response supplies a depth-uniform contraction gap. Robin factors preserve the `q` budget on nonnegative complete inputs, while pant relative killing is only `O(s_n)` on its constant compression. The first unresolved gate is therefore the actual `P/H`-split neighboring-pant return/reassembly representation and the accumulated source/escape balance across the full factors, including any nonconstant-mode or residual physical-high contribution.

A targeted prior-art audit places the Green-potential/fundamental-matrix and excessive-function machinery in standard Markov/potential and positive-operator theory; it supplies no independent novelty claim. The project-specific unresolved question is whether the canonical prime-flute elimination produces such a positive or signed source-coordinate structure with a uniform `q`-weighted forcing/return balance. Failure to obtain that structure is itself informative only if the residual mixed operator is identified explicitly and returned to the PF-290 deficit.