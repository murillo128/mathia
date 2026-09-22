# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond spectrally tight fixed-width source-zero coercivity

**Linked intuitions:** `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing` through `MI-064-fixed-width-source-zero-weil-trials-saturate-the-zero-coercivity-floor`, `MI-065-fixed-width-profile-freedom-cannot-open-a-weil-coercive-gap`, `MI-066-dilute-high-frequency-sidebands-separate-gamma-margin-from-spectral-tightness`, `MI-067-zeta-spectral-tightness-has-a-sharp-logarithmic-scalar-moment-boundary`.

WI-369--WI-386 reduce the fixed-width source-zero family to a recurrent nonnegative spectral energy under RH and show that changing any one fixed profile cannot open a uniform positive Weil gap once exact source-slot perforation and the full explicit-formula ledger are retained.

WI-387 extends that obstruction to arbitrary endpoint-dependent profiles whose zeta-frequency spectra are uniformly tight. A uniform fixed-width `H^1` bound is one sufficient hypothesis: finite-frequency recurrence is coefficient-independent, the high-frequency sampled tail is uniformly negligible, and the exact source-hole transfer remains uniformly `o(1)`.

WI-388 shows that a strict negative archimedean margin plus exact source slots does not imply that compactness. A carrier at frequency `R` costs only `O(log R)` in the gamma difference form; placing `c/log R` of the `L^2` mass there preserves the negative margin while a packet containing `Omega(log R)` zero ordinates retains `Omega(1)` sampled energy at frequencies tending to infinity.

WI-389 identifies the exact scalar-moment boundary behind that escape. Fixed support gives

`sum_(|gamma|>T)|F_g(gamma)|^2`

`<= C int_(|xi|>T/2) log(2+|xi|)|F_g(xi)|^2 dxi + O(T^(-M))`.

Thus uniform integrability against the logarithmic sampling density implies zeta-spectral tightness. Any bounded Fourier moment with superlogarithmic weight—`log^(1+delta)` for any `delta>0`, or `H^s` for any `s>0`—is sufficient for the spectral-recurrence half of WI-387. The WI-388 family shows that a bounded logarithmic-order moment is insufficient in general.

WI-390 supplies the missing source-transfer half at that same logarithmic compactness scale. If the logarithmically weighted Fourier tails are uniformly integrable, perforating a fixed-width trial to create exact prime-power source slots changes both its `L^2` norm and the logarithmic difference-form energy by `o(1)`. The estimate survives the exact source holes rather than merely the unperforated spectral model. Combined with WI-389, this extends the fixed-width recurrence/no-gap mechanism from `H^1` families to the sharp logarithmic-tail compact class; in particular every uniformly superlogarithmic moment-bounded family lies inside the no-go.

The positive fixed-width route is now correspondingly sharper. It must **fail uniform logarithmic Fourier-tail integrability in a source-admissible way** and also control the endpoint factors `sin^2(gamma A_k/2)` strongly enough to prevent recurrent near-zero returns. Merely leaving `H^1`, adding exact source perforations, or keeping a bounded logarithmic-order moment does not provide such a mechanism. WI-388 establishes spectral escape, not a phase-stable positive floor.

Growing width, multiscale/nonlocal structure, semidefinite use or an exact graph/domain restriction remain separate geometry changes.

## Keep inherited core inertia, source restriction, sampling density and elimination category distinct

The fixed-width quasimodes are robust to arbitrary profile retuning inside families with uniformly integrable logarithmic Fourier tails. WI-388 shows that gamma negativity and exact source slots do not imply that compactness; WI-389 identifies the sampling-density threshold; WI-390 shows that exact source perforation preserves the obstruction once that threshold is actually met.

Future claims must therefore state which resource changes: continuous Fourier-tail compactness, zeta-sampled tightness, exact source-perforation stability, endpoint phase control, width, locality, domain or operator category. A bounded logarithmic moment is not uniform logarithmic-tail integrability; a superlogarithmic moment supplies the latter and is now covered on both the recurrence and source-transfer sides. Destroying compactness removes one obstruction but does not create coercivity.
