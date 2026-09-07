---
id: CLUE-mobius-cancellation-mean-absolute-mertens-transfer-budget
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier.md
  - research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling.md
  - research/mobius_cancellation/findings/MC-009-pintz-mean-absolute-zero-boundary.md
  - research/mobius_cancellation/findings/MC-013-discrete-tanaka-l1-feedback-carrier.md
  - research/mobius_cancellation/findings/MC-019-path-energy-coarse-riesz-rh-equivalence.md
  - research/mobius_cancellation/findings/MC-044-growing-riesz-endpoint-visibility-delay.md
  - research/mobius_cancellation/findings/MC-115-mean-absolute-mertens-mellin-zero-free.md
  - research/mobius_cancellation/findings/MC-116-subpower-dense-mean-absolute-checkpoints.md
  - research/mobius_cancellation/findings/MC-117-fractional-mertens-moment-transfer-ceiling.md
  - research/mobius_cancellation/findings/MC-118-balanced-prime-block-multiplicative-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-119-uniform-polynomial-window-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-120-fixed-function-lacunary-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-121-arbitrary-checkpoint-mean-absolute-rh-criterion.md
---

# Can a source-natural local statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The current local and averaged inputs remain below the polynomial information budget needed for RH-scale Möbius cancellation. `MC-001` isolates the exceptional-mass loss in almost-all short intervals, while `MC-006` shows that the available averaged two-point Chowla input yields only logarithmic saving through the audited black-box van der Corput route.

The useful endpoint is

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` proves directly that an all-scale bound `D_M(X)=O_epsilon(X^(1/2+epsilon))` is equivalent to RH through absolute Mellin convergence. `MC-116` then showed that monotonicity can recover such an all-scale bound from a subpower-dense checkpoint sequence.

`MC-121` materially shrinks the output requirement again. Pintz's 1987 Theorem A gives, for every off-critical zero `rho=beta+i gamma`,

`D_M(Y) > Y^beta/gamma^5` for every `Y>gamma^5`.

Therefore RH is already equivalent to the square-root-plus-epsilon bound for `D_M` along **any unbounded checkpoint sequence, with no density condition at all**. The subpower-density gate from `MC-116` belongs only to its monotone interpolation mechanism; it is not a gate for RH once Pintz's established zero-to-mean lower bound is used. Equivalently, RH is characterized by `liminf log D_M(Y)/log Y <= 1/2`.

The source-side obstruction remains severe. `MC-117` proves that fixed fractional moments below `L^1` underweight rare coherent excursions sharply enough to miss the required first moment. `MC-118` shows generic multiplicativity plus exact square-free support does not repair that loss. `MC-119` makes the weak bound uniform through a polynomial scale window and still preserves a super-square-root first-absolute excursion. `MC-120` embeds infinitely many such bad windows in one fixed multiplicative function. Thus the missing ingredient is not endpoint scale density; it is a genuinely Möbius-specific mechanism that recovers first-moment amplitude from weaker source information.

## Research question

Can a source-natural signed local, bilinear, multiplicative, correlation, or multiscale **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some rigorously produced unbounded sequence `X_j -> infinity`, without first proving a pointwise RH-scale bound for `M`, inserting an RH-equivalent coarse statistic into the hypotheses, or reconstructing Möbius tautologically from its complete prime law?

After `MC-117`--`MC-120`, a viable source condition must contain information absent from exact-support multiplicative comparators with balanced prime-block transport. Candidate information therefore has to be genuinely joint or arithmetic: quantitative correlation-plus-multiplicativity, an intermediate prime-local constraint weaker than exact specification, a bilinear identity with sign retained, or another Möbius-specific law that forbids coherent first-moment excursions.

The downstream burden is now minimal in scale. Once the actual Möbius function satisfies the RH-scale `D_M` estimate on any unbounded sequence, `MC-121` closes RH directly. There is no remaining need to interpolate `D_M` between those output scales.

## Why it may matter

Mean-absolute control is weaker than pointwise Mertens control but remains RH-complete. `MC-121` shows it is also extraordinarily sparse in the scale variable: even super-power-lacunary checkpoints suffice. A successful source-to-`D_M` transfer can therefore focus entirely on obtaining the right **amplitude exponent** where its arithmetic structure is strongest, rather than simultaneously solving a scale-coverage problem.

This also sharpens what the comparator program must test. `MC-120` used lacunarity to construct one fixed multiplicative countermodel, but that lacunarity no longer protects a proposed theorem about the actual Möbius mean. A comparator only kills a candidate source statistic if it satisfies that statistic at the same claimed source strength while keeping `D_1` too large; it cannot appeal to generic scale-interpolation failure after the source statistic has already transferred to actual `D_M`.

## Decisive test

Fix an explicit source-natural statistic and prove one of two outcomes:

1. derive a source-compatible implication from a quantitatively polynomial hypothesis on that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on **any explicitly controlled unbounded sequence**; or
2. construct a single fixed-function or equally source-faithful matched control satisfying the proposed source hypothesis at the claimed scales while its first-absolute partial-sum mean retains exponent `>1/2` there.

A candidate fails if its input already contains an RH-equivalent fixed Riesz/coarse mode, if smoothing makes the controlled quantity normalization-vacuous, if inversion reintroduces the original partial-sum burden, if triangle inequality spends the polynomial gain on exceptional mass, if a sub-`L^1` compression discards rare coherent amplitude without a source-specific recovery theorem, if it relies only on generic multiplicativity or exact square-free support, or if exact agreement with `mu(p)=-1` at every prime is used as the supposed intermediate condition.

Scale density of the **final `D_M` output** is no longer a failure criterion. If a candidate genuinely proves the RH-scale mean-absolute estimate for actual Möbius on an arbitrarily sparse unbounded sequence, `MC-121` says that is already enough.

## Evidence boundary

`MC-121` is a literature-backed target reduction based on Pintz's 1987 zero-to-mean theorem; it is not a source-natural cancellation mechanism. It does not make the square-root estimate easier in exponent and does not transfer any existing local/correlation theorem to `D_M`.

`MC-116` remains valid as an interpolation theorem and still quantifies what sampled mean-absolute information implies at intermediate physical scales without invoking the Pintz zero theorem. Its subpower-density condition is simply no longer necessary for the narrower goal of proving RH.

`MC-117`--`MC-120` remain generic/comparator obstructions. Their constructions do not preserve all quantitative Möbius correlation information or the exact prime law, and they do not inherit Pintz's zeta-specific lower bound. They therefore do not rule out a theorem using genuinely Möbius-specific joint structure.

The stronger 2026 Pintz claims in `MC-009` about the full limiting logarithmic exponent and terminal-window maxima remain audit-sensitive. `MC-121` does not depend on them; its scale reduction comes from the established 1987 theorem.

## Research disposition

**Accepted, narrowed through `MC-121`.** The active residual is now a pure information-recovery problem rather than an information-plus-scale-coverage problem. A surviving route must preserve enough signed Möbius-specific structure to upgrade weaker local, bilinear, multiplicative, or correlation control to the first absolute mean at square-root exponent. It may do so on any unbounded sequence of output scales. The clue remains accepted rather than resolved because no such polynomial source-to-`D_M` transfer is currently established.