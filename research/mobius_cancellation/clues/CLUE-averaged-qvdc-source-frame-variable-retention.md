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
---

# Can the staged factor-weighted source kernel beat the Möbius source-frame tariff?

## Observation

The factor-specific route still starts from the staged decomposition

\[
w(m)=\sum_{r\mid m}\alpha_r B_\beta(m/r),
\qquad
B_\beta(y)=\sum_{s\mid y}\beta_s,
\]

but the surviving channels are now more sharply separated.

`MC-459`--`MC-467` price the generic staged source geometry: the true residual diagonal is only subpower, compatible gcd sectors collapse to one normalized anchor modulus, favorable normalized-gcd classes are sparse even under Fejér weighting, large outer gcd gives no net advantage, and support growth is coupled to shrinking source-interval length. In the nonendpoint bulk,

\[
A_XH_X\le 4\frac{N}{RT},
\qquad
M_X<\frac{2N}{\eta pR},
\]

with `R=[r,r']` and `T=r'/(h,r')`.

`MC-468` shows that generic well-factorability supplies no missing anti-concentration theorem. `MC-469` then opens a concrete modified linear-sieve decomposition. Its empty-vector component has

\[
\alpha=\delta_1,
\qquad
\beta=\lambda^{(0)},
\qquad
R=T=1,
\]

so no growing outer-support suppression applies. `MC-470` identifies the base residual as a nonnegative upper-sieve boundary count

\[
B(y)=B_{\lambda^{(0)}}(y)
=R_z(y)+E(y),
\qquad
R_z(y)=\mathbf 1_{(y,P(z))=1},
\qquad E(y)\ge0.
\]

Its internal coefficient signs therefore cannot supply the missing oscillation.

`MC-471` removes a further apparent resource specific to this unavoidable base cell. Because `r=r'=1`, the staged reciprocal coordinate is only a divisor parametrization of the fixed translated-ratio phase. The base correlation recombines exactly to

\[
C_h^{(0)}(I)
=
\sum_{n\in I}
K_h(n)B(n+h)B(n),
\qquad
K_h(n)=\chi(n+h)\overline{\chi(n)}
=\chi\!\left(\frac{n+h}{n}\right)
\]

on nonzero character support. If `n+h=sj`, the staged phase `chi(j) overline{chi(j-h/s)}` is exactly the same `K_h(n)` after the constant `chi(s)` factors cancel. Thus `D_s=h/s` is not an independent source-phase resource in the empty-vector cell.

The exact positive-amplitude decomposition is

\[
B(n+h)B(n)
=
R_z(n+h)R_z(n)
+R_z(n+h)E(n)
+E(n+h)R_z(n)
+E(n+h)E(n).
\]

`MC-472` now closes the complete-period arithmetic of the leading rough×rough term. After removing the conductor prime from the small-prime modulus when necessary, write

\[
W_z=\prod_{\substack{q<z\\q\ne p}}q,
\qquad
A_{W_z,h}(n)=\mathbf 1_{(n(n+h),W_z)=1}.
\]

For `h not=0 (mod p)`, the exact joint-period identity is

\[
\sum_{n\bmod pW_z}K_h(n)A_{W_z,h}(n)
=-W_z\delta_{W_z}(h),
\]

where

\[
\delta_W(h)=\prod_{q\mid W}\left(1-\frac{\nu_q(h)}q\right),
\qquad
\nu_q(h)=1\ (q|h),\quad 2\ (q\nmid h).
\]

Thus the normalized complete mean is exactly `-delta_W(h)/p`: the character coordinate and the pair-sieve coordinate factor under CRT. There is no additional complete-period sieve/phase resonance. If `z>2`, all odd-shift rough×rough terms vanish exactly, while the uniform shift average satisfies

\[
\frac1W\sum_{h\bmod W}\delta_W(h)
=\left(\frac{\varphi(W)}W\right)^2.
\]

The `q|h` local enhancements therefore redistribute pair-sieve mass rather than creating free average density gain.

There is also a direct prior-art boundary. Gong--Jia--Korolev prove, for prime conductor and `N` above `p^(1/2+epsilon)`, logarithmic cancellation in `sum f(n)chi(n+a)` for every `1`-bounded multiplicative `f`. Taking `f(n)=R_z(n) overline{chi(n)}` controls the **one-sided** rough sum `sum R_z(n)K_h(n)`; translating `n+h` gives the symmetric one-sided statement. The theorem does not apply to the joint coefficient `R_z(n)R_z(n+h)`, which is not multiplicative, and supplies only logarithmic rather than conductor-power saving.

The live base problem is therefore no longer generic factorability, one rough coefficient, or a complete-period pair-sieve mean. It is the **incomplete joint-period discrepancy** of the fixed translated-ratio phase against simultaneous shifted roughness, together with the positive first-exit boundary terms. Nonempty rough-block components and pre-positive cross-component interference remain separate channels.

## Research question

Can the concrete staged-sieve decomposition produce a strict conductor-power gain through one of the mechanisms that survives `MC-472`?

For the **empty-vector base component**, the primary rough×rough target is now the centered incomplete discrepancy

\[
\mathcal D_{W,h}(I)
=
\sum_{n\in I}
\chi\!\left(\frac{n+h}{n}\right)
\mathbf 1_{(n(n+h),W)=1}
+\frac{|I|}{p}\delta_W(h),
\]

with `W=W_z` and even `h` when `z>2`. Can incomplete trace-function cancellation, simultaneous shifted roughness, or a genuinely bilinear/dispersion representation give a conductor-power bound for this discrepancy that is unavailable from the exact complete-period factorization and the one-sided shifted-character theorem?

The three boundary variants obtained by replacing one or both rough indicators by `E` remain separate live targets. Their positive first-exit structure may interact differently with the character phase and is not covered by `MC-472`.

A staged divisor representation is still admissible, but only when it exposes a bilinear, dispersion, or cross-component structure that is **not already present as a reparametrization** of the recombined `n`-sum. Merely varying the reciprocal coordinate `h/s`, re-deriving the local pair-sieve density, or completing to a full `pW` period does not qualify in the base cell.

For **nonempty rough-block components**, after discarding every bin tuple whose product cannot enter the `MC-467` small-outer region, does the surviving normalized signed mass remain large and structured enough for factor-specific dispersion to matter?

A third channel is **cross-component interference**. It is admissible only if the complete signed finite decomposition is carried through an oscillatory transform before componentwise absolute values or positive quadratic closure.

## Why it may matter

The route has moved from a generic appeal to factorability to a narrowly defined arithmetic interaction. Large gcd, extra factor labels, Fejér concentration, independent support/interval tuning, generic well-factorability, blanket support pruning, internal signs of the empty-vector upper-sieve residual, the apparent reciprocal source degree of freedom, and now complete-period pair-sieve resonance have all been priced or removed as standalone resources.

At the same time, prior art rules out spending effort on the simplest remaining surrogates: one rough multiplicative coefficient against the shifted character is already controlled in the long range, while the exact complete pair-sieve period factors by CRT. The unresolved object starts at the **incomplete** translated pair constraint, exactly where multiplicativity is broken and completion no longer closes the estimate.

A positive estimate here would therefore identify a genuinely incomplete joint character-versus-sieve mechanism. A negative estimate showing that this discrepancy and the boundary channels still pay the existing source tariff would bring the componentwise architecture close to closure and leave only nonempty components or pre-positive cross-component interference.

## Decisive test

For the **base component**, set `R=T=1` from the outset and work first in the recombined `n` representation. Separate

\[
B(n+h)B(n)
=
R_hR+R_hE+E_hR+E_hE.
\]

1. For rough×rough, remove odd `h` exactly when `z>2`, subtract the complete mean `-delta_W(h)/p`, and target the centered discrepancy `mathcal D_{W,h}(I)`. Derive either a strict conductor-power saving in the actual source-interval regime or a quantitative obstruction showing that available incomplete trace-function/sieve machinery cannot pay the source budget. Re-deriving the local singular-series factors or using complete `pW` blocks is not progress.

2. Keep the exact two-residue local sieve pattern for even shifts, including every `q|h` degeneration, but do not count those degeneracies as average density gain: `MC-472` proves that their uniform shift average is exactly the independent reduced-residue baseline.

3. For the mixed and boundary terms, use the exact first-exit formula from `MC-470`. Its rank condition may be used only after proving a quantitative count or weighted estimate on the actual shifted pair trajectories; nonnegativity and high rank alone are not sparsity.

4. Use the Gong--Jia--Korolev one-sided theorem only as a prior-art/control benchmark. A logarithmic one-sided saving does not satisfy the conductor-power target, and applying it to `R_z(n)R_z(n+h)` by pretending that coefficient is multiplicative is invalid.

5. Return to a staged divisor representation only if the transform preserves information absent from the recombined form, such as a genuine bilinear modulus split, a factor-specific off-diagonal phase coupled to the pair-sieve condition, or signed cross-component interference. The identities in `MC-471` and `MC-472` kill arguments based solely on counting `h/s` as new source occupancy or on complete-period sieve/phase interaction.

Keep exact `(U,D)` collision aggregation wherever the staged form is used, and isolate the near-complete endpoint `L_X>(1-eta)p` instead of absorbing it into a bulk estimate. Any claimed saving must survive shell summation, Fejér weights, endpoints, coefficient normalization, and source depth.

For **nonempty components**, use the exact lower support `a>D_1...D_r` to remove impossible bin tuples before estimating anything else. Price only surviving tuples with their actual scalar normalization/sign and Fejér participation factor.

For **cross-component interference**, retain the signed finite sum through the proposed transform and exhibit an explicit cross term whose cancellation remains after normalization and source-length costs. Separate positive energies followed by a later appeal to cancellation do not qualify.

## Evidence boundary

`MC-467` is a shellwise geometric restriction, not a bound for the full staged kernel. `MC-468` rules out generic anti-concentration from well-factorability. `MC-469` shows that the concrete upper-sieve decomposition contains an unavoidable base component at `R=T=1`. `MC-470` proves that its residual is a nonnegative rough-plus-boundary count. `MC-471` proves that its staged reciprocal coordinate is not independent source information and identifies the exact two-sided pair-sieve target; it also imports the classical one-sided shifted-character theorem only in its legitimate long-range multiplicative-coefficient regime. `MC-472` proves only the exact complete-period factorization, parity gate, and uniform shift-average density identity for rough×rough; it does **not** estimate the incomplete discrepancy.

None of these findings proves a power saving for the centered rough×rough discrepancy, any boundary term, the nonempty components, or cross-component interference. No conductor-power gain, Möbius bound, zero-free region, or RH consequence has been obtained.

## Research disposition

The clue remains `accepted` and is **materially narrowed through `MC-472`**. The immediate base test is now a conductor-power estimate for the centered incomplete pair-sieve discrepancy on even shifts, not generic staged source occupancy or complete-period correlation. One-sided roughness, the reciprocal divisor coordinate, odd rough×rough shifts, and complete CRT factorization are controls rather than candidate missing resources. Positive first-exit boundary terms, nonempty rough-block pruning, and pre-positive cross-component interference remain distinct surviving channels.