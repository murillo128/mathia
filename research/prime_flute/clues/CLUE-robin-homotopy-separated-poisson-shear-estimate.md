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
  - research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate.md
  - research/prime_flute/findings/PF-270-post-propagation-smoothing-needs-only-one-sided-graph-locality.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can a fixed-seam Robin homotopy close the high-high shear estimate before global reassembly?

## Observation

PF-240 needs more than one total scaled boundary derivative, with an `O(beta)` constant, for the actual-seam-normalized shear difference. PF-241 removes shrinking-width loss of interior ellipticity, but leaves the Hardy ends, growing strip length, and noncommuting seam normalization. PF-242 adds exact exponential locality for the direct hypercycle-shear multiplier in Pöschl--Teller mode index, but explicitly does not transfer that locality through the full Schur map.

PF-243 independently reconstructs the fixed-seam homotopy at the form level. The normalized Schur derivative is exactly an Alessandrini-type pairing with one explicit shear multiplier and two seam-normalized Robin Poisson solutions. An exact partition in the crossing coordinate `X` shows that the full high-high difference does not need a symmetric weighted estimate on both boundary legs at once: on each partition piece all Schatten regularity may be charged to the Poisson leg observed a fixed positive distance from its forcing boundary.

PF-269 then removes an overstrong intermediate interpretation of that target. The boundary injection itself need not gain a positive transverse derivative before propagation: the exact matched seam has energy-normalized injection `B=I/2`, so `BK^R` is unbounded for every `R>0`, while its separated Poisson leg is smoothing of every order.

PF-270 sharpens the surviving requirement further. If the complete unsmoothed boundary conversion before the designated positive separation satisfies the one-sided graph estimate

\[
K_a^{-q}B K_a^q\in\mathcal B
\]

for some `q>1`, and the remaining far propagation `P_far` satisfies `P_far K_a^q\in\mathcal B`, then

\[
P_{\rm far}BK_a^R
=(P_{\rm far}K_a^q)(K_a^{-q}BK_a^q)K_a^{R-q}
\]

is bounded for every `1<R<=q`. Thus the live issue is now **high-input-to-low-output graph locality plus positive separation**, not standalone smoothing of the Robin conversion.

## Research question

With exactly the PF-238 actual complete-lift seam `Q=diag(Q_1,Q_2)`, let `Lambda_t` be the corridor Dirichlet-to-Neumann map obtained by replacing `b` with `t b`, for `0<=t<=1`, and set

\[
D_t=(I+Q^{-1/2}\Lambda_tQ^{-1/2})^{-1}
    =Q^{1/2}(\Lambda_t+Q)^{-1}Q^{1/2}.
\]

PF-243 proves the fixed-seam variational derivative and the exact localized factorization. Can the four designated far source-to-bulk energy legs be factored or estimated so that **all spectral conversion before the paid positive separation** has a uniform one-sided graph-locality exponent `q>1`, while the separated remainder pays the same `q` transverse derivatives?

A sufficient form, when an exact factorization `T_far=P_far B_unsmoothed` is available, is

\[
\sup_{s,t}\|K_a^{-q}B_{\rm unsmoothed}K_a^q\|<\infty,
\qquad
\sup_{s,t}\|P_{\rm far}K_a^q\|<\infty
\]

for one `q>1`. The especially natural target is `q=2`, because PF-255/PF-256 already prove two-derivative graph locality for the hypercycle/corridor coordinate transports. PF-270 then supplies any `1<R<2` needed by PF-243 without requiring `B_unsmoothed K_a^R` to be bounded by itself.

Equivalently, after choosing `chi_L+chi_R=1` with `chi_L` separated from boundary 2 and `chi_R` separated from boundary 1, the final target remains the PF-243 estimates

\[
\|X_{t,2}^{L}K_a^RP_Z\|+\|Y_{t,2}^{L}K_a^RP_Z\|
+\|X_{t,1}^{R}K_a^RP_Z\|+\|Y_{t,1}^{R}K_a^RP_Z\|
\le C_{R,Z},
\]

for `P_Z=1_(Z,infinity)(K_a)`, with `C_{R,Z}` independent of `s`, the corridor index, and `t`. PF-243 shows that this is sufficient for

\[
\|P_Z(D_1-D_0)_{21}P_Z\|_1
\le C_{R,Z}\frac{\beta}{s}.
\]

The point of PF-270 is that these composed estimates need not be proved by assigning positive Sobolev gain to the boundary injection itself.

## Why it may matter

A positive result would turn the entire remaining local shear correction into an absolutely trace-summable error after the reciprocal-prime weight, using PF-239 and PF-243. The immediate downstream test would then be physical `P/H` recoupling and finite-pant completion, not another generic coefficient or full-Schur regularity lemma.

The graph-local formulation also makes the negative target sharper. PF-268's proportional high-high finite-seam tails do not by themselves kill the route, because output that remains at a comparable high transverse scale can still be paid for by positive longitudinal propagation. A decisive obstruction must instead exhibit **genuine high-to-low conversion before the separated leg**, strong enough that no one-sided graph exponent `q>1` survives uniformly.

## Decisive test

Freeze PF-243's exact form identity rather than re-deriving a formal inverse derivative. Work in PF-241's long-strip coordinates with

\[
\mathcal T_s=A_s(\partial_Y+C_s),
\qquad
q_t[u]=\int_{\Omega_s}
\bigl(|u_X|^2+|\mathcal T_su-t\mathsf b_su_X|^2+V_s|u|^2\bigr),
\]

and keep the actual PF-238 seam fixed throughout. Use the exact normalized Robin Poisson solutions and the `X`-partition from PF-243.

For each of the four far legs, identify every boundary conversion, reflection, density/congruence correction, or other operator that acts before the fixed positive source-to-observation separation. Do not test the naked Robin injection in isolation if later unsmoothed factors can still change transverse scale. Either package those operators into one `B_unsmoothed` and prove

\[
K_a^{-q}B_{\rm unsmoothed}K_a^q\in\mathcal B
\]

uniformly for some `q>1`, or prove an equivalent high-input-to-low-output block estimate directly for the complete pre-separation conversion. In parallel prove that the remaining far propagation pays `q` output derivatives, `P_far K_a^q\in\mathcal B`. The `q=2` case is the first target because it matches the already-established PF-255/PF-256 transport regularity.

Carry the original boundary forcing through both the mass conjugation and the unitary dilation. Square roots do not commute with a nonunitary congruence, and PF-238 supplies only one-sided seam domination. Do not replace the transported forcing by the square root of a congruent seam form without proving the correction.

Keep low-frequency excursions generated inside the Poisson solution. Projecting the boundary input high does not make the whole bulk solution high. The one-sided conjugation orientation matters: `K_a^{-q}BK_a^q` controls dangerous high-input-to-low-output conversion, while `K_a^qBK_a^{-q}` controls the wrong direction.

Check `b=0` and the exactly separated diagonal corridor as calibrations. PF-242 should be used only where its exact hypothesis applies: it controls multiplication by the direct shear coefficient, not the Robin solution map. PF-269's matched seam `B=I/2` is the positive calibration for graph locality without standalone smoothing; PF-244 is the negative calibration whose high-to-fixed-low mixer violates every `q>0` one-sided graph bound.

A meaningful obstruction is a canonical sequence of normalized high-frequency or endpoint-escaping boundary data whose pre-separation conversion retains order-one mass in sufficiently low `K_a` output channels that the subsequent fixed positive separation cannot absorb one `K_a^R` weight for any `R>1`.

The method-level prior-art boundaries remain Isaev--Novikov, *Stability estimates for determination of potential from the impedance boundary map*, arXiv:1112.3728 (Robin-map integral identities), Große--Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, Potential Analysis 53 (2020), 407--447, DOI `10.1007/s11118-019-09774-y`, arXiv:1703.07228 (uniform Robin boundary regularity), and the Davies--Gaffney/off-diagonal functional-calculus literature already audited in PF-260. None directly supplies the required actual-seam one-sided graph estimate in the growing long-strip/Hardy geometry.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative, localized bulk factorization, and the implication from its four separated `R>1` estimates to an `O(beta/s)` trace bound. PF-269 proves that standalone positive-order smoothing of the normalized boundary injection is not necessary. PF-270 proves the abstract graph-locality/propagation factorization and the associated `(M/N)^q` high-to-low block bound.

What is **not** established is that the actual PF-243 far legs admit a factorization with `q>1`, that the complete unsmoothed actual Robin/reflection conversion preserves `Dom(K_a^q)`, or that the separated sheared/Hardy propagation pays the same `q` uniformly. PF-241's strong ellipticity, PF-242's coefficient locality, and PF-238's one-sided seam domination separately do not prove those statements.

No full weak-trace theorem, finite-pant theorem, physical `P/H` recoupling theorem, neighboring-cell theorem, scattering statement, determinant/resonance result, prime/clone separation, zeta-zero statement, or RH consequence is established by accepting this clue.

## Research disposition

The clue remains `accepted`. PF-243 reduced the shear problem to four one-sided far Robin-Poisson estimates; PF-269 removed the false requirement that the boundary injection itself gain derivatives; PF-270 now identifies a strictly weaker sufficient currency. The next load-bearing question is whether the **complete actual pre-separation boundary conversion** has uniform one-sided graph locality of some order `q>1`—preferably `q=2`—and whether the remaining far propagation pays the corresponding output derivatives. A positive answer would supply the required `R>1` range without proving any standalone Robin smoothing theorem.