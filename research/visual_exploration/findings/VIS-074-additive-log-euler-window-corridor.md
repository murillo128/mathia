# VIS-074 — additive log-Euler windows have no cross-prime small-divisor barrier

## Claim

Fix a finite prime cutoff `X` and write `omega_X=(log p)_(p<=X)`. Consider a coordinate-separable prime-harmonic observable

`f_X(theta)=c_0 + sum_(p<=X) sum_(k in K_p) c_(p,k) exp(i k theta_p)`,

where each `K_p` is a finite subset of `Z\{0}`. Let

`B_(X,L)(theta)=(1/L) integral_0^L f_X(theta-t omega_X) dt`.

Then the nonconstant modes have frequencies only

`lambda_(p,k)=k log p`,

so there are no cross-prime cancellations or `P_X`-smooth near-resonant ratios. Direct integration gives

`B_(X,L)(theta)-c_0`
` = sum_(p<=X) sum_(k in K_p) c_(p,k) exp(i k theta_p)`
`   * exp(-i L k log p/2) sinc(L k log p/2)`

and therefore

`sup_theta |B_(X,L)(theta)-c_0|`
` <= sum_(p,k) |c_(p,k)| min(1, 2/(L |k| log p))`
` <= (2/L) sum_(p,k) |c_(p,k)|/(|k| log p)`.

Under Haar-uniform prime phases the same orthogonality gives

`(E |B_(X,L)(Theta)-c_0|^2)^(1/2)`
` <= (2/L) (sum_(p,k) |c_(p,k)|^2/(k^2 log^2 p))^(1/2)`.

Thus **growing prime support does not create a small-divisor obstruction for additive one-prime-at-a-time observables**. The exponential degree-box corridor in `VIS-073` is relevant only when the witness contains mixed-coordinate Fourier modes; coordinate-separable prime harmonics admit a much stronger weighted `1/L` corridor.

For the truncated logarithmic Euler field at any `sigma>0`,

`E_X(sigma,t)=sum_(p<=X) sum_(k>=1) p^(-k sigma) exp(-i k t log p)/k`,

absolute convergence in `k` permits termwise integration and yields the exact uniform bound

`sup_h |(1/L) integral_h^(h+L) E_X(sigma,t) dt|`
` <= (2/L) sum_(p<=X) Li_2(p^(-sigma))/log p`.

For `0<sigma<1`, the prime number theorem and partial summation give

`sum_(p<=X) Li_2(p^(-sigma))/log p`
` ~ X^(1-sigma)/((1-sigma)(log X)^2)`.

In particular on the critical line,

`sup_h |(1/L) integral_h^(h+L) E_X(1/2,t) dt|`
` <= (4+o(1)) sqrt(X)/(L (log X)^2)`.

Hence any additive log-Euler window with

`L (log X)^2/sqrt(X) -> infinity`

collapses uniformly to its phase mean even though the admitted prime support grows.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER/ALMOST-PERIODIC SPECIALIZATION + DECISIVE-NEGATIVE + NO-NOVELTY-CLAIM`.

No corresponding rate for the exponentiated Euler product, arbitrary nonlinear path functionals, mixed-prime Fourier modes, the zero factor, the hybrid residual, or RH is claimed.

## 1. Coordinate separation removes the dangerous resonances

`VIS-072` shows that a general torus Fourier mode `m` is filtered over a window by

`exp(-i L lambda_m/2) sinc(L lambda_m/2)`,

with `lambda_m=sum_p m_p log p`. Mixed modes can make `lambda_m=log(a_m/b_m)` very small when two distinct smooth integers are close, which is the source of the crude exponential corridor in `VIS-073`.

For the present observable every nonzero mode is supported on exactly one prime coordinate. Its integer vector is `m=k e_p`, so

`lambda_m=k log p`.

Since `p>=2` and `k!=0`, `|lambda_m|>=log 2`. More importantly, the exact denominator is known mode by mode; no cancellation between different prime logarithms can occur. Substituting the one-coordinate modes into the `VIS-072` sinc formula proves the displayed expansion and pointwise bound immediately.

This distinction is structural rather than quantitative bookkeeping. Increasing the number of prime coordinates can increase coefficient mass, but it cannot manufacture a new near-zero frequency until the chosen witness itself multiplies or otherwise mixes coordinates.

## 2. Haar RMS has the same weighted one-coordinate corridor

For Haar-uniform `Theta`, distinct characters `exp(i k theta_p)` are orthogonal unless both `p` and `k` agree. Therefore

`E |B_(X,L)(Theta)-c_0|^2`
` = sum_(p,k) |c_(p,k)|^2 sinc^2(L k log p/2)`.

Using `|sinc y|<=min(1,1/|y|)` gives the stated weighted `l2` bound. This is again free of a dimension-dependent small-divisor penalty; all support growth enters through the coefficient array itself.

## 3. Logarithmic Euler products are exactly coordinate-separable

For fixed `X` and `sigma>0`, each Euler factor satisfies `|p^(-sigma-it)|<1`, so

`log(1-p^(-sigma-it))^(-1)`
` = sum_(k>=1) p^(-k sigma) exp(-i k t log p)/k`

with absolute and uniform convergence in `t`. Summing over finitely many primes gives `E_X` and justifies termwise window integration.

The general pointwise estimate becomes

`(2/L) sum_(p<=X) sum_(k>=1) p^(-k sigma)/(k^2 log p)`
` = (2/L) sum_(p<=X) Li_2(p^(-sigma))/log p`.

This exact expression is already the useful control: it replaces the worst-case `exp(D_X vartheta(X))` cost of a full Fourier box by the actual additive Euler coefficients.

For `0<sigma<1`, `Li_2(p^(-sigma))=p^(-sigma)+O(p^(-2 sigma))`; the error is lower order after prime summation. Partial summation from the prime number theorem then gives

`sum_(p<=X) p^(-sigma)/log p`
` ~ X^(1-sigma)/((1-sigma)(log X)^2)`.

At `sigma=1/2` this is `2 sqrt(X)/(log X)^2`, yielding the displayed critical-line corridor.

## 4. Prior art and novelty boundary

The ingredients are classical. `VIS-072` already anchors the Fourier/Kronecker finite-window calculation to Kuipers--Niederreiter, *Uniform Distribution of Sequences* (1974), and Drmota--Tichy, *Sequences, Discrepancies and Applications* (1997). The almost-periodic interpretation of finite Dirichlet sums is classical Bohr theory. NIST DLMF §27.12 supplies an authoritative prime-number-theorem reference for the final prime-sum asymptotic.

No new almost-periodic theorem, prime number theorem, or general quantitative equidistribution result is claimed. The Mathia-specific contribution is the control diagnosis: in the active prime-phase visual program, additive log-Euler coordinates have a far stronger growing-support averaging corridor because their Fourier support never forms mixed-prime small divisors.

## 5. Boundary and falsification

The theorem is about additive coordinate-separable prime harmonics and their continuous-time window averages. Exponentiating `E_X`, multiplying prime factors, taking nonlinear functions of several coordinates, or using a general path functional can create mixed Fourier modes and restore the `log(a/b)` small-divisor geometry of `VIS-072`--`VIS-073`.

That reappearance does not by itself create new arithmetic information: it is still a deterministic function of the same prime torus. It does, however, change the finite-window quantitative problem, so the one-coordinate bound cannot be applied after such nonlinear mixing without expanding the actual Fourier support.

The result also says nothing about an independently defined zero factor or hybrid residual. Those remain separate information channels only to the extent established by their own construction and controls.

Falsify the exact inequalities by exhibiting a coordinate-separable Fourier coefficient array whose directly integrated window average exceeds the corresponding weighted sinc bound, or falsify the critical-line asymptotic by contradicting the stated prime-sum consequence of the prime number theorem.

## Research consequence

The additive prime-field part of `CLUE-zeta-prime-phase-recursive-geometry` is closed much further than `VIS-073` alone suggests. **Growing the prime cutoff in the logarithmic Euler field cannot expose a new finite-window population merely through slow cross-prime torus filling**, because there are no mixed-prime frequencies to become near resonant.

A genuine growing-support escape must therefore introduce and control mixed-coordinate complexity, an independently anchored selection rule, or an independently defined factor/residual coordinate. Simply plotting more additive prime harmonics, even on the critical line, remains inside the explicit weighted `1/L` averaging corridor above.