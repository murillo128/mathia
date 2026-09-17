# MI-051 — Gaussian readout noise converts analog source information into an SNR cost

**Evidence level:** exact/classical information-theoretic synthesis from [MC-339](../../findings/MC-339-bounded-energy-dephasing-needs-linear-joint-source-information.md), [MC-340](../../findings/MC-340-punctured-source-total-correlation-is-only-constant.md), [MC-341](../../findings/MC-341-low-dimensional-analog-source-capacity-costs-metric-spread.md), [MC-342](../../findings/MC-342-forward-source-regularity-does-not-price-analog-capacity.md), and [MC-343](../../findings/MC-343-gaussian-noise-transcript-capacity.md).

MC-342 shows that a bounded, forward-smooth analog transcript can hide `Theta(R)` source bits in exponentially small separations. That construction defeats any attempt to price source information using range, forward Lipschitz constants or fixed positive-moment source-gradient energies alone. MC-343 identifies the missing operational resource once the transcript is actually read at nonzero precision.

Let `T=Phi(X) in R^d` and let the downstream observation be `Z=T+N` with `N~N(0,sigma^2 I_d)`. If `V_T=E||T-ET||^2`, Gaussian channel capacity gives

`I(X;Z) <= (d/2) log(1+V_T/(d sigma^2)) <= V_T/(2 sigma^2)`.

If `D_T` is the transcript diameter, the same argument gives

`I(X;Z) <= (d/2) log(1+D_T^2/(2d sigma^2)) <= D_T^2/(4 sigma^2)`.

MC-339--MC-340 independently require `L_R=Theta(R)` joint source information for bounded-energy nontrivial dephasing in the reciprocal endpoint model. Therefore any noisy transcript capable of supplying that information must satisfy

`V_T/sigma^2 >= d(exp(2L_R/d)-1)`

and

`D_T/sigma >= sqrt(2d(exp(2L_R/d)-1))`.

For fixed `d` the required signal-to-noise spread is exponential in `R`; for `d=o(R/log R)` it is superpolynomial; without any dimension restriction the variance-to-noise budget is still at least linear in the required information. The dyadic scalar encoder of MC-342 is therefore not a counterexample to a noise-aware capacity obstruction: its entire information content lives below an exponentially fine resolution and is destroyed unless the noise scale shrinks accordingly.

There is also a qualitative endpoint. For a finite source alphabet and every `sigma>0`, distinct Gaussian output laws have overlapping support, so exact source recovery — and hence exact source-determined dephasing through that readout — is impossible. Positive Gaussian noise does not merely make the MC-342 encoder inconvenient; it removes exact decoding while quantitative capacity measures the surviving approximate information.

The reusable lesson is that **inverse precision becomes a mathematical resource only after the observation declares a resolution/noise model**. Forward smoothness does not price analog capacity, but additive noise does: source information must appear as dimension, variance/SNR, diameter/spread or some corresponding distinguishability resource in the actual channel consumed downstream. An architecture that claims robust source use should therefore state its readout model before counting analog coordinates as freely informative.

**Boundary.** MC-343 is a finite-source Gaussian-readout theorem for the reciprocal endpoint information/dephasing problem. It does not prove a Mertens estimate, does not establish that Gaussian noise is the uniquely correct physical metric, and does not forbid noiseless exact-real access by assumption. A different readout model may have a different capacity law, but it must supply an explicit source-natural distinguishability theorem rather than appeal to forward regularity.