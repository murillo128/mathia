# VIS-319 — Bézout strip coordinates restore the two-prime local sieve dimension

## Claim

Keep the represented same-shell determinant geometry of `VIS-315`--`VIS-318`: `gcd(u,v)=1`,

`M/2 < u,v,q,r <= 2M`,

and

`h=qv-ur`.

Choose any Bézout pair `a,b in Z` with

`au-bv=1`.

Define the integer-coordinate map

`Psi(t,h)=(q,r)=(u t-b h, v t-a h)`.

Then:

1. `qv-ur=h` identically;
2. the matrix of `Psi` has determinant `-1`, so `Psi: Z^2 -> Z^2` is a unimodular bijection;
3. for every prime `ell`, reduction of `Psi` modulo `ell` is a bijection of `F_ell^2`, and therefore exactly `(ell-1)^2` residue pairs `(t,h) mod ell` map to pairs with `q != 0` and `r != 0 mod ell`.

Thus the full two-prime local sieve factor

`((ell-1)/ell)^2 = (1-1/ell)^2`

is preserved exactly in the joint `(t,h)` coordinates. The loss identified in `VIS-317` occurs only after the further projection `(t,h)->h`.

At the same time, the shell preimage

`Omega_(M,D)(u,v)`
` = {(t,h) in R^2 : |h|<=D, M/2<ut-bh<=2M, M/2<vt-ah<=2M}`

is a long thin region: for each fixed `h`, the admissible `t` interval has length `<3`, while `h` ranges over `O(D)` values. At the natural Wang resolution `D asymp M^2/V` with `V asymp M log log M`, this means `D asymp M/log log M`.

So `VIS-317` and `VIS-318` do not leave a missing sieve **dimension**. Bézout coordinates restore that dimension exactly. What remains missing is a **thin-domain distribution theorem**: one must control how the long-thin set `Omega_(M,D)(u,v) cap Z^2` occupies the two-dimensional residue classes strongly enough, uniformly in the moving represented slope `u/v`, for the classical local factor `(1-1/ell)^2` to produce the required `log^(-2) M` saving.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-AUDIT + SIEVE-LOCAL-FACTOR + PROOF-METHOD REDUCTION + NO-NOVELTY-CLAIM`.

No prime-ratio occupancy estimate, sieve remainder bound, prime-pair asymptotic, natural-window Wang theorem, or stronger RH criterion is claimed.

## 1. A unimodular coordinate system for the whole determinant strip

Because `gcd(u,v)=1`, choose `a,b` with `au-bv=1`. Put

`q=ut-bh`,

`r=vt-ah`.

Then

`qv-ur`
` = (ut-bh)v-u(vt-ah)`
` = h(au-bv)`
` = h`.

The transformation matrix from `(t,h)` to `(q,r)` is

`[[u,-b],[v,-a]]`,

whose determinant is

`-ua+bv=-1`.

Hence the map is unimodular. In particular, every integer pair `(q,r)` has a unique integer coordinate pair `(t,h)`, with the second coordinate exactly the determinant `qv-ur`.

This representation aggregates all determinant slices at once. Freezing `h` recovers the one-parameter affine slice of `VIS-318`, while allowing `h` to vary retains the transverse direction that was lost by treating each slice independently.

## 2. The two prime-coordinate exclusions reappear exactly

Reduce the unimodular matrix modulo a prime `ell`. Its determinant remains `-1`, so it is invertible over `F_ell` for **every** `ell`; no assumption `ell not dividing uv` is needed for this statement.

Therefore `(t,h) mod ell` runs bijectively through `(q,r) mod ell`. Among the `ell^2` residue pairs, exactly

`(ell-1)^2`

have both `q` and `r` nonzero. Equivalently, the forbidden union

`{q=0} union {r=0}`

contains exactly

`2 ell-1`

residue pairs.

This is the ordinary two-coordinate prime local factor. In the joint coordinates there are two genuine codimension-one exclusions. `VIS-317` found that after projecting all these points to the single determinant coordinate `h`, every odd determinant residue remains represented by admissible nonzero `(q,r)`, so the exclusions cease to be visible as forbidden `h` classes. The present calculation shows that the information was compressed by that projection, not destroyed in the full strip.

## 3. Why this does not yet give the desired occupancy bound

The shell conditions become

`M/2 < ut-bh <= 2M`,

`M/2 < vt-ah <= 2M`.

For fixed `h`, the first inequality alone restricts `t` to an interval of length

`(3M/2)/u < 3`,

because `u>M/2`. Thus every vertical `h`-fiber of `Omega_(M,D)(u,v)` contains at most three integer values of `t`, exactly as in `VIS-318`.

Consequently the complete strip is not a two-dimensional box with two long independent averaging directions. It is a thin lattice region of length `asymp D` in the transverse determinant coordinate and bounded thickness in the affine coordinate. The unimodular map preserves area and congruence structure, but it does not manufacture a second long variable.

This distinction is decisive for sieve use. The local residue count says what the correct multiplicative factor would be **if** the lattice points of the thin region were sufficiently distributed among the relevant residue classes. It does not establish that distribution. A sieve over a long thin region can have remainder terms governed by boundary/alignment effects that are invisible in the full residue-plane count.

Thus it would be incorrect to infer

`# {(t,h) in Omega cap Z^2 : q,r prime} << D/log^2 M`

from unimodularity and the local factor alone.

## 4. The next exact proof obligation

The active density frontier can now be stated without the representation ambiguity left by `VIS-317`--`VIS-318`.

A pair-preserving sieve route should work with `Omega_(M,D)(u,v)` or an equivalent unimodular image and prove enough congruence distribution, uniformly over represented same-shell `u/v`, that the dimension-two local exclusions survive summation over the thin domain. Schematically, for squarefree moduli `d` in the sieve range, one needs control of the discrepancy between the actual lattice-point counts in the relevant residue classes and the counts predicted by the invertible `(t,h)<->(q,r)` residue map, with total remainder small enough for an upper-bound sieve to retain two logarithmic prime-density factors.

At the natural Wang window,

`D asymp M/log log M`,

so this is a genuinely short/thin moving-domain problem. A theorem for fixed-coefficient binary linear forms in a large two-dimensional box does not automatically settle it, nor does a theorem for one fixed determinant slice.

An equivalent successful route may avoid worst-cell sieving altogether and prove the coefficient-weighted/additive-energy estimate already allowed by `VIS-315`--`VIS-316`. The present finding only identifies the correct coordinate-level sieve object.

## Prior-art and novelty boundary

The Bézout parametrization, unimodular change of lattice coordinates, and the count `(ell-1)^2` of residue pairs avoiding two coordinate hyperplanes are elementary classical facts. No novelty is claimed for them. Classical higher-dimensional Selberg/Brun sieve and binary-linear-form literature provides the general background for interpreting `(1-1/ell)^2` as a two-prime local factor; the sparse-energy and Beatty-prime literature already recorded in `VIS-315` remains nearby orientation for alternative formulations.

A targeted check of nearby sieve literature does not justify importing a standard box or fixed-linear-form theorem directly into the present moving long-thin region. This finding therefore records an exact representation reduction and a sharpened proof obligation, not a new sieve theorem.

## Boundaries and falsification

This finding does not prove the occupancy hypothesis of `VIS-315`, improve the aggregate criterion of `VIS-316`, or contradict the negative results `VIS-317` and `VIS-318`. Instead it reconciles them: projection to `h` loses the two local exclusions, while freezing `h` leaves too little averaging length; the joint unimodular coordinates retain both the exclusions and the full family of short slices.

The exact algebra is independent of the shell, but the thin-domain conclusion uses the represented same-shell assumption `u,v>M/2`. If the center direction has a much smaller primitive step, the thickness in `t` can be long and the geometry must be re-audited.

Falsify the exact claim by finding coprime `u,v` and a Bézout pair `a,b` with `au-bv=1` for which the displayed map fails to be unimodular, fails to satisfy `qv-ur=h`, or fails to induce a bijection modulo some prime.

## Dependencies

- `VIS-315`: identifies a Fourier-resolution prime-ratio cell with a thin determinant strip around a represented same-shell slope.
- `VIS-316`: shows that only the taper-weighted shell occupancy excess must be controlled globally.
- `VIS-317`: proves that scalar determinant projection hides the two odd-prime coordinate exclusions.
- `VIS-318`: proves that each fixed determinant slice has only bounded affine length in the same-shell regime.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining pair-preserving thin-strip/energy frontier.

## Research consequence

The pair-preserving route is now localized more precisely. The correct sieve coordinates are not the scalar determinant `h` and not one fixed affine slice, but the unimodular joint coordinates `(t,h)` for the whole strip. They preserve the exact two-prime local factor while exposing the real remaining difficulty: uniform congruence distribution on a moving long-thin lattice region.

A next useful result should therefore attack that thin-domain discrepancy/remainder problem directly, or abandon worst-cell sieving in favor of the weighted-energy route. Re-deriving sieve dimension, projecting again to `h`, or applying a long one-variable sieve to a fixed slice would not address the remaining obstruction.