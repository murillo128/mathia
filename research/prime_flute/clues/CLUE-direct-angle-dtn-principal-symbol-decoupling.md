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
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-239-reciprocal-prime-shear-makes-critical-band-leakage-absolutely-trace-summable.md
  - research/prime_flute/findings/PF-242-hypercycle-shear-is-exponentially-local-in-poschl-teller-mode-index.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-315-sequential-physical-band-elimination-factorizes-the-full-angle-defect.md
  - research/prime_flute/findings/PF-316-direct-channel-payment-makes-the-conditional-angle-endpoint-visible.md
  - research/prime_flute/findings/PF-317-positive-diagonal-completion-reduces-the-direct-angle-to-local-pant-crossing.md
  - research/prime_flute/findings/PF-318-logarithmic-rank-hilbert-schmidt-averages-already-close-the-direct-angle-at-weak-trace.md
  - research/prime_flute/findings/PF-319-corridor-form-smallness-alone-does-not-control-the-seam-normalized-direct-angle.md
  - research/prime_flute/findings/PF-320-form-smallness-controls-the-direct-angle-even-when-raw-seam-blocks-amplify.md
---

# Can the shear-deleted local pant angle reach reciprocal-prime mean-square leakage?

## Observation

PF-315--PF-316 reduce the full physical `P/H` endpoint to two genuine angle channels, the conditional post-low angle `T_H` and the direct angle

\[
Z_{LH}=J_{LL}^{-1/2}J_{LH}J_{HH}^{-1/2}.
\]

PF-317 shows that the direct channel may be bounded through local pant crossing, and PF-318 shows that logarithmic low rank makes the endpoint tolerant of mean-square leakage: a local squared Hilbert--Schmidt budget

\[
C\frac{1+\log P_n}{P_n^2}
\]

is enough for the prime-density weak-`S_1` count.

PF-319 then blocks one apparently easy route. PF-232's `O(P_n^{-1})` form-smallness is measured in the diagonal corridor energy, while the raw pant cross block in PF-317 is normalized by the seam energy. An arbitrary change between those positive metrics can amplify a mixed raw block, so the PF-232 Loewner sandwich does not by itself prove the PF-318 estimate for

\[
LQ^{-1/2}\Lambda_EQ^{-1/2}H.
\]

PF-320 changes the preferred target. Multiplicative closeness of positive forms **does** control their intrinsic low/high cross angles, because each angle divides by the same form's own diagonal low and high energies. For the PF-232 sandwich there are local low/high unitaries such that the actual sheared local angle differs from the shear-deleted local angle by operator norm `O(\beta_n)`, `\beta_n=O(P_n^{-1})`. Since the retained low sector has rank `O(1+\log P_n)`, the shear-angle error automatically satisfies

\[
\boxed{
\|E_n^{\rm shear}\|_{\mathcal S_2}^2
\lesssim
\frac{1+\log P_n}{P_n^2}.
}
\]

PF-320 also proves that sums of positive local forms reassemble by a contraction sandwich of the orthogonal direct sum of their local angles. Common positive finite-pant completion may remain in both the actual and shear-deleted forms without changing PF-232's multiplicative sandwich. Therefore the shear no longer has to be transported through PF-242/PF-255 into the final seam-normalized raw `K_{LH}` representation merely to meet the direct-angle endpoint budget.

PF-215 remains the essential negative control: the complete adjacent normalized pant block diverges on the cuff-constant channel. The target is still specifically the retained nonconstant-low/high angle after constants are removed.

## Research question

For one canonical one-cusp pant contribution, delete only the PF-232 hypercycle-straightening shear while retaining:

- the actual PF-205 seam energy used by simultaneous normalization;
- the variable-width diagonal corridor;
- the full common finite-pant/cusp-side completion;
- the fixed physical low/high cutoff from PF-212.

After distributing a positive block-diagonal share of the identity as in PF-320, let

\[
T_{0,n}^{(r)}
\]

be the intrinsic local low/high angle of this **shear-deleted** positive pant form for one of the finitely many neighboring offsets `r`.

Does the local reference family satisfy the endpoint-compatible estimate

\[
\boxed{
\|T_{0,n}^{(r)}\|_{\mathcal S_2}^2
\le
C\frac{1+\log P_n}{P_n^2},
}
\]

or another singular-value envelope that places the orthogonal direct sum of the local reference angles in `\mathcal S_{1,\infty}`?

A positive answer closes the **direct-angle** weak-`S_1` gate: PF-320 adds the actual shear with an error already inside the PF-318 mean-square budget, and its positive-sum factorization passes the local ideal estimate to the global direct angle. The separate conditional post-low angle `T_H` remains independent.

## Why it may matter

The live theorem is now materially narrower than the previous raw-block question. PF-319 still says not to infer seam-normalized raw `K_{LH}` smallness from corridor form-smallness. PF-320 shows that this stronger raw estimate is unnecessary for controlling the shear contribution to the actual direct angle.

The reference problem can therefore concentrate on the geometry that survives after the shear is removed. PF-233 gives an exact operator-valued transfer law for the variable-width diagonal corridor, and PF-238 shows that the actual complete-lift seam is compatible with the required dressed transfer envelope through one-sided domination. What remains is to turn that diagonal transfer structure, together with the physical `L/H` split and finite pant completion, into the local intrinsic angle envelope above.

This also separates two difficulties that were previously entangled. The reciprocal-prime shear is now perturbative at angle level; the unresolved issue is whether the **diagonal/reference pant itself** has sufficiently little retained-low/high correlation.

## Decisive test

Work on one local positive pant form and its fixed physical `L/H` split. Keep the actual seam normalizer, but replace the PF-232 sheared corridor by its shear-deleted variable-width diagonal form while leaving every common completion term unchanged.

Estimate the intrinsic angle

\[
T_{0,n}^{(r)}
=A_{0,n}^{-1/2}B_{0,n}^{(r)}C_{0,n}^{-1/2}
\]

directly, rather than the raw externally normalized block `B_{0,n}^{(r)}`. Use PF-233's exact mass-conjugated transfer law and PF-238's one-sided actual-seam domination to identify which parts of the diagonal corridor already have the required prime-scale damping. Then isolate the finite one-cusp-pant completion and determine whether it preserves the mean-square physical low/high envelope.

If a Hilbert--Schmidt estimate is unavailable, determine the local singular-value distribution and test it against PF-318's threshold count. A negative result must exhibit nonconstant-low/high angle mass incompatible with every weak-`S_1` prime-density envelope; constant-mode growth from PF-215 and raw metric amplification from PF-319 are not such witnesses.

PF-242/PF-255 remain available as independent structural information, but under PF-320 they are no longer the mandatory bridge for the shear term. Reintroduce them only if the shear-deleted reference estimate itself exposes a representation issue they genuinely resolve.

## Evidence boundary

PF-320 does not prove the shear-deleted local angle estimate. It proves that PF-232's actual shear changes the local angle only by `O(P_n^{-1})` in operator norm, hence by the PF-318-compatible squared Hilbert--Schmidt budget after logarithmic low-rank counting, and that positive local angles admit contraction-sandwich reassembly.

PF-233 and PF-238 control diagonal-corridor transfer in useful operator-energy representations, but neither currently proves the physical retained-low/high local angle with the complete pant attached. The finite pant completion therefore remains part of the live reference problem rather than an afterthought.

The fixed-domain DtN literature remains prior-art guidance rather than a degeneration theorem. No current external source supplies this canonical shrinking-pant physical-angle endpoint.

The clue therefore remains `accepted`, not `resolved`.

## Research disposition

Outcome: `accepted`.

PF-320 materially changes the preferred proof obligation. The previous same-seam raw `K_{LH}` shear estimate is stronger than necessary and is no longer the primary target. The next decisive step is the shear-deleted local pant **angle** with actual seam energy and full common completion. If that reference family meets a PF-318-compatible singular-value envelope, PF-320 adds the real shear at no additional endpoint cost and reassembles the direct angle through positive-form contraction.