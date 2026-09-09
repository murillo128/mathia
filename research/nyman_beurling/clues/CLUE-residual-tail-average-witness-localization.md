---
id: CLUE-residual-tail-average-witness-localization
type: research-clue
status: resolved
origin: master-researcher
target_line: nyman_beurling
based_on:
  - research/nyman_beurling/findings/NB-004-fixed-semigroup-target-probes-admit-target-orthogonal-mellin-aliases.md
  - research/nyman_beurling/findings/NB-006-prime-log-recurrence-forces-a-superlogarithmic-mellin-probe-budget.md
  - research/nyman_beurling/findings/NB-007-full-harmonic-semigroup-defect-is-singular-off-the-target-line.md
---

# Can the actual residual expose a quantitatively large tail-average witness at a controlled index?

## Observation

NB-007 closes the infinite harmonic-defect question: the full sum is finite only on the target line. It is therefore too singular to serve as a stable finite certificate. Its useful finite statement is instead

\[
\mathcal E_X(h)\ge\frac{|c_n(h)-c_1(h)|^2}{4n}
\bigl(H_{\lfloor X/n\rfloor}-1\bigr),\qquad X\ge2n,
\]

where `c_n(h)=n integral_0^(1/n) h`, `H_j` is the harmonic sum, and `mathcal E_X(h)=sum_(m=2)^X ||(A_m^*-m^(-1/2)I)h||^2` in the canonical Bagchi space.

The supremum `Gamma(h)` in NB-007 does not specify where a useful witness occurs. Even a lower bound for that supremum is insufficient for a prescribed finite probe budget if the witnessing index escapes beyond the cutoff. NB-006 independently prevents replacing this issue by a uniform claim on arbitrary Mellin aliases.

## Research question

For the actual projection residual `r_N=e-P_(V_N)e`, with `d_N=||r_N||` and `c_1(r_N)=d_N^2`, can the canonical finite-section geometry force both witness amplitude and witness location? A concrete candidate is an independently specified index budget `B_N` and positive quantitative bound `kappa_N` such that

\[
\Gamma_{B_N}(r_N):=
\max_{1\le n\le B_N}\frac{|c_n(r_N)-d_N^2|^2}{n}
\ge\kappa_N d_N^2(1-d_N^2).
\]

The dependence of both quantities on `N` must be proved; defining `B_N` as the first successful witness index is not localization. This refines the residual-specific question in NB-007 rather than reopening infinite-defect rigidity or duplicating the accepted general target-aware Gram certificate.

## Why it may matter

A localized witness can be inserted into NB-007 before passing to a limit. If the candidate inequality holds, its finite bound gives, for `X_N>=2B_N`,

\[
\mathcal E_{X_N}(r_N)\ge
\frac{\kappa_N d_N^2(1-d_N^2)}4
\bigl(H_{\lfloor X_N/B_N\rfloor}-1\bigr).
\]

This makes the index cost visible. Any normalization by `log X_N` must retain the loss `log(X_N/B_N)/log X_N`; a witness at almost the full cutoff can erase the gain. A separate source-derived upper bound or other implication for `d_N` would still be needed for an approximation rate.

## Decisive test

Start from the target-augmented finite space `F_N^0=span(e,V_N) intersect e^perp`. For `0<d_N<1`, independently verify the projection identity

\[
z_N=\frac{r_N-d_N^2e}{d_N\sqrt{1-d_N^2}}\in F_N^0,
\qquad\|z_N\|=1.
\]

The candidate is then a lower bound for `Gamma_(B_N)(z_N)`. Construct the exact finite observation matrix of

\[
T_Bz=\left(\sqrt n\int_0^{1/n}z(x)\,dx\right)_{2\le n\le B}
\]

on `F_N^0`, using the full Hilbert norm, the actual target pairings, and the harmonic-interval tail indicators. Determine an explicit index range with quantitative conditioning, or find near-null directions for proposed ranges. A finite positive eigenvalue or eventual full rank is only a diagnostic: quantify its deterioration with `N` and retain the full tail norm. An `ell^2` singular-value bound for `T_B` must also pay the conversion to the maximum defining `Gamma_B`.

A bound on all of `F_N^0` would be sufficient but may be unnecessarily strong. If that broader test fails, use the actual normal equations `r_N perpendicular V_N` together with `r_N=e-v_N`, `v_N in V_N`. A near-null vector in the augmented space is not automatically a best-approximation residual. A counterexample to the residual-specific bound must satisfy these source restrictions, or a precisely stated and norm-certified near-optimal variant.

Use both existing controls. NB-007's two-shell unit vectors have their sole nonzero tail average at an arbitrarily late index; NB-006's Mellin aliases defeat finite harmonic probes. Check whether either control can survive projection into the admitted finite space and the residual constraints without losing its small observation defect. Do not assume that projection preserves the alias. If a useful localized bound survives, expose the additional upper estimate needed to change `d_N`, and compare that estimate with existing zero-sensitive approximation bounds before claiming an advantage.

## Evidence boundary

Sources were inspected through `8d3ded047405f07aa10140dd7baa7c036faa293b`; the destination must check their current claim and review state before use. No witness-localization bound, finite observation-matrix computation, Mellin-bandwidth restriction, or improved approximation rate is established here. The displayed finite implication is a test specification based on NB-007, not a new finding. Failure of a sufficient bound on the larger augmented space does not refute a residual-specific theorem, and failure to prove either bound is not a counterexample. Keep the existing accepted target-aware clue and the settled infinite-defect result unchanged.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/nyman_beurling/findings/NB-008-finite-nyman-residuals-have-an-explicit-lcm-scale-tail-average-witness.md]]

`NB-008` independently reconstructs the canonical harmonic-interval formula and proves the candidate with the explicit choices

\[
B_N=\operatorname{lcm}(2,3,\ldots,N)+1,
\qquad
\kappa_N=\frac1{4B_N^3}.
\]

It also uses the common-zero shell of the actual best residual to strengthen the finite witness to

\[
\Gamma_{B_N}(r_N)\ge\frac{1-d_N^2}{8B_N^3}.
\]

This resolves finite witness existence and location, but only at the lcm scale. Since `log lcm(1,...,N)=N+o(N)`, the guaranteed index budget is exponential and the resulting coefficient is exponentially small. The useful remaining question is therefore narrower: whether the projection normal equations or other source-specific target data force a **sub-lcm** witness at polynomial or otherwise asymptotically informative scale. No new approximation rate follows from the resolved clue.