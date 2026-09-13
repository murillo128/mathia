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
  - research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-239-reciprocal-prime-shear-makes-critical-band-leakage-absolutely-trace-summable.md
  - research/prime_flute/findings/PF-242-hypercycle-shear-is-exponentially-local-in-poschl-teller-mode-index.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-319-corridor-form-smallness-alone-does-not-control-the-seam-normalized-direct-angle.md
---

# Can the local pant `L/H` block reach reciprocal-prime mean-square leakage?

## Observation

PF-315--PF-316 reduce the full physical `P/H` endpoint to two genuine angle channels, the conditional post-low angle `T_H` and the direct angle

\[
Z_{LH}=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}.
\]

PF-317 localizes the direct channel. In PF-214's simultaneous seam-energy coordinates the positive precision is `I+K`, with

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}\ge0,
\]

and

\[
Z_{LH}
=(I+K_{LL})^{-1/2}K_{LH}(I+K_{HH})^{-1/2}.
\]

The diagonal factors are contractions, so `s_j(Z_{LH})<=s_j(K_{LH})`. Nearest-neighbor cuff topology then reduces `K_{LH}` to the three offsets `r=-1,0,1`, each an orthogonal direct sum of local pant blocks.

PF-318 weakens the required local theorem further. Since each retained low target has rank only `O(1+log P_n)`, it is enough to prove

\[
\boxed{
\|L_{n+r}KH_n\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2},
\qquad r=-1,0,1.
}
\]

Threshold counting then gives `K_{LH},Z_{LH} in S_{1,infinity}`. The largest local singular value may therefore lose a factor `sqrt(log P_n)` relative to `P_n^{-1}` without breaking the endpoint. Equivalently, by self-adjointness, the target is aggregate high-frequency leakage of an orthonormal basis of retained low modes rather than a worst-input operator norm.

PF-319 closes an important proof-strategy loophole. PF-232's `O(P_n^{-1})` relative form-smallness of the hypercycle straightening shear is small in the **diagonal corridor energy metric**, whereas the direct angle is normalized by the PF-205 seam energy. PF-319 proves abstractly and by an exact `2x2` countermodel that a small Loewner-relative perturbation in one positive metric can be arbitrarily amplified after normalization by another. In particular PF-232's reciprocal-prime form sandwich cannot simply be combined with logarithmic low rank to infer the PF-318 estimate.

The shear is not thereby shown to be bad. PF-239, PF-242 and PF-255 give additional structure absent from the PF-319 countermodel: critical-band trace summability, strong mode locality and a parity-local two-derivative leakage bound. A positive proof should exploit that actual locality **after placing the perturbation in the same seam-normalized physical-frequency representation as `K`**, or estimate the required rows directly. The remaining finite-pant completion must be treated separately rather than hidden inside a generic form comparison.

PF-215 remains the essential negative control. The complete adjacent normalized pant block diverges on the cuff-constant channel, so no proof may bound the whole neighboring pant transfer uniformly. The target below is specifically the nonconstant-low/high corner after constants have been removed.

## Research question

For one canonical one-cusp pant core and its neighboring PF-205 artificial boundaries, let `Lambda_E` be the positive shifted pant DtN form and let `Lambda_Q^0` be the explicit flat shifted-strip seam energy. At a fixed physical cutoff define

\[
\widetilde B_{n+r,n}
:=
L_{n+r}(\Lambda_Q^0)^{-1/2}
\Lambda_E
(\Lambda_Q^0)^{-1/2}H_n,
\qquad r=-1,0,1.
\]

Do the three local mixed-frequency blocks satisfy

\[
\boxed{
\|\widetilde B_{n+r,n}\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2}
}
\]

uniformly on the canonical tail?

A positive answer closes the direct-angle weak-`S_1` gate through PF-317/PF-318. The stronger operator-norm estimate `||\widetilde B_{n+r,n}||<=C/P_n` remains sufficient but is no longer the preferred target unless the geometry yields it naturally.

## Why it may matter

The direct endpoint has become a concrete local geometric/spectral estimate. For only `O(log P_n)` retained low Fourier rows, apply the actual one-pant seam-normalized DtN map and measure the component landing above the fixed physical cutoff on the neighboring/source module. Total squared leakage must be `O((1+log P_n)/P_n^2)`.

PF-319 also tells us what **not** to prove. Reciprocal-prime form perturbation before the final normalization is insufficient unless the corresponding change of energy metric is controlled on the source/target sectors. The most promising surviving route is therefore to transport the actual PF-239/PF-242/PF-255 locality into the seam-normalized low/high corner, where it can be summed rowwise, rather than try to close the endpoint by a global Loewner sandwich.

## Decisive test

Work on one actual PF pant core at a time, with no global inverse. Use the explicit flat two-face seam multiplier controlled by PF-234/PF-317 and the fixed physical low/high cutoff from PF-212.

Choose an orthonormal basis `E_{n+r}^L` for the retained nonconstant-low target and estimate directly

\[
\sum_{e\in\mathcal E_{n+r}^{L}}
\left\|
H_n(\Lambda_Q^0)^{-1/2}\Lambda_E(\Lambda_Q^0)^{-1/2}e
\right\|^2.
\]

The endpoint target is `C(1+log P_n)P_n^{-2}`.

Decompose only by mechanisms that remain meaningful in this final metric. The diagonal ultraparallel/variable-width corridor has explicit transfer laws from PF-231--PF-233. For the hypercycle/shear contribution, do **not** use PF-232's relative form error alone: PF-319 shows that the corridor-to-seam metric conversion can amplify it. Instead, conjugate the actual shear transport into the seam-normalized physical-frequency representation and use PF-239/PF-242/PF-255 to prove either a direct rowwise Hilbert--Schmidt bound or a source/target-restricted metric-conversion/locality estimate that preserves reciprocal-prime leakage.

Then isolate whatever part of the finite one-cusp pant completion remains after these controlled pieces. If the Hilbert--Schmidt target fails, determine the actual local singular-value distribution rather than falling back immediately to operator norm: PF-318 gives one sufficient envelope, not a necessary one. A negative result must exhibit nonconstant-low/high squared singular mass incompatible with every weak-`S_1` prime-density envelope; constant-mode growth from PF-215 is not such a witness.

## Evidence boundary

PF-317 proves the structural localization and PF-318 proves that reciprocal-prime mean-square local leakage is sufficient. Neither proves the estimate for the actual canonical pant.

PF-232 proves only corridor-relative form-smallness of the straightening shear. PF-319 proves that this statement is not stable under an uncontrolled change to the seam energy metric. PF-239/PF-242/PF-255 provide stronger structural locality for the real shear/compactification, but no current finding completes their conversion into the exact local `L/H` Hilbert--Schmidt corner above. The finite pant completion is also still open.

The fixed-domain DtN literature remains prior-art guidance rather than a degeneration theorem. Girouard--Karpukhin--Levitin--Polterovich identify standard local DtN pseudodifferential structure, Hislop--Lutzer give fixed-domain component decoupling, and Speciel shows that global commutation with the boundary Laplacian is restrictive; none supplies the canonical degenerating-pant endpoint estimate.

The clue therefore remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-318 leaves the mean-square reciprocal-prime leakage estimate as the endpoint-complete local target. PF-319 removes the shortcut through PF-232's Loewner sandwich and narrows the next step to a same-metric argument: transfer the actual shear locality into the seam-normalized physical low/high representation, then bound the remaining finite-pant completion. The direction stays open until that estimate, another weak-`S_1`-compatible singular-value envelope, or a genuine nonconstant-low/high obstruction is established.