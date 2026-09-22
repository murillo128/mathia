# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond spectrally tight fixed-width source-zero coercivity

**Linked intuitions:** `MI-050-full-localized-weil-energy-turns-any-rh-failure-into-a-finite-radius-first-crossing` through `MI-064-fixed-width-source-zero-weil-trials-saturate-the-zero-coercivity-floor`, `MI-065-fixed-width-profile-freedom-cannot-open-a-weil-coercive-gap`, `MI-066-dilute-high-frequency-sidebands-separate-gamma-margin-from-spectral-tightness`, `MI-067-zeta-spectral-tightness-has-a-sharp-logarithmic-scalar-moment-boundary`, `MI-068-escaping-logarithmic-spectral-compactness-can-open-a-positive-rh-weil-floor`, `MI-069-dilute-carrier-floors-are-collective-and-sparse-defect-blind`.

WI-369--WI-386 reduce the fixed-width source-zero family to a recurrent nonnegative spectral energy under RH and show that changing any one fixed profile cannot open a uniform positive Weil gap once exact source-slot perforation and the full explicit-formula ledger are retained.

WI-387 extends that obstruction to arbitrary endpoint-dependent profiles whose zeta-frequency spectra are uniformly tight. A uniform fixed-width `H^1` bound is one sufficient hypothesis: finite-frequency recurrence is coefficient-independent, the high-frequency sampled tail is uniformly negligible, and the exact source-hole transfer remains uniformly `o(1)`.

WI-388 shows that a strict negative archimedean margin plus exact source slots does not imply that compactness. A carrier at frequency `R` costs only `O(log R)` in the gamma difference form; placing `c/log R` of the `L^2` mass there preserves the negative margin while a packet containing `Omega(log R)` zero ordinates retains `Omega(1)` sampled energy at frequencies tending to infinity.

WI-389 identifies the exact scalar-moment boundary behind that escape. Fixed support gives a logarithmically weighted Fourier-tail criterion for zeta-spectral tightness. Uniform integrability against the logarithmic sampling density is sufficient; any bounded Fourier moment with superlogarithmic weight is therefore inside the compact class, while a merely bounded logarithmic-order moment is insufficient in general.

WI-390 supplies the missing source-transfer half at that same logarithmic compactness scale. If the logarithmically weighted Fourier tails are uniformly integrable, perforating a fixed-width trial to create exact prime-power source slots changes both its `L^2` norm and the logarithmic difference-form energy by `o(1)`. Combined with WI-389, this extends the recurrence/no-gap mechanism to the sharp logarithmically compact class.

WI-391 shows that this compactness hypothesis is genuinely load-bearing and closes the endpoint-phase caveat left by WI-388 on the RH side. It constructs source-exact fixed-width trials with dilute carrier frequencies `R_k` escaping so rapidly that `A_k/log log R_k->0`, while retaining a uniform negative archimedean margin. Under RH the local zero density supplies enough phase-weighted carrier samples to give

`liminf W[f_k] >= kappa > 0`,

and exact prime-power perforation remains negligible. Thus source exactness and fixed width are compatible with a positive RH Weil floor once uniform logarithmic spectral compactness is deliberately broken in a phase-stable way.

WI-392 identifies the corresponding reverse-direction limitation. In the same dilute-carrier family, each off-critical zero in a fixed-width packet around the moving frequency contributes at most

`q(A,R)=e^(A/2)/log R + e^(-A/2)/A^2 + e^(A/2)R^(-2M)`,

with `q(A,R)->0` on the WI-391 scale. Hence any off-line packet with multiplicity `M_off q(A,R)->0` is invisible at order-one scale to this moving-frequency channel. The RH-side floor is collective: `Theta(log R)` critical-line samples compensate the `1/log R` carrier dilution, while a sparse packet of defects does not. For `R=exp(exp(A^2))`, the sufficient invisible regime includes `M_off=o(A^2e^(A/2))`.

The live fixed-width question has therefore changed again. WI-391 proves that logarithmic compactness can be escaped while preserving source exactness and an RH-side floor; WI-392 shows that this same scalar escape does not automatically become a converse detector for sparse moving off-line zeros. A useful unconditional/equivalence mechanism must add a quantitatively different defect-sensitive channel, aggregate enough off-line mass, use a multiscale family whose sparse sensitivity is not diluted away, or invoke a fuller form without reintroducing the compactness/no-gap obstruction.

## Keep inherited core inertia, source restriction, sampling density, collective floor and sparse-defect sensitivity distinct

The fixed-width quasimodes are robust to arbitrary profile retuning inside families with uniformly integrable logarithmic Fourier tails. WI-388 shows that gamma negativity and exact source slots do not imply that compactness; WI-389 identifies the sampling-density threshold; WI-390 shows that exact source perforation preserves the obstruction once that threshold is met; WI-391 demonstrates that a controlled failure of the same compactness can carry a phase-stable positive floor under RH; WI-392 proves that the same dilute carrier assigns vanishing weight to each sufficiently sparse co-moving off-line defect.

Future claims must therefore state which resource changes: continuous Fourier-tail compactness, zeta-sampled tightness, exact source-perforation stability, endpoint phase control, collective zero density, individual off-line response, width, locality, domain or operator category. A positive RH floor is not yet a coercive equivalence when its carrier obtains order-one mass only by summing many individually vanishing contributions.
