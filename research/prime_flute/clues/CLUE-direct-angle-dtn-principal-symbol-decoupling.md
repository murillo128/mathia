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
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
---

# Can the local pant `L/H` block reach reciprocal-prime mean-square leakage?

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

PF-214 also makes `K` exactly nearest-neighbor in the cuff-module index. Consequently `K_{LH}` is the sum of only the three offsets `r=-1,0,1`, and each fixed-offset family is a two-sided orthogonal direct sum of local pant blocks. The low target on one module has only `O(1+\log P_n)` dimensions. PF-210 therefore makes the pointwise estimate

\[
\|L_{n+r}KH_n\|\le C/P_n
\]

sufficient, but PF-318 shows that this is not the cheapest endpoint theorem.

The actual weak-trace target is only the Hilbert--Schmidt average

\[
\boxed{
\|L_{n+r}KH_n\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2},
\qquad r=-1,0,1.
}
\]

PF-318 proves that this mean-square reciprocal-prime scale already gives

\[
K_{LH},Z_{LH}\in\mathcal S_{1,\infty}
\]

by splitting singular-value counting at `P_n\asymp\sigma^{-1}`: logarithmic target rank controls the lower-prime side and Hilbert--Schmidt counting plus the Chebyshev prime tail controls the upper-prime side. In particular the largest local singular value may lose a factor `\sqrt{\log P_n}` relative to `P_n^{-1}` without breaking the endpoint.

This changes the analytic proof obligation in a useful way. Since `K` is self-adjoint and the low output is finite dimensional,

\[
\|L_{n+r}KH_n\|_{\mathcal S_2}^2
=
\sum_{e\in\mathcal E_{n+r}^{L}}
\|H_nKe\|^2
\]

for any orthonormal basis of the retained low band. One may therefore estimate the **aggregate high-frequency leakage of explicit low Fourier modes** rather than the worst unit vector in the entire high source.

PF-317 also extends PF-234's coefficient comparison to the full two-face strip DtN form. Thus this Hilbert--Schmidt leakage may be computed after normalizing by the explicit flat shifted-strip DtN matrix rather than by an unknown collapsing-collar pseudodifferential model, at only a `1+O(P_n^{-2})` bounded-factor loss.

PF-215 remains the essential negative control. The **complete** adjacent normalized pant block diverges on constant-to-constant data, so no proof may bound `Q_{n+1}KQ_n` wholesale. That obstruction lies in the cuff-constant channel removed before `Z_{LH}` is formed. The remaining question is specifically whether the nonconstant retained-low rows have only reciprocal-prime **mean-square** leakage into physical high frequencies even though the all-frequency pant transfer is large.

The fixed-geometry DtN facts from the previous audit remain background rather than the target. Girouard--Karpukhin--Levitin--Polterovich (JST 2022, DOI `10.4171/JST/399`) identify the standard local pseudodifferential structure, and Hislop--Lutzer (Inverse Problems 2001, DOI `10.1088/0266-5611/17/6/313`) give fixed-domain component decoupling. Romain Speciel (JST 2026, DOI `10.4171/JST/617`) confirms that global commutation with the boundary Laplacian is restrictive. None supplies the canonical degenerating-pant estimate below. PF-318's counting step itself uses only standard Hilbert--Schmidt singular-value counting, Ky Fan finite-sum inequalities, and the elementary Chebyshev prime bound already audited in PF-199/PF-210.

## Research question

For one canonical one-cusp pant core and its neighboring PF-205 artificial boundaries, let `\Lambda_E` be the positive shifted pant DtN form and let `\Lambda_Q^0` be the explicit flat shifted-strip energy on the seam modules. At fixed physical cutoff define

\[
\widetilde B_{n+r,n}
:=
L_{n+r}(\Lambda_Q^0)^{-1/2}
\Lambda_E
(\Lambda_Q^0)^{-1/2}H_n,
\qquad r=-1,0,1.
\]

Do the three local mixed-frequency blocks satisfy the endpoint-complete mean-square estimate

\[
\boxed{
\|\widetilde B_{n+r,n}\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2}
}
\]

uniformly on the canonical tail?

A positive answer closes the direct-angle weak-`S_1` gate through PF-317/PF-318. The stronger operator-norm estimate

\[
\|\widetilde B_{n+r,n}\|\le C/P_n
\]

would still suffice, but it is no longer the preferred target unless the geometry naturally yields it.

## Why it may matter

PF-316 reduces the full physical endpoint to two genuine channels, `Z_{LH}` and `T_H`. PF-317 shows that the direct channel is substantially more local than previously thought: topology already supplies its finite reassembly, positivity makes same-sector completion contractive, and the seam normalization can be made explicit. PF-318 now removes an additional worst-case requirement: the local theorem need only control total squared leakage across the logarithmic retained-low band.

The unresolved mathematics is therefore concentrated in a concrete geometric/spectral quantity. For each of only `O(\log P_n)` low Fourier rows, apply the actual one-pant normalized DtN map and measure the part landing above the fixed physical cutoff on the neighboring/source module. The sum of those squared high tails must be `O((1+\log P_n)/P_n^2)`. This is closer to an averaged symbol/off-diagonal-energy estimate than to a uniform block norm, and may be accessible even if isolated near-cutoff rows are worse than `P_n^{-1}`.

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

First choose an orthonormal basis `\mathcal E_{n+r}^{L}` for the retained nonconstant-low target and estimate

\[
\sum_{e\in\mathcal E_{n+r}^{L}}
\left\|
H_n(\Lambda_Q^0)^{-1/2}\Lambda_E(\Lambda_Q^0)^{-1/2}e
\right\|^2.
\]

The endpoint target is

\[
C(1+\log P_n)P_n^{-2}.
\]

This formulation allows cancellation/decay to be proved row by row or in aggregate and avoids taking a supremum over all high inputs before summing the low rows.

Second, separate mechanisms already controlled by local geometry. PF-231--PF-233 show that the ultraparallel corridor and variable-width diagonal part have explicit operator-valued transfer laws, while PF-232/PF-255 make the hypercycle/shear transport reciprocal-prime small or graph-local in the relevant normalized senses. Any remaining leakage estimate must identify which part of the actual finite pant completion mixes the physical low rows into high frequencies; it should not repackage PF-215's constant-mode conductance as a mixed-frequency obstruction.

Third, if the Hilbert--Schmidt target fails, compute the local singular-value distribution rather than falling back immediately to operator norm. PF-318 gives one sufficient envelope but not a necessary one: any per-module law whose fixed-offset prime-density threshold count yields `N(a)=O(a^{-1})` can still close `Z_{LH}`.

For a negative result, isolate a sequence of **nonconstant-low/high** local blocks whose squared singular mass violates every weak-`S_1`-compatible prime-density envelope. Constant-mode growth from PF-215 is not such a witness, and a single singular value larger than `C/P_n` is no longer enough after PF-318.

## Evidence boundary

PF-317 proves only the structural reduction and explicit normalization comparison. PF-318 proves only that reciprocal-prime **mean-square** local leakage is sufficient for the endpoint. Neither proves the Hilbert--Schmidt estimate for the actual canonical pant.

PF-212 controls particular local recoupling words, PF-231--PF-233 control corridor models and their variable-width normalization, PF-255 controls the prime-dependent hypercycle footpoint transport, and PF-215 rules out a uniform bound on the complete neighboring pant block. None of those statements determines the specific nonconstant `L/H` Hilbert--Schmidt corner above.

The fixed-domain DtN literature remains prior-art guidance, not a degeneration theorem. The clue therefore remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-318 materially weakens the local obligation left by PF-317. The preferred next target is now

\[
\|\widetilde B_{n+r,n}\|_{\mathcal S_2}^2
=O((1+\log P_n)/P_n^2)
\]

for each of the three pant offsets. Equivalently, prove reciprocal-prime root-mean-square singular scale across the logarithmic retained-low band. The former `O(P_n^{-1})` operator-norm target remains a sufficient stronger theorem but is no longer required. The direction stays open until this averaged leakage, another weak-`S_1`-compatible singular-value envelope, or a genuine nonconstant-low/high obstruction is established.