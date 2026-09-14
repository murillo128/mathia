# MI-023 — Two-island Lambert screening localizes to only `X^(1/10+o(1))` candidate pieces inside rare upper prime deserts

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island branch through WI-288--[WI-292](../../findings/WI-292-upper-gap-localization-caps-full-screening-components-at-x-one-tenth.md). Heath-Brown's large-gap theorem and the Peck/Maynard prime-gap second-moment input are prior art. No theorem excludes all remaining candidate components or proves cross-scale independence.

WI-288 reduces complete screening on two symmetric narrow islands to the nearest-prime-power condition and the Lambert-scale separation

`sqrt(x) delta_pp(x) >= W(c sqrt(x))`.

WI-289 resolves the prime-power layers through

`delta_pp(x)=min_(k>=1) k delta_p(x^(1/k))`.

The ordinary-prime layer near `x` demands a `sqrt(x) log x`-scale desert. Prime squares are the unique macroscopically critical composite layer, requiring an approximately mean-gap-sized prime-free interval near `sqrt(x)`; every `k>=3` root window is subunit.

WI-290 shows that the composite-safe lower-scale reservoir is highly fragmented: using the published prime-gap second moment, it has at least `X^(3/8-o(1))` positive-length safe components on `[X,2X]`. WI-291 supplies complementary upper-scale sparsity: the ordinary-prime condition lives in at most `O(X^(1/10+epsilon)/log X)` giant gap hosts of total length `O(X^(3/5+epsilon))`.

WI-292 proves that these two facts can be partially coupled **without any stochastic cross-scale theorem**. Enlarge each eligible upper host by the additive Lambert radius `O(sqrt(X) log X)`. The enlarged total length remains `O(X^(3/5+epsilon))`. A `k`-th power in the dyadic shell has spacing at least a constant multiple of `X^(1-1/k)`, so counting all integer powers—not merely prime powers—through those enlarged hosts gives only `O(X^(1/10+epsilon))` relevant incidences after summing over `k>=2`.

Removing one prime-power Lambert neighborhood can increase the number of components inside an upper host by at most one. Therefore

`# pi_0(F_c(X)) << X^(1/10+epsilon)`

for the full screened candidate set `F_c=A_c intersect R_c`, and at most that many positive-length components of the composite-safe residual can meet the ordinary-prime safe set. Since the global residual has `X^(3/8-o(1))` positive components, the fraction that can even enter an eligible host is at most

`X^(-11/40+o(1))`.

The bottleneck has therefore shifted from a global cross-scale abundance problem to a **rare-host incidence problem**. Almost every lower-scale safe component is deterministically irrelevant. Improving the global count of lower windows cannot close the branch because the surviving arithmetic lives inside only `X^(1/10+o(1))` host-localized pieces.

This is meaningful pruning, not exclusion. The remaining pieces may all be empty after finer arithmetic checks, or some may survive infinitely often. A closing theorem must now show that composite prime powers necessarily hit the rare upper-safe cores, establish a cross-scale avoidance/correlation law strong enough on this selected host family, exploit amplitudes/signs from the null equation, or leave the symmetric two-island topology.

**Boundary.** WI-292 uses only worst-case spacing of integer powers once the upper hosts are localized; it does not prove independence between primes near `x` and `sqrt(x)`, does not rule out any particular candidate host, and says nothing about sign-changing, incomplete-screening or many-island geometries. The exact conclusion is a localization theorem: complete two-island screening can occupy only a polynomially tiny subfamily of the lower safe reservoir.