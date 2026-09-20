# VIS-334 — Wang's summatory-remainder filter has an exact causal inverse with a first-derivative tax

## Claim

Retain the notation of `VIS-333`:

`F(u)=e^(-u)E_A(e^u)`

for the normalized squared-von-Mangoldt summatory remainder, and

`Q(u)=S(e^u)-u+(3/4)e^(-2u)`

for Wang's adjusted source-profile remainder. Extend `F` by zero to `u<0`, and let `Q_ext` be the full-line convolution from `VIS-333`, so

`hat Q_ext(xi)=m(xi) hat F(xi)`

with

`m(xi)=4(1+i xi)/(4+xi^2)`.

Then the inverse multiplier factors exactly as

`1/m(xi)=(1-i xi)/4 + 3/[4(1+i xi)]`.

Hence, distributionally on the full line,

`F = (Q_ext-Q_ext')/4 + (3/4)(1+D)^(-1)Q_ext`,

where `D=d/du` and

`[(1+D)^(-1)q](u)=integral_(-infinity)^u e^(-(u-v))q(v)dv`.

Because the zero extension of `F` implies

`Q_ext(u)=Q(0)e^(2u)` for `u<0`,

the physical half-line has the exact causal inversion formula

`F(u)`
` = [Q(u)-Q'(u)]/4`
`   + [Q(0)e^(-u)]/4`
`   + (3/4) integral_0^u e^(-(u-v))Q(v)dv`

for `u>=0`, with derivatives interpreted almost everywhere or distributionally at the source breakpoints.

Consequently, let `phi` be eventually differentiable with `phi(u)->infinity` and

`0 <= phi'(u) <= eta < 1`

eventually. If

`Q(u)=O(e^(-phi(u)))`

and

`Q'(u)=O(e^(-phi(u)))`,

then

`F(u)=O(e^(-phi(u)))`.

Thus Wang's first-order smoothing cannot produce a smooth sublinear pointwise envelope that is absent from the normalized source remainder **unless the corresponding log-derivative pays for the gain**. In particular, for Korobov--Vinogradov-type sublinear exponents, any claimed transform-induced improvement that controls both `Q` and `Q'` at the improved scale transfers back to `E_A(x)/x` at that same scale.

**Evidence/status:** `EXACT-DERIVED + POINTWISE INVERSE + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not bound `Q'` from `Q`, improve the known squared-von-Mangoldt remainder, or rule out a genuinely high-frequency/nonstationary arithmetic mechanism.

## 1. Exact factorization of the inverse

`VIS-333` gives

`m(xi)=4(1+i xi)/(4+xi^2)`.

Writing `z=i xi`, one has

`1/m = (4-z^2)/[4(1+z)]`
`    = (1-z)/4 + 3/[4(1+z)]`.

Under the Fourier convention used in `VIS-333`, multiplication by `i xi` is differentiation. The first term therefore becomes `(Q_ext-Q_ext')/4`.

The second term is the resolvent of the first-order operator `1+D`. The decaying inverse is the one-sided exponential convolution

`[(1+D)^(-1)q](u)=integral_(-infinity)^u e^(-(u-v))q(v)dv`.

This proves the full-line formula directly from the exact transfer multiplier.

It is also consistent with the local identity from `VIS-333`. Applying `1+D` to the inverse gives

`(1+D)F`
` = (1/4)(1-D^2)Q_ext + (3/4)Q_ext`
` = (1/4)(4-D^2)Q_ext`,

which is exactly

`(4-D^2)Q_ext=4(1+D)F`.

The factorized form is useful because it needs only one derivative of the observed Wang remainder plus an exponentially weighted memory term.

## 2. The zero-extension boundary gives a physical half-line inverse

For `u<0`, the support condition `F(v)=0` for `v<0` and the kernel of `VIS-333` give

`Q_ext(u)=3 integral_0^infinity e^(2(u-v))F(v)dv`.

At `u=0`, the same expression is exactly `Q(0)`. Hence

`Q_ext(u)=Q(0)e^(2u)`

for negative `u`.

Split the first-order resolvent at zero. For `u>=0`,

`integral_(-infinity)^u e^(-(u-v))Q_ext(v)dv`
` = [Q(0)e^(-u)]/3`
`   + integral_0^u e^(-(u-v))Q(v)dv`.

Substituting this into the full-line inverse gives

`F(u)`
` = [Q(u)-Q'(u)]/4`
`   + [Q(0)e^(-u)]/4`
`   + (3/4) integral_0^u e^(-(u-v))Q(v)dv`.

No asymptotic approximation is used.

In the original multiplicative coordinate, if

`R(x)=S(x)-log x+3/(4x^2)=Q(log x)`,

then away from source breakpoints the same identity is

`E_A(x)`
` = (x/4)[R(x)-xR'(x)]`
`   + R(1)/4`
`   + (3/4) integral_1^x R(t)dt`.

The log-scale form is the cleaner statement because it makes the one-order smoothing and its inverse explicit.

## 3. Slowly varying pointwise envelopes transfer back to the source

Assume for large `u` that

`|Q(u)|+|Q'(u)| <= C e^(-phi(u))`

and `0<=phi'(u)<=eta<1`. For `v<=u` in that large-`u` region,

`phi(u)-phi(v) <= eta(u-v)`,

so

`e^(-phi(v)) <= e^(eta(u-v)) e^(-phi(u))`.

Therefore

`integral e^(-(u-v)) e^(-phi(v))dv`

from any fixed sufficiently large lower limit to `u` is at most

`e^(-phi(u))/(1-eta)`.

The omitted finite initial segment contributes `O(e^(-u))`; the explicit boundary term `Q(0)e^(-u)` has the same faster exponential scale. The causal inverse then yields

`F(u)=O(e^(-phi(u)))`.

For the standard Korobov--Vinogradov shape

`phi(u)=c u^(3/5)(log u)^(-1/5)`,

one has `phi'(u)->0`, so the hypothesis is automatic once both `Q` and `Q'` are controlled at that scale. The same applies to ordinary smooth sublinear improvements of this type.

This is a transfer statement, not a new arithmetic estimate. It says that a smooth pointwise gain cannot be credited to Wang's filter alone when the derivative is equally small: the same gain is already present in the normalized source remainder.

## 4. What remains open

`VIS-333` left open the possibility that the actual arithmetic remainder moves spectral mass to increasing log-frequency, where the multiplier attenuates like `|xi|^-1`. The present inverse identifies the pointwise price of that possibility.

A high-frequency component can make `Q` much smaller than `F` while keeping `Q'` comparable to the unsmoothed scale. Thus the derivative term is not a technical nuisance; it is precisely where a genuine scale-migrating mechanism can hide.

Accordingly, a viable Wang-source improvement now has to do one of two things:

- prove a genuinely stronger bound for `F` itself, which is direct new source arithmetic; or
- exploit arithmetic high-frequency/nonstationary structure that makes `Q` small while quantifying the larger derivative cost, and then show that Wang's final statistic benefits from `Q` without requiring a derivative estimate that destroys the gain.

A bound on `Q` alone is not inverted by this result, so the second route remains open.

## 5. Prior art and evidence boundary

The operator algebra is classical. `VIS-292` already anchors the exponential modified-Helmholtz Green/resolvent picture to standard Green-function theory, while `VIS-333` derives the asymmetric first-order transfer multiplier used here. Factoring a rational Fourier multiplier and representing `(1+D)^(-1)` by a one-sided exponential integrating-factor kernel are standard constant-coefficient operator manipulations. No novelty is claimed for those analytic tools.

The Mathia-specific content is the exact specialization to Wang's squared-von-Mangoldt summatory remainder and the resulting pointwise control boundary for the accepted Wang clue.

The result does not show that `Q'` has the same size as `Q`, that the actual source has high-frequency migration, or that the Korobov--Vinogradov envelope is optimal. It also does not create a new RH criterion. It only rules out one remaining false mechanism: a smooth sublinear pointwise improvement of both the Wang remainder and its first log-derivative cannot be a free consequence of the smoothing transform.

## Dependencies

- `VIS-291`: current Korobov--Vinogradov envelope for the squared-von-Mangoldt summatory remainder.
- `VIS-292`: exact symmetric Green-resolvent representation and classical operator prior-art anchor.
- `VIS-332`: exact signed two-tail representation of the summatory remainder.
- `VIS-333`: asymmetric log-frequency multiplier and one-order smoothing control.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose remaining source-cancellation branch is narrowed here.

## Research consequence

The accepted Wang clue should no longer treat a small `Q` as evidence that the symmetric two-tail smoothing has manufactured a pointwise gain. For any smooth sublinear candidate envelope, simultaneous control of `Q` and `Q'` at that envelope transfers the same estimate back to `E_A(x)/x`.

The live escape is therefore sharper: identify source-specific nonstationary/high-frequency structure for which Wang's transform reduces `Q` while the derivative carries the missing scale, and prove that the complete downstream Wang budget can use the smaller `Q` without reintroducing that derivative cost. Establishing such arithmetic structure is a separate research question and is left for a later invocation.
