---
id: CLUE-prime-flute-conformal-rectangle-dtn-normalizer-transfer
type: research-clue
status: resolved
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-231-ultraparallel-corridor-is-exactly-separable-in-logarithmic-coordinates.md
  - research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect.md
  - research/prime_flute/findings/PF-236-operator-matched-seam-normalizer-preserves-dressed-variable-corridor-transfer.md
  - research/prime_flute/findings/PF-237-complete-lift-seam-spectral-type-blocks-direct-matched-normalizer-comparison.md
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can corridor endpoint suppression recover dressed transfer for the actual seam?

## Observation

PF-236 proves the desired dressed singular-value profile for the operator-matched seam on PF-233's exact variable-width diagonal corridor. PF-237 then shows why a direct two-sided replacement by the complete lifted actual seam is impossible: the actual seam inverse is noncompact because longitudinal packets can escape, while the matched seam inverse is compact.

PF-238 resolves the apparent conflict. Under the canonical density-corrected `tau<->theta` compactification, the complete-axis seam generator is bounded **above** by a fixed multiple of the PF-233 Pöschl--Teller control. Combined with PF-235 and the PF-233 matched-normalizer lower bound, this gives the one-sided order

\[
Q_i^{act}\le C_iQ_i^{mat}
\]

with uniform canonical-tail constants. PF-237 forbids the reverse order, but PF-238 proves that the reverse order is unnecessary: for the normalized inverse, the off-diagonal block is contractively dominated by one off-diagonal block of `Q^{1/2}Lambda_a^{-1}Q^{1/2}`. The exact inverse-corridor block contributes `K^{-1}csch K`, and the one-sided seam order inserts at most the two PF-236 matched square-root factors around it.

Consequently

\[
s_{m+1}(D^{act}_{21})
\lesssim
\frac{\sqrt{w_1w_2}}s\,
\frac{\sqrt{c_0}s(m+\alpha)}
{\sinh(\sqrt{c_0}s(m+\alpha))}
\]

for the **actual complete lifted seam plus exact PF-233 diagonal corridor**, with a uniform multiplicative constant. The endpoint-escaping packets from PF-237 are therefore suppressed by crossing the corridor without an explicit central/endpoint cutoff.

## Research question

Does the actual complete lifted seam preserve PF-236's `sqrt(w_1w_2)/s` dressed transfer scale and high-mode decay despite its spectral-type mismatch with the operator-matched seam?

PF-238 answers this question positively for the exact PF-233 diagonal corridor. The next unresolved question is different: whether PF-232's reciprocal-prime-small shear can be inserted at the **normalized off-diagonal inverse level** without losing the `F(sm)` envelope, followed by the physical `P/H` recoupling and finite-pant completion.

## Why it may matter

PF-228 identifies `sqrt(w_nw_{n+1})/s_n` as the amplitude currency that makes the reciprocal-prime weighted inverse-seam population compatible with the intended weak-trace endpoint. PF-238 shows that the actual complete-seam endpoint escape does not destroy that currency. The local conformal route can therefore move past the seam-normalization/endpoint gate instead of trying to force a false two-sided equivalence ruled out by PF-237.

The result also separates the remaining risks cleanly. Any later failure of the smooth route must now occur when passing from the diagonal corridor to the sheared corridor, through the physical `P/H` boundary split, through finite-pant completion/neighboring-cell coupling, or during PF-222's nested global reassembly. It cannot be attributed merely to the complete-lift seam's noncompact inverse.

## Decisive test

The decisive test was to avoid the impossible comparison `Q_act asymp Q_mat` and ask whether the **one-sided** order compatible with PF-237 is enough.

PF-238 carries this out in two stages. First, it computes the density-corrected compactification of the complete-axis generator exactly and proves a one-sided Pöschl--Teller form bound, which together with PF-235 yields `Q_act<=C Q_mat`. Second, it rewrites the normalized inverse using

\[
\mathcal G=Q^{1/2}\Lambda_a^{-1}Q^{1/2},
\qquad
D=\mathcal G(I+\mathcal G)^{-1},
\]

and proves

\[
s_j(D_{21})\le s_j(\mathcal G_{21}).
\]

Douglas factorization of the one-sided seam order then reduces the crossing block to

\[
\sqrt{\tanh(r_1K)\tanh(r_2K)}\,\operatorname{csch}K,
\]

which is bounded by the PF-236 `sqrt(r_1r_2) K csch K` profile. This establishes the requested endpoint compensation globally on the complete lifted trace space.

## Evidence boundary

The clue is resolved only at the level it asked about: the actual **complete lifted symmetric seam** coupled to PF-233's **diagonal** variable-width corridor. PF-238 does not insert PF-232's sheared full hypercycle form, identify the complete lift with the actual closed-cuff/finite-pant boundary problem, control physical `P/H` projections, perform neighboring-cell extension, or prove PF-222's nested weak-`S_1` reassembly.

PF-237 remains valid: the actual and matched seam normalizers are not two-sided equivalent, and their inverse compactness classes differ. PF-238 succeeds precisely because only the opposite one-sided order is needed after the inverse-corridor block is exposed.

No weak-`S_1`, scattering, determinant, resonance, zeta-zero, or RH conclusion follows from this clue resolution alone.

## Research disposition

Outcome: supported

Resolved by:
- [[research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer]]

The conformal route should now leave endpoint-normalizer comparison behind and attack PF-232 shear at the normalized off-diagonal inverse level. The broader weak-trace program remains tracked by `CLUE-weak-trace-reassembly-with-summable-local-mass`.
