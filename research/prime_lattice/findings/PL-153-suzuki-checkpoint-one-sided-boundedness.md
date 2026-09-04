# PL-153 — One-sided prime-power checkpoint boundedness is equivalent to RH

## Claim

Let `Psi` be Suzuki's completed zeta screw potential and let

`2=q_1<q_2<...`

be the increasing sequence of prime powers. Set

`E_j := Psi(log q_j)`.

Then the Riemann hypothesis is equivalent to **either one-sided boundedness condition on the prime-power event values**:

`RH <=> sup_j E_j < +infinity`

and

`RH <=> inf_j E_j > -infinity`.

Consequently

`RH <=> sup_j |E_j| < infinity`,

while failure of RH forces

`limsup_(j->infinity) E_j = +infinity`

and

`liminf_(j->infinity) E_j = -infinity`.

The upper-bound equivalence needs only Suzuki's transform plus the strict convexity between consecutive prime-power events established in `PL-146`. The lower-bound equivalence additionally uses the fact that prime-power event intervals become sufficiently fine: Suzuki's curvature is `O(sqrt(q))`, while Baker--Harman--Pintz gives an ordinary-prime gap `O(q^0.525)`, so the maximal possible sag of `Psi` below the chord joining two consecutive prime-power endpoint values is `O(q^-0.45)`.

This is substantially weaker than either of Suzuki's published conditions `Psi(t)=O(1)` and `Psi(t)>=0`: **one finite upper ceiling alone, or one finite lower floor alone, already forces RH**, and after the prime-power reduction it is enough to impose that one-sided bound only on the axis-event sequence `log(p^k)`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + RH-EQUIVALENT-DISCRETE-CRITERION + STRUCTURAL-REDUCTION`. Suzuki's transform, growth estimate, boundedness criterion, and prime-power formula are peer-reviewed literature. The one-sign Laplace obstruction is the classical Landau principle already used in `PL-149`; the checkpoint convexity is reconstructed in `PL-146`; the required mesh estimate is the Baker--Harman--Pintz theorem already used in `PL-150`. The one-sided global criterion and its endpoint-only prime-power consequence are exact deductions from those inputs. A targeted literature audit, including Suzuki's paper and the August 2026 Mittermeier checkpoint series through its public Part 5 description, did not locate this exact one-sided endpoint-boundedness equivalence. **No novelty claim is made**: the argument is a line-level synthesis of classical/known ingredients.

## One-sided boundedness of the continuous screw potential already forces RH

Suzuki proves, initially for `Re(a)>1/2`,

`F(a) := integral_0^infinity Psi(t) exp(-a t) dt`

`      = (1/a^2) (xi'/xi)(1/2+a)`.

He also proves the unconditional growth estimate

`Psi(t) << exp(t/2-c sqrt(t))`

for some `c>0`, so the displayed Laplace integral is legitimate in that initial half-plane. Suzuki's Theorem 1.6 gives

`RH <=> Psi(t)=O(1)`.

The stronger one-sided statement follows by applying Landau's boundary-singularity theorem to a nonnegative tail.

Assume first that `Psi` is bounded below on a tail. Thus there are `T,C` such that

`Psi(t)>=-C`  for `t>=T`.

Define

`h_-(t)=(Psi(t)+C) 1_[T,infinity)(t)>=0`.

For `Re(a)>1/2`, its Laplace transform is

`H_-(a)`

`= (1/a^2)(xi'/xi)(1/2+a)`

`  - integral_0^T Psi(t) exp(-a t) dt`

`  + C exp(-a T)/a`.

The finite integral is entire and the last term is holomorphic away from `a=0`. The completed `xi` function has no zeros on the real interval `s>1/2`, so the displayed meromorphic continuation of `H_-` is analytic at every **positive real** `a`.

Let `sigma_c` be the abscissa of convergence of the nonnegative tail transform. The Landau theorem for nonnegative Laplace transforms says that if `sigma_c` is finite, the real point `a=sigma_c` is a singularity of the analytic function represented by the transform. Since the explicit continuation above has no singularity at any positive real `a`, one must have

`sigma_c<=0`

(or the transform converges still farther left). Hence the actual Laplace integral `H_-(a)` is holomorphic throughout `Re(a)>0`.

Now suppose there were a zeta zero `rho` with `Re(rho)>1/2`. Then

`a_rho=rho-1/2`

lies in `Re(a)>0`, and `(xi'/xi)(1/2+a)` has a genuine pole there. Neither the finite initial integral nor `C exp(-aT)/a` can cancel such a pole. But `H_-` is holomorphic in that half-plane, a contradiction. Therefore there is no zero with real part greater than `1/2`; the functional equation `xi(s)=xi(1-s)` then forces all nontrivial zeros onto the critical line.

Thus

`Psi bounded below => RH`.

The upper-bound case is identical. If `Psi(t)<=C` for `t>=T`, use

`h_+(t)=(C-Psi(t))1_[T,infinity)(t)>=0`.

Its Laplace transform differs from

`-(1/a^2)(xi'/xi)(1/2+a)`

only by an entire finite-interval term and `C exp(-aT)/a`. The same Landau argument excludes every pole with `Re(a)>0`, hence every zeta zero with `Re(rho)>1/2`, and therefore gives RH.

Combining with Suzuki's unconditional implication `RH => Psi=O(1)` yields the exact continuous equivalences

`RH <=> Psi is bounded above on [0,infinity)`

`   <=> Psi is bounded below on [0,infinity)`.

Equivalently, if RH is false, `Psi` must escape arbitrarily far in **both** signs. This conclusion is stronger than merely negating Suzuki's two-sided boundedness theorem.

## Why the Landau step is legitimate

The argument does not assume an Euler product in the critical strip. The identity for `F(a)` is first established in Suzuki's valid transform half-plane `Re(a)>1/2`. The right-hand side then supplies the meromorphic continuation through the completed function `xi'/xi`.

The only Tauberian input is the standard positive-transform boundary principle already used in `PL-149`. For completeness, its mechanism is elementary. If a nonnegative locally integrable `h` has finite Laplace abscissa `sigma_c` and its transform were analytic through the real point `sigma_c`, the Taylor expansion there, together with positivity of the moments

`integral_0^infinity t^n h(t) exp(-sigma t) dt`,

would extend convergence to a real point left of `sigma_c`, contradicting the definition of the abscissa. Positivity is therefore what converts analytic continuation into a one-sided sign obstruction.

The role of the completed zeta object is equally precise: `xi'/xi(1/2+a)` is regular on the positive real `a`-axis but has a pole at `a=rho-1/2` for every zero `rho`. A one-sided bound on `Psi` creates a nonnegative transform whose convergence boundary cannot stop at a positive real number; that forces its genuine domain of holomorphy across the whole right half-plane and thereby excludes every off-line zero on the right.

## Upper event values control the whole function by convexity

Now use the exact prime-power event geometry of `PL-146`. On every interval

`I_j=[lambda_j,lambda_(j+1)]`,  `lambda_j=log q_j`,

Suzuki's formula has the form

`Psi(t)=R(t)-P_j t+Q_j`,

where the arithmetic state `(P_j,Q_j)` is constant in the value formula and

`Psi''(t)=R''(t)>0`

throughout the open interval. The newly activated von-Mangoldt ramp has value zero at an event, so `Psi` is continuous at both endpoints.

A convex function on a closed interval cannot exceed both endpoint values. Hence

`sup_(t in I_j) Psi(t) = max(E_j,E_(j+1))`.

Therefore, apart from the finite initial interval before `log 2`,

`sup_(t>=log 2) Psi(t) = sup_j E_j`.

This immediately gives

`sup_j E_j < infinity`

`=> Psi is bounded above`

`=> RH`.

The converse is Suzuki's theorem under RH. Thus

`boxed: RH <=> sup_(q=p^k) Psi(log q) < infinity.`

No prime-gap theorem is needed for this direction. The prime-power axis events alone capture every possible large positive excursion because the completed potential is convex between them.

## Lower event values control the whole function after a vanishing sag estimate

Convexity works in the opposite direction for minima: the interior may lie below both endpoints. However, the amount by which it can do so is controlled by curvature and interval length.

Let `[a,b]=[log q,log r]` be an interval between consecutive prime powers and let

`M_q=sup_[a,b] R''`.

For any twice differentiable function with `f''<=M_q`, the semiconvex chord inequality gives

`f(t) >= ((b-t)/(b-a)) f(a) + ((t-a)/(b-a)) f(b)`

`         - (M_q/2)(t-a)(b-t)`.

Applying this to `Psi` on the event interval and using

`(t-a)(b-t) <= (b-a)^2/4`

yields

`Psi(t) >= min(Psi(a),Psi(b)) - M_q(b-a)^2/8`.

The curvature estimate from `PL-146`/`PL-150` is

`R''(log x) = (x^3-x-1)/(sqrt(x)(x^2-1))`

and, for `x>=2`,

`0<R''(log x) <= (4/3)sqrt(x)`.

Thus

`M_q <= (4/3)sqrt(r)`.

Baker--Harman--Pintz prove that `[x,x+x^0.525]` contains a prime for all sufficiently large `x`. Since an ordinary prime is itself a prime-power event, the next prime-power `r` after any sufficiently large prime power `q` satisfies

`r-q << q^0.525`.

Consequently

`b-a = log(r/q) << q^-0.475`

and `sqrt(r) asymp sqrt(q)`. Hence, uniformly over **every** sufficiently large prime-power interval,

`M_q(b-a)^2 << q^(1/2) q^-0.95 = q^-0.45`.

Therefore

`min_(t in [log q,log r]) Psi(t)`

`>= min(Psi(log q),Psi(log r)) - O(q^-0.45)`.

This extends the recovery-specific terminal drawdown estimate of `PL-150` to a simpler all-interval endpoint-to-interior statement. If the checkpoint event values have a uniform lower floor

`E_j>=-C`,

then the whole continuous tail satisfies

`Psi(t)>=-C-o(1)`.

After absorbing finitely many initial intervals, `Psi` is globally bounded below. The one-sided Landau criterion proved above then gives RH. Conversely, RH gives `Psi(t)>=0` by Suzuki's Theorem 1.7, so every event value is nonnegative.

Hence

`boxed: RH <=> inf_(q=p^k) Psi(log q) > -infinity.`

The numerical exponent `0.525` is not important. If one only knows a prime-event mesh

`r-q << q^theta`,

then the same estimate gives an interior sag

`O(q^(2 theta-3/2))`.

Any unconditional `theta<3/4` is sufficient for the qualitative lower-bound transfer.

## Prime-exponent interpretation

Each sampled point is an axis vector

`v(q)=k e_p`,  `q=p^k`,

with energy

`log q=<k e_p,(log ell)_ell>`.

The criterion can therefore be stated entirely on the ordered energy projection of the prime-power rays:

`RH <=> the completed screw values on {k log p} have a finite upper ceiling`

and independently

`RH <=> the completed screw values on {k log p} have a finite lower floor`.

This is not a full-lattice mechanism: mixed-support exponent vectors still do not enter Suzuki's von-Mangoldt forcing. What is nontrivial is that the axis skeleton is sufficient even for the much weaker **one-sided boundedness** test. The completed archimedean curvature and the arithmetic event mesh ensure that no hidden between-event excursion can evade the sampled criterion.

The upper and lower directions expose two different geometric facts. Positive excursions are captured exactly by interval convexity. Negative excursions require quantitative control of the energy mesh relative to the growing archimedean curvature. Thus the lower criterion is the one in which prime distribution enters beyond the support statement `Lambda(p^k)!=0`.

## Prior art and novelty audit

Primary theorem-level inputs:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448--1487, DOI `10.1112/jlms.12785`. Theorem 1.1 gives the one-sided transform and growth estimate; Theorem 1.6 gives `RH <=> Psi=O(1)`; Theorem 1.7 gives `RH <=> Psi>=0`; equation (1.1) supplies the von-Mangoldt prime-power forcing used in `PL-146`.
- **Masatoshi Suzuki**, “On variants of Chebyshev's conjecture,” *The Ramanujan Journal* **68** (2025), article 95, DOI `10.1007/s11139-025-01238-9`, arXiv `2411.07436`. Proposition 1 records the Landau-type Mellin/Laplace boundary theorem used in sign arguments and already audited in `PL-149`.
- **R. C. Baker, G. Harman, J. Pintz**, “The Difference Between Consecutive Primes, II,” *Proceedings of the London Mathematical Society* **83**(3) (2001), 532--562, DOI `10.1112/plms/83.3.532`. Gives a prime in `[x,x+x^0.525]` for large `x`, the mesh input already used in `PL-150`.

Direct current novelty controls:

- **Rainer Andreas Mittermeier**, “Prime-Power Checkpoints for Suzuki's Riemann Zeta Screw Function: Rigorous Positivity Certificate through `q=10^10` and an Explicit Chebyshev-Memory Barrier,” Zenodo, August 2026. Its public description uses exact interval convexity/checkpoint minima and the same prime-power event sequence.
- **Rainer Andreas Mittermeier**, “Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail — Part 4,” Zenodo, 26 August 2026, DOI `10.5281/zenodo.22076079`.
- **Rainer Andreas Mittermeier**, “Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence — Part 5,” Zenodo, 26 August 2026, DOI `10.5281/zenodo.22076088`. Its public description uses a Pringsheim--Landau argument to rule out an eventually active **workload** and is direct prior art for the Landau/recovery organization reconstructed in `PL-149`.

A targeted audit searched combinations of Suzuki's `Psi`, `bounded above`, `bounded below`, `one-sided boundedness`, `prime-power checkpoint`, `endpoint values`, and the current Mittermeier series. Suzuki explicitly states only the two-sided boundedness theorem in the 2023 paper; the public checkpoint descriptions found in the audit focus on positivity, recovery, workload sign, and finite certification. No exact statement matching

`RH <=> one-sided boundedness of {Psi(log p^k)}`

was located. This absence is **not** treated as proof of novelty. The present result is stored as an exact derived synthesis because it materially weakens the checkpoint obligation and is reusable in subsequent analysis.

## Adversarial boundaries

1. **This is another RH-equivalent criterion, not progress toward proving the required bound.** The result lowers the target from positivity of every checkpoint minimum to preventing one-sided escape of the event values. It does not supply that prevention.

2. **The global one-sided theorem is largely continuation-generic.** Any real function with a nonnegative-tail transform to which the same Landau argument applies, and whose meromorphic continuation has no positive-real boundary singularity but does have right-half-plane poles exactly when a target zero leaves its symmetry line, will exhibit an analogous one-sided criterion. The zeta-specific arithmetic content enters mainly in the discrete prime-power sampling theorem.

3. **The upper endpoint criterion does not use prime density.** It follows purely from the convexity of each arithmetic interval. Therefore it should not be misread as evidence that detailed prime-gap statistics explain RH.

4. **The lower endpoint criterion does use an unconditional prime-gap input, but only weakly.** Any exponent below `3/4` would suffice. The strong `0.525` theorem is convenient rather than critical.

5. **Convexity is only interval-local.** The derivative of `Psi` jumps downward at every prime-power event. There is no claim that `Psi` is globally convex.

6. **No pole cancellation is available in the Landau argument.** The finite initial-interval transform is entire and the constant-tail term has only a possible pole at `a=0`; neither can cancel a shifted-zero pole with `Re(a)>0`.

7. **The critical half-weight remains imported from completion.** The event amplitudes are `Lambda(q)/sqrt(q)`. This finding does not derive `1/2` from the abstract exponent cone; it exploits the already-completed Suzuki object.

8. **Mixed exponent vectors remain invisible.** The sampled set consists only of `k e_p`. A future full-lattice proposal must still show how mixed-support geometry constrains these completed axis-event values rather than merely re-encoding them.

A falsification of the displayed equivalence would require failure of Suzuki's transform/growth formula, failure of the Landau boundary theorem for nonnegative Laplace transforms, an error in the strict-convex interval decomposition, or prime-power gaps large enough that `sqrt(q)(Delta log q)^2` is unbounded despite the Baker--Harman--Pintz prime theorem. The cited inputs exclude those possibilities.

## Consequence for the research line

The Suzuki checkpoint frontier can now be weakened sharply. It is unnecessary, at the level of an equivalent criterion, to prove a positive reserve at every local minimum or even to prove that event values remain nonnegative. It would already suffice to establish **either**

`Psi(log p^k) <= C  for all prime powers p^k`

for some finite `C`, or

`Psi(log p^k) >= -C  for all prime powers p^k`

for some finite `C`.

Conversely, any counterexample to RH would have to force the completed prime-power event sequence to make arbitrarily large excursions in **both** directions. This gives a precise falsifiable tail target for subsequent work on the axis-event dynamics: the question is no longer only whether recovered minima cross zero, but whether exact rational-prime structure can prevent even one side of event-level escape. The criterion is weaker, but the Landau audit also warns that its continuous part is generic; any genuinely new mechanism must explain the arithmetic event bound itself rather than merely rederive the analytic continuation implication.