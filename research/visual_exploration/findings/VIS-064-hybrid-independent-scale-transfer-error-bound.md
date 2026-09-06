# VIS-064 — independently defined hybrid prime/zero scale transfer is controlled by the hybrid residual

## Claim

Let `P_X(s)` and `Z_X(s)` be the independently defined prime and zero factors in a hybrid Euler–Hadamard representation at scale `X`, and define the exact multiplicative residual

`E_X(s) = zeta(s) / (P_X(s) Z_X(s))`

where the quantities are nonzero. For two admissible scales `X<Y`, the branch-free identity

`P_Y(s) Z_Y(s) / (P_X(s) Z_X(s)) = E_X(s) / E_Y(s)`

holds exactly.

Consequently the summed log-modulus scale increment of the independently defined prime and zero factors is not a free cross-scale observable:

`[log|P_Y|-log|P_X|] + [log|Z_Y|-log|Z_X|]`
` = log|E_X| - log|E_Y|`.

If the hybrid approximation supplies pointwise relative-error bounds

`|E_X-1| <= eta_X < 1`,
`|E_Y-1| <= eta_Y < 1`,

then

`| [log|P_Y|-log|P_X|] + [log|Z_Y|-log|Z_X|] |`
` <= -log(1-eta_X) - log(1-eta_Y)`.

The corresponding phase-transfer defect is also controlled. Writing circular distance modulo `2 pi` as `dist_T`,

`dist_T(`
`  [arg P_Y-arg P_X] + [arg Z_Y-arg Z_X],`
`  0`
`)`
` <= min(pi, arcsin(eta_X)+arcsin(eta_Y))`.

Thus the exact quotient obstruction in `VIS-010` has a quantitative analogue for the **independently constructed** hybrid factors: whenever the hybrid product is accurate at both scales, prime and zero scale increments are forced to nearly cancel in modulus and phase up to the explicitly measurable hybrid residual.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

The hybrid Euler–Hadamard representation is established prior art. The identities and bounds above are elementary consequences of treating its approximation error as an explicit third channel. No new hybrid-product theorem, zeta estimate, or RH consequence is claimed.

## 1. Exact three-channel scale identity

The defining residual gives

`zeta = P_X Z_X E_X`

and also

`zeta = P_Y Z_Y E_Y`.

Equating the two factorizations yields

`P_Y Z_Y / (P_X Z_X) = E_X/E_Y`.

This differs materially from the control in `VIS-010`. There the complementary channel was defined tautologically as `R_X=zeta/P_X`, so opposite scale increments were exact by construction. Here `Z_X` is independently defined from the zero side of the hybrid formula. Nevertheless, once the product is known to approximate `zeta` well, its prime/zero transfer is still constrained: any failure of exact cancellation is exactly the change in the hybrid residual between scales.

The natural visual quantity

`D_mod(X,Y;s)`
` = [log|P_Y|-log|P_X|] + [log|Z_Y|-log|Z_X|]`

therefore equals

`log|E_X/E_Y|`.

A heatmap or animation of this summed scale-transfer defect is mathematically a visualization of the hybrid approximation-error ratio. It is not an independent prime/zero coupling statistic.

## 2. Relative hybrid error gives a deterministic modulus bound

Assume `|E_X-1|<=eta_X<1`. The reverse and ordinary triangle inequalities give

`1-eta_X <= |E_X| <= 1+eta_X`.

Hence

`|log|E_X|| <= -log(1-eta_X)`.

The same holds at `Y`, and therefore

`|log|E_X|-log|E_Y||`
` <= |log|E_X|| + |log|E_Y||`
` <= -log(1-eta_X)-log(1-eta_Y)`.

Combining this with the exact scale identity gives the stated pointwise bound.

For small errors this is

`eta_X + eta_Y + O(eta_X^2+eta_Y^2)`,

so an accurate hybrid approximation forces near-conservation of prime-plus-zero log-amplitude increments at the same accuracy scale. Visually strong anticorrelation between the two channels is therefore expected background unless it exceeds what the explicit hybrid residual permits.

## 3. The same control applies to phase modulo `2 pi`

If `|E-1|<=eta<1`, then `E` lies in the closed disk centered at `1` with radius `eta`, which does not contain the origin. The maximal absolute argument of a point in that disk is the tangent angle

`arcsin(eta)`.

Thus the principal argument satisfies

`|Arg E| <= arcsin(eta)`.

From

`P_Y Z_Y/(P_X Z_X)=E_X/E_Y`,

the sum of the prime and zero phase increments equals `Arg(E_X/E_Y)` modulo `2 pi`. The triangle inequality for circular distance therefore gives

`dist_T(Delta arg P + Delta arg Z,0)`
` <= min(pi, arcsin(eta_X)+arcsin(eta_Y))`.

Branch choices in separate displayed arguments cannot create a new signal because the statement is intrinsically modulo `2 pi`.

## 4. Visual falsification rule

For a scale-recursive prime/zero visualization based on independently constructed hybrid factors, three channels must be distinguished:

- the prime scale increment;
- the zero scale increment;
- the hybrid residual increment.

The first two are not independent once the third is small. A claimed cross-scale lock, amplitude transfer, or phase compensation must therefore be compared with the exact residual identity above before it can be interpreted as additional arithmetic structure.

In particular, the following are not discriminating by themselves:

- `Delta log|P|` visually mirroring `-Delta log|Z|`;
- prime and zero phase increments approximately summing to zero;
- a small value of `Delta log|P|+Delta log|Z|` in a regime where the hybrid theorem already makes `E_X` and `E_Y` close to `1`.

These effects may simply certify that the hybrid product is doing what its approximation theorem says it should do.

A surviving visual statistic must use structure not fixed by this one-complex-dimensional product constraint: for example within-factor geometry, zero-window entry/exit organization after deterministic windowing is controlled, prime-band structure beyond the summed transfer, or a hybrid-error feature whose size or organization is itself unexpected relative to the theorem and matched controls.

## 5. Prior art and novelty boundary

S. M. Gonek, C. P. Hughes, and J. P. Keating, **A hybrid Euler-Hadamard product for the Riemann zeta function**, *Duke Mathematical Journal* 136:3 (2007), 507–549, DOI `10.1215/S0012-7094-07-13634-2`, establish the smoothed hybrid representation with a finite prime factor, a zero factor, and explicit pointwise approximation error. This is already the canonical source anchor for `VIS-010` and the accepted prime-phase recursive-geometry clue.

The present finding does not add a theorem to that literature. It records a Mathia-specific negative control that follows once the hybrid error is kept as an explicit channel rather than discarded: scale variation of the independently defined prime and zero factors is quantitatively constrained by variation of that error.

`VIS-010` remains the stronger exact obstruction for the artificial quotient residual `zeta/P_X`. `VIS-064` covers the more relevant hybrid setting in which `Z_X` is independently defined and the complementarity is approximate rather than definitional.

## 6. Boundaries and falsification

The logarithmic statements require the displayed factors and `zeta` to be nonzero at the evaluation point. At or extremely near zeros, use the branch-free multiplicative identity directly or a separately justified regularization rather than treating divergent logarithms as visual structure.

The bounds are only as strong as the available relative-error bounds `eta_X,eta_Y`. If the hybrid theorem is used in a regime where its error is not small, the result does not predict strong prime/zero cancellation there.

The finding also does not say that every joint statistic of `P_X` and `Z_X` is tautological. It controls the particular product-direction combination selected by the hybrid factorization. Nonlinear shape statistics, conditional geometry, within-factor organization, and matched-control differences can remain informative if they are not reducible to the residual ratio.

Falsify the exact claim by finding nonzero quantities satisfying `E_X=zeta/(P_X Z_X)` and `E_Y=zeta/(P_Y Z_Y)` for which `P_Y Z_Y/(P_X Z_X) != E_X/E_Y`. Falsify the stated quantitative bounds by producing `|E-1|<=eta<1` that violates either the log-modulus disk bound or the phase disk bound.

## Research consequence

The accepted prime-phase recursive-geometry clue remains live but is narrower. Passing from the artificial quotient `zeta/P_X` to the independently defined hybrid zero factor does **not** by itself make scale-transfer anticorrelation informative. The hybrid residual must be treated as the third coordinate, and any claimed prime/zero scale organization must survive the deterministic error-controlled complementarity recorded here.

A useful next visual experiment should therefore avoid testing whether the two hybrid factors merely compensate each other as `X` changes. It should freeze a statistic that is not determined by their product-direction sum and then compare that statistic across admissible scales, smoothing choices, and matched prime/zero controls. A failure to beat this residual-controlled baseline closes the apparent recursive-transfer signal without closing the broader hybrid-geometry direction.