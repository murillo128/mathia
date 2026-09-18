# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Determine what survives after the fixed-source field energy diagonalizes through `L^-2`

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-036-a-uniform-theorem-exponent-can-disappear-after-specializing-to-the-physical-source-regime`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The fixed-source representation audit has removed the apparent generic `L^-3/2` frontier from every direct sector inspected so far. VIS-271--VIS-278 identify the theorem/source coordinate mismatch, reconstruct the gamma-normalized source and show that its invariant residual has positive prime-power energy `C_Lambda` entering only at `L^-2`. VIS-279--VIS-281 then show that the direct `D_x--E_x` envelope, the `D_x--B_x` cross and the zero-window localization loss all fall to `L^-2` or below after specializing to compact physical source before rescaling.

VIS-282 resolves the formerly anonymous `O(H)` Dirichlet mean square. At fixed source,

`int_I |D_x(t)|^2 dt = H S_D(x)+O_K(1)`,

where

`S_D(x)=x^(-2) sum_(n<=x)n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`.

The profile has explicit derivative jumps `-4 Lambda(m)^2/m^2` at prime powers, so the coefficient-scale `L^-2` term contains deterministic arithmetic structure rather than merely theorem error.

VIS-283 closes the signed recombination question left by VIS-282. After reconstructing `S_x=B_x+E_x`, the arithmetic residual `zeta'/zeta(3/2-it)` has the wrong temporal-frequency orientation to resonate with `D_x`: the product frequencies are `-log(mn)`, not differences, so there is no zero-frequency diagonal. Consequently

`int_I D_x overline(E_x) dt = O_K(1)`,

and the complete prime/source cross is only `O_K(L)` because of the slowly varying classical gamma baseline. After the fixed-`q` pullback and pair-statistic normalization that cross is `O_K(1/(HL))`, hence power-small.

Through constant field-energy order the fixed-source decomposition is therefore diagonal:

`(1/H) int_I |A(x,t)|^2 dt = S_D(x) + x^(-2)[log(T/(2*pi))^2 + C_Lambda] + o_K(1)`.

Keeping the exact gamma baseline intact leaves the positive coefficient-scale arithmetic profile

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

There is no equal-scale signed prime/source cross available to cancel this profile before packet projection. The prime-power kinks of `S_D` survive the field-level recombination.

The live question has moved one stage later. Determine how the actual admissible packet/test projection acts on `Q_gamma(e^(2*pi q))`, and audit any remaining theorem-level truncation or replacement sector that could still exceed `L^-2`. If the packet projection preserves a nontrivial component of `Q_gamma`, identify the exact arithmetic functional it measures. If it annihilates the profile, explain the cancellation as a property of the destination test rather than as hidden source interference. Any claimed intrinsic `L^-3/2` term must now be exhibited in a specific remaining sector.

## Keep packet conditioning, arithmetic selectivity, theorem coordinates and parameter-uniformity separate

The current ledger separates moving-test seminorm cost, prime-power support, normalization gauge, physical source scale, sign/covariance retention and temporal-frequency orientation. VIS-283 adds a new hard distinction: two individually `L^-2`-sized diagonal sectors need not admit an `L^-2` cross term when their Fourier supports cannot resonate. A future probe should preserve exact source structure through the physical pullback and only then project or majorize it.