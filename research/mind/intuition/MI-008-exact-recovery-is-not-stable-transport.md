# MI-008 — Exact recovery, source normalization, and target-conditioned robustness are different resources

**Evidence level:** supported by the finite inverse/timing/zero-count results through AF-291 and the scalar propagation/Green results through PF-305; no universal target modulus or full mixed-response theorem is claimed.

Arithmetic Fidelity separates acquisition from the final analytic target. AF-282--AF-289 classify genuinely mixed recovery, frame conditioning, and timing perturbations for finite Dirichlet coefficients, with the common timing center removed as the exact gauge `F(s)->F(s+i sigma)`.

AF-290 identifies the finite zero-count target geometry itself. The exact coefficient perturbation radius protecting the zero count is distance to the boundary-zero discriminant,

\[
\operatorname{dist}_2(b,\Delta_\Gamma)
=
\min_{z\in\Gamma}
\frac{|P_b(z)|}{(\sum_{n\le N}n^{-2\operatorname{Re}z})^{1/2}}.
\]

AF-291 then shows that this target radius can deteriorate systematically with breadth even while analytic approximation improves. For raw eta truncations on a fixed zero-free contour, the boundary modulus stays bounded away from zero but the normalized coefficient-space margin tends to zero with an explicit `N`-dependent rate. Thus a breadth-independent relative recovery error cannot be promoted to a uniform zero-count guarantee through this gate.

Prime Flute supplies a complementary normalization phenomenon. PF-303--PF-304 turn the scalar killed Green response into reversible Markov averaging. PF-305 exposes the Hilbert factorization

\[
R_NG_NF_N
=(R_ND_N^{-1/2})\,S_N\,(D_N^{-1/2}F_N),
\qquad
0<S_N\le I,
\quad\|S_N\|=1.
\]

The scalar middle is therefore neutral for symmetric operator ideals. It cannot destroy compactness/ideal decay already present at one normalized conversion vertex, but its exact unit direction means it cannot create the missing decay either. What matters is the geometry of the entrance and exit maps relative to the killing scale.

The cross-line lesson is concrete: **remove exact nuisance symmetries, normalize by the source's own coercive currency, then price the destination's instability in the metric actually used downstream**. Each step can expose a different failure. Stable acquisition can feed a shrinking target margin; a bad bare Green norm can disappear after source normalization; a norm-one middle can still leave all compactness burden at conversion interfaces.

**Boundary.** AF-291 concerns raw eta truncations on fixed compact contours and does not prove universal margin collapse. PF-305 concerns finite scalar-mediated responses and does not prove the physical `P/H` response factors through them. The two geometries are analogous only at the level of resource separation, not by transfer of operators or estimates.
