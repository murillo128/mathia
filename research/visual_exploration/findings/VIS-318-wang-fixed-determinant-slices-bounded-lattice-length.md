# VIS-318 — exact determinant slices have bounded lattice length in represented prime-ratio shells

## Claim

Keep the same-shell determinant geometry of `VIS-315`--`VIS-317`. Thus a represented center `u/v` and a candidate pair `q/r` satisfy

`M/2 < u,v,q,r <= 2M`,

with `gcd(u,v)=1`, and the determinant coordinate is

`h = qv-ur`.

For a fixed integer `h`, let

`S_h(M;u,v) = {(q,r) in Z^2 : M/2 < q,r <= 2M, qv-ur=h}`.

Then

`#S_h(M;u,v) <= 3`.

More generally, for any fixed comparable-shell convention `cM<q,r,u,v<=CM`, the number of lattice points on one exact determinant slice is `O_(c,C)(1)`.

Consequently, for any `D>=0`,

`#{(q,r) : M/2<q,r<=2M, |qv-ur|<=D}`
` <= 3(2 floor(D)+1)`
` << 1+D`.

At the Fourier resolution of `VIS-315`, where `D asymp M^2/V`, this recovers the ambient strip scale

`O(1+M^2/V)`.

At the natural Wang window `V asymp M log log M`, one exact determinant value therefore contains only `O(1)` candidate pairs, while the whole strip contains at most `O(M/log log M)` integer candidates before primality is imposed.

The fixed-`h` parametrization suggested after `VIS-317` does retain the two prime coordinates, but it has **no long one-parameter sifting range** in the represented same-shell regime. A dimension-two sieve applied separately on each exact determinant slice cannot be the source of the desired `log^{-2} M` occupancy saving through asymptotic averaging in its slice parameter. Any such saving must come from treating many determinant values jointly while retaining the pair coordinates, or from an equivalent weighted/additive-energy mechanism.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + REPRESENTATION-AUDIT + NO-NOVELTY-CLAIM`.

No prime-ratio occupancy estimate, prime-pair asymptotic, new sieve theorem, natural-window Wang theorem, or stronger RH criterion is claimed.

## 1. Exact parametrization of one determinant slice

Assume `S_h(M;u,v)` is nonempty and choose one integer solution `(q_0,r_0)` of

`vq-ur=h`.

Since `gcd(u,v)=1`, the complete integer solution set is

`q=q_0+u t`,

`r=r_0+v t`,

with `t in Z`.

This is the usual one-parameter parametrization of a primitive linear Diophantine equation. It indeed preserves the two moving coordinates rather than projecting them to the scalar determinant.

The decisive point is the scale of the step vector: here `u,v` themselves belong to the same represented prime-ratio shell as `q,r`, so both are `>M/2`.

## 2. Same-shell geometry makes the slice parameter bounded

The condition

`M/2 < q_0+u t <= 2M`

restricts `t` to an interval of length

`(3M/2)/u < 3`.

An interval of length strictly less than `3` contains at most three integers. Hence the `q` constraint alone already gives

`#S_h(M;u,v) <= 3`.

The simultaneous `r` constraint can only reduce this number. Under a general fixed shell `cM<q,r,u,v<=CM`, the same argument gives an interval for `t` of length at most `(C-c)/c`, so the slice multiplicity remains bounded by a constant depending only on the shell convention.

Thus the affine-linear representation is exact but short: changing `t` by one moves `(q,r)` by the vector `(u,v)`, whose size is already comparable with the diameter of the shell.

## 3. Summing exact slices recovers the unsieved strip scale

If `|qv-ur|<=D`, the integer determinant `h` has at most `2 floor(D)+1` possible values. Combining this with the slice bound gives

`#{(q,r) in shell : |qv-ur|<=D}`
` << 1+D`.

For the `1/V` log-frequency cell of `VIS-315`, `D<<M^2/V`, so

`kappa_M(V) << 1+M^2/V`

is recovered at the level of all integer pairs. This is the same scale that one obtains from ambient lattice geometry before exploiting primality.

The desired arithmetic occupancy scale is instead

`1 + M^2/[V log^2 M]`.

Because each exact `h` contributes only boundedly many candidate lattice points, the missing `log^{-2} M` factor cannot arise from a long Selberg-sieve average in the fixed-`h` parameter `t`: there is no long `t` interval to sieve.

This does **not** say that the prime constraints disappear on a fixed slice. It says that the exact-slice parametrization is too short to average them asymptotically slice by slice in the present geometry.

## 4. What representation still retains enough averaging length

`VIS-317` ruled out sieving the scalar determinant values themselves by forbidden odd-prime residue classes. The present finding rules out the opposite extreme of freezing one determinant value and expecting a long two-linear-form sieve in its affine parameter.

The remaining arithmetic object is therefore the **family of short determinant slices taken together**. A successful pair-preserving argument must obtain its prime-density saving across the whole thin strip, or across an equivalent set that still remembers both coordinates. Possible forms include:

- a two-coordinate upper-bound sieve whose base set is the complete thin strip rather than one `h`-slice;
- a rational/Beatty-type formulation that controls the candidate pair selected as the transverse coordinate varies;
- a coefficient-weighted or additive-energy inequality that never asks for worst-case prime density on each exact determinant slice.

These are surviving representations, not proved estimates.

## Prior-art and novelty boundary

The parametrization of solutions to a primitive linear Diophantine equation and the bounded number of lattice points obtained when the step vector is comparable with the box are elementary classical facts. No novelty is claimed for them. Classical fixed-dimensional Selberg upper-bound sieve theory, already cited in `VIS-314`, supplies the relevant background for why retaining two prime coordinates can produce a two-prime density saving when a sufficiently large sifted family is available.

A targeted literature check around prime values of linear forms, binary-form sieve methods, Beatty-prime problems, and thin determinant regions did not identify a result whose statement directly supplies the moving represented-slope occupancy estimate needed by `VIS-315`/`VIS-316`. The present claim is therefore only a representation-level obstruction for the current proof search, not a new theorem in sieve theory.

## Boundaries and falsification

This finding does not disprove the occupancy criterion of `VIS-315`, bound any shell excess `A_M`, or rule out a uniform sieve over the whole determinant strip. It does not exclude singular-series dependence on `h`, averaging over `h`, bilinear methods, rational Beatty-sequence methods, or the additive-energy route.

It applies specifically to represented centers `u/v` in the same comparable shell as the candidate ratios, which is exactly the reduction used to realize `kappa_M(V)` in `VIS-315`. If a future argument deliberately centers the strip at a direction whose primitive step vector is much smaller than `M`, this bounded-slice conclusion need not apply and must be re-audited.

Falsify the exact claim by exhibiting two same-shell coprime centers for which the solution set of `vq-ur=h` is not generated by `(u,v)`, or more than three integer values of `t` satisfying `M/2<q_0+ut<=2M` with `u>M/2`.

## Dependencies

- `VIS-315`: identifies a Fourier-resolution cell with a thin determinant strip around a represented same-shell prime ratio.
- `VIS-316`: shows that only the taper-weighted shell occupancy profile is needed globally.
- `VIS-317`: shows that scalar determinant projection erases the odd-prime forbidden residue classes needed for a direct determinant-value sieve.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining pair-preserving local-density/energy frontier.

## Research consequence

The pair-preserving frontier has narrowed again. The route “fix `h`, parametrize by two affine linear forms, then obtain the missing two-prime density factor from a long one-dimensional sieve” is not available at represented same-shell slopes because the affine parameter has only bounded length.

The next useful density argument must therefore preserve both prime coordinates **and** aggregate over the family of determinant slices, or bypass worst-cell density through weighted energy. This is a more precise target than either determinant-only sieving or slice-by-slice affine-form sieving.