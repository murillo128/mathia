# MI-001 — Fixed-complexity qualitative or logarithmic cancellation has no polynomial global budget; the summability carrier matters

**Evidence level:** supported by MC-001, MC-004--MC-006, and the matched-control/Tauberian classifications MC-039--MC-042

## Core intuition

Very strong qualitative pseudorandomness can coexist with nearly linear anchored sums. The current controls now cover exact Möbius support, multiplicativity, strong aperiodicity, all qualitative logarithmic two-point Elliott tests, and every fixed odd-order logarithmic self-correlation. None supplies a fixed power saving. The newer Tauberian audit adds a second separation: even quantitatively small **harmonic** correlation primitives do not become comparably small ordinary correlations without an additional signed inverse mechanism.

The missing resource is therefore not “more fixed-order randomness” but a **polynomial information budget in the same summability/scale category used by the target, or a proved transfer between categories**.

## Strongest justified principle

MC-001 and MC-006 give the generic transfer ceilings. Local-window control and van der Corput convert absolute local/correlation budgets into global cancellation only at the rate actually present in those budgets; logarithmic decay stays logarithmic.

MC-004--MC-005 provide matched controls with exact squarefree support, and then with multiplicativity, whose partial sums remain `x/(log x)^beta` despite strong qualitative cancellation properties.

MC-039 strengthens the multiplicative control: the explicit family is strongly aperiodic and satisfies Tao's complete qualitative logarithmic two-point Elliott conclusion against bounded multiplicative comparators while retaining near-linear anchored sums. MC-040 raises the correlation order: every fixed odd-order logarithmic self-correlation vanishes, yet the same partial-sum asymptotic survives. Increasing fixed qualitative correlation order therefore does not create a polynomial budget.

MC-041 isolates the change-of-summability obstruction exactly. If `H_b(X)=sum_{n<=X}b_n/n`, discrete Abel summation gives

`B_b(X)=X H_b(X)-sum_{m<X} H_b(m)`.

A bound on `sup |H_b|` loses an `X` factor in black-box conversion, and explicit sign sequences can have uniformly bounded harmonic prefixes but linear ordinary sums; the phenomenon can even be realized as a fixed-lag autocorrelation. Quantitative logarithmic Chowla thus needs a genuinely Tauberian/arithmetic bridge before ordinary van der Corput can yield a power saving.

MC-042 closes the obvious smoothing workaround. Every fixed-order Möbius Riesz mean has Mellin transform equal to `1/zeta(s)` times a zero-free Gamma quotient, so its `x^(1/2+epsilon)` bound is RH-equivalent for every fixed order. Fixed smoothing changes regularity but not the critical zero-information class. A distinct route must use scale-dependent smoothing, a nonlinear/multiscale carrier, or an independently weaker input together with a quantitative inverse theorem.

## What remains possible

Polynomially quantitative growing-shift correlations, ordinary rather than logarithmic correlations, a source-specific Tauberian identity preserving sign, scale-dependent Riesz laws, bilinear/Type-I-II structure, or higher-order information whose complexity itself grows with scale can lie outside these controls. The requirement is an explicit transfer inequality showing where the polynomial gain enters.

## Status / novelty

The correlation theorems, pretentiousness, Abel summation, Riesz/Mellin factors, and matched multiplicative controls use classical or literature-backed mechanisms. The synthesis is the information-budget boundary: **fixed qualitative complexity and fixed analytic smoothing do not manufacture the exponent needed by the ordinary anchored sum**.

## Falsification criterion

Derive a fixed power saving for the anchored sum from only the properties matched by MC-039--MC-040, or a power ordinary-correlation bound from harmonic-prefix magnitudes without additional structure, or show that a fixed-order Riesz critical bound is weaker than RH despite MC-042's zero-free Mellin multiplier.
