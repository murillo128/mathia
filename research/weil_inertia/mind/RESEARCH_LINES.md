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

The live fixed-width no-go question is now precise: can exact source-slot perforation be transferred **uniformly** under a condition as weak as superlogarithmic Fourier compactness? WI-389 supplies the recurrence-side tail theorem but not that source-transfer estimate. If such a transfer holds, the no-go extends far below `H^1`; if it fails, the failure must identify a source-sensitive roughness mechanism rather than merely high-frequency spectral escape.

A positive route remains harder: it must violate the compactness condition in a source-admissible way and also control the endpoint factors `sin^2(gamma A_k/2)` strongly enough to prevent recurrent near-zero returns. WI-388 establishes spectral escape, not a phase-stable positive floor.

Growing width, multiscale/nonlocal structure, semidefinite use or an exact graph/domain restriction remain separate geometry changes.

## Keep inherited core inertia, source restriction, sampling density and elimination category distinct

The fixed-width quasimodes are robust to arbitrary profile retuning inside uniformly zeta-spectrally tight families. WI-388 shows that gamma negativity and exact source slots do not imply that tightness; WI-389 shows that the natural scalar compactness threshold is set by the logarithmic local density of zeta ordinates.

Future claims must therefore state which resource changes: continuous Fourier tail control, zeta-sampled tightness, uniform source-perforation transfer, endpoint phase control, width, locality, domain or operator category. A bounded logarithmic moment is not compactness; a superlogarithmic moment controls recurrence but does not automatically control the source-hole perturbation; destroying tightness removes one obstruction but does not create coercivity.
