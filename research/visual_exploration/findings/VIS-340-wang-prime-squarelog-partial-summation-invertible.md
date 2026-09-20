# VIS-340 — prime square-log summation is an invertible partial-summation image of the theta remainder

## Claim

Let

`theta(x)=sum_(p<=x) log p`

and

`G(u)=e^(-u)theta(e^u)-1`,

as in `VIS-339`. Define the prime-only squared-log summatory function

`A_prime(x)=sum_(p<=x) (log p)^2`

and, for `u>=log 2`, its normalized remainder relative to the natural main term,

`P(u)=e^(-u)[A_prime(e^u)-e^u(u-1)]`.

Then classical Stieltjes/Abel partial summation gives the exact identity

`P(u)=uG(u)-H(u)+2e^(-u)`,

where

`H(u)=e^(-u) integral_(log 2)^u e^v G(v) dv`.

Thus the passage from the Chebyshev-theta remainder to the prime-only squared-log summatory remainder is only multiplication by `u` followed by subtraction of a one-sided exponential average and an explicit endpoint term.

This map is exactly invertible. Put

`P_0(u)=P(u)-2e^(-u)`.

Then

`H(u)=u e^(-u) integral_(log 2)^u [e^v/v^2] P_0(v) dv`

and therefore

`G(u)=P_0(u)/u + e^(-u) integral_(log 2)^u [e^v/v^2] P_0(v) dv`.

For Wang's full squared-von-Mangoldt summatory remainder from `VIS-333`,

`F(u)=e^(-u)[A(e^u)-e^u(u-1)]`,

one has

`F(u)=P(u)+R_pp(u)`,

where the proper-prime-power summatory correction satisfies

`R_pp(u)=O(u^2 e^(-u/2))`.

Consequently, after the exponentially smaller proper-prime-power correction is removed, the normalized `Lambda^2` summatory source used by Wang and the normalized Chebyshev-theta remainder carry the same information through an explicit causal first-order transform.

There is also a useful envelope consequence. Let

`V(u)=u^(3/5)(log u)^(-1/5)`

and suppose, for some fixed `c>0`, that

`|G(u)| <= C exp(-c V(u))`

for all sufficiently large `u`. Then

`H(u)=O(exp(-c V(u)))`

and hence

`F(u)=uG(u)+O(exp(-c V(u)))+O(u^2 e^(-u/2))`.

Equivalently,

`F(u)/u = G(u)+O(exp(-c V(u))/u)+O(u e^(-u/2))`.

Therefore at any sequence of heights on which `|G(u)|` occupies a fixed positive fraction of that envelope, the passage from theta error to Wang's normalized summatory source preserves its sign and leading scale after division by `u`. **Partial summation itself cannot manufacture an envelope-scale pointwise gain.**

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PARTIAL-SUMMATION SPECIALIZATION + SOURCE-SPECIFIC NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new estimate for `theta(x)-x`, no improvement of the Korobov--Vinogradov remainder, no nonstationarity theorem, and no RH consequence is claimed.

## 1. Exact prime-only partial-summation map

Since `theta` is the staircase with jump `log p` at each prime,

`A_prime(x)=integral_(2-)^x log t d theta(t)`.

Stieltjes integration by parts gives, exactly for `x>=2`,

`A_prime(x)=log x theta(x)-integral_2^x theta(t)/t dt`.

Set `x=e^u` and use

`theta(e^v)=e^v[1+G(v)]`.

The integral becomes

`integral_2^(e^u) theta(t)/t dt`
` = integral_(log 2)^u theta(e^v) dv`
` = e^u-2 + integral_(log 2)^u e^v G(v) dv`.

Therefore

`A_prime(e^u)`
` = u e^u[1+G(u)] - e^u + 2 - integral_(log 2)^u e^v G(v) dv`
` = e^u(u-1) + u e^u G(u) + 2 - integral_(log 2)^u e^v G(v) dv`.

Dividing the remainder by `e^u` yields

`P(u)=uG(u)-H(u)+2e^(-u)`

with the stated `H`.

This is an identity, not an asymptotic approximation.

## 2. The transform is causally invertible

By definition,

`H(u)=e^(-u) integral_(log 2)^u e^v G(v) dv`,

so

`H'(u)=G(u)-H(u)`

and `H(log 2)=0`.

After removing the explicit endpoint term,

`P_0(u)=uG(u)-H(u)`.

Hence

`G(u)=[P_0(u)+H(u)]/u`

and

`H'(u)+(1-1/u)H(u)=P_0(u)/u`.

The integrating factor is `e^u/u`, so

`d/du [(e^u/u)H(u)] = e^u P_0(u)/u^2`.

Using `H(log 2)=0` gives

`H(u)=u e^(-u) integral_(log 2)^u [e^v/v^2]P_0(v)dv`,

and substitution gives the displayed inverse for `G`.

Thus the prime-only summatory weighting `log p -> (log p)^2` and subsequent normalization do not introduce an independent arithmetic information channel. They only apply an explicitly invertible first-order integral transform to the same theta remainder already isolated in `VIS-339`.

## 3. Proper prime powers remain exponentially lower order

Write

`A(x)=sum_(n<=x) Lambda(n)^2`

and decompose

`A=A_prime+A_pp`,

where

`A_pp(x)=sum_(p^k<=x, k>=2) (log p)^2`.

Then

`F(u)=P(u)+e^(-u)A_pp(e^u)`.

For `k=2`, discarding primality gives

`sum_(p<=e^(u/2)) (log p)^2 <= O(u^2 e^(u/2))`.

For every `k>=3`, the same elementary bound is at most `O(u^2 e^(u/k))`, and summing the admissible exponents contributes only an exponentially smaller term after multiplication by `e^(-u)`. Therefore

`e^(-u)A_pp(e^u)=O(u^2 e^(-u/2))`.

This is the summatory counterpart of the source/Green-response control in `VIS-338`. Proper prime powers remain present in the exact formula but are far below the live subexponential envelope.

## 4. Korobov--Vinogradov-scale envelopes survive the averaging step

Assume

`|G(u)| <= C B(u)`,

where

`B(u)=exp(-cV(u))`

and `V(u)=u^(3/5)(log u)^(-1/5)`.

Rewrite

`H(u)=integral_0^(u-log 2) e^(-s)G(u-s)ds`.

For `0<=s<=u/2`, the derivative of `V` on `[u/2,u]` tends uniformly to zero. Thus

`V(u)-V(u-s) <= epsilon_u s`

with `epsilon_u->0`, and therefore

`B(u-s) <= B(u) exp(c epsilon_u s)`.

The contribution of this range is bounded by

`C B(u) integral_0^(u/2) exp(-(1-c epsilon_u)s)ds = O(B(u))`.

For `s>u/2`, the exponential kernel contributes `e^(-u/2)` while `G` is bounded on the remaining finite/controlled range, so this tail is `O(e^(-u/2))=o(B(u))`. Hence

`H(u)=O(B(u))`.

Substituting in the exact formula and adding the proper-prime-power correction gives

`F(u)=uG(u)+O(B(u))+O(u^2e^(-u/2))`.

In particular, if along a sequence `u_j->infinity`

`|G(u_j)| >= kappa B(u_j)`

for some fixed `kappa>0`, then

`F(u_j)/(u_j G(u_j)) -> 1`.

So at envelope-saturating heights the prime square-log summation step preserves the theta remainder rather than suppressing it. Any smaller Wang output must come from the later nonvanishing Wang filter acting on genuinely nonstationary structure, not from the elementary transition `theta -> sum_(p<=x)(log p)^2`.

## 5. Prior art and evidence boundary

Partial summation / Abel summation for prime sums is classical. Tom M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976, is a standard reference for this machinery. The standard Chebyshev function itself is recorded, for example, in the *Encyclopedia of Mathematics* entry **Chebyshev function**:

`https://encyclopediaofmath.org/wiki/Chebyshev_function`.

The exact identity

`sum_(p<=x)(log p)^2 = log x theta(x)-integral_2^x theta(t)/t dt`

is the direct partial-summation specialization with weight `log t`. The integrating-factor inversion in logarithmic coordinates is elementary first-order calculus. No novelty is claimed for either ingredient.

The Mathia-specific value is as a control on the surviving Wang branch. `VIS-339` shows that the centered prime source measure is already a differential image of `G`; the current finding shows that Wang's normalized summatory `Lambda^2` source is, up to exponentially smaller proper prime powers, likewise an invertible partial-summation image of `G`. Atomic packets, prime square-log weighting, and summatory normalization therefore do not create a new arithmetic source before Wang's actual filter is applied.

The finding does not rule out a genuinely nonstationary property of `G`, and it does not show that Wang's filter cannot attenuate such a property. It only prevents crediting the theta-to-summatory-source conversion itself with the desired gain.

## Dependencies

- `VIS-291`: records the live Korobov--Vinogradov envelope shape used as the source-scale benchmark.
- `VIS-333`: defines the normalized summatory remainder `F` and Wang's exact nonvanishing log-frequency transfer.
- `VIS-338`: proper prime powers are collectively exponentially negligible at the live source scale.
- `VIS-339`: the surviving centered prime source is exactly the weighted differential image `u(1+D)G`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose source-level search is narrowed here.

## Research consequence

The accepted Wang clue can be narrowed one step further. Before Wang's low-pass filter is applied, both natural descriptions of the surviving arithmetic source — the centered prime measure and the normalized squared-log summatory remainder — are explicitly recoverable from the same Chebyshev-theta remainder.

The remaining source question is therefore not whether prime weighting or partial summation creates useful smoothing. It is whether `G` itself contains a genuinely nonstationary or scale-migrating component that Wang's nonvanishing one-order filter attenuates pointwise, while the complete destination avoids paying that gain back through `Q'` or equivalent unsmoothed information.