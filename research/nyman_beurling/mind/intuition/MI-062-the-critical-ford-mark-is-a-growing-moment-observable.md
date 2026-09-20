# MI-062 — The critical Ford mark is exactly recoverable at finite depth but can be uniformly invisible to bounded interior probes

**Evidence level:** exact synthesis from NB-237--[NB-245](../../findings/NB-245-cauchy-stieltjes-laws-resolve-ford-cells-but-average-away-depth-marked-blocks.md). No RH-equivalent reconstruction theorem is claimed.

The Ford reduction isolates a depth-marked local coefficient rather than an unstructured phase variable. Earlier work expressed that coefficient through increasingly high moments, jets or derivatives as the strip depth grows. NB-245 clarifies what this does and does not mean for Cauchy/Stieltjes representations.

For a fixed finite carrier law, the unnormalized rational transform `M(z)=sum_r c_r/(z-r)` determines every coefficient exactly: the residues at the known poles recover the `c_r`. There is therefore no finite-dimensional algebraic ambiguity. Calling the critical coefficient “missing from the Cauchy transform” would be false.

The real obstruction is conditioning across a growing family. NB-245 gives pairs whose top depth-marked coefficients differ by order one while their normalized transforms differ by only `O(k/L)` on fixed compact subsets away from the support. Bounded interior probes average away a block that becomes deeper in the carrier even though the complete exact transform remains injective. The critical observable is therefore a growing-resolution quantity.

This puts the burden on a source-available lower modulus, not on uniqueness. A complete exact rational transform with individually resolved poles and residues already contains the answer; the arithmetic question is whether the norm actually supplied by the Nyman/Ford argument resolves the critical block uniformly as the depth grows.

**Boundary.** NB-245 does not prove that every source-faithful observable is ill-conditioned. In particular, it does not rule out local information tied to the smooth Ford current rather than a fixed compact family of normalized Cauchy probes; NB-246 identifies such a separate moving-center mechanism.
