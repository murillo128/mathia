# VIS-079 — full signed Euler-product window energy is a triangular autocorrelation on the doubled line

## Claim

Fix `sigma>0` and a finite prime cutoff `X`. Let

`P_X(sigma,t)=prod_(p<=X) (1-p^(-sigma-it))^(-1)`,

`A_X=P_X(2 sigma,0)`,

and

`F_(X,sigma)(t)=|P_X(sigma,t)|^2/A_X`.

Then `F_(X,sigma)` has long-height mean `1`. Its exact long-height autocorrelation is

`C_(X,sigma)(u)`
` = lim_(T->infinity) (1/T) integral_0^T F_(X,sigma)(h) F_(X,sigma)(h+u) dh`
` = prod_(p<=X) (1-p^(-4 sigma))/|1-p^(-2 sigma-iu)|^2`
` = |P_X(2 sigma,u)|^2/P_X(4 sigma,0)`.

Consequently the full sinc-filtered spectral energy from `VIS-078` has the exact one-dimensional form

`V_(X,sigma)(L)/A_X^2`
` = (2/L^2) integral_0^L (L-u) [C_(X,sigma)(u)-1] du`
` = (2/L^2) integral_0^L (L-u)`
`   [|P_X(2 sigma,u)|^2/P_X(4 sigma,0)-1] du`.

On the critical-line parameter `sigma=1/2`, this becomes

`V_(X,1/2)(L)/P_X(1,0)^2`
` = (2/L^2) integral_0^L (L-u)`
`   [|P_X(1,u)|^2/P_X(2,0)-1] du`.

Thus the complete high-dimensional signed-resonance energy is exactly a **triangularly weighted centered mean of a one-variable finite Euler product on the doubled real part**. In particular, the unresolved critical-line growing-support problem from `VIS-078` can be attacked without enumerating signed prime-log near resonances: it is equivalent to controlling this weighted `Re(s)=1` finite-Euler-product autocorrelation under the same frozen joint law `X=X(L)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER/POISSON/FEJER SPECIALIZATION + STRUCTURAL REDUCTION + NO-NOVELTY-CLAIM`.

No asymptotic for the weighted integral, sharp joint cutoff/window threshold, new finite-Euler-product mean-value theorem, zeta approximation theorem, or RH consequence is claimed.

## 1. Start from the exact Poisson-product Fourier law

`VIS-076` gives the absolutely convergent expansion

`F_(X,sigma)(t)`
` = sum_(k in Z^(pi(X))) w_k exp(-it lambda_k)`,

where

`lambda_k=sum_(p<=X) k_p log p`

and

`w_k=prod_(p<=X) p^(-sigma |k_p|)`.

Unique factorization makes the prime logarithms rationally independent over the integers, so

`lambda_k=lambda_l <=> k=l`

and

`lambda_k+lambda_l=0 <=> l=-k`.

Because the series is absolutely convergent, the autocorrelation may be averaged termwise. Hence

`C_(X,sigma)(u)`
` = sum_k w_k^2 exp(iu lambda_k)`.

This is real and even because the terms for `k` and `-k` pair.

## 2. The entire signed spectrum factors into ordinary one-prime Poisson kernels

The squared Fourier weights factor prime by prime:

`w_k^2=prod_(p<=X) p^(-2 sigma |k_p|)`.

Therefore

`C_(X,sigma)(u)`
` = prod_(p<=X) sum_(m in Z) p^(-2 sigma |m|) exp(i m u log p)`.

For `0<r<1`, the classical Poisson-kernel identity is

`sum_(m in Z) r^|m| exp(i m theta)`
` = (1-r^2)/(1-2r cos theta+r^2)`.

Taking `r=p^(-2 sigma)` and `theta=u log p` gives

`C_(X,sigma)(u)`
` = prod_(p<=X)`
`   (1-p^(-4 sigma))/[1-2p^(-2 sigma) cos(u log p)+p^(-4 sigma)]`.

But

`|P_X(2 sigma,u)|^2`
` = prod_(p<=X) [1-2p^(-2 sigma) cos(u log p)+p^(-4 sigma)]^(-1)`

and

`P_X(4 sigma,0)=prod_(p<=X) (1-p^(-4 sigma))^(-1)`.

This proves

`C_(X,sigma)(u)=|P_X(2 sigma,u)|^2/P_X(4 sigma,0)`.

The high-dimensional signed exponent lattice has therefore not disappeared by approximation: its complete squared-coefficient law has been summed exactly into a one-dimensional Euler product.

## 3. Box-window energy is the triangular autocorrelation average

Let

`M_(X,L)(h)=(1/L) integral_h^(h+L) |P_X(sigma,t)|^2 dt`.

Then

`M_(X,L)(h)/A_X=(1/L) integral_0^L F_(X,sigma)(h+t) dt`.

Long-height averaging and Fubini give

`lim_(T->infinity) (1/T) integral_0^T |M_(X,L)(h)/A_X|^2 dh`
` = (1/L^2) integral_0^L integral_0^L C_(X,sigma)(t-s) dt ds`.

Since `C` is even,

`(1/L^2) integral_0^L integral_0^L C(t-s) dt ds`
` = (2/L^2) integral_0^L (L-u) C(u) du`.

The long-height mean of `M/A_X` is `1`, and

`(2/L^2) integral_0^L (L-u) du=1`.

Subtracting the squared mean therefore yields

`V_(X,sigma)(L)/A_X^2`
` = (2/L^2) integral_0^L (L-u)[C_(X,sigma)(u)-1] du`.

Substituting the Euler-product expression for `C` proves the claim.

This is exactly the time-domain form of the `VIS-078` sinc-square spectrum: the box window produces a triangular lag kernel, equivalently a Fejer-type squared Fourier multiplier. The integrand need not be pointwise nonnegative after subtracting `1`; nonnegativity belongs to the complete weighted integral and is already guaranteed by the equivalent spectral-square formula.

## 4. Critical-line consequence: the energy problem moves to Re(s)=1

At `sigma=1/2`,

`A_X=P_X(1,0)`

and the doubled-line correlation is

`C_(X,1/2)(u)=|P_X(1,u)|^2/P_X(2,0)`.

Hence

`V_(X,1/2)(L)`
` = [2 P_X(1,0)^2/L^2] integral_0^L (L-u)`
`   [|P_X(1,u)|^2/P_X(2,0)-1] du`.

This changes the live proof interface. `VIS-077` and `VIS-078` showed that coefficientwise reciprocal-frequency certificates can be dominated by tiny prime-log denominators whose actual spectral mass vanishes. The present identity bypasses those certificates entirely: the **full** signed spectrum is already encoded by a centered weighted mean of `|P_X(1,u)|^2`.

Accordingly, a growing-support theorem for the exact visual observable may now be sought as a weighted finite-Euler-product mean-value estimate on `Re(s)=1`. Any such theorem must use the same joint law `X=X(L)` and triangular weight; a result for a different cutoff, normalization, moment, or averaging regime does not automatically settle the present energy.

The reduction is exact at every finite `X,L`. It neither proves that the energy vanishes nor suggests that `Re(s)=1` behavior is arithmetic-free. It only replaces a high-dimensional resonance census by an equivalent one-dimensional autocorrelation object.

## 5. Prior art and novelty boundary

The ingredients are classical harmonic analysis. The local identity is the ordinary Poisson-kernel Fourier series, and the passage from a squared Fourier multiplier to a triangular lag average is the standard autocorrelation/Fejer mechanism. No new general harmonic-analysis theorem is claimed.

S. M. Gonek and J. P. Keating, **Mean values of finite Euler products**, *Journal of the London Mathematical Society* 82:3 (2010), 763--786, DOI `10.1112/jlms/jdq049`, studies mean values of the modulus squared of finite Euler products and when Euler factors behave independently. It is the nearest direct analytic-number-theory boundary for the one-variable object appearing here. The present finding does not import a particular asymptotic theorem from that paper and does not claim that its hypotheses automatically cover the triangular joint limit above.

The Mathia-specific content is therefore a structural reduction at the current visual frontier: the complete critical-line sinc-filtered signed energy from `VIS-078` is **exactly** a triangular centered mean of the doubled-line finite Euler product. This identifies the next theorem surface without promoting small-divisor geometry or certificate failure into evidence.

## Boundary and falsification

The identity is for finite prime support and the linear box-window average of `|P_X(sigma,t)|^2`. It does not cover arbitrary nonlinear path functionals, adaptive windows, hybrid prime/zero residuals, or other visual witnesses without deriving their own autocorrelation law.

The critical-line specialization uses `sigma=1/2`; the general formula is valid for every fixed `sigma>0` and finite `X` because all relevant product Fourier series are absolutely convergent.

Falsify the exact result by finding a finite `X,sigma,L` for which the Poisson-product correlation differs from the squared-weight Fourier sum, or for which the triangular autocorrelation integral differs from the `VIS-078` sinc-filtered spectral energy.

## Research consequence

For `CLUE-zeta-prime-phase-recursive-geometry`, the next signed-support question is no longer merely “control the full spectral sum.” It has an equivalent one-dimensional form:

`(2/L^2) integral_0^L (L-u)`
` [|P_X(1,u)|^2/P_X(2,0)-1] du`

under a frozen growing law `X=X(L)`.

A useful next step is therefore a theorem-level upper/lower/asymptotic analysis of this **exact triangular mean** in a declared joint regime, compared carefully with existing finite-Euler-product mean-value results. Failure of `l^1` or reciprocal-frequency `l^2` certificates remains irrelevant unless it changes this actual weighted correlation energy.