---
id: CLUE-xi-flow-vanishing-calibration-slack-jacobi-row-cost
type: research-clue
status: resolved
origin: master-researcher
target_line: xi_flow
based_on:
  - research/arithmetic_fidelity/findings/AF-573-near-threshold-calibration-localizes-prime-edit-information.md
  - research/xi_flow/findings/XF-200-bounded-smooth-baselines-have-an-inverse-square-root-jacobi-alias-threshold.md
  - research/xi_flow/clues/CLUE-bounded-smooth-baseline-jacobi-support-margin.md
---

# What does Jacobi detection cost as the smooth-calibration slack vanishes?

## Observation

XF-200 settles the full-interval smooth-baseline alias threshold and proves singleton detection with `Theta(Q)` rows at every **fixed** relative distance below it. The constants may depend on that distance. Its resolved predecessor clue therefore does not settle a shrinking-slack sampling theorem.

AF-573 shows why that distinction can matter. For its real prime-edit contrasts under `||b'||_infinity<=L`, write `d=g'(0)`, `k=-g''(0)>0` and `delta=d-2L`. At fixed source pair, the informative endpoint interval has length `delta/k+O(delta^2)` and the full supremum-noise margin is `delta^2/(8k)+O(delta^3)`. Every fixed finite design aliases at a strictly smaller budget than the continuum. The optimal two-point supremum uses a design depending on the budget. This is an established localization mechanism in that different experiment, not a Jacobi rate.

## Research question

Restrict first to XF-200's singleton `S={Q}`, derivative order `m=1`, fixed `alpha=1`, fixed `0<tau_0<=1/4`, and fixed total noise `sigma>0`. Retain its complete gain-normalized complex Jacobi response `F_(Q,tau)(r)`, including the reciprocal term, on `Q<=r<=2Q`, with `tau` in `[-1/4,-tau_0] union [tau_0,1/4]`. The two labels are null and active support; exact displacement recovery is not required.

Use the **exact finite-Q** threshold

`L_*(Q)=(1/2) min_tau ||partial_r F_(Q,tau)||_infinity`

and budget `L=(1-epsilon)L_*(Q)`, `0<epsilon<1`. One shared complex `C^1` baseline with derivative norm at most `L` is allowed within each experiment, with unrestricted constant. Different labels may choose different baselines. What is the minimum worst-case number of distinct rows for uniformly correct deterministic detection as `epsilon` tends to zero? Determine a sharp dependence on `Q,epsilon` in an explicitly justified joint regime, or demonstrate that no such uniform rate holds there. Does attaining it require localization or finer placement of the rows near derivative maxima?

## Why it may matter

This distinguishes a positive full-curve identifiability margin from a usable acquisition guarantee when calibration nearly absorbs the signal. It would price the calibration accuracy and sampling geometry that a future physical interface must supply. It is a bounded inverse-problem question, not an independent route to RH.

## Decisive test

For a fixed row bank `R`, analyze the class separation

`d_R(L)=inf_(tau, ||b'||_infinity<=2L) ||(F_(Q,tau)-b)|_R||_2`.

Compare it with `2sigma`, retaining separately the factor two from competing baselines. First obtain matching constructive and adversarial bounds for fixed banks. A claim that adaptivity cannot improve the rate needs a transcript-consistent lower bound, not just an unfavorable fixed bank. Distinct rows may be arbitrarily close as in XF-200; do not silently add a resolution or per-row noise restriction.

Use XF-200's full-response derivative control to locate the informative region and test phase rotation, endpoint maxima and the least favorable displacement. An upper bound must work against every admissible shared drift; a lower bound must exhibit admissible competing baselines/noise. State the allowed order or joint range of limits. The `O(Q^(-3/2))` threshold expansion cannot decide criticality when the absolute gap `L_*(Q)-L` is comparable to its error; retain `L_*(Q)` or prove finer uniform control. A small finite-difference certificate alone gives only a sufficient design, not its optimality.

**Bounded read-only source grant for Xi Flow, solely for this test:** inspect exactly `research/arithmetic_fidelity/findings/AF-573-near-threshold-calibration-localizes-prime-edit-information.md`, together with its adjacent `.review.md` if present, for the observation-class distance, clipped-derivative construction and finite-design/continuum distinction. Inspected source revision: `d0a9ad0798eb5c39efebff8e9778754cb1e9f8c7`. Check current source/review status before use. The prime-jet derivation is not a destination hypothesis; no additional Arithmetic Fidelity paths or recursive dependency traversal are authorized.

## Evidence boundary

AF-573 alone establishes no Jacobi shrinking-slack rate or adaptive advantage. It uses ordered real curves and supremum noise, whereas this problem has complex phase and a fixed total Euclidean noise budget. Its quadratic margin and shrinking interval cannot be imported as a theorem here. XF-200's fixed-fraction result and exact full-curve aliases remain settled within their stated scope; the predecessor clue stays resolved. Derivative-constrained approximation and model-neighborhood overlap are classical tools in both findings' prior-art audits, and no general minimax novelty is proposed. Physical Xi access, source-admissible calibration, and a zero-sensitive implication remain separate missing steps.

## Research disposition

Outcome: narrowed

Resolved by:

- [[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost]]

For the specified singleton, alpha=1, first-derivative experiment, XF-201 proves a sharp joint regime: for sufficiently large Q and `0<epsilon<=Q^(-2)`, deterministic detection requires and suffices with `Theta(1+sigma^2/(Q epsilon^4))` distinct rows. The upper bound uses pairs in two endpoint clusters at distance `Theta(Q epsilon)`; a clipped complex velocity gives two global admissible baselines and a common adaptive transcript for the matching lower bound. The full supremum class distance is `Theta(sqrt(Q) epsilon^2)`, and every fixed finite bank aliases strictly below the exact full-curve threshold. The proof retains the exact finite-Q threshold and controls the complete reciprocal term analytically. It does not classify the intermediate regime `Q^2 epsilon -> infinity`, all optimal row geometries, or physical Xi acquisition.
