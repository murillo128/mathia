# MI-015 — Terminal Nyman geometry has separate volume, target-access and state-leverage currencies

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman geometry through [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md)--[NB-107](../../findings/NB-107-one-zero-backfill-has-a-sharp-leverage-target-pareto-frontier.md). No growing-multiplicity, multi-zero state-subspace or full Nyman-distance theorem is claimed.

NB-103--NB-105 identify the determinant-volume resource. After confluence, fixed-multiplicity volume is controlled by radial depth, and under a terminal natural-index budget `B` the optimal placement starts at the zero-ordinate scale and uses the budget completely. The irreducible volume coordinate is

`L=2a log(B/G)`,

with `a=Re(lambda_*)` and `G=max(1,|Gamma|)`.

NB-106 shows that volume does not finish target conversion. The Nyman target has a preferred origin in Paley--Wiener time, so moving the visible band toward the ordinate can preserve determinant volume while losing target mass. A second coordinate appears,

`H=2ad log G`,

with the sharp fixed-multiplicity frontier `H=log(1/theta)` for retaining a target-bearing fraction `theta` of the terminal volume. The actual maximal one-zero causal state is even more target-poor at natural ordinate start despite nonzero leverage.

NB-107 tests the obvious cross-scale repair and finds a third currency. Backfilling the one-zero state through **all** earlier integer cells down to any fixed natural scale does not rotate its maximal state direction toward the target: the normalized target correlation still tends to zero. But the whole rank-one channel is not target-coercive. If `eta(f)` is the fraction of maximal one-zero state gain and `chi(f)` the visible target occupation, then for every fixed `theta in (0,1]`,

`sup_(eta(f)>=theta) chi(f)=1-theta+o(1)`.

Thus target-poorness is forced only as the state-leverage fraction tends to one. A vector may retain any fixed fraction below full leverage and asymptotically keep the complementary target fraction. A large maximal generalized eigenvalue and a target-poor maximizer therefore do not imply a coercive target obstruction.

The reusable geometry is now at least three-dimensional. `L` measures resolution beyond the zero ordinate; `H` measures target access from the origin to that ordinate; and `eta` measures how much of the available one-zero state leverage the actual vector uses. Earlier cells can restore ambient target mass without repairing the maximal state direction, while submaximal state directions can trade leverage back for target occupation exactly.

The next genuinely different obstruction must force the canonical Nyman residual to carry asymptotically full state leverage, or replace the rank-one geometry by a multi-zero/growing-rank state subspace whose principal angles with the target are quantitatively coercive.

**Boundary.** NB-107 is a single-zero rank-one statement. It does not control the principal angles of a multi-zero state subspace, the fully Blaschke-deflated target pairing, the unseen tail beyond the finite window, or the full Nyman distance. Its Pareto formula shows precisely why none of those conclusions follows from the maximal one-zero eigenvalue alone.