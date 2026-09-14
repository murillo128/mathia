# MI-015 — Selector subtraction and subcritical finite sections are classically reproducible

**Evidence level:** proved unconditionally by PC-282--[PC-285](../../findings/PC-285-boundary-log-spectra-classicalize-through-vinogradov-korobov-scale.md) for the radial logarithmic one-profile branch, and sharpened conditionally under RH by [PC-287](../../findings/PC-287-flat-clipping-pushes-rh-boundary-log-collapse-to-log-cubed-gap.md). No converse RH criterion is claimed, and no theorem is claimed for richer observables outside the normalized singular-spectrum law.

PC-282 separates the divergent boundary anchor from the finite-section operator: after normalization, the boundary-first regime collapses to the exact modular collision selector. PC-283 classifies the selector-subtracted complete-domain remainder. Its nonconstant Fourier multipliers are strictly negative, its finite-`q` spectrum is explicit through the digamma function, and its low-mode large-`q` limit is the classical logarithmic Green kernel.

PC-284 closes the first attempt to recover arithmetic information from source-dependent finite-section placement of that exact logarithmic remainder. The singularity can be clipped on a microscopic residue set while keeping the anchor exact, and the resulting profile is regular enough for prime-to-Li transport. PC-285 then pushes the unconditional matched-control reproduction to the Vinogradov--Korobov source-transport range.

PC-287 shows that, **assuming RH**, the same exact one-profile statistic classicalizes much farther. Flat value clipping keeps the source-independent collision anchor exact but makes the source-dependent profile only `O(1/epsilon)`-Lipschitz. More importantly, the exceptional logarithmic arc is charged by its actual square-summable depth,

`sum_t |delta_(q,epsilon)(t)|^2 << epsilon q + (log q)^2`,

rather than by its worst `O(log q)` value at every exceptional residue. If `D_q` is the prime-to-Li source Wasserstein distance, this gives

`W_1 << sqrt(epsilon log q + (log q)^3/q) + (B/epsilon)D_q + (log q)^2/q`.

Under RH, `D_q << q^(-1/2)(log q)^2+q^(-1)`. Optimizing `epsilon` therefore forces the complete normalized singular-spectrum law on prime pairs to converge to the denominator-`q` Li-grid law whenever

`B=o(sqrt(q)/(log q)^3)`.

The important separation is logical. The complete-domain symbol is classical, and **RH itself suppresses the prime-versus-Li distinction of this one-profile finite-section spectrum nearly up to the rational square-root scale**. Persistent order-one separation in the PC-287 range would contradict RH rather than support it; collapse is only a one-way RH consequence and does not imply RH.

The surviving one-profile frontier is therefore the remaining polylogarithmic neighborhood of the denominator-microscopic transition, or a different RH signature than an order-one prime/Li separation. The exponent `3` is the loss of this clipping-and-transport proof, not an intrinsic arithmetic threshold. Otherwise the architecture must enrich the observable through cross-level, multi-source, directional, noncommuting or information-preserving structure not compressed to one ordered singular-value vector.

**Boundary.** The unconditional and RH-conditional ranges are different claims. PC-287 imports the RH source estimate and therefore cannot upgrade PC-285 unconditionally. It also does not cover observables that magnify a vanishing residual, couple several levels/sources before taking spectra, or retain non-spectral phase/directional information.