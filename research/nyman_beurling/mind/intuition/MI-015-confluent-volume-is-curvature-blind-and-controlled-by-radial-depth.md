# MI-015 — Terminal Nyman geometry has separate volume and target-access depths

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman geometry through [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md)--[NB-106](../../findings/NB-106-terminal-volume-retention-has-a-sharp-target-access-frontier.md). No growing-multiplicity or full Nyman-distance theorem is claimed.

NB-103--NB-105 identify the determinant-volume resource. After confluence, fixed-multiplicity volume is controlled by radial depth, and under a terminal natural-index budget `B` the optimal placement starts at the zero-ordinate scale and uses the budget completely. The irreducible volume coordinate is

`L=2a log(B/G)`,

with `a=Re(lambda_*)` and `G=max(1,|Gamma|)`.

NB-106 shows that this does **not** finish target conversion. The Nyman target has a preferred origin in Paley--Wiener time, so moving the visible band toward the ordinate can preserve determinant volume while losing target mass. A second coordinate appears:

`H=2ad log G`.

If a band must retain a fraction `theta` of the maximal fixed-multiplicity volume, then the exact continuum frontier is `H=log(1/theta)`. Above that threshold by a positive amount, every such band is forced into an exponentially target-poor tail. Below it, a band beginning at the target origin can retain the requested volume fraction. Thus scaled placement uniqueness near `G` does not imply ordinary-index target exclusion when `a log G` is small.

For the actual one-zero causal state at the natural ordinate start, the loss is stronger: with fixed terminal depth `L`, the normalized target energy is of order `a/G^3`, even though the leverage tends to the nonzero quantity `e^L-1`. Large local state volume and target occupation are therefore quantitatively different resources.

The reusable geometry is now two-dimensional. `L` measures resolution **beyond** the zero ordinate; `H` measures scaled depth **from the target origin to** that ordinate. Any terminal-volume obstruction must cross both gates, or explicitly use cross-scale cooperation with earlier cells. Determinant volume alone cannot force target loss below the `H` threshold.

**Boundary.** The sharp frontier applies to fixed multiplicity and terminal-band target mass. The actual approximant may combine earlier cells with the terminal band, and the one-zero `a/G^3` estimate is not yet a theorem for repeated-zero Jordan packets or growing multiplicity.