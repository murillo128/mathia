# MI-016 — Finite-radius Weil positivity has a sharp `a^-2` reserve whose leading constant cannot be improved by resolvent optimization

**Evidence level:** supported; exact finite-radius reserve proved, arithmetic exclusion open

## Core intuition

Localized Weil theory creates an explicit finite-radius archimedean reserve that a hypothetical odd zero witness must pay through the signed von-Mangoldt source. Global control of a natural signed discrepancy is already RH-equivalent, so the useful route stays finite-radius/first-crossing.

The newest result closes a tempting mean-side optimization: jointly optimizing all positive digamma resolvents improves the finite-radius reserve **strictly** at every finite aperture, but cannot improve its leading `a^-2` asymptotic or coefficient. Any stronger leading coercivity must come from arithmetic source structure or another invariant, not from recombining the same positive resolvents more cleverly.

## Strongest justified claim

WI-238--WI-243 show that absolute PNT envelopes are on the wrong scale and that subexponential global control of a natural signed odd discrepancy is already equivalent to RH.

WI-244--WI-245 derive the finite-radius reserve. Odd support in `[-a,a]` forces positive loss in each exponential resolvent, and exact Dirichlet--Robin spectral analysis gives `B_Robin(a) ~ (pi^2/4) zeta(3,5/4) a^-2`.

WI-246 defines the exact joint variational reserve `beta_*(a)` from the whole positive digamma-resolvent mean form. Distinct Robin parameters have incompatible ground states, so `beta_*(a)>B_Robin(a)` for every finite `a`. But a common Dirichlet test gives a matching upper bound, hence `a^2 beta_*(a) -> (pi^2/4) zeta(3,5/4)`. The incompatibility gain is asymptotically subleading.

## Synthesis of evidence

The classical mean side is now calibrated to leading order. The next theorem should attack the **actual signed arithmetic charge** at a finite-radius first crossing and show it cannot pay the exact joint reserve, or couple the reserve to an additional source-sensitive finite-radius constraint.

Trying to squeeze a better leading constant from the same family of positive resolvents cannot change the asymptotic tariff.

## Counterevidence / boundary cases

The reserve is necessary for an odd zero witness but does not prove the first crossing lies in the odd sector or that the arithmetic source fails to pay it. WI-246 also leaves subleading finite-radius improvements available, which may matter in a genuinely finite first-crossing argument.

The RH-equivalence in WI-243 concerns one global diagnostic and does not rule out weaker directional source estimates.

## Epistemic status

**Supported finite-radius boundary:** the exact joint positive-resolvent reserve is strictly stronger at finite aperture but has the same sharp leading `a^-2` tariff as the termwise Robin sum. Progress at leading order must come from source-specific arithmetic, not mean-side reoptimization.

## Novelty/prior-art status

Suzuki localization, digamma expansions, exponential kernels, Robin spectra, and two-projection geometry retain their finding-level prior-art boundaries.

## Falsification criterion

Invalidate the WI-245 Robin spectrum, the WI-246 strict incompatibility, or the matching `a^-2` asymptotic. Strategically, prove a finite-radius signed-source bound incompatible with `beta_*(a)` at the first crossing.
