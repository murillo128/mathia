---
id: CLUE-montgomery-taylor-six-point-curvature-deficit-screening
type: research-clue
status: proposed
origin: research-watch
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-030-montgomery-taylor-extremizer-forces-palm-zero-set-rigidity.md
  - research/analytic_frontier/findings/ANF-059-exact-montgomery-taylor-curvature-transform-shrinks-the-five-point-separation-annulus.md
  - research/analytic_frontier/findings/ANF-066-certified-curvature-convexity-completes-two-branch-montgomery-taylor-near-extremizer-stability.md
  - research/analytic_frontier/findings/ANF-068-montgomery-taylor-affine-slack-screens-six-point-infinitesimal-collapse-reversal.md
  - research/analytic_frontier/findings/ANF-069-one-pair-collapse-reversal-is-curvature-seeded-through-ten-points.md
---

# Screen the complete six-point reversal branch with the certified spatial floor

## Observation

Independent compute execution of [issue #126](https://github.com/murillo128/mathia/issues/126) supplies the rigorous interval certificate missing from ANF-069 (37). With the exact ANF-030/ANF-059 definitions

\[
G(t)=\frac{\cos(\pi t)-\sqrt2\,\pi\cot(1/\sqrt2)t\sin(\pi t)}{1-2\pi^2t^2},
\quad F_{\rm MT}=G^2,\quad K=-\frac{(G^2)''}{4\pi^2},\quad K_0=K(0),
\]

the complete rational cover of `[109/200,101/100]` certifies

\[
Q(t):=8F_{\rm MT}(t)+K(t)+K_0/3>\varepsilon,
\qquad \varepsilon=\frac{5246646}{10^9}=0.005246646.
\]

The computation used Python 3.12.3, python-flint 0.8.0 / FLINT 3.3.1, interval-valued transcendental constants, and explicit quotient derivatives of `G`. It visited 21 rational cells, accepted 11 leaves, and left zero unresolved cells. Every accepted leaf closed at 128 bits; unresolved parents were reevaluated at 256 and 512 bits before subdivision. The declared limits were 100,000 cells and depth 20; maximum used depth was 5. The smallest enclosure lower endpoint exceeded `0.00524664647179411988`. This is a conservative cover bound, not the minimum of `Q`. A fresh fertility audit independently replayed all leaves with Arb power-series differentiation. The issue discussion contains the compact executable certificate, exact rational partition, and arithmetic consequences; the source revision is `ff2e979e833963cef516d59f91182a35e2a3d71f`.

Evenness and the inherited ANF-059 exterior estimate therefore give the global computer-assisted inequality

\[
\boxed{F_{\rm MT}(t)\ge\frac18 r(t)\quad(t\in\mathbb R),
\qquad r(t)=(-K_0/3-K(t))_+.}
\]

For four simple real anchors, put `D(T)=2K_0+sum_j K(t_j)` and `k_*=min_R K`. Substituting this floor into ANF-069 (34) gives affine slack greater than `143/100000` throughout the base-profile one-pair/four-simple-real-anchor collapse-reversing branch. This follows by minimizing the concave quadratic

\[
\frac{k}{3}+\frac{x}{2}-\frac{3x^2}{2m}\quad(0\le x\le d),
\quad k=0.1549985926411760,\quad d=0.055099459323598,
\quad m=0.05854458579969,
\]

where `x=-D(T)` and the three decimal bounds are exact rationals inherited from ANF-069. Both endpoints exceed `143/100000`.

The audit also recovered information discarded by reducing the certificate to `Q>=0`. Negative `D(T)` forces at least three anchors to have `r(t_j)>0`: otherwise `D(T)>=(2/3)(2K_0+3k_*)>0`. For each active anchor, `F_MT(t_j)>r(t_j)/8+epsilon/8`. The collapsed slack consequently gains `3epsilon/2`, giving the stronger derived floor

\[
\mathcal S_{\rm MT}(W_{y,T})>\frac{93}{10000}
\qquad(D(T)<0,\ y>0).
\]

## Research question

Can the certified spatial floor and its retained surplus close the entire base-profile six-point reversal branch and extend ANF-068's notch screening from a small-height neighborhood to that complete branch?

The precise proposed extension is: for the admissible central tent of ANF-068, with `0<eta<1`, `0<s<=1`, `J_s=J_MT-s phi_eta`, and intercept `A_s=2-2s b_eta eta`, does

\[
s b_\eta\eta\le\frac{93}{1600000}
\quad\Longrightarrow\quad
\mathcal S_s(W_{y,T})>\frac{93}{20000}
\]

hold uniformly over every configuration whose **base Montgomery–Taylor profile** reverses real collapse?

## Why it may matter

ANF-069 proves that every such reversal is curvature-seeded and has `y<0.267431`; the spatial floor was its explicit remaining scalar gate. Closing that gate screens the complete base reversal mechanism with a fixed margin, including horizontally escaping anchor families. A uniform notch splice would narrow the remaining six-point obstruction to configurations outside this base reversal branch.

## Decisive test

Independently reconstruct the issue's finite certificate and ANF-069 (28)–(34), including ordered-pair multiplicities and the active-deficit argument. Check the exact rational quadratic endpoint bounds. Then apply ANF-068 (26)–(28) on the actual reversing branch, where ANF-069 bounds the height. The same outward-rounded arithmetic certifies

\[
\left(2\cosh(2\pi\cdot0.267431)+4\right)^2-12<80.
\]

Thus the proposed notch loss is at most `80 s b_eta eta`; the displayed parameter bound leaves `93/20000` of the strengthened margin. Audit admissibility and intercept conventions before promoting this consequence to a finding. A defect in the exterior threshold, spatial certificate, affine multiplicity factors, or notch identity kills the corresponding implication.

## Evidence boundary

The new scalar evidence is an exhaustive rigorous Arb certificate, not dense sampling. The global floor inherits ANF-059's exterior certificate; the affine and notch consequences additionally use the persisted analytic reductions. The proposed clue has not undergone Research Watch acceptance, canonical derivation, or its prior-art gate. No optimal spatial constant or minimizer is claimed. The notch question covers only the base-profile reversing branch and does not establish the complete notched six-point inequality, configurations with multiple nonreal pairs, other spectra, a universal affine inequality, or RH.
