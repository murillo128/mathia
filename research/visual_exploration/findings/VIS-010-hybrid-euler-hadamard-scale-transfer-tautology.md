# VIS-010 — Hybrid Euler–Hadamard scale transfer has a quotient tautology

## Claim

Gonek, Hughes, and Keating give an unconditional smoothed hybrid representation of the Riemann zeta function in which a scale parameter `X` splits the same value of `zeta(s)` between a finite prime factor and a local zero factor. In their Theorem 1, for `s = sigma + i t` with `sigma >= 0`, `|t| >= 2`, and suitable smoothing,

`zeta(s) = P_X(s) Z_X(s) (1 + explicit error)`,

where

`P_X(s) = exp(sum_{n <= X} Lambda(n)/(n^s log n))`

and `Z_X(s)` is a smoothed exponential product over nontrivial zeros. The useful approximation regime is intermediate: increasing `X` moves descriptive burden from the zero factor toward the prime factor, while the theorem records the approximation error explicitly.

This gives a mathematically justified baseline for prime-scale visual recursion in the critical strip, but it also exposes an exact visual trap. If one defines the finite residual directly by

`R_X(s) = zeta(s) / P_X(s)`,

then away from zeros, for any two cutoffs `X < Y`,

`R_Y(s) / R_X(s) = P_X(s) / P_Y(s)`.

Hence

`log|R_Y(s)| - log|R_X(s)| = -(log|P_Y(s)| - log|P_X(s)|)`.

Any apparent scale-by-scale "transfer", anticorrelation, or conservation between `P_X` and the quotient residual `zeta/P_X` is therefore algebraically forced. It is not evidence of a new prime/zero coupling.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL-BASELINE + NEGATIVE/OBSTRUCTION`.

The hybrid representation is prior art. The quotient identity is elementary. The research value is a visual falsification rule: a recursive prime/zero picture must beat the exact complementarity built into the decomposition before its geometry can be interpreted as additional structure.

## Derivation

The hybrid formula supplies a legitimate scale parameter in a region where an ordinary convergent Euler product is unavailable. Its prime factor is not an arbitrary prime ordering but the exponential of the finite von-Mangoldt sum through `X`; its complementary factor is built from zeros through the same scale.

For the exact finite quotient residual `R_X = zeta/P_X`, no approximation is needed. Since `P_X(s)` is an exponential, it is nonzero. At every point where `zeta(s) != 0`,

`R_Y/R_X = (zeta/P_Y)/(zeta/P_X) = P_X/P_Y`.

Taking absolute values and logarithms gives the stated increment identity. The corresponding phase increments are also opposite modulo the usual branch ambiguity:

`arg R_Y - arg R_X = -(arg P_Y - arg P_X) mod 2 pi`.

Thus a two-channel animation that defines one channel as the exact residual of the other will necessarily look like information is being transferred between them as `X` changes. That visual behavior contains no more mathematics than the quotient definition.

GHK's independently defined `Z_X`, by contrast, is not introduced as the exact quotient. The informative quantity is therefore the comparison between the independently constructed prime and zero factors together with the theorem's error, not the tautological comparison between `P_X` and `zeta/P_X`.

## Relevance to visual exploration

The existing clue on prime-phase recursive geometry asked for a mathematically justified hierarchy that can be continued toward the critical strip without pretending that the ordinary Euler product converges there. The hybrid Euler–Hadamard formula supplies exactly such a baseline: `X` is a genuine prime/zero resolution parameter, and the prime and zero factors are defined from their respective arithmetic/spectral data.

It also narrows what would count as a visual discovery. A plot in which prime contribution grows while the quotient residual shrinks, or their log-modulus increments mirror each other, is guaranteed. A useful visualization must instead expose a statistic of the independently defined `P_X` and `Z_X`, or of the hybrid approximation error, that is not fixed by the product identity.

## Prior art and novelty assessment

S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136 (2007), 507–549, DOI `10.1215/S0012-7094-07-13634-2`, prove the smoothed prime/zero representation and emphasize that `X` mediates between the truncated prime and zero descriptions. Their theorem is unconditional, while the usefulness of particular asymptotic regimes depends on the stated error terms.

S. M. Gonek, **Finite Euler products and the Riemann hypothesis**, *Transactions of the American Mathematical Society* 364 (2012), 2157–2191, DOI `10.1090/S0002-9947-2011-05546-7`, studies short Euler-product approximations in the critical strip and further delineates when finite prime products can meaningfully approximate zeta.

No novelty is claimed for either representation or for the quotient algebra. The Mathia-specific contribution is the explicit visual-control consequence: exact prime/residual complementarity must be removed before interpreting recursive scale transfer as structure.

## Boundary conditions and failure modes

The GHK theorem does not say that a raw infinite Euler product converges in the critical strip, and it does not license arbitrary prime ordering or unsmoothed truncation as a canonical limit there. The explicit error matters; the paper itself notes that both prime and zero contributions are needed in an intermediate regime if the approximation is to be informative.

The exact quotient increment identity is stated away from zeros so that ratios and logarithms are ordinary finite quantities. Near a zero, one should use a regularized local comparison or the independently constructed `Z_X` rather than divide two vanishing residuals.

A nontrivial cross-scale statistic is not ruled out. The obstruction applies only to statistics determined by the exact complementary factorization `R_X = zeta/P_X`. Geometry of the independently defined zero factor, hybrid approximation error, zero-localization window, prime-band phase organization, or matched-control response may still contain information not forced by this identity.

## Audit criterion

For any proposed prime-scale visualization near the critical strip, first ask whether one plotted channel is defined as the exact quotient of `zeta` by the other. If so, compute the same statistic after replacing the data by an arbitrary nonzero reference function `F(s)` and setting `R_X = F/P_X`. Any scale-transfer feature implied solely by

`R_Y/R_X = P_X/P_Y`

is universal and must be subtracted from the claim.

A surviving candidate should instead use the independently specified hybrid objects — or another representation with its own source definitions — and identify a quantitative statistic not determined by their product relation.

## Consequence for the research line

The prime-phase recursive-geometry direction remains viable, but its first canonical baseline is now fixed by prior art. Future visual work should use the hybrid Euler–Hadamard decomposition or an equally justified prime/zero scale split, and it should not count exact prime-versus-residual anticorrelation as a discovery. The live question is whether an independently defined cross-scale statistic survives the hybrid error analysis, smoothing/grouping changes, and matched prime/zero controls.