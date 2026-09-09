---
id: CLUE-prime-flute-robin-homotopy-separated-poisson-shear-estimate
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold.md
  - research/prime_flute/findings/PF-241-scaled-tangential-blowup-turns-the-shear-interior-into-a-uniform-long-strip-family.md
  - research/prime_flute/findings/PF-242-hypercycle-shear-is-exponentially-local-in-poschl-teller-mode-index.md
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can a fixed-seam Robin homotopy close the high-high shear estimate before global reassembly?

## Observation

PF-240 needs more than one total scaled boundary derivative, with an `O(beta)` constant, for the actual-seam-normalized shear difference. PF-241 removes shrinking-width loss of interior ellipticity, but leaves the Hardy ends, growing strip length, and noncommuting seam normalization. PF-242 adds exact exponential locality for the direct hypercycle-shear multiplier in Pöschl--Teller mode index, but explicitly does not transfer that locality through the full Schur map.

PF-243 now independently reconstructs the fixed-seam homotopy at the form level. The normalized Schur derivative is exactly an Alessandrini-type pairing with one explicit shear multiplier and two seam-normalized Robin Poisson solutions. More importantly, an exact partition in the crossing coordinate `X` shows that the full high-high difference does not need a symmetric weighted estimate on both boundary legs at once: on each partition piece all Schatten regularity may be charged to the Poisson leg observed a fixed positive distance from its forcing boundary.

The accepted question is therefore no longer whether the formal homotopy identity exists. It is whether the **separated Robin-Poisson maps** have a uniform `K_a` smoothing estimate strong enough to exploit PF-243's factorization while retaining the actual complete-lift seam and the inverse-square Hardy endpoints.

## Research question

With exactly the PF-238 actual complete-lift seam `Q=diag(Q_1,Q_2)`, let `Lambda_t` be the corridor Dirichlet-to-Neumann map obtained by replacing `b` with `t b`, for `0<=t<=1`, and set

\[
D_t=(I+Q^{-1/2}\Lambda_tQ^{-1/2})^{-1}
    =Q^{1/2}(\Lambda_t+Q)^{-1}Q^{1/2}.
\]

PF-243 proves the fixed-seam variational derivative and the exact localized factorization. Can one now prove, for some fixed `R>1` and `Z>0`, the one-sided separated estimates in PF-243 equations (20)--(21), uniformly on the canonical tail?

Equivalently, after choosing `chi_L+chi_R=1` with `chi_L` separated from boundary 2 and `chi_R` separated from boundary 1, do the seam-normalized source-to-bulk energy maps satisfy

\[
\|X_{t,2}^{L}K_a^RP_Z\|+\|Y_{t,2}^{L}K_a^RP_Z\|
+\|X_{t,1}^{R}K_a^RP_Z\|+\|Y_{t,1}^{R}K_a^RP_Z\|
\le C_{R,Z},
\]

for `P_Z=1_(Z,infinity)(K_a)`, with `C_{R,Z}` independent of `s`, the corridor index, and `t`? PF-243 shows that this is sufficient for

\[
\|P_Z(D_1-D_0)_{21}P_Z\|_1
\le C_{R,Z}\frac{\beta}{s}.
\]

The earlier symmetric target

\[
\|K_a^rP_Z(D_1-D_0)_{21}P_ZK_a^r\|\le C\beta,
\qquad r>1/2,
\]

remains sufficient by PF-240, but it is no longer the most localized proof obligation.

## Why it may matter

A positive result would turn the entire remaining local shear correction into an absolutely trace-summable error after the reciprocal-prime weight, using PF-239 and PF-243. The immediate downstream test would then be physical `P/H` recoupling and finite-pant completion, not another generic coefficient or full-Schur regularity lemma.

The localized formulation also sharpens a possible negative result. Failure must occur in a source-to-bulk energy map observed a fixed positive `X`-distance from its forcing boundary, despite PF-241's uniform ellipticity and PF-242's direct coefficient locality. Near-boundary roughness by itself can no longer kill this route, because PF-243 never asks the near leg to carry the Schatten derivatives.

## Decisive test

Freeze PF-243's exact form identity rather than re-deriving a formal inverse derivative. Work in PF-241's long-strip coordinates with

\[
\mathcal T_s=A_s(\partial_Y+C_s),
\qquad
q_t[u]=\int_{\Omega_s}
\bigl(|u_X|^2+|\mathcal T_su-t\mathsf b_su_X|^2+V_s|u|^2\bigr),
\]

and keep the actual PF-238 seam fixed throughout. Use the exact normalized Robin Poisson solutions and the `X`-partition from PF-243.

The positive target is now to prove the four separated estimates above for one `R>1`. A proof may use uniform local elliptic regularity, parameter-dependent Poisson estimates, the exact PF-233 tangential functional calculus, PF-242's Jacobi locality, or a Hardy-adapted commutator argument, but it must control the **actual seam-normalized source maps**, not a Dirichlet or matched-seam surrogate.

Carry the original boundary forcing through both the mass conjugation and the unitary dilation. Square roots do not commute with a nonunitary congruence, and PF-238 supplies only one-sided seam domination. Do not replace the transported forcing by the square root of a congruent seam form without proving the correction.

Keep any low-frequency excursions generated inside the Poisson solution. Projecting the boundary input high does not make the whole bulk solution high. What must be shown is that precomposition by `K_a^RP_Z` is absorbed by propagation over the fixed positive `X` separation on the designated far leg.

Check `b=0` and the exactly separated diagonal corridor as calibrations. PF-242 should be used only where its exact hypothesis applies: it controls multiplication by the direct shear coefficient, not the Robin solution map. A meaningful obstruction is a canonical sequence of normalized high-frequency or endpoint-escaping boundary data for which one of the four separated source-to-bulk norms diverges with `s->0`.

The method-level prior-art boundaries remain Isaev--Novikov, *Stability estimates for determination of potential from the impedance boundary map*, arXiv:1112.3728 (Robin-map integral identities), and Große--Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, Potential Analysis 53 (2020), 407--447, DOI `10.1007/s11118-019-09774-y`, arXiv:1703.07228 (uniform Robin boundary regularity). Neither theorem, nor the fixed-domain off-diagonal DtN smoothing literature already audited in PF-240, directly supplies the PF estimate with its growing tangential interval, inverse-square Hardy ends, nonlocal actual seam, and exact `K_a` scale.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative, localized bulk factorization, and the implication from the four separated `R>1` estimates to an `O(beta/s)` trace bound. It does **not** certify those separated estimates themselves. PF-241's strong ellipticity and PF-242's coefficient locality separately do not prove them, and PF-238 does not give a reverse seam comparison.

No full weak-trace theorem, finite-pant theorem, physical `P/H` recoupling theorem, neighboring-cell theorem, scattering statement, determinant/resonance result, prime/clone separation, zeta-zero statement, or RH consequence is established by accepting this clue.

## Research disposition

The clue is `accepted`. The fixed-seam homotopy survived independent reconstruction and produced PF-243, which materially strengthens the route by replacing full two-sided Schur smoothing with two one-sided separated-source estimates. The live task is now precisely the uniform `K_a^R`, `R>1`, smoothing of the far Robin-Poisson energy legs in the actual long-strip/Hardy/seam geometry. PF-242's exponential locality is useful supporting structure for that proof attempt but is not itself the missing estimate.