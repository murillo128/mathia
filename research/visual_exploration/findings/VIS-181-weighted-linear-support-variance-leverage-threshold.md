# VIS-181 — natural prime-power weights suppress linear-support quadratic crowding at and beyond the critical exponent

## Claim

Keep the notation of `VIS-179`. For a finite prime support `P_y`, positive weights `w_p`, and

`Q_y = sum_(p in P_y) w_p^2`,

`D_2(y) = (sum_(p in P_y) w_p)^2 / Q_y`,

define the quadratic leverage

`L_y = sum_(p in P_y) p w_p^2`.

Then the proof of `VIS-179`, before the coarse substitutions `p<=y` and `D_2(y)<=y`, gives the sharper uniform bound

`| H^(-1) int_T^(T+H) S_y(t)^2 dt - 1/8 |`
` <= C [ L_y/(H Q_y) + D_2(y)/H ]`

for an absolute constant `C`, uniformly in the interval start `T`.

Consequently, if `H/y -> rho` with `0<rho<infinity`, the deterministic variance is Haar-matched whenever

`L_y/(y Q_y) -> 0`

and

`D_2(y)/y -> 0`.

For the natural full-prime power family

`P_y={p<=y}`, `w_p=p^(-alpha)`,

both conditions hold for every fixed

`alpha >= 1/2`.

In particular, at the critical exponent `alpha=1/2`,

`Q_y ~ log log y`,

`L_y = pi(y) ~ y/log y`,

`D_2(y) ~ 4y/[(log y)^2 log log y]`,

so for `H asymp y`

`| H^(-1) int_T^(T+H) S_y(t)^2 dt - 1/8 |`
` = O( 1/[log y log log y] )`

uniformly in `T`.

Thus the bounded-gap two-prime obstruction in `VIS-180` is a genuine obstruction to a **uniform arbitrary-subset theorem**, but it does not survive the diffuse full-prime `p^(-1/2)` coefficient profile at quadratic order. The critical-line prime amplitude already washes out that linear-support crowding channel in the normalized global variance.

**Evidence/status:** `CLASSICAL MEAN-VALUE THEOREM + CLASSICAL PRIME ASYMPTOTICS + EXACT WEIGHTED SPECIALIZATION + LINEAR-SUPPORT NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made that `alpha=1/2` is a source-sensitive RH mechanism, that the same conclusion holds for higher moments or full laws at linear support, or that variance separates for `alpha<1/2`.

## 1. Keep the weighted Montgomery–Vaughan error instead of replacing it by `y`

As in `VIS-179`, write

`A_y(t)=sum_(p in P_y) w_p p^(it)`

and

`S_y(t)=-(1/(2 sqrt(Q_y))) Re A_y(t)`.

Then

`S_y(t)^2=(1/(8Q_y))[ |A_y(t)|^2 + Re(A_y(t)^2) ]`.

The Montgomery–Vaughan mean-value theorem gives

`H^(-1) int_T^(T+H) |A_y(t)|^2 dt`
` = Q_y + O( L_y/H )`,

where

`L_y=sum_(p in P_y) p w_p^2`.

This is the exact coefficient-sensitive quantity hidden by the coarse estimate `L_y<=yQ_y` used in the headline statement of `VIS-179`.

For the nonconjugated square,

`A_y(t)^2=sum_(p,q in P_y) w_p w_q (pq)^(it)`.

Since `log(pq)>=log 4`, direct integration gives

`| H^(-1) int_T^(T+H) A_y(t)^2 dt |`
` <= C W_y^2/H`,

where `W_y=sum w_p`. Dividing by `Q_y` gives the second error `C D_2(y)/H`.

Combining the two estimates proves the displayed weighted variance bound. No new mean-value theorem is needed; the new information comes from refusing to erase the coefficient profile at the final step.

## 2. The full `p^(-1/2)` profile crosses the linear-support gate

Take all primes `p<=y` and `w_p=p^(-1/2)`. Then

`Q_y=sum_(p<=y) 1/p ~ log log y`

by Mertens' theorem for reciprocal primes, while

`L_y=sum_(p<=y) p * p^(-1)=pi(y) ~ y/log y`

by the prime number theorem.

`VIS-178` already records

`D_2(y) ~ 4y/[(log y)^2 log log y]`.

Therefore, when `H/y->rho in (0,infinity)`,

`L_y/(H Q_y) = O(1/[log y log log y])`

and

`D_2(y)/H = O(1/[(log y)^2 log log y])`.

Both vanish. Hence the deterministic continuous-window variance converges uniformly in `T` to the Haar value `1/8` even though the support has reached the linear scale `y asymp H` where the arbitrary-subset theorem of `VIS-179` is no longer uniformly small.

This is exactly the coefficient profile corresponding to the first prime term `p^(-s)` on `Re(s)=1/2`. That alignment is a representation-level fact, not evidence that the critical line has been explained: the proof uses only the coefficient decay, classical prime counting, and a classical Dirichlet-polynomial mean square.

## 3. Every fixed `alpha>1/2` is also linearly variance-matched

Let `w_p=p^(-alpha)` with fixed `alpha>1/2` and all primes `p<=y`.

Then

`Q_y=sum_(p<=y) p^(-2alpha) -> P(2alpha)>0`.

For `1/2<alpha<1`, partial summation and the prime number theorem give

`L_y=sum_(p<=y) p^(1-2alpha)`
` ~ y^(2-2alpha)/[(2-2alpha) log y]`,

while

`W_y=sum_(p<=y) p^(-alpha)`
` ~ y^(1-alpha)/[(1-alpha) log y]`.

Thus for `H asymp y`,

`L_y/(H Q_y) = O( y^(1-2alpha)/log y ) -> 0`

and

`D_2(y)/H = O( y^(1-2alpha)/(log y)^2 ) -> 0`.

At `alpha=1`, one has `L_y~log log y`, `W_y~log log y`, and both normalized errors still vanish after division by `H asymp y`. For `alpha>1`, the relevant weighted sums are bounded and the conclusion is immediate.

So the linear-support quadratic null extends through the entire `alpha>=1/2` full-prime family, even though `VIS-175` only gave a full weak-law transfer for `alpha>1/2` under a much slower sufficient cutoff gate.

## 4. What remains open below `alpha=1/2`

For fixed `0<=alpha<1/2`, the same prime asymptotics give

`Q_y ~ y^(1-2alpha)/[(1-2alpha) log y]`

and

`L_y ~ y^(2-2alpha)/[(2-2alpha) log y]`.

Hence

`L_y/(y Q_y) -> (1-2alpha)/(2-2alpha) > 0`.

The present weighted Montgomery–Vaughan criterion therefore stops proving variance matching at linear support below `alpha=1/2`.

This is only a **failure of the sufficient bound**. It does not prove that the full-prime variance has a non-Haar limit for `alpha<1/2`. Additional cancellation among off-diagonal prime pairs could still make the actual variance defect vanish. Conversely, `VIS-180` shows that one cannot recover a uniform theorem over arbitrary subsets merely from the support ratio.

The useful linear-support question is therefore narrower: for diffuse full-prime profiles below the critical exponent, determine the actual off-diagonal asymptotic or use a crowding-preserving matched control. A residual from an adversarial sparse subset is not enough.

## 5. Prior art and novelty boundary

The decisive mean-square input is the classical Montgomery–Vaughan Dirichlet-polynomial theorem already used in `VIS-179`; see H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`. R. C. Vaughan's **Mean Value Theorems in Prime Number Theory**, *Journal of the London Mathematical Society* (2) 10 (1975), 153–162, DOI `10.1112/jlms/s2-10.2.153`, is broader classical context for mean-value arguments over prime-supported Dirichlet polynomials.

The weighted-prime asymptotics are classical consequences of the prime number theorem by partial summation, and the endpoint `sum_(p<=y)1/p~log log y` is Mertens' reciprocal-prime theorem; these are already the prior-art inputs of `VIS-178`.

A targeted literature check found abundant classical mean-value theory for Dirichlet polynomials and prime-supported sums, but no need for a new theorem: the present result is a direct specialization of those standard estimates to the active normalized visual observable. No novelty is claimed for the analytic-number-theory ingredients or for weighted Dirichlet-polynomial mean squares.

## 6. Boundaries and falsification

The theorem concerns continuous averaging on an interval whose length is comparable to the prime cutoff. It does not apply automatically to Gram-point or another discrete sampling rule.

It controls only the global second moment. Higher moments, characteristic functions, shrinking events, extremes, unbounded functionals, and full weak-law transfer at `y asymp H` require separate estimates.

The `alpha>=1/2` conclusion uses the full prime support with the fixed deterministic profile `p^(-alpha)`. Sparse subsets, adaptive weights, and concentrated tapers can fail the leverage conditions even when their largest prime is the same.

The apparent threshold `alpha=1/2` is a threshold for this coefficient-sensitive quadratic control. It must not be promoted to a proof that the critical line is dynamically preferred or that RH follows from a variance principle.

Falsify the finding by finding an error in the uncoarsened Montgomery–Vaughan error `L_y/(H Q_y)`, the `A_y^2` bound `D_2/H`, or the weighted-prime asymptotics used to verify the two leverage conditions.

## Research consequence

The active prime-phase clue should no longer treat the `VIS-180` bounded-gap obstruction as a generic warning for every natural linear-support weight profile. For full prime-power weights with `alpha>=1/2`, the global quadratic variance is already representation-matched at `y asymp H`.

At the especially natural `p^(-1/2)` profile, close prime-log beats are diluted strongly enough that the normalized variance defect is `O(1/[log y log log y])`. A source-sensitive linear-support program must therefore use higher/growing complexity, stronger functionals, different sampling, hybrid/zero information, or genuinely more diffuse profiles below `alpha=1/2`; another global variance plot at critical-line weighting is a matched null, not evidence.