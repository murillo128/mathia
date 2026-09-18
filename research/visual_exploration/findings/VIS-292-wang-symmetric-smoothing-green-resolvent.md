# VIS-292 — Wang's symmetric smoothing is a log-scale Green resolvent with no blind frequencies

## Claim

For Wang's symmetric squared-von-Mangoldt coefficient sum

`S(x)=x^(-2) sum_(n<=x) n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`,

put `u=log x` and define the locally finite measure

`mu = sum_(n>=2) [Lambda(n)^2/n] delta_(log n)`

on the logarithmic source coordinate. With

`K(v)=exp(-2|v|)`,

one has the exact convolution identity

`S(e^u)=(K*mu)(u)`.

Moreover, in the sense of distributions,

`(4-d^2/du^2) K = 4 delta_0`,

and therefore

`(4-d^2/du^2) S(e^u) = 4 mu`.

Thus Wang's symmetric smoothing is exactly the Green/resolvent filter for the one-dimensional modified Helmholtz operator on log scale. It is smoothing but not information-destroying at the exact distributional level: the underlying weighted prime-power source measure is recovered by one local second-order differential operator.

Equivalently, with the Fourier convention `hat f(xi)=integral_R f(u)e^(-i xi u)du`,

`hat K(xi)=4/(4+xi^2)`.

This multiplier is strictly positive for every real `xi`. Hence the symmetric kernel has **no exact blind log-frequency**. Any improvement of `S(x)-log x` beyond the generic prime-number-theorem envelope cannot be attributed to an exact spectral null built into the smoothing kernel itself.

The same statement has a multiplicative form. For

`k(y)=min(y,1/y)^2`,

its Mellin transform is

`M k(w)=integral_0^infinity k(y)y^(w-1)dy = 4/(4-w^2)`,

valid for `-2<Re(w)<2`. If

`D(s)=sum_(n>=2) Lambda(n)^2 n^(-s)`,

then absolute convergence gives, for `0<Re(w)<2`,

`integral_0^infinity S(x)x^(-w-1)dx = [4/(4-w^2)] D(1+w)`.

The Mellin multiplier likewise has no zeros in its strip of validity.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL GREEN/MELLIN KERNEL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No sharper asymptotic for `S(x)-log x`, no new prime-number-theorem remainder, and no new pair-correlation or RH result is claimed.

## 1. Exact logarithmic convolution

Starting from Wang's coefficient square,

`S(x)=sum_n [Lambda(n)^2/n] min(n/x,x/n)^2`.

Write `x=e^u` and `n=e^t`. Then

`min(e^(t-u),e^(u-t))^2 = e^(-2|t-u|)`.

Since the arithmetic source is discrete at `t=log n`, this gives exactly

`S(e^u)=sum_n [Lambda(n)^2/n] e^(-2|u-log n|)`
`      =(K*mu)(u)`.

This representation is intrinsic to the symmetric `min(n/x,x/n)` weighting. It separates the problem into an arithmetic source `mu` and a fixed translation-invariant kernel on logarithmic scale.

## 2. The source is exactly recoverable distributionally

Away from the origin, `K''=4K`. At the origin the first derivative jumps from `+2` to `-2`, so the distributional second derivative is

`K''=4K-4 delta_0`.

Therefore

`(4-d^2/du^2)K=4 delta_0`.

Convolution with `mu` yields

`(4-d^2/du^2)S(e^u)=4mu`.

This is stronger than merely observing that the weighting is symmetric. The exact smoothed profile determines the complete weighted prime-power source measure. There is no quotient or exact kernel-induced loss of arithmetic information before approximation, truncation, or noisy observation is introduced.

For the asymptotic remainder

`R(u)=S(e^u)-u`,

the corresponding exact source equation is

`(4-d^2/du^2)R = 4mu - 4u du`,

where `u du` denotes the absolutely continuous measure with density `u`. This matches the fact that `S(e^u)~u`: the linear baseline is the Green response to the coarse logarithmic source density `u`.

The inverse is not numerically benign. Applying `4-d^2/du^2` amplifies high log-frequencies quadratically. The statement is exact injectivity/recoverability in the distributional sense, not stable recovery from finite-precision or truncated data.

## 3. Fourier and Mellin multipliers rule out exact blind modes

Direct integration gives

`hat K(xi)=integral_R e^(-2|u|)e^(-i xi u)du = 4/(4+xi^2)`.

The multiplier is nonzero for every real frequency. Hence no logarithmic Fourier mode of the source is annihilated by Wang's symmetric smoothing. High frequencies are attenuated like `xi^(-2)`, but none is exactly removed.

The multiplicative version follows from the same kernel. Split the Mellin integral at `1`:

`integral_0^infinity k(y)y^(w-1)dy`
` = integral_0^1 y^(w+1)dy + integral_1^infinity y^(w-3)dy`
` = 1/(w+2) + 1/(2-w)`
` = 4/(4-w^2)`.

For `0<Re(w)<2`, absolute convergence permits summation before integration, giving

`M[S](w)=[4/(4-w^2)]D(1+w)`.

Again the kernel multiplier itself has no zero. A genuinely sharper asymptotic for `S(x)-log x` may still arise because the arithmetic source has cancellation or additional analytic structure, and the filter can strongly attenuate high-frequency source components. What is ruled out is a stronger explanation in which the symmetric kernel automatically cancels a distinguished nonzero log/Mellin frequency by having a null there.

## 4. Prior art and evidence boundary

The exponential Green kernel is classical. For example, the University of Edinburgh *Methods of Mathematical Physics*, Tutorial Sheet 8, gives the one-dimensional modified Helmholtz Green function for `d^2/dx^2-k^2` as `-(2k)^(-1)e^(-k|x-x'|)` under decay at infinity. Setting `k=2` is exactly the kernel identity used here, up to the operator/sign normalization. The Fourier multiplier and Mellin transform above are elementary direct calculations from that standard kernel.

No novelty is claimed for Green functions, the Fourier transform of an exponential absolute-value kernel, Mellin convolution, or resolvent inversion. The Mathia-specific content is the exact identification of **Wang's particular symmetric squared-von-Mangoldt coefficient sum** with this classical log-scale Green filter and the resulting negative control on proposed smoothing-specific cancellation mechanisms.

The result does not show that the Korobov–Vinogradov envelope in `VIS-291` is optimal. A source-specific cancellation can still make `S(x)-log x` smaller than the generic PNT transfer. Such an improvement would have to be traced to arithmetic information in `mu` or `D(s)`, or to how that information interacts with the nonzero multiplier, rather than to an exact blind frequency of the smoothing kernel.

## Dependencies

- `VIS-289`: establishes `S(x)=log x+o(1)` from the two-term squared-von-Mangoldt asymptotic.
- `VIS-290`: propagates a classical quantitative PNT remainder through the same symmetric coefficient sum.
- `VIS-291`: sharpens the fixed-power envelope to the Korobov–Vinogradov scale and leaves open smoothing-specific improvement.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue whose deeper fixed-power branch is narrowed here.

## Research consequence

The next fixed-power question is now more specific. Searching for cancellation caused merely by the symmetry of `min(n/x,x/n)^2` is not enough: the exact kernel has no blind log-frequency and can be inverted distributionally. Any improvement beyond `VIS-291` must expose a non-generic property of the weighted source measure or its Dirichlet/Mellin transform, and then show that the resulting term survives Wang's complete error budget.

A natural but separate next step is to study the analytic structure of

`D(s)=sum Lambda(n)^2 n^(-s)`

under this nonvanishing Mellin multiplier. That requires a new prior-art/analytic-continuation audit and is therefore left for a later invocation rather than folded into this finding.