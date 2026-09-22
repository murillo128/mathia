# MI-059 — Deep positive blocks can only be cancelled by shallow negative divisor ancestry

**Evidence level:** exact one-sided divisor-incidence synthesis from [FD-266](../../findings/FD-266-deep-positive-mertens-blocks-need-negative-divisor-ancestry.md), sharpening the post-convolution sign ledger of MI-058.

Let `U_N(q)=M(qN)-M((q-1)N)` and `G_N(d)=sum_(q|d) U_N(q)`. On a dyadic coefficient band `x<d<=2x`, the top divisor `d` is the only divisor of `d` in that same deep band: every proper divisor satisfies `q<=x`. Therefore

`(G_N(d))_+ >= (U_N(d)-A_N^-(d))_+`,

where

`A_N^-(d)=sum_(q|d, q<d) U_N(q)^-`

is entirely shallow negative ancestry. Summing gives the exact lower certificate

`R_N^-(x) >= 1/2 sum_(x<d<=2x) (U_N(d)-A_N^-(d))_+ - O(x log x)`

for the canonical rounded full-grid repair.

This removes one ambiguity left by MI-058. A positive deep Mertens block cannot be cancelled by another deep block through divisor convolution; same-scale population does not interfere. The only convolutional cancellation channel is negative mass already present on proper divisors. Equivalently, the source must build a signed weighted divisor cover of the positive deep coordinates. With `P_N^+(x)=sum_(x<d<=2x)U_N(d)^+`, FD-266 makes this explicit through a cover cost `C_N^-(x)` and the bound

`uncovered positive mass >= P_N^+(x)-C_N^-(x)`.

The physical consequence is correspondingly sharper. Under the FD-260 positive-cushion capacity, a realizable canonical lift forces the uncovered positive mass to stay below `Lambda_N x^(2-beta)+O(x log x)`, with `beta=log_2(3/2)`. The missing arithmetic theorem is therefore no longer an unspecified `l^1` survival statement for the whole smoothed field. It is a **signed cross-scale incidence estimate** showing that enough positive deep block variation escapes the negative proper-divisor cover to cross the same capacity threshold.

Prime-index deep coordinates illustrate the geometry but do not solve it. For prime `p in (x,2x]`, the only proper divisor is `1`, so when `M(N)>=0` a positive `U_N(p)` transfers without ancestry loss. FD-266 supplies no density, sign or amplitude theorem ensuring enough such blocks, and prime density by itself does not control their Mertens increments.

**Boundary.** The certificate is specific to the canonical full-grid divisor repair and its controlled rounding error. It proves neither a lower bound for the uncovered mass nor a Möbius/Mertens sign theorem. Switched-only repairs or different physical lifts can have a different incidence ledger. The advance is the exact localization of where cancellation would have to come from, not the missing source lower bound itself.