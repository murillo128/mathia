# MI-006 — Normalized odd Schur stability is the correct Lamzouri screening carrier; source coercivity remains the gate

**Evidence level:** supported by WI-115--WI-132, with exact periodic/grouped controls and literature-backed zeta source inputs in the stated regimes

## Core intuition

Pre-scalar Hilbert geometry really does charge off-real directions, but the correct quantitative carrier is subtler than the singular spectrum of the raw exponential/Vandermonde system. Growing-period screening can force a macroscopic raw near-null sector, yet the same raw collapse can arise from harmless confluent center pairs while the actual Lamzouri anti-invariant quotient remains uniformly transverse.

WI-132 now isolates the right normalized invariant. Dividing each odd conjugate-pair direction by its horizontal depth removes the unavoidable vanishing as the pair approaches the critical line and turns it into an exact exponential divided difference. The resulting Schur-complement Gram matrix measures genuine screening modulo the complete retained even/real space.

## Strongest justified principle

WI-115--WI-127 establish the base screening/coercivity picture. Support-one scalar data admit screening aliases; independent zeta moment input excludes some long density extremizers; mirror symmetry forces lower-half reciprocal leakage; and Lamzouri's Hilbert proof contains an exact nonnegative horizontal remainder

`R_H >= 4 sum m_z dist(h_z,V)^2`.

For a fixed simple periodic cell with distinct reciprocal roots, WI-127 makes this charge extensive under repetition.

WI-128 strengthens the growing-period necessary condition. If a positive density of bounded-depth off-line pairs has subextensive normalized horizontal remainder, then a positive-density bottom tail of the normalized raw reciprocal-node Vandermonde must collapse in mean square. One bad singular direction is not enough.

WI-130 shows why that raw tail is not the discriminator. A density-one family with nearby same-sign pair centers can make the entire bottom half of the raw Vandermonde spectrum collapse while the Lamzouri `g/h` quotient stays transverse and pays extensive horizontal slack. Raw ill-conditioning can therefore encode confluent parametrization rather than horizontal screening.

WI-131 removes the parallel shortcut through real projections. The conjugate lattice `2n+/-ib` gives an explicit complex exponential Riesz basis although the real projections duplicate and are nonminimal. Conjugation symmetry and projected collisions do not by themselves destroy complex scalar stability; clustered systems naturally require grouped/vector-valued or divided-difference coordinates.

WI-132 converts that correction into an exact target. For `z_j=x_j+i y_j`, define the normalized odd divided differences

`u_j=h_{z_j}/y_j=(f_{z_j}-f_{bar z_j})/(z_j-bar z_j)`

and let

`S=U^*(I-P_V)U`, `a=lambda_min(S)>0`.

Then Lamzouri's finite inequality sharpens to

`n >= 2N-Q + 4 a D_2`,  where `D_2=sum_j m_j y_j^2`.

Hence if the Lamzouri baseline is asymptotically sharp while `D_2` remains a positive proportion of `N`, necessarily `a -> 0`. Near-extremal screening with macroscopic off-line square depth must create a genuinely anti-invariant grouped near-null direction after the trivial depth factor has been divided out. A lower Riesz bound for the full normalized conjugation-adapted family is sufficient, but stronger than necessary; `S` is the sharper object.

## Evidence synthesis and boundaries

These results still do not give an unconditional zeta percentage improvement. There is no source-uniform lower bound for `a`, and the square-depth mass can itself vanish if exceptional zeros approach the critical line. Multiplicity, irregular growing configurations, and an arbitrary surrounding reservoir also remain part of the source-transfer problem.

What is closed is the idea that raw Vandermonde conditioning or real-projection collisions are faithful proxies for the horizontal Lamzouri charge. A decisive theorem must control the normalized odd Schur quotient itself, or derive zeta source information strong enough to force either `D_2=o(N)` or a positive lower bound for the relevant Schur spectrum.

## Status / novelty

Vandermonde singular values, Eckart--Young, fiberization, Riesz bases, exponential divided differences, and Schur complements are classical tools. The persisted synthesis is the carrier correction: **horizontal zero information lives in a depth-normalized anti-invariant quotient, and the exact product `a D_2` is the coercive quantity exposed by Lamzouri's slack**.

## Falsification criterion

Construct a configuration satisfying the WI-132 hypotheses with macroscopic `D_2`, asymptotically sharp Lamzouri baseline, and `a` bounded away from zero. A source theorem forcing such a lower bound would instead yield the desired positive advance by charging off-line square depth.

## Lean-formalizable core

- Bottom-singular-tail lower bound from a rank-`k` Schur residual.
- Confluent raw-Vandermonde collapse construction.
- Depth-normalized odd divided differences.
- Exact `n >= 2N-Q+4aD_2` Schur/slack inequality.
