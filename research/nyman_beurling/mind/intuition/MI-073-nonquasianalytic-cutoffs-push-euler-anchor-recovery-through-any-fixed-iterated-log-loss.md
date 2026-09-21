# MI-073 — Nonquasianalytic reconstruction pushes Euler-anchor recovery through any fixed iterated-log loss

**Evidence level:** exact Fourier-reconstruction synthesis from [NB-266](../../findings/NB-266-infinite-convolution-cutoffs-push-ford-mesh-coercivity-through-iterated-log-losses.md), extending NB-264--NB-265. The infinite-convolution cutoff construction and Fourier tail estimates are classical analytic ingredients; the line-specific content is their use in the exact rank-coupled Ford reconstruction.

The Euler normalization `sum c_j=1` can be reconstructed exactly from the carrier-locked shallow Ford samples with a compact `C^infinity` plateau. By choosing an infinite-convolution cutoff whose transform decays like

`exp(-c |xi|/L_(r,epsilon)(|xi|))`,

NB-266 localizes the required response to

`B_K = C_(r,epsilon) log K L_(r,epsilon)(log K)`,

where `L_(r,epsilon)` is any fixed finite hierarchy of iterated logarithms ending with exponent `1+epsilon`. For every fixed `delta>0`, this is `o((log K)^(1+delta))`.

The same exact reconstruction still forces both a nonvanishing sample and aggregate `Omega(m)` carrier response inside that radius. Thus the gap left by the Gevrey argument is not a generic near-logarithmic region: bounded resolved `ell^2` cost already prevents suppression through every fixed finite iterated-log enlargement of `log K`.

The pure `O(log K)` endpoint remains genuinely separate. NB-266 does not obtain exponential Fourier decay from a compact plateau and does not prove that every possible exact reconstruction must pay an iterated-log loss. The next scalar question is therefore whether the endpoint can be reached by another reconstruction/duality mechanism, or whether a matching lower obstruction forces some slowly varying loss.

**Boundary.** The result retains the bounded resolved carrier-cost hypothesis and remains a matched Ford-interface statement. It does not assert actual zeta-zero locations, does not control growing total variation or conditioning for free, and does not replace the final Hardy/Nyman projection by the matched compatibility estimate.