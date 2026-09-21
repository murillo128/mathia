# MI-064 — Soft-sparse Hilbert fidelity has a sharp tail-resolution budget

**Evidence level:** exact metric-embedding synthesis from [AF-474](../../findings/AF-474-best-s-term-tail-mass-gives-sharp-additive-hilbert-fidelity.md), interpreted against the hard-support theorem [AF-472](../../findings/AF-472-hard-support-budgets-have-exact-square-root-hilbert-distortion.md) and the all-scales obstruction [AF-473](../../findings/AF-473-any-positive-tail-budget-destroys-scale-free-hilbert-fidelity.md). Best-`s`-term approximation and sparse `ell^1`/`ell^2` comparison are classical; the line-specific content is the exact tail/resolution ledger for the probability-source geometry used here.

For a probability law `mu`, let `tau_s(mu)` be its best `s`-term tail mass. The canonical coordinate Hilbert embedding `H(mu)=sqrt(2) mu` obeys

`((d_1(mu,nu)-tau_s(mu)-tau_s(nu))_+)/sqrt(s) <= ||H(mu)-H(nu)||_2 <= d_1(mu,nu)`.

Hence on the soft-sparse class `tau_s<=epsilon`, every source separation `d_1(mu,nu)>=delta>2epsilon` has multiplicative distortion at most

`sqrt(s)/(1-2epsilon/delta)`.

The discontinuity between AF-472 and AF-473 is therefore specifically an **all-scales** discontinuity. A positive diffuse tail still permits arbitrarily high-dimensional switches below its absolute mass scale, so no finite scale-free distortion survives on the full soft class; but above a declared resolution the same tail has a finite, explicit additive cost and the hard-support `sqrt(s)` factor reappears.

This turns approximate sparsity into a three-resource statement rather than a yes/no property. The support budget `s`, tail mass `epsilon`, and smallest downstream separation `delta` must be controlled together. Increasing `s` may reduce the tail while worsening the Hilbert factor, and the conditioning diverges as `delta` approaches `2epsilon`.

**Boundary.** The positive theorem is for the canonical coordinate Hilbert representation and the full soft-sparse source class. It does not prove that a physical arithmetic source has a useful best-`s`-term tail profile, that its destination theorem tolerates a separation floor above `2epsilon`, or that narrower correlated tails cannot do better. Those are source- and destination-specific obligations.