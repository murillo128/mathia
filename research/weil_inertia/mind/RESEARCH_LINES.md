# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Rule out zero-critical supports using the aperture-growing prime family, not finite screening shadows

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`, `MI-021-complete-screening-promotes-support-avoidance-to-prime-deleted-spectral-criticality`, `MI-022-fixed-finite-prime-power-screening-cannot-buy-prime-deleted-spectral-coercivity`.

WI-281 shows that complete one-signed screening forces `log 2` support packing and the strict scalar budget `K_pack<K_+`. WI-282--WI-283 prove that adding every prime-power lag, full essential span and the prime-translation support-domination shadow of the Suzuki null equation still leaves that packing relaxation sharp. Pure support topology is exhausted.

WI-284 restores the full first-crossing form constraint before scalar compression. If a nonnegative null mode screens every active prime-power autocorrelation and `E={v>0}`, then the von Mangoldt translation form vanishes on the **entire** supported form-domain subspace `D_E`. Since the first-crossing form is PSD and `v` is null, the prime-deleted gamma-plus-pole form restricted to `D_E` is PSD with bottom exactly zero.

WI-285 now blocks every fixed-finite-base approximation to that target. For any fixed finite set of primes, one can build arbitrarily sparse full-span supports that avoid every power `k log p` of those bases, yet contain odd vectors whose prime-deleted Rayleigh quotient tends to `-infinity`. Support measure, span, fixed-family packing and even fixed-family maximal domination therefore do not control the restricted bottom.

The highest-value one-signed theorem must use information absent from that construction: the fact that the number of active prime bases grows with aperture, quantitative amplitudes from the actual null equation, or another source-specific coupling tying the support to the full operator. A finite list of prime lattices, no matter how many powers are included from each, cannot supply the required coercivity.

The direct contradiction target remains

`for every admissible completely screened E, inf q_arch^a|_(D_E) != 0`,

ideally by producing a negative direction or proving a strictly positive bottom. But WI-285 sharpens the quantifiers: the proof must be genuinely **uniform in the growing active prime family** rather than obtained from any fixed finite screening template. A quantitative negative gap in that regime would also create a currency for incomplete screening.

## Keep complete-screening spectral criticality separate from the sign-changing and incomplete branches

The operator-domain deletion in WI-284 uses one-signedness to turn zero autocorrelation into support disjointness and uses complete screening to erase every prime term. Sign-changing cancellation does not imply disjointness, and one surviving prime lag destroys the prime-deleted identity. WI-285 concerns fixed finite screening shadows and therefore cannot be promoted to a statement about the complete branch. Progress must state which hypothesis is being relaxed and what quantitative replacement is retained.

## Keep endpoint firstness, source reserve, growing-family rigidity and sign geometry as separate gates

The reserve inequalities are sign-independent, while the support/spectral bootstrap uses a one-signed mode. A support-sensitive archimedean contradiction would not prove that the relevant first mode has one sign, and a sign theorem would not by itself close the quantitative reserve. WI-285 additionally separates finite-base packing information from the aperture-growing arithmetic diversity that complete screening supplies. Future work should state which gate is being crossed.
