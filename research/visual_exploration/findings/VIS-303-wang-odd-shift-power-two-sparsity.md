# VIS-303 — Wang's odd-shift off-diagonal sector is power-of-two sparse

## Claim

Let

`I=(T,T+H]`,

and let Wang's Dirichlet polynomial be

`D_x(t)=sum_(n>=2) a_n n^(-it)`,

with

`a_n=(Lambda(n)/sqrt(n)) min(n/x,x/n)`.

Write

`D_x=D_2+D_o`,

where `D_2` contains exactly the terms `n=2^k`, `k>=1`, and `D_o` contains the odd prime-power terms. Since `Lambda(n)` vanishes away from prime powers, this is the complete parity decomposition of the nonzero coefficient support.

Put

`R_x = integral_I |D_x(t)|^2 dt - H sum_n a_n^2`

and define `R_o` analogously for `D_o`.

Then, as `x->infinity`,

`sum_(k>=1) a_(2^k)^2 << 1/x`,

and

`sum_(k>=1) 2^k a_(2^k)^2 << 1`.

Consequently, in every moving-source regime satisfying

`x log(2x) = O(H)`,

one has

`R_x = R_o + o(H)`.

Equivalently, at the current `H`-resolution boundary `x log x asymp H`, the entire off-diagonal sector with odd additive difference `|m-n|` is negligible. Every potentially `H`-scale off-diagonal contribution is therefore carried by pairs of **odd prime powers**, and hence by **even additive differences**.

**Evidence/status:** `EXACT-DERIVED + ARITHMETIC PARITY REDUCTION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not estimate the surviving even-shift sector, improve a shifted-prime theorem, or prove that the boundary `x log x asymp H` is sharp. It only removes one complete arithmetic sector from the live boundary problem.

## 1. Opposite parity is exactly the power-of-two cross sector

The coefficient support is the set of prime powers because `Lambda(n)` is zero otherwise. Every even prime power is a power of two. Therefore a nonzero coefficient pair `(m,n)` has odd difference if and only if exactly one of `m,n` is a power of two and the other is an odd prime power.

Expanding the energy gives

`integral_I |D_x|^2`
` = integral_I |D_2|^2`
`   + integral_I |D_o|^2`
`   + 2 Re integral_I D_2 overline(D_o)`.

The last term is not merely a convenient subterm: it is exactly the full opposite-parity, hence odd-additive-shift, off-diagonal sector. The self-interactions of `D_2` and `D_o` both have even additive difference.

## 2. The power-of-two coefficient mass is sparse

For `q=2^k`, one has `Lambda(q)=log 2`. Hence

`a_q^2 = (log 2)^2 q/x^2` for `q<=x`,

and

`a_q^2 = (log 2)^2 x^2/q^3` for `q>x`.

The dyadic geometric sums therefore give

`E_2(x):=sum_(q=2^k) a_q^2`
` << x^(-2) sum_(q<=x, q=2^k) q`
`    + x^2 sum_(q>x, q=2^k) q^(-3)`
` << 1/x`.

Likewise the coefficient weight entering the Montgomery--Vaughan mean-value remainder satisfies

`M_2(x):=sum_(q=2^k) q a_q^2`
` << x^(-2) sum_(q<=x, q=2^k) q^2`
`    + x^2 sum_(q>x, q=2^k) q^(-2)`
` << 1`.

Thus the only even part of the von-Mangoldt support has vanishing diagonal mass and uniformly bounded mean-value error weight.

## 3. The odd-shift cross term is `o(H)` at the live boundary

Apply the same Montgomery--Vaughan mean-value theorem used by Wang to the two sub-polynomials, with the omitted coefficients set to zero. Section 2 gives

`integral_I |D_2(t)|^2 dt << H/x + 1`.

For `D_o`, positivity of the coefficient moments and `VIS-302` give

`sum_(n odd prime power) a_n^2 << log(2x)`

and

`sum_(n odd prime power) n a_n^2 << x log(2x)`.

Therefore

`integral_I |D_o(t)|^2 dt << H log(2x) + x log(2x)`.

Assume now `x log(2x)=O(H)`. Cauchy--Schwarz yields

`|integral_I D_2 overline(D_o)|`
` << [(H/x+1) H log(2x)]^(1/2)`.

After division by `H`, the square of the right-hand side is

`<< log(2x)/x + log(2x)/H`,

which tends to zero because `x->infinity` and `x log(2x)=O(H)`. Hence

`integral_I D_2 overline(D_o) = o(H)`.

The Montgomery--Vaughan estimate for `D_2` also gives

`integral_I |D_2|^2 - H E_2(x) = O(M_2(x)) = O(1)`.

Subtracting the diagonals in the full decomposition therefore gives

`R_x = R_o + o(H)`.

No cancellation hypothesis for primes is used in this reduction.

## 4. What remains at `x log x asymp H`

The live upper-source question in `CLUE-wang-fixed-source-packet-localization` asks whether the actual off-diagonal mean-value remainder at `x log x asymp H` is `o(H)`, contains a stable `H`-scale correction, or can attain `H` scale under an admissible control.

This finding removes all pairs with odd additive difference from that question. The surviving remainder can be organized entirely through pairs of odd prime powers

`m=p^a`, `n=q^b`, with `p,q` odd,

so `m-n` is even. Any further analysis of the boundary should therefore preserve the exact interval kernel and frequencies `log(m/n)` while grouping, when useful, by even shifts `m-n=2r`. A model whose apparent obstruction is driven mainly by opposite parity cannot be sharp for Wang's actual coefficient support.

## Prior art and evidence boundary

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the coefficient sequence and the Montgomery--Vaughan mean-value step used here. `VIS-302` already audits that application and sharpens Wang's coefficient moment from `O(x log^2 x)` to its natural `x log x` scale.

The present parity split uses only the classical support property of the von Mangoldt function, `Lambda(p^k)=log p`, elementary dyadic geometric sums, the same mean-value theorem, and Cauchy--Schwarz. No novelty is claimed for any of those ingredients or for parity decompositions of prime-power sums. The Mathia-specific consequence is the exact localization of the currently exposed Wang boundary: odd additive shifts cannot supply an `H`-scale remainder there.

The result says nothing about cancellation among the surviving even shifts. In particular it does not imply a Hardy--Littlewood-type asymptotic, does not distinguish prime pairs from general odd-prime-power pairs, and does not turn the proof boundary into an arithmetic transition.

## Dependencies

- `VIS-302`: coefficient moments and identification of `x log x asymp H` as the first unresolved generic interior scale.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue defining the actual off-diagonal remainder as the live upper-source test.

## Research consequence

At `H` resolution, replace the unrestricted off-diagonal Wang problem by its **odd-prime-power/even-shift sector**. The next decisive calculation should inspect the exact interval-kernel sum over those surviving pairs rather than spending effort on powers of two or odd additive shifts, which are already `o(H)` at the current boundary.