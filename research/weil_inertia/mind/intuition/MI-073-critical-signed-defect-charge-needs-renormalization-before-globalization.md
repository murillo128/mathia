# MI-073 — Critical signed defect charge needs renormalization before globalization

**Evidence level:** conditional synthesis from WI-404 and [WI-405](../../findings/WI-405-signed-widder-mellin-averages-collapse-to-superzeta-and-require-renormalization.md), within the recent non-peer-reviewed Widder framework audited in WI-399--WI-400.

WI-404 shows why ordinary nonnegative averaging loses a high defect: for a fixed-depth zero at ordinate `gamma`, every subcritical polynomial height weight assigns vanishing finite-`p` cost as `gamma` grows. The natural response is to retain sign and move toward a critical Mellin weight rather than discard cancellation before integration.

WI-405 shows that this move has its own globalization gate. In the half-plane where the signed pure-power Mellin average is absolutely convergent, the resulting family collapses to classical Voros superzeta data and the desired high-ordinate leverage is not new. At the locally attractive critical weight, by contrast, one gets an exact defect-scale charge for an individual zero or finite configuration, but the corresponding global zero sum is no longer absolutely convergent.

Therefore an exact finite defect charge cannot simply be promoted to a global coercive statistic. Analytic continuation of the superzeta makes a renormalized global quantity meaningful, but it does not preserve a termwise positive decomposition or certify that the local defect contribution survives the subtraction of the divergent/global background. The missing theorem is not convergence by notation; it is a source-specific cancellation or renormalization identity with a retained defect-sensitive remainder.

This separates three currencies that can otherwise be conflated: local sensitivity of the Widder kernel, summability of the zero population, and coercivity of the renormalized global observable. Safe summability can classicalize the family; critical local sensitivity can fail to globalize; and analytic continuation can exist without preserving the sign or localization needed by the inertia argument.

A viable signed route must therefore specify the critical global quantity, the exact counterterm or cancellation law that defines it, and the residual term whose dependence on off-critical displacement is still controlled strongly enough for the destination theorem. Without that bridge, finite-height signed calculations remain local evidence rather than a global RH criterion.

**Boundary.** This synthesis inherits the conditional Widder framework and does not claim that a suitable zeta-specific renormalization exists. It also does not transfer the positive finite-`p` asymptotic of WI-404 to a signed global sum or derive RH from superzeta continuation.