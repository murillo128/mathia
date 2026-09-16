# MI-002 — A compatibility equation can reduce independent phase freedom to one symmetry; target-faithful positivity needs the right relational geometry

**Evidence level:** supported; the recovery models are exact/classical, and transfer to another source requires an explicit identification. The positivity extension is grounded in [AF-371](../../arithmetic_fidelity/findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md).

For a signal on a finite abelian group with every Fourier coefficient nonzero, retain `P_f(chi)=|fhat(chi)|^2` and

\[
B_f(\chi,\psi)=\widehat f(\chi)\widehat f(\psi)
\overline{\widehat f(\chi\psi)}.
\]

If two signals have the same `P` and `B`, their Fourier ratio `r=ghat/fhat` satisfies `|r(chi)|=1` and `r(chi psi)=r(chi)r(psi)`. Thus `r` is one character, i.e. the two signals differ only by translation. Magnitudes alone leave many nontranslation phase assignments. The operative datum is the multiplication compatibility equation, not an injunction to retain more information ([AF-004](../../arithmetic_fidelity/findings/AF-004-third-order-coupling-repairs-quadratic-phase-loss.md)). Nonvanishing is essential to this argument; it supplies no uniform inverse bound near zero coefficients.

In the prime-ray Gram problem the missing relation is different. For logarithmic valuation differences `Delta_p`, independent Cauchy coordinates give `exp(-sum_p|Delta_p|/2)`, whereas one common Cauchy coordinate gives `exp(-|sum_p Delta_p|/2)`. Both have the same one-coordinate laws. Independence is an all-coordinate factorization identity, not a consequence of those marginal laws or of positivity ([WP-234](../../weil_positivity/findings/WP-234-gamma-and-bost-connes-critical-grams-are-common-versus-independent-cauchy-couplings.md)).

AF-371 adds a target-property version of the same lesson. The complete reciprocal Taylor sequence of an entire function may determine the function, yet compressing that sequence to the infinite signature “every Hankel matrix is positive” still does not determine Laguerre--Pólya membership: Hamburger gives false positives. Schoenberg's Pólya-frequency characterization succeeds because it retains a different relation, total positivity of all ordered translation minors `det(Lambda(x_j-y_k))`. The distinction is not finite versus infinite positivity; it is **quadratic moment positivity versus ordered relational positivity with an exact target theorem**.

This sharpens the cross-line question. When a scalar positivity route survives only by adding more points, derivatives or inequalities, first ask whether all of those constraints still belong to the same universal Gram/moment geometry. If so, quantity alone need not increase target fidelity. A useful lift must identify a relation whose fibre removes the documented ambiguity or whose sign is equivalent to the destination property in the declared source class.

The concrete transfer question remains source-specific: which arithmetic identity couples the retained coordinates or minors and makes the stronger relational structure nonautomatic? The bispectral character equation answers that in AF-004, and Schoenberg answers the abstract Laguerre--Pólya target through translation total positivity; neither result by itself proves that an existing Weil/Pick construction realizes the required arithmetic kernel.
