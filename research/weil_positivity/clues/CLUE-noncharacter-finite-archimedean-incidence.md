---
id: CLUE-weil-positivity-noncharacter-finite-archimedean-incidence
type: research-clue
status: accepted
origin: master-researcher
target_line: weil_positivity
based_on:
  - research/weil_positivity/findings/WP-155-canonical-resultant-cell-completions-cannot-create-mixed-prime-curvature.md
  - research/weil_positivity/findings/WP-157-separated-cyclotomic-tensor-determinant-lines-are-rank-additive.md
  - research/weil_positivity/findings/WP-158-torus-character-correspondences-split-over-prime-primary-shells.md
  - research/weil_positivity/findings/WP-159-unit-coefficient-three-term-additive-torsion-collapses-to-sixth-root-geometry.md
  - research/weil_positivity/findings/WP-160-toric-manin-mumford-closes-fixed-algebraic-torsion-incidence.md
  - research/weil_positivity/findings/WP-161-radial-cyclotomic-boundary-value-is-mangoldt-but-its-differential-jet-is-jordan-totient.md
  - research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md
  - research/prime_lattice/findings/PL-169-ratios-one-swap-additive-correlation.md
---

# Is there an intrinsic non-character incidence before Weil positivity is formed?

## Observation

WP-155 rules out obtaining mixed-prime curvature merely by flag/cubical completion of the existing resultant support. WP-157 makes separated determinant densities rank-additive. WP-158 further proves that fixed translated torus-character equations split by prime-primary torsion, so the group law and CRT do not create the missing interaction.

WP-159 kills the simplest additive escape: `x+y=1` collapses to the sixth-root pair, while `x+y=z` has only fixed equilateral relative geometry. WP-160 then closes the whole fixed finite-arity algebraic continuation using toric Manin--Mumford: any scalable torsion locus of a fixed Laurent-polynomial incidence lies in finitely many torsion cosets and therefore reduces back to the translated-character category of WP-158.

WP-161 tests the first source-forced escape that genuinely leaves that category: a moving non-torsion real radial point coupled by logarithmic chord product to a primitive shell. The construction is not empty or artificial: its centered boundary value is exactly `log Phi_n(1)=Lambda(n)`. But the complete local differential germ separates from that selector. Its positive boundary curvature is `J_2(n)/12`, and every higher centered even derivative is a Bernoulli multiple of `J_{2k}(n)`, hence has full shell support. The exact control `n=6` already has zero Mangoldt boundary value but strictly positive radial curvature. A shared radial scalar is also additive over shell logarithmic potentials, so it does not create irreducible cross-prime incidence by itself.

WP-162 then tests the whole radial path rather than another finite jet. For the canonical interior potential `G_n(s)=log Phi_n(e^{-s})`, the inward flux `rho_n=-G_n'` has exact total mass `Lambda(n)`. Prime powers are exactly the shells on which this flux is pointwise positive; every non-prime-power has positive boundary flux but zero total mass and therefore must develop a negative region. Thus the nonlocal radial selector survives only as signed cancellation. Any shellwise pointwise-positive bulk scalarization of that flux — total variation, an `L^q` size, a square, or any strictly positive local density — becomes nonzero on every shell and loses Mangoldt support. Even positive exponential damping already makes the `n=6` readout nonzero.

A separate literature audit, PL-169, identifies the first classical ratios off-diagonal with the additive relation `m=n+h` between multiplicative coefficients. This is a conditional ratios/correlation interface, not an unconditional sign theorem. It illustrates the kind of extra relation absent from independent prime-coordinate operations; it does not supply a Weil-positive form.

## Research question

Can the existing source geometry force one explicit non-character relation coupling different finite primes or a finite prime with the real place, before taking a determinant, norm, or positivity projection? After WP-160, a surviving relation must leave the class of a fixed finite-arity algebraic subvariety of the torsion torus. After WP-161, merely introducing the canonical real radial scale and using a local finite-order differential/curvature readout is insufficient: the arithmetic selector remains at zero order while the sign-bearing jet becomes Jordan-totient. After WP-162, using the whole radial path is not enough if positivity is imposed pointwise along that path: the exact Mangoldt mass then relies on signed cancellation on every mixed shell, and positive shellwise bulk energies erase it.

The remaining escape therefore needs more than a real parameter or a positive radial density. Plausible categories are a source-forced nonlocal radial/boundary operator that retains signed finite information until after cross-shell coupling, a varying or growing-arity incidence whose dependence is not reducible to a fixed torsion variety, a nonalgebraic metric/differential coupling with genuinely mixed finite-place response, or a finite--archimedean construction in which the same global operation creates both the Mangoldt cancellation and the sign theorem.

The question is the incidence itself, distinct from the accepted clue about quotienting an already positive mixed-prime completion.

## Why it may matter

This targets the missing ingredient upstream of the repeatedly unsuccessful positive completions. A negative calculation can reject a candidate before elaborate cohomology is built; a surviving incidence would give a specific object on which a sign mechanism could subsequently be tested.

The Laurent reduction is useful because it removes a large false escape class: merely choosing a more complicated fixed polynomial in roots of unity cannot provide the required scalable cross-prime geometry. WP-161 removes a second tempting shortcut: the natural radial real deformation does recover the exact Mangoldt boundary value, but local geometric differentiation destroys the support and scale. WP-162 removes the most direct positive nonlocal continuation: integrating the whole radial derivative recovers Mangoldt exactly, but mixed-prime zeros are cancellations, so norming or making the flux positive shell by shell necessarily introduces false support. The remaining search can focus on structures whose global dependence is genuinely additional and whose positivity acts only after the required signed finite information has participated in a global coupling.

## Decisive test

Choose one relation already forced by the full embedded-root/chord or finite--archimedean construction, and justify why it is canonical rather than a weight chosen for its desired answer. Compute its smallest two-place restriction before scalarization. Show whether its solution set and response factor after primary decomposition; for a differential formulation, calculate a mixed variation and separate genuine interaction from a logarithm, rank normalization, local radial-curvature artifact, or shellwise positive bulk norm.

The first gate is a nonzero source-forced mixed response outside WP-158's translated-character class, WP-160's fixed-algebraic torsion reduction, WP-161's place-separable radial finite-jet class, and WP-162's shellwise pointwise-positive radial-flux class. The exact `n=6` flux is now a required radial control: a candidate that first replaces the signed flux by `|rho|`, `rho^2`, an `L^q` norm, total variation, or any strictly positive local energy density has already lost the selector before finite--archimedean assembly.

If a candidate survives, specify the natural measure/domain and compare its finite and archimedean coefficients with the same Weil normalization. Then identify the independent theorem that could force the sign. A relation reducing to characters, CRT, rank additivity, a fixed Laurent-polynomial torsion locus, a shellwise radial jet, a pointwise-positive radial bulk energy, arbitrary coordinates, or an inserted Weil kernel kills that candidate. Mere nonseparability is insufficient for positivity.

## Evidence boundary

No surviving incidence, measure, global form, or sign theorem is established. WP-160 proves only that fixed finite-arity algebraic torsion incidence cannot supply scalable irreducible mixed-prime geometry. WP-161 proves only that the canonical shell-to-real radial log-product carries `Lambda(n)` at zero order while its local differential sign data are Jordan-totient and shellwise separable. WP-162 proves that its canonical boundary-to-origin radial flux has net mass `Lambda(n)`, but mixed-prime zeros require sign cancellation and therefore cannot survive ordinary pointwise-positive bulk scalarization. None of these results excludes a global operator that keeps the signed radial data through a cross-shell or finite--archimedean coupling and proves positivity only after assembly, nor do they exclude varying/growing families or genuinely mixed nonalgebraic relations.

The PL-169 analogy supplies neither a canonical relation in this geometry nor an unconditional analytic estimate.

## Research disposition

Accepted, with the search category materially narrowed by WP-159--WP-162. The fixed algebraic root-of-unity route is closed: finite torsion exceptions cannot scale, while infinite torsion families classicalize to torsion cosets and split prime by prime. The simplest non-torsion real deformation is also classified at both local and direct nonlocal levels: it exactly recovers the Mangoldt selector as a boundary potential and as net inward radial flux, but its positive local Hessian/higher jet have the wrong full-support arithmetic, while its exact nonlocal selector depends on signed cancellation that shellwise positive bulk energies destroy.

The unresolved question is whether Mathia forces a **genuinely global or nonlocal incidence before positivity is formed**, especially one in which finite and archimedean data participate in the same source geometry, signed finite-place cancellation is retained through the coupling, and the final sign theorem applies to the assembled form rather than to each shell or radial point separately.
