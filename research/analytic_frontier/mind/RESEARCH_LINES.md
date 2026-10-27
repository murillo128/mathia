# Analytic-frontier research lines

This file holds the current mathematical questions suggested by the durable analytic-frontier intuitions. It is not a roadmap, task queue, status page, or history.

## Optimize the real notch floor after exact multiplicity reduction

[MI-008](intuition/MI-008-small-real-notches-admit-exact-simple-double-reduction.md)
retains ANF-213's exact reduction for `0<eta<=1/2`, `0<a<=1/100`:
the infimum of `sum_(i,j)m_i m_j V(x_i-x_j)/sum_i ell(m_i)` is unchanged
by restricting `m_i` to `1,2` and quarter-interval occupation to at most
four. Here `V=F-a eta sinc^2(eta x)` and `ell(1)=1`, `ell(2)=4`.
Can minimizing sequences still lower this floor through unbounded numbers
of occupied intervals, or can one prove a finite-cardinality reduction
in a specified regime such as `a=lambda eta^3`? The local occupation
bound neither gives a minimum separation nor prevents mass from escaping
to many distant clusters; those are the remaining variational freedoms.

## Decide whether the surviving same-profile cascade is fatally non-excisable

**Linked intuition:** `MI-005-one-pair-collapse-is-curvature-seeded-before-higher-order-effects`.

ANF-134--ANF-143 remove raw depth, span, slack-spend, coefficient-spread, fixed exponential zero-pinching and finite-stage conditioning as existential obstructions to a same-profile cascade. ANF-184 makes the late-layer activation scale explicit. At every frozen admissible stage, the first positive odd-dilation return satisfies

`c_G ell^-2 <= theta_ell <= C_G ell^-2`,

and both integer activation and geometric source resolution occur at the same physical crossover `A~ell^2`: the new saddle lies at distance `Theta_G(ell^-1)` from the old critical skeleton while its Laplace width is `Theta_G(A^-1/2)`.

This removes another qualitative ambiguity from ANF-143. A frozen late layer is not merely cheap; its coefficient density, chamber scale and physical activation clock are quantitatively locked together. What remains uncontrolled is **depth uniformity**: the frozen-stage constants may deteriorate arbitrarily as the cascade evolves.

The live gate is therefore still source-side. Prove that the controlled finite-prefix plus late cloud carries source energy/coherence that cannot be excised without destroying the near-extremizer, or prove a converse excision theorem. Any positive continuation that uses the `ell^2` clock across growing depth must additionally control the stage dependence of the return, curvature and recurrence constants rather than treating the frozen-stage law as uniform.

## Prove or kill the deterministic critical high-pass on the actual source

**Linked intuition:** `MI-007-bow-variance-needs-source-specific-coherence-at-the-distinguished-twist`.

ANF-150--ANF-185 reduce bow variance to a phase-sensitive endpoint-memory problem and identify the sharp physical resolution. A target-sized packet of width `Theta(a_X)` can remain invisible throughout every aperture `o(X/a_X)`, while triangular twist averaging at the deterministic base `X` and critical aperture `T~X/a_X` gives one fixed positive high-pass whose transition width is exactly `a_X`.

ANF-186 closes the next source-blind escape. Even after matching the actual prime-versus-rough coefficient alphabet, the natural positive and negative densities, zero first moment, the correct `asymp log X` diagonal scale and a local absolute-mass envelope `O(H+log X)`, one can place those signs after reading the exact logarithmic carrier and still load endpoint charge `>=a_X` for `Theta(K)` prefixes with negligible diagonal cost.

Thus the one-point source law is not the missing theorem. The surviving distinction is **joint arithmetic placement relative to the distinguished carrier**. A successful continuation must prove `o(a_X)` control of the ANF-185 deterministic weighted prime-minus-Ramanujan residual, control the equivalent signed Fejer scale difference, or prove a source law that prevents the actual prime/rough signs from occupying the carrier-aligned matched-control configuration. Marginals, local absolute mass and diagonal variance cannot substitute for that placement theorem.

## Treat subcritical local complexity and physical aperture as controls, not targets

Low-spectrum abundance, carrier resonance, phase-blind uniformity, coefficient quantization, fixed finite tomography, derivative depth `o(K/a_X)`, physical twist aperture `o(X/a_X)`, and now source-alphabet/marginal matching without placement control are matched controls. On the same-profile branch, frozen-stage odd-dilation activation below `A~ell^2` is likewise a control because the layer is absent or unresolved there.

A viable source theorem must therefore cross the relevant absolute endpoint-memory or physical-resolution scale **and** constrain the arithmetic joint law with the carrier, or exploit nonlocal structure that the matched controls cannot preserve.