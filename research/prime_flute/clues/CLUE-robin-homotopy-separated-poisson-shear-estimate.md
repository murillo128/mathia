---
id: CLUE-prime-flute-robin-homotopy-separated-poisson-shear-estimate
type: research-clue
status: proposed
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold.md
  - research/prime_flute/findings/PF-241-scaled-tangential-blowup-turns-the-shear-interior-into-a-uniform-long-strip-family.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can a fixed-seam Robin homotopy close the high-high shear estimate before global reassembly?

## Observation

PF-240 needs more than one total scaled boundary derivative, with an `O(beta)` constant, for the actual-seam-normalized shear difference. PF-241 removes shrinking-width loss of interior ellipticity, but leaves the Hardy ends, growing strip length, and noncommuting seam normalization. The accepted weak-trace clue already asks for this estimate; the additional proposal here is a specific variational factorization that keeps the perturbative coefficient outside the regularity argument.

A bound for the direct shear multiplier is not a bound for the full Schur map. Conversely, estimating the two normalized maps separately discards their small difference. Interpolate the interior shear while holding the actual seam fixed, and differentiate the already-normalized inverse. The resulting bilinear form should have one explicit shear factor and two boundary-source solutions.

## Research question

With exactly the PF-238 actual complete-lift seam `Q=diag(Q_1,Q_2)`, let `Lambda_t` be the corridor Dirichlet-to-Neumann map obtained by replacing `b` with `t b`, for `0<=t<=1`. In the original trace coordinates, set

\[
D_t=(I+Q^{-1/2}\Lambda_tQ^{-1/2})^{-1}
    =Q^{1/2}(\Lambda_t+Q)^{-1}Q^{1/2}.
\]

Can the form-domain version of this identity and its variational derivative yield, for some fixed `r>1/2` and `Z>0`,

\[
\left\|K_a^r P_Z(D_1-D_0)_{21}P_ZK_a^r\right\|
\le C_{r,Z}\beta,\qquad P_Z=\mathbf1_{(Z,\infty)}(K_a),
\]

uniformly on the canonical tail? This is a sufficient route to the existing PF-240 gate, not a new requirement that its full exponential diagonal envelope survive.

## Why it may matter

A positive result would turn the entire remaining local shear correction into an absolutely trace-summable error after the reciprocal-prime weight, using PF-240 and the already-controlled low-touch part. The immediate downstream test would then be physical `P/H` recoupling and finite-pant completion, not another coefficient-locality lemma. A failure of this factorization's sufficient estimates would identify a more precise boundary-domain or normalization problem without falsely disproving the original high-high target.

## Decisive test

**Differentiate with the seam fixed.** First use real test data, and then polarize. If `gamma` is the boundary trace, define `u_{t,f}` variationally by

\[
q_t[u_{t,f},v]+\langle Q^{1/2}\gamma u_{t,f},
 Q^{1/2}\gamma v\rangle
=\langle Q^{1/2}f,\gamma v\rangle.
\]

Prove existence on the appropriate completed trace/energy spaces, justify the boundary Schur identity, and independently reconstruct

\[
\langle f,\dot D_t g\rangle
=-\dot q_t[u_{t,f},u_{t,g}].
\]

Use bounded spectral regularizations if necessary and remove them uniformly; a formal inverse derivative on unbounded products is not a domain proof. The homotopy does not change `Q`, so no derivative of its square root should be introduced.

In PF-241's long-strip coordinates, write
\(\mathcal T_s=A_s(\partial_Y+C_s)\). The interior form is

\[
q_t[u]=\int_{\Omega_s}
\bigl(|u_X|^2+|\mathcal T_su-t\mathsf b_su_X|^2+V_s|u|^2\bigr).
\]

For real data its candidate derivative is exactly

\[
\dot q_t[u,v]=-\int_{\Omega_s}\mathsf b_s
\left[u_X(\mathcal T_sv-t\mathsf b_sv_X)
+v_X(\mathcal T_su-t\mathsf b_su_X)\right].
\]

This exposes the `O(beta)` factor before any triangle inequality. Carry the original boundary forcing through both the mass conjugation and the unitary dilation: square roots do not commute with a nonunitary congruence. Do not replace the transported forcing by the square root of a congruent seam form without proving the required correction.

**Exploit separation in the transverse coordinate, not a fictitious orthogonal sum of tangential modes.** Split `(0,1)_X` into two end regions and an overlapping middle region with fixed smooth cutoffs. For data injected on boundary 1 and tested on boundary 2, at least one of the two solutions is observed a fixed positive distance from its forcing boundary on each region. Try to estimate the derivative pairing there using distant-boundary regularity, the local energy estimate for the other solution, and duality/interpolation in the exact `K_a` scale. Keep any low-frequency excursions generated inside the solution maps; projecting the input high does not make the whole solution high.

The substantive acceptance target is an integrable-in-`t` bound

\[
\left\|K_a^rP_Z(\dot D_t)_{21}P_ZK_a^r\right\|
\le C_{r,Z}\beta
\]

with constants independent of `s`, `L_s=pi/s`, the corridor index, and the spectral regularization. Track the inverse-square Hardy domain at both tangential ends and the actual seam forcing throughout. PF-238's one-sided form domination is not a license to commute `Q`, `K_a`, or their square roots.

Check `b=0` and the exactly separated corridor as calibrations. A meaningful obstruction would be a canonical sequence of normalized high-frequency or endpoint-escaping boundary data for which this derivative estimate loses uniformity. Failure of one intermediate sufficient norm bound is not yet a counterexample to the integrated difference estimate.

The method-level prior-art boundaries are Isaev--Novikov, *Stability estimates for determination of potential from the impedance boundary map*, arXiv:1112.3728 (Robin-map integral identities), and Große--Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, arXiv:1703.07228 (uniform boundary regularity). Neither is being used as a black-box theorem for the present singular long strip with its nonlocal actual seam. The exact hypotheses and trace dictionary must be checked.

## Evidence boundary

The homotopy identity and the weighted Robin-Poisson estimates are proposed for independent reconstruction; no PF-240 estimate is certified by this clue. Uniform strong ellipticity, coefficient analyticity, and one-sided seam domination separately do not prove it. No reverse seam comparison, global weak-trace theorem, finite-pant theorem, scattering statement, or RH consequence is asserted. The existing accepted clue and all findings retain their current status.
