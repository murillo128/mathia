# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Control the explicit Burnol-scale skeleton defect rather than treating the early-shell model as an oracle

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-036 build a weighted moving-tail quotient that preserves source coordinates and has polynomial conditioning independent of the discarded upper section. NB-037--NB-038 show that the true retained Gram and target-correlation corrections are forced at the Burnol scale `d_N^2`, with one explicit Möbius/Vasyunin direction already carrying a multiplicatively accurate copy of the original distance.

NB-039 makes the compression threshold itself sharp. The nuisance tail contains a dilated copy of a smaller canonical Nyman section, giving

`(1-d_floor(N/M)^2)/M <= kappa_hat_(M,N)^2-d_N^2 <= 1/M`.

For `N>=2M` the additive loss is therefore `asymp 1/M`, and multiplicative preservation holds exactly when `M d_N^2 -> infinity`. The familiar superlogarithmic cutoff is an unconditional sufficient condition and, under the expected `d_N^2 asymp 1/log N`, order-necessary for this quotient. At the same time, the explicit Burnol/source defect can already be seen under the weaker adaptive condition involving `d_floor(N/M)`.

The live theorem is thus not to improve conditioning or pretend the `1/M` loss can be squeezed away inside this skeleton. It is to control the explicit Burnol-scale directional defect from source information genuinely cheaper than the Nyman distance itself, or to construct a materially different quotient whose target-loss floor changes for a mathematical reason rather than by reparameterization.

## Treat representation compression, target-loss floor, and oracle cost as separate gates

The weighted skeleton is a good representation: source-faithful and conditioned. Its target loss is nevertheless intrinsically `Theta(1/M)`, and the correction needed to recover the true geometry carries the original distance scale. Future compression claims should price all three quantities separately rather than infer source progress from low dimension or conditioning alone.
