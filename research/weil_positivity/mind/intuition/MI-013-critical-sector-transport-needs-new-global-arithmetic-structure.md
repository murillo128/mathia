# MI-013 — Critical prime-layer coherence exists as a finite part, but its sign and Weil scale are regulator-dependent

**Evidence level:** supported by the exact Fock coefficient carrier and correlation/renormalization boundaries through WP-265; a regulator-independent completed Weil orientation remains open.

WP-256 produces the exact positive Mangoldt half-density from prime-word multiplicity and arithmetic energy. WP-259 passes canonically to the permutation-fixed sector, restoring the `beta=1` Gibbs boundary while retaining the prime-power diagonal `Lambda(n)/sqrt(n)`. WP-260 shows that canonical bosonic Gibbs/Fisher convexity inserts the wrong occupation factor.

WP-261--WP-263 test increasingly global cross-prime mechanisms. Finite-dimensional coherent collapse is nonclosable at the critical scale. Infinite-dimensional locally finite incidence is bounded but leaves support/phases programmable. Conditional-Gibbs complete incidence lets the source Hamiltonian choose a canonical weighted complete graph, but critical unit-diagonal normalization collapses fixed prime-prime correlations because `sum_p1/p` diverges.

WP-264 shows that this collapse hides a nontrivial finite part. Its cutoff Gram decomposes as

\[
M_X=H_XD_W+a_Xa_X^*-2D_X,
\]

and removing the divergent diagonal coefficient exposes `R=aa^*-2D`, with exactly one positive direction and strict negativity on `ker a^*`. The shifted family `R_C=R+CD_W` then shows that the sign theorem alone does not fix the finite normalization.

WP-265 realizes both sides of this ambiguity using natural source-compatible regulators. With a sharp prime cutoff, subtracting only `\log\log X\,D_W` leaves

\[
R_{B_1},\qquad B_1>0,
\]

which has infinite positive index. With Gibbs/Abel damping, subtracting only `\log(1/\varepsilon)D_W` leaves

\[
R_{B_1-\gamma},\qquad B_1-\gamma<0,
\]

which has exactly one positive direction. Thus regulator choice changes the qualitative inertia class, not merely a harmless scalar convention.

Both schemes can be forced to converge to `R_0`, but only by adding different finite constants, differing by exactly `\gamma`. That reconciliation is an extra finite-part prescription. The source Hamiltonian and local positivity construction, by themselves, therefore do not determine a regulator-independent Hodge/Weil form.

The missing structure must now be **regulator-selecting or regulator-covariant**. A successful global construction should derive the finite subtraction before looking at the desired Weil coefficient and either prove why one regulator is geometrically canonical or show how regulator shifts are compensated by an archimedean/polar boundary term so that the completed form is invariant. A counterterm chosen to recover index one or the target half-density remains programmable.

**Boundary.** WP-265 does not rule out a canonical boundary response, quotient, cohomological construction, non-scalar subtraction, or regulator-covariant completion. It shows that the current complete-incidence source plus leading-divergence subtraction is insufficient even to make the critical inertia regulator-independent.