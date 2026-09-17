# VIS-264 — the fixed-weight quadratic carrier splits into DC pole compensation plus prime-power curvature samples

## Claim

Use the fixed-margin Rodgers setting and Fourier convention of `VIS-260`--`VIS-263`,

`hat omega(xi)=integral_R omega(u) exp(-2*pi*i*xi*u) du`,

with `omega` real and even and `hat omega` smooth and compactly supported. Let

`F(u)=(1/(2*pi^2))[Re((zeta'/zeta)'(1+iu)-B(iu))+1/u^2]`

be Rodgers' exact `t`-independent Bogomolny--Keating-minus-naive-GUE source kernel and

`C_2(omega)=integral_R u^2 omega(u)F(u)du`.

Then the quadratic carrier has the exact finite decomposition

`C_2(omega)`
` = hat omega(0)/(2*pi^2)`
`   - (1/(8*pi^4)) sum_p sum_(m>=1)`
`       [(log p)^2/p^m] hat omega''(m log(p)/(2*pi))`,

where only finitely many prime powers contribute because `hat omega''` has compact support.

Thus `C_2` has two mathematically distinct channels:

- the zero-frequency pole-compensation term `hat omega(0)/(2*pi^2)`;
- a nonconstant prime-power channel obtained by sampling the curvature of the frozen test weight at the arithmetic frequencies `m log(p)/(2*pi)`.

In particular, if

`supp(hat omega) subset (-log(2)/(2*pi), log(2)/(2*pi))`,

then every prime-power sample vanishes and

`C_2(omega)=hat omega(0)/(2*pi^2)`.

This recovers `VIS-263` as a special case and shows exactly why its nonzero carrier is prime-frequency blind. Conversely, merely letting the Fourier support cross the first prime frequency is not sufficient for source selectivity: the relevant weighted curvature sum can still vanish by zero curvature or cancellation. For a support interval containing only the first nonzero arithmetic frequency, however, the nonconstant channel is exactly

`-(log(2)^2/(16*pi^4)) hat omega''(log(2)/(2*pi))`.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BRIDGED + SOURCE-SELECTIVITY DECOMPOSITION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, explicit-formula theorem, prime-power identity, moving-edge transfer, or RH implication is claimed.

## 1. Rodgers' two arithmetic series collapse coefficientwise

For `Re(s)>1`, absolute convergence gives

`(zeta'/zeta)'(s)`
` = sum_(n>=2) Lambda(n) log(n) n^(-s)`
` = sum_p sum_(m>=1) m (log p)^2 p^(-ms)`.

Rodgers' second term has the absolutely convergent expansion on `s=1+iu`

`B(iu)`
` = sum_p [log(p)^2/(p^(1+iu)-1)^2]`
` = sum_p sum_(m>=2) (m-1)(log p)^2 p^(-m) exp(-i m u log p)`.

For each prime power the coefficient difference is therefore exactly one copy of `(log p)^2/p^m`: for `m=1` only the zeta-logarithmic-derivative term is present, while for `m>=2` the coefficients `m` and `m-1` subtract. Formally, and rigorously after pairing with the band-limited test below,

`(zeta'/zeta)'(1+iu)-B(iu)`

has nonconstant prime-power frequencies

`m log(p)/(2*pi)`

with coefficient `(log p)^2/p^m`.

The point is not a new Euler-product identity. It is that Rodgers' two source terms combine much more cleanly for the quadratic moment than their separate appearance suggests.

## 2. Multiplication by `u^2` turns each arithmetic frequency into a curvature sample

Put

`psi(u)=u^2 omega(u)`.

Fourier differentiation gives

`hat psi(xi)=-(1/(4*pi^2)) hat omega''(xi)`.

Because `hat omega` is smooth and compactly supported, so is `hat psi`. Pair first with `(zeta'/zeta)'(sigma+iu)` for `sigma>1`, where the Dirichlet series is absolutely convergent. Every term with frequency outside `supp(hat psi)` pairs to zero, so only finitely many prime powers survive. Letting `sigma` decrease to `1` is then harmless at the paired level: the surviving sum is finite and each coefficient converges to its boundary value.

The same calculation for `B` is already absolutely convergent on the one-line. Since `omega` is real and even, `hat omega''` is real and even, and taking real parts introduces no additional factor. Hence

`integral_R u^2 omega(u)`
`  Re((zeta'/zeta)'(1+iu)-B(iu)) du`
` = -(1/(4*pi^2)) sum_p sum_(m>=1)`
`     [(log p)^2/p^m] hat omega''(m log(p)/(2*pi)).`

The apparent boundary pole of `(zeta'/zeta)'` causes no extra unrecorded term in this identity. The band-limited pairing is defined by the `sigma>1` limit above; near `u=0`, the factor `u^2` also removes the local double-pole singularity. Rodgers' separate `+1/u^2` term is precisely what supplies the explicit zero-frequency contribution in the next step.

## 3. The pole-compensation channel is exactly the DC mass

The remaining term in `C_2` is elementary:

`integral_R u^2 omega(u) (1/u^2) du`
` = integral_R omega(u)du`
` = hat omega(0)`.

Multiplying the two pieces by Rodgers' overall factor `1/(2*pi^2)` gives

`C_2(omega)`
` = hat omega(0)/(2*pi^2)`
`   - (1/(8*pi^4)) sum_p sum_(m>=1)`
`       [(log p)^2/p^m] hat omega''(m log(p)/(2*pi)).`

This is the desired source-selectivity decomposition. It separates a nonzero carrier that can exist even below every prime frequency from the part that actually samples the discrete prime-power spectrum.

For a normalized weight with `hat omega(0)=1`, the DC baseline is always `1/(2*pi^2)`. `VIS-263` chose support strictly below `log(2)/(2*pi)`, so the arithmetic sum is empty and its exact value follows immediately.

## 4. A frozen quadratic weight has a precise prime-sensitivity test

Define the nonconstant quadratic channel

`C_2^pp(omega)`
` = -(1/(8*pi^4)) sum_p sum_(m>=1)`
`       [(log p)^2/p^m] hat omega''(m log(p)/(2*pi)).`

Then the statement "this fixed Rodgers weight has a quadratic carrier not explained by the pole-compensation control" is exactly

`C_2^pp(omega) != 0`.

This is stronger than the support-only test suggested after `VIS-263`. Fourier support reaching prime frequencies is necessary for a nonzero `C_2^pp`, but not sufficient: `hat omega''` may vanish on the sampled frequencies, or different prime-power samples may cancel.

The first-frequency regime gives a useful clean control. If the support radius `R` satisfies

`log(2)/(2*pi) < R < min(log(3),2log(2))/(2*pi)`,

then only `p=2,m=1` can contribute, and

`C_2^pp(omega)`
` = -(log(2)^2/(16*pi^4)) hat omega''(log(2)/(2*pi)).`

There is no multi-prime cancellation in that corridor. A frozen admissible weight with nonzero curvature there therefore has an explicitly source-specific quadratic component, still entirely within Rodgers' fixed smooth test class.

This does **not** make such a weight faithful to the original bounded-tent/Montgomery support-edge observable. It only supplies an exact calibration coordinate for deciding whether a proposed fixed weight sees nonconstant prime-power structure at quadratic order.

## 5. Prior art and novelty boundary

The load-bearing external source remains Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, arXiv `1203.3275`. Rodgers supplies the smooth fixed-test setting, the exact source kernel `F`, and the `B` term used above. A targeted literature check around this formula, macroscopic pair correlation, and low-frequency smooth-test moments found Rodgers' paper as the directly relevant source and no reason to classify the coefficientwise Euler/Fourier simplification here as a new general theorem.

The expansions of `(zeta'/zeta)'`, `(p^s-1)^(-2)`, and the identity between multiplication by `u^2` and Fourier curvature are classical. No novelty is claimed for those ingredients, nor for the general principle that a band-limited test samples a discrete Dirichlet spectrum.

The Mathia-specific value is the exact decomposition in the normalization already fixed by `VIS-260`--`VIS-263`: it turns the qualitative warning from `VIS-263` into a precise test for which part of `C_2` is detailed prime-power information and which part is only zero-frequency pole compensation.

## 6. Boundaries and falsification

The formula is for one fixed admissible Rodgers weight with smooth compactly supported Fourier transform. It does not justify a changing family `omega_T`, a support radius moving with `T`, or the bounded physical tent from `VIS-128`; those remain outside what `VIS-260` permits without a separate uniform comparison.

The prime-power channel is a two-level mean carrier only. Its nonvanishing does not provide the four-level cross-window covariance required by the original edge--edge statistic and does not solve the moving Montgomery-edge support problem.

The decomposition is falsified if Rodgers' `B` coefficient expansion or Fourier convention is mismatched. Under the conventions fixed in `VIS-263`, however, the coefficient check is direct: `(zeta'/zeta)'` contributes `m(log p)^2/p^m`, `B` contributes `(m-1)(log p)^2/p^m` for `m>=2`, and their difference is one copy for every prime power.

No untouched confirmation-zero data are used.

## Research consequence

The accepted support-edge clue now has an exact quadratic source-selectivity coordinate. A future frozen fixed-weight calibration should report `C_2^pp(omega)` separately from the DC term instead of treating `C_2(omega)!=0` as evidence of detailed arithmetic structure.

The next coherent application step is genuinely different and is intentionally not taken here: construct or derive a weight with a justified dictionary to the intended bounded-tent/Montgomery observable, then ask whether its prime-power curvature channel survives the fixed-margin conditioning and transfer gates. Because the bounded-tent geometry is not automatically a fixed Rodgers test, that dictionary must be proved rather than inferred from the present fixed-weight formula.
