---
id: CLUE-analytic-frontier-semidefinite-pair-correlation-horizontal-lift
type: research-clue
status: accepted
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-002-pair-correlation-hilbert-horizontal-information.md
  - research/analytic_frontier/findings/ANF-003-common-translation-vector-features-scalarize.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can a signed semidefinite or multi-observable lift beat Montgomery--Taylor unconditionally while retaining horizontal sensitivity?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality converts the existing unconditional BGSST complex-difference pair-correlation formula directly into a lower bound for zeros that are simultaneously simple and on the critical line. It also records a sharp obstruction: when the certificate is built from one feature `eta` through `K=widehat{eta^2}` and the quadratic observable `K^2`, the Carneiro--Chandee--Littmann--Milinovich extremal theorem forces the Montgomery--Taylor constant `C_MT`, so the resulting simple-critical proportion cannot exceed `0.6725007...`.

`WI-118` closes the obvious alternative that retains support one and restores deterministic extraction by requiring every real-axis pair term to be nonnegative: universal termwise positivity forces endpoint taper and screening on the critical lattice.

`ANF-003` now closes the smallest apparent semidefinite enlargement as well. If finitely many feature components share the same translation character `e^{-2 pi iuz}` and the counting inequality consumes only their scalar Hilbert Gram kernel, then the vector seed `a(u)` enters only through `q(u)=||a(u)||^2`. The whole construction is exactly the scalar Lamzouri feature `eta=sqrt(q)`, and constant positive-semidefinite mixing or positive convex combinations remain bounded below by `C_MT`. Thus **feature multiplicity by itself is not additional pair-correlation information**.

There is nevertheless established evidence that a broader quadratic class can do better when RH is assumed. Chirre--Gonçalves--de Laat replace compact Fourier support by a Cohn--Elkies sign condition and optimize the resulting pair-correlation bound by semidefinite programming, obtaining the multiplicity constant `1.3208` and hence a `0.6792` simple-zero proportion under RH. Their proof uses a real-ordinate pair-correlation function and an out-of-band sign argument, so this gain does not automatically survive for arbitrary off-line zeros. Separately, `WI-001` records an unaudited 2026 claim that several legal bandlimited profiles and pair interactions already give a smaller unconditional gain, suggesting that genuinely joint quadratic constraints may escape the one-feature extremal problem even without widening Fourier support.

## Research question

Is there a genuinely RH-free extension of Lamzouri's simple-real Hilbert inequality that retains **several pair observables or matrix entries as independent information** rather than collapsing them to one scalar translation-invariant Gram kernel, and whose optimized normalized constant is strictly smaller than `C_MT` while every zero-side observable remains evaluable by the unconditional BGSST support-one theorem?

The most conservative surviving form is a finite signed or matrix-valued family whose validity follows from one global Hilbert/operator inequality. The operator or multi-observable structure must remain present until after the counting inequality is applied; `ANF-003` shows that a direct-sum feature representation followed by scalar Gram compression is exactly the old one-feature problem.

A second, more ambitious version is to identify an unconditional replacement for the out-of-band sign-discard step in the Chirre--Gonçalves--de Laat linear-programming class. The replacement must operate on the conjugation-invariant complex zero multiset rather than silently reducing to the RH real-ordinate setting, and it must survive the `WI-118` screening control.

## Why it may matter

Any certificate with normalized quadratic constant `< C_MT` would immediately improve the unconditional `0.6725007...` proportion of simple critical zeros while staying inside a pair-correlation framework. More importantly, it would identify exactly what additional second-order information is available beyond one scalar Gram kernel, potentially supplying the richer horizontal observable sought by both `analytic_frontier` and `weil_inertia` without invoking unproved higher prime correlations.

A no-go theorem for the surviving operator/multi-observable class would be nearly as valuable: combined with `ANF-003` and `WI-118`, it would show that support-one second-order information is exhausted much more broadly and redirect the program toward wider support or genuinely higher-order correlations.

## Decisive test

Start with the smallest model that is **not** covered by `ANF-003`: two or more support-one scalar pair profiles whose BGSST asymptotics are individually legal, but keep their quadratic forms separate and derive a counting inequality involving a nontrivial matrix of these observables. Equivalently, use a translation-invariant operator-valued kernel and ensure that at least two operator entries survive into the deterministic simple-real bound before any scalar trace or fixed-vector compression.

First apply the scalarization control from `ANF-003`. If the proposed block inequality depends only on one effective density `q(u)` or on a positive convex average of separately normalized scalar certificates, kill it immediately as a disguised one-feature certificate.

If genuine matrix information survives, derive the exact deterministic inequality on an arbitrary finite conjugation-invariant complex multiset, then expand every required zero-side observable into BGSST-legal support-one test functions. The direction survives if the resulting rigorous asymptotic certificate has constant `< C_MT` with signed cross-height terms controlled by the global matrix inequality itself. It is killed within this class if an operator-valued duality or Gram-equivalence theorem proves reduction to the scalar extremal problem.

For the out-of-band variant, the decisive requirement remains an exact RH-free inequality controlling the Fourier tail that Chirre--Gonçalves--de Laat handle through their RH-side real-ordinate form factor. A numerical SDP improvement without that inequality, or a construction that restores universal termwise positivity and therefore re-enters `WI-118`, is not evidence.

## Evidence boundary

No multi-observable unconditional improvement or general operator-valued no-go theorem is established here. `ANF-003` rules out only common-translation vector features after scalar Gram compression, constant PSD mixing of that representation, and positive convex combinations of scalar Lamzouri certificates. Genuine operator-valued kernels can retain matrix spectral information if a new counting inequality actually consumes it.

The `0.6792` semidefinite result assumes RH, and the multi-profile unconditional improvement recorded in `WI-001` remains `NEEDS-AUDIT`; neither is proof that the surviving lift works. `WI-118` rules out universal termwise-positive support-one extraction but not a globally controlled signed matrix certificate.

## Research disposition

Accepted, with the search region narrowed by `ANF-003`. Do not spend further effort on direct-sum vector features, constant PSD feature mixing, or convex ensembles that collapse to one scalar Gram kernel. The unresolved question is whether genuinely **joint** support-one pair information can be retained in an operator/multi-observable counting inequality and beat `C_MT` without RH.