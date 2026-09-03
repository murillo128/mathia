---
id: CLUE-analytic-frontier-semidefinite-pair-correlation-horizontal-lift
type: research-clue
status: accepted
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-002-pair-correlation-hilbert-horizontal-information.md
  - research/analytic_frontier/findings/ANF-003-common-translation-vector-features-scalarize.md
  - research/analytic_frontier/findings/ANF-004-convex-finite-pair-moment-lifts-dualize.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can a signed support-one dual profile or genuinely configuration-level matrix lift beat Montgomery--Taylor unconditionally?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality converts the existing unconditional BGSST complex-difference pair-correlation formula directly into a lower bound for zeros that are simultaneously simple and on the critical line. Its one-factor positive class is sharply capped by the Montgomery--Taylor constant `C_MT`, while `WI-118` rules out the obvious support-one escape based on universal termwise nonnegativity because positivity forces endpoint taper and screening.

`ANF-003` closes common-translation vector features that are eventually compressed to one scalar Gram kernel: feature multiplicity, constant PSD mixing, and positive convex averaging do not add information beyond one nonnegative scalar spectral density.

`ANF-004` now closes a broader interpretation of “genuinely joint.” If finitely many BGSST-legal global pair sums are combined by an affine lower bound, their combination is exactly one signed scalar support-one profile. If they enter through a convex lower-bound aggregator that is subdifferentiable at the asymptotic BGSST moment point, a supporting hyperplane gives an affine certificate of identical asymptotic strength there, hence again one signed effective profile. Appropriate finite LP/SDP/conic moment relaxations with strong duality therefore have a scalar signed dual witness whenever their only zeta-side data are those finitely many global pair moments.

This does not exhaust support-one information. The effective dual profile can change sign, so neither the positive one-factor Montgomery--Taylor extremal theorem nor `WI-118` applies. It also does not cover matrix/eigenvalue/order information retained before global scalar summation, nonconvex configuration-level statistics, wider support, or higher-order correlations.

There is established evidence that broader auxiliary-function information can improve pair-correlation bounds when RH is assumed. Chirre--Gonçalves--de Laat enlarge the usual bandlimited class to a Cohn--Elkies sign class and optimize it by semidefinite programming, obtaining the `1.3208` multiplicity constant and `0.6792` simple-zero proportion under RH. That gain relies on a real-ordinate pair-correlation framework and an out-of-band sign argument, so it is not yet an unconditional complex-zero certificate.

## Research question

Does there exist a real-even **signed** support-one BGSST-legal profile whose globally summed complex-difference statistic satisfies a deterministic conjugation-invariant inequality strong enough to force a simple-critical proportion strictly above `2-C_MT`?

The counting inequality must control the signed cross-height reservoir globally; it may not restore universal termwise positivity, since `WI-118` would then force screening. The first target should therefore be the scalar dual normal form exposed by `ANF-004`, not another finite vectorization or SDP wrapper around the same global moments.

A separate surviving branch is genuinely configuration-level matrix information: an operator-valued or multi-observable construction in which matrix order, eigenvalues, inertia, or local block structure is used **before** the zero configuration is compressed to finitely many global scalar pair sums. Such a mechanism lies outside the `ANF-004` dual reduction and should be tested only if the scalar signed route fails or the matrix structure supplies an exact new inequality.

## Why it may matter

A valid signed support-one certificate with normalized constant `< C_MT` would immediately improve the unconditional `0.6725007...` simple-critical proportion without requiring wider Fourier support or unproved higher prime correlations. More importantly, it would identify the precise extra second-order information hidden by positive-kernel formulations: not “more features,” but controlled cancellation among cross-height pair terms.

Conversely, a no-go theorem for the signed scalar normal form would combine with `ANF-003`, `ANF-004`, and `WI-118` to show that a very broad support-one second-order program is exhausted, strongly redirecting the line toward wider support, finite-`T` joint fluctuation information, or genuinely higher-order correlations.

## Decisive test

Start with one real-even signed profile `J` supported in `[-1,1]` whose BGSST evaluation is legal and whose endpoint behavior is not forced into the screened termwise-positive class. Derive the exact pair statistic on an arbitrary finite conjugation-invariant complex multiset and seek a global Hilbert/operator inequality that lower-bounds the number of simple real points while allowing individual cross-height contributions to have either sign.

The candidate survives only if the deterministic inequality is valid without RH or a narrow-box assumption and the resulting BGSST asymptotic constant is strictly smaller than `C_MT`. If every such global inequality can be dualized or factorized back into Lamzouri's nonnegative one-factor class, record the corresponding no-go theorem.

For any proposed finite multi-profile SDP, first extract its dual certificate at the BGSST limiting moment point. If the dual is a fixed affine combination of the input moments, replace the SDP analytically by its signed effective scalar profile under `ANF-004`; do not count the matrix optimization itself as additional zero information. Only retain a matrix route when its counting step uses configuration-level operator structure before global moment compression.

## Evidence boundary

No signed support-one improvement, signed-profile no-go theorem, or genuinely configuration-level matrix certificate is established here. `ANF-004` proves only the affine/convex finite-global-moment reduction under its stated subgradient/duality hypotheses; it does not show that the resulting signed profile is impossible.

The `0.6792` semidefinite result assumes RH, and the contemporary multi-profile unconditional improvement mentioned in `ANF-002`/`WI-001` remains unaudited. If that proposal is a convex finite-global-moment certificate with ordinary strong duality, `ANF-004` predicts an equivalent signed scalar dual profile; that prediction is an audit diagnostic, not evidence that the external claim is correct or incorrect.

## Research disposition

Accepted and narrowed. Direct-sum vector features, constant PSD mixing, positive convex ensembles, and finite affine/convex aggregations of already-global BGSST pair moments are no longer treated as distinct information carriers. The immediate unresolved target is the **signed scalar support-one dual inequality**; genuinely configuration-level matrix structure remains a separate escape only when it survives before global scalar compression.