# PL-150 — Prime gaps make terminal Suzuki recovery drawdown vanish; the surviving defect is event-level memory

## Claim

The exact Suzuki checkpoint dynamics of `PL-146` has an unconditional asymptotic flattening property at every sufficiently large **recovery witness**. Let `q=p^k` be the last prime-power event before a workload recovery, let `r` be the next prime-power event, and write

`lambda=log q`,  `lambda'=log r`.

On the event interval `[lambda,lambda']`, write

`Psi(t)=R(t)-P_q t+Q_q`,

as in `PL-146`, and let `t_q in (lambda,lambda']` be the recovery point/minimizer satisfying

`R'(t_q)=P_q`.

Then the final inter-event drawdown from the event value to the recovered local minimum is

`d_q := Psi(lambda)-Psi(t_q)`

and obeys the exact Bregman bound

`0 <= d_q <= (1/2) sup_[lambda,lambda'] R'' * (lambda'-lambda)^2`.

Suzuki's explicit curvature formula gives `R''(log x) <= (4/3)sqrt(x)` for `x>=2`. Combining this with the classical Baker--Harman--Pintz prime-gap bound `p_(n+1)-p_n << p_n^0.525` yields

`r-q << q^0.525`,

hence

`boxed:  0 <= Psi(log q)-Psi(t_q) << q^(-0.45).`

In particular, along any unbounded sequence of recovery witnesses,

`Psi(t_q)=Psi(log q)+o(1)`.

Thus the terminal convex descent inside the last prime-power interval of a recovered episode becomes asymptotically negligible. Since `PL-149` proves unconditionally that recoveries occur infinitely often, this is an infinite-tail statement rather than a finite-computation observation.

The consequence is primarily a **negative structural reduction** for the RH program. A large-`q` violation at a recovered minimum cannot be attributed to an order-one local Bregman drop between the last event and the recovery. Up to a shrinking `O(q^-0.45)` boundary layer, its height is already present at the preceding prime-power event. The unresolved information therefore lies in the accumulated event-level history/memory that determines `Psi(log q)`, not in the final local convex geometry by itself.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + STRUCTURAL-REDUCTION + NEGATIVE/OBSTRUCTION`. The Suzuki checkpoint representation and curvature formula are already reconstructed from peer-reviewed literature in `PL-146`; Baker--Harman--Pintz supply the unconditional short-prime-interval exponent `0.525`. The displayed `q^-0.45` estimate is an elementary consequence of those inputs. Current August 2026 checkpoint preprints already use the recovery-witness/Bregman organization, so no novelty is claimed for that organization. A targeted literature search did not locate this specific prime-gap asymptotic for the terminal recovery drawdown; it is stored as an exact derived line-level reduction, not as a novelty claim.

## Exact Bregman estimate on the last active interval

Let `q` be the last arithmetic event before a recovery and `r` the next prime-power event. The post-event workload is

`Y(lambda^+)=P_q-R'(lambda)>0`.

Because the workload recovers before the next upward jump, one has

`P_q <= R'(lambda')`.

Strict convexity from `PL-146` therefore gives a unique `t_q in (lambda,lambda']` with

`R'(t_q)=P_q`.

On this entire interval the active arithmetic state is fixed, so

`Psi(t)=R(t)-P_q t+Q_q`.

Subtracting the value at the minimizer gives

`d_q = R(lambda)-R(t_q)-R'(t_q)(lambda-t_q)`.

This is the Bregman divergence of `R` with the arguments in the displayed order. Integrating the derivative difference gives the exact positive representation

`d_q = integral_lambda^t_q [R'(t_q)-R'(u)] du`

`    = integral_lambda^t_q (v-lambda) R''(v) dv.`

Consequently

`0 <= d_q <= (1/2) M_q (t_q-lambda)^2`

with

`M_q=sup_[lambda,lambda'] R''`,

and therefore

`0 <= d_q <= (1/2) M_q (lambda'-lambda)^2.`

The estimate also covers the endpoint case `t_q=lambda'`: the newly activated ramp at `r` has zero value at the event, so the old-state formula gives the value at the right endpoint exactly.

## Curvature grows only like the square root of the event scale

`PL-146` derives from Suzuki's smooth completed term

`R''(log x) = (x^3-x-1)/(sqrt(x)(x^2-1))`,  `x>=2`.

It follows directly that

`0 < R''(log x)`

and

`R''(log x) < x^3/(sqrt(x)(x^2-1))`

`             = sqrt(x) x^2/(x^2-1)`

`             <= (4/3) sqrt(x)`

for `x>=2`. Hence on `[log q,log r]`,

`M_q <= (4/3)sqrt(r)`

and

`d_q <= (2/3)sqrt(r) (log(r/q))^2.`

This estimate is purely local and exact apart from the harmless numerical upper bound on the curvature. It uses no zero information and no assumption of RH.

## Prime gaps force the terminal drawdown to zero

Baker, Harman and Pintz proved the unconditional short-interval exponent `0.525`; equivalently, consecutive ordinary primes satisfy

`p_(n+1)-p_n << p_n^0.525`.

This immediately controls the mesh of **prime powers** as well. If the event `q` is itself prime, the next prime is an admissible later prime-power event and lies `O(q^0.525)` away. If `q` is a proper prime power, place it between consecutive primes `p_n<q<p_(n+1)`. Their gap is `O(p_n^0.525)` and, because that gap is `o(p_n)`, one has `p_n asymp q`; the next prime is again a later prime-power event. Therefore the next prime-power `r` satisfies

`r-q << q^0.525`.

Since

`log(r/q) = log(1+(r-q)/q) <= (r-q)/q`,

we obtain

`log(r/q) << q^(-0.475)`

and also `sqrt(r) asymp sqrt(q)`. Substitution in the preceding Bregman estimate yields

`d_q << q^(1/2) q^(-0.95) = q^(-0.45)`.

The exponent `0.525` is only a convenient unconditional theorem-level input, not a claimed optimal value. More generally, any prime-gap estimate

`r-q << q^theta`

with `theta<3/4` gives

`d_q << q^(2 theta-3/2)=o(1)`.

Thus the qualitative conclusion needs only a substantially weaker mesh theorem than the best classical short-interval results.

## Asymptotic equivalence of witness-event and recovery-minimum values

Let `q_j -> infinity` be any sequence of recovery witnesses and `t_j=t_(q_j)` the associated recovered minima. The estimate above gives

`0 <= Psi(log q_j)-Psi(t_j) -> 0`.

Therefore the two sequences have the same finite or extended limit points, in particular

`liminf_j Psi(t_j) = liminf_j Psi(log q_j)`

and

`limsup_j Psi(t_j) = limsup_j Psi(log q_j)`.

This is the strongest useful interpretation of the local estimate. It does **not** say that positivity at `log q_j` is pointwise equivalent to positivity at `t_j`: a positive event value smaller than the shrinking drawdown can still cross below zero. That distinction matters because `PL-146` already proves conditionally under RH that the checkpoint margins have infimum zero. Any valid RH proof must therefore tolerate arbitrarily small reserves; replacing the exact minimum inequality by an endpoint inequality with a fixed positive buffer is impossible.

What the estimate does say is that no order-one asymptotic information is created during the terminal recovery segment. If a subsequence of recovered minima has a negative limit bounded away from zero, the corresponding event values have the same negative limit. Conversely, any order-one lower-bound mechanism at witness events transfers to the recovered minima with only a vanishing error.

## Relation to the exponent lattice

For the event `q=p^k`,

`v(q)=k e_p`,

`log q=<v(q),(log ell)_ell>`,

and the workload jump is

`w_q=Lambda(q)/sqrt(q)=log(p) exp(-log(q)/2)`.

The estimate therefore concerns the spacing of consecutive events in the energy projection of the prime-power axis skeleton. Ordinary primes alone are dense enough on the multiplicative scale to force

`Delta log q = log(r/q)=O(q^-0.475)`,

while the completed archimedean curvature grows only as `sqrt(q)`. Their combination makes the final Bregman loss vanish.

This does not restore mixed-support exponent vectors: the Suzuki forcing remains on the rays `k e_p`, exactly as in `PL-146`--`PL-149`. Nor does the estimate derive the critical `1/2`; the `sqrt(q)` scale and the jump weight `Lambda(q)/sqrt(q)` already come from Suzuki's completed critical normalization.

## Prior-art and novelty audit

The theorem-level inputs are:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487, DOI `10.1112/jlms.12785`. This is the peer-reviewed source for the completed screw function, the prime-power explicit formula, and the RH-equivalent positivity criterion underlying the exact checkpoint reconstruction in `PL-146`.
- **R. C. Baker, G. Harman, J. Pintz**, “The Difference Between Consecutive Primes, II,” *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`. The paper proves that sufficiently large intervals at scale `x^0.525` contain primes, giving the standard consecutive-prime-gap consequence used above.
- **Rainer Andreas Mittermeier**, “Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail — Part 4,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076079`. Its public description already organizes the last active prime-power event as a recovery witness and uses the same service-clock/Bregman language. It is a current self-published novelty control, not authority for the estimate proved here.
- **Rainer Andreas Mittermeier**, “Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence — Part 5,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076088`. Its public description gives the no-terminal/recovery-recurrence conclusion independently reconstructed in `PL-149`.

Targeted searches combining `recovery witness`, `prime gap`, `Bregman drawdown`, `prime-power checkpoint`, and Suzuki's screw function did not locate the quantitative implication `d_q=O(q^-0.45)`. That absence is not sufficient for a novelty claim, especially because the derivation is elementary once the checkpoint and prime-gap inputs are placed together. The safe classification is therefore `EXACT-DERIVED`: the result is preserved because it materially narrows the live RH mechanism, not because it is asserted to be new mathematics.

## Generic matched control

The flattening is not, by itself, rational-prime rigidity. Consider any event-driven convex reservoir with event scale `x`, inter-event logarithmic mesh `Delta log x=O(x^(theta-1))`, and smooth curvature `R''(log x)=O(x^beta)`. The same calculation gives terminal recovery drawdown

`O(x^(beta+2 theta-2))`.

It vanishes whenever

`beta+2 theta<2`.

The Suzuki/Riemann case has `beta=1/2`, so the threshold is exactly `theta<3/4`. Any generalized-prime or synthetic event system satisfying a comparable mesh bound and curvature law inherits the same local flattening. The phenomenon is therefore a geometric consequence of mesh density plus reservoir curvature, not a discriminator of the exact rational-prime norm map.

The rational-prime content that remains is in the accumulated state

`P_q=sum_(a<=q) Lambda(a)/sqrt(a)`,

`Q_q=sum_(a<=q) Lambda(a) log(a)/sqrt(a)`,

and hence in the event value `Psi(log q)`. A successful RH mechanism must constrain that history, or an equivalent completed arithmetic quantity, in a way that survives the generic mesh control.

## Adversarial boundaries and falsification

1. **This is not an RH proof and not a new RH criterion.** The exact unresolved condition remains nonnegativity of every recovered checkpoint/minimum. The estimate only compares that minimum with the preceding witness-event value.

2. **The estimate is terminal, not episode-wide.** An active episode may span many prime-power events and accumulate an order-one or larger loss before its final event. Nothing here proves that Mittermeier's full debit/history statistic or the cumulative `J_q` term is `o(1)`.

3. **Vanishing additive error does not preserve signs near zero.** Because RH-compatible checkpoint margins can approach zero, `Psi(log q)>0` without a quantitative buffer does not imply `Psi(t_q)>=0`.

4. **The prime-gap theorem is used only as a mesh bound.** The exponent `0.525` is sufficient, not canonical, and the local flattening persists in matched non-Riemann systems with a similar event mesh. It cannot explain the critical line by itself.

5. **No illicit analytic continuation occurs.** The Bregman calculation is performed directly on Suzuki's real-variable completed function. The prime-gap input is an ordinary theorem about rational primes. No Euler product is evaluated outside its convergence region.

6. **Recovery existence is logically separate.** `PL-149` supplies infinitely many recoveries from the completed `xi` transform and Landau's theorem. The present estimate does not reprove that recurrence; it quantifies the local value loss once a recovery witness exists.

7. **The full exponent lattice remains absent.** As in the parent Suzuki findings, the forcing uses only prime-power axis points. The result cannot justify mixed-prime geometry unless that geometry produces an independent constraint on the accumulated event-level state.

A falsification of the quantitative claim would require failure of the exact convex interval formula in `PL-146`, failure of the curvature bound derived from Suzuki's displayed `R''`, or failure of the classical short-prime-interval estimate used to bound the next prime-power mesh. The derivation contains no additional asymptotic assumption.

## Consequence for the research line

Do not spend further passes looking for an RH mechanism solely in the **terminal local shape** of a recovered Suzuki interval. At large recovery witnesses that shape contributes only `O(q^-0.45)` to the minimum height. Together with `PL-149`, the picture is now sharper: analytic continuation forces infinitely many recoveries, prime-gap density makes the last recovery descent asymptotically flat in value, and the unresolved RH content sits in the accumulated height carried into those terminal intervals.

A surviving checkpoint approach must therefore control `Psi(log q)` (or an equivalent cumulative Chebyshev/explicit-formula memory) at the recovery-witness events to a precision compatible with a vanishing reserve. Any genuinely prime-lattice mechanism should explain how exact rational-prime structure constrains that event-level memory beyond the generic continuation recurrence and mesh-flattening effects established here.