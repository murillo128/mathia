# MI-015 — Terminal Nyman geometry separates volume, target access, fixed-rank state angle and realized leverage

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman geometry through [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md)--[NB-108](../../findings/NB-108-fixed-confluent-state-subspaces-remain-target-poor-after-full-backfill.md). No growing-rank multi-zero state-subspace or full Nyman-distance theorem is claimed.

NB-103--NB-105 identify the determinant-volume resource. After confluence, fixed-multiplicity volume is controlled by radial depth, and under a terminal natural-index budget `B` the optimal placement starts at the zero-ordinate scale and uses the budget completely. The irreducible volume coordinate is `L=2a log(B/G)`, with `a=Re(lambda_*)` and `G=max(1,|Gamma|)`.

NB-106 shows that volume does not finish target conversion. The Nyman target has a preferred origin in Paley--Wiener time, so moving the visible band toward the ordinate can preserve determinant volume while losing target mass. A second coordinate appears, `H=2ad log G`, with the sharp fixed-multiplicity frontier `H=log(1/theta)` for retaining a target-bearing fraction `theta` of the terminal volume.

NB-107 adds realized leverage. Backfilling the one-zero state through all earlier integer cells down to any fixed natural scale does not rotate its maximal direction toward the target, but the whole rank-one channel is not target-coercive: for every fixed `theta in (0,1]`, `sup_(eta>=theta) chi=1-theta+o(1)`.

NB-108 shows that this is not a rank-one accident. For every fixed confluent multiplicity, the terminal band gives a uniformly nondegenerate Laguerre Gram on the derivative/Jordan state span, while large Mellin frequency drives every fixed derivative-state target pairing to zero even after full backfill. The principal angle between the **entire fixed-dimensional state subspace** and the target therefore tends to `pi/2`. For any positive state update with that range, the same sharp Pareto law `sup_(eta>=theta) chi=1-theta+o(1)` survives.

The reusable geometry is now at least four-way. `L` measures radial resolution beyond the zero ordinate; `H` measures target access from the origin to that ordinate; fixed state rank determines whether the terminal Gram remains uniformly conditioned; and `eta` measures how much of the available state leverage the actual vector uses. Once a fixed-dimensional state subspace is asymptotically target-orthogonal, increasing its fixed multiplicity does not improve the leverage-target frontier.

The next genuinely different obstruction must therefore force the canonical Nyman residual to carry asymptotically full state leverage or enter **growing-rank / several-distinct-zero geometry** where the fixed-dimensional Laguerre conditioning and principal-angle argument no longer apply.

**Boundary.** NB-108 is fixed-rank. Its lower Gram bound may deteriorate with multiplicity, and it does not control a growing collection of distinct zero states, the fully Blaschke-deflated target pairing, the unseen tail beyond the finite window, or the full Nyman distance.