# MI-026 — Page balance prices the subset spectrum, and a strong exception enlarges the exclusion band

**Evidence level:** exact line-specific consequence of [MC-293](../../findings/MC-293-landau-page-low-source-cost-near-negative-spectrum.md)--[MC-297](../../findings/MC-297-pair-overlap-stability-of-endpoint-page-spectrum.md), sharpened conditionally by [MC-299](../../findings/MC-299-deuring-heilbronn-expands-page-source-band.md). MC-293 imports classical Landau--Page uniqueness; MC-299 uses classical explicit Deuring--Heilbronn repulsion. MC-298 separately shows that bounded overlap order does not determine Page parity. No arithmetic impossibility theorem for the full actual Legendre shell and no bound for `M(x)` is claimed.

For a nonzero shell functional `lambda`, let `Q(lambda)` be the minimum lower-prime product cost realizing it. Below the quasi-subpower Page threshold `D_y`, MC-293 shows that every generated mode is asymptotically balanced except possibly one Landau--Page exceptional functional. MC-294 turns many selected near-negative directions into a high-cost quotient-dimension bill, while MC-295 shows that a generic fixed-weight model can still pay that bill.

MC-296--MC-297 strengthen the bill from basis cost to subset-spectrum cost. Disjoint defect sets make almost every noncentral subset sum expensive, and overlap is the finite-harmonic correction that can soften the upper half. MC-298 then shows that no **fixed** hierarchy of overlap moments determines high-cardinality parity in a generic endpoint system, so adding finitely many intersection levels cannot by itself close the escape.

MC-299 supplies a different arithmetic mechanism. If the sole allowed Page exception is genuinely near-negative, its associated real zero satisfies `1-beta_* << 1/(log y log log y)`. Deuring--Heilbronn repulsion then makes every other shell mode with

`Q(lambda) <= E_y = exp(kappa_A log(y) log log log(y)/log log(y))`

smaller than any chosen power of `1/log y`, for sufficiently small fixed `kappa_A`. The old Page band had logarithm only `Theta(log y/log log y)`, so the exceptional mode **pushes all competing near-negative directions outward by an unbounded `log log log y` factor in the logarithmic cost scale**.

The surviving obstruction is therefore not merely “many expensive basis modes.” Apart from at most one exceptional direction, a near-negative family must occupy a large high-cost subset spectrum beyond the enlarged `E_y` band, while bounded-order overlap data remain generically insufficient to reconstruct parity. A closing theorem can attack the actual arithmetic geometry or the collective capacity of the lower-prime source to realize that family.

**Boundary.** The Deuring--Heilbronn enlargement is conditional on the Page exception actually being near-negative at the stated scale. It does not remove that one mode, control characters beyond `E_y`, or turn individual source-cost lower bounds into a dimension contradiction. MC-298's generic moment-matched controls also remain valid; the new restriction is arithmetic and spectral, not a finite-overlap identity.
