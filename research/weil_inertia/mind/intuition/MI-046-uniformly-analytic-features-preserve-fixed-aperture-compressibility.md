# MI-046 — Uniform projective continuity preserves fixed-aperture compressibility

**Evidence level:** exact synthesis from [WI-345](../../findings/WI-345-fixed-degree-polynomial-carriers-remain-compressible.md), [WI-346](../../findings/WI-346-uniformly-analytic-bow-features-remain-compressible.md), and [WI-347](../../findings/WI-347-extensive-bow-feature-rank-requires-projective-resolution-collapse.md). Polynomial/analytic approximation and Kolmogorov-width mechanisms are classical in broad form; the Mathia content is the fixed-aperture projective-resolution consequence for the bow carrier.

WI-344 proves that one bounded logarithmic source aperture cannot support an extensive family of scale-preserving height directions after fixed height-independent linear preprocessing. WI-345 and WI-346 show that the same compression survives fixed-degree polynomial/tensor enrichment and uniformly analytic height-independent maps with controlled coefficient budget and transmission.

WI-347 reveals that analyticity was not the essential hypothesis. Normalize the source carriers `w_U` and outputs `h_U` projectively. Suppose that for each `epsilon>0` there is a radius `rho_epsilon>0`, independent of height, such that

`d_P(w_U,w_V)<=rho_epsilon` implies `d_P(h_U,h_V)<=epsilon`.

For ordinates sampled in a window of width `H` from a log-frequency aperture `Delta`, a projective source ball of radius `rho_epsilon` covers a height interval of length comparable to `rho_epsilon/Delta`. Consequently the output Gram family has spectral-tail effective rank bounded after

`N_epsilon = 1+ceil(H Delta/(2 rho_epsilon))`.

At the natural bow scale `H Delta<=1`, any feature family with a height-uniform projective continuity modulus therefore has bounded effective dimension at fixed tolerance. This statement does not require linearity, polynomial degree, an analytic expansion, a fixed output dimension, or any particular number of channels.

The contrapositive is the useful resource statement. If the construction needs effective rank `r(T)->infinity` while retaining a fixed tail fraction, then its usable source-resolution radius must collapse at least like

`rho=O(H Delta/r(T))`.

For a fixed Hölder law this means the Hölder/Lipschitz constant must grow accordingly. The earlier analytic budget lower bound is one realization of the same phenomenon: extensive rank requires some feature complexity, conditioning or resolution parameter to scale with the problem.

Thus `use nonlinear or nonsmooth features` is not by itself an escape from time--bandwidth compression. A feature map can be arbitrarily complicated in ambient coordinates yet remain information-limited if nearby physical carriers stay nearby in projective output geometry. What matters is whether the map resolves progressively finer differences of the **actual source family** at nonvanishing transmitted scale.

The alternative is to bypass generic feature-rank manufacture altogether through a source-specific arithmetic identity, especially the distinguished signed covariance sought by the bow program. Such an identity need not create many generic height directions if it couples directly to the destination quantity.

**Boundary.** The theorem does not cover families whose projective continuity radius collapses with height, diverging Lipschitz/Hölder constants, vanishing output transmission, growing source aperture, essential sensitivity to global phase, explicitly height-dependent maps, cross-window/cross-scale constructions, or direct signed arithmetic covariance. It is a compression theorem for uniformly resolvable fixed-aperture feature families, not an impossibility theorem for the bow program and not a zero-location result.