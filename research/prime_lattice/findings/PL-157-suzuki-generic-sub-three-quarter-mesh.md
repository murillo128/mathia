# PL-157 — Suzuki prime-basis sampling is a generic sub-three-quarter mesh phenomenon

## Claim

Let `Psi` be Masatoshi Suzuki's completed real even function for the Riemann zeta function, written in the prime-power ramp form already used in `PL-146` and `PL-156`,

`Psi(t) = R(t) - sum_(q<=exp(t)) w_q (t-log q)`,

where `q` ranges over prime powers and `w_q=Lambda(q)/sqrt(q)`.

Let

`1 < x_1 < x_2 < ... -> infinity`

be **any** increasing sampling sequence, not necessarily arithmetic, and suppose that for some `kappa<3/4`,

`x_(j+1)-x_j = O(x_j^kappa)`.

Put `a_j=log x_j`, `b_j=log x_(j+1)` and let `Ch_j[Psi]` be the affine chord joining the two sampled values. Then

`sup_(a_j<=t<=b_j) |Psi(t)-Ch_j[Psi](t)|`

`= O(x_j^(2 kappa-3/2) log x_j) = o(1)`.

Consequently every such mesh has exactly the same one-sided tail information as the continuum:

`Psi bounded above on R_+ <=> {Psi(log x_j)} bounded above`,

and independently

`Psi bounded below on R_+ <=> {Psi(log x_j)} bounded below`.

Using `PL-153`, either sampled boundedness condition is equivalent to RH. If `Theta=sup{Re rho:xi(rho)=0}` and `theta=Theta-1/2`, the one-sided sampled power-growth exponents are also both exactly `theta`, by `PL-154`.

The same mesh theorem applies to Suzuki's weighted-Chebyshev statistic

`F(x)=sum_(n<=x) Lambda(n)/sqrt(n) log(x/n)-4 sqrt(x)`.

Hence Suzuki's peer-reviewed criterion

`RH <=> F(x)/log x -> -alpha`,  `alpha=zeta'(1/2)/zeta(1/2)`,

remains equivalent after restriction to **any** mesh satisfying the displayed gap condition.

In particular the completely non-prime sampling sequence

`x_j=j^3`

has gaps `O(x_j^(2/3))`, so

`RH <=> sup_j Psi(3 log j)<infinity`,

independently

`RH <=> inf_j Psi(3 log j)>-infinity`,

and

`RH <=> F(j^3)/log(j^3) -> -alpha`.

Thus `PL-156`'s ordinary-prime basis restriction is valid, but its **sampling sufficiency is not itself a rational-prime discriminator**. Once Suzuki's completed scalar function has already encoded the arithmetic, ordinary primes are merely one sufficiently fine observation mesh among many. Rational-prime structure remains in the construction/forcing of `Psi`, not in the fact that the depth-one basis values form an RH-complete tail sampling set.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE/STRUCTURAL-REDUCTION`. Suzuki's formulas and RH criteria are peer-reviewed inputs. The interpolation theorem is an elementary exact consequence of the ramp representation, Suzuki's `sqrt(x)` smooth curvature scale, and a crude count of how much von-Mangoldt half-weight can occur inside an arbitrary short interval. A targeted current-literature search found the Suzuki and prime-power-checkpoint literature but no statement of this generic sub-`3/4` sampling reduction; no novelty claim is made because the derivation is elementary once the completed ramp formula is available.

## Arbitrary-mesh chord decomposition

Fix consecutive sampling scales `x<y`, put

`a=log x`, `b=log y`, `Delta=b-a`,

and let

`Q_(x,y)={q : q is a prime power and x<q<y}`.

Every ramp activated at or before `x` is affine throughout `[a,b]`. A ramp activated exactly at `y` has zero value at the right endpoint and does not alter the chord identity. Therefore

`Psi(t)=R(t)-L_x(t)-sum_(q in Q_(x,y)) w_q (t-log q)_+`,

where `L_x` is affine. Since affine interpolation kills `L_x`,

`Psi-Ch[Psi]`

`=(R-Ch[R])-sum_(q in Q_(x,y)) w_q (h_q-Ch[h_q])`,

with `h_q(t)=(t-log q)_+`.

Two deterministic inequalities suffice. First,

`sup |R-Ch[R]| <= (Delta^2/8) sup |R''|`.

The exact Suzuki curvature already audited in `PL-146` and reused in `PL-150/156` satisfies

`R''(log u)=O(sqrt(u))`,

hence

`sup |R-Ch[R]| = O(sqrt(y) Delta^2)`.

Second, for every hinge with breakpoint inside the interval,

`sup |h_q-Ch[h_q]| <= Delta/4`.

Thus

`sup |Psi-Ch[Psi]|`

`<= O(sqrt(y) Delta^2) + (Delta/4) sum_(q in Q_(x,y)) Lambda(q)/sqrt(q)`.

This is the same local identity underlying `PL-156`, but here no alignment of the sampling grid with ordinary primes is assumed. The price is that the internal event sum now contains ordinary primes as well as higher prime powers.

## Crude event counting already gives the same `3/4` threshold

Assume

`h=y-x=O(x^kappa)`

with `kappa<1`. Then `y/x->1` and

`Delta=log(y/x) <= h/x = O(x^(kappa-1))`.

For every prime power `q` in `(x,y)`,

`Lambda(q)/sqrt(q) <= log(y)/sqrt(x)`.

There are at most `h+1` integers in the interval, hence certainly at most that many prime powers. Therefore

`sum_(q in Q_(x,y)) Lambda(q)/sqrt(q)`

`<= (h+1) log(y)/sqrt(x)`

`= O(x^(kappa-1/2) log x + x^(-1/2) log x)`.

No prime number theorem, short-interval theorem, or information about the distribution of prime powers is used. Combining this with the chord bound gives

`sup |Psi-Ch[Psi]|`

`= O(x^(1/2) x^(2kappa-2))`

`  + O(x^(kappa-1) x^(kappa-1/2) log x)`

`  + O(x^(kappa-1) x^(-1/2) log x)`

`= O(x^(2kappa-3/2) log x)`.

For every fixed `kappa<3/4`, this tends to zero.

The exponent `3/4` is therefore not a special property of the prime basis. It is already the generic interpolation threshold produced by the completed smooth curvature scale `sqrt(x)` and a mesh of width `x^kappa`. `PL-156` exploits the special fact that between consecutive ordinary primes the only internal events are higher prime powers, giving a sharper event-mass term; but that sharpening is unnecessary for the qualitative `o(1)` sampling conclusion.

## Transfer of RH-sensitive boundedness and zero-frontier growth

Let the mesh satisfy the preceding hypothesis. For every sufficiently large `t`, choose the unique `j` with

`log x_j <= t <= log x_(j+1)`.

The chord formula gives

`Psi(t)=(1-lambda)Psi(log x_j)+lambda Psi(log x_(j+1))+o(1)`

uniformly on each interval, where `0<=lambda<=1`.

If all sufficiently large sampled values are bounded above by `M`, the chord is bounded above by `M`, so `Psi` is bounded above on the continuous tail. The compact initial segment has a finite maximum. Restriction proves the converse. The identical argument applied to `-Psi` gives the lower-bounded equivalence.

`PL-153` proves that either one-sided continuum boundedness condition is equivalent to RH. Hence either one-sided condition on the arbitrary sub-`3/4` mesh is also equivalent to RH. In particular, if RH fails, every such mesh necessarily satisfies

`limsup_j Psi(log x_j)=+infinity`

and

`liminf_j Psi(log x_j)=-infinity`.

The growth-exponent transfer is just as direct. Because `kappa<1`,

`x_(j+1)/x_j -> 1`.

If, for a fixed `delta>=0`,

`Psi(log x_j) <= C x_j^delta`

eventually, then both chord endpoints over the `j`th interval are `O(e^(delta t))`, uniformly there; the `o(1)` interpolation error is harmless. Thus the same one-sided exponential bound holds on the continuum. Restriction gives the reverse implication. The same argument applies to the lower side. By `PL-154`, both sampled one-sided exponents therefore equal

`Theta-1/2`.

This means that the rightmost-zero frontier recovered in `PL-154` and then on the ordinary-prime basis in `PL-156` is actually recoverable on a broad class of exogenous meshes that carry no prime-exponent geometry at all.

## Non-prime polynomial controls

Take `x_j=j^m` for an integer `m=1,2,3`. Then

`x_(j+1)-x_j = O(j^(m-1)) = O(x_j^(1-1/m))`.

For `m<=3`,

`1-1/m <= 2/3 < 3/4`,

so the mesh theorem applies. The cubic control is especially useful because it is sparse on the ordinary `x` scale while still lying comfortably below the threshold:

`x_j=j^3`,  `x_(j+1)-x_j=O(x_j^(2/3))`.

Sampling at `t_j=3 log j` therefore retains the one-sided RH criterion and the exact horizontal zero-frontier exponent. These sample locations are not prime basis vectors and do not arise from a prime-gap theorem. They are a deterministic comparison showing that **observation-set completeness after scalar completion is a mesh property rather than a prime-lattice rigidity property**.

The same control applies to Suzuki's 2025 statistic. Put

`H(t)=F(e^t)=sum_(q<=e^t) w_q(t-log q)-4e^(t/2)`.

Its smooth part has

`H''_smooth(t)=-e^(t/2)`,

and its internal prime-power hinges have the same weights. The identical absolute chord estimate therefore yields

`H(t)=Ch[H](t)+o(1)`

on every sub-`3/4` mesh interval. Since adjacent logarithmic sample locations differ by `o(1)`, Suzuki's limit criterion transfers in both directions:

`RH <=> F(x_j)/log x_j -> -alpha`.

In particular this is true for `x_j=j^3`.

## Prior-art and novelty audit

The theorem-level external inputs are the same completed scalar facts already audited in `PL-146` and `PL-156`:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. Equation (1.1) supplies the prime-power ramp representation of `Psi`; Theorem 1.1 supplies its completed transform/zero representation.
- **Masatoshi Suzuki**, “On variants of Chebyshev's conjecture,” *The Ramanujan Journal* **68** (2025), article 95, DOI `10.1007/s11139-025-01238-9`. Theorem 1 supplies the RH-equivalent asymptotic for `F(x)`.

Current August 2026 prime-power-checkpoint preprints by Rainer Andreas Mittermeier were checked as novelty controls. Their public descriptions emphasize exact event ordering and complete interval minima rather than inference from a numerical sampling grid. They do not supply the generic asymptotic mesh theorem above. That distinction is important: exact finite positivity certification and asymptotic tail sampling are different problems.

Targeted searches combining Suzuki's screw function with `sampling sequence`, `sampling grid`, cubic/polynomial subsequences, ordinary-prime sampling, and `F(n)` did not expose a published statement of the exact sub-`3/4` reduction. This absence is not evidence of novelty. The proof is elementary interpolation plus event counting once Suzuki's formula is known, so the safe classification is `EXACT-DERIVED` and the durable contribution is the negative structural implication for `prime_lattice`.

## Adversarial boundaries and falsification

1. **This does not make the arithmetic in `Psi` generic.** The completed function being sampled still contains the full rational-prime von-Mangoldt history, pole term, gamma factor, and analytic continuation. The genericity concerns only the observation mesh after that information has already been compressed into one scalar function.

2. **It does not replace prime-power checkpoints for exact finite positivity.** An `o(1)` additive interpolation error cannot preserve positivity when the true margin may tend to zero. The Mittermeier/Suzuki checkpoint minimum machinery remains necessary for a rigorous finite-interval positivity certificate. The present theorem transfers boundedness, growth exponents, and asymptotic ratios, not exact pointwise sign from sparse samples.

3. **`kappa<3/4` is a sufficient threshold for this crude deterministic argument, not a proved necessary threshold for every possible sampling theorem.** At or above `3/4`, the smooth curvature term alone ceases to be `o(1)` under this chord estimate. Additional cancellation could in principle improve a special mesh, but it would require new structure.

4. **The result does not say a fixed one-prime axis is sufficient.** Geometric sampling `x_j=p^j` has gaps of order `x_j`, corresponding to `kappa=1`, far outside the proved regime. The one-prime-axis question remains logically separate from this mesh reduction.

5. **No Euler product is continued into the critical strip.** All interpolation is performed on Suzuki's already-completed real-variable objects. RH enters only through Suzuki's peer-reviewed criterion and the separately audited completed `xi'/xi`/Landau consequences in `PL-153/154`.

A falsification of the generic mesh theorem would require failure of the exact ramp decomposition, the standard chord-error inequality, the hinge bound `Delta/4`, the curvature estimate `R''(log x)=O(sqrt(x))`, or the elementary bound that an interval of length `h` contains at most `h+1` integer prime-power events. No distributional hypothesis on primes is present.

## Consequence for the research line

`PL-156` remains useful as an exact statement that the canonical depth-one prime basis is an RH-complete observation set for Suzuki's completed scalar tail. The present control changes how that fact should be interpreted: **being an RH-complete observation set is not evidence that the prime basis itself supplies the missing mechanism.** Cubic integers and many other exogenous meshes have the same property.

Accordingly, do not pursue the Suzuki scalar channel by trying to make the observation set progressively more "prime-geometric" after completion. The research burden remains upstream: explain or constrain the cumulative arithmetic state that produces `Psi(log x)` before generic interpolation takes over. A genuinely prime-lattice mechanism must act on the forcing/history, on a non-scalar structure, or on a discriminator that fails for the cubic-mesh control; sampling sufficiency by itself no longer qualifies as such a discriminator.