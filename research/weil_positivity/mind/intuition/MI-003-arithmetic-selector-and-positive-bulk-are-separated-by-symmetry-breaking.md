# MI-003 — Arithmetic selectors can survive in positive finite readouts, but the critical completion keeps changing the pairing

**Evidence level:** supported by exact finite selectors and decisive completion obstructions

## Core intuition

The newer Weil-positivity evidence refines the earlier “signed selector versus positive bulk” picture. Positivity does not always erase arithmetic immediately: finite incidence Gram determinants and primitive-shell log-determinants can recover `Lambda(n)` from canonical positive operators. The failure occurs one step later. Those positive readouts are rank/cyclotomic tests in the wrong pairing, and the operations needed to pass to the critical infinite Weil form either become nonclosable, expose an unbounded-below signed birth operator, or cancel that birth term under natural positive radial compression. The decisive variable is therefore not positivity alone but **which pairing and completion carries the selector**.

## Strongest justified principle

The exact evidence now has two complementary sides.

1. **Positive finite recovery is possible.** WP-030 constructs a canonical positive degree-one Gram operator whose determinant recovers `Lambda(n)^2`; the mechanism is nevertheless a rank test universal for weighted free commutative monoids and has no archimedean sector. WP-043 gives an independent Prime-Circle realization: the positive cycle Laplacian has primitive-shell log-determinant exactly `Lambda(n)`. That identity is cyclotomic and lives in scalar spectral calculus, not in the pointwise shell pairing needed for the Weil birth matrix.
2. **Critical completion changes category or pairing.** WP-032 proves that the direct critical Gram completion with amplitudes `(log p)/sqrt(p)` is nonclosable on the natural `ell^2` place space; WP-033 rules out rescue by an equivalent Hilbert renorming. WP-034 shows that the intrinsic Prime-Circle boundary birth operator contains the correct interior Weil ray weights but is unbounded below, while its stable positive orientation classicalizes to the Poisson/GCD route. WP-037 identifies the same birth form as a singular first-order tangent to profinite Haar rather than an ordinary positive probability tangent.
3. **Natural sign-preserving reductions erase the finite birth operator.** WP-044 proves that finite positive radial contrasts remove the universal collision mode and the arithmetic birth operator in the same common radial channel. WP-045 shows that ordinary positive Schur/Feshbach elimination has the same failure: the boundary limit becomes a universal scalar radial kernel tensored with the shell identity, with the birth operator surviving only in a vanishing correction.

Together with WP-018--WP-023, these results support a stronger design rule: **extracting the right arithmetic coefficient is easier than transporting it through the right positive global pairing.**

## What remains possible

A successful construction may use shell-dependent or singular radial filtering, a nonseparable finite--archimedean sector, a boundary/distributional pairing, a nonlinear determinant/intersection form, or another category-changing operation with an independent sign theorem. The operation must be forced before the finite selector is averaged into a universal radial/Haar mode and must also generate the archimedean/polar contribution.

The exact finite positive selectors remain useful evidence about what information is available; they are not themselves evidence for the Weil sign.

## Status / novelty

The finite determinant identities, nonclosability results, boundary birth spectrum, singular Haar tangent, and radial contrast/Schur cancellations are persisted findings. Their common “pairing/completion gate” interpretation is a supported synthesis, not a theorem that every positive completion fails.

## Falsification criterion

Start from one of the audited finite positive selectors and derive a canonical completion whose closed/global pairing retains the exact critical finite-prime coefficients, supplies the archimedean/polar sector, and has an independently proved Weil sign. A shell-blind finite radial contrast or ordinary Schur elimination retaining the leading birth operator would contradict WP-044--WP-045.

## Lean-formalizable core

- Rank-one Gram determinant selector for `Lambda`.
- Nonclosability criterion for the critical rank-one form.
- Primitive-shell cycle determinant `log det = 2 Lambda(n)`.
- Common-mode cancellation of the boundary birth operator under finite radial contrasts and Schur elimination.
