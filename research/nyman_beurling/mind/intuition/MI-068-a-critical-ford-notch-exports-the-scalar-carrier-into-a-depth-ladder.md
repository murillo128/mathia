# MI-068 — A critical Ford notch exports the scalar carrier into a depth ladder

**Evidence level:** proven within the `H`-resolved scalar carrier model by [NB-260](../../findings/NB-260-critical-depth-cancellation-leaves-a-polynomial-depth-ladder-and-a-shallower-matched-ford-packet.md), refining the critical-cell escape of NB-259. The matched packet is an admissible control against the currently imported zeta-information ledger, not a claim that actual zeta zeros realize that packet.

Let the legal critical zero layer lie at imaginary Ford height `A_J=Theta(log J)` and define the effective depth resolution

`N_J=J/A_J ~ J/log J`.

For a bounded shell-Hilbert-cost carrier with `C_J(0)=1`, if `K<=N_J^(1-delta)` for fixed `delta>0`, some fixed derivative of the rescaled depth profile `D_J(s)=C_J(isA_J)` tends uniformly to zero. Hence `D_J` is asymptotically a fixed-degree polynomial with value one at `s=0`, and every fixed interval `I subset (0,1]` retains a positive `L^2` floor. Suppressing a positive fraction of the whole depth ladder therefore requires

`K >= N_J^(1-o(1))`.

At the cheaper NB-259 crossover `K~N_J^(2/3)`, an exact critical notch `D_J(1)=0` is even more rigid:

`D_J(s)=1-s+o(1)` uniformly on `[0,1]`.

The notch is therefore an affine ramp rather than a broad suppression mechanism. For every fixed `theta<1/6`, NB-260 constructs a carrier-locked matched packet at depth `X(1-beta)=theta log J` with `Theta(J^theta)` points that remains compatible with the same zero-free, density and local-count information used by the line, while its signed Hardy-projected residue contribution stays bounded away from zero. The critical notch exports order-one mass to a shallower admissible layer.

The durable consequence is that **single-cell cancellation is not the correct scalar destination currency**. A surviving obstruction must control a genuinely two-dimensional region: near-full effective depth resolution together with the hard Ford ordinate width `Theta(J)`, or else use a different legal Hardy/Nyman quantity that couples those directions before cancellation can migrate between them.

**Boundary.** The near-full depth-rank requirement is necessary only for the resolved scalar signed carrier with bounded shell-Hilbert cost and exact Euler normalization; it is not a lower bound on the total number of terms in an arbitrary Nyman approximant. The `theta<1/6` packet range is a proof range, not an intrinsic threshold. Vector-valued, unresolved-overlap, or differently projected constructions remain outside the statement.