# VIS-282 — Wang's fixed-source Dirichlet energy retains an exact prime-power profile

## Claim

Keep the fixed-source regime of `VIS-274`–`VIS-281`: `H=T^theta` with fixed `0<theta<1`, `L=log T`, `I=(T,T+H]`, and

`x=e^(2*pi*q)`

with `q` restricted to a fixed compact set in `(0,infinity)`. For Wang's Dirichlet polynomial/series

`D_x(t)=sum_(n>=2) a_n(x) n^(-it)`,

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`,

define its exact diagonal energy

`S_D(x)=sum_(n>=2) a_n(x)^2`.

Then, uniformly for `x` in any fixed compact `K subset (1,infinity)`, Montgomery–Vaughan's mean-value theorem as used by Wang gives the sharper fixed-source identity

`integral_I |D_x(t)|^2 dt = H S_D(x) + O_K(1)`.

Moreover,

`S_D(x)`
` = x^(-2) sum_(2<=n<=x) n Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^3`.

Thus Wang's subsequent replacement

`S_D(x)=log x+O(1)`

is harmless for his theorem uniform in growing `x`, but it discards order-one source structure in the compact fixed-source regime. Writing

`C_D(x)=S_D(x)-log x`,

one has

`integral_I |D_x(t)|^2 dt`
` = H log x + H C_D(x) + O_K(1)`.

The function `C_D` is continuous and piecewise smooth, and its derivative has a jump at every prime power `m=p^k`:

`C_D'(m+)-C_D'(m-) = -4 Lambda(m)^2/m^2`.

Consequently the apparently featureless `O(H)` term in Wang's equation (2.19) contains, at fixed physical source, an exact deterministic prime-power profile. Under the fixed-`q` packet pullback, both `H log x` and `H C_D(x)` enter the normalized pair statistic at order `L^-2`, while the genuine mean-value remainder `O_K(1)` is power-small after normalization.

**Evidence/status:** `LITERATURE+DERIVED + EXACT REGIME SPECIALIZATION + CLASSICAL MEAN-VALUE INPUT + ARITHMETIC PROFILE + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No new Montgomery–Vaughan theorem, new asymptotic for `S_D(x)` as `x->infinity`, improved global pair-correlation estimate, secondary coefficient for the full pair statistic, or RH implication is claimed.

## 1. Wang's `O(H)` combines two mathematically different losses

Biao Wang defines in equation (2.8)

`a_n(x)=Lambda(n)/sqrt(n) min(n/x,x/n)`

and in the proof of Proposition 2.6 applies Montgomery–Vaughan's mean-value theorem to obtain

`integral_I |D_x(t)|^2 dt`
` = H sum_(n>=2) a_n(x)^2 + O(sum_(n>=2) n a_n(x)^2)`.

His Lemma 2.5 gives

`sum a_n(x)^2 = log x + O(1)`

and

`sum n a_n(x)^2 << x log^2(2x)`,

so equation (2.19) is recorded as

`integral_I |D_x(t)|^2 dt`
` = H log x + O(H + x log^2(2x))`.

For a source parameter ranging as far as `x<=T^lambda`, that is the appropriate uniform form. But on a compact fixed-source window the two pieces inside this error have different meanings.

The actual mean-value-theorem remainder is

`O(sum n a_n^2)=O_K(1)`.

The much larger `O(H)` term comes only from replacing the exact diagonal quantity `S_D(x)` by its coarse large-range approximation `log x+O(1)`. It is therefore not averaging noise and should not be treated as an undifferentiated theorem error when `x` is held fixed.

## 2. The exact diagonal profile is elementary and arithmetic

From Wang's coefficient definition, if `n<=x` then

`a_n(x)^2 = n Lambda(n)^2/x^2`,

whereas for `n>x`,

`a_n(x)^2 = x^2 Lambda(n)^2/n^3`.

Splitting the absolutely convergent square sum gives

`S_D(x)`
` = x^(-2) sum_(2<=n<=x) n Lambda(n)^2`
`   + x^2 sum_(n>x) Lambda(n)^2/n^3`.

This is already a complete fixed-source formula. No prime-number-theorem approximation is required.

For `x` away from integers, differentiation gives

`S_D'(x)`
` = -2 x^(-3) sum_(2<=n<=x) n Lambda(n)^2`
`   + 2x sum_(n>x) Lambda(n)^2/n^3`.

At an integer `m`, the `n=m` summand moves continuously from the tail expression to the head expression: both equal `Lambda(m)^2/m` at `x=m`. Hence `S_D` is continuous. The one-sided derivative contribution of that summand changes from

`+2 Lambda(m)^2/m^2`

to

`-2 Lambda(m)^2/m^2`,

so

`S_D'(m+)-S_D'(m-)=-4 Lambda(m)^2/m^2`.

Because `Lambda(m)=0` unless `m` is a prime power, the only derivative kinks occur at prime powers. Subtracting the smooth function `log x` leaves the same jumps for `C_D(x)=S_D(x)-log x`.

In the physical coordinate `x=e^(2*pi*q)`, these kinks lie at

`q=log(p^k)/(2*pi)`.

This does not make them a new invariant: they are simply the von Mangoldt support already present in Wang's coefficients, exposed by retaining the exact fixed-source diagonal rather than collapsing it to `log x+O(1)`.

## 3. Fixed-source normalization places the whole profile at `L^-2`

Wang's pair formula uses

`2*pi F_I(x)=integral_I |A(x,t)|^2 dt + ...`,

and Theorem 2.2 integrates `F_I(T^alpha)` over `alpha`. In the current physical-source packet,

`alpha=2*pi*q/L`,

so

`d alpha=(2*pi/L)dq`,

while the normalized pair statistic contributes a further factor proportional to `1/(H L)`.

Therefore any fixed-source `H S_D(e^(2*pi*q))` contribution is of order

`H * L^-1 * (H L)^-1 = L^-2`.

The same is true separately for `H log x` and `H C_D(x)`: on compact `q` both are order `H` before pullback. Thus the approximation `S_D=log x+O(1)` does not determine the `L^-2` coefficient of the `D_x` sector. It discards information at exactly the scale one would be trying to resolve.

By contrast, the genuine Montgomery–Vaughan remainder is only `O_K(1)`. After the same pullback and normalization it contributes

`O_K(1/(H L^2))`,

which is smaller than every fixed negative power of `L` because `H=T^theta`.

This cleanly separates a deterministic arithmetic source profile from the finite-interval mean-value error.

## 4. Consequence for the current fixed-source audit

`VIS-279` used Wang's exact equation (2.19) only to recover the compact-source scale `||D_x||_2=O_K(sqrt(H))`, enough to eliminate the apparent `L^-3/2` D–E floor. The present finding asks what remains inside that `O_K(H)` energy once the theorem-level bound is no longer the target.

The answer is that the leading compact-source `D_x` energy is not merely `H log x` plus unstructured uncertainty. It is `H S_D(x)` up to `O_K(1)`, and `S_D` carries an explicit prime-power kink profile.

Therefore a future attempt to compute or compare a fixed-source `L^-2` pair-correlation coefficient must retain `S_D(e^(2*pi*q))` itself, or prove that its packet projection cancels against another exact sector. Replacing it by `log x` and carrying an anonymous `O(H)` remainder loses the entire coefficient-scale information.

This does **not** assert that the prime-power kinks survive in the final pair statistic. Cross terms and the `B_x+E_x` source sector can contribute at the same `L^-2` scale, and signed cancellation is possible. The finding identifies the exact `D_x` contribution that must be present before those sectors are recombined.

## 5. Prior art and novelty boundary

The primary source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918 (2026), equations (2.8), (2.17), and (2.19), and Proposition 2.6. Wang supplies the coefficient sequence, the estimates for its square sums, and the mean-value step used here.

The mean-value input is H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* s2-8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`, specifically the corollary cited by Wang. No strengthening of that result is used.

The exact formula for `S_D(x)` and the prime-power derivative jumps are direct algebraic consequences of Wang's displayed coefficient definition. They are recorded here as a representation/audit result, not as a claim of new analytic-number-theory prior art.

The fixed compact-source restriction is essential. If `x=x(T)` grows, the Montgomery–Vaughan remainder `O(x log^2(2x))`, the large-`x` behavior of `S_D(x)-log x`, and the other sectors of Proposition 2.6 must all be tracked uniformly; none is controlled by this finding.

No confirmation-zero data or numerical fitting are used.

## Dependencies

- `VIS-274`: fixed physical-source coordinate and packet normalization.
- `VIS-278`: the standalone gamma-normalized `B_x+E_x` source energy also lives at `L^-2`.
- `VIS-279`: the fixed-source `D_x` mean-square is already enough to remove the apparent `L^-3/2` D–E floor.
- `VIS-280`: the direct D–B cross is power-small on the same packet.
- `VIS-281`: zero-window localization is power-small after fixed-source pullback.

## Research consequence

The remaining bare `H` in Wang's Dirichlet mean square is now resolved into an exact fixed-source diagonal profile plus a power-small averaging remainder. The profile has deterministic prime-power kinks and contributes at the same `L^-2` scale as the other surviving fixed-source secondary sectors.

The next coherent question is whether the exact `D_x` profile cancels, combines, or remains visible after recombination with the `B_x+E_x` and signed cross terms at `L^-2`. That is a separate thread and is intentionally left for a later invocation.