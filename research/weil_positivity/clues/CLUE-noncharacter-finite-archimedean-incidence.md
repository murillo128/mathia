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
  - research/prime_lattice/findings/PL-169-ratios-one-swap-additive-correlation.md
---

# Is there an intrinsic non-character incidence before Weil positivity is formed?

## Observation

WP-155 rules out obtaining mixed-prime curvature merely by flag/cubical completion of the existing resultant support. WP-157 makes separated determinant densities rank-additive. WP-158 further proves that fixed translated torus-character equations split by prime-primary torsion, so the group law and CRT do not create the missing interaction.

WP-159 kills the simplest additive escape: `x+y=1` collapses to the sixth-root pair, while `x+y=z` has only fixed equilateral relative geometry. WP-160 then closes the whole fixed finite-arity algebraic continuation using toric Manin--Mumford: any scalable torsion locus of a fixed Laurent-polynomial incidence lies in finitely many torsion cosets and therefore reduces back to the translated-character category of WP-158.

WP-161 tests the first source-forced escape that genuinely leaves that category: a moving non-torsion real radial point coupled by logarithmic chord product to a primitive shell. The construction is not empty or artificial: its centered boundary value is exactly `log Phi_n(1)=Lambda(n)`. But the complete local differential germ separates from that selector. Its positive boundary curvature is `J_2(n)/12`, and every higher centered even derivative is a Bernoulli multiple of `J_{2k}(n)`, hence has full shell support. The exact control `n=6` already has zero Mangoldt boundary value but strictly positive radial curvature. A shared radial scalar is also additive over shell logarithmic potentials, so it does not create irreducible cross-prime incidence by itself.

A separate literature audit, PL-169, identifies the first classical ratios off-diagonal with the additive relation `m=n+h` between multiplicative coefficients. This is a conditional ratios/correlation interface, not an unconditional sign theorem. It illustrates the kind of extra relation absent from independent prime-coordinate operations; it does not supply a Weil-positive form.

## Research question

Can the existing source geometry force one explicit non-character relation coupling different finite primes or a finite prime with the real place, before taking a determinant, norm, or positivity projection? After WP-160, a surviving relation must leave the class of a fixed finite-arity algebraic subvariety of the torsion torus. After WP-161, merely introducing the canonical real radial scale and using a local finite-order differential/curvature readout is also insufficient: the arithmetic selector remains at zero order while the sign-bearing jet becomes Jordan-totient.

The remaining escape therefore needs more than a real parameter. Plausible categories are a source-forced nonlocal radial/boundary operator, a varying or growing-arity incidence whose dependence is not reducible to a fixed torsion variety, a nonalgebraic metric/differential coupling with genuinely mixed finite-place response, or a finite--archimedean construction in which the same global operation creates both the Mangoldt cancellation and the sign theorem.

The question is the incidence itself, distinct from the accepted clue about quotienting an already positive mixed-prime completion.

## Why it may matter

This targets the missing ingredient upstream of the repeatedly unsuccessful positive completions. A negative calculation can reject a candidate before elaborate cohomology is built; a surviving incidence would give a specific object on which a sign mechanism could subsequently be tested.

The Laurent reduction is useful because it removes a large false escape class: merely choosing a more complicated fixed polynomial in roots of unity cannot provide the required scalable cross-prime geometry. WP-161 removes a second tempting shortcut: the natural radial real deformation does recover the exact Mangoldt boundary value, but local geometric differentiation destroys the support and scale. The remaining search can focus on structures whose global dependence is genuinely additional rather than hidden inside a fixed torsion variety or a local radial jet.

## Decisive test

Choose one relation already forced by the full embedded-root/chord or finite--archimedean construction, and justify why it is canonical rather than a weight chosen for its desired answer. Compute its smallest two-place restriction before scalarization. Show whether its solution set and response factor after primary decomposition; for a differential formulation, calculate a mixed variation and separate genuine interaction from a logarithm, rank normalization, or local radial-curvature artifact.

The first gate is a nonzero source-forced mixed response outside WP-158's translated-character class, WP-160's fixed-algebraic torsion reduction, and WP-161's place-separable radial finite-jet class. If it survives, specify the natural measure/domain and compare its finite and archimedean coefficients with the same Weil normalization. Then identify the independent theorem that could force the sign. A relation reducing to characters, CRT, rank additivity, a fixed Laurent-polynomial torsion locus, a shellwise radial jet, arbitrary coordinates, or an inserted Weil kernel kills that candidate. Mere nonseparability is insufficient for positivity.

## Evidence boundary

No surviving incidence, measure, global form, or sign theorem is established. WP-160 proves only that fixed finite-arity algebraic torsion incidence cannot supply scalable irreducible mixed-prime geometry. WP-161 proves only that the canonical shell-to-real radial log-product carries `Lambda(n)` at zero order while its local differential sign data are Jordan-totient and shellwise separable. Neither result excludes source-forced nonlocal radial operations, varying/growing families, genuinely mixed nonalgebraic relations, boundary/operator structures, or a finite--archimedean coupling whose global sign acts before that separation.

The PL-169 analogy supplies neither a canonical relation in this geometry nor an unconditional analytic estimate.

## Research disposition

Accepted, with the search category materially narrowed by WP-159--WP-161. The fixed algebraic root-of-unity route is closed: finite torsion exceptions cannot scale, while infinite torsion families classicalize to torsion cosets and split prime by prime. The simplest non-torsion real deformation is now also classified: it exactly recovers the Mangoldt selector as a boundary potential value, but its positive local Hessian and higher differential jet have the wrong full-support Jordan-totient arithmetic.

The unresolved question is whether Mathia forces a **genuinely global or nonlocal incidence before positivity is formed**, especially one in which finite and archimedean data participate in the same source geometry and the same sign-bearing operation retains, rather than reconstructs afterward, the prime-power cancellation.
