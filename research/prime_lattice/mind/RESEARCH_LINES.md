# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Derive source-structured completed-Weil BV/derivative-measure compactness from the actual eigen-equation

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`, `MI-017-fixed-order-shift-differentiability-survives-without-uniform-half-sobolev-control`.

PL-280--PL-296 separate source-static all-log transport, the universal zero-exterior boundary obstruction, the source-specific sign problem and the failure of an explicit Volterra shortcut. PL-297 shows that the renormalized fractional Hadamard boundary stress can stay finite while the zero extensions diverge in `H^(1/2)`, so the critical Fourier moment is not the correct uniform currency.

PL-298 proves that every fixed positive-order fractional state has enough physical-space regularity for `C^1` translation autocorrelations. PL-299 resolves the singular limit for the pure principal fractional/logarithmic branch: uniform convergence plus symmetry/monotonicity gives a uniform BV bound, and a BV convolution lemma yields `C_s -> C_0 in C^1(R)` even though `||u_s||_(H^(1/2)) -> infinity`.

PL-300 shows that generic spectral stability does not transport this mechanism: norm-small rank-two perturbations can preserve a simple isolated branch and uniform state convergence while making variation and a fixed-lag shift derivative diverge.

PL-301 checks the **actual Suzuki remainder** against that failure mode. Each active prime-power compressed translation is total-variation nonexpansive, while the archimedean completion maps `L^1` uniformly into `BV` on compact aperture ranges. The rough high-frequency injection used by PL-300 therefore cannot hide inside the exact lower-order remainder.

PL-302 closes the simplest contraction escape. The arithmetic shift comb itself is a strict `BV_0` contraction only through `a<=log(3)/2`; as soon as the `n=3` channel is genuinely active, endpoint localization gives an operator-norm lower bound above one. At the working `a=0.8` target, no sharpening of a **shift-comb-only** BV or `L^1` norm estimate can close the branch.

PL-303 now closes the ordinary gap/resolvent escape for the exact operator. Although the odd sector at `a=0.8` is spectrally separated from the even ground level, its resolvent is not bounded `L^2_odd -> BV_0`: high-frequency odd packets cost only `O(log K)` in completed-Weil graph norm while their variation is `asymp K`. Therefore an `L^2` bound on a differentiated forcing plus the certified odd gap cannot produce the uniform derivative-measure control required by PL-299.

The live theorem is therefore a genuinely **source-structured coupled eigen-equation estimate**. It must show that the actual commutator/derivative forcing lies in a smaller class on which high-frequency packets are excluded, or prove coercivity directly in a BV/finite-measure/linear-frequency-sensitive norm. Source-channel cancellation, a stronger forcing-space resolvent, or a direct derivative-measure identity remain viable; generic Kato theory, standalone shift contractivity and `spectral gap + L2 forcing` are closed.

## Keep the source-specific sign theorem separate

PL-294--PL-295 still show that ordinary Beurling--Deny positivity ends before the first prime translation and that ambient `H^log`/subcritical Sobolev closeness does not protect the sign of the selected ground state. PL-299 is an analytic compactness theorem on a positive monotone control branch; PL-300 shows that BV is not generically perturbation-stable; PL-301--PL-302 show that the actual remainder is BV-bounded but not shift-contracting in the relevant aperture; PL-303 shows that the exact odd spectral gap does not upgrade ordinary `L^2` forcing into BV smoothing. None transfers order structure to the arithmetic perturbation.

The sign gate therefore continues to require an arithmetic mechanism from the actual rational-prime eigen-equation: a boundary-weighted lower law, source-specific oscillation/maximum principle, absolute-value defect identity or another order structure unavailable to matched generic operators.

## Keep boundary stress, Hilbert-space stability, BV transport, forcing-space coercivity and order structure distinct

PL-297 separates stress from the half-Sobolev moment. PL-298 supplies fixed-order physical-space variation. PL-299 shows that uniform BV plus uniform state convergence is enough for the pure singular limit. PL-300 proves spectral stability does not imply BV. PL-301 proves the exact remainder transports/smooths BV rather than injecting arbitrary high-frequency variation. PL-302 proves that this boundedness does not become a standalone contraction after the 3-channel activation. PL-303 proves that even a genuine odd spectral gap does not make the logarithmic resolvent an `L^2 -> BV` smoother. None of these resources implies cone membership. Future arguments must identify the **source-specific forcing geometry or non-Hilbert coercivity** that controls derivative measures on the actual ground branch.
