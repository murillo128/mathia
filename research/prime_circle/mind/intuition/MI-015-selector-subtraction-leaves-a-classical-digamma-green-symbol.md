# MI-015 — Diffuse one-profile averaging drives the complete absolute spectrum to the classical Green sequence

**Evidence level:** unconditional classicalization from PC-282--PC-285, conditional RH sharpening through [PC-290](../../findings/PC-290-count-matched-l2-transport-reaches-square-root-boundary.md), and unconditional square-root boundary results [PC-291](../../findings/PC-291-microscopic-resonance-band-is-spectrally-invisible-at-square-root-resolution.md)--[PC-295](../../findings/PC-295-diffuse-boundary-log-spectrum-converges-to-green-sequence.md). PC-295 treats diffuse source averaging and the complete absolute ordered singular spectrum; it does not control phase-sensitive, nonnormal, multi-profile or non-diffuse observables.

After selector subtraction, the complete-domain remainder is a classical logarithmic/digamma Green symbol. Prime dependence in this branch survives only through source placement inside the finite section. PC-285 reproduces that placement with a matched Li-grid control through the unconditional Vinogradov--Korobov range, while PC-287--PC-290 show under RH that the normalized one-profile singular-spectrum laws collapse for every `B=o(sqrt(q))` once total source count is matched.

PC-291--PC-294 separate microscopic relation onset, worst-case local amplitude, source-averaged local amplitude and total spectral mass. At `N~sqrt(q)`, a fixed source pair can already have an order-one local Hankel band, yet every local band is negligible after diffuse source averaging and the full Hilbert--Schmidt mass is source-universal with limit `pi^2/12`.

PC-295 closes the spectral-redistribution escape. Let `beta_q=||mu_q||_infty`. If

`N->infinity`, `(log q)^2 sqrt(q beta_q/N) -> 0`,

then the ordered singular-value vector of the normalized boundary-log matrix converges in expected `ell^infinity` distance to

`s^(N)=(1/2,1/2,1/4,1/4,1/6,1/6,...)`

truncated after `N` entries. This is exactly the singular spectrum of the classical mean-zero logarithmic Green/single-layer operator on the circle with Fourier multiplier `-1/(2|m|)`.

The mechanism has two parts. Diffuse source dilations make every fixed finite set of Fourier mode vectors asymptotically orthonormal, so the low-mode singular values converge to the absolute Fourier multipliers. The remaining Fourier tail has universally vanishing operator norm after source averaging; its Hilbert--Schmidt mass converges to the tail `1/2 sum_(m>M)m^-2`, which vanishes as the fixed mode cutoff is sent to infinity. Thus the earlier `pi^2/12` mass identity was the total Green mass, not a reservoir for hidden prime-specific spectral redistribution.

For prime-scale diffuse sources, `beta_q=O(log q/q)`, the condition follows from `N/(log q)^5->infinity` and therefore includes the square-root scale `N~sqrt(q)`. Both the prime source and count-matched Li-grid control lie in this class. Consequently every continuous statistic of the complete absolute ordered singular vector has the same deterministic limit in this regime; higher absolute moments, edge values and small-singular-value statistics cannot restore prime specificity simply by reprocessing the same one-profile spectrum.

The surviving information must sit before or outside absolute singular-value compression: orientation/phase, signed or nonnormal structure, joint spectra of several source profiles, cross-level coupling, an exceptional non-diffuse source regime, or another relational observable not determined by `Sigma(K/N)`. This is a stronger representation boundary than Hilbert--Schmidt universality: the whole absolute one-profile spectral shape classicalizes.

**Boundary.** The theorem is averaged over independent source draws and assumes diffuseness at the stated rate. Fixed exceptional pairs, highly atomic source laws, phase-sensitive observables, singular vectors/eigenvectors, and multi-profile joint data remain outside it. It does not show that every richer representation is useful; it shows that the complete absolute one-profile singular spectrum is no longer a viable averaged arithmetic carrier at square-root resolution.