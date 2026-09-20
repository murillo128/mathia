# MI-055 — Late endpoint collars are gamma-positive; the negative debt is inherited bulk

**Evidence level:** exact archimedean synthesis from [WI-369](../../findings/WI-369-corrected-archimedean-decomposition-has-a-universal-negative-floor.md), [WI-373](../../findings/WI-373-digamma-multiplier-gives-the-exact-negative-index-profile.md), and [WI-374](../../findings/WI-374-gamma-endpoint-reserve-expels-negative-debt-from-late-collars.md). This is a statement about the corrected gamma block on sufficiently late endpoint collars; it does not prove positivity of the rooted/common-cut Schur complement or of the full Weil form.

WI-369 writes the corrected archimedean block as a universal negative floor plus explicitly nonnegative terms. WI-373 identifies the bulk negative spectral profile exactly through the digamma multiplier. WI-374 adds a spatial localization fact that changes where this debt can live.

If a test function is supported in an endpoint strip of physical width `r`, the corrected decomposition gives the local lower bound

`A_A[f] >= (H(r)-C_Gamma)||f||^2`,

with `H` decreasing and divergent at the endpoint. For the Desogus collar geometry `a_j=(1/2)log j`, the new collar width is `(1/2)w_k`, `w_k=log(1+1/k)`. WI-374 proves elementarily that `H(w_k)>C_Gamma` for every `k>=16384`. Hence sufficiently late fresh collars are already nonnegative for the corrected gamma block.

The important distinction is **where the negative index is generated**. The linearly growing gamma debt of WI-373 is a bulk/interior phenomenon; it is not recreated locally each time a new sufficiently thin endpoint collar is appended. A common-cut or rooted-Schur construction should therefore not budget fresh negative gamma debt against every late shell. Its hard part is the inherited old core and the coupling between that core and newly positive collars.

This local positivity does not erase the global spectral profile. Old interior modes may still carry the full digamma negative sector, and Schur complementation can transmit their effect through old--new coupling. What changes is the bookkeeping: any repair theorem should separate inherited core debt from the endpoint reserve instead of charging the latter as if it generated new negative directions.

**Boundary.** The collar threshold and lower bound are for the corrected gamma block in the stated geometry. They do not prove that arithmetic terms or Schur cross terms preserve positivity, do not remove the WI-373 bulk quantile requirements for additive repair on the old core, and do not imply RH.