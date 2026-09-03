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
  - research/analytic_frontier/findings/ANF-006-local-ordered-gap-certificates-escape-global-pair-moment-ceiling.md
  - research/analytic_frontier/findings/ANF-007-two-point-local-gap-bridge-cannot-beat-montgomery-taylor.md
  - research/analytic_frontier/findings/ANF-008-improving-n-point-bridge-saturates-block-cap.md
  - research/analytic_frontier/findings/ANF-009-increasing-point-order-pressure-bridge-collapses-to-montgomery-taylor.md
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-118-termwise-positive-support-one-pair-kernels-are-screened.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can a signed support-one dual profile beat Montgomery--Taylor, and what is the verified ceiling of local configuration-level certificates?

## Observation

`ANF-002` shows that Lamzouri's conjugation-invariant Hilbert inequality converts the unconditional BGSST complex-difference pair-correlation formula into horizontal information about zeros. `ANF-003` closes common-translation vector features that are eventually compressed to one scalar Gram kernel, while `ANF-004` closes finite convex lifts whose zeta inputs have already been compressed to finitely many global scalar pair moments: at the BGSST limiting point such a certificate has an affine signed scalar dual witness.

`ANF-005` gives the first exact obstruction inside that signed affine normal form. For a universal certificate

\[
s(Z)\ge A|Z|-\sum_{z,s\in Z}F(z-s),
\]

with \(d=F(0)\) and normalization slack \(\delta=1+d-A\), one- and two-point configurations force

\[
\delta\ge0,\qquad F(x)\ge-\delta,\qquad F(iy)\ge1-\delta,
\]

a real double point forces \(d\ge1-\delta\), and large real multiplicities force every finite real translation Gram of \(F\) to be copositive. In the zero-slack case, the Carneiro--Chandee--Littmann--Milinovich extremal theorem recovers the Montgomery--Taylor floor throughout the full nonnegative support-one admissible class. For signed profiles, an unconditional improvement requires

\[
M(F)+\delta<m_{\rm MT},
\qquad
m_{\rm MT}=0.3274992963\ldots .
\]

`ANF-006` changes the status of the separate configuration-level branch. The Palomar-registered `teal-sea/zeta-lab` development proves an unconditional four-point local-gap certificate and its passage to zeta zeros entirely in Lean, giving

\[
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge0.6728470197666887\ldots
>0.6725007036794116\ldots .
\]

This does not contradict `ANF-004`: the local-gap method preserves ordered consecutive gaps, applies a nonlinear spectral defect to finite block Gram matrices, and performs pinching/shifted-block assembly before the final global scalar solve. Configuration-level second-order information is therefore a **demonstrated** escape from the global-pair-moment ceiling, not merely a hypothetical one.

`ANF-007` sharpens the local branch further: inside this exact bridge, two points can never beat Montgomery--Taylor, while the fully checked three-point theorem does. The first successful local object is therefore a triple of consecutive zeros, where two adjacent gaps and their sum must be compatible.

`ANF-008` removes another apparent optimization axis. For fixed local certificate `(n,c,p)`, if any admissible block size improves the baseline then `Phi_n` is strictly increasing in `m`, so the unique optimal integer block is the cap-saturating value

\[
m_{\max}=(n-1)+\left\lfloor1/c\right\rfloor.
\]

Equivalently, existence of any improvement is decided exactly by the single scalar gate at `m_max`. Thus block-size tuning after the finite certificate carries no independent zero information in this architecture.

`ANF-009` closes the equally natural point-count escalation. For every `n>=3`, every admissible instance of this exact `F/Phi_n` pressure bridge satisfies

\[
\Phi_n<H\frac{n}{n-1}=H+\frac{H}{n-1},
\]

while admissible constants approach `H` arbitrarily closely from below. Hence the optimal envelope tends exactly to `H` as `n->infinity`. Raising `n` can improve a small finite-order certificate, but it cannot preserve any fixed gain in this architecture; its maximum possible headroom is only `O(1/n)`.

`WI-118` still rules out the obvious support-one escape based on universal termwise nonnegativity because real-axis positivity forces Fourier-edge taper and screening.

## Research question

There are now two distinct unresolved questions.

First, in the **global affine signed** class, does there exist a BGSST-admissible real-even support-one kernel \(F\) and \(\delta>0\) satisfying the necessary universal constraints of `ANF-005` for which

\[
M(F)+\delta<m_{\rm MT},
\]

and, if such a candidate exists, can the corresponding global conjugation-invariant counting inequality be proved for arbitrary complex multisets? The cheapest first theorem remains to decide whether the finite-configuration constraints already imply \(M(F)+\delta\ge m_{\rm MT}\).

Second, in the now-established **local configuration-level** class, what modification of the information carrier can escape the structural collapse of the current pressure family? `ANF-008` shows that `m` is forced once `(n,c,p)` is fixed, and `ANF-009` shows that `n->infinity` in the unchanged bridge returns to `H`. The live variables are therefore genuinely new local compatibility or memory, a different nonlinear defect, window or pressure accounting, or a different analytic bridge -- not simply larger blocks or more points inside the same `F/Phi_n` architecture.

The second question should not be replaced by simply quoting larger interval-search candidates. An eight-point bridge with a named `hCert`, or a larger externally certified finite search that has not been independently replayed in the current evidence chain, is a candidate input rather than an unconditional theorem of the same formal status.

## Why it may matter

A signed support-one profile with \(M(F)+\delta<m_{\rm MT}\) and a valid universal counting inequality would improve the unconditional simple-critical proportion while staying inside global support-one pair correlation. Conversely, a no-go theorem at \(m_{\rm MT}\) would combine `ANF-003`--`ANF-005` and `WI-118` into a broad exhaustion result for universal affine global second-order certificates.

The local-gap branch is already known to beat that baseline, so its value is different. It supplies a concrete example of **information preserved by delaying compression**. But `ANF-007`--`ANF-009` now show that the present pressure architecture has three built-in limits: isolated one-gap information is insufficient, scalar block length carries no independent optimization once the certificate is fixed, and unlimited point order has vanishing headroom. Understanding the next verified gain therefore means identifying an information carrier that changes one of those structural facts.

## Decisive test

For the signed scalar branch, solve or sharply bound the constrained extremal problem from `ANF-005`. Normalize a real-even BGSST-admissible support-one kernel \(F\), introduce the smallest \(\delta\) compatible with

\[
F(x)\ge-\delta,\qquad F(iy)\ge1-\delta,
\]

and impose the copositivity conditions already derived. A rigorous lower bound \(M(F)+\delta\ge m_{\rm MT}\) rejects the universal affine signed route; an explicit strict sub-Montgomery--Taylor candidate only passes the cheap falsifier and must still survive the full counting inequality.

For the configuration-level branch, first apply `ANF-008`'s exact gate to any proposed `(n,c,p)` certificate and use `m_max`. Then apply `ANF-009`: if the proposal keeps the same registered `F`, cap and `Phi_n` and relies only on increasing `n`, any claimed fixed asymptotic gain is impossible before certificate search begins. A surviving direction must alter the local functional or the bridge itself and then supply an evidence-matched finite inequality plus a complete passage to `riemannZeta` at the claimed trust tier.

Any proposed finite multi-profile SDP must still have its dual extracted before being treated as new information. If it only consumes finitely many already-global BGSST moments, `ANF-004` reduces it to the scalar signed problem. It belongs to the configuration-level branch only if order, matrix spectrum/inertia, local block structure, or genuine finite memory is used before global compression.

## Evidence boundary

No signed support-one improvement and no complete signed-profile no-go theorem is established. `ANF-005` gives necessary constraints and an exact slack tradeoff, not a solution of the constrained extremal problem.

`ANF-006` establishes that one particular local configuration-level mechanism beats the Montgomery--Taylor baseline at the fully checked four-point level. `ANF-007` establishes the minimal point count inside the same bridge, `ANF-008` the forced block-size optimization, and `ANF-009` only the asymptotic `n`-order ceiling for that exact pressure family. None is a ceiling for richer Bellman/coboundary, altered-window, multi-profile or otherwise modified pre-compression methods. In particular, the registered eight-point theorem retains `hCert`, and later larger research-draft candidates depend on external finite certificates or broader imported trust boundaries that this watch has not promoted to the same formal-evidence tier.

## Research disposition

Accepted and narrowed. The scalar signed branch remains an extremal/no-go problem around \(M(F)+\delta\). The configuration-level branch has now passed four structural filters: local processing can beat the global pair-moment ceiling (`ANF-006`), two points are insufficient (`ANF-007`), block size is forced once a current-bridge local certificate is fixed (`ANF-008`), and increasing point order without changing the bridge has optimal envelope tending back to `H` (`ANF-009`). The remaining frontier is a genuinely richer local information carrier or bridge, not scalar `m` tuning or point-count escalation.