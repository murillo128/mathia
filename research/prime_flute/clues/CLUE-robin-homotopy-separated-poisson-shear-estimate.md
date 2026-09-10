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
  - research/prime_flute/findings/PF-271-separated-propagation-only-needs-sublinear-low-output-leakage.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can a fixed-seam Robin homotopy close the high-high shear estimate before global reassembly?

## Observation

PF-243 reconstructs the fixed-seam shear homotopy at the form level. The normalized Schur derivative is an exact Alessandrini-type pairing with one explicit shear multiplier and two seam-normalized Robin Poisson solutions. Partitioning in the crossing coordinate `X` shows that, term by term, all Schatten regularity may be charged to the Poisson leg observed a fixed positive distance from its forcing boundary.

PF-269 then removes the false requirement that the normalized Robin boundary injection smooth before propagation. PF-270 gives a useful sufficient replacement: if the complete conversion before positive separation obeys `K_a^{-q}BK_a^q\in\mathcal B` for some `q>1`, and the remaining far leg pays the same derivatives, then the composition supplies every `1<R\le q` required by PF-243.

PF-271 now shows that even this full graph-domain condition is stronger than necessary. If the far leg pays arbitrary polynomial output derivatives, then for a target `R>1` it is enough to control high input near `\Lambda` only when it leaks into an output window below `\Lambda^\theta` for one `\theta<1`:

\[
\left\|
\mathbf 1_{[\kappa,\Lambda^\theta]}(K_a)
B_{\rm unsmoothed}
\mathbf 1_{[\Lambda,2\Lambda)}(K_a)
\right\|
\lesssim \Lambda^{-R-\varepsilon}.
\]

When the remaining propagation contains an exact exponential spectral factor, the dangerous output window shrinks further to order `\log\Lambda`. PF-271 also proves the matching necessary low-window decay for an exact `e^{-dK_a}` composition. Thus proportional high-high conversion is no longer the live discriminator: only sufficiently deep high-to-low leakage can outrun the later separation.

## Research question

With exactly the PF-238 actual complete-lift seam `Q=diag(Q_1,Q_2)`, let `\Lambda_t` be the corridor Dirichlet-to-Neumann map obtained by replacing the shear coefficient `b` with `tb`, `0\le t\le1`, and set

\[
D_t=Q^{1/2}(\Lambda_t+Q)^{-1}Q^{1/2}.
\]

PF-243 proves the fixed-seam variational derivative and its localized factorization. Can each of its four designated far source-to-bulk energy legs be cut **after the last unsmoothed operator capable of changing `K_a` scale** so that:

1. the remaining genuinely separated propagation pays arbitrarily high output derivatives uniformly in `s`, the corridor index, and `t`; and
2. the complete preceding Robin/reflection/density/congruence conversion has `\Lambda^{-R-\varepsilon}` leakage from input shell `[\Lambda,2\Lambda)` into output below `\Lambda^\theta`, for some `R>1`, `\varepsilon>0`, and one fixed `\theta<1`?

If the last factor after spectral conversion is an exact `e^{-dK_a}` propagator, replace the sublinear target by the sharper logarithmic window from PF-271. Full one-sided graph locality with `q>1` remains a valid sufficient route, but it is no longer the primary proof obligation.

Equivalently, after choosing `\chi_L+\chi_R=1` as in PF-243, the final target remains

\[
\|X_{t,2}^{L}K_a^RP_Z\|+\|Y_{t,2}^{L}K_a^RP_Z\|
+\|X_{t,1}^{R}K_a^RP_Z\|+\|Y_{t,1}^{R}K_a^RP_Z\|
\le C_{R,Z}
\]

for one `R>1`, with `C_{R,Z}` uniform on the canonical tail. PF-243 then gives the `O(\beta/s)` high-high trace bound. PF-271 changes only the intermediate currency by which those composed estimates should be attacked.

## Why it may matter

A positive result would close the remaining local high-high shear correction and hand the smooth route to physical `P/H` recoupling and finite-pant completion. More immediately, PF-271 avoids spending effort on spectral sectors that positive separation already controls.

This matters because PF-268's exact finite-seam obstruction occurs on proportional blocks `i\asymp j\asymp N`. Such blocks lie above every sublinear output window `N^\theta` and therefore do not threaten the PF-271 criterion. By contrast, PF-244's abstract bad seam sends arbitrarily high input to a fixed low output mode and fails the necessary logarithmic/fixed-window leakage condition. The revised target separates these two geometries exactly.

The fixed-axis Green chain PF-264--PF-267 is therefore relevant in a more favorable regime than before: as output/input ratio tends to zero. Its proportional-ray `N^{-2}` floor need not be repaired. What remains is to insert the **combined** Robin/reflection conversion honestly and quantify only its leakage into a strongly lower spectral sector.

## Decisive test

Freeze PF-243's exact form identity and work in PF-241's long-strip coordinates with the actual PF-238 seam fixed throughout. For each of the four far legs, inventory every Robin source factor, reflection, mass/unitary transport, density/congruence correction, or shear-dependent conversion that occurs before the designated positive source-to-observation separation.

Place the factorization boundary immediately after the last such conversion. First prove arbitrary-order output smoothing for the remainder. Then, for dyadic input shells `E_\Lambda=\mathbf1_{[\Lambda,2\Lambda)}(K_a)`, estimate only

\[
F_{\Lambda,\theta}B_{\rm unsmoothed}E_\Lambda,
\qquad
F_{\Lambda,\theta}=\mathbf1_{[\kappa,\Lambda^\theta]}(K_a),
\]

for one small fixed `\theta<1`. The target is operator-norm decay `O(\Lambda^{-R-\varepsilon})` for some `R>1`. If the remainder has exact exponential spectral damping, use `F_{\Lambda}=\mathbf1_{[\kappa,A\log\Lambda]}(K_a)` instead and calibrate `A` against the propagation distance as in PF-271.

Use PF-264--PF-267 on the fixed-axis finite seam in this genuinely high-to-low regime before attempting a full graph conjugation. PF-255/PF-256's `q=2` graph locality for the coordinate transports remains available and can still be used where it is cheap; it need not be promoted into a global condition on the entire pre-separation Robin conversion.

Carry the original boundary forcing through both the mass conjugation and unitary dilation. Do not replace the transported forcing by the square root of a congruent seam form. Keep low-frequency excursions generated inside the Poisson solution. The relevant orientation is always high input to low output.

Calibrate against three exact cases. The matched seam of PF-269 shows that no standalone boundary smoothing is necessary. PF-244 must fail the revised leakage criterion because its high input reaches a fixed low mode. PF-268 must *not* count as a failure merely because proportional high-high blocks have an `N^{-2}` floor; those blocks are paid by the far leg under the PF-271 decomposition.

A route-level negative result must now exhibit a canonical sequence whose complete pre-separation conversion puts enough input-shell mass below `\Lambda^\theta` (or below the logarithmic window in the exponential case) to violate every possible `R>1` leakage estimate. Failure of full graph locality without such deep leakage is no longer decisive.

The method-level prior-art boundary includes Jaffard's and Gröchenig--Klotz's classical theories of globally localized/almost-diagonal matrices, as audited in PF-271, together with the Robin-map and Davies--Gaffney literature already audited in PF-243/PF-260. None supplies the actual Prime-Flute low-output leakage estimate or the required uniform sheared far-leg theorem.

## Evidence boundary

PF-243 certifies the fixed-seam variational derivative, localized bulk factorization, and the implication from four separated `R>1` estimates to an `O(\beta/s)` trace bound. PF-269 proves that standalone positive-order smoothing of the normalized boundary injection is unnecessary. PF-270 proves that one-sided graph locality plus matching far smoothing is sufficient. PF-271 proves a strictly weaker dyadic criterion: arbitrary-order far smoothing only needs control of sublinear low-output leakage, while exact exponential propagation reduces the dangerous window to logarithmic size and forces a corresponding necessary leakage bound.

What is **not** established is that the actual PF-243 conversion satisfies the PF-271 leakage estimate, that the fully sheared/Hardy far leg pays arbitrary output derivatives uniformly, or that the fixed-axis Green estimates survive the complete Robin/reflection algebra with the required uniform constants. No claim is made that full graph locality is false; it is simply no longer required if the weaker composition-adapted estimates can be proved.

No full weak-trace theorem, finite-pant theorem, physical `P/H` recoupling theorem, neighboring-cell theorem, scattering statement, determinant/resonance result, prime/clone separation, zeta-zero statement, or RH consequence is established by accepting this clue.

## Research disposition

The clue remains `accepted`, but its next proof obligation is narrowed by PF-271. The preferred discriminator is now **deep high-to-low leakage after the last unsmoothed conversion**, measured only below a sublinear spectral window and paired with arbitrary-order smoothing of the genuinely separated remainder. Full `K_a^{-q}BK_a^q` graph locality remains a sufficient fallback, not the default target. A positive leakage/far-propagation pair for one `R>1` closes the PF-243 high-high shear gate; a meaningful negative must fail the weaker PF-271 criterion rather than merely exhibit proportional high-high tails or loss of global graph invariance.
