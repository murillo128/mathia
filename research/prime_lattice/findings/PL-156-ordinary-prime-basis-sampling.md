# PL-156 — Ordinary prime basis vectors already sample Suzuki's RH-sensitive growth

## Claim

Let `Psi` be Masatoshi Suzuki's completed real even function attached to the Riemann zeta function, with the decomposition used in `PL-146`

`Psi(t) = R(t) - sum_(q<=exp(t)) w_q (t-log q)`,

where the arithmetic events are prime powers `q=l^k` and

`w_q = Lambda(q)/sqrt(q) = log(l)/sqrt(q)`.

Write `p<r` for consecutive **ordinary primes**, set `a=log p`, `b=log r`, and let `C_(p,r)(t)` be the affine chord joining `Psi(a)` and `Psi(b)`. Then, uniformly for `a<=t<=b`,

`Psi(t) = C_(p,r)(t) + eta_p(t)`

with

`sup_(a<=t<=b) |eta_p(t)| = O(p^(-0.45) + p^(-0.475) log^2 p) = o(1)`.

More structurally, if one only assumes a consecutive-prime gap bound

`r-p = O(p^kappa)`

for some `kappa<3/4`, the same argument gives

`sup |eta_p| = O(p^(2 kappa-3/2) + p^(kappa-1) log^2 p) = o(1)`.

Baker--Harman--Pintz supply the unconditional admissible value `kappa=0.525`.

Thus, although Suzuki's explicit arithmetic forcing is supported on **all prime powers** `k e_l`, its completed scalar function is asymptotically determined between consecutive ordinary-prime energies by the values on the basis vectors

`v(p)=e_p`,  `E(e_p)=log p`.

Combining this interpolation theorem with the exact one-sided checkpoint results `PL-153` and `PL-154` gives

`RH <=> sup_(p prime) Psi(log p) < infinity`,

and, independently,

`RH <=> inf_(p prime) Psi(log p) > -infinity`.

If RH fails, therefore,

`limsup_(p->infinity, p prime) Psi(log p)=+infinity`

and

`liminf_(p->infinity, p prime) Psi(log p)=-infinity`.

Moreover, if `Theta=sup{Re rho: xi(rho)=0}` and `theta=Theta-1/2`, define the prime-basis one-sided exponents

`beta_+ = inf{delta>=0 : Psi(log p) <= C p^delta eventually on primes}`,

`beta_- = inf{delta>=0 : -Psi(log p) <= C p^delta eventually on primes}`.

Then

`beta_+ = beta_- = theta = Theta-1/2`.

There is also a direct peer-reviewed Suzuki corollary that does not use `PL-153/154`. For

`F(x)=sum_(n<=x) Lambda(n)/sqrt(n) log(x/n) - 4 sqrt(x)`

and `alpha=zeta'(1/2)/zeta(1/2)>0`, Suzuki proves

`RH <=> F(x)/log x -> -alpha`.

The same ordinary-prime interpolation argument gives the sharper sampling equivalence

`RH <=> F(p)/log p -> -alpha` as `p->infinity` through ordinary primes.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + STRUCTURAL-REDUCTION + NEGATIVE/OBSTRUCTION`. Suzuki's formulas and RH equivalences are peer-reviewed literature; the required prime-gap estimate is classical Baker--Harman--Pintz. The ordinary-prime chord estimate and its consequences are exact derived statements. A targeted current-literature search did not locate this exact restriction of Suzuki's criteria to ordinary-prime sampling, but no novelty claim is made.

## Exact chord decomposition between consecutive ordinary primes

Fix consecutive ordinary primes `p<r`, and put

`a=log p`, `b=log r`, `Delta=b-a`.

Every prime-power event strictly inside `(p,r)` must have exponent at least two. Let

`Q_(p,r)={q=l^k : k>=2, p<q<r}`.

All prime-power ramps activated at or before `p` are affine functions of `t` throughout `[a,b]`; the new ordinary-prime ramp at `r` has zero value at `b` and does not affect the value on the closed interval. Hence Suzuki's exact formula can be written on `[a,b]` as

`Psi(t)=R(t)-L_(p)(t)-sum_(q in Q_(p,r)) w_q (t-log q)_+`,

where `L_(p)` is affine and `(u)_+=max(u,0)`.

Let `Ch[f]` denote affine interpolation of `f(a)` and `f(b)`. Since `Ch[L_(p)]=L_(p)`,

`Psi-Ch[Psi] = (R-Ch[R]) - sum_(q in Q_(p,r)) w_q (h_q-Ch[h_q])`,

with `h_q(t)=(t-log q)_+`.

Two elementary interpolation bounds now separate the smooth and arithmetic errors.

First, for every twice differentiable function on `[a,b]`,

`sup |f-Ch[f]| <= (Delta^2/8) sup |f''|`.

The exact curvature calculation already derived from Suzuki's formula in `PL-146` is

`R''(t) = (x^3-x-1)/(sqrt(x)(x^2-1))`,  `x=e^t`.

For `x>=2` this is `O(sqrt(x))`, so on the present interval

`sup_(a<=t<=b) |R(t)-Ch[R](t)| = O(sqrt(r) Delta^2)`.

Second, if `u` lies in `[a,b]`, direct inspection of the hinge `h_u(t)=(t-u)_+` gives

`sup_(a<=t<=b) |h_u(t)-Ch[h_u](t)| <= Delta/4`.

Therefore

`sup |Psi-Ch[Psi]| <= O(sqrt(r) Delta^2) + (Delta/4) sum_(q in Q_(p,r)) w_q`.

This estimate is deterministic and uses no zero information.

## Bounding the skipped higher-prime-power mass

Only the prime powers with exponent at least two are skipped when the sampling grid keeps ordinary primes and discards internal events. Their total half-weight up to `x` is small enough for a very crude estimate to suffice:

`W_2(x)=sum_(l^k<=x, k>=2) log(l)/l^(k/2) = O(log^2 x)`.

Indeed, the square terms satisfy

`sum_(l<=sqrt(x)) log(l)/l <= sum_(n<=sqrt(x)) log(n)/n = O(log^2 x)`,

while all `k>=3` terms are uniformly summable because

`sum_l sum_(k>=3) log(l)/l^(k/2)
 <= sum_(n>=2) [log n * n^(-3/2)/(1-n^(-1/2))] < infinity`.

No prime number theorem is needed for this weight estimate. In particular,

`sum_(q in Q_(p,r)) w_q <= W_2(r)=O(log^2 r)`.

Now assume `r-p=O(p^kappa)` with `kappa<1`. Then

`Delta=log(r/p)=O(p^(kappa-1))`

and `r/p->1`. Substitution into the chord bound yields

`sup |Psi-Ch[Psi]|
 = O(p^(1/2) p^(2kappa-2)) + O(p^(kappa-1) log^2 p)`

`= O(p^(2kappa-3/2) + p^(kappa-1) log^2 p)`.

The first term tends to zero exactly when `kappa<3/4`; the second already tends to zero for every `kappa<1`. Baker, Harman and Pintz prove that every sufficiently large interval `[x,x+x^0.525]` contains a prime, giving the standard consequence

`p_(n+1)-p_n = O(p_n^0.525)`.

Thus `kappa=0.525<3/4` is unconditional and gives the displayed numerical exponents `-0.45` and `-0.475`.

The threshold `3/4` is worth recording. It is not a zeta-zero threshold: it is the sampling-density threshold obtained by balancing Suzuki's smooth curvature scale `sqrt(x)` against the **square** of the logarithmic ordinary-prime mesh.

## One-sided boundedness and zero-frontier exponents on the basis

For `t in [log p,log r]`, write

`lambda=(t-log p)/(log r-log p)`.

The interpolation theorem says

`Psi(t)=(1-lambda)Psi(log p)+lambda Psi(log r)+o(1)`

uniformly as `p->infinity` through consecutive ordinary primes.

If the ordinary-prime samples are eventually bounded above by `M`, then the chord is bounded above by `M`, and the `o(1)` error makes `Psi` bounded above on the entire sufficiently large half-line. The compact initial interval contributes only a finite maximum. The converse is immediate because the prime samples are a subset of the continuum. Hence

`Psi bounded above on R_+ <=> {Psi(log p)}_(p prime) bounded above`.

The same argument with `-Psi` gives the lower-bounded equivalence. By the exact Landau/zero-series argument in `PL-153`, either one-sided continuum boundedness is equivalent to RH. This proves the two prime-basis RH criteria in the claim and transfers the off-RH two-sided unbounded oscillation to the basis samples.

The growth-exponent transfer is equally direct. If, for example,

`Psi(log p) <= C p^delta`

for all sufficiently large primes, then the neighboring endpoint values on an interval `[log p,log r]` are `O(e^(delta t))` because `r/p->1`; affine interpolation plus the uniform `o(1)` error gives the same exponent on the continuum. Restricting a continuum bound back to prime points is trivial. Therefore the prime-basis one-sided exponents equal the continuum/checkpoint exponents. `PL-154` identifies each of those exactly with

`Theta-1/2`.

So the basis vectors do not merely retain the yes/no RH criterion; their one-sided growth rates retain the full rightmost-zero frontier encoded by Suzuki's completed scalar function.

## Direct ordinary-prime sampling of Suzuki's weighted-Chebyshev criterion

The same interpolation estimate applies to Suzuki's 2025 statistic without invoking the completed screw function. Put

`H(t)=F(e^t)=sum_(q<=e^t) w_q (t-log q)-4e^(t/2)`.

Between prime-power events its smooth second derivative is exactly

`H''(t)=-e^(t/2)`,

and every internal higher-prime-power event contributes the positive hinge `w_q(t-log q)_+`. Repeating the preceding chord argument gives, between consecutive ordinary primes,

`H(t)=Ch[H](t)+o(1)`

uniformly.

Suzuki's Theorem 1 states

`RH <=> H(t)/t -> -alpha`,  `alpha=zeta'(1/2)/zeta(1/2)`.

If this limit is known only at ordinary-prime points `t=log p`, the chord relation recovers it at every intermediate `t`: the two endpoint logarithms and `t` are asymptotic because `Delta=o(1)`, and the additive interpolation error is `o(1)`, hence negligible after division by `t`. The reverse implication is restriction. Therefore

`RH <=> F(p)/log p -> -alpha` along ordinary primes.

This gives an independent literature-backed bridge from basis sampling to RH and prevents the completed-screw route from being the only support for the reduction.

## Prime-exponent interpretation

The sampling set in this finding is exactly

`{e_p : p prime}`,

the canonical basis of the positive exponent lattice. This is a stronger dimensional collapse than the prime-power-axis reduction in `PL-146` and `PL-147`: those findings show that the **forcing** of the relevant scalar statistics lives on the full axis skeleton `{k e_p}`. Here the forcing remains unchanged, but the **observation set** needed to recover the RH-sensitive tail behavior can be reduced to depth-one basis points alone.

This does not mean higher prime powers have disappeared from the arithmetic. The value `Psi(log p)` or `F(p)` contains the cumulative history of every prime power below `p`. What disappears is the need to observe the scalar function at those higher-power event locations separately. Their possible distortion between successive basis samples is too small to hide a boundedness failure or a nonzero growth exponent.

Unlike the two-prime dense-group reduction in `PL-155`, this ordinary-prime result is **not generic Kronecker sampling**. The set `{log p}` is not dense on bounded real intervals, and continuity alone would be useless because the derivative scale grows with `p`. The proof needs two specifically arithmetic facts together:

1. ordinary rational primes have gaps `O(p^kappa)` for some `kappa<3/4`;
2. the skipped higher powers have total critical half-weight only `O(log^2 p)` in the required estimate.

That distinction survives the line's generalized-prime control. A Beurling/generalized-prime system with much larger gaps need not admit the same basis-sampling theorem even if its prime-power formula is formally similar.

## Analytic-continuation boundary

No Euler product is analytically continued in the interpolation proof. Suzuki's displayed formulas for `Psi` and `F` are already established arithmetic/analytic objects, and the chord estimate is a real-variable consequence of those formulas plus a theorem on ordinary-prime gaps.

The RH implication enters only through previously justified continuation mechanisms: Suzuki's peer-reviewed weighted-Chebyshev theorem for `F`, and the completed `xi'/xi`/Landau arguments audited in `PL-153` and `PL-154` for `Psi`. Sampling does not create continuation; it shows that once those scalar criteria are constructed, their RH-sensitive tail cannot hide between consecutive ordinary primes.

## Prior-art and novelty audit

Primary sources:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. Equation (1.1) gives the prime-power-ramp formula for `Psi`; Theorem 1.1 gives the transform/zero representation; Theorem 1.2 and the later positivity criteria provide the completed screw framework used by `PL-146`, `PL-153`, and `PL-154`.
- **Masatoshi Suzuki**, “On variants of Chebyshev's conjecture,” *The Ramanujan Journal* **68** (2025), article 95, DOI `10.1007/s11139-025-01238-9`; arXiv `2411.07436`. Theorem 1 proves the RH-equivalent eventual-sign and asymptotic criterion for `F(x)`. The December 2025 correction concerns later arithmetic-progression material, not Theorem 1.
- **R. C. Baker, G. Harman, J. Pintz**, “The Difference Between Consecutive Primes, II,” *Proceedings of the London Mathematical Society* **83**(3) (2001), 532–562, DOI `10.1112/plms/83.3.532`. Their short-interval theorem with exponent `0.525` supplies the unconditional consecutive-prime mesh bound used here.

Current novelty controls:

- Rainer Andreas Mittermeier's August 2026 Zenodo checkpoint series explicitly works with one convex checkpoint per **prime-power** interval and exact prime-power event ordering. Searches of its public records for ordinary-prime-only sampling did not locate the basis restriction above. Those preprints are used only as current novelty controls, not as authority for this proof.
- Targeted searches for `"Psi(log p)" Riemann hypothesis Suzuki`, `ordinary primes Suzuki screw function`, `prime-only screw function`, `prime sampling Suzuki Riemann`, and `consecutive primes Suzuki Riemann hypothesis` did not locate a published statement of the exact ordinary-prime interpolation or the resulting one-sided basis criteria.
- The proof uses standard interpolation estimates and a classical prime-gap theorem, so absence of exact wording is not evidence of novelty. The durable value is the structural consequence for this research line, not a priority claim.

This finding is not a duplicate of `PL-146`: that finding discretizes the continuum at **every prime-power interval minimum**. It is not a duplicate of `PL-153/154`: those identify one-sided boundedness and growth exponents on the full prime-power checkpoint set. It is not a duplicate of `PL-155`: that finding uses a generic rank-two dense difference group to test completed screw positivity. Here the observation set is the disconnected rank-infinite basis `{e_p}`, and the bridge is quantitative rational-prime spacing plus the small mass of skipped higher-power hinges.

## Adversarial boundaries and falsification

1. **This does not prove RH.** It says that any boundedness/growth failure required by an off-line zero must already become visible along the ordinary-prime basis samples. Proving those samples satisfy the required bound remains RH-equivalent.

2. **Basis sampling is not basis-only forcing.** Every sampled value retains the cumulative contribution of all prior prime powers. It would be false to infer that the von Mangoldt prime-power terms can be deleted from Suzuki's formula.

3. **The critical `1/2` is still supplied by Suzuki's construction.** The event weights are `Lambda(q)/sqrt(q)` and the smooth curvature has scale `sqrt(x)`. The argument exploits that normalization; it does not derive the critical line from abstract lattice geometry.

4. **The prime-gap input is genuinely load-bearing.** Mere `p_(n+1)/p_n -> 1` is not enough for the displayed `o(1)` interpolation estimate because the smooth curvature grows like `sqrt(p)`. The elementary proof above requires a gap exponent strictly below `3/4`; Baker--Harman--Pintz supplies `0.525`.

5. **The `O(log^2 x)` higher-power bound is deliberately crude but sufficient.** Sharpening it does not change the `3/4` threshold, which comes from the smooth curvature term. A falsification would need either a missing non-hinge arithmetic term, a larger curvature scale, or failure of the claimed consecutive-prime gap estimate.

6. **Pointwise positivity does not automatically interpolate with its sign.** Nonnegative endpoint samples would only imply an `o(1)` lower error between them, not literal positivity at every intermediate point. The RH equivalences used here are one-sided boundedness/growth and Suzuki's asymptotic criterion, for which `o(1)` interpolation is sufficient. This distinction prevents an invalid claim that checking `Psi(log p)>=0` is directly the same finite-sign test as checking every prime-power minimum.

7. **Generalized-prime controls need not inherit the theorem.** The reduction depends on a quantitative gap theorem for the actual rational primes and on the specific critical half-weights. A formal Beurling analogue without comparable spacing can fail at the sampling step.

The cleanest audit test is the chord bound itself. For every sufficiently large pair of consecutive ordinary primes, independently verify the decomposition into the smooth term, an affine old-event term, and higher-power hinges; then verify the two interpolation inequalities and substitute any proven `kappa<3/4` prime-gap exponent. If this yields a non-vanishing error term, the basis-sampling consequences must be withdrawn.

## Consequence for the research line

For Suzuki's scalar completed/weighted-Chebyshev channels, the observation geometry has now collapsed further than the prime-power axis skeleton suggests:

`full exponent lattice -> prime-power forcing {k e_p} -> ordinary-prime observations {e_p}`.

The last arrow is not generic harmonic-analysis universality: it uses a quantitative theorem about rational-prime spacing. Nevertheless it is still a **reduction**, not the missing RH mechanism. It shows that adding higher-depth axis observations or mixed exponent points cannot by itself solve the scalar tail problem; any successful new lattice mechanism must force the required basis-sample bound/sign through additional arithmetic or operator structure.

A useful surviving target is therefore to seek a structure that constrains the sequence

`p -> Psi(log p)`

(or equivalently Suzuki's weighted statistic at prime arguments) in a way unavailable for generalized-prime controls. The sampling theorem guarantees that such a bound would not lose zero-frontier information, while avoiding the false hope that more lattice dimensions are needed merely to observe that information.