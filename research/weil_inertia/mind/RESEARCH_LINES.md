# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use source/eigenfunction structure beyond scalar profiles and generic cut covariance

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`, `MI-020-complete-one-signed-screening-trades-discrete-vanishing-for-support-packing`.

WI-274--WI-280 separate scalar firstness, retained Hilbert orientation and source-specific compatibility. Oriented cut covariance is stronger than scalar norm profiles, but arbitrary finite covariance mixtures on the generic PSD/null-partition class still admit two-pulse countergeometry. Noncommensurate shifts and more generic Hilbert optimization therefore do not cross the scalar budget wall by themselves.

WI-281 now shows that the actual arithmetic lags can feed back into the admissible geometry on the **one-signed complete-screening branch**. If every active prime-power autocorrelation vanishes, the powers of two alone force the nonzero set of the hypothetical first null mode to be a measurable selector modulo `log 2`, hence of measure at most `log 2`. Riesz rearrangement converts that packing into an exact positive archimedean budget

`K_pack=(1/2) lambda_max(T_(log 2))`,

with the strict inequality `K_pack<K_+` against the unrestricted WI-274 budget. Complete screening therefore implies the stronger necessary condition

`2 int_(a/2)^a lambda_r dr <= K_pack<K_+`.

This is the kind of source-specific compatibility missing from WI-280: the discrete arithmetic hypothesis shrinks the continuous admissible class. It still does not finish the branch. The new constant need not lie below the actual spectral-area lower bound, and the first null mode has not been proved one-signed.

The live continuation is to exploit **more of the actual source equation than power-of-two packing**. Add other prime lags, firstness/null-equation constraints, nodal/regularity information, or a nonlinear invariant that lowers the admissible budget further. In parallel, the sign-changing branch remains separate and needs its own mechanism; one-signed packing cannot simply be transferred to it.

## Keep scalar exhaustion, generic Hilbert geometry and arithmetic compatibility distinct

WI-279 proves that scalarizing the cut path loses information. WI-280 proves that generic Hilbert orientation is still too large a class. WI-281 proves that a concrete arithmetic screening hypothesis can shrink that class quantitatively. The next theorem should identify which additional source constraints survive without assuming the desired sign or RH conclusion.

## Keep endpoint firstness, source reserve, sign geometry and prime overlap as separate gates

The reserve inequalities are sign-independent, while the packing bootstrap and prime-overlap tariff currently use a one-signed mode. A successful packing improvement does not prove that the relevant null mode has one sign, and a sign theorem does not by itself close the quantitative reserve. Future work should state which gate is being crossed.
