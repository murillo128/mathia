# MI-053 — The corrected odd archimedean block has an exact sharp negative bulk floor

**Evidence level:** exact source-specific synthesis from WI-363--[WI-369](../../findings/WI-369-desogus-gamma-corrected-odd-block-has-sharp-negative-bulk-floor.md). These statements audit the current Desogus source-to-cell derivation and do not establish or refute RH.

WI-367 repairs the diagonal half-density bookkeeping and WI-368 shows that the printed gamma cancellation fails at the nonlocal cross-kernel sign. WI-369 now resolves the archimedean-only reserve question exactly. On the common test core, the full gamma-corrected odd block decomposes as

`A_A[f] + C_Gamma ||f||_2^2 = screened-difference[f] + endpoint[f] + gamma-image[f]`,

with all three terms nonnegative and `C_Gamma = pi/2 + gamma + log(8 pi)`. Hence `A_A >= -C_Gamma I`.

The lower bound is asymptotically sharp: fixed interior test functions make all three positive remainders vanish as the scale `A -> infinity`, so the form bottom tends to `-C_Gamma`. The corrected archimedean collar therefore cannot supply a positive uniform OSPR/Schur reserve on the full cofinal test core. This is stronger than the earlier failure of comparison with a bare Carleman reserve.

The surviving repair must be source-conditioned. The arithmetic/source/polar channels must contribute at least the fixed debit `C_Gamma` on the subspaces reached by the induction, or the source geometry must exclude the interior bulk quasimodes that attain the negative floor. A new positive nonlocal channel could also change the form, but it must be genuinely absent from the decomposition above rather than a scalar or endpoint renormalization.

**Boundary.** WI-369 is a barrier to an archimedean-only reserve, not to the full Weil operator or every rooted/Schur induction. It does not prove that the source-conditioned surplus is unavailable.