# VIS-314 — Selberg prime-pair sieve removes one logarithm from Wang shell energy

## Claim

Keep the notation and cutoff-free near/far decomposition of `VIS-313`. Thus

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`,

and the nonzero ratio frequencies in the strict near band `0<|lambda|<log 2` are cross-base prime-power ratios. For a dyadic arithmetic-height shell `M<max(q,r)<=2M`, let

`E_M=sum_(lambda in shell M) |B_lambda|^2`

be the shell energy used in `VIS-313`, and put

`v_x(M)=min(M/x,x/M)`.

Then the coarse shell estimate inherited there from `VIS-307`,

`E_M << M v_x(M)^4 log^3(4M)`,

can be sharpened by one logarithm:

`E_M << M v_x(M)^4 log^2(4M)`.

Consequently, with `L=log(3x)`, uniformly in starting point `T0` and interval length `V>0`,

`V^(-1) integral_(T0)^(T0+V) |R_near(T)|^2 dT`
` << x L^2 + x^3 L^2/V`,

and after recombining the unchanged far band from `VIS-313`,

`V^(-1) integral_(T0)^(T0+V) |R_(x,H)(T)|^2 dT`
` << x^2 + x L^2 + x^3 L^2/V`.

At the active Wang scale

`H asymp x ell`, `ell=log log(3x)`,

the normalized mean square is therefore

`H^(-2) V^(-1) integral |R_(x,H)(T)|^2 dT`
` << ell^(-2) + L^2/(x ell^2) + x L^2/(V ell^2)`,

so it is `o(1)` on the sufficient scale

`V >> x L^2/ell^2`.

This improves the `VIS-313` horizon by one factor of `log x`. The remaining gap to the natural local window `V asymp H asymp x ell` is still logarithmic, now roughly `L^2/ell^3`.

**Evidence/status:** `CLASSICAL SELBERG UPPER-BOUND SIEVE + EXACT-DERIVED SPECIALIZATION + CUTOFF-FREE SHELL-ENERGY IMPROVEMENT + PROOF-METHOD RESULT + NO-NOVELTY-CLAIM`.

No prime-pair asymptotic, pointwise cancellation theorem, new sieve theorem, or stronger RH criterion is claimed.

## 1. The old third logarithm came from a pointwise weight majorant

For a near-band pair in one shell, `q` and `r` are comparable to `M`, and

`|log(q/r)| asymp |q-r|/M`.

Since

`a_q^2=[Lambda(q)^2/q] v_x(q)^2`,

and `v_x(q),v_x(r)` differ from `v_x(M)` only by absolute factors on the shell, the kernel bound from `VIS-307` gives

`E_M`
` << v_x(M)^4 sum_(q!=r; shell M) Lambda(q)^2 Lambda(r)^2/(q-r)^2`.

`VIS-307` bounded one von-Mangoldt square pointwise by `O(log^2 M)` and then summed the other one by `sum Lambda(n)^2<<M log M`. That is exactly where the factor `log^3 M` entered. At the present frontier it is worth retaining the two-point sparsity instead of paying those two estimates independently.

## 2. Prime-prime pairs save one logarithm by the classical dimension-two sieve

Write `h=|q-r|`. For the contribution where both variables are ordinary primes, the standard Selberg upper-bound sieve for the pair of linear forms `n,n+h` gives, uniformly for nonzero `|h|=O(M)`,

`N_h(M) := #{p in a fixed enlarged M-shell : p and p+h are prime}`
` << [M/log^2(3M)] S_2(h)`,

where for even `h`

`S_2(h) << prod_(p|h, p>2) (p-1)/(p-2)`

and odd `h` contributes only the irrelevant parity exceptions (none in a sufficiently large comparable shell). Constants absorb the finite small-`M` cases and the fixed enlargement of the shell.

For each such prime pair,

`Lambda(q)^2 Lambda(r)^2 << log^4(3M)`.

Hence, at fixed `h`,

`sum_(q-r=+/- h; q,r prime) Lambda(q)^2 Lambda(r)^2`
` << M log^2(3M) S_2(h)`.

The singular factor is harmless against the squared gap kernel. Indeed `S_2` is multiplicative up to the fixed parity factor and its extra local factor at a prime divisor is `1+O(1/p)`, so

`sum_(h>=1) S_2(h)/h^2 < infinity`.

Therefore the whole prime-prime part of the shell satisfies

`<< M log^2(3M)`,

and after restoring the Wang taper,

`E_M^(prime-prime) << M v_x(M)^4 log^2(3M)`.

The saving is not a new prime-correlation theorem. It is the familiar `M/log^2 M` upper-sieve density of two simultaneous primes cancelling two of the four logarithms supplied by the squared von-Mangoldt weights.

## 3. Proper prime powers are lower order

It remains to include pairs in which at least one of `q,r` is a proper prime power. There are only `O(M^(1/2))` proper prime powers in a comparable interval of scale `M`.

Fix such a `q`. Crude integer separation is now sufficient:

`sum_(r!=q; r prime power, comparable) Lambda(r)^2/(q-r)^2`
` << log^2(3M) sum_(h!=0) h^(-2)`
` << log^2(3M)`.

Since also `Lambda(q)^2<<log^2(3M)`, summing over all proper prime powers gives

`<< M^(1/2) log^4(3M)`.

For all sufficiently large `M` this is `O(M log^2(3M))`; the bounded initial range is absorbed into the implied constant. Double-proper-power pairs are already contained in this estimate. Thus

`E_M << M v_x(M)^4 log^2(4M)`

for the full prime-power shell.

## 4. Replaying the cutoff-free shell recombination

The only change to `VIS-313` is the shell energy. Its separated-frequency mean-value step remains

`V^(-1) integral |F_M(T)|^2 dT`
` << (1+M^2/V) E_M`.

With the improved estimate,

`E_M^(1/2) << M^(1/2) v_x(M)^2 log(4M)`.

The dyadic sums now give

`sum_M E_M^(1/2) << x^(1/2) L`,

`sum_M M E_M^(1/2) << x^(3/2) L`.

Minkowski therefore yields

`||R_near||_(L^2_V)`
` << x^(1/2) L + x^(3/2) L/V^(1/2)`,

and hence

`V^(-1) integral |R_near(T)|^2 dT`
` << x L^2 + x^3 L^2/V`.

The far-band argument of `VIS-313` is unchanged: `sup_T |R_far(T)|<<x`. Recombination gives

`V^(-1) integral |R(T)|^2 dT`
` << x^2 + x L^2 + x^3 L^2/V`.

At `H asymp x ell`, division by `H^2` proves the announced sufficient horizon

`V >> x L^2/ell^2`.

## Prior art and novelty boundary

The load-bearing new input relative to `VIS-313` is entirely classical sieve theory. Hugh L. Montgomery and Robert C. Vaughan, **Multiplicative Number Theory II: Primes and Sieves**, Cambridge University Press (2026), Chapter 21, *Sieves of Fixed Dimension and Applications*, DOI `10.1017/9781009445030.007`, is a current reference for fixed-dimensional upper-bound sieves. Ben Green and Terence Tao, **Restriction theory of the Selberg sieve, with applications**, *Journal de Théorie des Nombres de Bordeaux* 18:1 (2006), 147--182, DOI `10.5802/jtnb.538`, explicitly treats Selberg-sieve majorants for primes and twin-prime/prime-tuple patterns.

The separated-frequency mean-value inequality and the dyadic recombination are the same classical Montgomery--Vaughan machinery already recorded in `VIS-313`. No novelty is claimed for the prime-pair sieve estimate or for summability of its singular factor. The Mathia-specific content is the observation that applying the two-point sieve before discarding Wang's von-Mangoldt weights removes exactly one logarithm from the current cutoff-free finite-window bound.

## Boundaries and falsification

This remains a sufficient **mean-square-in-starting-height** result. It does not prove `R_(x,H)(T)=o(H)` for every `T`, does not justify a joint moving `x(T)` limit, and does not show that the residual logarithmic loss is intrinsic.

The sieve is used only as an upper bound. No Hardy--Littlewood prime-pair asymptotic, lower bound, or unproved prime-pair hypothesis enters the result.

The shell must remain in the strict cross-base near band from `VIS-313`; same-base harmonic frequencies are assigned to the far band there. The proper-prime-power estimate is intentionally crude and only needs their `O(M^(1/2))` sparsity.

Falsify the finding by finding a failure of the stated dimension-two upper-sieve bound in the required uniform `|h|=O(M)` range, divergence of `sum S_2(h)/h^2`, an overlooked prime-power contribution exceeding `M log^2 M`, or an error when inserting the improved shell energy into the `VIS-313` Montgomery--Vaughan/Minkowski recombination.

## Dependencies

- `VIS-307`: original `M v_x(M)^4 log^3 M` shell-energy calculation.
- `VIS-313`: cutoff-free near/far decomposition and dyadic separated-frequency recombination.
- `CLUE-wang-fixed-source-packet-localization`: accepted localization clue whose remaining upper-source frontier is the logarithmic finite-window gap.

## Research consequence

The first residual logarithm in `VIS-313` is not structural: it came from forgetting prime-pair sparsity while estimating the squared von-Mangoldt shell energy. Classical two-dimensional sieve control lowers the sufficient finite-window horizon from

`V >> x log^3 x/(log log x)^2`

to

`V >> x log^2 x/(log log x)^2`.

The next useful step should therefore not repeat two-point prime-pair counting. To reach `V asymp x log log x`, one must remove a further factor of roughly `log^2 x/(log log x)^3`, most plausibly by improving the shellwise `M^2/V` aggregate frequency-density cost, exploiting cancellation across shells, or isolating a genuine exceptional-height coherence mechanism. The remaining obstruction has moved from crude two-point coefficient mass to the organization of many ratio frequencies over finite windows.