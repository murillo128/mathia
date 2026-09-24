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
  - research/mobius_cancellation/findings/MC-474-pair-sieve-fourier-spectral-norm-is-exponential.md
  - research/mobius_cancellation/findings/MC-475-pair-sieve-parseval-coupling-pays-full-frequency-dimension.md
  - research/mobius_cancellation/findings/MC-476-sifted-restriction-is-coefficient-blind-at-zero-frequency.md
  - research/mobius_cancellation/findings/MC-477-low-denominator-envelope-admits-denominator-free-character-completion.md
  - research/mobius_cancellation/findings/MC-478-pair-sieve-local-fourier-factorization-lowers-envelope-l1-cost.md
  - research/mobius_cancellation/findings/MC-479-selberg-envelope-leakage-is-order-one-on-near-cutoff-single-violations.md
  - research/mobius_cancellation/findings/MC-480-selberg-leakage-complete-period-phase-factorizes.md
  - research/mobius_cancellation/findings/MC-481-centered-selberg-leakage-is-target-equivalent-modulo-envelope.md
  - research/mobius_cancellation/findings/MC-482-two-sided-beta-sieve-transfer-forces-a-polylogarithmic-cutoff.md
  - research/mobius_cancellation/findings/MC-483-well-factorable-bracket-width-does-not-transfer-the-signed-error.md
  - research/mobius_cancellation/findings/MC-484-buchstab-first-exit-removes-selector-but-preserves-dimension-two.md
  - research/mobius_cancellation/findings/MC-485-complete-q-shift-frame-coefficient-blind-l2-ceiling.md
  - research/mobius_cancellation/findings/MC-486-incomplete-q-subframes-remain-l2-tight.md
  - research/mobius_cancellation/findings/MC-487-first-exit-inverse-shifts-are-affine-gauge.md
  - research/mobius_cancellation/findings/MC-488-first-exit-cells-form-disjoint-source-partition.md
  - research/mobius_cancellation/findings/MC-489-first-exit-rowwise-dilation-retains-p-scale-diagonal.md
  - research/mobius_cancellation/findings/MC-490-sifted-rowwise-subframes-are-riesz-stable.md
  - research/mobius_cancellation/findings/MC-491-repeated-residue-first-exit-rows-have-logarithmic-coherence.md
  - research/mobius_cancellation/findings/MC-492-native-repeated-residue-blocks-have-no-common-sign-cancellation.md
  - research/mobius_cancellation/findings/MC-493-native-cross-root-blocks-need-square-root-multiplicity.md
  - research/mobius_cancellation/findings/MC-494-complete-repeated-residue-blocks-tensorize-before-root-interference.md
  - research/mobius_cancellation/findings/MC-495-incomplete-cross-root-multiplicity-collapses-to-weighted-character-bias.md
  - research/mobius_cancellation/findings/MC-496-endpoint-only-cross-root-bias-has-a-square-root-conductor-threshold.md
  - research/mobius_cancellation/findings/MC-497-quadratic-short-overlap-bias-requires-exceptional-starts.md
  - research/mobius_cancellation/findings/MC-498-endpoint-start-bias-is-priced-by-effective-quotient-fibres.md
  - research/mobius_cancellation/findings/MC-499-endpoint-start-dispersion-has-a-source-population-ceiling.md
  - research/mobius_cancellation/findings/MC-500-dyadic-endpoint-quotient-support-has-q-free-square-root-ceiling.md
  - research/mobius_cancellation/findings/MC-501-dyadic-endpoint-certificate-has-q-free-source-width-barrier.md
  - research/mobius_cancellation/findings/MC-502-cross-root-first-exit-rows-have-q-plus-r-logarithmic-sieve-coherence.md
---

# Can load-bearing q-dependent arithmetic asymmetry beat the Möbius source-frame tariff?

## Observation

The normalized empty-vector source has survived a long chain of exact reductions, but most generic uses of the first-exit label are closed. `MC-472`--`MC-495` eliminate direct completion, coefficient-blind phase averaging, affine inverse shifts, multiplicity-only repeated-residue effects, and several positive/bracketed sieve replacements. The incomplete two-root problem reduces to one nonnegative source-derived weight against an explicit relative character phase.

The endpoint contribution is now sharply staged. `MC-496` rules out endpoint-only order-one bias above the square-root completion scale. `MC-497` strengthens the quadratic short-overlap start average by Fourier-Weil diagonalization:

\[
\sum_x|S_{c,x}(H)|^2\ll pH,
\]

so dangerous fixed-length starts occupy only `O(p/H)` conductor residues. `MC-498` maximalizes this to a weighted variable-length tariff

\[
\boxed{
T_{p,H}=\frac pH\log^2(2H),
}
\]

with no residual `sqrt(p)` floor, and expresses endpoint bias through the effective start support or the exact winning-endpoint participation/fibre ratios. `MC-499` shows that one repeated-residue dyadic source block has at most `O(1+Q/p)` endpoint labels, while `MC-500` combines label growth with reciprocal-quotient compression to give the Q-free source-location ceiling

\[
R_{\rm start}\le4+\sqrt{2Z_*/p}.
\]

Hence the corrected source-location admission gate is

\[
\boxed{
Z_*\gg_\delta\frac{p^3}{H^2}\log^4(2H).
}
\]

`MC-501` supplies an independent Q-free gate from the physical source width `Y`. Since first exit shortens every row to at most `1+Y/Q`, a nonempty dyadic overlap band of length `H` forces `Q\ll Y/H`; combining this with the repeated-residue population resource gives, for `H>=4`,

\[
\boxed{
Y\gg_\delta p^2\log^2(2H).
}
\]

Thus a source can have ample location height but still be too narrow to provide both long overlaps and enough distinct repeated-residue starts. Only regimes passing both Q-free gates can make the current endpoint-dispersion certificate feasible.

The lower-prime hard-mask route is now narrower as well. `MC-502` proves that for one complete plus/minus first-exit pair the exact common lower-prime collision law is controlled by `q+r`, and its complete-period normalized sieve coherence satisfies

\[
\rho_{\rm sieve}^{+-}(q,r)
\ll_{h,\mathcal E}
\frac1{\log\max(q,r)}\frac{q+r}{\varphi(q+r)}.
\]

So complete-period hard-mask overlap supplies only logarithmic/totient enhancement, not a conductor power. What remains live there is specifically the **incomplete endpoint/conductor projection** of the exact hard mask, where truncation may retain phase-selective information erased by complete auxiliary-sieve averaging. A genuinely q-dependent pre-aggregation sign, phase, modulus, or reciprocal role remains a separate live arithmetic channel.

## Research question

Can the exact normalized first-exit family produce either remaining load-bearing resource?

For endpoints, do the physical source width, source location, and overlap-length regime pass both corrected Q-free gates at any material scale? If so, which dyadic q-blocks pass the `MC-499` population gate, and on those blocks do the exact winning-endpoint weights pass the `MC-498` participation/fibre threshold?

Beyond endpoints, can **incomplete projection** of the retained `q+r`-structured lower-prime hard masks create a centered conductor weight with fixed negative correlation against the relative phase, despite the complete-period logarithmic ceiling of `MC-502`? Or can another exact source operation produce a genuinely q-dependent signed/complex coefficient before the nonnegative aggregation of `MC-495`?

If neither resource survives with all reconstruction costs restored, the normalized empty-vector first-exit continuation should be closed and attention returned to separately retained nonempty rough-block, boundary, or pre-positive cross-component channels.

## Why it may matter

The surviving question is no longer whether more averaging variables can be exposed. Exact reductions repeatedly show that visible multiplicity, shifts, support labels, endpoints, and complete hard-mask overlaps can collapse before they yield conductor-scale cancellation. The corrected `MC-497`--`MC-502` chain now separates negative outcomes cleanly: failure of either Q-free source-width/location gate makes the entire endpoint-dispersion certificate method-limited for every dyadic `Q`; passing those but failing the per-block population gate makes that block population-limited; passing all three but failing the exact participation/fibre audit isolates a source-localization or quotient-folding problem; and replacing the incomplete lower-prime profile by its complete-period pair overlap can yield at most the `q+r` logarithmic/totient coherence of `MC-502`.

That ordering prevents detailed coefficient audits or fresh complete-period sieve calculations in regimes where the current mechanism is structurally incapable of producing a conductor power.

## Decisive test

Work in the `R=T=1` empty-vector source frame and retain the exact first-exit cell

\[
E_q=\{n:q\mid n(n+h),\ (n(n+h),P(q))=1\}
\]

with exact shortened endpoints and all source/reconstruction coefficients.

For the quadratic endpoint-only branch, partition the material source into dyadic overlap-length bands. For each band compute

\[
T_{p,H}=\frac pH\log^2(2H).
\]

First record the physical source width `Y` before division by the first-exit label and the source location `Z_*=max(X,X+h)`. For every band with `H>=4`, test the `MC-501` width gate

\[
Y\gg_\delta p^2\log^2(2H)
\]

and the `MC-500` location gate

\[
T_{p,H}\ll_\delta4+\sqrt{2Z_*/p}.
\]

If either fails, record that source-width/location regime as method-limited: no dyadic `Q` can supply both the needed physical overlap length and enough physical start diversity for the current exceptional-start certificate.

Only when both Q-free gates are feasible should each repeated-residue dyadic q-block be compared with the `MC-499` population ceiling `1+Q/p`, or the exact active-label count when available. If the available population is not larger than `T_{p,H}` by the margin required for the target saving, classify the block as method-limited by population.

Only for blocks passing all three admission gates form the actual nonnegative pair weights, split them by the winning start `max(ceil(X/q),ceil((X+h)/r))`, and compute `kappa_+`, `kappa_-`, `D_+`, and `D_-` from `MC-498`. Charge the number of dyadic bands and the original shell/reconstruction weights. If the corrected `MC-498` threshold holds with enough margin, endpoint-only bias is closed on that block. If it fails despite ample width, location height, and label population, isolate whether the loss comes from quotient folding, winning-side imbalance, or genuine coefficient localization.

For the remaining hard-mask route, compute the exact projected overlap weight

\[
w(t)=\sum_{m\equiv t\ (p)}A(m)B(m)
\]

with lower-prime pair-sieve factors retained. Split its conductor profile into the complete auxiliary-sieve contribution and the endpoint/truncation discrepancy. Charge the complete piece by the `MC-502` `q+r` coherence ceiling rather than reopening complete-period local-density analysis, and estimate only the centered **incomplete discrepancy** against `chi(1-t^{-2})`. Do not replace `w` by a smooth, uniform, random, or interval model unless the replacement error is quantitatively transferred.

For any pre-aggregation proposal, identify the first exact formula where two first-exit labels occupy genuinely different arithmetic roles inside the transformed kernel or coefficient. A scalar row factor, affine relabeling, increased multiplicity, or complete-period `q+r` collision factor does not pass.

## Evidence boundary

`MC-484` proves exact selector-free Buchstab first exit and retains the dimension-two pair sieve. `MC-485`--`MC-495` close coefficient-blind phase-frame, affine-shift, partition, dilation, completed repeated-residue, and multiplicity-only loopholes. `MC-496` closes long endpoint-only overlaps. The corrected `MC-497` proves `O(pH)` fixed-length start energy in the quadratic case; `MC-498` gives the corrected maximal/effective-support tariff `pH^{-1}log^2(2H)`; `MC-499` supplies the per-block source-population ceiling; `MC-500` supplies the Q-free source-location ceiling; `MC-501` supplies the independent Q-free source-width ceiling obtained by restoring exact row shortening; and `MC-502` proves that complete-period plus/minus lower-prime hard-mask coherence is controlled by divisors of `q+r` and is only logarithmic/totient-sized.

None of these findings evaluates all material source-width/location/length regimes for the full q-vdC reconstruction, computes the exact participation ratios on triply feasible blocks, controls the **incomplete endpoint discrepancy** of the lower-prime hard-mask conductor profile, derives a new q-dependent signed/complex pre-aggregation coefficient, or improves `M(x)`. `MC-456` remains a neighboring positive template only; it is not evidence that the required quotient-breaking structure exists here.

## Research disposition

The clue remains `accepted`. The endpoint audit is strictly staged: **apply the MC-501 Q-free source-width gate and the corrected MC-500 Q-free source-location gate first; only surviving regimes proceed to the MC-499 per-block population gate; only triply feasible blocks proceed to the exact MC-498 winning-endpoint participation/fibre audit**. Failure at any of the first three stages is a limitation of the present endpoint-dispersion certificate, not evidence for true phase bias.

The lower-prime branch is now also staged: **complete-period pair coherence is closed at logarithmic/totient scale by MC-502; only the incomplete endpoint/conductor discrepancy remains admissible as a phase-selective hard-mask resource**. Genuinely q-specific pre-aggregation arithmetic asymmetry remains an independent admissible route.