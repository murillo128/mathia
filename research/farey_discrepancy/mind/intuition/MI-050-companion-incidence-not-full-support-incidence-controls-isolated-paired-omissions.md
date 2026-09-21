# MI-050 — Companion incidence, not full support incidence, controls isolated paired omissions

**Evidence level:** exact paired-coefficient synthesis from [FD-253](../../findings/FD-253-companion-incidence-controls-paired-exact-omission-conditioning.md), refining the support-only separation in [FD-252](../../findings/FD-252-parity-dilation-embeds-arbitrary-divisor-conditioning-into-exact-omission-supports.md).

For isolated omissions `E`, the response increment is not a free vector on `E union (E+1)`. Writing `g=Delta Y=mu*b`, each omitted start `e` produces the exact pair

`g(e)=Y(e)`, `g(e+1)=-Y(e)`.

Let `C=E+1`. If no omitted start divides any companion location, `e' not| e+1` for all `e,e' in E`, then the coefficient rows indexed by `C` close on the companion coordinates alone. The weighted incidence inverse therefore gives

`sum_(d<=H) |g(d)|/d <= (2+1/e_min) C_b |E| kappa(C)`,

and hence

`sum_(n<=H) |b_n| <= (2+1/e_min) C_b H |E| kappa(C)`.

This can be radically smaller than the free-support norm. For every finite divisor set `D subset [1,M]`, choose `L>M`, set `E=LD` and `C=LD+1`. Then `C` is a divisibility antichain, so `kappa(C)=1`, while the full support `LD union (LD+1)` preserves every induced divisibility interval on the core `LD` and therefore has `kappa(LD union (LD+1)) >= kappa(D)`. Thus arbitrarily bad support conditioning can coexist with uniformly linear paired exact-omission conditioning.

The remaining paired obstruction is consequently more specific than a large Möbius row somewhere in the active support. A genuinely bad isolated family must make the companion subsystem itself ill-conditioned, or allow start coordinates to feed companion rows so that the private-sensor closure fails. For pure dilations `E=LD` the latter mechanism is absent, leaving the concrete simultaneous-conditioning question for `D` and `LD+1`.

**Boundary.** FD-253 is response-side and signed. It does not prove a universal improved exponent for arbitrary exact omissions, does not handle touching omissions by the same closed-companion argument, and does not supply positivity, finite prime-reservoir capacity, squarefree source realization or full arithmetic coherence.