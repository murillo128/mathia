# MI-058 — One-sided full-grid cost is post-convolution variation plus sign polarization

**Evidence level:** exact positive-part decomposition from [FD-265](../../findings/FD-265-full-grid-one-sided-escape-requires-negative-triangle-saturation.md), refining the absolute replication ledger of MI-056 and the signed-average collapse of MI-057.

Let `U_N(q)=M(qN)-M((q-1)N)` and let the divisor-smoothed block field be `G_N(d)=sum_(q|d) U_N(q)`. For the canonical real full-grid repair, `c_N(d)=-G_N(d)/2`. On a dyadic band `I_x`, write `L_N=sum_(d in I_x)|G_N(d)|` and `S_N=sum_(d in I_x)G_N(d)`. FD-265 gives the exact one-sided identity

`R_N^-(x)=1/4(L_N(x)+S_N(x))+O(x log x)`

for the rounded repair, while FD-264 identifies `S_N(x)` with a positive Mertens scale average.

This separates two losses that raw block-population arguments conflate. First, Mertens block variation must survive the divisor convolution `U_N -> G_N`; the replication ledger only upper-bounds the resulting `L_N`. Second, even a large `L_N` produces little negative repair demand only in the extremal regime `S_N/L_N -> -1`. Thus a large post-convolution field can evade a positive cushion only by becoming almost entirely nonpositive in `l^1` mass.

Equivalently, any uniform triangle gap `S_N >= -(1-eta)L_N` converts a lower bound for `L_N` into a one-sided lower bound without losing the depth exponent. The exact physical certificate is therefore the positive divisor-smoothed block mass `sum (G_N(d))_+`, not raw block count, raw block amplitude, total variation alone, or the signed band mean alone.

The live arithmetic source problem is correspondingly two-stage: prove enough Mertens variation survives divisor smoothing, and prove the surviving field stays quantitatively away from total negative polarization. A theorem controlling only one of those stages does not yet cross the positive-capacity boundary.

**Boundary.** FD-265 proves no lower bound for `L_N`, no triangle gap, and no new estimate for Mertens blocks. The identity is specific to the canonical full-grid repair plus its controlled rounding error. Switched-only constructions, sharper response cones, or different physical lifts can obey a different one-sided ledger.