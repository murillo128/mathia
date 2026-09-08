---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-189-complete-short-collar-central-sector-is-weak-trace-class.md
  - research/prime_flute/findings/PF-201-global-to-local-cwikel-factorization-removes-regular-body-off-diagonal-remainder.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-207-dirichlet-block-dilation-restores-critical-seam-scale.md
  - research/prime_flute/findings/PF-210-prime-density-makes-logarithmic-rank-low-modes-weak-trace-class.md
  - research/prime_flute/findings/PF-211-energy-normalized-dtn-gluing-removes-exterior-amplification-from-low-mode-gate.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-213-summable-schur-off-diagonal-decay-closes-smooth-interface-reassembly-gate.md
  - research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality.md
  - research/prime_flute/findings/PF-215-thin-pant-corridors-force-normalized-adjacent-hopping-to-diverge.md
  - research/prime_flute/findings/PF-216-positive-shift-pant-compression-has-a-growing-mass-floor.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, while several exact sectors now sit at the natural two-dimensional weak endpoint. PF-189 controls the complete fixed-central short-collar sector. PF-196--PF-201 control the regular Lambert-body critical sector, including matrix-valued `L\log L` localization and off-diagonal reassembly. PF-203/PF-204 provide an exact unsmoothed two-native-resolvent factorization for the decomposition interfaces, while PF-205--PF-212 develop a competing smooth boundary route with natural-width strips, scale-matched commutators, low-mode counting, energy-normalized DtN gluing, and high-frequency control.

The remaining smooth-route issue has now become much more precise. PF-213 proves an abstract weak-trace reassembly theorem once the normalized Schur factors have a summable module-decay envelope. PF-214 shows that, for the simultaneous PF-205 seam cut, the normalized exterior precision

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

is exactly block Jacobi at the form/support level. PF-215 then rules out the simplest sufficient argument: its adjacent normalized blocks diverge on the low symmetric constant modes because the thin one-cusp pant corridor has conductance `\gtrsim s_n^{-1}`.

PF-216 shows that this divergent hopping is accompanied by the missing compensating scale. On a growing embedded Fermi corridor the positive-shift pant energy satisfies

\[
E_n(a,b)\ge c_0(a+b)^2+c_1s_n^{-1}(a-b)^2,
\]

and the PF-205 strip normalization of the symmetric constant module is asymptotically

\[
q_n=2w_nL_n(1+O(w_n^2))\asymp\frac{\log P_n}{P_n}.
\]

Hence the raw low-symmetric form compression obeys

\[
\mathfrak k[f]
\ge c\sum_nq_n^{-1}|x_n|^2
\asymp c\sum_n\frac{P_n}{\log P_n}|x_n|^2.
\]

Equivalently, the large negative cross conductance from PF-215 comes with a comparably large diagonal-sum precision. The uniform-hopping failure is therefore not evidence that `D=(I+K)^{-1}` is nonlocal; the raw constant sector is increasingly coercive.

The unresolved point is that this constant sector is not known to reduce the full pant DtN form. If `P` projects onto the low-symmetric module vectors and `Q=I-P`, the correct object is the effective low form obtained by minimizing the closed form of `I+K` over `Q`-data. That variational elimination can lower the raw low-sector energy and could erase part of the mass/conductance floor. The smooth-route frontier is now **high-mode Schur survival followed by scale-sensitive inverse locality**, not raw-hopping boundedness.

The true-short-collar endpoint remains independent. PF-183 reduces it to disjoint normalized thick slabs, but the required conservative endpoint splice has not yet been completed. The unsmoothed PF-204 route also remains available and could bypass boundary Schur reassembly entirely.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, does the growing PF-216 low-symmetric mass/conductance floor survive variational elimination of the higher tangential boundary modes strongly enough to force a PF-213-compatible decay or weighted-transport estimate for the effective inverse? For the competing unsmoothed route, can PF-204's exact `(dR_g)^*M_{C_0}P_{F_0}dR_+` factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`. PF-216 also changes the likely mechanism. The smooth route would no longer depend on uniform absolute hopping, but on whether a growing coercive low-sector form survives its coupling to high modes and yields locality after inversion.

A negative answer is now more discriminating. On the smooth branch it must exhibit genuine high-mode variational cancellation or failure of the resulting effective inverse transport, rather than infer nonlocality from PF-215's divergent raw cross blocks. On the unsmoothed or true-short-collar branches it must identify a concrete operator-ideal obstruction not already covered by the persisted local estimates.

## Decisive test

Let `\mathfrak a[f]=\|f\|^2+\mathfrak k[f]` be the closed positive form associated with `I+K`. For a finite-support low-symmetric vector `x\in P`, define

\[
\mathfrak s_{\rm low}[x]
:=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}\mathfrak a[x+y].
\]

This form-level shorting is the decisive object and does not assume that unbounded raw blocks of `K` extend boundedly. Whenever a compatible operator-block realization exists it reduces to the usual Schur complement.

Use the PF-207--PF-212 scale/frequency estimates to prove a tail coercivity inequality

\[
\mathfrak s_{\rm low}[x]\ge c\,\mathfrak m_{\rm PF216}[x]
\]

for some fixed `c>0`, where `\mathfrak m_{\rm PF216}` retains a quantitative fraction of PF-216's raw mass/conductance form. If this holds, derive a weighted Green-kernel, Agmon, Combes--Thomas, or equivalent inverse estimate for the resulting variable-coefficient effective chain and test its module transport directly against PF-213's summability envelope.

If the coercivity inequality fails, construct explicit high-mode boundary data whose minimizing contribution cancels an asymptotically non-negligible fraction of the raw PF-216 floor. Positivity alone, separate high-mode bounds without coupling information, or the size of individual raw blocks cannot decide this gate.

As alternative work, attack PF-204's native two-Hilbert-space factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately write one first-relative-resolvent identity for a single global identification and verify every term against persisted sector estimates; mutually incompatible smooth and unsmoothed architectures cannot simply be combined to cover gaps.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-216 proves only a raw quadratic-form compression and explicitly does not prove that the low-symmetric sector reduces `K`. Variational elimination of high modes may weaken the growing floor, so PF-213's inverse-decay hypothesis remains open. PF-204's unsmoothed endpoint and PF-183's true-short-collar endpoint are also unresolved.

Clue acceptance therefore means only that the sharp weak-trace classification remains a concrete, evidence-backed target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. PF-215 closed the uniform normalized-hopping sub-branch negatively; PF-216 closes the first compensating-scale question positively by showing a growing raw low-symmetric mass/conductance floor. The next smooth-route gate is now the survival of that floor under high-mode variational elimination, after which inverse locality can be tested at the actual variable scale. PF-204 and the PF-183 true-short-collar splice remain the two independent competing/complementary gates.