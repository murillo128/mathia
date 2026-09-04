# PL-154 — Prime-power checkpoint growth recovers the rightmost zeta-zero frontier

## Claim

Let `Psi` be Suzuki's completed zeta screw potential and define

`Theta := sup { Re(rho) : xi(rho)=0 }`,

where nontrivial zeros are counted in the usual completed `xi` zero set. By the functional equation and the existence of critical-line zeros,

`1/2 <= Theta <= 1`.

Set

`theta := Theta - 1/2`.

For every prime power `q=p^k`, write

`E(q) := Psi(log q)`.

Define the one-sided prime-power growth exponents

`alpha_+ := inf { delta>=0 : E(q) <= C q^delta for all sufficiently large prime powers q, for some C }`,

`alpha_- := inf { delta>=0 : E(q) >= -C q^delta for all sufficiently large prime powers q, for some C }`.

Then

`boxed: alpha_+ = alpha_- = theta = Theta - 1/2.`

Equivalently,

`Theta = 1/2 + limsup_(q=p^k -> infinity) log(1+max(E(q),0))/log q`

and independently

`Theta = 1/2 + limsup_(q=p^k -> infinity) log(1+max(-E(q),0))/log q`.

Thus the ordered prime-power axis skeleton does more than furnish the boundedness criterion of `PL-153`: **either sign by itself recovers the horizontal frontier of the complete nontrivial zeta-zero divisor.** In particular,

`RH <=> E(q) <= q^epsilon up to an epsilon-dependent constant for every epsilon>0`

and independently

`RH <=> E(q) >= -q^epsilon up to an epsilon-dependent constant for every epsilon>0`.

These subpower one-sided criteria are strictly weaker hypotheses than the finite ceiling/floor conditions in `PL-153`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + QUANTITATIVE-ZERO-FRONTIER + STRUCTURAL-REDUCTION`. Suzuki's zero-series and one-sided Fourier/Laplace transform are peer-reviewed theorem-level inputs. The one-sign boundary argument is the classical Landau principle already audited in `PL-149` and `PL-153`. The checkpoint interpolation is the exact convexity/mesh mechanism established in `PL-146` and `PL-153`. A targeted audit of Suzuki's paper and the public August 2026 prime-power checkpoint literature located boundedness, positivity, recovery, and terminal-episode criteria, but not this exact identification of the rightmost-zero abscissa with each one-sided checkpoint power-growth exponent. No novelty claim is made: this is stored as an exact line-level synthesis of known ingredients.

## Continuous exponential order is exactly the zero frontier

Suzuki proves the unconditional zero-series representation

`Psi(t) = sum_gamma (1-exp(i gamma t))/gamma^2`,

where `gamma` ranges over the zeros of

`xi(1/2-i z)`.

If `rho` is a zero of `xi` and

`rho = 1/2 - i gamma`,

then

`Im(gamma) = Re(rho)-1/2`.

The functional equations of `xi` make the zero set symmetric under `rho -> 1-rho` and conjugation, so

`sup_gamma |Im(gamma)| = Theta-1/2 = theta`.

Moreover `sum_gamma |gamma|^-2 < infinity`. Therefore, for `t>=0`,

`|Psi(t)|`

`<= sum_gamma (1+|exp(i gamma t)|)/|gamma|^2`

`<= (1+exp(theta t)) sum_gamma |gamma|^-2`

`<< exp(theta t)`.

Hence the ordinary two-sided exponential order of `Psi` is at most `theta`.

It cannot be smaller. Suzuki also proves, initially for `Re(a)>1/2`,

`F(a) := integral_0^infinity Psi(t) exp(-a t) dt`

`      = (1/a^2) (xi'/xi)(1/2+a)`.

If `Psi(t)=O(exp(delta t))` for some `delta<theta`, the actual Laplace integral would be holomorphic in `Re(a)>delta`. But by the definition of `theta` there is a zero `rho` with

`Re(rho)-1/2 > delta`,

and the meromorphic continuation on the right has a genuine logarithmic-derivative pole at

`a_rho=rho-1/2`.

The two analytic functions agree in Suzuki's initial half-plane, so uniqueness of continuation gives a contradiction. Therefore

`inf { delta>=0 : |Psi(t)| << exp(delta t) } = theta`.

This part uses the zero-series and the completed logarithmic derivative, not an Euler product continued into the critical strip.

## Each sign separately has the same exponential order

The stronger statement is that neither sign can have smaller exponential order than the full function. The zero-series estimate already gives both one-sided bounds with exponent `theta`, so it remains only to rule out a one-sided bound with exponent `delta<theta`.

Fix `0<=delta<theta`. Since `theta<=1/2`, necessarily `delta<1/2`. Assume first that

`Psi(t) <= C exp(delta t)`

for all `t>=T`. Define the nonnegative tail

`h_+(t) = (C exp(delta t)-Psi(t)) 1_[T,infinity)(t)`.

For `Re(a)>1/2`, this is an identity for the **actual Laplace transform** because both Suzuki's transform of `Psi` and the majorant integral converge there, the latter since `Re(a)>1/2>delta`:

`H_+(a)`

`= C exp(-(a-delta)T)/(a-delta)`

`  - F(a)`

`  + integral_0^T Psi(t) exp(-a t) dt`.

The finite integral is entire. The right-hand side gives a meromorphic continuation beyond the initial convergence half-plane and has no real singularity strictly to the right of `delta`: the only new majorant pole is at `a=delta`, while `xi` has no real zero with `s>1/2`; the removable/known completed singular behavior at `a=0` is also not to the right of `delta`.

Let `sigma_c` be the abscissa of convergence of the nonnegative Laplace transform of `h_+`. The genuine convergence just established gives `sigma_c<=1/2`. If `sigma_c>delta`, Landau's boundary-singularity theorem says that the real point `a=sigma_c` must be a singularity of the analytic function represented by the transform. But `sigma_c` is strictly to the right of `delta`, where the displayed continuation is analytic on the real axis, contradiction. Thus

`sigma_c <= delta`.

Consequently the actual nonnegative-tail transform is holomorphic throughout `Re(a)>delta`. Because `delta<theta`, by the definition of `theta` there is a zeta zero satisfying

`Re(rho)-1/2 > delta`.

At `a=rho-1/2`, the term `-F(a)` has a genuine nonreal logarithmic-derivative pole; neither the exponential majorant term nor the finite initial integral can cancel it. This contradicts holomorphy of the actual transform in `Re(a)>delta`. Therefore no eventual upper bound with exponent `delta<theta` exists.

The lower side is identical. If for some `0<=delta<theta`

`Psi(t) >= -C exp(delta t)`

eventually, then `delta<1/2` and the actual transform of

`h_-(t)=(C exp(delta t)+Psi(t))1_[T,infinity)(t)`

has the corresponding identity on the common genuine convergence half-plane `Re(a)>1/2`. The same Landau argument forces its abscissa of convergence to be at most `delta`, after which a zero with `Re(rho)-1/2>delta` produces the same impossible nonreal pole.

Therefore

`inf { delta>=0 : Psi(t) <= C exp(delta t) eventually } = theta`

and

`inf { delta>=0 : Psi(t) >= -C exp(delta t) eventually } = theta`.

For exponents `delta>=theta` the inequality `theta<=delta` is of course already automatic; the Landau contradiction is needed only in the strict range `delta<theta`, which is why the initial transform identity never requires integrating `exp(delta t)` outside its convergence domain.

This quantitatively strengthens the `delta=0` Landau argument in `PL-153`. If RH fails, the positive and negative parts cannot merely be unbounded: **each has exponential order exactly equal to the distance of the rightmost zero frontier from the critical line.**

## Transfer to the prime-power axis checkpoints

The upper transfer uses only the exact interval convexity from `PL-146`. Let

`lambda_j=log q_j`,

where `q_j` and `q_(j+1)` are consecutive prime powers. On every interval `[lambda_j,lambda_(j+1)]`, `Psi` is strictly convex and continuous, so

`Psi(t) <= max(E(q_j),E(q_(j+1)))`.

Suppose

`E(q) <= C q^delta`

for all sufficiently large prime powers. The next prime-power event is no farther than the next ordinary prime. In particular the standard prime-gap bounds used in `PL-153` give

`q_(j+1)/q_j -> 1`

(and a fixed bounded ratio would already suffice here). Hence, uniformly for `t` in the interval,

`Psi(t) << exp(delta t)`.

The preceding one-sided continuous theorem forces `theta<=delta`. Conversely the global bound `|Psi(t)|<<exp(theta t)` immediately gives

`E(q) << q^theta`.

Thus `alpha_+=theta`.

For the lower transfer, convexity alone is not enough because an interior minimum may lie below both endpoints. The semiconvex chord estimate from `PL-153` gives, on consecutive prime-power events `q<r`,

`Psi(t) >= min(E(q),E(r)) - O(q^-0.45)`

uniformly on `[log q,log r]`; the exponent `-0.45` comes from Suzuki's `O(sqrt(q))` curvature together with the Baker--Harman--Pintz prime-event mesh `r-q << q^0.525`. Any prime-gap exponent below `3/4` would suffice.

If

`E(q) >= -C q^delta`

for a fixed `delta>=0`, then `r/q->1` and the vanishing sag is harmless compared with `exp(delta t)>=1`. Therefore

`Psi(t) >= -C' exp(delta t)`

on the continuous tail, and the one-sided Landau argument again forces `theta<=delta`. The global zero-series bound gives the reverse checkpoint estimate at `delta=theta`, hence `alpha_-=theta`.

For a nonnegative sequence `x_q`, the infimum of exponents `delta` for which `x_q=O(q^delta)` equals

`limsup log(1+x_q)/log q`.

Applying this elementary identity separately to the positive and negative parts of `E(q)` yields the two displayed limsup formulae for `Theta`.

## Prime-exponent interpretation

Every checkpoint is an axis point

`v(q)=k e_p`,

and its energy is

`log q = <k e_p,(log ell)_ell>`.

Thus the horizontal spectral frontier

`Theta-1/2`

can be read from the power-growth exponent of **either sign** of the completed potential sampled only on the ordered energy projection

`{ k log p : p prime, k>=1 }`.

This is a precise arithmetic-to-spectral statement: the axis-event sequence retains quantitative information about how far the completed zero divisor extends horizontally, not merely the yes/no information of RH. It does not use mixed-support exponent vectors; its arithmetic content is the von-Mangoldt support and the prime-event mesh.

The critical line is singled out here by completion: the `1/sqrt(q)` event normalization and the centered transform `xi'/xi(1/2+a)` make horizontal displacement from `1/2` become exponential growth rate in the event-time variable `t=log q`. The lattice itself does not derive the half-weight.

## Prior-art and novelty audit

The theorem-level inputs are:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487, DOI `10.1112/jlms.12785`. Theorem 1.1 gives the exact zero-series, the one-sided transform, and the unconditional growth estimate; Theorems 1.6 and 1.7 give the published boundedness/positivity RH criteria.
- **Masatoshi Suzuki**, “On variants of Chebyshev's conjecture,” *The Ramanujan Journal* **68** (2025), article 95, DOI `10.1007/s11139-025-01238-9`. Proposition 1 is the Landau-type nonnegative Mellin/Laplace boundary theorem used in Suzuki's own sign arguments and already audited in `PL-149`/`PL-153`.
- **R. C. Baker, G. Harman, J. Pintz**, “The Difference Between Consecutive Primes, II,” *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`. Supplies the mesh estimate already used in `PL-150` and `PL-153` for the lower checkpoint interpolation.

Current direct checkpoint controls were also searched, including Rainer Andreas Mittermeier's August 2026 Zenodo series through Part 5. Those public descriptions cover strict convex checkpoint reduction, finite positivity certification, smoothed von-Mangoldt reserve balances, recovery witnesses, and the Pringsheim--Landau exclusion of terminal workload episodes. The audit did not locate the quantitative identity

`one-sided checkpoint growth exponent = Theta-1/2`.

That absence is not evidence of novelty. The continuous growth statement is a direct consequence of Suzuki's exact zero-series/Laplace transform, and the discrete statement is an exact synthesis with the already-persisted checkpoint interpolation. The result is therefore classified as derived rather than as a new theorem claim.

## Adversarial boundaries

1. **This does not prove a new bound on `Theta`.** It exactly translates the unknown zero frontier into a one-sided growth exponent. Showing that exponent is zero remains RH-equivalent.

2. **The continuous mechanism is continuation-generic.** For any completed meromorphic spectral object whose real potential has an absolutely convergent zero-exponential expansion and a one-sided Laplace transform with logarithmic-derivative poles, the same argument can identify a horizontal pole frontier with an exponential growth frontier. The rational-prime-specific content enters only in reducing the continuum to the exact prime-power axis checkpoints.

3. **The result does not recover individual zeros or ordinates.** It recovers only `Theta`, the supremum of real parts. Many different zero configurations share the same frontier.

4. **The checkpoint lower-side transfer still uses external prime-distribution input.** The exact event support alone does not control interior convex sag. The available prime-gap mesh makes the transfer rigorous, but this is not a new geometric consequence of the free exponent cone.

5. **No Euler product is used in the strip.** Suzuki proves the transform in its valid initial half-plane; the completed logarithmic derivative gives meromorphic continuation. The zero-series is unconditional and already includes continuation globally.

6. **The half-axis is inserted by completion.** The equality measures displacement from `Re(s)=1/2`; it does not explain from the abstract exponent lattice why the completed normalization must be centered there.

7. **The limsup formula concerns power-growth exponent, not a pointwise asymptotic.** It does not assert `E(q)` is comparable to `q^theta`, nor that a rightmost zero exists when `Theta` is only a supremum. It says every exponent below `theta` fails as a one-sided eventual bound, while exponent `theta` is sufficient.

8. **The positive-transform identity is used only on its genuine convergence half-plane.** In the contradiction step one fixes `delta<theta<=1/2`, hence `delta<1/2`; therefore `Re(a)>1/2` is simultaneously inside Suzuki's initial transform domain and the majorant-transform domain `Re(a)>delta`. The continuation is invoked only after equality with the actual nonnegative Laplace transform has been established there.

## Consequence for the research line

`PL-153` reduced RH to a finite one-sided ceiling or floor on the prime-power checkpoint values. The present result shows the sharper quantitative structure:

`rightmost zero frontier <-> one-sided power-growth frontier of axis checkpoints`.

Accordingly, future checkpoint work need not aim immediately for a uniform bound. Any genuinely arithmetic estimate that proves

`E(q) <= q^epsilon` for every `epsilon>0`

in only the upper direction, or the corresponding lower estimate, already forces RH. More generally, a proved exponent `delta<1/2` would give the explicit zero-free half-plane

`Re(s) > 1/2 + delta`.

The remaining burden is still arithmetic rather than transform-theoretic: derive a one-sided subpower checkpoint estimate from the exact rational-prime forcing in a way that fails for matched generic/Beurling controls.