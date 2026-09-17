# VIS-269 — diagonal-safe shrinking packets are eventually prime-power blind at every fixed even Rodgers jet order

## Claim

Use the Fourier convention and exact Rodgers source kernel from `VIS-264`,

`g(xi)=hat omega(xi)=integral_R omega(u) exp(-2*pi*i*xi*u) du`,

`F(u)=(1/(2*pi^2))[Re((zeta'/zeta)'(1+iu)-B(iu))+1/u^2]`,

and for an integer `r>=1` define the fixed even source carrier

`C_(2r)(omega)=integral_R u^(2r) omega(u) F(u) du`.

Let

`xi_(p,m)=m log(p)/(2*pi)`.

Then every real even smooth `g` with compact support satisfies the exact finite decomposition

`C_(2r)(omega)`
` = [(-1)^(r-1)/(2*pi^2*(2*pi)^(2r-2))] g^(2r-2)(0)`
`   + [(-1)^r/(2*pi^2*(2*pi)^(2r))]`
`       sum_p sum_(m>=1) [(log p)^2/p^m] g^(2r)(xi_(p,m)).`

The first term is the zero-frequency pole-compensation channel. The second is the nonconstant prime-power channel.

Consequently, if

`supp(g) subset (-log(2)/(2*pi), log(2)/(2*pi))`,

then the entire prime-power channel vanishes for **every fixed even order** `2r`, because every arithmetic frequency satisfies

`xi_(p,m) >= log(2)/(2*pi)`.

For the Wang-diagonal-safe packet family of `VIS-268`, where

`g_b in C_c^infinity((-b,b))`, `g_b(0)=0`,

this has two immediate consequences once `b<log(2)/(2*pi)`:

1. the quadratic Rodgers carrier vanishes exactly,

   `C_2(omega_b)=0`;

2. every higher fixed even carrier `C_(2r)`, `r>=2`, contains only the zero-frequency pole-compensation jet `g_b^(2r-2)(0)` and **no detailed prime-power contribution**.

In particular, for any shrinking bandwidth `b(T)->0` — including the logarithmic families `b=L^(-q)` admitted by `VIS-268` — the packet is eventually prime-power blind at every fixed even Rodgers jet order.

**Evidence/status:** `EXACT-DERIVED + COMPOSITION OF CANONICAL FINDINGS + DECISIVE-NEGATIVE FOR THE SHRINKING LOW-FREQUENCY ROUTE + NO-NOVELTY-CLAIM`.

This does not say that Wang's short-interval pair-correlation statistic has no arithmetic lower-order structure. It says that the specific fixed-order Rodgers/Bogomolny--Keating source carriers isolated in `VIS-260`--`VIS-264` cannot provide that source-specific signal through a packet whose Fourier support shrinks entirely below the first prime frequency.

## 1. The prime-power part at general even order

`VIS-264` showed that after combining Rodgers' two arithmetic series, the nonconstant source kernel has prime-power frequencies

`xi_(p,m)=m log(p)/(2*pi)`

with coefficient

`(log p)^2/p^m`.

For `sigma>1` the relevant Dirichlet series is absolutely convergent. Pair there first and then let `sigma` decrease to one, exactly as in `VIS-264`; compact Fourier support leaves only finitely many arithmetic frequencies, so the boundary passage is harmless after pairing.

Fourier differentiation gives

`g^(2r)(xi)`
` = (-1)^r (2*pi)^(2r)`
`   integral_R u^(2r) omega(u) exp(-2*pi*i*xi*u) du`.

Hence each nonconstant prime-power mode contributes

`[(-1)^r/(2*pi)^(2r)] g^(2r)(xi_(p,m))`.

Multiplying by Rodgers' overall factor `1/(2*pi^2)` gives the second term in the claim. For `r=1` this reduces exactly to the prime-power curvature sampler of `VIS-264`,

`-(1/(8*pi^4)) sum_(p,m) [(log p)^2/p^m] g''(xi_(p,m)).`

No new Euler-product identity is being introduced; this is the same discrete source spectrum paired with a higher even monomial.

## 2. The pole-compensation term stays at zero frequency

Rodgers' explicit pole-compensation piece is `1/u^2`. After multiplying by `u^(2r)`, its contribution is

`(1/(2*pi^2)) integral_R u^(2r-2) omega(u) du`.

The same Fourier differentiation identity at zero gives

`integral_R u^(2r-2) omega(u) du`
` = [(-1)^(r-1)/(2*pi)^(2r-2)] g^(2r-2)(0)`,

which is the first term in the claim.

At quadratic order this is just `g(0)/(2*pi^2)`, recovering `VIS-264`. At quartic and higher orders, derivatives of `g` at zero can remain even when `g(0)=0`. Those terms are local pole-compensation jets; they are not samples of the nonconstant prime-power spectrum.

This distinction matters because a nonzero higher-order carrier inside a narrow diagonal-safe packet can otherwise look like a rescued arithmetic signal when it is actually still supported entirely at zero frequency.

## 3. Subprime Fourier support annihilates the detailed arithmetic channel

The smallest positive arithmetic frequency is

`xi_2=log(2)/(2*pi)`,

coming from `p=2,m=1`. Every other `xi_(p,m)` is at least `xi_2`.

If `g` is smooth and supported strictly inside `(-xi_2,xi_2)`, then `g` and all of its derivatives vanish at every `xi_(p,m)`. Therefore

`C_(2r)^pp(omega)=0`

for every fixed `r>=1`.

For `r=1`, imposing the additional Wang-diagonal-safe condition `g(0)=0` from `VIS-268` also annihilates the only remaining pole term, so

`C_2(omega)=0`

exactly.

For `r>=2`, no corresponding conclusion follows merely from the moment constraints used to construct `VIS-268`: conditions such as

`int q^(2j) g_b(q)dq=0`

are integral moments of the frequency-side packet, whereas the remaining pole terms here depend on point derivatives `g_b^(2r-2)(0)`. These are different linear functionals. The correct conclusion is therefore prime-power blindness, not automatic vanishing of every higher carrier.

## 4. Shrinking Wang packets cross the first-prime threshold permanently

`VIS-268` studies packet families supported in `(-b,b)` and, for the scale comparison with Wang's theorem, allows logarithmic choices

`b=L^(-q)`, `q>0`, `L=log T`,

subject to the seminorm gate `q<1/(2m+2)` for a unit `2m`-th moment carrier.

Every such family has `b(T)->0`. Therefore there exists a finite height after which

`b(T)<xi_2`.

From that point onward, all fixed-order Rodgers prime-power jet channels are exactly absent, independently of whether the Wang seminorm error is small enough to transfer the packet.

This is stronger than an error-budget obstruction. The source-specific coefficient is not merely hidden below Wang's remainder; within this particular low-frequency shrinking representation it has been projected out before the theorem error is considered.

## 5. Prior-art and novelty boundary

The external mathematical inputs are exactly those already audited in the canonical predecessor findings.

Brad Rodgers, **Macroscopic Pair Correlation of the Riemann Zeroes for Smooth Test Functions**, *Quarterly Journal of Mathematics* 64:4 (2013), 1197--1219, DOI `10.1093/qmath/has024`, supplies the exact smooth source kernel and the arithmetic `B` term used in `VIS-264`.

Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), supplies the short-interval smooth-test interface whose leading functional motivated the diagonal-safe packet class of `VIS-268`.

The remaining ingredients are elementary Fourier differentiation and the ordering of the prime-power frequencies. A targeted novelty audit is therefore bounded by those exact sources and the already canonical decompositions `VIS-264` and `VIS-268`: no novelty is claimed for band limitation, Fourier jets, or the fact that support below the first sampled frequency kills a discrete Fourier sampler.

The durable Mathia result is the composition of the two interfaces. The packet modification required to make Wang's leading term vanish, when combined with the shrinking low-frequency design used to control Wang's seminorm error, removes the detailed Rodgers prime-power carrier that the branch was trying to expose.

## 6. Boundaries and falsification

This finding concerns the fixed-order source carriers obtained by pairing Rodgers' `t`-independent source kernel with `u^(2r) omega(u)`. It does not prove that every conceivable arithmetic correction is a finite Rodgers jet or that Wang's true lower-order short-interval statistic is universal.

It also does not rule out a **fixed-width or multiband** diagonal-safe test whose support reaches one or more prime-power frequencies, nor a packet translated toward an arithmetic frequency, nor a different source kernel whose arithmetic information is present arbitrarily close to zero frequency. Those are different representations and require their own theorem/error audit.

The conclusion would fail if the Fourier dictionary between the Rodgers weight and Wang's `g` were mismatched. Under the conventions already fixed in `VIS-260`--`VIS-268`, both roles use the compactly supported frequency-side test paired against the physical zero-separation variable, so the identification is the one already used throughout this branch.

No untouched confirmation-zero data are used.

## Research consequence

The specific next step proposed at the end of `VIS-268` — derive a source-specific quadratic or quartic coefficient for the same shrinking diagonal-safe packet — is now closed for Rodgers' fixed-order prime-power channel. At quadratic order the carrier is exactly zero once the packet lies below the first prime frequency. At quartic and higher fixed orders, any surviving carrier is zero-frequency pole compensation unless the test support actually reaches a prime-power frequency.

The next coherent source-specific design must therefore change representation rather than add more moment cancellations to the same shrinking packet: for example, keep or introduce support at a pre-registered arithmetic frequency while separately enforcing Wang's leading-null conditions, and then re-price the seminorm/error budget. That is a distinct research question and is intentionally left for a later invocation.