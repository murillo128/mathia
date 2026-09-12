# VIS-194 — weighted nearest-neighbor prime-ratio spacing controls finite-start dephasing

## Claim

Keep the notation and hypotheses of `VIS-192` and `VIS-193`. Thus

`F_(y,H)(T)=M_v(y;H,T)-1`

is the finite symmetric exponential polynomial

`F_(y,H)(T)=sum_(lambda in Lambda_y) c_lambda exp(i lambda T)`,

with

`Lambda_y={+/-log(q/p): p<q<=y, p,q prime}`

and exact coefficient mass

`sum_(lambda in Lambda_y) |c_lambda|^2 = R_v(y,H)`.

For every `lambda in Lambda_y`, define its individual nearest-neighbor spacing

`delta_lambda=min_(mu in Lambda_y, mu!=lambda) |lambda-mu|`,

and define the weighted inverse-spacing energy

`W_v(y,H)=sum_(lambda in Lambda_y) |c_lambda|^2/delta_lambda`.

Then for every real start `T0` and every `L>0`,

`|R_(v,L)(T0;y,H)-R_v(y,H)| <= (3 pi/L) W_v(y,H)`.

When `R_v(y,H)>0`, put

`D_v(y,H)=W_v(y,H)/R_v(y,H)`.

Then

`|R_(v,L)(T0;y,H)-R_v(y,H)| <= [3 pi D_v(y,H)/L] R_v(y,H)`.

The estimate is uniform in `T0`. If `R_v(y,H)=0`, all coefficients vanish and the conclusion is trivial.

Consequently, in the `VIS-192` regime `H=H(y)->infinity`, `H<=y`, any deterministic start-window family satisfying

`L >= C D_v(y,H)`

obeys

`R_(v,L)(T0;y,H) <<_(alpha,v,C) 1/H`

uniformly in `T0`. If instead

`L/D_v(y,H) -> infinity`,

then uniformly in `T0`,

`R_(v,L)(T0;y,H)=R_v(y,H)(1+o(1))`.

If also `H log y/y -> 0`, this gives

`R_(v,L)(T0;y,H) asymp_(alpha,v) 1/H`.

Moreover

`D_v(y,H) <= y^2+1`,

so the weighted theorem recovers the coarse `VIS-193` horizon up to constants. Its value is that the sufficient horizon is no longer forced by the single worst pair of frequencies: it is the coefficient-energy-weighted average of the individual inverse spacings.

**Evidence/status:** `LITERATURE+DERIVED + WEIGHTED-HILBERT REDUCTION + NO-NOVELTY-CLAIM`.

No estimate `D_v=o(y^2)` is proved here. The finding isolates that estimate, or a comparable weighted near-collision bound, as the exact next arithmetic question.

## 1. Finite-start error is the difference of two Hilbert forms

For brevity write `F(T)=sum_lambda c_lambda exp(i lambda T)`. Expanding the finite-window mean square gives

`int_(T0)^(T0+L) |F(T)|^2 dT`
` = L sum_lambda |c_lambda|^2`
` + sum_(lambda!=mu) c_lambda conjugate(c_mu)`
`   [exp(i(lambda-mu)(T0+L))-exp(i(lambda-mu)T0)]/[i(lambda-mu)]`.

For any real endpoint `A`, define

`H_A=sum_(lambda!=mu) c_lambda conjugate(c_mu)`
`    exp(i(lambda-mu)A)/(lambda-mu)`.

Then the off-diagonal contribution is `(H_(T0+L)-H_T0)/i`.

Thus the finite-start problem is exactly a pair of generalized Hilbert forms on the prime-ratio frequency set. Translation in `T0` only rotates the coefficients and does not change their moduli or frequency spacings.

## 2. Montgomery–Vaughan weights the error by local frequency spacing

Montgomery and Vaughan's weighted Hilbert inequality for distinct real frequencies states, in the quadratic specialization used here, that if

`delta_lambda=min_(mu!=lambda)|lambda-mu|`,

then

`|sum_(lambda!=mu) z_lambda conjugate(z_mu)/(lambda-mu)|`
` <= (3 pi/2) sum_lambda |z_lambda|^2/delta_lambda`.

Apply this first with

`z_lambda=c_lambda exp(i lambda T0)`

and then with

`z_lambda=c_lambda exp(i lambda (T0+L))`.

Both endpoint forms therefore satisfy

`|H_A| <= (3 pi/2) W_v(y,H)`.

The triangle inequality gives

`|H_(T0+L)-H_T0| <= 3 pi W_v(y,H)`.

After division by `L`, and using `sum |c_lambda|^2=R_v(y,H)`, the claimed finite-window estimate follows.

This is strictly a specialization of the classical weighted Hilbert inequality. The new Mathia content is the identification of its local-spacing weights as the appropriate resource for the exact prime-ratio polynomial produced by `VIS-192`.

## 3. Relation to the worst-spacing bound in VIS-193

`VIS-193` used only the global minimum spacing

`delta_y=min_(lambda!=mu)|lambda-mu| >= log(1+y^(-2))`.

Therefore every individual spacing obeys

`delta_lambda^(-1) <= delta_y^(-1) <= y^2+1`,

and hence

`W_v(y,H) <= (y^2+1) R_v(y,H)`,

which proves

`D_v(y,H) <= y^2+1`.

Substitution into the weighted inequality gives a `O(y^2/L)` relative error, recovering the same universal scale as `VIS-193` with a weaker absolute constant. Thus `VIS-194` is not a better global minimum-gap theorem; it is a refinement that can improve only when the coefficient mass avoids, or assigns little energy to, the closest frequency collisions.

This distinction matters because the taper already changes the coefficient profile strongly through

`c_(+log(q/p))=Q_y^(-1) p^(-alpha) q^(-alpha) kappa_v(H log(q/p))`,

with the negative-frequency coefficient its conjugate. A near-collision with tiny coefficient mass should not determine the entire deterministic observation horizon, and the weighted Hilbert inequality makes that principle exact.

## 4. Each prime-ratio frequency has an elementary arithmetic spacing floor

The individualized spacings also admit a simple pair-dependent lower bound. Fix the positive frequency

`lambda=log(q/p)`, `p<q<=y`.

For another positive frequency `mu=log(s/r)`,

`lambda-mu=log(qr/(ps))`.

For a negative frequency `mu=-log(s/r)`,

`lambda-mu=log(qs/(pr))`.

In either case the numerator and denominator are distinct positive integers, and each is at most `q y`. Therefore

`|lambda-mu| >= log(1+(q y)^(-1))`.

The same bound holds for the reflected negative frequency. Hence

`delta_(p,q)^(-1) <= [log(1+(q y)^(-1))]^(-1) <= q y+1`.

Consequently the weighted resource has the explicit prime-pair bound

`W_v(y,H)`
` <= 2 Q_y^(-2) sum_(p<q<=y)`
`    p^(-2alpha) q^(-2alpha) |kappa_v(H log(q/p))|^2 (q y+1)`.

This inequality by itself need not improve the `y^2` scale because the energy may still be concentrated near the largest primes. Its role is to show that `D_v` is a concrete arithmetic/taper-weighted spacing functional rather than an abstract spectral parameter.

## Prior-art audit

The weighted inequality is classical. H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`, proves generalized Hilbert inequalities for nonuniformly spaced real frequencies. The standard weighted form uses each frequency's own nearest-neighbor spacing and the constant `3 pi/2`; modern expositions emphasize that this is advantageous precisely when some frequencies are much more widely separated than the global minimum.

`VIS-193` already used the unweighted separated-frequency mean-square consequence of the same classical machinery. The present finding makes no novelty claim for Hilbert's inequality, nonharmonic Fourier analysis, large-sieve ideas, or local-spacing weighted inequalities. Nor is the definition of a weighted effective spacing claimed as a new general analytic concept.

The Mathia-specific step is the exact reduction of the `VIS-192` prime-ratio start-dephasing problem to the coefficient-weighted inverse nearest-neighbor spacing `D_v(y,H)`, together with the elementary pair-specific arithmetic floor above. This changes the live question from controlling the single worst collision to controlling the coefficient mass carried by near-colliding prime ratios.

## Boundaries and falsification

The hypotheses on `alpha`, `v`, `H`, `M_v`, and the normalization are exactly those of `VIS-192`. The finite-window weighted Hilbert estimate itself is deterministic and requires no asymptotic regime.

The theorem does **not** prove `D_v=o(y^2)`, does not identify the optimal deterministic start horizon, and does not show that a window shorter than `D_v` must fail. A weighted average of inverse nearest-neighbor spacings is a sufficient resource produced by this inequality, not a proved necessary scale.

The constant `3 pi` in the endpoint-difference estimate is also not competitive with the `2 pi` constant in the global minimum-gap formulation of `VIS-193`. When no information beyond the worst gap is available, `VIS-193` is numerically sharper. The new statement is useful only when local spacing and coefficient mass are analyzed together.

The individual spacing `delta_lambda` is taken in the full symmetric set `Lambda_y`, so possible positive/negative near-collisions are included. Distinctness follows from the same reduced prime-ratio argument used in `VIS-193`.

Falsify the finding by finding an error in the boundary-term decomposition, an incorrect constant or weighting in the Montgomery–Vaughan inequality, a missed collision in the symmetric frequency set, a failure of `sum |c_lambda|^2=R_v`, or an invalid integer-product bound in the individualized spacing floor.

## Research consequence

`VIS-193` closed the existence question for a deterministic finite start horizon at the coarse universal scale `y^2`. The present result identifies the first non-worst-case horizon supplied by classical nonharmonic Fourier theory:

`effective horizon = D_v(y,H)`.

The next coherent theorem is therefore arithmetic rather than formal-functional-analytic: estimate the weighted mass of prime-ratio near-collisions strongly enough to prove `D_v=o(y^2)` in a useful `(y,H)` regime, or show that the downstream application already supplies a deterministic start window `L` dominating `D_v`.

A further extension that merely reuses the global minimum gap would add no new information. Progress now requires a weighted multiplicative-energy or local large-sieve estimate adapted to the actual tapered coefficients.