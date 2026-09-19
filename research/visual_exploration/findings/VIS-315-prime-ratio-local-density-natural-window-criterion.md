# VIS-315 — natural Wang windows reduce to local density of prime-ratio frequencies

## Claim

Keep the cutoff-free near/far decomposition of `VIS-313` and the prime-pair shell energy improvement of `VIS-314`. For a dyadic arithmetic-height shell `M`, let

`Lambda_M^pp = { log(q/r) : q,r prime, q!=r, M<max(q,r)<=2M, |log(q/r)|<log 2 }`

be the ordinary-prime part of the strict near band, and let

`F_M^pp(T)=sum_(lambda in Lambda_M^pp) B_lambda exp(-i lambda T)`.

Because `q/r` is reduced, every frequency in `Lambda_M^pp` has a unique oriented prime pair. Put

`E_M^pp=sum_(lambda in Lambda_M^pp)|B_lambda|^2`

and define the local frequency occupancy at resolution `1/V` by

`kappa_M(V)=sup_(theta in R) # { lambda in Lambda_M^pp : |lambda-theta|<=2/V }`.

Then, uniformly in the starting point `T0`, one has the deterministic local-density large-sieve bound

`V^(-1) integral_(T0)^(T0+V) |F_M^pp(T)|^2 dT << kappa_M(V) E_M^pp`.

Moreover, any nonempty cluster counted by `kappa_M(V)` can be centered, up to an absolute enlargement of the window, at one represented ratio `u/v` from the same shell. Since all four primes are then `asymp M`, the cluster condition is equivalent up to absolute constants to the thin determinant condition

`|qv-ur| << M^2/V`.

Thus the unresolved finite-window cost is not intrinsically a minimum-spacing problem. It is a **local density problem for prime ratios**, or equivalently a count of prime lattice points in thin determinant strips around represented rational directions.

Write `L=log(3x)` and `ell=log log(3x)`. Suppose that, for the finite-window length `V` under consideration, there is a factor `A=A(x,V)>=1` such that for every dyadic shell

`kappa_M(V) << 1 + A M^2/(V log^2(4M))`.

Then the full Wang remainder satisfies

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + A x^3/V + x^(1/2) L^4 + x^(5/2) L^4/V`.

Consequently, at the active boundary

`H asymp x ell`, `V asymp x ell`,

the normalized mean square is

`H^(-2) V^(-1) integral |R_(x,H)(T)|^2 dT`
` << ell^(-2) + L^2/(x ell^2) + A/ell^3`
`    + L^4/(x^(3/2) ell^2) + L^4/(x^(1/2) ell^3)`.

Hence the natural local window is sufficient whenever

`A(x,x ell)=o(ell^3)`.

In particular, an essentially average-density bound

`kappa_M(V) << 1 + M^2/(V log^2 M)`

would remove the remaining logarithmic finite-window tariff of `VIS-314` at the level of mean square in starting height.

**Evidence/status:** `EXACT-DERIVED REDUCTION + CONDITIONAL SUFFICIENT CRITERION + PROOF-METHOD FRONTIER + NO-NOVELTY-CLAIM`.

No such uniform prime-ratio occupancy estimate is proved here. No pointwise Wang asymptotic, moving-`x(T)` theorem, prime-pair asymptotic, or stronger RH criterion is claimed.

## 1. Local occupancy replaces worst spacing

Order the frequencies in `Lambda_M^pp`. By definition of `kappa_M(V)`, no interval of length `4/V` contains more than `kappa_M(V)` of them. Color the ordered frequencies cyclically with `kappa_M(V)` colors. Two frequencies of the same color are then separated by more than `4/V`: otherwise the endpoints together with the intervening frequencies would put `kappa_M(V)+1` points in one interval of length `4/V`.

For each color class, the classical Montgomery--Vaughan separated-frequency mean-value inequality therefore gives

`V^(-1) integral |sum_(lambda in class) B_lambda exp(-i lambda T)|^2 dT`
` << sum_(lambda in class)|B_lambda|^2`,

uniformly in the interval location. Applying Cauchy--Schwarz to the sum of the color classes gives one factor equal to the number of classes, so

`V^(-1) integral |F_M^pp(T)|^2 dT`
` << kappa_M(V) sum_lambda |B_lambda|^2`
` = kappa_M(V) E_M^pp`.

This is only the standard separated-frequency large sieve plus a coloring argument. Its role is conceptual: `VIS-313` paid the universal shell spacing `M^2/V` because it treated all reduced ratios as though the shell were as dense as the full Farey lattice. The correct deterministic replacement can instead depend on how many **actual prime-ratio frequencies** occupy one Fourier-resolution cell.

## 2. A frequency cell is a thin prime determinant strip

Every prime-prime ratio in the strict near shell satisfies

`M/2 < q,r <= 2M`.

Take a nonempty interval realizing, up to the supremum, `kappa_M(V)`, and choose one frequency `lambda_0=log(u/v)` from it. Every other frequency `lambda=log(q/r)` in that interval obeys

`|lambda-lambda_0| <= 4/V`.

Now

`lambda-lambda_0 = log(qv/(ur))`.

Both `qv` and `ur` are between absolute multiples of `M^2`. For `V>=1`, the mean-value theorem for `log` therefore gives

`|log(qv/(ur))| << 1/V`
`  => |qv-ur| << M^2/V`.

Conversely, on the same compact ratio range, a bound

`|qv-ur| <= c M^2/V`

implies `|lambda-lambda_0| << 1/V`. Thus, up to harmless absolute changes in the window constant, `kappa_M(V)` is the maximal number of prime pairs in the shell lying in a determinant strip

`|qv-ur| << M^2/V`

around a represented prime-ratio direction `u/v`.

At the central shell `M asymp x` and natural window `V asymp x ell`, this becomes

`|q-(u/v)r| << 1/ell`.

So the missing estimate is a uniform simultaneous-prime, Beatty-like thin-strip count over slopes that themselves vary with `x` and are selected from prime ratios. The total number of prime-prime ratio frequencies in a central shell is of order at most the ambient `M^2/log^2 M` scale, so the quantity

`M^2/(V log^2 M)`

is exactly the naive average occupancy of a frequency cell of width `1/V`. The criterion above asks that the worst represented direction not exceed that average by more than the factor `A`.

## 3. Insert the VIS-314 shell energy

`VIS-314` proves for the ordinary-prime part

`E_M^pp << M v_x(M)^4 log^2(4M)`,

where

`v_x(M)=min(M/x,x/M)`.

Under the stated occupancy hypothesis,

`||F_M^pp||_(L^2_V)^2`
` << M v_x(M)^4 log^2(4M)`
`    + A M^3 v_x(M)^4/V`.

Taking square roots and summing the dyadic shells by Minkowski gives

`sum_M ||F_M^pp||_(L^2_V)`
` << x^(1/2) L + A^(1/2) x^(3/2) V^(-1/2)`.

Indeed, on `M<=x`, the two summands are dominated dyadically by

`M^(5/2) x^(-2) log(4M)`

and

`A^(1/2) V^(-1/2) M^(7/2) x^(-2)`,

while on `M>=x` they decay respectively like

`x^2 M^(-3/2) log(4M)`

and

`A^(1/2) V^(-1/2) x^2 M^(-1/2)`.

Thus the prime-prime strict-near component satisfies

`V^(-1) integral |R_near^pp(T)|^2 dT`
` << x L^2 + A x^3/V`.

The important cancellation is visible here: `VIS-314` supplies the two-prime density factor `log^(-2) M` inside `E_M^pp`, while the desired local-density estimate supplies the **second** `log^(-2) M` factor needed to cancel the `log^2 M` coefficient weight in the finite-window clustering cost.

## 4. Proper prime powers do not control the natural-window criterion

`VIS-314` isolates the contribution from near-band pairs with at least one proper prime power before absorbing it into the prime-prime shell bound. Its crude shell energy is

`E_M^pow << M^(1/2) v_x(M)^4 log^4(4M)`.

For this sparse remainder there is no need to assume a new local-density theorem. The universal reduced-ratio shell separation of `VIS-313` still gives

`||F_M^pow||_(L^2_V)^2`
` << (1+M^2/V) E_M^pow`.

Minkowski over dyadic shells therefore yields

`||R_near^pow||_(L^2_V)`
` << x^(1/4) L^2 + x^(5/4) L^2 V^(-1/2)`,

and hence

`V^(-1) integral |R_near^pow(T)|^2 dT`
` << x^(1/2) L^4 + x^(5/2) L^4/V`.

At `V asymp x ell` these terms are already negligible relative to `H^2 asymp x^2 ell^2`. The unresolved logarithmic tariff therefore belongs to clustering of the ordinary prime-prime ratio frequencies, not to the proper-prime-power tail.

## 5. Recombine with the far band

The far-ratio component of `VIS-313` is unchanged and satisfies pointwise

`|R_far(T)| << x`.

Combining the far band, the prime-prime near band, and the proper-power near band proves

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + A x^3/V`
`    + x^(1/2)L^4 + x^(5/2)L^4/V`.

At `H,V asymp x ell`, division by `H^2` gives the displayed normalized criterion. All terms except `A/ell^3` vanish unconditionally. Therefore an occupancy loss `A=o(ell^3)` is enough to close the current mean-square finite-window gap at the natural Wang scale.

This identifies a sharper decision boundary than “improve the large sieve.” One may now either prove such local density directly, replace it by a weighted/additive-energy inequality strong enough to imply the same shell bound, or exhibit represented slopes whose prime-ratio clusters force `A` to be at least of order `ell^3` and then test whether those clusters actually carry coherent Wang coefficient mass.

## Prior art and novelty boundary

The large-sieve step is classical. H. L. Montgomery and R. C. Vaughan, **The large sieve**, *Mathematika* 20 (1973), 119--134, DOI `10.1112/S0025579300004708`, and their separated-frequency Hilbert technology already underlie the finite-window estimates used in `VIS-313`. The coloring argument above is an elementary local-density packaging of that standard input, not a new large-sieve theorem.

A targeted literature audit also finds an established program of replacing uniform spacing by structural sparsity or energy. Roger C. Baker, Marc Munsch, and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68 (2022), 362--399, DOI `10.1112/mtk.12140`, derives large-sieve bounds depending on additive energy for sparse sequences. That paper is relevant prior-art orientation for an energy-based alternative to `kappa_M(V)`, but no theorem from it is asserted to apply directly to the logarithms of Wang prime ratios.

Prime distribution in Beatty-type sets is also classical. William D. Banks and Igor E. Shparlinski, **Prime numbers with Beatty sequences**, arXiv `0708.1015`, studies primes in fixed irrational Beatty sequences, and Glyn Harman, **Primes in Beatty sequences in short intervals**, *Mathematika* 62 (2016), 572--586, DOI `10.1112/S0025579315000376`, develops short-interval variants. By the statements audited here, these results do not directly provide the present uniform **two-prime** occupancy bound over moving slopes selected from prime ratios and windows of thickness `M/V`.

No novelty claim is made for local-density large-sieve principles, sparse-sequence energy methods, or Beatty-prime estimates. The durable Mathia contribution is the exact reduction of the residual `VIS-314` logarithmic tariff to a concrete prime-ratio occupancy scale and the proof that an `o((log log x)^3)` excess over average density suffices for the natural Wang mean-square window.

## Boundaries and falsification

The local occupancy estimate is a sufficient condition, not an established theorem. It may be false uniformly over represented slopes; arithmetic singularities or exceptional rational directions may create larger clusters.

The criterion controls mean square in starting height. Even if proved with `A=o(ell^3)`, it would not by itself give pointwise cancellation for every `T` or justify a moving `x(T)` pointwise theorem without an additional exceptional-set or maximal argument.

The reduction uses ordinary primes separately from proper prime powers. An overlooked proper-power shell contribution larger than the `VIS-314` bound would invalidate the stated global criterion.

Falsify the exact part by finding an error in the frequency-coloring argument, the equivalence between a `1/V` log-frequency cell and the determinant strip at dyadic height, the insertion of the `VIS-314` shell energy, the proper-power recombination, or the dyadic Minkowski sums.

## Dependencies

- `VIS-309`: the exact deterministic Wang ratio-frequency remainder and its long-time Bohr/Haar interpretation.
- `VIS-313`: cutoff-free near/far decomposition, dyadic ratio shells, and universal `M^(-2)` shell separation.
- `VIS-314`: prime-pair Selberg-sieve shell energy `M v_x(M)^4 log^2 M` and the lower-order proper-prime-power contribution.
- `CLUE-wang-fixed-source-packet-localization`: accepted localization clue whose moving upper-source frontier is the remaining finite-window logarithmic tariff.

## Research consequence

The remaining `VIS-314` gap is now attached to one explicit arithmetic object: the maximal number of prime ratios that can fall in a Fourier cell of width `1/V`, equivalently prime pairs in a thin determinant strip around another represented prime ratio.

At the natural window the target occupancy is essentially the average prime-ratio density, up to a factor `o((log log x)^3)`. Proving that bound, obtaining the same shell estimate from a sparse-energy large sieve, or constructing a genuine exceptional direction that violates it is the next coherent test. Another minimum-gap estimate or another two-point fixed-shift sieve does not address this boundary.