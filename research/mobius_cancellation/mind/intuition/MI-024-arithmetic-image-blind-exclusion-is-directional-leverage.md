# MI-024 — Arithmetic-image leverage reduces to near-injectivity, affine bias, or exponentially small effective occupancy

**Evidence level:** exact variational/certificate reduction from MC-281, sharpened through MC-282, MC-284--MC-288 and [MC-289](../../findings/MC-289-weighted-odd-moment-character-bias.md). The Geelen step is established finite-geometric prior art; the weighted odd-moment step is exact finite Fourier algebra. No theorem is claimed that the desired Christoffel certificate exists for the actual shell.

For feature matrix `A` on the actual arithmetic shell and blind row `v`, endpoint-normalized energy is directional synthesis cost, not generic nonblindness. Moderate-conductor Legendre shadows can already be Boolean-complete, yet favorable endpoint leverage still requires stronger geometry.

For odd target weight `t`, MC-286 identifies the exact affine obstruction: failure of an odd zero-sum row can place the occupied shell in an affine hyperplane, equivalently giving one generated product character constantly `-1`. MC-288 shows that in the collision-rich branch, absence of the target row forces odd girth greater than `t`; Geelen then gives either that affine obstruction or support density at most `(t+2)/2^(t+1)` in the support's own span.

MC-289 makes the surviving non-affine branch multiplicity-sensitive. If `n_s` are shell multiplicities and

`eta = N^2/(2^r sum_s n_s^2)`,

then vanishing of every odd convolution at zero through order `t` gives exact odd Fourier moments. Combined with Parseval, they force a nontrivial generated character with

`A_lambda/N <= -(eta/(1-eta))^(1/(t-2))`.

Hence a collision-rich target failure with no substantial negative character bias is possible only when `eta` is exponentially small in `t`. At the Geelen-scale occupancy with reasonably flat multiplicities, the forced negative bias is order one (`-1/2+o(1)` at `eta~t2^-t`).

The arithmetic target is therefore sharper than a raw occupancy theorem. One can attack the affine branch by ruling out the exact constant-negative generated character; attack the non-affine branch by proving either one-sided shell cancellation for every generated quadratic character or a lower bound on the effective occupancy `eta`; and attack near-injectivity through its rank/conductor cost.

**Boundary.** `eta` is an `L^2` participation ratio, not raw support density. A support lower bound alone does not control it without multiplicity information, and MC-289 gives no conductor bound for the forced character. The finite-geometric/Fourier reduction does not improve `M(x)` by itself.
