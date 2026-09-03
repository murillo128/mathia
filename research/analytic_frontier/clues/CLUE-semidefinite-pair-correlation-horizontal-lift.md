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
  - research/analytic_frontier/findings/ANF-005-signed-affine-pair-certificates-pay-normalization-slack.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can a signed support-one dual profile or genuinely configuration-level matrix lift beat Montgomery--Taylor unconditionally?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality converts the existing unconditional BGSST complex-difference pair-correlation formula directly into a lower bound for zeros that are simultaneously simple and on the critical line. `WI-118` rules out the obvious support-one escape based on universal termwise nonnegativity because real-axis positivity forces Fourier-edge taper and screening.

`ANF-003` closes common-translation vector features that are eventually compressed to one scalar Gram kernel: feature multiplicity, constant PSD mixing, and positive convex averaging do not add information beyond one scalar spectral density. `ANF-004` closes a broader interpretation of finite convex “jointness”: any affine combination of already-global BGSST pair moments is one signed scalar support-one profile, and a convex lower-bound aggregator with a supporting hyperplane at the BGSST limiting point has an equally strong affine signed dual witness there.

`ANF-005` now supplies the first exact obstruction inside that signed affine normal form. For any universal certificate

\[
s(Z)\ge A|Z|-\sum_{z,s\in Z}F(z-s)
\]

on all finite conjugation-invariant multisets, with `d=F(0)` and normalization slack

\[
\delta=1+d-A,
\]

one- and two-point configurations force

\[
\delta\ge0,\qquad F(x)\ge-\delta,\qquad F(iy)\ge1-\delta,
\]

and a real double point forces `d>=1-delta`. Large real multiplicities further force every finite translation Gram of `F` to be copositive. In the zero-slack case `delta=0`, `F` is nonnegative on the real axis; Corollary 14 of Carneiro--Chandee--Littmann--Milinovich then applies to the full nonnegative support-one admissible class and recovers the exact Montgomery--Taylor floor.

For a BGSST-legal signed kernel, the same bookkeeping gives the quantitative improvement condition

\[
M(F)+\delta<m_{\rm MT},
\qquad
m_{\rm MT}=C_{\rm MT}-1=0.3274992963\ldots.
\]

Thus sign changes are not a free escape: any deterministic allowance for negative pair values costs exactly the slack `delta` in the final simple-critical bound. The unresolved question is whether the pair-correlation functional can fall by *more* than this compulsory loss while all finite-configuration constraints remain satisfied.

There is established evidence that broader auxiliary-function information can improve pair-correlation bounds when RH is assumed. Chirre--Gonçalves--de Laat enlarge the usual bandlimited class to a Cohn--Elkies sign class and optimize it by semidefinite programming, obtaining the `1.3208` multiplicity constant and `0.6792` simple-zero proportion under RH. That gain relies on a real-ordinate pair-correlation framework and an out-of-band sign argument, so it is not yet an unconditional complex-zero certificate.

## Research question

Does there exist a BGSST-admissible real-even support-one kernel `F` and `delta>0` satisfying the necessary universal affine constraints from `ANF-005` for which

\[
M(F)+\delta<m_{\rm MT},
\]

and, beyond those necessary tests, can one prove the corresponding global conjugation-invariant counting inequality for arbitrary complex multisets?

The immediate scalar problem is now an extremal one rather than a generic search for “more features.” Determine whether the finite-configuration constraints alone already imply `M(F)+delta>=m_MT`. If they do, the universal affine signed support-one route is closed. If an explicit strict sub-Montgomery--Taylor candidate survives them, only then is it worth attacking the harder Hilbert/operator proof of the full counting inequality.

A separate surviving branch is genuinely configuration-level matrix information: an operator-valued or multi-observable construction in which matrix order, eigenvalues, inertia, or local block structure is used **before** the zero configuration is compressed to finitely many global scalar pair sums. Such a mechanism lies outside the `ANF-004` dual reduction and the affine scalar setup of `ANF-005`.

## Why it may matter

A valid signed support-one certificate satisfying `M(F)+delta<m_MT` would immediately improve the unconditional `0.6725007...` simple-critical proportion without requiring wider Fourier support or unproved higher prime correlations. More importantly, it would identify the exact second-order information hidden by positive-kernel formulations: controlled signed cancellation whose analytic gain exceeds its unavoidable deterministic normalization cost.

Conversely, a no-go theorem for the constrained extremal problem would combine `ANF-003`, `ANF-004`, `ANF-005`, and `WI-118` into a broad exhaustion result for universal affine support-one second-order certificates. That would redirect the line sharply toward wider support, finite-`T` joint fluctuation information, genuinely configuration-level matrix structure, or higher-order correlations.

## Decisive test

Solve or sharply bound the necessary scalar extremal problem first. Normalize a real-even BGSST-admissible support-one kernel `F`, introduce the smallest `delta` compatible with

\[
F(x)\ge-\delta,\qquad F(iy)\ge1-\delta,
\]

and require copositivity of every finite real translation Gram as derived in `ANF-005`. Determine whether the infimum of `M(F)+delta` under these constraints is at least `m_MT`.

A rigorous lower bound at `m_MT` rejects the universal affine signed branch without needing to invent a new counting proof. An explicit candidate below `m_MT` does not establish a zeta result, but it survives the cheapest deterministic falsifiers and justifies the next stage: prove or disprove the full affine simple-real inequality on arbitrary conjugation-invariant complex multisets.

For any proposed finite multi-profile SDP, extract its dual at the BGSST limiting point before treating it as new information. If the dual is a fixed affine combination of the legal moments, reduce it to the scalar `F,delta` problem above. Retain a matrix route only when its counting step uses configuration-level operator structure before global moment compression.

## Evidence boundary

No signed support-one improvement, complete signed-profile no-go theorem, or genuinely configuration-level matrix certificate is established here. `ANF-005` proves necessary finite-configuration constraints and the exact slack tradeoff; it does not prove those conditions sufficient for a universal counting inequality and does not yet solve the constrained extremal problem.

The `0.6792` semidefinite result assumes RH, and the contemporary multi-profile unconditional improvement mentioned in `ANF-002`/`WI-001` remains unaudited. If that proposal is a convex finite-global-moment certificate with ordinary strong duality, `ANF-004` predicts an equivalent signed scalar dual profile and `ANF-005` predicts the normalization slack that profile must pay; these are audit diagnostics, not evidence that the external claim is correct or incorrect.

## Research disposition

Accepted and narrowed. The scalar branch is no longer “find any signed support-one profile.” Its first unresolved theorem is the constrained extremal inequality `M(F)+delta >= m_MT` versus an explicit counterexample under the one-/two-point, imaginary-axis, and copositivity constraints of `ANF-005`. Genuinely configuration-level matrix structure remains a separate escape only when it survives before global scalar compression.