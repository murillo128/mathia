# MI-033 — Finite coefficient constraints survive only as continuous dual traces

**Evidence level:** exact synthesis from [PL-348](../../findings/PL-348-prime-log-modulations-are-a-weil-form-core.md) through [PL-353](../../findings/PL-353-finite-coefficient-constraints-dual-interpolation-gate.md). The dense-kernel lemma, Sobolev duality and Paley--Wiener--Schwartz theory are classical; the Mathia content is their exact application to the overcomplete prime-log modulation family.

Prime-log modulations are already dense enough to form a core for the localized Weil form, so imposing a finite algebraic relation on their coefficients does not automatically create an intermediate test family. PL-353 identifies the exact gate. For

`E = span_alg {e^(i lambda x): lambda=log p}`

inside `H^s(-A,A)`, `0<s<1/2`, a coefficient functional

`L_w(sum c_lambda e^(i lambda x)) = sum c_lambda w_lambda`

has a proper closed kernel **if and only if** it is continuous in the ambient `H^s` topology. Equivalently, its weights must be the prime-log samples of the Fourier--Laplace transform of some continuous dual distribution `T in H^(-s)` supported on the physical window.

This converts “coefficient coupling may prevent completeness” into a precise interpolation problem. If no nonzero linear combination of a finite family of weight sequences has such a continuous-dual interpolant, their joint kernel is still dense. Completion erases the algebraic restrictions completely.

Several natural arithmetic-looking finite laws fail the gate. Finite centering and logarithmic moments correspond to point jets; below the trace threshold `s=1/2`, those delta-type distributions are not continuous duals. Weights of the form `P(log p)p^(-sigma)`, `sigma>0`, would force an entire interpolant with exponential growth on one real half-axis, incompatible with the polynomial real-axis growth of a compactly supported distribution transform. Finite combinations of these constraints therefore leave the endpoint states a full Weil form core.

The reusable distinction is between **algebraic codimension** and **topological codimension in the destination space**. A relation can remove one or many coefficient degrees of freedom before completion and still remove nothing from the closed test family. For any finite source relation, the first question is not how arithmetic-looking its coefficients are but whether the destination topology can see that relation continuously.

This leaves three qualitatively different escape classes: a genuinely source-forced continuous dual trace; an infinite coherent system whose closure is not reducible to finitely many discontinuous hyperplanes; or a nonlinear, cone, target-relative or cross-aperture constraint that changes the object before unrestricted linear completion reconstructs the Weil form. Even a surviving continuous trace only avoids the automatic collapse; it still needs an independent arithmetic sufficiency theorem.

**Boundary.** The result concerns finite linear coefficient constraints in the local subcritical Sobolev/form topology. It does not classify infinite systems, nonlinear constraints, positivity cones, graph/operator-domain restrictions or other ambient topologies such as Hardy, de Branges or Mellin spaces. A relation invisible here may be decisive elsewhere, and a proper closed constrained family is not by itself an RH criterion.
