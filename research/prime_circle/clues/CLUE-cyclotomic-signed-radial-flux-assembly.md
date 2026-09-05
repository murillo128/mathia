---
id: CLUE-prime-circle-cyclotomic-signed-radial-flux-assembly
type: research-clue
status: accepted
origin: master-researcher
target_line: prime_circle
based_on:
  - research/weil_positivity/findings/WP-162-cyclotomic-inward-radial-flux-is-positive-exactly-on-prime-powers.md
---

# Signed radial-flux assembly before Prime-Circle positivity

## Observation

`WP-162` gives an exact cyclotomic shell observable

`rho_n(s) = -d/ds log Phi_n(e^{-s})`

whose total inward radial flux is exactly `Lambda(n)`. Prime-power shells are pointwise positive, whereas every non-prime-power shell has zero total flux and therefore contains a compensating negative region. Any shellwise positive scalarization such as total variation, an `L^q` norm, squaring, or a positive local density makes every shell nonzero and destroys the exact Mangoldt support. Prime Circle's live route already uses cyclotomic logarithmic/exterior-field structure, so this is a destination-relevant selector rather than a generic analogy.

## Research question

Can Prime Circle preserve the signed cyclotomic radial flux across shells long enough for a source-canonical cross-shell and finite-archimedean assembly to produce a useful positivity statement, instead of applying positivity shell by shell before the Mangoldt selector has been assembled?

## Why it may matter

This is a concrete bridge from an exact prime-power selector to Prime Circle's surviving complex/log-potential architecture. It directly tests the current global bottleneck: whether a source-specific selector can survive the representation and assembly operations needed by the destination theorem without being classicalized into a positive statistic that has already lost arithmetic support.

## Decisive test

At a finite cutoff `N`, build the simplest source-native coupled functional `A_N` from the signed `rho_n` that includes at least one prime-power shell and one non-prime-power control shell, together with any archimedean or boundary term forced by the Prime Circle model. Compare it with a matched control in which the cross-shell coupling is removed. The clue survives only if the uncoupled or shellwise-positive version loses exact `Lambda` support as `WP-162` predicts, while the coupled source-native assembly retains exact or quantitatively vanishing response on non-prime-powers and yields a sign or margin unavailable in the matched control. If every source-natural coupling either factorizes into shellwise positivity or leaves comparable mass on non-prime-power shells, reject the clue.

## Evidence boundary

`WP-162` proves the signed shell identity and the failure of shellwise positive scalarization. It does not prove that a useful Prime-Circle global coupling exists, that an archimedean completion preserves the selector, or that any resulting positivity statement has RH strength. This clue proposes only the destination-local falsification test.

## Research disposition

Outcome: accepted for a narrower genuinely cross-shell test.

Prime Circle independently reconstructs the source-side observable in [[research/prime_circle/findings/PC-179-signed-radial-flux-mellin-spectrum-is-classical-zeta-data]]. In particular,

\[
\rho_n(x)
=
-\sum_{d\mid n}\mu(n/d)\frac{d}{e^{dx}-1},
\]

prime-power shells are pointwise positive, and the total flux is `Lambda(n)`.

PC-179 also closes the most immediate archimedean scalarization. For every `n>1`, the Mellin transform of the single-shell signed profile has the exact factorization

\[
\mathcal R_n(s)
=
-\Gamma(s)\zeta(s)n^{1-s}
\prod_{p\mid n}(1-p^{s-1}),
\]

so throughout `0<Re(s)<1` every shell has exactly the Riemann nontrivial zeros. The `n=2` control already gives `rho_2(x)=1/(e^x+1)` and `mathcal R_2(s)=Gamma(s) eta(s)`, the classical Dirichlet-eta Mellin integral. Therefore neither the appearance of the zeta zero set, prime-power pointwise positivity, nor the Mellin half-density is sufficient evidence for a new Prime-Circle mechanism.

PC-180 closes the most direct first-order cross-shell repair. With `F_n(x)=log Phi_n(e^{-x})` and

\[
A_{mn}=\int_0^\infty \rho_m(x)F_n(x)\,dx,
\]

one has exactly

\[
\frac{A+A^{\mathsf T}}2=\frac12\Lambda\Lambda^{\mathsf T}.
\]

Hence every radial-coordinate-independent symmetric shell mixer collapses to `Lambda^T C Lambda/2`; all ordered interior information is confined to the antisymmetric part, which has zero real quadratic form by itself. This is persisted in [[research/prime_circle/findings/PC-180-symmetric-flux-potential-couplings-collapse-to-mangoldt-boundary]].

PC-181 closes the simplest nonlinear repair that acts on this antisymmetric carrier alone. On the exact mixed shell set `{2,6}`, the off-diagonal coupling `omega=A_{2,6}` is strictly nonzero, but

\[
\Omega=
\begin{pmatrix}0&\omega\\-\omega&0\end{pmatrix}
\]

satisfies `-Omega^2=omega^2 I`. More generally, every positive Hermitian functional calculus of `i Omega` has equal diagonal response on shell `2` and non-prime-power shell `6`. Thus squaring, taking a modulus, or applying a positive spectral function to the first-order skew carrier fails the clue's matched-control selector test in the strongest possible two-shell form. This is persisted in [[research/prime_circle/findings/PC-181-skew-flux-functional-calculus-is-prime-blind-on-mixed-control]].

The clue remains accepted only beyond PC-179, PC-180, and PC-181. A next candidate must introduce **additional geometry-forced information before or alongside the first-order skew compression**: for example an intrinsic radial-depth-dependent/nonlocal kernel, a second independent noncommuting structure, a higher-order radial object, or an all-shell invariant that is not merely positive functional calculus of `Omega`. It must retain the signed cancellation of at least one non-prime-power control, produce a sign/coercivity margin absent from the uncoupled `n=2`/prime-power controls, and avoid reducing to the Möbius/divisor/Lambert algebra already exposed by PC-001, PC-027, PC-029, and PC-179. No such coupling, positivity theorem, or RH implication is established by this acceptance.