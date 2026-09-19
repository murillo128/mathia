# MI-040 — Wang's finite-height transfer has a cutoff-free dyadic-shell route with only a logarithmic gap

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-313](../../findings/VIS-313-wang-dyadic-ratio-shell-linear-horizon.md), using Wang's displayed localization/mean-value identities, the classical Montgomery--Vaughan Hilbert inequality and the matched support/phase controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-304 then move the upper obstruction from localization leakage to the actual prime-power coefficient/frequency geometry, obtaining the absolute bound `x log log x=o(H)`.

VIS-305--VIS-308 successively preserve density, parity, exact prime-power support, coefficient magnitudes and finally all same-base multiplicative harmonic relations while randomizing cross-prime phase. Each matched control has signed remainder far below `H` at `H~x log log x`. Same-base multiplicative coherence is therefore not enough.

VIS-309 tests the actual deterministic common-time orbit `p -> p^(-it)`. For fixed `x,H`, rational independence of prime logarithms makes its Bohr quadratic mean exactly the completely multiplicative Haar mean. The resulting second moment is `O(x log^3(3x))`, so large signed remainders have vanishing long-time density at the candidate boundary. Generic deterministic cross-prime alignment is not the missing mechanism either.

VIS-310 asks how cheaply that Bohr cancellation can be transported to a finite height window. Hard truncation plus one global minimum gap gives only a quintic sufficient horizon. VIS-311 preserves local geometry of the retained finite spectrum and lowers it to the cubic scale

`V >> x^3 log^3 x/(log log x)^2`.

VIS-312 then shows that this nearest-neighbour representation has no cutoff-free continuation: the full supported cross-base ratio spectrum is dense, so every fixed retained frequency loses individual isolation as the support grows. The failure is in the representation, not a lower bound on true dephasing.

VIS-313 supplies the first cutoff-free aggregate replacement. Split the spectrum at the fixed ratio boundary `|lambda|=log 2`. The far band is pointwise `O(x)` because the positive coefficient mass is `O(sqrt(x))`, hence it is already `o(H)` at `H~x log log x`. Inside the strict near band, same-base prime powers are absent, so each frequency comes from a unique reduced ratio of distinct prime-power bases.

Now group near frequencies by dyadic arithmetic height `M<max(q,r)<=2M`. Two distinct reduced ratios in one shell have logarithmic separation `delta_M >> M^(-2)`, while the inherited Wang taper gives shell energy

`E_M << M v_x(M)^4 log^3(4M)`.

Applying Montgomery--Vaughan shellwise and summing the resulting `L^2` norms by Minkowski yields the cutoff-free estimate

`V^(-1) int |R_near(T)|^2 dT << x log^3 x + x^3 log^3 x / V`,

and after restoring the far band,

`V^(-1) int |R(T)|^2 dT << x^2 + x log^3 x + x^3 log^3 x / V`.

At `H~x log log x`, the deterministic finite-window mean square is therefore `o(H^2)` whenever

`V >> x log^3 x/(log log x)^2`.

This removes the polynomial gap created by hard-cutoff pointwise spacing. Dense support is compatible with useful finite-height control once frequencies are aggregated before inversion; the relevant currency is **scale-local separation plus summable coefficient energy**, not an isolation radius attached to each frequency in the infinite spectrum.

The unresolved gap is now logarithmic. The natural local window is `V~H~x log log x`, whereas the current sufficient horizon is larger by roughly `log^3 x/(log log x)^3`. A further advance must reduce shell-energy/large-sieve logarithms, exploit cancellation between shells, sharpen the signed far band in a way that affects the dominant logarithmic term, or exhibit a genuine exceptional-height packet that proves some loss unavoidable. Another hard support cutoff or unpartitioned nearest-neighbour functional is no longer informative.

**Boundary.** VIS-313 is a sufficient mean-square-in-starting-height estimate. It does not prove pointwise cancellation for every `T`, justify a moving `x(T)` inside the averaging integral without a joint-limit argument, or show that the remaining logarithmic gap is intrinsic. The shell argument depends on the VIS-307 energy profile, unique reduced cross-base ratios in `|lambda|<log 2`, and the classical separated-frequency mean-value inequality.
