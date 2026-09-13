---
id: CLUE-prime-flute-direct-angle-dtn-principal-symbol-decoupling
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-210-prime-density-makes-logarithmic-rank-low-modes-weak-trace-class.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality.md
  - research/prime_flute/findings/PF-215-thin-pant-corridors-force-normalized-adjacent-hopping-to-diverge.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
---

# Can the local pant `L/H` block reach the reciprocal-prime scale?

## Observation

PF-316 isolates

\[
Z_{LH}=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}
\]

as one of the two exact weak-`S_1` gates for the full physical `P/H` angle. The original version of this clue therefore asked for a principal/remainder decomposition of the complete boundary precision and a global truncation-independent singular-value count.

PF-317 materially sharpens that obligation. In PF-214's simultaneous seam-energy coordinates the positive precision is `I+K`, with

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\]

and the direct nonconstant blocks satisfy

\[
Z_{LH}
=(I+K_{LL})^{-1/2}K_{LH}(I+K_{HH})^{-1/2}.
\]

The two diagonal factors are contractions, so

\[
s_j(Z_{LH})\le s_j(K_{LH}).
\]

Same-sector pant completion therefore does not need to be inverted or localized for this sufficient direction.

PF-214 also makes `K` exactly nearest-neighbor in the cuff-module index. Consequently `K_{LH}` is the sum of only the three offsets `r=-1,0,1`, and each fixed-offset family is a two-sided orthogonal direct sum of local pant blocks. The low target on one module has only `O(1+\log P_n)` dimensions. PF-210 then shows that the concrete local estimate

\[
\boxed{
\|L_{n+r}KH_n\|\le C/P_n,
\qquad r=-1,0,1,
}
\]

is already sufficient for

\[
Z_{LH}\in\mathcal S_{1,\infty}.
\]

No additional global reassembly theorem is required for this direct channel once those local bounds hold.

PF-317 also extends PF-234's coefficient comparison to the full two-face strip DtN form. Thus the local block may be normalized by the explicit flat shifted-strip DtN matrix rather than by an unknown collapsing-collar pseudodifferential model, at only a `1+O(P_n^{-2})` multiplicative loss. This removes the seam-normalizer degeneration from the live estimate.

PF-215 is the essential negative control. The **complete** adjacent normalized pant block diverges on constant-to-constant data, so no proof may bound `Q_{n+1}KQ_n` wholesale. That obstruction lies in the cuff-constant channel removed before `Z_{LH}` is formed. The remaining question is specifically whether frequency separation makes the nonconstant-low/high corner small even though the all-frequency pant transfer is large.

The fixed-geometry DtN facts from the previous audit remain background rather than the target. Girouard--Karpukhin--Levitin--Polterovich (JST 2022, DOI `10.4171/JST/399`) identify the standard local pseudodifferential structure, and Hislop--Lutzer (Inverse Problems 2001, DOI `10.1088/0266-5611/17/6/313`) give fixed-domain component decoupling. Romain Speciel (JST 2026, DOI `10.4171/JST/617`) confirms that global commutation with the boundary Laplacian is restrictive. None supplies the canonical degenerating-pant estimate below, and PF-317 means a global pseudodifferential calculus is no longer required merely to organize the endpoint count.

## Research question

For one canonical one-cusp pant core and its two neighboring PF-205 artificial boundaries, let `\Lambda_E` be the positive shifted pant DtN form and let `\Lambda_Q^0` be the explicit flat shifted-strip energy on the adjacent seam modules. At fixed physical cutoff, do the three possible local mixed-frequency blocks

\[
\widetilde B_{n+r,n}
:=
L_{n+r}(\Lambda_Q^0)^{-1/2}
\Lambda_E
(\Lambda_Q^0)^{-1/2}H_n,
\qquad r=-1,0,1,
\]

satisfy

\[
\boxed{
\|\widetilde B_{n+r,n}\|\le C/P_n
}
\]

uniformly on the canonical tail?

A positive answer closes the direct-angle weak-`S_1` gate through PF-317 and PF-210. A slower norm rate does not automatically kill the route if the local singular values have additional decay, but `O(P_n^{-1})` is now the cheapest sufficient theorem.

## Why it may matter

PF-316 reduces the full physical endpoint to two genuine channels, `Z_{LH}` and `T_H`. PF-317 shows that the direct channel is substantially more local than previously thought: topology already supplies its finite reassembly, positivity makes same-sector completion contractive, and the seam normalization can be made explicit.

The unresolved mathematics is therefore concentrated in a single geometric issue: whether a thin one-cusp pant can transfer a physical-high trace into the retained nonconstant-low band at reciprocal-prime strength after the correct boundary-energy normalization. This is exactly where PF-215's huge constant-mode conductance and PF-212/PF-255's favorable frequency-decoupling mechanisms meet.

## Decisive test

Work on one actual PF pant core at a time, with no global inverse. Use the explicit flat two-face seam multiplier from PF-317,

\[
\Lambda^0_{L,w}(\xi)
=\frac{\mu}{\sinh(2\mu w)}
\begin{pmatrix}
\cosh(2\mu w)&-1\\
-1&\cosh(2\mu w)
\end{pmatrix},
\qquad
\mu=\sqrt{1+\xi^2},
\]

and the fixed physical low/high cutoff from PF-212.

First, estimate each of the three local form corners `L_{n+r}\Lambda_EH_n` after these source/target energy normalizers. Any positive proof must visibly exploit low/high frequency separation; PF-215 forbids replacing this by an all-frequency pant norm estimate.

Second, track the estimate in the canonical parameters `w_n\asymp P_n^{-1}`, cuff length `O(\log P_n)`, and tight-pant separation. The preferred endpoint is `C/P_n` with a constant independent of the pant index and finite Fourier cutoff. PF-317 then supplies the actual-strip comparison automatically.

Third, if the block norm does not reach `O(P_n^{-1})`, compute a local singular-value envelope rather than abandoning the route. Because each fixed module offset is already a literal orthogonal sum, the only acceptable weaker result is one whose prime-density threshold count still gives `N(a)=O(a^{-1})`.

For a negative result, isolate a sequence of **nonconstant-low/high** normalized local vectors whose mixed pant correlation violates every weak-`S_1`-compatible count. Constant-mode growth from PF-215 is not such a witness, and a large unnormalized pant DtN coefficient is not enough.

## Evidence boundary

PF-317 proves only the structural reduction and the explicit normalization comparison. It does **not** prove the reciprocal-prime local block estimate, weak-`S_1` membership of `K_{LH}`, or weak-`S_1` membership of `Z_{LH}`. PF-212 controls particular local recoupling words, PF-255 controls the prime-dependent hypercycle footpoint transport, and PF-215 rules out a uniform bound on the complete neighboring pant block; none of those statements determines the specific local `L/H` corner above.

The fixed-domain DtN literature remains prior-art guidance, not a degeneration theorem. The clue therefore remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-317 replaces the previous broad global principal/remainder task by a sharper local obligation. The next preferred positive target is the three-offset flat-seam-normalized estimate `\|\widetilde B_{n+r,n}\|=O(P_n^{-1})`; PF-210 and PF-317 then perform the global weak-trace counting automatically. If that rate fails, the fallback is a local singular-value law strong enough to give the same prime-density count. The direction remains open until one of those local estimates is proved or a genuine nonconstant-low/high obstruction is exhibited.