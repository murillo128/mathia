# VIS-339 — Wang's prime-only source is a weighted differential image of the Chebyshev theta remainder

## Claim

Let

`theta(x)=sum_(p<=x) log p`

be Chebyshev's first function and define, for `u>0`,

`G(u)=e^(-u) theta(e^u)-1`.

Retain the prime-only part of Wang's logarithmic source from `VIS-338`,

`mu_prime=sum_p [(log p)^2/p] delta_(log p)`,

and its centered signed source

`nu_prime=mu_prime-u du`.

Then, in the sense of distributions on `(0,infinity)`,

`nu_prime = u(1+D)G`,

where `D=d/du`.

Thus the entire surviving `k=1` source after `VIS-338` is not a new arithmetic information channel independent of the prime-number-theorem remainder. It is exactly a first-order weighted differential image of the normalized Chebyshev-theta error.

More precisely, for every compactly supported `C^1` test function `phi` on `(0,infinity)`,

`integral phi(u) nu_prime(du)`
` = integral [(u-1)phi(u)-u phi'(u)] G(u) du`.

Conversely, for `0<a<u`,

`G(u)=e^(-(u-a))G(a)+e^(-u) integral_(a,u] [e^v/v] nu_prime(dv)`.

So, after one boundary value is fixed, `G` and `nu_prime` determine each other exactly.

Combining this with the exact Wang equation from `VIS-337` and the decomposition from `VIS-338` gives

`(4-D^2)Q = 4u(1+D)G + 4 mu_pp`,

where `mu_pp` is the proper-prime-power source. Since `VIS-338` proves that `mu_pp` and its Wang response are exponentially negligible at the live Korobov--Vinogradov scale, the unresolved source-specific branch is precisely a question about nonstationary structure of the normalized Chebyshev-theta remainder and how Wang's filter redistributes that structure.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CHEBYSHEV/ABEL REPRESENTATION + SOURCE-SPECIFIC NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No improved estimate for `theta(x)-x`, no new prime-number theorem remainder, no frequency-migration theorem, and no RH consequence is claimed.

## 1. Exact differential representation

Put

`T(u)=theta(e^u)`.

`T` is a right-continuous staircase whose jump at `u=log p` is `log p`. Distributionally,

`D T = sum_p (log p) delta_(log p)`.

Since

`G=e^(-u)T-1`,

the product rule gives

`D G`
` = -e^(-u)T du + e^(-u)D T`
` = -(G+1)du + sum_p [(log p)/p] delta_(log p)`.

Therefore

`(1+D)G`
` = -du + sum_p [(log p)/p] delta_(log p)`.

Multiplying this measure by the log-coordinate `u` gives

`u(1+D)G`
` = -u du + sum_p [(log p)^2/p] delta_(log p)`
` = nu_prime`,

because the coordinate of the atom is exactly `u=log p`.

This identity is exact and uses no asymptotic input.

## 2. Every smooth prime packet is a theta-error functional

Let `phi` be `C^1` with compact support in `(0,infinity)`. From

`nu_prime=u G du + u dG`,

Stieltjes integration by parts yields

`integral phi d nu_prime`
` = integral phi u G du + integral phi u dG`
` = integral [(u-1)phi-u phi'] G du`.

So a smooth block, phase, taper, wave packet, or multiscale linear statistic of the centered prime source is already an exact weighted functional of `G`.

For an interval `(a,b]` whose endpoints are not prime logarithms, the specialization `phi=1` gives

`nu_prime((a,b])`
` = bG(b)-aG(a) + integral_a^b (u-1)G(u)du`.

At prime-log endpoints the same statement holds with the corresponding one-sided boundary convention.

This does not say that every useful nonlinear property of the primes is trivial. It says that the current **linear source channel actually entering Wang's resolvent** contains exactly the same information as this weighted differential form of the Chebyshev-theta remainder. Calling a visually or spectrally attractive packet a new source mechanism is therefore premature unless its translated statement about `G` is itself nontrivial.

## 3. The representation is invertible after one boundary value

From

`(1+D)G = u^(-1) nu_prime`,

multiply by `e^u` to obtain

`D(e^u G)=e^u u^(-1) nu_prime`.

Integrating from `a` to `u` gives

`e^u G(u)-e^a G(a)`
` = integral_(a,u] [e^v/v] nu_prime(dv)`,

which is the displayed inversion formula.

Hence the map is not merely a one-way estimate or a lossy smoothing. On any positive log interval, the centered prime source and the normalized theta remainder are equivalent up to the natural single boundary datum of a first-order equation.

This is a useful control for the accepted Wang clue. A proposed collective prime organization cannot acquire independent evidential status merely by being expressed as atoms, packets, phases, or a source measure: if it enters through `nu_prime`, it can be translated exactly back to `G`.

## 4. Consequence for the Wang frontier

`VIS-337` gives

`(4-D^2)Q=4(mu-u du)`.

`VIS-338` splits

`mu=mu_prime+mu_pp`

and proves that the complete proper-prime-power source `mu_pp`, including its Green response and derivative jumps, is exponentially below the live PNT envelope. Substitution of the present identity therefore yields

`(4-D^2)Q = 4u(1+D)G + 4mu_pp`.

The remaining source question is consequently sharper than "do many prime atoms form a useful packet?" A positive mechanism must identify a genuine nonstationary or multiscale property of `G` strong enough that the nonvanishing Wang filter makes `Q` smaller while the derivative channel carries the missing source scale. A packet construction that only repackages the exact test-function identity above has not found new cancellation.

The destination question remains independent. Even if such a property of `G` exists, Wang's complete final error decomposition must still exploit the smaller `Q` without reintroducing `Q'` or another unsmoothed quantity that repays the gain under `VIS-334`.

This finding therefore narrows, but does not resolve, `CLUE-wang-fixed-source-packet-localization`.

## 5. Prior art and evidence boundary

The Chebyshev function

`theta(x)=sum_(p<=x) log p`

is classical; the *Encyclopedia of Mathematics* entry **Chebyshev function** records the standard definition and relation to prime distribution:

`https://encyclopediaofmath.org/wiki/Chebyshev_function`.

The passage between a weighted prime sum and its cumulative Chebyshev function is classical Abel summation / summation by parts. The *Encyclopedia of Mathematics* entry **Abel transformation** records the standard discrete integration-by-parts identity:

`https://encyclopediaofmath.org/wiki/Abel_transformation`.

The distributional formulas here are the log-coordinate/Stieltjes form of that standard machinery. No novelty is claimed for Chebyshev functions, partial summation, integrating factors, or first-order distributional calculus.

The Mathia-specific contribution is the exact identification of the **currently surviving Wang prime-only source** with `u(1+D)G`, together with the resulting control on what can count as a genuinely new packet-localization mechanism after `VIS-337` and `VIS-338`.

The identity does not prove that `G` lacks source-envelope-scale nonstationary structure. It does not prove that Wang's output cannot be smaller than the source remainder, nor that derivative repayment necessarily destroys every possible downstream gain. Those are the live questions.

## Dependencies

- `VIS-292`: exact Green-resolvent representation of Wang's weighted prime-power source.
- `VIS-334`: exact causal inverse and first-derivative repayment boundary.
- `VIS-337`: exact source equation and prime-power derivative jumps.
- `VIS-338`: proper prime powers are collectively exponentially negligible at the live envelope scale.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose surviving source question is narrowed here.

## Research consequence

The next source-level test should be formulated directly on

`G(u)=e^(-u)theta(e^u)-1`.

Before crediting any smooth prime packet, phase, taper, or multiscale statistic as new structure, translate it through

`integral phi d nu_prime = integral [(u-1)phi-u phi']G du`.

Only a property of `G` that survives this exact quotienting and yields a source-envelope-scale distinction remains a genuine candidate. If such a property is found, the separate Wang destination-level derivative-repayment audit still has to pass.