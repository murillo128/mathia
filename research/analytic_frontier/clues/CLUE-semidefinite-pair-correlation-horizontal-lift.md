---
id: CLUE-analytic-frontier-semidefinite-pair-correlation-horizontal-lift
type: research-clue
status: proposed
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-002-pair-correlation-hilbert-horizontal-information.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can a signed semidefinite or multi-feature lift beat Montgomery--Taylor unconditionally while retaining horizontal sensitivity?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality converts the existing unconditional BGSST complex-difference pair-correlation formula directly into a lower bound for zeros that are simultaneously simple and on the critical line. It also records a sharp obstruction: when the certificate is built from one feature `eta` through `K=widehat{eta^2}` and the quadratic observable `K^2`, the Carneiro--Chandee--Littmann--Milinovich extremal theorem forces the Montgomery--Taylor constant `C_MT`, so the resulting simple-critical proportion cannot exceed `0.6725007...`.

The neighboring `weil_inertia` line now closes the most obvious alternative inside support one. `WI-118` proves that any real-even support-one pair profile whose kernel is universally termwise nonnegative on real vertical separations is forced into an endpoint-tapered class whose mirror-pair-versus-double signal is `o(M)` on the critical screening lattice. Thus a useful extension cannot simply restore the old strategy “make every unwanted cross-height term positive and discard it.” It must tolerate sign changes and control the signed reservoir globally, or add genuinely new support/information.

There is established evidence that a broader quadratic class can do better when RH is assumed. Chirre--Gonçalves--de Laat replace compact Fourier support by a Cohn--Elkies sign condition and optimize the resulting pair-correlation bound by semidefinite programming, obtaining the multiplicity constant `1.3208` and hence a `0.6792` simple-zero proportion under RH. Their proof uses a real-ordinate pair-correlation function and an out-of-band sign argument, so this gain does not automatically survive for arbitrary off-line zeros. Separately, `WI-001` records an unaudited 2026 claim that several legal bandlimited profiles and pair interactions already give a smaller unconditional gain, suggesting that joint quadratic constraints may escape the one-feature extremal problem even without widening Fourier support.

## Research question

Is there a genuinely RH-free extension of Lamzouri's simple-real Hilbert inequality from a single factorized kernel to a finite **signed** positive-semidefinite or multi-feature family whose total complex-zero pair contribution remains evaluable by the unconditional BGSST support-one theorem, and whose optimized normalized constant is strictly smaller than `C_MT`?

A second, more ambitious version is to identify an unconditional replacement for the out-of-band sign-discard step in the Chirre--Gonçalves--de Laat linear-programming class. The replacement must operate on the conjugation-invariant complex zero multiset rather than silently reducing to the RH real-ordinate setting, and it must survive the `WI-118` screening control.

## Why it may matter

Any certificate with normalized quadratic constant `< C_MT` would immediately improve the unconditional `0.6725007...` proportion of simple critical zeros while staying entirely inside a pair-correlation framework. More importantly, it would identify exactly what extra second-order information is present beyond one global squared kernel, potentially supplying the richer horizontal observable sought by both `analytic_frontier` and `weil_inertia` without invoking unproved higher prime correlations.

If no such lift exists, a structural no-go theorem would be nearly as valuable: it would show that the whole support-one positive-semidefinite second-order world collapses to the Montgomery--Taylor ceiling once universal termwise positivity is excluded by screening, and that progress must use wider support, higher-order correlations, or a genuinely different analytic input.

## Decisive test

Start with the smallest nontrivial multi-feature model. Let several compactly supported real-even feature functions `eta_j` generate a vector-valued feature map for each conjugate-symmetric point and derive the strongest simple-real counting inequality obtainable from its block Gram operator. Require every scalar zero-side observable appearing after expansion to be the Fourier transform of a test function supported in `[-1,1]`, so BGSST evaluates it unconditionally. Do **not** impose termwise nonnegativity on the resulting real-axis kernels; `WI-118` already shows that such a restriction forces screening.

Then solve the resulting finite convex/semidefinite extremal problem, first symbolically where possible and then with a rigorous numerical certificate if needed. The direction survives if one exhibits a valid certificate whose asymptotic pair constant is `< C_MT` and whose signed cross-height terms are controlled by the global Hilbert/PSD inequality itself. It is killed within this class if the multi-feature inequality reduces exactly to a convex combination or congruence of one-feature certificates, or if a dual extremizer proves the universal lower bound `C_MT`.

For the out-of-band variant, the decisive requirement is an exact RH-free inequality controlling the Fourier tail that Chirre--Gonçalves--de Laat handle through their RH-side real-ordinate form factor. A numerical SDP improvement without such an inequality, or a proof that recovers universal termwise positivity and therefore re-enters `WI-118`, is not evidence.

## Evidence boundary

No multi-feature unconditional improvement or no-go theorem is established here. The `0.6792` semidefinite result assumes RH, and the multi-profile unconditional improvement recorded in `WI-001` remains `NEEDS-AUDIT`; neither can be imported as proof that the proposed lift works. `WI-118` rules out universal termwise-positive support-one extraction but does not rule out a globally controlled signed PSD/multi-feature certificate. The clue identifies a precise certificate class and a strict numerical threshold whose resolution would materially change the line.