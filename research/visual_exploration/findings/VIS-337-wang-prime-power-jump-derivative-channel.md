# VIS-337 — Wang's derivative channel carries every prime-power jump exactly, but each individual jump is exponentially below the PNT envelope

## Claim

Retain the actual squared-von-Mangoldt source from `VIS-291`--`VIS-336`:

`A(x)=sum_(n<=x) Lambda(n)^2`,

`E_A(x)=A(x)-(x log x-x)`,

and, on logarithmic scale,

`F(u)=e^(-u)E_A(e^u)`.

Let

`mu=sum_(n>=2) [Lambda(n)^2/n] delta_(log n)`

be the weighted prime-power source measure of `VIS-292`, and let

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

be Wang's adjusted smoothed remainder from `VIS-333`--`VIS-336`.

Then the actual arithmetic source has the exact distributional evolution

`D F = -F du-u du+mu`,

or equivalently

`(1+D)F = mu-u du`.

Consequently the exact Wang equation is

`(4-D^2)Q = 4(mu-u du)`.

In particular, if `u_n=log n` and `n=p^k` is a prime power, then

`Delta F(u_n)=Lambda(n)^2/n=(log p)^2/p^k`,

`Delta Q'(u_n)=-4 Lambda(n)^2/n`.

Thus **every prime-power jump of the normalized summatory remainder is transferred exactly into the first-derivative channel of the Wang output**. This is the source-specific realization of the derivative repayment mechanism identified abstractly in `VIS-334`.

However, an individual atom at height `u_n` satisfies

`Lambda(n)^2/n=(log p)^2/p^k <= u_n^2 e^(-u_n)`.

Hence, for every fixed `c>0`,

`u^2 e^(-u) = o(exp(-c u^(3/5)(log u)^(-1/5)))`.

The individual prime-power jumps are therefore exponentially smaller than the Korobov--Vinogradov-scale normalized source envelope carried through Wang's statistic in `VIS-291`.

So the obvious singular high-frequency content of the arithmetic staircase does **not** by itself realize the generic chirp escape of `VIS-336` at the currently relevant PNT scale. Any useful `Q`-small / derivative-large mechanism at that scale must come from **collective organization of many prime-power atoms against the continuous baseline**, not from one prime-power discontinuity or a bounded number of isolated jumps.

**Evidence/status:** `EXACT-DERIVED + SOURCE-SPECIFIC DERIVATIVE REPAYMENT + QUANTITATIVE NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No improved bound for `E_A`, no frequency-migration theorem, no pair-correlation improvement, and no RH consequence is claimed.

## 1. Exact hybrid evolution of the normalized arithmetic source

Write

`B(u)=A(e^u)`.

The function `B` is a right-continuous staircase with jump `Lambda(n)^2` at `u=log n`. Distributionally,

`D B = sum_(n>=2) Lambda(n)^2 delta_(log n)`.

Since

`F(u)=e^(-u)B(u)-(u-1)`,

the product rule gives

`D F`
` = -e^(-u)B(u) du + e^(-u)D B-du`.

At the atom `u=log n`, multiplication by `e^(-u)` contributes `Lambda(n)^2/n`, so the atomic term is exactly `mu`. Also

`e^(-u)B(u)=F(u)+u-1`.

Therefore

`D F = -(F+u-1)du-du+mu`
`    = -F du-u du+mu`,

which proves

`(1+D)F=mu-u du`.

Away from prime-power locations this reduces to the ordinary differential equation

`F'(u)=-F(u)-u`.

At a prime power the smooth main term is continuous and the staircase contributes

`Delta F(log n)=Lambda(n)^2/n`.

This decomposition is exact; no asymptotic prime-counting input is being used.

## 2. Wang transfers those atoms into `Q'` with factor `-4`

`VIS-333` derived the exact operator relation

`(4-D^2)Q=4(1+D)F`.

Substituting the source equation above gives

`(4-D^2)Q=4(mu-u du)`.

The same identity follows directly from `VIS-292`: `S(e^u)=K*mu` with `K(v)=e^(-2|v|)` and `(4-D^2)K=4 delta_0`; the extra terms `-u+(3/4)e^(-2u)` contribute the smooth baseline `-4u du`, while `e^(-2u)` lies in the homogeneous kernel of `4-D^2`.

The function `Q` is continuous at every `u_n=log n`. Integrate the displayed distributional equation through a shrinking interval around `u_n`. The bounded `4Q` term and the smooth baseline vanish in the limit, whereas `mu` contributes `Lambda(n)^2/n`. Hence

`-Delta Q'(u_n)=4 Lambda(n)^2/n`,

or

`Delta Q'(u_n)=-4 Delta F(u_n)`.

This also cross-checks the causal inverse of `VIS-334`: its memory and boundary terms are continuous, so taking jumps in

`F=(Q-Q')/4 + continuous memory`

gives the same relation.

The derivative tax is therefore not only a generic Fourier possibility. On the actual arithmetic source, `Q'` contains an exact copy of every prime-power atom.

## 3. Individual arithmetic atoms are far below the live envelope

If `n=p^k` and `u_n=log n=k log p`, then

`Delta F(u_n)`
` = (log p)^2/p^k`
` = (u_n/k)^2 e^(-u_n)`
` <= u_n^2 e^(-u_n)`.

The same bound, multiplied by `4`, holds for `|Delta Q'(u_n)|`.

By `VIS-291`, the strongest generic unconditional input currently propagated through the fixed-power Wang branch has normalized shape

`exp(-c V(u))`,

where

`V(u)=u^(3/5)(log u)^(-1/5)`

up to weakening the positive constant. Since `V(u)=o(u)`, for every fixed `c>0`

`u^2 e^(-u) / exp(-c V(u))`
` = u^2 exp(-u+cV(u)) -> 0`.

Thus the singularity attached to any one prime power is vastly smaller than the scale of the unresolved source envelope. The same is true for any fixed finite collection of nearby individual atoms.

This distinction matters because a staircase automatically has arbitrarily fine singular Fourier content. Counting that singularity as evidence of the useful nonstationary migration requested by the accepted Wang clue would be a false positive: the amplitudes of the individual jumps are already too small at the relevant normalized scale.

## 4. Representation and falsification audit

The representation delta is source-specific rather than another generic filter variant. `VIS-292` already proved exact recovery of the weighted prime-power measure by a second-order operator, and `VIS-334` already proved that smooth pointwise inversion charges one derivative. The new interface here is the exact first-derivative jump map

`Delta F(log n) -> Delta Q'(log n)=-4 Delta F(log n)`

for the **actual** `Lambda^2` staircase, together with the comparison of those atomic amplitudes against the live Korobov--Vinogradov envelope.

Several possible overinterpretations fail:

- the existence of arbitrarily small-scale prime-power jumps does not imply useful source-envelope-scale frequency migration;
- the exact derivative atoms do not show that `Q'` is globally large at Korobov--Vinogradov scale;
- summing absolute jump magnitudes over a growing window would discard the cancellation against the continuous `u du` baseline that defines the remainder and therefore cannot certify the desired signed mechanism;
- the result does not exclude collective packets of many atoms whose signed organization produces a larger nonstationary derivative channel.

Accordingly this is a negative control on the most immediate arithmetic realization of `VIS-336`, not a closure of the accepted Wang clue.

## 5. Prior art and evidence boundary

The ingredients are standard or already canonical in this line. The von Mangoldt function is supported on prime powers; distributional differentiation of a staircase produces point masses at its jumps; and the Korobov--Vinogradov PNT scale used for comparison is classical analytic-number-theory prior art recorded in `VIS-291` (with Bellotti 2026 and NIST DLMF §27.12.6 as its current literature anchors).

`VIS-292` already identifies Wang's weighted `Lambda^2` source measure `mu` and the modified-Helmholtz Green resolvent, while `VIS-333` and `VIS-334` give the exact first-order summatory transfer and its derivative-priced inverse. No novelty is claimed for distributional jump calculus, Green-function inversion, the PNT bound, or the von Mangoldt support description.

The durable contribution is only the exact source-specific control needed at the current frontier: isolated prime-power singularities are indeed stored in `Q'`, but their normalized amplitudes are exponentially below the unresolved PNT envelope. This neither proves nor disproves a collective arithmetic frequency-migration mechanism.

## Dependencies

- `VIS-291`: supplies the current Korobov--Vinogradov-scale normalized source envelope.
- `VIS-292`: identifies the exact weighted prime-power source measure and Green resolvent.
- `VIS-333`: supplies `(4-D^2)Q=4(1+D)F`.
- `VIS-334`: supplies the causal inverse and first-derivative repayment interpretation.
- `VIS-336`: supplies the generic single-trajectory chirp control whose arithmetic realization is being tested.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue asking for an actual-source mechanism and downstream repayment audit.

## Research consequence

The accepted Wang clue narrows from “does the arithmetic source have high-frequency structure?” to a stricter question. The source certainly has arbitrarily fine singular structure at prime powers, and Wang's derivative channel records those atoms exactly, but **individual arithmetic jumps are too small to explain a useful gain at the current PNT envelope scale**.

The next source-level advance therefore has to identify a collective signed organization of many prime-power atoms — for example a quantitatively controlled packet, phase, or multiscale imbalance — whose contribution survives after subtracting the continuous baseline and is large enough to matter at Korobov--Vinogradov scale. Separately, the destination-level branch must still show that Wang's complete statistic can use the smaller `Q` without paying back that collective derivative carrier. Developing either of those independent next questions is left for a later invocation.