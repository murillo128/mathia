# AF-580 — Positive noise destroys finite stopping under unknown polynomial calibration

## Claim and evidence boundary

EXACT-DERIVED · LITERATURE+DERIVED · NEGATIVE/OBSTRUCTION · SHARP-MINIMAX · NO-GENERAL-NOVELTY-CLAIM

Under polynomial output calibration of unknown, unrestricted finite degree, **every fixed positive allowance for bounded observation error destroys the noiseless continuous-random stopping advantage**. This holds on the whole positive ray, even when the source classes retain a strictly positive full-curve separation margin. Arbitrarily large finite query coordinates, continuous randomness, and unbounded input-dependent query counts do not repair the obstruction.

More precisely, worst-case error is at least `1-1/m` times the probability of a finite label return on **each input whose error has strict slack below the permitted noise bound**, including every noiseless input. The same inequality holds at every continuous-error input even without strict slack. Thus a policy returning almost surely on every input has exact minimax error `1-1/m`. At zero worst-case error, it cannot return with positive probability on even one noiseless input. This is stronger than the finite-cap and worst-case stopping-tail bounds in [[research/arithmetic_fidelity/findings/AF-579-unbounded-query-locations-preserve-polynomial-budget-obstruction|AF-579]]. It does not assert the same pointwise return bound at arbitrary discontinuous, noise-saturated inputs.

The proof uses classical polynomial approximation and a seed-independent coupling of entire compact-window transcripts. The prime-edit application remains a generalized-prime matched-control result, not an ordinary-prime discriminator or an RH conclusion.

## Experiment and sharp theorem

Let `F_1,...,F_m`, `m>=2`, be known continuous real functions on `D=(0,infinity)`. Let `Pi` be the set of all real polynomials of finite degree, without a supplied degree or coefficient bound. Fix `epsilon>0`. An input is
\[
 x=(i,b,\eta),\qquad y_x=F_i+b+\eta,\qquad
 b\in\Pi,\quad \eta:D\to\mathbb R\text{ Borel measurable},\quad
 \|\eta\|_\infty\le\varepsilon.
 \tag{1}
\]
The norm is the pointwise supremum, not an essential supremum. The polynomial and error function are fixed before the policy's independent random seed and shared by all observations. Repeated queries therefore return the same value. This already lies inside the usual arbitrary bounded-error model; a seed-adaptive error adversary is unnecessary.

A measurable policy may choose any finite positive real coordinate from its seed and the previous value history. The seed may have any distribution, including an ideal continuous one. It may return one label after finitely many queries or never return; abstention counts as nonreturn. Only value queries are supplied, with exact real operations otherwise allowed. Write `T<infinity` for finite label return and
\[
 e_\varepsilon(\mathcal A)
   =\sup_{x\text{ satisfying (1)}}
       \Pr_x(T<\infty,\widehat i\ne i),\qquad c_m=1-1/m.
 \tag{2}
\]
No fixed cap, moment bound, or finite-bit assumption is imposed. For every admitted `x_0` with `||eta_0||_infinity<epsilon`, or with `eta_0` continuous on `D`,
\[
 \boxed{e_\varepsilon(\mathcal A)\ge
        c_m\Pr_{x_0}(T<\infty).}
 \tag{3}
\]
Consequently
\[
 \boxed{\inf_{\mathcal A:\,\Pr_x(T<\infty)=1\ \forall x}
                 e_\varepsilon(\mathcal A)=c_m.}
 \tag{4}
\]
In fact, almost-sure return on just one strict-slack input suffices for the lower bound in (4), if error is still controlled over the full class (1). The coefficient in (3) is sharp: return a uniform label with probability `gamma` and otherwise do not return. Then every input has return probability `gamma` and error `c_m gamma`. Uniform guessing gives the upper bound in (4).

Continuity of the sources is enough for this negative theorem. Analyticity, nonpolynomial source gaps, bounded gaps, and endpoint derivative estimates enter only when contrasting it with noiseless success or positive full-curve margin.

## Exact compact-window matching

Fix `x_0=(i_0,b_0,eta_0)` with strict slack
\[
 \delta=\varepsilon-\|\eta_0\|_\infty>0.
\]
For each integer `R>=2`, put
\[
 K_R=[1/R,R],\qquad J_R=[1/(2R),R+1].
\]
Choose a smooth function `chi_R`, valued in `[0,1]`, equal to one on `K_R` and with compact support inside the interior of `J_R`. For every label `j`, [[research/prior_art/incremental/PA-weierstrass-polynomial-approximation|polynomial approximation]] on the compact interval `J_R` supplies `p_(j,R) in Pi` such that
\[
 g_j=F_{i_0}-F_j,\qquad
 \sup_{J_R}|g_j-p_{j,R}|<\delta/2.
 \tag{5}
\]
Define one competing input per label by
\[
 b_{j,R}=b_0+p_{j,R},\qquad
 \eta_{j,R}=\eta_0+\chi_R(g_j-p_{j,R}).
 \tag{6}
\]
These are globally admissible fixed inputs:
\[
 \|\eta_{j,R}\|_\infty
 \le\|\eta_0\|_\infty+\delta/2<\varepsilon,
 \qquad F_j+b_{j,R}+\eta_{j,R}=y_{x_0}\quad\text{on }K_R.
 \tag{7}
\]
For `j=i_0`, one may simply take `p_(j,R)=0`, recovering `x_0`. No single polynomial is required to approximate a gap on the entire ray: the polynomial degree and coefficients may grow with `R`, and outside `J_R` the compensating error is exactly `eta_0`.

If all sources and `eta_0` are smooth, every competing error in (6) is smooth. In particular, against a noiseless reference, all competing errors can be chosen smooth and compactly supported. Thus even restricting the error class to `C_c^infinity(D)` with the same supremum bound leaves the almost-sure-return minimax value (4) unchanged for smooth sources. No common derivative or support bound is supplied in that restricted class.

**Continuous reference errors do not need slack.** If `eta_0` is continuous, approximate `g_j+eta_0` on `J_R` by a polynomial `p_(j,R)` to error less than `epsilon/2`, and instead set
\[
 b_{j,R}=b_0+p_{j,R},\qquad
 \eta_{j,R}=\chi_R(g_j+\eta_0-p_{j,R}).
 \tag{7a}
\]
The new error has norm below `epsilon/2` and the observation again equals `y_(x_0)` on `K_R`, regardless of whether `||eta_0||_infinity=epsilon`. It is continuous and compactly supported; it is smooth when the sources and `eta_0` are smooth. Therefore (3) holds on every input in the continuous-error or smooth-error experiment, including its noise-saturated boundary. For arbitrary discontinuous errors, (6)'s strict-slack argument remains the asserted pointwise guarantee.

## Exhaust returning executions, not a fixed query budget

Run the policy on `x_0`. Define
\[
 E_R=\{T<\infty\text{ and every queried coordinate belongs to }K_R\},
 \quad q_R=\Pr_{x_0}(E_R),
 \quad q_{j,R}=\Pr_{x_0}(E_R,\widehat i=j).
 \tag{8}
\]
The zero-query case is included. Each returning execution has a finite list of finite positive coordinates, hence lies in some `E_R`. Therefore
\[
 E_R\uparrow\{T<\infty\},\qquad
 q_R\uparrow\Pr_{x_0}(T<\infty).
 \tag{9}
\]
This assertion needs neither a uniform bound on query count nor tightness of the maximum query coordinate over nonreturning executions.

Couple the runs on `x_0` and the `m` inputs (6), or (7a) for the continuous-error case, by the same seed. On `E_R`, induction through the complete finite execution shows that every query, response, stopping decision, and returned label agrees because the observations agree on `K_R`. Thus the input with true label `j` has error at least `q_R-q_(j,R)`. Since the output labels partition `E_R`,
\[
 e_\varepsilon(\mathcal A)
 \ge\max_{1\le j\le m}(q_R-q_{j,R})
 \ge\frac1m\sum_{j=1}^m(q_R-q_{j,R})
 =c_mq_R.
 \tag{10}
\]
Let `R` increase to prove (3). For each `R`, all `m` adversarial inputs are fixed independently of the realized seed. They may change with `R` because the left side is a supremum over inputs. No seed-dependent interpolation, minimax interchange, or continuity of the policy in its observed values is used. Equality on an entire window is what permits arbitrary continuously distributed coordinates.

The abstract sufficient condition is exact local matching of a reference input in every label class on an exhausting sequence of windows. Polynomial density together with bounded-error slack, or continuity of the reference error, establishes that condition here. This is different from equality on a finite list of points, which alone did not defeat the noiseless continuous-random procedure in [[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]].

## Positive full-ray margin still survives for prime-edit controls

For a known finite set `S={p_1<...<p_m}` of distinct odd rational-prime edit locations, use
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
 \tag{11}
\]
AF-577/579 establish that these curves are analytic on the ray and that each ordered gap `Phi_q-Phi_p`, `p<q`, is positive, bounded, and tends to zero at both ends. In particular, let
\[
 d(S)=\min_{i<m}\sup_{a>0}(\Phi_{p_{i+1}}-\Phi_{p_i})(a)>0.
 \tag{12}
\]
The full-curve margin can be checked without the stopping argument. For bounded `g`, every nonconstant polynomial has infinite uniform error against `g` on the ray, whereas
\[
 \inf_{c\in\mathbb R}\|g-c\|_\infty
   =\tfrac12(\sup g-\inf g).
 \tag{13}
\]
Thus the minimum distance between distinct polynomial-calibrated prime-edit classes is `d(S)/2`: nonadjacent positive gaps are sums of adjacent gaps and cannot lower the minimum. Uniform-error balls are disjoint for `2 epsilon<d(S)/2`. At `epsilon=d(S)/4`, the midpoint of a closest, constant-shifted pair gives an alias, as in AF-579.

Consequently, for **every**
\[
                    0<\varepsilon<d(S)/4,
 \tag{14}
\]
the entire observed curve determines its unique source label, but every policy returning almost surely from finite point observations has worst-case error at least `c_m`; uniform guessing attains the bound. The smooth compactly supported errors constructed above already prove that lower bound. The full-curve alias at the endpoint need not have compact support; only the strict separation below the endpoint is needed for this contrast.

At `epsilon=0`, AF-577's independent continuous validation point instead identifies each fixed input almost surely within its actual calibration degree plus two queries. The discontinuity at zero is in the uniform recovery requirement over unknown degree and bounded errors. It is not an arithmetic phase transition. More queries can reveal any fixed compact-window witness eventually, but there is no uniformly reliable finite return rule over all such witnesses.

## Explicit control and validation

Take `F_j(a)=j g(a)`, `j=0,...,m-1`, with
\[
 g(a)=\frac{a}{(1+a)^2}.
\]
The gap is positive, tends to zero at both ends, and has maximum `1/4` at `a=1`, since `(1+a)^2-4a=(a-1)^2`. The nearest source-class distance is `1/8` and the full-curve noise radius is `1/16`, independently of the finite number of consecutive labels. For every `0<epsilon<1/16`, (3)--(4) nevertheless apply. This verifies that the mechanism is not prime-specific.

There is an explicit approximation certificate. For `B>0`, `0<=a<=B`, put `u=(B-a)/(1+B)` and
\[
 p_n(a)=\frac{a}{(1+B)^2}\sum_{k=0}^n(k+1)u^k.
\]
The finite differentiated geometric sum gives
\[
 g(a)-p_n(a)
   =g(a)u^{n+1}\{(n+2)-(n+1)u\},\qquad
 0\le g-p_n\le\frac{n+2}{4}
                    \left(\frac B{1+B}\right)^{n+1}\longrightarrow0.
 \tag{15}
\]
For the reference `y=b_0`, alternative label `j` uses `b_j=b_0-j p_n` and `eta_j=j(p_n-g)chi`. Choosing the bound in (15) below `epsilon/(m-1)` supplies (7) on any prescribed window.

A scratch-only `fractions.Fraction` check verified (15) and its bound at 1,428 rational cases: `B in {1/4,1,3,10}`, `n=0,...,16`, and `a=B k/20`, `k=0,...,20`. A second exact check used three labels, `epsilon=1/100`, `b_0(a)=a^2-a/7`, and windows `[0,R]` for `R=1,3,10`. Approximating on `[0,R+1]` gave polynomial degrees `17,34,98`. With a piecewise-linear cutoff equal to one on `[0,R]` and zero beyond `R+1`, all sampled errors satisfied the bound. For rational seed samples `U=k/100`, the adaptive coordinates
\[
 a_1=U/(1-U),\qquad a_2=a_1\{1+y(a_1)^2\}
\]
and output `1_(y(a_2)>0)+1_(a_1>1)` agreed exactly across all three matched inputs whenever both coordinates were in the window: 477 reconstructed executions. At each matched seed, the three error indicators summed to two. These checks validate the concrete algebra, noise sign, and adaptive coupling; they do not simulate the arbitrary-seed or exhaustion theorem. The smooth-cutoff strengthening follows from (5)--(7), not from the piecewise-linear test.

## Prior art, mathematical delta, and limits

[Trefethen, *Approximation Theory and Approximation Practice*, extended edition (2019), Chapter 6](https://epubs.siam.org/doi/10.1137/1.9781611975949.ch6), supplies the classical polynomial-density theorem. Its use here is local to a compact interval, not uniform approximation on a ray.

[Kunsch, Novak and Rudolf (2019), *Solvable integration problems and optimal sample size selection*, §3.4, Theorem 3.15](https://arxiv.org/abs/1805.08637), already rule out randomized almost-surely finite integration on unrestricted smooth classes using hidden smooth perturbations and transcript comparisons. The general unsolvability mechanism is established prior art. Here it is realized inside a **fixed finite list of source curves plus polynomial calibration and arbitrarily small bounded errors**, where full-curve label classes can remain positively separated.

[Bertanha and Moreira, *Impossible Inference in Econometrics: Theory and Applications*, arXiv:1612.02024v5, §2, Corollary 1](https://arxiv.org/abs/1612.02024), identifies total-variation closure as a classical obstruction to nontrivial testing. This is relevant background for comparing observational closure with global identification, not a theorem automatically covering adaptive value queries. The exact coupling (7)--(10) proves the needed statement here without imposing continuity on the policy. No general approximation, testing, or sequential-impossibility novelty is claimed.

The local delta is the positive-noise, **variable-stopping** boundary left open by AF-579: the earlier noiseless continuous-random repair fails at every fixed positive error allowance, even strictly below the full-ray identification radius. The sharp error/return inequality localizes that failure to every strict-slack input and every continuous-error input, not merely a sequence of hard bounded-budget inputs.

Load-bearing boundaries are:

- Error is an arbitrary fixed bounded function, not known independent, centered, or resampled measurement noise. Repeated readings need not average it away.
- Smoothness alone does not help, but no analytic-error result is asserted. A nonzero analytic correction cannot have compact support, and exact agreement of analytic observations on an interval has different consequences.
- No degree/coefficient bound, common derivative bound on errors, or common support window is supplied. Such restrictions can invalidate (5)--(7) and require a separate recovery analysis.
- Queries at infinity, integrals of the unknown curve, symbolic calibration access, and an oracle able to reduce its error allowance on demand are outside (1).
- The pointwise return bound uses either strict slack or continuity of the reference error. No claim is made for arbitrary discontinuous errors saturating the bound.
- The error bound is unconditional over wrong finite returns; nonreturn is not an error. No contradiction follows from a procedure that never returns.

For the line's recovery problem, a positive full-curve metric margin is therefore insufficient even for input-dependent finite certification. A useful calibration promise must also prevent these exact compact-window matches or provide additional nonlocal information. This result supplies no such arithmetic promise.
