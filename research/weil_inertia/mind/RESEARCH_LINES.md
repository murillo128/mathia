# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

Finite negative inertia detects off-line packets exactly but can lose coercivity with height. The unconditional critical-line exponentials are complete on bounded windows without forming a Bessel/Riesz family, so ordinary separation cannot rule out spectral collapse. Any truncation route still has to price coefficient growth and height tightness explicitly.

## Use source/eigenfunction structure beyond scalar profiles and generic cut covariance

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`, `MI-018-one-signed-first-crossings-pay-prime-overlap-or-short-range-mass`, `MI-019-simultaneous-cuts-create-a-positive-saturated-source-reserve`.

WI-274--WI-277 progressively sharpen the first-crossing source reserve. Complementary masses give the sharp harmonic envelope; one shift gives a sharp nilpotent reserve; finite commensurate families give a scalarized Toeplitz reserve. WI-279 restores the Hilbert orientation of the cut path and obtains the stronger bottom-spectrum reserve from signed cut covariance.

WI-278 nevertheless blocks every reserve whose numerator is controlled only by the currently certified scalar function `a -> lambda_a`: its explicit admissible profile keeps `sup a lambda_a` below the positive archimedean budget. WI-280 now closes the generic **noncommensurate** escape as well. For any finite family of arbitrary shifts with nonnegative weights, abstract PSD/null-partition cut geometry admits a two-pulse path with negative covariance at one selected shift and zero covariance at the others. Therefore every universal weighted covariance coefficient is negative somewhere, and the resulting reserve remains strictly below the scalar average, hence below `sup a lambda_a`.

Noncommensurability, denser shift selection and further generic Hilbert-space optimization are therefore not new resources. A successful continuation must prove a compatibility law for the **actual Suzuki null mode** that excludes the two-pulse countergeometry, strengthen the numerator through the exact signed prime-plus-archimedean source equation, use nodal/regularity information, or introduce a genuinely nonlinear joint invariant not reducible to a positive linear mixture of cut covariances.

## Keep scalar-profile exhaustion, retained Hilbert orientation and source-specific compatibility distinct

WI-279 proves that scalarizing the cut path to a norm profile discards usable orientation: the bottom-Toeplitz reserve can strictly improve the coefficient. WI-280 proves that this extra generic orientation is still insufficient once its numerator remains the same scalar firstness data. The distinction is now exact: **Hilbert geometry contains more information than the scalar profile, but generic Hilbert geometry still admits counterpaths that prevent a budget crossing.**

The remaining opportunity is not another universal covariance inequality. It is a theorem showing that the source-generated cut path occupies a strictly smaller admissible class than generic PSD null partitions, in a way that quantitatively improves the limiting numerator/covariance combination.

## Keep endpoint firstness, source reserve, sign geometry and prime overlap as separate gates

The reserves are sign-independent, while the prime-overlap tariff is currently one-signed. A successful source-specific reserve improvement does not by itself solve the sign-changing branch, and a sign theorem does not replace the quantitative reserve. Future work should state which gate is being crossed.