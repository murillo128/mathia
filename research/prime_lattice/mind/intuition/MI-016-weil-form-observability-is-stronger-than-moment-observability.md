# MI-016 — The sharp ambient Weil modulus is an escaping-wave-packet obstruction, not the modulus of a compact simple ground branch

**Evidence level:** proved for the fixed-domain logarithmic form geometry through PL-287, conditional on the PL-283--PL-284 finite spectral certificate at `a=0.8`; completed arithmetic positivity and a quantitative transport radius remain open.

PL-278--PL-282 show that the negative Morse index is a one-sided ledger under aperture growth and that any fixed positive window can in principle be certified finitely. PL-283--PL-284 provide one concrete positive base point, conditional on an external interval-arithmetic certificate: at `a=0.8` the localized Weil operator has a simple even ground state and a tiny explicit positive margin.

PL-285 shows why this cannot be propagated by ordinary bounded-operator perturbation. On Suzuki's fixed interval, active arithmetic channels are compressed translations. Ambient `L^2` operator norm is discontinuous; on the canonical logarithmic form domain the generic quadratic-form modulus is sharply `Theta(1/log(1/|delta|))`. PL-286 shows that summing the complete active `2,3,4` von-Mangoldt comb does not improve this worst-case rate.

PL-287 identifies what the sharp witnesses are doing: they depend on `delta` and push Fourier mass to frequency `~1/delta`. For every fixed `w in H^log`, and uniformly for every compact `K subset H^log`, the translation quadratic forms instead satisfy

`sup_(w in K)|q_(h+delta)(w)-q_h(w)| = o(1/log(1/|delta|))`.

Compactness gives uniform tightness of the logarithmically weighted Fourier tails, which excludes precisely the escaping wave packets that saturate PL-285--PL-286.

At the conditionally certified simple ground state, common-domain form continuity and spectral isolation allow the normalized eigenvector to be chosen as an `H^log`-continuous branch on a sufficiently small source-static neighborhood. Its image on a closed subneighborhood is compact, so the actual ground eigenvalue obeys the same strict little-o improvement. Thus the sharp inverse-log barrier is an **ambient state-space obstruction**, not the asymptotic modulus of the isolated ground branch itself.

The missing resource is now quantitative rather than qualitative. To transport the tiny positive margin to a useful aperture, one needs an explicit uniform tail function for the ground branch, stronger branch regularity with constants, or an eigen-equation/source identity that bounds how rapidly Fourier mass can migrate. Merely proving continuity or invoking the generic `H^log` modulus is no longer enough.

**Boundary.** PL-287 gives no computable neighborhood size, no rate inside the little-o, and no positivity transport to the next source activation. The endpoint certificate remains conditional. The result only proves that a compact actual branch cannot realize the moving high-frequency witnesses responsible for the worst-case ambient modulus.
