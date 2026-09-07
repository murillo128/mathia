---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-173-relative-central-recoupling-is-trace-summable.md
  - research/prime_flute/findings/PF-175-weighted-defect-gives-dual-resolvent-schatten-bridge.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-189-complete-short-collar-central-sector-is-weak-trace-class.md
  - research/prime_flute/findings/PF-190-weighted-endpoint-gives-log-square-resolvent-envelope.md
  - research/prime_flute/findings/PF-191-exact-area-lambert-transport-retains-suppressed-strong-L1-endpoint.md
  - research/prime_flute/findings/PF-192-generic-strong-L1-geometric-rigidity-fails-at-the-endpoint.md
  - research/prime_flute/findings/PF-194-hamiltonian-reflection-marked-korn-still-fails-in-L1.md
  - research/prime_flute/findings/PF-195-critical-one-sided-weak-S2-localization-is-not-controlled-by-endpoint-mass-alone.md
  - research/prime_flute/findings/PF-196-solomyak-orlicz-penalty-is-logarithmic-but-prime-summable.md
  - research/prime_flute/findings/PF-197-matrix-valued-critical-cwikel-theory-removes-local-vector-endpoint-gap.md
  - research/prime_flute/findings/PF-198-finite-window-lambert-localization-preserves-critical-orlicz-budget.md
  - research/prime_flute/findings/PF-199-two-sided-finite-color-localization-has-no-weak-trace-counting-loss.md
  - research/prime_flute/findings/PF-200-regular-lambert-body-principal-cwikel-constants-are-uniform.md
  - research/prime_flute/findings/PF-201-global-to-local-cwikel-factorization-removes-regular-body-off-diagonal-remainder.md
  - research/prime_flute/findings/PF-202-decomposition-cuff-seams-have-arbitrarily-summable-critical-orlicz-budget.md
  - research/prime_flute/findings/PF-203-piecewise-area-gluing-removes-cuff-smoothing-operator-gate.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
---

# Can the weak-trace endpoint be completed from physical interfaces and the true-short-collar splice?

## Observation

The endpoint problem has narrowed substantially. PF-189 proves weak `S_1` for the complete fixed-central short-collar sector and PF-173 makes its matched recoupling trace summable. PF-191 gives the exact-area Lambert/body comparison a summable strong-`L^1` defect, PF-196 identifies the critical `L\log L` coefficient currency, PF-197 supplies the matrix-valued critical Cwikel theorem for smooth localized order-`-1` factors, and PF-198--PF-201 close fragmentation, finite-color counting, regular-body constant uniformity, and the regular-body external off-diagonal concern. The entire regular Lambert-body principal cotangent sector is therefore already controlled in `S_{1,\infty}`.

PF-202 showed that PF-182's smooth distinguished-cuff correction can be made arbitrarily small in the summed critical coefficient budget, but left open whether shrinking its support destroys the local operator constant through higher derivatives and shrinking buffers. PF-203 changed the architecture: **that smoothing correction is not required at the quadratic-form level.** The pantwise exact-area maps already glue to one globally bi-Lipschitz area-preserving map, and its relative form has no separate cuff surface term.

PF-204 sharpens the unsmoothed route again. It proves the exact two-Hilbert-space identity

\[
R_gU_0-U_0R_+
=(dR_g)^*M_{C_0}P_{F_0}dR_+,
\]

where `R_g` and `R_+` are the two **native smooth hyperbolic resolvents** and `P_{F_0}` is the bounded a.e. cotangent pullback by the PF-203 map. Thus a critical theorem for the globally rough pulled resolvent is no longer mandatory. The physical-cuff difficulty is now narrower: control the mixed critical product with its explicit piecewise-smooth order-zero transport, without losing the prime-summable `L\log L` coefficient scale.

The geometric true-short-collar endpoint remains independent. PF-183 reduces the complete PF-138 family to disjoint normalized thick slabs; PF-184--PF-188 remove flux, marked Killing modes, and qualitative Sobolev degeneration as generic obstructions; PF-192/PF-194 rule out a generic strong-`L^1` rigidity shortcut. The PF-177 optimized gauges are still needed because the issue there is the **bulk endpoint coefficient budget**, not decomposition-cuff regularity.

Thus the live question is whether the remaining physical interface transport and the canonical true-short-collar splice can be put into the same prime-summable weak endpoint without recreating a global logarithmic loss.

## Research question

Can the exact prime/shift first relative resolvent be decomposed into already controlled regular/central pieces plus physical-interface and true-short-collar terms so that the complete operator belongs to

\[
\mathcal S_{1,\infty}
\quad\text{while PF-112 still excludes}\quad
\mathcal S_1?
\]

For the decomposition cuffs, use PF-204's exact native-resolvent factorization as the preferred unsmoothed starting point. The precise analytic question is whether the physical cuff/module-interface coefficient can be localized so that

\[
(dR_g)^*M_{C_{\mathrm{cuff}}}P_{F_0}dR_+
\in\mathcal S_{1,\infty}
\]

with a weak-trace constant uniform or prime-summably controlled over the infinite cuff family while preserving the PF-196 effective-area coefficient scale. Both resolvents are smooth; what remains is to handle `P_{F_0}` honestly. A proof may use branchwise smooth extensions, a two-manifold/Fourier-integral critical estimate, or another exact reduction, but it may not simply drop the bounded transport from Ponge's `Q u P` theorem.

For the true PF-138 short collars, the separate question is whether the canonical exact-area body/core interpolation admits an endpoint conservative splice whose local cost is summable in the correct strong-`L^1` or critical weak currency. No generic `L^1` Korn/rigidity theorem may be assumed after PF-192/PF-194.

## Why it may matter

A positive answer would establish the natural two-dimensional critical endpoint suggested independently by PF-189 and the matrix-valued Cwikel mechanism, while PF-112 would keep trace class excluded. This would show that PF-190's `O(log^2 n/n)` singular-value envelope is an artifact of strong-Schatten extrapolation rather than a genuine loss in the exact prime/shift geometry.

PF-203/PF-204 also make the test conceptually cleaner. A negative result can no longer be attributed merely to an arbitrarily thin smoothing collar or to the decision to represent the target Laplacian as a rough pulled operator. It must expose a genuine critical failure of the physical interface transport, a true-short-collar endpoint obstruction, or another explicitly derived global term whose critical budget fails.

## Decisive test

First isolate one **physical decomposition-cuff interface** using the unsmoothed PF-203 map and PF-204 factorization. Prove a stable estimate of the form

\[
q\!\left((dR_g)^*M_{C_{\mathrm{cuff},n}}P_{F_0}dR_+\right)
\le C\,\|C_{\mathrm{cuff},n}\|_{L\log L},
\]

or an equivalent branchwise/direct-sum estimate with a tail constant cheap enough to preserve prime summability. The localization must not differentiate a sharp characteristic function or manufacture a delta term on the cuff. If the piecewise transport is replaced by smooth branch extensions, their critical constants must be quantified; boundedness of `P_{F_0}` on `L^2` alone is not an endpoint estimate.

If that succeeds, sum the finitely-many-per-module exceptional families that PF-200/PF-201 excluded: physical cuff/body transmission, module ends, corner/assembly corrections, and any remaining coefficient pieces outside the regular recentered family. A fixed number per module is still infinite globally and needs a prime-summable counting budget. PF-201's regular sector should remain in its exact `A_h^*DA_g` architecture rather than being recut with external resolvent cutoffs.

Then settle the **true-short-collar endpoint splice** on PF-183's disjoint normalized thick slabs. Use the canonical PF-177/PF-184 structure to construct or refute an exact-area marked interpolation with a cuffwise strong-`L^1` estimate, or an explicitly identified Lorentz/Orlicz substitute sufficient for weak `S_1`. PF-192/PF-194 forbid justifying this by generic endpoint rigidity.

Finally write the complete first-relative-resolvent identity for one chosen global exact-area identification and verify that every term belongs to a proved sector. Under the PF-203/PF-204 unsmoothed architecture, do not add a separate smooth decomposition-seam term and do not reintroduce a rough-resolvent theorem unless it is genuinely useful. If a smooth PF-182/PF-202 identification is deliberately chosen instead, its shrinking-family operator constant must still be proved rather than assumed.

## Evidence boundary

No global weak-`S_1` theorem is established. PF-201 controls only the regular Lambert-body principal cotangent sector. PF-203 proves that decomposition-cuff smoothing is optional at form level. PF-204 proves the exact native two-Hilbert-space factorization, but **not** a critical ideal estimate for the bounded piecewise cotangent transport inside that factorization.

PF-202 remains valid and useful as a smooth-comparison alternative, but its shrinking-family local Cwikel constant is unresolved if that architecture is chosen. The PF-183 true-short-collar endpoint conservative splice also remains unproved. PF-190 is therefore still the persisted complete weighted-endpoint consequence.

The clue makes no wave-operator, scattering-matrix, determinant, resonance, or RH claim. A future weak-`S_1` theorem would classify the exact prime/shift control at the critical first-resolvent level and would still have to be interpreted under the README's arithmetic-control discipline.

## Research disposition

The clue remains `accepted`, with a sharper frontier. **Regular Lambert-body critical localization is closed through PF-201; PF-203 removes distinguished-cuff smooth-pasting as a mandatory form-level gate; PF-204 removes the rough pulled resolvent as a mandatory analytic factor.** The active interface problem is now the critical weak-trace estimate for the explicit native-resolvent/cotangent-transport product, alongside the independent canonical endpoint conservative splice on the true PF-138 short collars. PF-202's shrinking smooth seam should be revisited only if a later operator argument genuinely requires global smoothness.