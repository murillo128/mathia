# MI-015 — Selector-subtracted one-profile spectra are classically reproducible nearly to square-root scale

**Evidence level:** unconditional classicalization from PC-282--[PC-285](../../findings/PC-285-boundary-log-spectra-classicalize-through-vinogradov-korobov-scale.md), and conditional RH sharpening from PC-286--[PC-288](../../findings/PC-288-koksma-path-variation-pushes-rh-boundary-log-collapse-to-log-five-halves.md). No converse RH criterion is claimed, and no theorem is claimed for richer observables outside the normalized one-profile singular-spectrum law.

After selector subtraction, the complete-domain remainder is a classical logarithmic/digamma Green symbol. The only surviving prime dependence in this branch is source placement inside its finite section. PC-285 shows that placement is already reproducible by the matched Li-grid control through the unconditional Vinogradov--Korobov range.

Under RH, PC-287 pushed the same exact boundary-log statistic to `B=o(sqrt(q)/(log q)^3)` by flat clipping and by charging the singular arc in `L^2` rather than at its worst value. PC-288 removes another artificial loss. For a one-Lipschitz test of the ordered clipped singular spectrum, the path obtained by varying one source coordinate has total variation

`O(B/sqrt(epsilon))`,

because the squared derivative of the clipped log-sine profile integrates to `O(1/epsilon)`. One-dimensional Koksma/Stieltjes integration therefore transports prime to Li through the Kolmogorov discrepancy `Delta_q`, giving

`W_1 << sqrt(epsilon log q + (log q)^3/q) + (B/sqrt(epsilon)) Delta_q + (log q)^2/q`.

RH supplies `Delta_q << q^(-1/2)(log q)^2 + (log q)/q`. Balancing the first two terms yields

`epsilon = B q^(-1/2)(log q)^(3/2)`

and forces the complete normalized spectral law to the Li-grid law whenever

`B=o(sqrt(q)/(log q)^(5/2))`.

The reusable point is not the numerical `5/2` alone. **Integrated output-path variation can be a strictly cheaper transport currency than a global input Lipschitz constant when the source is one-dimensional before productization.** Here it removes a half-logarithmic loss without changing the matrix, clipping, control law or output observable.

The logical direction remains essential. RH makes this particular prime-specific distinction disappear. An order-one separation in the proven range would be anti-RH evidence for this architecture, while convergence itself is not a converse criterion. The remaining question is whether the last polylogarithmic neighborhood of the square-root denominator scale can be removed by an even sharper matched transport, or whether a useful RH mechanism must retain information that one ordered singular-spectrum vector discards.

**Boundary.** PC-288 still uses RH prime-counting input and the exact one-profile finite section. It says nothing about multi-source/cross-level observables, non-spectral phase information, or statistics designed to magnify a vanishing residual with a separately justified normalization.
