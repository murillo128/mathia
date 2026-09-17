# VIS-275 — Laplace-null Wang probes do not improve the present source-bound rate by moment cancellation alone

## Claim

Keep the fixed-source setting of `VIS-274`. Let `L=log T`, `H=T^theta`, fix `0<lambda<theta<1`, and let

`h in C_c^infinity((0,infinity))`

be a fixed nonzero real profile with support in a compact interval `[q_-,q_+] subset (0,infinity)`. Set

`g_T(alpha)=h(L|alpha|/(2*pi)).`

The proof-level Wang remainder used in `VIS-274` yields, after the same change of variables `q=L alpha/(2*pi)` and normalization by `2*pi/(H L)`, the absolute majorant

`|R_T[h]|`
` <= C_(lambda,theta) [`
`      (8*pi^2/L) integral |h(q)| exp(-4*pi q) dq`
`    + (8*pi^2/L^(3/2)) integral |h(q)| exp(-2*pi q) dq`
`    + (8*pi^2/L^2) integral |h(q)| dq`
`    + (8*pi^2 L/H) integral |h(q)| exp(2*pi q) dq`
`    + (8*pi^2/(H L)) integral |h(q)| exp(-pi q) dq ]`

for all sufficiently large `T`, with the harmless displayed constants absorbable into the source big-`O` constant if desired.

In particular, the dominant certified term is

`O( L^-1 integral |h(q)| exp(-4*pi q) dq ).`

Because `exp(-4*pi q)>0` on the fixed support, this weighted `L^1` quantity is strictly positive for every fixed nonzero `h`. Therefore imposing signed cancellation conditions such as

`integral h(q) exp(-4*pi q) dq = 0`

or any finite family

`integral q^j h(q) exp(-4*pi q) dq = 0`

cannot by itself improve the **rate certified by the present Wang pointwise remainder estimate** from `O(1/L)` to `o(1/L)`: the proof majorant sees `|h|`, not the signed moments of `h`.

This is a limitation of the currently exposed proof interface, not a lower bound on the true residual. The actual Wang remainder for a special signed packet may cancel below `1/L`; that cancellation simply is not available from the absolute-value envelope used in `VIS-274`.

**Evidence/status:** `LITERATURE+DERIVED + EXACT SOURCE-BOUND PROPAGATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No sharp `1/L` lower bound, secondary coefficient, impossibility theorem for improved pair correlation, prime-power transfer, or RH implication is claimed.

## 1. Propagate the five source-error terms without collapsing their weights

`VIS-274` records the uniform estimate extracted in `VIS-266` from the proof of Biao Wang's Theorem 2.2:

`F_I(T^alpha)`
` = (H/(2*pi)) [L^2 exp(-2L alpha) + L alpha]`
`   + O_(lambda,theta)(H + H L exp(-2L alpha)`
`       + H sqrt(L) exp(-L alpha) + L^3 exp(L alpha)`
`       + L exp(-L alpha/2)).`

For an even test,

`W_I(g_T)=2 integral_0^lambda g_T(alpha) F_I(T^alpha) d alpha.`

The two displayed main terms were rescaled exactly in `VIS-274`. Here retain the absolute weights of the five remainder terms instead of immediately replacing them by a generic `O_h(1/L)`.

On the positive half-line put

`q=L alpha/(2*pi)`, `d alpha=(2*pi/L)dq`.

For the bare `O(H)` term, the normalized weighted contribution is bounded by

`(2*pi/(H L)) * 2 * (2*pi/L) * H integral |h(q)| dq`
` = (8*pi^2/L^2) integral |h(q)| dq.`

For the dominant source term `O(H L exp(-2L alpha))`, it is bounded by

`(2*pi/(H L)) * 2 * (2*pi/L) * H L`
`  * integral |h(q)| exp(-4*pi q)dq`
` = (8*pi^2/L) integral |h(q)| exp(-4*pi q)dq.`

Likewise the `O(H sqrt(L) exp(-L alpha))` term gives

`(8*pi^2/L^(3/2)) integral |h(q)| exp(-2*pi q)dq.`

The `O(L^3 exp(L alpha))` term gives

`(8*pi^2 L/H) integral |h(q)| exp(2*pi q)dq,`

and the `O(L exp(-L alpha/2))` term gives

`(8*pi^2/(H L)) integral |h(q)| exp(-pi q)dq.`

All integrals are over the fixed support of `h`. Since `H=T^theta`, the `L/H` and `(HL)^-1` terms are negligible compared with every negative power displayed above. The unique theorem-level `L^-1` contribution is therefore the weighted absolute norm inherited from Wang's `H L exp(-2L alpha)` error term.

## 2. Laplace nulling kills the main term but not this majorant

The leading fixed-source term in `VIS-274` is

`4*pi integral h(q) exp(-4*pi q)dq.`

A sign-changing `h` can annihilate this functional exactly. But the dominant source-error bound is controlled instead by

`integral |h(q)| exp(-4*pi q)dq.`

For every fixed nonzero `h`, this quantity is positive because the weight is positive everywhere on the compact support. Signed orthogonality therefore has no algebraic action on the current majorant.

The same remains true after imposing any finite collection of signed polynomial-Laplace moments. Such constraints can reorganize positive and negative mass of `h`, but they cannot make the positive weighted norm vanish unless `h=0` almost everywhere. They may change its numerical constant, but not the certified asymptotic exponent in `L` for a fixed nonzero profile.

This separates two different questions that were still conflated at the end of `VIS-274`:

- the leading **main term** is a signed Laplace functional and can be removed by orthogonality;
- the leading **available error control** is an unsigned weighted norm and survives that orthogonality.

The first fact creates the Laplace-null channel. The second explains why adding more signed moments cannot, from the present estimate alone, sharpen that channel below `O(1/L)`.

## 3. What would actually be needed to cross the boundary

An `o(1/L)` result for a fixed nonzero Laplace-null packet requires information not present in the pointwise majorant above. Several logically distinct upgrades would suffice.

One is a signed first-order expansion of the source remainder: after the fixed-source rescaling, prove that

`L R_T(q) -> A(q)`

in a mode strong enough to integrate against fixed smooth `h`. Then one could test whether `A` has an arithmetic component and choose packets orthogonal to any universal part.

A second is a proof-level cancellation mechanism for the `H L exp(-2L alpha)` error itself, rather than an absolute-value bound. Such structure could make a signed test useful even though the present majorant cannot see it.

A third is an improved pointwise estimate whose fixed-source rescaling is already `o(1/L)` or whose leading error has a different explicit kernel. Any of these would create a genuinely new theorem interface. Merely adding more moment conditions to `h` does not.

This is the precise negative control for the next fixed-source step: **orthogonality engineering is exhausted until the source remainder acquires signed structure or a stronger rate.**

## 4. Stress tests and boundaries

The statement is deliberately about what is certified by the existing Wang estimate. It does not assert that the true remainder has size comparable to `1/L`, that the displayed majorant is sharp, or that a specially chosen `h` cannot enjoy accidental or structural cancellation in the actual statistic.

The profile `h` is fixed as `T` grows. A `T`-dependent family whose weighted `L^1` norm itself shrinks is a different scaling problem and is not covered. Likewise the support remains in a fixed compact subset of `(0,infinity)`; moving windows or packets touching `q=0` require separate accounting.

The conclusion also does not forbid using more information from Wang's proof than the final pointwise envelope. If the proof contains recoverable signed correlations between the remainder terms that were discarded when taking absolute values, extracting them would be exactly the kind of stronger interface identified above.

Finally, the explicit deterministic cusp contribution from `VIS-274`,

`(8*pi^2/L^2) integral q h(q)dq,`

remains below the current `O(1/L)` source-bound floor. Killing or retaining that `L^-2` moment cannot identify a secondary coefficient until the larger remainder is sharpened.

## 5. Prior-art and novelty boundary

The sole external analytic input is the same one already audited for `VIS-266` and `VIS-274`: Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), especially the proof-level estimate behind Theorem 2.2.

The passage from a pointwise big-`O` envelope to a weighted `L^1` majorant by

`|integral h R| <= integral |h| |R|`

is elementary. No novelty is claimed for that inequality, for weighted-norm duality, or for the general fact that signed moment cancellation cannot cancel an estimate after its sign information has been discarded.

The durable Mathia result is the exact specialization of that elementary limitation to the newly opened fixed-`q` Wang channel: it identifies which source error creates the surviving `1/L` boundary, preserves its rescaled kernel, and rules out a tempting but ineffective next move — stacking further signed moment constraints without first strengthening the theorem interface.

## Research consequence

The fixed-source branch should not spend further research budget constructing increasingly elaborate Laplace-null packets merely to try to beat the current `O(1/L)` certificate. For every fixed nonzero packet, the existing proof envelope retains the positive weighted `L^1` term at that rate.

The next coherent theorem question is therefore source-side rather than packet-side: can the `H L exp(-2L alpha)` remainder in Wang's proof be replaced, decomposed, or expanded so that its fixed-`q` rescaling has signed structure or a rate below `1/L`? Only after such an upgrade does it become meaningful to ask which additional source moments isolate an arithmetic coefficient.

No untouched confirmation-zero data are used.