# MI-067 — A diffuse modular centralizer can erase exact arithmetic point support

**Evidence level:** exact operator-algebraic synthesis from [WP-395](../../findings/WP-395-critical-kms-centralizer-erases-exact-prime-power-orbit-support.md), testing the genuine critical-KMS/von-Neumann escape left by WP-394.

Moving to a genuinely larger source-derived category does not guarantee that the arithmetic observable one wants remains meaningful there. WP-395 computes the modular centralizer of the original Bost--Connes critical `KMS_1` state:

`M_phi = pi_phi(C*(Q/Z))'' ~= L^infinity(hat Z, m_Haar)`.

This is a real von Neumann enlargement of the norm-closed diagonal `C(hat Z)`, and affiliated self-adjoint operators are measurable multipliers. But the completion is diffuse. Every standard arithmetic orbit `{n alpha:n>=1}` and its prime-power subset `{p^j alpha}` are countable and therefore Haar-null.

That produces a two-sided obstruction to an exact prime-power selector inside, or affiliated with, the modular centralizer. Literal operator support contained in the prime-power orbit has zero support projection and hence gives the zero operator. If instead one prescribes point values on prime-power versus mixed-prime orbit points, those assignments occur on a null set and can be changed arbitrarily without changing the `L^infinity` class or the affiliated operator. The requested distinction is then not an operator invariant at all.

The mechanism differs from the earlier bounded no-go results. WP-392 kept the arithmetic basis visible but forced positive mixed-prime-null bounded elements to vanish. WP-393 showed that Woronowicz affiliation did not enlarge the original unital C-star algebra. WP-394 allowed genuinely unbounded forms but pulled them back through a source-valued resolvent. WP-395 really changes category; the obstruction is now that the measure-class quotient itself forgets the discrete orbit.

The reusable lesson is that category enlargement has two independent gates: it must add the needed operator freedom **and preserve the source datum as a non-null invariant of that category**. A diffuse completion can be strictly larger while destroying exact point-support questions.

**Boundary.** WP-395 concerns the modular centralizer of the critical Bost--Connes KMS factor, not the whole noncommutative factor or arbitrary noncentral modular spectral subspaces. Positive-measure arithmetic cylinder sets remain visible. The result rules out exact prime-power support on standard countable orbits inside the centralizer; it does not rule out a different source-forced positive form or global sign mechanism whose arithmetic content is encoded by positive-measure, noncentral, module, boundary or finite--archimedean structure.