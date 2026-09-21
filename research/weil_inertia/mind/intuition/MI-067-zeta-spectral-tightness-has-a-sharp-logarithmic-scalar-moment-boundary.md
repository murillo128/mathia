# MI-067 — Zeta-spectral tightness has a sharp logarithmic scalar-moment boundary

**Evidence level:** exact/classical Fourier-sampling synthesis from [WI-389](../../findings/WI-389-superlog-fourier-moments-force-zeta-spectral-tightness.md), sharpening the high-frequency escape of MI-066 and the adaptive-profile recurrence theorem of WI-387.

For a fixed-width profile `g` with Fourier transform `F_g`, the local density of zeta ordinates is logarithmic. WI-389 turns that density into the exact tail estimate

`sum_(|gamma|>T) |F_g(gamma)|^2`

`<= C_L int_(|xi|>T/2) log(2+|xi|)|F_g(xi)|^2 dxi + C_(L,M) T^(-M)||F_g||_2^2`.

The proof uses only fixed exponential type, a Schwartz reproducing kernel and the classical Riemann--von Mangoldt unit-interval count. No RH input is needed for the sampling estimate itself.

Consequently, uniform integrability of the continuous Fourier energy against `log(2+|xi|)` forces uniform tightness of the zeta-sampled tail. Any uniformly bounded scalar moment with weight `w(r)` satisfying

`log(2+r)/w(r) -> 0`

therefore suffices. In particular every `log^(1+delta)` moment with `delta>0`, and every positive Sobolev moment `H^s` with `s>0`, is already strong enough for the **spectral recurrence** part of WI-387. The earlier uniform `H^1` hypothesis was sufficient but far from sharp for that step.

MI-066/WI-388 shows that logarithmic order is the exact boundary inside this natural one-weight class. A sideband carrying only `epsilon_R=c/log R` of the `L^2` mass has uniformly bounded logarithmic Fourier moment while a suitable frequency packet contains `Omega(log R)` zeta ordinates, leaving `Omega(1)` sampled mass escaping to infinity. The same countermodel works for every weight `w(r)=O(log r)`. Bounded logarithmic moment is therefore not the same as uniform logarithmic integrability.

The reusable mechanism is **sampling-density-weighted compactness**. A continuous Fourier norm controls a discrete destination only after its weight dominates the local density of destination samples strongly enough to make the weighted tails uniformly integrable. Here that density is logarithmic, so superlogarithmic scalar moments close high-frequency escape while logarithmic-order moments can still leak an order-one zeta-sampled tail.

This does not by itself extend the full source-exact recurrence no-go. WI-387 used `H^1` both for spectral tightness and for a uniform transfer showing that the exact source-slot perforation is negligible over the whole adaptive family. WI-389 replaces `H^1` only in the spectral recurrence step. A no-go theorem under merely superlogarithmic Fourier control still needs an independent **uniform source-perforation transfer estimate** at that weaker regularity.

**Boundary.** The log-versus-superlog threshold is sharp only for scalar moment-growth hypotheses over arbitrary fixed-width families. Direct zeta-sampled conditions, arithmetic restrictions, nonlinear compactness criteria or more structured profile classes can behave differently. WI-389 does not prove RH, a positive Weil gap, or the source-perforation estimate needed to replace `H^1` in the full WI-387 theorem.
