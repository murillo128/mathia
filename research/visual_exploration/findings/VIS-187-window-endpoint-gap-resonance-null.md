# VIS-187 — a flat even-gap kernel null has endpoint-resonant logarithmic accumulation

## Claim

Let

`K_(H,T)(p,q) = H^(-1) int_T^(T+H) exp(it log(q/p)) dt`

be the interval kernel used in `VIS-185` and `VIS-186`. Fix constants `c>0` and `tau in R`, put

`H = c p`,

`T = tau p`,

and let `M=M(p)` satisfy `M -> infinity` and `M=o(p^(1/2))`. Consider the deterministic flat even-gap null

`E_p(M;c,tau) = sum_(1<=m<=M) K_(cp,tau p)(p,p+2m)`.

Define

`S_M(theta) = sum_(1<=m<=M) exp(i theta m)/m`.

Then

`E_p(M;c,tau)`
` = [S_M(2(tau+c)) - S_M(2 tau)]/(2 c i)`
`   + O_(c,tau)(M^2/p)`.

Consequently, with

`r(x)=1` if `x in pi Z`, and `r(x)=0` otherwise,

one has

`E_p(M;c,tau)`
` = [(r(tau+c)-r(tau))/(2 c i)] log M`
`   + O_(c,tau)(1) + O_(c,tau)(M^2/p)`.

In particular, for every fixed `0<delta<1/2`, taking `M=floor(p^delta)` gives

`E_p(M;c,tau)/log p`
` -> [delta(r(tau+c)-r(tau))]/(2 c i)`.

Thus the flat even-gap null has an order-`log p` cumulative contribution precisely when exactly one scaled window endpoint `tau` or `tau+c` is resonant modulo `pi`. For the natural anchored window `T=0`, if `c notin pi Z`,

`E_p(floor(p^delta);c,0)/log p -> i delta/(2c)`.

If neither endpoint is resonant, the same normalized quantity tends to zero. If both are resonant, the logarithmic terms cancel.

**Evidence/status:** `EXACT-DERIVED + DETERMINISTIC WINDOW-KERNEL NULL + NEGATIVE MULTISCALE CONTROL + CLASSICAL FOURIER/HARMONIC INPUT + NO-NOVELTY-CLAIM`.

No statement about actual prime-pair asymptotics, singular-series cancellation, or a nonzero prime off-diagonal contribution is claimed.

## 1. Exact reduction to one scalar phase variable

For `q=p+2m`, write

`u_m = log(1+2m/p)`

and

`x_m = p u_m`.

Direct integration gives

`K_(cp,tau p)(p,p+2m)`
` = [exp(i(tau+c)x_m)-exp(i tau x_m)]/(i c x_m)`.

Introduce the smooth function on positive real `x`

`G_(c,tau)(x)`
` = [exp(i(tau+c)x)-exp(i tau x)]/(i c x)`.

Then the exact kernel term is `G_(c,tau)(x_m)`.

For `m=o(p)`, Taylor expansion of `log(1+2m/p)` gives

`x_m = 2m + O(m^2/p)`.

For fixed `c,tau`, differentiation of `G_(c,tau)` shows

`|G'_(c,tau)(x)| <<_(c,tau) 1/x`

for `x>=1`. Since `x_m asymp m` throughout `m<=M=o(p^(1/2))`, the mean-value theorem yields

`G_(c,tau)(x_m) - G_(c,tau)(2m)`
` = O_(c,tau)(m/p)`.

Summing gives

`E_p(M;c,tau)`
` = sum_(m<=M) G_(c,tau)(2m)`
`   + O_(c,tau)(M^2/p)`.

The assumed range makes the accumulated linearization error `o(1)`.

## 2. The linearized null is a difference of harmonic exponential sums

At the linearized point,

`G_(c,tau)(2m)`
` = [exp(2i(tau+c)m)-exp(2i tau m)]/(2 c i m)`.

Therefore

`sum_(m<=M) G_(c,tau)(2m)`
` = [S_M(2(tau+c))-S_M(2 tau)]/(2 c i)`.

This is the claimed reduction.

The asymptotics of `S_M` are elementary. If `theta in 2 pi Z`, then

`S_M(theta)=sum_(m<=M) 1/m = log M + gamma + o(1)`.

If `theta notin 2 pi Z`, the geometric partial sums of `exp(i theta m)` are uniformly bounded, so Dirichlet summation implies that

`sum_(m>=1) exp(i theta m)/m`

converges. Hence `S_M(theta)=O_theta(1)` as `M->infinity`.

Because `2x in 2 pi Z` exactly when `x in pi Z`, only resonant scaled window endpoints contribute a logarithmic term. Subtracting the two endpoint series gives the coefficient in the claim.

## 3. Why this is the right null for the VIS-185/VIS-186 frontier

`VIS-185` found the cumulative absolute-value envelope

`O(log D/log y)`

for a near-diagonal gap band at the linear observation scale. `VIS-186` then showed that each individual polynomial dyadic gap shell contributes only `O(1/log y)`, leaving open whether `Theta(log y)` shells can accumulate coherently.

The present null shows that a logarithmic cross-scale sum is already available **without any arithmetic source structure at all**. Equal deterministic weight on the admissible even gaps, combined only with the exact rectangular-window kernel, produces a `log M` term at a resonant window endpoint. After the natural `log p` normalization, a polynomial cumulative range `M=p^delta` leaves the nonzero constant `i delta/(2c)` for `T=0` and generic `c`.

This does not model the actual multiplicities or weights of prime pairs. Its role is narrower and adversarial: the mere appearance of a cumulative logarithmic contribution across many mesoscopic gap octaves cannot by itself be interpreted as arithmetic cross-scale coherence. A matched control must first account for deterministic window-endpoint resonance.

The null also shows that the worst-case uniform-in-`T` envelope and a generic fixed scaled start are mathematically different questions. Away from endpoint resonance, the flat null has no logarithmic accumulation even though the absolute shell bounds still sum to an order-one envelope.

## 4. Prior-art and novelty boundary

Every analytic ingredient here is classical: the Fourier transform of a rectangular interval, the Taylor expansion of `log(1+x)`, the harmonic asymptotic, and Dirichlet convergence of `sum exp(i theta m)/m` away from zero frequency. No new Fourier-series or exponential-sum theorem is claimed.

The Mathia-specific content is the exact placement of these elementary facts against the unresolved `VIS-185`/`VIS-186` multiscale control: it identifies a deterministic endpoint-resonance mechanism that can saturate the logarithmic cumulative scale in a flat even-gap null.

No literature search result was found or needed that would support treating this elementary null as a novel general theorem. The finding is retained as a negative control, not as a novelty claim.

## 5. Boundaries and falsification

The comparison with the exact logarithmic kernel is proved only for `M=o(p^(1/2))`, which is enough to cover every fixed polynomial range `M=p^delta` with `delta<1/2`. No claim is made here for larger cumulative gap ranges.

The parameters `c` and `tau` are fixed as `p->infinity`. Constants are not uniform as a nonresonant endpoint approaches `pi Z`; near resonance there is a crossover regime that this finding does not quantify.

The null uses equal deterministic weight per even gap. It deliberately does not encode prime-pair multiplicity, singular-series variation, the `p^(-alpha)(p+d)^(-alpha)` weight profile, or variation of `H/p` across a dyadic prime block. Therefore it cannot prove that the actual prime off-diagonal sum has a logarithmic term, nor that subtracting this null removes all non-arithmetic accumulation.

Falsify the finding by locating an error in the exact interval-kernel reduction, the estimate `x_m=2m+O(m^2/p)`, the derivative bound for `G_(c,tau)`, the accumulated `O(M^2/p)` error, or the harmonic-exponential endpoint classification.

## Research consequence

The cross-scale frontier should now distinguish **source coherence** from **window-endpoint coherence**. Before treating an order-one polynomial cumulative contribution as arithmetic, compare it against a control that preserves the same scaled window endpoints and coarse even-gap density, or use a statistic whose endpoint-resonant component is explicitly removed.

A future positive result must survive that control and then explain what additional prime-dependent structure couples the logarithmic gap scales. Conversely, a cancellation theorem may reasonably target the nonresonant or endpoint-centered residual rather than trying to beat a worst-case logarithmic envelope that this deterministic null can already realize.