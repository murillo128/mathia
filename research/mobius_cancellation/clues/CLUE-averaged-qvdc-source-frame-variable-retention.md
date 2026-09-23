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
---

# Can load-bearing q-dependent arithmetic asymmetry beat the Möbius source-frame tariff?

## Observation

The empty-vector source has survived a long sequence of exact reductions but most generic summaries are now closed. `MC-472`--`MC-476` rule out direct full-period, inclusion-exclusion, hard-mask Fourier, plain Parseval and coefficient-blind restriction routes. `MC-477`--`MC-483` show that positive or bracketed sieve surrogates either leak too much, retain the hard-mask selector, or force only a polylogarithmic useful cutoff when one demands a fixed conductor-power gain.

`MC-484` supplied the canonical selector-free escape: exact Buchstab first exit writes the hard mask as a signed sum over first-exit primes `q`, leaving a dimension-two residual pair sieve. `MC-485`--`MC-486` close complete and incomplete coefficient-blind inverse-shift frame gains. `MC-487` shows that the common inverse shifts `hq^{-1}` in the phase and residual sieve are affine gauge: in an intrinsic integer coordinate the translated-ratio separation and pair polynomial are fixed, while q-dependence moves to support, cutoff, endpoints and coefficients.

`MC-488` proves that the exact progression-plus-cutoff first-exit cells are disjoint: each source integer in the Buchstab shell has a unique least active prime divisor `q_*(n)`. Their incidence Gram matrix is diagonal and every common unitary transform preserves that orthogonality. If the outer coefficient is common, the q-sum refolds exactly to the original hard-mask difference; with q-dependent coefficients it becomes the one-variable weight `c_{q_*(n)}(n)`.

`MC-489` tests the first literal escape. Rowwise dilation `n=qm` is genuinely q-dependent and can create nonzero cross-row terms after alignment in the `m` coordinate. But the exact hard-mask row has complete energy `(p-2)P(q)d_q` with `d_q >> (log q)^-2`; after removing sieve-period replication its `L^2` size remains `p^{1/2-o(1)}` throughout polynomial q-ranges. The complete cross-row term factorizes into the classical shifted-character correlation times an ordinary local sieve-overlap count. Hence q-dependent coordinates plus coefficient-blind positive `L^2` closure are exhausted.

`MC-490` closes the favorable-scalar-direction loophole for distinct conductor residues. After putting the exact moving hard-mask rows on one common complete period and normalizing each row, any `k=o(p)` first-exit family with distinct residues modulo `p` has Gram matrix `I+E` with `|E_{q,r}|<=2/(p-2)`. A scalar function of the least prime therefore cannot align those rows with a hidden small singular subspace.

`MC-491` prices the repeated-residue branch that `MC-490` left open. If `q!=r` but `q=r (mod p)`, the completed character phases coincide, yet the exact nested pair-sieve masks do not: their normalized coherence satisfies

\[
\rho(q,r)=\frac{d_{q,r}}{\sqrt{d_qd_r}}
\ll \frac{\log\log(3|h(q-r)|)}{\log r}.
\]

Thus in polynomial ranges every repeated-residue pair has coherence `O(log log p/log p)`, and an arbitrary-residue family of size `o(log p/log log p)` is still Riesz-stable.

`MC-492` closes the most direct dense-block interpretation that remained. For `q=r (mod p)`, rows in the **same root branch have identical character phase pointwise**, so with the native Buchstab coefficient and exact nonnegative masks/endpoints every same-root cross term is nonnegative on complete or incomplete intervals. This is independent of block cardinality. Opposite-root completed interaction is instead the exact Jacobi sum `chi(4)J(chi,chi)-1`, hence at most `sqrt(p)+1` and normalized `O(p^-1/2)` pairwise (`O(p^-1)` for quadratic `chi`). Dense conductor collisions therefore matter only if another exact arithmetic step creates q-dependent signs/phases, if a collective cross-root effect beats the Jacobi pair tariff, or if an incomplete signed transform changes the kernel before positive closure.

The live resource is now narrower than “use a q-dependent transform, coefficient, or dense collision.” It must be **load-bearing arithmetic asymmetry inside the inner source variable or kernel before positive closure**, a genuinely incomplete signed transform, or a collective cross-root mechanism with an exact sign structure and restored source costs.

## Research question

Can the exact normalized first-exit family be passed through a justified dispersion, reciprocity, Poisson, staged-factor, or coefficient-sensitive operation in which the first-exit label `q` changes the arithmetic kernel itself — not only the row coordinate or scalar row weight — and for which the resulting signed off-diagonal structure yields a fixed conductor-power gain after all diagonals, endpoints and source weights are restored?

Equivalently, does the exact source frame retain an **inner-coordinate-dependent** least-prime structure strong enough to beat the harmonic/endpoint and `p^{1/2-o(1)}` row tariffs without replacing the exact first-exit cutoff by an uncontrolled envelope? For repeated conductor residues, can the exact source algebra first create a q-dependent sign/phase, or can opposite-root rows exhibit a collective signed effect strong enough to overcome their Jacobi-scale completed pair interaction? If neither such structure nor a genuinely non-complete signed transform survives, the normalized empty-vector first-exit continuation should be closed and research should return to the separately retained nonempty rough-block, boundary or pre-positive cross-component channels.

## Why it may matter

The current chain has separated six notions that initially looked like one source variable. The visible inverse shift is coordinate gauge (`MC-487`); the exact first-exit support is a deterministic least-prime partition (`MC-488`); the natural row-dependent dilation retains the conductor-scale diagonal (`MC-489`); scalar reweighting of a sublinear distinct-residue completed family cannot access a small singular direction (`MC-490`); repeated residues are pairwise decorrelated by their different exact sieve masks (`MC-491`); and, at arbitrary cardinality, the native same-root repeated-residue coefficient has constructive rather than destructive interference (`MC-492`). Repeating those representations cannot create a new averaging dimension.

The surviving positive template remains the asymmetry identified in `MC-456`: in successful neighboring dispersion arguments, factor labels become analytically visible because they enter different modulus or reciprocal-phase roles **before** positive closure. The open question is whether the exact Möbius source frame contains that stronger arithmetic role for `q`, or whether first exit is ultimately only deterministic bookkeeping once all inner-coordinate source data are exposed.

## Decisive test

Work first in the `R=T=1` empty-vector source frame and normalize to the common intrinsic source coordinate. Keep the exact first-exit cell

\[
E_q=\{n:q\mid n(n+h),\ (n(n+h),P(q))=1\}
\]

with exact interval endpoints and source coefficients.

Reject immediately any proposal whose only q-dependence is one of the following already-priced effects: a common transform of the disjoint cells (`MC-488`); the inverse shifts `hq^{-1}` (`MC-487`); complete or incomplete coefficient-blind phase-frame averaging (`MC-485`--`MC-486`); rowwise dilation/completion followed by a uniform positive `L^2` operator bound (`MC-489`); scalar q-reweighting of a sublinear distinct-residue completed family (`MC-490`); isolated/small repeated-residue alignment (`MC-491`); or a dense same-root repeated-residue block carrying only the native common-sign Buchstab coefficient (`MC-492`). A harmless row scaling is not an escape unless the exact reconstruction constants are charged.

For a surviving proposal, identify the first formula at which two first-exit labels occupy mathematically different arithmetic roles **inside the transformed kernel or inner source coefficient**. Examples that pass the admission gate include a q-dependent modulus or reciprocal phase not removable by affine relabeling, a factor-specific pre-positive kernel analogous to `MC-456`, a genuinely `m`-dependent signed/complex law for the actual source coefficient, a proved collective opposite-root interaction beyond the `MC-492` Jacobi pair scale, or an incomplete-interval mechanism outside the complete-period hypotheses. Merely changing coordinates, multiplying each completed row by a scalar, or grouping more same-root primes in one conductor class does not pass.

Then compute the true diagonal and off-diagonal terms before claiming gain. Accept the route only if the final estimate saves a fixed conductor power after coefficient normalization, dyadic q summation, endpoint costs, root collisions, shell reconstruction and all q-vdC/Fejér/staged-sieve weights are restored. A per-q estimate followed by triangle inequality is insufficient unless its aggregate already beats the existing first-exit budget; a positive complete-period norm whose normalized Gram remains well conditioned is likewise insufficient.

Dropping the exact cutoff `A_q` merely to recover overlap of bare progressions `q|n` or `q|n+h` changes the family and must still pay the positive/bracket transfer barriers of `MC-479`--`MC-483`.

## Evidence boundary

`MC-484` proves exact selector-free Buchstab first exit and the residual dimension-two pair sieve. `MC-485`--`MC-486` close complete and incomplete coefficient-blind inverse-shift frame routes. `MC-487` proves that the shared inverse shifts are affine gauge. `MC-488` proves that the exact normalized progression-plus-cutoff cells form a disjoint least-prime partition and remain orthogonal under every common unitary transform. `MC-489` proves that the natural row-dependent dilation passes the literal common-transform gate but retains a `p^{1/2-o(1)}` complete-row diagonal in polynomial q-ranges, with complete cross interactions factoring into character correlation times sieve overlap. `MC-490` shows that for `k=o(p)` distinct conductor residues, the exact hard-mask rows are uniformly well conditioned in every scalar outer-weight direction. `MC-491` shows that repeated conductor residues have only `O(log log p/log p)` pair coherence in polynomial ranges and extends Riesz stability to arbitrary-residue families of size `o(log p/log log p)`. `MC-492` shows that arbitrary-size same-root repeated-residue blocks cannot cancel with the native common-sign Buchstab coefficient, even on incomplete exact intervals, and that complete opposite-root pair correlation is only Jacobi-sum scale.

None of these findings proves or rules out a genuinely factor-specific dispersion/reciprocity theorem, an `m`-dependent signed arithmetic law for exact source coefficients/endpoints, a dense collective opposite-root mechanism beyond the Jacobi pair scale, a signed incomplete-interval conductor-power saving before positive closure, or an improved bound for the Möbius function. `MC-456` supplies only a neighboring quotient-breaking template whose factor-specific modulus geometry must still be derived here.

## Research disposition

The clue remains `accepted`, but the admission gate is stricter again. Closed routes include positive/bracket replacement without transfer control; complete or incomplete coefficient-blind inverse-shift averaging; exploiting the visible `hq^{-1}` motion; cross-q dispersion from exact first-exit supports through one common source transform; q-dependent row dilation/completion followed only by coefficient-blind positive `L^2` closure; scalar least-prime reweighting of sublinear distinct-residue completed rows; isolated/small repeated-residue completed families; and arbitrary-size same-root repeated-residue blocks with the native common-sign first-exit coefficient.

The active test is **inner-coordinate-dependent signed arithmetic q-asymmetry, a collective opposite-root effect that beats the Jacobi pair tariff, or a genuinely incomplete signed transform retained before positive closure**. If no such operation can be derived from the source frame with a quantitative gain, the normalized empty-vector first-exit branch should be treated as exhausted rather than revisiting another scalar, coordinate, or conductor-collision version of the same partition.