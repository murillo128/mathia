# VIS-316 — natural Wang windows need weighted shell occupancy, not uniform density

## Claim

Keep the ordinary-prime near-band notation of `VIS-315`. For each dyadic arithmetic-height shell `M`, let `kappa_M(V)` be the maximal number of prime-ratio frequencies in a log-frequency cell of width `O(1/V)`, and let

`v_x(M)=min(M/x,x/M)`.

Assume shell-dependent excess factors `A_M=A_M(x,V)>=0` such that

`kappa_M(V) << 1 + A_M M^2/[V log^2(4M)]`.

Define the scale weight

`w(r)=r^(7/2)` for `0<r<=1`,

`w(r)=r^(-1/2)` for `r>=1`,

and the weighted shell excess

`B(x,V)=sum_(M dyadic) w(M/x) sqrt(A_M)`.

Then the cutoff-free Wang remainder satisfies, with `L=log(3x)`,

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + x^3 B(x,V)^2/V`
`    + x^(1/2)L^4 + x^(5/2)L^4/V`,

uniformly in `T0`.

Consequently, at the natural local scale

`H asymp V asymp x ell`, `ell=log log(3x)`,

the normalized mean square is

`H^(-2) V^(-1) integral |R_(x,H)(T)|^2 dT`
` << ell^(-2) + L^2/(x ell^2) + B(x,V)^2/ell^3`
`    + L^4/(x^(3/2) ell^2) + L^4/(x^(1/2) ell^3)`.

Thus the natural Wang window does **not** require the uniform shell condition `A_M=o(ell^3)` from the simplified statement of `VIS-315`. It is enough that

`B(x,x ell)=o(ell^(3/2))`.

The uniform criterion is recovered because `sum_M w(M/x)=O(1)` on dyadic shells, but isolated or sparse bad shells may be much worse than average provided their scale weights make the square-root excess summable.

**Evidence/status:** `EXACT-DERIVED RECOMBINATION + WEIGHTED SUFFICIENT CRITERION + PROOF-METHOD FRONTIER + NO-NOVELTY-CLAIM`.

No prime-ratio density estimate is proved here. No pointwise Wang asymptotic, new large-sieve theorem, moving-`x(T)` theorem, or stronger RH criterion is claimed.

## 1. Keep the local-density excess shell by shell

`VIS-315` combines its local-density coloring argument with the prime-prime shell energy of `VIS-314` to give, for each dyadic shell,

`||F_M^pp||_(L^2_V)^2`
` << M v_x(M)^4 log^2(4M)`
`    + A_M M^3 v_x(M)^4/V`,

where

`||F||_(L^2_V)^2 = V^(-1) integral_(T0)^(T0+V) |F(T)|^2 dT`.

Taking square roots and using `sqrt(a+b)<=sqrt(a)+sqrt(b)`,

`||F_M^pp||_(L^2_V)`
` << M^(1/2) v_x(M)^2 log(4M)`
`    + V^(-1/2) sqrt(A_M) M^(3/2) v_x(M)^2`.

Minkowski therefore yields

`||R_near^pp||_(L^2_V)`
` << sum_M M^(1/2) v_x(M)^2 log(4M)`
`    + V^(-1/2) sum_M sqrt(A_M) M^(3/2) v_x(M)^2`.

The first sum is the same baseline as in `VIS-315` and is `O(x^(1/2)L)`.

## 2. The Wang taper supplies an explicit shell weight

Write `r=M/x`. Then

`M^(3/2) v_x(M)^2`
` = x^(3/2) r^(3/2) min(r,r^(-1))^2`
` = x^(3/2) w(r)`.

Hence

`sum_M sqrt(A_M) M^(3/2) v_x(M)^2`
` = x^(3/2) B(x,V)`.

So

`||R_near^pp||_(L^2_V)`
` << x^(1/2)L + x^(3/2) B(x,V)/V^(1/2)`.

Squaring and absorbing the cross term gives

`V^(-1) integral |R_near^pp(T)|^2 dT`
` << x L^2 + x^3 B(x,V)^2/V`.

This is the exact place where the uniform `A` used for exposition in `VIS-315` can be relaxed. The dyadic recombination sees `sqrt(A_M)` multiplied by a strongly scale-dependent taper, not `sup_M A_M`.

## 3. Only a weighted neighborhood of the central shell is expensive

For shells below the Wang scale, `M=2^(-j)x` with `j>=0`,

`w(M/x)=2^(-7j/2)`.

For shells above it, `M=2^j x`,

`w(M/x)=2^(-j/2)`.

Thus low shells are suppressed very strongly and high shells geometrically. The central shells `M asymp x` are the genuinely expensive region.

For example, one isolated upper shell `M=2^j x` may have excess as large as

`A_M=o(ell^3 2^j)`

without violating the natural-window criterion, while one isolated lower shell `M=2^(-j)x` may have

`A_M=o(ell^3 2^(7j))`.

These examples are only consequences of the sufficient criterion; they do not assert that such large occupancies actually occur. Their role is to show that a uniform worst-shell theorem is stronger than the Wang mean-square recombination needs.

## 4. Recombine the unchanged pieces

The far band remains pointwise `O(x)` as in `VIS-313`. The proper-prime-power near band remains controlled exactly as in `VIS-315`:

`V^(-1) integral |R_near^pow(T)|^2 dT`
` << x^(1/2)L^4 + x^(5/2)L^4/V`.

Combining these with the weighted prime-prime estimate proves

`V^(-1) integral |R_(x,H)(T)|^2 dT`
` << x^2 + xL^2 + x^3 B(x,V)^2/V`
`    + x^(1/2)L^4 + x^(5/2)L^4/V`.

At `H,V asymp x ell`, division by `H^2` gives the stated normalized bound. Every term except `B^2/ell^3` vanishes unconditionally, so

`B=o(ell^(3/2))`

is sufficient.

If a uniform bound `A_M<=A` holds, then the dyadic weight has bounded total mass:

`sum_(M<=x) (M/x)^(7/2) + sum_(M>=x) (x/M)^(1/2) << 1`.

Therefore `B<<sqrt(A)`, recovering the `A=o(ell^3)` criterion of `VIS-315` as a special case.

## Prior art and novelty boundary

No new large-sieve or sieve theorem is used. The shellwise local-density estimate is exactly the classical separated-frequency large-sieve/coloring input already audited in `VIS-315`, and the passage from shell estimates to the global remainder is ordinary Minkowski plus the existing Wang taper.

Sparse-sequence large sieves depending on structural energy are established prior art; Roger C. Baker, Marc Munsch, and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68 (2022), 362--399, DOI `10.1112/mtk.12140`, is a relevant general example already noted in `VIS-315`. Nothing from that paper is imported into the proof above.

The Mathia-specific content is only the exact bookkeeping consequence: the current Wang mean-square problem needs a taper-weighted dyadic profile of prime-ratio crowding, not a uniform occupancy theorem over every arithmetic-height shell.

## Boundaries and falsification

This remains a conditional sufficient criterion. It does not bound any `A_M`, prove average prime-ratio density, or exclude a central shell whose local crowding is too large.

The criterion is mean-square in starting height. It does not imply pointwise cancellation for every `T` and does not justify a moving `x(T)` pointwise theorem without an additional maximal or exceptional-set argument.

The shell-dependent occupancy hypothesis must hold for the same prime-prime frequency sets and Fourier resolution used in `VIS-315`. Moving a bad cluster into a neighboring shell by changing the dyadic convention can alter individual `A_M`; only an estimate stable under a fixed finite shift of the shell partition should be interpreted structurally. The global bound itself is unaffected up to absolute constants because neighboring shell weights are comparable.

Falsify the finding by finding an error in the shellwise square-root step, the identity `M^(3/2)v_x(M)^2=x^(3/2)w(M/x)`, the dyadic Minkowski recombination, the proper-power/far-band insertion, or the normalization at `H,V asymp x ell`.

## Dependencies

- `VIS-313`: cutoff-free near/far dyadic decomposition and Wang taper.
- `VIS-314`: prime-prime shell energy `M v_x(M)^4 log^2 M`.
- `VIS-315`: local prime-ratio occupancy large-sieve bound and natural-window reduction.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue owning the remaining finite-window question.

## Research consequence

The next prime-ratio density step can target the **weighted shell profile** instead of a uniform theorem. It is enough to control

`sum_M w(M/x) sqrt(A_M)`

at `o((log log x)^(3/2))` on `V asymp x log log x`.

This changes the most useful search target. A large occupancy excess in a remote shell is not automatically an obstruction; it matters only after multiplication by the Wang taper weight. Conversely, a persistent excess in the central shells `M asymp x` remains genuinely dangerous. Future determinant-strip or additive-energy estimates should therefore be evaluated against this weighted profile before paying for uniformity that the destination theorem does not use.