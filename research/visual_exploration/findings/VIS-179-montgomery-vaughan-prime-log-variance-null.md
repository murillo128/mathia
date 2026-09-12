# VIS-179 — Montgomery–Vaughan mean square pushes the prime-log variance null to near-linear support

## Claim

Keep the notation of `VIS-177`. Let `P_y` be any finite set of primes `p<=y`, let `w_p>0`, and write

`W_y=sum_(p in P_y) w_p`,

`Q_y=sum_(p in P_y) w_p^2`,

`D_2(y)=W_y^2/Q_y`,

and

`S_y(t)=Q_y^(-1/2) sum_(p in P_y) w_p [sin^2(t log p/2)-1/2]`.

Then, uniformly in the interval start `T`,

`| H^(-1) int_T^(T+H) S_y(t)^2 dt - 1/8 | <= C y/H`

for an absolute constant `C` and every `H>0` (with the bound understood as useful when `y/H` is small).

The constant `1/8` is exactly the second moment of the matched Haar prime-phase field. Therefore every support law

`y(H)=o(H)`

has deterministic continuous-window variance converging to the Haar variance, uniformly in `T`, for **arbitrary positive prime weights and arbitrary prime subsets inside `[2,y]`**.

In particular, for every fixed `0<delta<1`, the polynomial support law `y=H^delta` is already variance-matched. For the prime-power family of `VIS-178`, this strictly improves the `k=2` consequence of the generic character-by-character bound, which only supplied the sufficient wedge `delta<=1/2`.

**Evidence/status:** `CLASSICAL MEAN-VALUE THEOREM + EXACT REDUCTION + STRICTLY STRONGER QUADRATIC NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No claim is made about higher moments, a Gaussian/full weak law at polynomial support, characteristic-function discrepancy, discrete/Gram sampling, rare events, hybrid prime/zero observables, sharpness at `y asymp H`, or RH.

## 1. Rewrite the visual observable as a Dirichlet polynomial

Since

`sin^2(t log p/2)-1/2=-(1/2) cos(t log p)`, 

define the finite Dirichlet polynomial

`A_y(t)=sum_(p in P_y) w_p p^(it)`.

Then

`S_y(t)=-(1/(2 sqrt(Q_y))) Re A_y(t)`

and hence

`S_y(t)^2=(1/(8Q_y)) [ |A_y(t)|^2 + Re(A_y(t)^2) ]`.

Under independent Haar prime phases, the cross terms vanish and

`E[(S_y^Haar)^2]=1/8`.

Thus the deterministic/Haar variance gap splits into the ordinary mean square of a Dirichlet polynomial plus the nonconjugated square term.

## 2. Montgomery–Vaughan controls the conjugated mean square at scale `y/H`

The classical Montgomery–Vaughan mean-value theorem for Dirichlet polynomials gives, for coefficients supported on integers `n<=y`,

`int_T^(T+H) |sum_(n<=y) a_n n^(it)|^2 dt`
` = H sum_(n<=y) |a_n|^2 + O(sum_(n<=y) n |a_n|^2)`.

The usual statement over `[0,H]` applies uniformly to a translated interval because translation only replaces `a_n` by `a_n n^(iT)`, preserving coefficient magnitudes.

Apply it with `a_p=w_p` on `P_y` and zero otherwise. Since every `p<=y`,

`H^(-1) int_T^(T+H) |A_y(t)|^2 dt`
` = Q_y + O(y Q_y/H)`.

This is the step missed by the absolute character-by-character estimate of `VIS-177`: the whole quadratic off-diagonal family is controlled collectively by the classical Hilbert-inequality mean-value mechanism rather than by paying the worst individual prime-log spacing for every pair.

## 3. The nonconjugated square is no larger

Expand

`A_y(t)^2=sum_(p,q in P_y) w_p w_q (pq)^(it)`.

Every frequency is positive and satisfies

`log(pq)>=log 4`.

For any nonzero real `lambda`,

`| H^(-1) int_T^(T+H) exp(i lambda t) dt | <= 2/(H|lambda|)`.

Therefore

`| H^(-1) int_T^(T+H) A_y(t)^2 dt |`
` <= [2/(H log 4)] W_y^2`
` = O(Q_y D_2(y)/H)`.

By Cauchy–Schwarz,

`D_2(y)<=|P_y|<=y`,

so after division by `8Q_y` this term is also `O(y/H)`.

Combining the two pieces proves

`H^(-1) int_T^(T+H) S_y(t)^2 dt = 1/8 + O(y/H)`.

No prime-number theorem or weight asymptotic is needed.

## 4. Consequence for polynomial support

If

`y=H^delta`, `0<delta<1`,

then

`y/H=H^(delta-1)->0`.

Thus the quadratic statistic remains representation-matched throughout every strictly sublinear polynomial support scale.

This is substantially stronger than inserting `k=2` into `VIS-177` or `VIS-178`. Their generic fixed-character estimate gives

`|time_2-Haar_2| <= y D_2(y)/H`,

which for prime-power weights leads only to a sufficient exponent near `y^2/H` up to logarithms. Montgomery–Vaughan captures cancellation among the complete quadratic off-diagonal family and replaces that bound by `O(y/H)` independently of `D_2`.

The improvement is deliberately only quadratic. It does not propagate automatically to `k>=3`, because the corresponding products are no longer a single ordinary Dirichlet-polynomial mean square with the same one-line reduction.

## 5. Prior art and novelty boundary

The decisive input is classical. H. L. Montgomery and R. C. Vaughan, **Hilbert's Inequality**, *Journal of the London Mathematical Society* (2) 8 (1974), 73–82, DOI `10.1112/jlms/s2-8.1.73`, develops the Hilbert-inequality machinery underlying the standard mean-value theorem for Dirichlet polynomials. Modern statements record the consequence in the form

`int_0^H |sum_(n<=N) a_n n^(it)|^2 dt = sum_(n<=N) |a_n|^2 [H+O(n)]`.

No novelty is claimed for this theorem, the Hilbert inequality, or its usual Dirichlet-polynomial applications. The Mathia-specific contribution is only to recognize that the active prime-phase visual observable's second moment is exactly in this classical mean-square class and therefore has a much larger matched-control regime than the generic character bound in `VIS-177`/`VIS-178` suggested.

This prior-art collision is itself the useful result: a visually attractive variance/energy separation cannot be interpreted as source-sensitive merely because it lies beyond the earlier `delta<=1/2` moment wedge.

## 6. Boundaries and falsification

The estimate concerns continuous averaging on one interval of length `H`. It does not transfer to Gram points or another sparse deterministic sampling rule without a separate sampling theorem.

The support is bounded by the largest integer frequency index `y`; the result does not claim optimal dependence on the actual prime subset, coefficient profile, or a shorter effective length. The coarse inequality `sum p w_p^2<=yQ_y` is enough for the present null.

At `y asymp H`, the theorem gives only an `O(1)` error and does not prove convergence to `1/8`. Failure of the bound to vanish there is not evidence that the deterministic variance actually separates.

The result controls only the second moment. Higher fixed moments remain governed by `VIS-177`/`VIS-178` unless a stronger mean-value theorem is brought to bear, and a second-moment match alone says nothing about full-law convergence, rare events, moving thresholds, or unbounded functionals.

Falsify the finding by finding an error in the identity expressing `S_y^2` through `|A_y|^2` and `Re A_y^2`, an inapplicability of the Montgomery–Vaughan mean-value theorem to the translated finite polynomial, or an error in the `A_y^2` frequency bound.

## Research consequence

The accepted prime-phase recursive-geometry clue should treat **every global quadratic energy/variance statistic of this additive prime-log field as a matched source null throughout `y=o(H)`**, not merely inside the `VIS-178` `k=2` wedge.

Consequently, moving to a support `H^delta` with `1/2<delta<1` does not by itself create a new quadratic opportunity. A surviving continuous prime-phase statistic in that range must use genuinely higher or growing complexity, a stronger functional class, a different sampling mechanism, or source-bearing information outside the same additive prime-torus representation.