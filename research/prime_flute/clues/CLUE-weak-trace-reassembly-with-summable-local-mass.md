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
  - research/prime_flute/findings/PF-217-tangential-boundary-screening-erases-the-raw-pant-mass-floor-after-shorting.md
  - research/prime_flute/findings/PF-218-raw-mass-damping-cannot-accompany-summable-low-schur-transport.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, while several exact sectors sit at the natural two-dimensional weak endpoint. PF-189 controls the complete fixed-central short-collar sector. PF-196--PF-201 control the regular Lambert-body critical sector, including matrix-valued `L\log L` localization and off-diagonal reassembly. PF-203/PF-204 provide an exact unsmoothed two-native-resolvent factorization for the decomposition interfaces, while PF-205--PF-212 develop a competing smooth boundary route with natural-width strips, scale-matched commutators, low-mode counting, energy-normalized DtN gluing, and high-frequency control.

The smooth-route Schur problem is now sharply constrained. PF-213 gives a sufficient reassembly theorem once normalized Schur factors have a summable module-decay envelope. PF-214 identifies the simultaneous seam precision as block Jacobi. PF-215 rules out uniform bounded adjacent normalized hopping. PF-216 then finds a compensating growing mass/conductance floor on the **raw symmetric constant compression**.

PF-217 closes the next proposed gate negatively. If `P` projects onto those low-symmetric module vectors and `Q=I-P`, the shorted form

\[
\mathfrak s_{\rm low}[x]
=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}\mathfrak a[x+y]
\]

does not retain any fixed positive fraction of PF-216's raw mass currency. Tangentially localized boundary bumps preserve a macroscopic low-symmetric projection while avoiding the growing-corridor ends responsible for the positive-shift onsite floor; a slowly varying tail envelope makes the remaining conductance energy sublinear.

PF-218 now passes that obstruction through the **actual inverse**. If `S` is the operator represented by the shorted form, then

\[
S^{-1}=P(I+K)^{-1}P=PDP.
\]

Writing `W\nu_n=q_n^{-1}\nu_n`, the PF-217 tail vectors force the finite-block norms of `W^{1/2}PDPW^{1/2}` to diverge. Therefore the screened inverse cannot satisfy any tail-uniform transport envelope of the form

\[
|\langle\nu_m,D\nu_n\rangle|
\le C\sqrt{q_mq_n}\,\eta_{m-n},
\qquad \eta\in\ell^1.
\]

So the smooth branch must no longer try either to prove `\mathfrak s_{\rm low}\gtrsim\mathfrak m_{\rm PF216}` or to recover the same raw `q_n` currency as endpoint damping of the inverse. What remains open is whether the **coefficient-weighted screened inverse** still has enough structure for PF-213-compatible reassembly once the physical `d_n` perturbation scale is retained. The unsmoothed PF-204 route and PF-183 true-short-collar route remain independent alternatives.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, what is the leading effective low form after the PF-217 tangential screening directions are actually minimized out, and does the **physical-coefficient-weighted inverse** satisfy a PF-213-compatible module transport estimate? PF-218 shows that one cannot first demand a `q_n^{1/2}` damping factor from each endpoint of `PDP` and then attach the smaller `d_n` coefficient afterwards. For the competing unsmoothed route, can PF-204's exact `(dR_g)^*M_{C_0}P_{F_0}dR_+` factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`.

PF-217 and PF-218 make the remaining smooth question more discriminating. Large raw pant conductance, raw onsite coercivity, and raw-`q` inverse damping are all insufficient descriptions after Schur elimination. Any successful smooth proof must expose the genuinely screened variable-coefficient boundary chain and estimate the inverse **in the same physical coefficient currency in which the relative-resolvent word is assembled**. Conversely, failure of that actual coefficient-weighted transport would be a substantive obstruction rather than an artifact of a raw compression or an overstrong endpoint normalization.

## Decisive test

Work directly with the exact closed form

\[
\mathfrak a[f]=\|f\|^2+\mathfrak k[f]
\]

and its low short

\[
\mathfrak s_{\rm low}[x]
=\inf_{y\in Q\operatorname{Dom}(\mathfrak a)}\mathfrak a[x+y].
\]

PF-217 has already falsified a fixed-fraction lower bound by the PF-216 raw mass floor, and PF-218 has falsified the corresponding `q`-damped summable inverse-transport completion. The next decisive calculation is therefore to identify upper and lower asymptotic weights for `\mathfrak s_{\rm low}` itself after tangential screening **or** to bypass a standalone model for `D` and estimate the actual `d_n`-weighted recoupling blocks directly.

If an explicit screened form is derived, estimate its Green kernel only in a weight that survives PF-218. A successful smooth result must control the actual effective inverse with the physical `d_n` coefficient present; it cannot infer locality from raw `K` blocks, raw constant-mode coercivity, or a hypothetical uniform `PDP\lesssim\operatorname{diag}(q_n)` bound. A negative result should exhibit a concrete family of low data whose **coefficient-weighted** screened Green response violates every candidate PF-213 transport envelope.

As alternative work, attack PF-204's native two-Hilbert-space factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately write one first-relative-resolvent identity for a single global identification and verify every term against persisted sector estimates; mutually incompatible smooth and unsmoothed architectures cannot simply be combined to cover gaps.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-217 proves only that PF-216's raw low-symmetric onsite floor is not stable under the variational elimination defining the correct low Schur form. PF-218 proves the exact inverse consequence that the low compression `PDP` cannot have a tail-uniform `q`-damped summable transport envelope. Neither result determines the screened effective form, proves slow unweighted inverse decay, refutes PF-213's sufficient locality criterion, or shows that the smooth architecture fails. PF-204's unsmoothed endpoint and PF-183's true-short-collar endpoint are also unresolved.

Clue acceptance therefore means only that the sharp weak-trace classification remains a concrete, evidence-backed target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. PF-217 resolves the previous "survival of the PF-216 raw floor" test negatively, and PF-218 removes the next raw-weight completion: the exact low Schur inverse cannot combine `q_n^{1/2}` endpoint damping with summable module transport. The smooth branch now has one sharper gate: derive and invert the **screened** effective boundary form in a weaker weight, or estimate the actual `d_n`-weighted recoupling operator directly. PF-204 and the PF-183 true-short-collar splice remain the two independent competing/complementary gates.