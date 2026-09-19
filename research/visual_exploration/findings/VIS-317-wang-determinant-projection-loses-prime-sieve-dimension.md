# VIS-317 — determinant projection erases the two prime-coordinate sieve exclusions

## Claim

Fix coprime odd integers `u,v` and consider the determinant coordinate

`h = qv - ur`

for moving prime candidates `q,r`. For every odd prime `ell` with `ell` not dividing `uv`, define

`N_ell(h;u,v) = #{(q,r) in (F_ell^*)^2 : qv - ur = h}`.

Then exactly

- `N_ell(h;u,v) = ell-1` when `h = 0 (mod ell)`;
- `N_ell(h;u,v) = ell-2` when `h != 0 (mod ell)`.

In particular **every residue class of `h mod ell` is compatible with both moving coordinates being nonzero modulo `ell`**. For `ell=2`, when `u,v,q,r` are odd, `h` is always even.

Thus projecting a prime pair `(q,r)` to the scalar determinant `h=qv-ur` preserves the geometric ratio-cell condition but erases the separate odd-prime residue exclusions carried by `q` and `r`. A sieve that acts only on `h` through forbidden residue classes cannot by itself recover the two prime-density factors behind the `1/log^2 M` scale sought in the Wang local-density frontier.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + REPRESENTATION-AUDIT + SIEVE-STRUCTURE CONTROL + NO-NOVELTY-CLAIM`.

This does not rule out a two-coordinate Selberg sieve, a sieve after parametrizing each determinant slice by two linear forms, a singular-series refinement depending on `h`, or a coefficient-weighted/additive-energy route.

## 1. Exact local count

Fix an odd prime `ell` not dividing `uv`. For each nonzero `r mod ell`, the congruence

`qv - ur = h`

has the unique solution

`q = v^(-1)(h+ur) mod ell`.

If `h=0 mod ell`, this `q` is nonzero for every nonzero `r`, because `u` and `v` are invertible. Hence there are exactly `ell-1` admissible pairs.

If `h!=0 mod ell`, exactly one nonzero value

`r = -h u^(-1) mod ell`

makes `q=0`. All other `ell-2` nonzero choices of `r` give a nonzero `q`. This proves the formula.

At the prime `2`, odd `q,r,u,v` give odd products `qv` and `ur`, so their difference `h` is even. Parity is therefore a genuine scalar restriction, but there is no analogous excluded residue class at any odd prime away from the fixed source factors.

## 2. Representation audit

The determinant coordinate is geometrically natural for `VIS-315`. Near a fixed represented slope `u/v`,

`|q/r-u/v| = |qv-ur|/(rv)`,

so a Fourier cell of width `1/V` becomes a thin strip `|h| << M^2/V` when all four primes are of comparable size. The scalar `h` therefore preserves exactly the closeness information needed to describe a local ratio cluster.

It does **not** preserve the two coordinatewise primality filters. Before projection, the conditions `q != 0 (mod ell)` and `r != 0 (mod ell)` are two explicit local exclusions in the pair coordinates. After projection, every `h mod ell` remains attainable by an admissible nonzero pair. The projection compresses the local prime-sieve information into multiplicities rather than forbidden scalar residue classes.

The small distinction `ell-1` versus `ell-2` can feed a singular factor according to whether `ell|h`; it does not restore a forbidden class of determinant values. Accordingly, the obstruction here is specifically to **determinant-only residue sifting**, not to arithmetic dependence on `h` altogether.

## 3. Consequence for the Wang local-density frontier

`VIS-315` reduced the natural-window mean-square problem to local occupancy of represented prime ratios, equivalently to counting prime pairs `(q,r)` in thin determinant strips around represented slopes. `VIS-316` then showed that only a taper-weighted aggregate of shell excesses must be controlled.

A tempting next reduction would be to regard `h=qv-ur` as the one-dimensional arithmetic variable and try to obtain the missing `1/log^2 M` density scale by sieving determinant values themselves. The exact local count above blocks that route: away from parity, primality of both moving coordinates removes no determinant residue class modulo an odd prime.

The logarithmic saving must therefore retain more information than the scalar determinant alone. Natural surviving representations include the pair lattice `(q,r)`, or for fixed `h` a one-parameter family of integer solutions in which `q` and `r` become two affine linear forms of the parameter. Those representations retain the two coordinatewise primality conditions and are compatible with a genuine dimension-two sieve analysis.

This also explains why the successful shell-energy estimate in `VIS-314` can access a logarithmic prime-pair saving: it keeps the prime-pair coordinates long enough for the sieve to see both primality constraints instead of first quotienting them to one determinant coordinate.

## Prior-art and novelty boundary

The finite-field count above is elementary and the principle that sieve dimension depends on the retained local residue exclusions is classical. No novelty is claimed for either fact. The Mathia contribution here is a representation-level negative result for the current `VIS-315`/`VIS-316` proof frontier: it identifies a specific tempting compression that cannot carry the required two-prime sieve structure by itself.

A bounded literature audit around fixed-determinant prime matrices, prime-pair sieve formulations, and thin determinant strips did not supply a theorem that settles the moving-slope occupancy estimate required by the active clue. This finding therefore does not promote any new prime-distribution theorem; it only narrows the admissible proof representations.

## Boundaries

This finding does not prove or disprove the local-density estimate of `VIS-315`, bound any shell excess `A_M`, or establish the natural-window Wang estimate. It does not exclude a singular-series analysis whose local factors depend on divisibility of `h`, a pair-coordinate Selberg sieve over the full determinant strip, distribution results for the corresponding two linear forms, or the coefficient-weighted/additive-energy alternative already allowed by the accepted clue.

Its exact conclusion is narrower: **after the projection `(q,r) -> h=qv-ur`, there are no odd-prime forbidden determinant residues left from the two primality conditions, so determinant-only residue sifting is not the missing source of the desired `log^{-2} M` density factor.**