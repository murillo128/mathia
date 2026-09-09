---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
  - research/prime_flute/findings/PF-220-coefficient-adjacent-low-recoupling-is-weak-trace-without-schur-locality.md
  - research/prime_flute/findings/PF-221-coefficient-weight-transfer-reduces-to-a-reciprocal-prime-schur-commutator.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-238-one-sided-seam-domination-closes-complete-lift-dressed-diagonal-transfer.md
  - research/prime_flute/findings/PF-239-reciprocal-prime-shear-makes-critical-band-leakage-absolutely-trace-summable.md
  - research/prime_flute/findings/PF-240-total-one-scaled-boundary-derivative-is-the-sharp-high-high-shear-trace-threshold.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

PF-112 excludes trace class for the exact first relative resolvent, while the smooth decomposition-interface route has now been reduced much further than the original raw-channel formulation.

PF-228 first showed in the straight-corridor control that Schur dressing suppresses the inverse-seam population to the favorable `sqrt(w_1w_2)/s` scale with the `z/sinh(z)` high-mode envelope. PF-232 then put the exact hypercycle trim on a fixed strip and proved that its shear is only `beta_n=O(P_n^-1)` in energy form. PF-233 solved the diagonal variable-width strip exactly at operator level, and PF-238 transferred its dressed crossing envelope to the **actual complete-lift seam normalization** using only one-sided seam domination.

PF-239 isolates the remaining shear risk. Every shear correction with at least one leg in a fixed PF-233 scaled band has trace norm `O(beta_n/s_n)`, and the reciprocal-prime commutator weight makes the resulting family absolutely trace summable because

\[
\delta_n\frac{\beta_n}{s_n}\lesssim \frac1{P_nP_{n+1}}.
\]

Only the high-high block survives this argument. PF-240 sharpens that gate again: the shear correction does **not** need to preserve the full exponential diagonal-corridor envelope. If its high-high block gains more than one total scaled boundary derivative across the two legs, then Schatten factorization and PF-233's one-dimensional scaled eigenvalue count already give trace norm `O(beta_n/s_n)`. Total smoothing order exactly one is the abstract critical threshold: it forces only weak trace class in the model case.

The smooth local frontier is therefore a single quantitative PDE question: does the exact PF-232 hypercycle perturbation, after PF-238's actual seam normalization, satisfy a scaled-uniform high-high Sobolev estimate with total order `>1` and coefficient `O(beta_n)`? Only after that should the line spend effort on physical `P/H` recoupling, finite one-cusp pant completion, neighboring-cell coupling, and the genuinely nested PF-222 global reassembly.

The independent PF-204 unsmoothed native-factorization route remains available if the smooth route fails.

## Research question

Can the exact prime/shift first relative resolvent be placed in

\[
\mathcal S_{1,\infty}
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the current smooth route, let

\[
H_{n,Z}=(I-\Pi_{n,Z})\,(D_{n,1}-D_{n,0})_{21}\,(I-\Pi_{n,Z}),
\]

where `D_{n,1}` and `D_{n,0}` are the actual-seam-normalized sheared and diagonal Schur factors and `Pi_{n,Z}=1_[0,Z](K_{a,n})`. Does there exist `r_1,r_2>0` with `r_1+r_2>1` such that

\[
\left\|K_{a,n}^{r_2}H_{n,Z}K_{a,n}^{r_1}\right\|
\le C_{Z,r_1,r_2}\,\beta_n
\]

uniformly on the canonical tail?

If so, PF-240 makes the entire remaining shear correction an absolutely trace-summable error after the reciprocal-prime weight. The next questions are then whether physical `P/H` recoupling and finite-pant completion preserve the dressed local scale and whether the overlapping prefix-flux series from PF-222 can finally be reassembled in weak trace class without replacing its nested cuts by an artificial orthogonal direct sum.

## Why it may matter

A positive answer to the high-high estimate would remove the last shear-specific obstruction without demanding an unnecessarily strong mode-by-mode analytic envelope. It would show that the exact hypercycle trim is perturbatively harmless at the trace-ideal level relevant to the global weak endpoint, leaving only physical recoupling and global reassembly.

A negative answer would also be decisive. PF-239 has already removed all low-touch shear leakage, and PF-240 identifies the precise regularity threshold needed for the tail. Failure must therefore appear as a canonical loss of scaled Sobolev smoothing in the high-high block, not merely as generic mode mixing, fixed-domain smoothing constants, or the inverse-seam channel count already neutralized by Schur dressing.

## Decisive test

Work directly with PF-232's exact straightened hypercycle quadratic form and PF-238's actual complete-lift seam normalization. Keep PF-233's `K_a` as the scaled transverse frequency operator and the same fixed high projector used in PF-239.

The positive target is any uniform estimate

\[
\|K_a^{r_2}H_ZK_a^{r_1}\|\le C\beta,
\qquad r_1+r_2>1.
\]

PF-240 then supplies the trace-class conclusion automatically; there is no need to re-prove an exponential `K csch(K)` envelope for the perturbation. A symmetric target `r_1=r_2=r>1/2` is sufficient.

The estimate must be **scaled-uniform** as `s->0` and must retain the perturbative factor `beta`. Qualitative `C^infty` smoothing for each fixed corridor is not enough. A decisive negative result should exhibit a canonical high-high sequence for which the relevant scaled Sobolev norm loses the `O(beta)` bound or fails for every total order above one.

If the high-high gate closes positively, test physical `P/H` recoupling and one-cusp pant completion next, before attempting the PF-222 nested global sum. Keep those stages separate so that a later failure can be assigned to the correct mechanism.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-238 is an exact theorem only for the diagonal variable-width corridor with actual seam normalization. PF-239 proves trace summability only for shear corrections touching a fixed scaled band. PF-240 is a sharp **conditional operator-ideal reduction**: it proves what amount of high-high smoothing would suffice, not that the exact hypercycle PDE supplies that smoothing.

Classical fixed-geometry Dirichlet-to-Neumann theory says that interaction between disjoint smooth boundary components is smoothing, but that does not supply the uniform collapsing-corridor constants or the `O(beta_n)` perturbative factor required here. The remaining local problem is therefore genuinely quantitative.

The physical `P/H` split, finite-pant completion, neighboring-cell extension, nested PF-222 reassembly, wave operators, determinants/resonances, prime/clone separation, zeta zeros, and RH remain unresolved. Clue acceptance records only that the weak-trace endpoint remains a research-worthy target.

## Research disposition

The clue remains `accepted`. The immediate smooth-route task is now the PF-240 scaled high-high estimate with total smoothing order `>1`. If it holds, treat shear as an absolutely trace-summable local error and move to physical `P/H` recoupling and finite-pant completion; only then return to the nested global weak-`S_1` reassembly.