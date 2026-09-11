# MI-002 — A compatibility equation can reduce independent phase freedom to one symmetry

**Evidence level:** supported; the recovery model is classical and its transfer to another source requires an explicit identification.

For a signal on a finite abelian group with every Fourier coefficient nonzero, retain `P_f(chi)=|fhat(chi)|^2` and

\[
B_f(\chi,\psi)=\widehat f(\chi)\widehat f(\psi)
\overline{\widehat f(\chi\psi)}.
\]

If two signals have the same `P` and `B`, their Fourier ratio `r=ghat/fhat` satisfies `|r(chi)|=1` and `r(chi psi)=r(chi)r(psi)`. Thus `r` is one character, i.e. the two signals differ only by translation. Magnitudes alone leave many nontranslation phase assignments. The operative datum is the multiplication compatibility equation, not an injunction to retain more information ([AF-004](../../arithmetic_fidelity/findings/AF-004-third-order-coupling-repairs-quadratic-phase-loss.md)). Nonvanishing is essential to this argument; it supplies no uniform inverse bound near zero coefficients.

In the prime-ray Gram problem the missing relation is different. For logarithmic valuation differences `Delta_p`, independent Cauchy coordinates give `exp(-sum_p|Delta_p|/2)`, whereas one common Cauchy coordinate gives `exp(-|sum_p Delta_p|/2)`. Both have the same one-coordinate laws. Independence is an all-coordinate factorization identity, not a consequence of those marginal laws or of positivity ([WP-234](../../weil_positivity/findings/WP-234-gamma-and-bost-connes-critical-grams-are-common-versus-independent-cauchy-couplings.md)).

The concrete question transferable between these models is which source identity couples the retained coordinates and removes their residual freedom. The bispectral character equation answers it in AF-004; it has not been identified with an arithmetic factorization law in the Weil problem. In particular, AF-004 is not evidence that three-prime tests suffice: [MI-009](MI-009-local-correctness-does-not-determine-global-coherence.md) contains explicit obstructions to every fixed marginal order.
