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
---

# Can the weak-trace endpoint be completed from the remaining interface and splice sectors?

## Observation

The endpoint problem has narrowed substantially. PF-189 proves weak `S_1` for the complete fixed-central short-collar sector and PF-173 makes its matched recoupling trace summable. PF-191 gives the exact-area Lambert/body comparison a summable strong-`L^1` defect, while PF-196 identifies the correct critical coefficient currency: the `L\log L` Luxemburg norm costs one geometric concentration logarithm but the exact prime/shift tail still pays every fixed polynomial Lambert-depth loss. PF-197 then supplies the matrix-valued critical Cwikel theorem needed for the localized two-dimensional gradient form.

PF-198--PF-201 remove the main regular-body analytic uncertainties one by one. PF-198 shows that cutting the long Lambert body into fixed-width windows preserves the total prime-summable `L\log L` coefficient budget. PF-199 shows that genuine two-sided finite-color localization causes no weak-trace counting loss. PF-200 makes the local Cwikel constants uniform on the regular recentered Lambert-body family. PF-201 then improves the architecture further: coefficient-side localization plus an auxiliary Hilbert direct sum gives the exact factorization

\[
T_{\rm reg}=A_h^*DA_g\in\mathcal S_{1,\infty}
\]

for the **entire regular Lambert-body principal cotangent coefficient sector**, with the global resolvents left uncut. The external off-diagonal remainder previously associated with that regular sector is therefore not a live obstruction and should not be recreated in future endpoint decompositions.

PF-202 closes the coefficient-space part of one remaining exceptional family. PF-182's distinguished decomposition-cuff seam correction can be supported arbitrarily thinly with no inverse-width first-derivative penalty and with any prescribed summable weighted `L^1` budget. Combining that freedom with PF-196's Luxemburg estimate shows that the seam cotangent coefficients can have an arbitrarily prescribed summable tail `L\log L` budget. Exact area kills the local scalar density coefficient. What remains at those cuffs is **operator localization**, not coefficient concentration: shrinking support can still worsen higher derivatives, fixed-buffer elliptic constants, or pseudodifferential chart constants, so PF-201 cannot simply be copied to the seam family without a new quantitative argument.

The geometric endpoint remains independent. PF-183 reduces the complete true-short-collar family to one energy-local conservative splice on disjoint normalized thick slabs. PF-184--PF-188 remove flux, the marked Killing mode, qualitative Sobolev degeneration, and boundary-normalization as generic qualitative obstructions, while PF-192/PF-194 show that a generic strong-`L^1` linear rigidity theorem cannot supply the endpoint. A successful endpoint splice must use additional canonical structure or a genuinely weak/critical formulation.

Thus the accepted clue no longer asks whether ordinary regular Lambert localization or its external off-diagonal tails can be controlled. The live question is whether the **non-regular interface families plus the canonical true-short-collar splice** can be put into the same prime-summable weak endpoint without recreating a global logarithmic loss.

## Research question

Can the exact prime/shift first relative resolvent be decomposed as

\[
T=T_{\rm reg}+T_{\rm central}+T_{\rm interface}+T_{\rm splice}+T_{\rm rem},
\]

where PF-201 controls `T_reg` in `S_{1,\infty}`, PF-189/PF-173 control the central sector and recoupling, and every remaining interface/splice/remainder term is trace class or weak `S_1` with a prime-summable counting budget, so that

\[
(\Delta_{g_+}+1)^{-1}F_*-F_*(\Delta_g+1)^{-1}
\in\mathcal S_{1,\infty}?
\]

For the distinguished decomposition cuffs, PF-202 says the coefficient norm can be made arbitrarily summable. The precise analytic question is whether the corresponding localized resolvent/Cwikel constants can be kept uniform, can grow slowly enough to be absorbed by the support-budget freedom, or can be bypassed by a stronger trace-class interface estimate.

For the true PF-138 short collars, the separate question is whether the canonical exact-area body/core interpolation admits an endpoint conservative splice whose local cost is summable in the correct strong-`L^1` or critical weak currency. No generic `L^1` Korn/rigidity theorem may be assumed after PF-192/PF-194.

## Why it may matter

A positive answer would establish the natural global endpoint suggested independently by the two-dimensional pseudodifferential order, PF-189's exact central calculation, and the critical Cwikel theory:

\[
T\in\mathcal S_{1,\infty}
\quad\text{while PF-112 gives}\quad
T\notin\mathcal S_1.
\]

That would show that PF-190's `O(\log^2 n/n)` global singular-value envelope came from strong-Schatten extrapolation rather than from the regular Lambert geometry or coefficient fragmentation. More importantly for the canonical composite-shift control, it would sharply classify how much of the prime flute's first-resolvent operator structure survives a literal-primality-destroying comparison.

A negative answer is useful only if it identifies a genuine remaining mechanism: a width-dependent interface operator constant that defeats arbitrary coefficient thinning, a canonical short-collar endpoint localization obstruction, or another explicitly derived global term that cannot be assigned a prime-summable weak-trace budget. Reintroducing already-closed regular-body window count, Cwikel-constant, or external off-diagonal concerns is not a decisive negative result.

## Decisive test

First isolate the **distinguished-cuff operator sector** using PF-202 rather than redoing its coefficient estimate. Let `K_n` denote the actual constant needed to convert the seam coefficient on `U_n` into a weak-`S_1` bound after whatever local chart/resolvent factorization is used. Determine how `K_n` depends on the shrinking support width, map regularity, cuff geometry, and the required source/target buffers. The seam route succeeds if the PF-182 support choice can be made so that

\[
\sum_n K_n\,
\|C_n\|_{L\log L}<\infty,
\]

or if an alternative direct interface argument gives a summable trace/weak-trace norm. Because PF-202 allows the coefficient tail budget to be prescribed arbitrarily small, any **finite cuffwise constant known before the support choice** is potentially absorbable; what must be audited is whether shrinking the support itself makes `K_n` depend circularly on that choice too fast. Do not assume the fixed-width PF-200 constant applies to these shrinking seams.

Second classify the other finitely-many-per-module exceptional windows that PF-200/PF-201 deliberately excluded: module ends, physical cuff/body transmission, corner/assembly corrections, and any remaining coefficient pieces outside the regular recentered family. For each infinite family, derive its actual coefficient scale and either place it in a uniform/prime-summable global-to-local critical factorization or prove a stronger summable remainder estimate. A fixed number of exceptional windows **per module** is still an infinite family and cannot be discarded as a finite head.

Third settle the **true-short-collar endpoint splice**. On PF-183's disjoint normalized thick slabs, use PF-191's endpoint body budget and PF-184 exactness to construct or refute an exact-area marked interpolation with a cuffwise estimate schematically of the form

\[
E_1(\operatorname{splice}_\eta;T_\eta)
\le
C\bigl(E_1^{\rm body}(T_\eta)+|t_\eta|\bigr),
\]

or an explicitly identified critical Lorentz/Orlicz analogue sufficient for weak `S_1`. PF-192/PF-194 forbid justifying this by generic strong-`L^1` rigidity. A negative result must be canonical to the PF germ or prove that every admissible conservative interpolation incurs a non-summable endpoint cost.

Finally write the global first-relative-resolvent form explicitly in the completed exact-area identification and verify that every term belongs to one of the proved sectors. In the exact-area gauge the density coefficient vanishes where that gauge is established, so do not manufacture a scalar density remainder there. Likewise do not insert external input/output cutoffs into the PF-201 regular sector merely to create off-diagonal terms that its exact `A_h^*DA_g` factorization already avoids.

## Evidence boundary

No global weak-`S_1` theorem is established. PF-201 proves only the regular Lambert-body principal cotangent contribution. PF-202 proves only a critical **coefficient-space** budget for the distinguished decomposition-cuff correction; it does not control the shrinking-family local Cwikel constants or produce its weak-trace operator estimate. PF-189/PF-173 concern the central short-collar sector and recoupling, not the complete geometric comparison.

The PF-183 true-short-collar endpoint conservative splice remains unproved. PF-191 supplies endpoint body mass, PF-184 exactness, and PF-185--PF-188 useful marked rigidity structure, but PF-192/PF-194 rule out promoting that structure to a generic strong-`L^1` linear theorem. PF-190 therefore remains the persisted full weighted-endpoint consequence until the interface and splice sectors are closed.

The clue also makes no wave-operator, scattering-matrix, determinant, resonance, or RH claim. Weak `S_1` of the complete first relative resolvent, if eventually proved, would be an operator-ideal classification of the exact prime/shift control and must be interpreted with the line README's arithmetic-control discipline.

## Research disposition

The clue remains `accepted`, but its analytic frontier is materially narrower. **Regular Lambert-body critical localization is now closed through PF-201, and distinguished-cuff coefficient concentration is closed through PF-202.** The active work is: (1) operator control of the shrinking distinguished-cuff and other exceptional interface families, and (2) the canonical endpoint conservative splice on the true PF-138 short collars. Future work should attack those two gates directly rather than reopening regular-body window fragmentation, finite-color counting, local Cwikel uniformity, or its external off-diagonal remainder.