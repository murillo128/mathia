---
id: CLUE-mobius-cancellation-averaged-qvdc-source-frame-variable-retention
type: research-clue
status: accepted
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-416-weighted-vdc-filters-cannot-remove-diagonal.md
  - research/mobius_cancellation/findings/MC-417-fejer-riesz-closes-positive-finite-band-kernels.md
  - research/mobius_cancellation/findings/MC-456-triply-well-factorable-dispersion-provides-a-factor-specific-quotient-breaking-template.md
  - research/mobius_cancellation/findings/MC-458-staged-factor-conditioning-exposes-residual-divisor-sum-kernel.md
  - research/mobius_cancellation/findings/MC-459-staged-residual-energy-is-controlled-by-the-normalized-shift.md
  - research/mobius_cancellation/findings/MC-460-one-sided-residual-conditioning-promotes-reduced-divisor-to-reciprocal-source-shift.md
  - research/mobius_cancellation/findings/MC-461-residual-source-starts-decompose-into-bounded-anchor-slices.md
  - research/mobius_cancellation/findings/MC-463-gcd-sector-normalization-collapses-to-common-anchor-quotient.md
  - research/mobius_cancellation/findings/MC-464-normalized-gcd-gate-makes-favorable-shifts-totient-sparse.md
  - research/mobius_cancellation/findings/MC-465-fejer-weighted-favorable-gcd-classes-remain-sparse.md
  - research/mobius_cancellation/findings/MC-466-original-shift-fejer-envelope-cancels-outer-gcd-advantage.md
  - research/mobius_cancellation/findings/MC-467-residual-scale-interval-shrinkage-cancels-support-growth.md
  - research/mobius_cancellation/findings/MC-468-root-scale-support-makes-well-factorability-vacuous.md
  - research/mobius_cancellation/findings/MC-469-empty-vector-sieve-component-survives-small-outer-cell-pruning.md
  - research/mobius_cancellation/findings/MC-470-empty-vector-residual-is-a-nonnegative-sieve-boundary-count.md
  - research/mobius_cancellation/findings/MC-471-empty-vector-base-is-two-sided-sifted-translated-ratio-sum.md
  - research/mobius_cancellation/findings/MC-472-pair-sieve-complete-period-factorizes.md
  - research/mobius_cancellation/findings/MC-473-termwise-pair-sieve-completion-pays-exponential-branch-multiplicity.md
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The factor-specific route has been reduced to a small number of genuinely different channels. `MC-459`--`MC-467` price the generic staged source geometry: normalized gcd sectors collapse to one anchor quotient, favorable gcd classes remain sparse under Fejér weighting, increasing residual support shortens the corresponding source interval, and nonendpoint gain is forced onto small outer scales. `MC-468` shows that generic well-factorability alone supplies no missing anti-concentration theorem.

The concrete modified linear-sieve decomposition then forces an `r=0` empty-vector component (`MC-469`) with outer geometry `R=T=1`. Its residual is the nonnegative upper-sieve boundary count

\[
B(y)=R_z(y)+E(y),
\qquad
R_z(y)=\mathbf 1_{(y,P(z))=1},
\qquad E(y)\ge0,
\]

so internal coefficient signs do not provide oscillation (`MC-470`). In this base cell, staging also creates no independent reciprocal phase: recombination gives exactly

\[
C_h^{(0)}(I)=\sum_{n\in I}K_h(n)B(n+h)B(n),
\qquad
K_h(n)=\chi(n+h)\overline{\chi(n)}
=\chi\!\left(\frac{n+h}{n}\right)
\]

on nonzero character support (`MC-471`). The amplitude splits into rough×rough, two mixed rough/boundary terms, and boundary×boundary.

For rough×rough, let

\[
W_z=\prod_{\substack{q<z\\q\ne p}}q,
\qquad
A_{W_z,h}(n)=\mathbf 1_{(n(n+h),W_z)=1}.
\]

`MC-472` proves that the complete joint period contains no hidden sieve/phase resonance:

\[
\sum_{n\bmod pW_z}K_h(n)A_{W_z,h}(n)
=-W_z\delta_{W_z}(h),
\]

with normalized mean `-delta_W(h)/p`. Odd shifts vanish exactly when `z>2`, and the uniform shift-average of `delta_W(h)` is the independent reduced-residue baseline. Thus the live rough×rough object is the centered incomplete discrepancy

\[
\mathcal D_{W,h}(I)
=
\sum_{n\in I}K_h(n)A_{W,h}(n)
+\frac{|I|}{p}\delta_W(h).
\]

`MC-473` closes the most direct incomplete repair. Exact Möbius expansion of both roughness constraints followed by a separate Fourier/Weil completion of every congruence branch gives

\[
|\mathcal D_{W,h}(I)|
\ll
\sqrt p\log p\,
\mathcal B_W(h),
\qquad
\mathcal B_W(h)=\prod_{q\mid W}(1+\nu_q(h)),
\]

up to the smaller finite-interval centering term. For a primorial sieve,

\[
2^{\omega(W)}\le\mathcal B_W(h)\le3^{\omega(W)}.
\]

So the individual progression character sums are easy, but full inclusion-exclusion plus branchwise absolute values is exponentially expensive in the number of sieve primes. This is a method obstruction, not a lower bound for the true discrepancy: any surviving sieve route must keep cancellation or approximation structure across divisor levels before absolute closure.

There is also a one-sided prior-art boundary from Gong--Jia--Korolev: above the square-root conductor scale, `sum R_z(n)K_h(n)` and its translated analogue receive logarithmic cancellation because one rough leg can be absorbed into a bounded multiplicative coefficient. That theorem neither handles the joint pair-sieve coefficient nor supplies the required conductor-power gain.

## Research question

Can the concrete staged-sieve decomposition still produce a strict conductor-power gain through a mechanism that survives `MC-473`?

For the **empty-vector rough×rough component**, the target is no longer generic incomplete completion. Can a **compressed sieve representation**—for example truncated/factorable beta-sieve weights, a Buchstab/bilinear decomposition, or dispersion before branchwise absolute values—control `mathcal D_{W,h}(I)` with a conductor-power gain while preserving the simultaneous shifted roughness? Any approximation to the exact pair-sieve indicator must price its error against the oscillatory sum on the actual source interval; positivity or a standard density asymptotic alone is insufficient.

The three positive boundary variants obtained by replacing one or both rough indicators by `E` remain separate targets. Their first-exit structure is not covered by the complete-period factorization or the branch-multiplicity calculation.

For **nonempty rough-block components**, after discarding every bin tuple whose product cannot enter the `MC-467` small-outer region, does the surviving normalized signed mass remain large and structured enough for factor-specific dispersion to matter?

A third channel is **cross-component interference**. It is admissible only if the complete signed finite decomposition is carried through an oscillatory transform before componentwise absolute values or positive quadratic closure.

## Why it may matter

The route has progressively removed fake resources: large gcd, extra factor labels, Fejér concentration, independent support/interval tuning, generic well-factorability, blanket support pruning, internal signs of the empty-vector upper-sieve residual, the reciprocal divisor coordinate, complete-period sieve/phase resonance, and now full exact pair-sieve inclusion-exclusion followed by independent completion.

The surviving rough×rough question is therefore sharply structural. A positive result must show how a sieve representation preserves enough divisor-level coherence to beat the `MC-473` branch tariff while still controlling the approximation error. A negative result showing that every natural compressed representation either loses conductor-power precision in the sieve error or recreates the existing source tariff would close most of the componentwise base architecture and leave the boundary, nonempty, or pre-positive interference channels.

## Decisive test

For the **base rough×rough term**, set `R=T=1` and work in the recombined `n` representation. Remove odd `h` exactly when `z>2` and subtract the complete mean `-delta_W(h)/p` from the outset.

Do **not** re-expand the exact pair sieve completely and estimate every divisor/residue branch independently: `MC-473` proves that this pays `B_W(h)=prod(1+nu_q(h))`. Instead choose one concrete compressed representation and derive both sides of its tradeoff:

1. the character/trace-function estimate for the retained divisor or bilinear pieces, with all modulus/support dependence explicit; and
2. the error incurred when replacing or decomposing the exact pair-sieve indicator on the actual source interval.

Accept the route only if the two bounds together produce a strict conductor-power saving after source length, shell summation, Fejér weights, endpoint separation, coefficient normalization, and source depth are charged. Kill the route if obtaining conductor-power sieve accuracy necessarily forces a divisor level or branch complexity that erases the character saving.

For the mixed and boundary terms, use the exact first-exit formula from `MC-470`; high rank or nonnegativity alone is not sparsity. For nonempty components, apply the exact lower support `a>D_1...D_r` before estimating surviving tuples. For cross-component interference, retain the signed finite sum through the proposed transform and exhibit a concrete cross term whose cancellation survives normalization; separate positive energies followed by a later appeal to cancellation do not qualify.

Keep exact `(U,D)` collision aggregation wherever a staged form is genuinely needed, and isolate the near-complete endpoint instead of hiding it in a bulk estimate.

## Evidence boundary

`MC-472` proves only complete-period factorization and local density identities. `MC-473` proves only that **full exact inclusion-exclusion plus independent branchwise completion** is too expensive; it does not bound the actual incomplete discrepancy and does not rule out structured sieve weights, Buchstab identities, bilinear forms, or dispersion.

Likewise, none of the persisted findings proves a power saving for the boundary terms, the surviving nonempty components, or cross-component interference. No conductor-power gain, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted` and is materially narrowed through `MC-473`. The immediate rough×rough test is now a **sieve-compression tradeoff**: preserve divisor-level structure strongly enough to avoid exponential branch multiplicity, while proving that the resulting approximation/decomposition error is small enough at conductor-power scale. Full inclusion-exclusion plus termwise completion is closed as a standalone route; boundary terms, nonempty components, and pre-positive cross-component interference remain distinct surviving channels.