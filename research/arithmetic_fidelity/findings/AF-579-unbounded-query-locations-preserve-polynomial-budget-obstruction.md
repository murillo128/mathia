# AF-579 — Unbounded query locations preserve the polynomial-budget obstruction while restoring full-curve margin

## Claim and evidence boundary

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · SHARP-MINIMAX · OBSERVATION-DOMAIN-BOUNDARY · NO-GENERAL-NOVELTY-CLAIM

Consider the registered prime-edit curves of AF-577/578, now observed on **all** `a>0`, with one shared polynomial output calibration of unknown finite degree and unrestricted coefficients. Enlarging the observation window has two different consequences:

- The full-curve deterministic-noise identification radius becomes strictly positive, equal to the constant-offset radius `d(S)/4` for every fixed finite candidate set `S`.
- Every finite query cap still has blind-guess minimax error `1-1/|S|`, even with adaptive coordinates, ideal continuous randomness, exact readings, and no bound on how far out a query may be placed. The obstruction for cap `N` already uses calibration degree at most `N-1`.

Thus the bounded-window positive-noise collapse in [[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]] is domain-dependent, whereas the fixed-cap obstruction in [[research/arithmetic_fidelity/findings/AF-578-continuous-randomness-retains-fixed-budget-polynomial-calibration-obstruction|AF-578]] survives this unbounded-domain change. Full-curve separation does not imply a uniform finite observation budget.

The new bridge is a degree-dependent compactification preserving the polynomial nuisance space and the exact adaptive experiment. Its source regularity is verified below, rather than assumed from boundedness of the source gaps. The controls are generalized-prime systems indexed by rational-prime edits; no RH conclusion follows.

## Exact experiment and conclusions

Let
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad Q_p=P-h_p,\quad
 \Phi_p(a)=Q_p^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
 \tag{1}
\]
Fix a known finite set `S={p_1<...<p_m}` of distinct odd primes, `m>=2`. An input is
\[
 y(a)=\Phi_{p_i}(a)+b(a),\qquad
 a>0,\quad b\in\Pi=\bigcup_{d\ge0}\Pi_d.
 \tag{2}
\]
The polynomial is fixed before the policy's independent seed and shared by all its observations. Policies are measurable, may query any finite positive real coordinate, and may adapt to previous responses. Only oracle value queries are counted. Source evaluations and exact real computation are free. Define
\[
 R_N^{\rm ray}=\inf_{\mathcal A:T\le N}\sup_{\substack{1\le i\le m\\b\in\Pi}}
       \Pr_{\Phi_{p_i}+b}(\widehat i\ne i),\quad
 c_m=1-1/m,\quad
 d(S)=\min_{i<m}\sup_{a>0}(\Phi_{p_{i+1}}-\Phi_{p_i})(a).
\]
Then, for every `N>=1`, without any large-prime assumption,
\[
 \boxed{R_N^{\rm ray}=c_m,\qquad
        \varepsilon_{\rm full}^{\rm ray,poly}(S)=d(S)/4>0.}
 \tag{3}
\]
The first equality also holds with `b in Pi_(N-1)`, even if that bound is supplied. The second is the supremal noise radius for unique identification from the entire curve with arbitrary additive error `||eta||_infinity<=epsilon`. At the displayed radius a midpoint alias exists; identification holds strictly below it. The fixed-cap lower bound also applies with bounded observation noise, because the allowed errors include zero.

For variable-length noiseless policies, let `T` be the query count at label return, or infinity on nonreturn, and put
\[
 e=\sup_{i,b}\Pr(T<\infty,\widehat i\ne i),\qquad
 q_N=\sup_{i,b}\Pr(T>N).
\]
Exactly as in AF-578,
\[
 \boxed{e+c_m q_N\ge c_m\quad\hbox{for every finite }N.}
 \tag{4}
\]
If `e<c_m`, the worst-case expected query count is infinite. Zero error forces `q_N=1` at every cap; this is a supremum over inputs, not a claim of nontermination on one input. The bound is sharp among policies returning almost surely on each fixed input: AF-577's continuous-random validation procedure can use a fixed bounded subinterval of the ray, and mixing it with immediate uniform guessing attains (4). That procedure returns within the actual calibration degree plus two queries almost surely. No corresponding noisy stopping theorem is asserted.

## Compactification preserves the capped exact experiment

Here is a sufficient condition for general sources `F_1,...,F_m` on the ray. Fix `N`, put `n=N-1`, and assume
\[
 H_i(x)=(1-x)^n(F_i-F_1)\!\left(\frac{x}{1-x}\right)
       \quad\hbox{extends to } C^n[0,1].
 \tag{5}
\]
There is no requirement that each `F_i` separately extend at infinity. Subtracting the known reference `F_1` is an invertible recoding of the exact observations.

The coordinate and response maps
\[
 x=\frac a{1+a},\qquad
 z(x)=(1-x)^n\{y(a)-F_1(a)\},\qquad
 \widetilde b(x)=(1-x)^n b\!\left(\frac{x}{1-x}\right)
 \tag{6}
\]
give `z=H_i+tilde b` on `(0,1)`. They bijectively carry `Pi_n` onto `Pi_n`, since
\[
 a^k\longmapsto x^k(1-x)^{n-k},\qquad
 b(a)=(1+a)^n\widetilde b\!\left(\frac a{1+a}\right).
 \tag{7}
\]
All maps are exact and invertible at every legal coordinate. A policy choosing an arbitrarily large finite `a` is simulated by a policy choosing `x` arbitrarily close to `1`, with the same seed, query count, responses after inversion, stopping event and label. No limiting value at `x=1` is supplied as an extra observation. Multiplication by the small factor in (6) loses no information in this exact-real model.

AF-578's bounded-interval theorem now applies to the sources `H_i` and nuisance `tilde b in Pi_n`. It gives minimax error `c_m` for cap `N`. This proves the first part of (3) whenever (5) holds. The lower bound on the degree-restricted subclass implies the lower bound for unknown unbounded degree; uniform guessing supplies the upper bound.

For clarity, the masking mechanism is still uniform over all adaptive query locations. AF-578 bounds the coefficient norm of an interpolant of any gap `H_i-H_j` at at most `N` arbitrary nodes by
\[
 B_N(H_i-H_j)=\sum_{k=0}^{N-1}\frac{2^k}{k!}
                   \|(H_i-H_j)^{(k)}\|_\infty.
 \tag{8}
\]
Giving the coefficients of `tilde b` an independent `N(0,L^2 I_N)` prior produces transcript total variation at most `B_N(H_i-H_j)/(2L)`. This prior pulls back through (7) to a proper Gaussian distribution on **one fixed admissible polynomial** on the ray. It need not be isotropic in the original monomial basis. Letting `L` grow is permitted because coefficients are unrestricted. Near-coincident nodes and nodes approaching infinity are covered by the same finite bound (8).

To derive (4), truncate at cap `N` and guess uniformly on nonreturn. The capped error is at most `e+c_m q_N`; apply the first equality of (3). The expectation conclusion follows from `sup E T>=N q_N`.

## Prime-edit gaps are smooth after compactification

The endpoint at `a=0` is controlled by [[research/arithmetic_fidelity/findings/AF-571-polynomial-drift-has-exact-small-window-probe-saturation|AF-571]]'s analytic implicit equation. With `B_p=Phi_p-1`, analytic functions
`R(u)=P(1+u)+log u` and `E(a)=E_1(a)+gamma+log a` near zero give
\[
 B_p(a)=a\exp\{\gamma+R(B_p(a))-h_p(1+B_p(a))-E(a)\}.
 \tag{9}
\]
The derivative with respect to `B_p` of left side minus right side is one at `(0,0)`. Thus the analytic implicit function theorem extends `Phi_p` through zero with `Phi_p(0)=1`. In particular every pairwise gap vanishes there and has all finite derivatives.

At infinity it is necessary to control derivatives, not just the values in AF-577. Fix odd primes `p<q` and interpolate their positive Dirichlet series:
\[
 Q_\tau=(1-\tau)Q_p+\tau Q_q,\quad
 k=Q_q-Q_p=h_p-h_q>0,\quad
 s_\tau(a)=Q_\tau^{-1}(E_1(a)),\quad 0\le\tau\le1.
\]
Positivity of `k` follows from `h_v(s)=s integral_v^(v+1) u^(-s-1) du`, which strictly decreases in `v`. The series `Q_tau` are positive Dirichlet series with the same smallest generator `2` and coefficient one. Set `lambda=log 2`. For each fixed derivative order `j`, absolute convergence at a fixed `s_0>1` gives, uniformly in `tau`,
\[
 Q_\tau(s)=2^{-s}\{1+R_\tau(s)\},\qquad
 \partial_s^jR_\tau(s)=O_j((2/3)^s)\quad(s\to\infty).
 \tag{10}
\]
For example, multiply each summand for a generator `ell>=3` by
`(2/ell)^(s-s_0)<=(2/3)^(s-s_0)` and sum its logarithmic moment at `s_0`. The finitely many altered generator weights remain bounded uniformly in `tau`.

Writing `u_tau=log(1+R_tau)` and `L(a)=-log E_1(a)`, the inverse equation is
\[
 \lambda s_\tau(a)=L(a)+u_\tau(s_\tau(a)).
 \tag{11}
\]
All positive-order derivatives of `L` are bounded for `a>=1`. One direct justification is
\[
 E_1(a)=\frac{e^{-a}}a J(a),\qquad
 J(a)=\int_0^\infty e^{-v}\frac a{a+v}\,dv:
\]
`J` is bounded away from zero there, and differentiation under the integral bounds every fixed derivative. Equation (10) bounds every derivative of `u_tau`; `lambda-u_tau'` is bounded away from zero for large `s`. Induction in (11) therefore bounds every positive-order derivative of `s_tau(a)`, uniformly in `tau` for sufficiently large `a`. Also `Q_tau(s)>=2^(-s)` and `E_1(a)<=e^(-a)/a` give `s_tau(a)>=a/lambda` for `a>=1`.

Differentiation in `tau` yields the exact identity
\[
 \partial_\tau s_\tau(a)
   =\frac{k(s_\tau(a))}{-Q_\tau'(s_\tau(a))}
   =W_\tau(s_\tau(a)).
 \tag{12}
\]
The numerator `k` is a fixed finite sum of exponentials with smallest base `p`; all its fixed derivatives are `O_(p,q,j)(p^(-s))`. The denominator equals `2^(-s){lambda+O((2/3)^s)}`. Differentiating the quotient gives
\[
 \partial_s^jW_\tau(s)=O_{p,q,j}((2/p)^s).
\]
Compose with `s_tau`, use its bounded derivatives and lower bound, and integrate (12) over `tau`. For every `j>=0`,
\[
 \boxed{\left|\partial_a^j(\Phi_q-\Phi_p)(a)\right|
       \le C_{p,q,j}e^{-c_p a}\quad(a\hbox{ sufficiently large}),
       \qquad c_p=\frac{\log(p/2)}{\log2}>0.}
 \tag{13}
\]
Each derivative in `x` of the compactified gap is a finite sum of polynomial powers of `(1-x)^(-1)` times a derivative in (13), with `a=x/(1-x)`. Exponential decay dominates all those powers. Consequently `(Phi_q-Phi_p)(x/(1-x))` extends smoothly, flat at `x=1`. Together with (9), this verifies (5) for every finite cap and every fixed finite odd-prime candidate set.

## Why the full-curve noise radius nevertheless becomes positive

For any bounded real function `g` on `(0,infinity)`,
\[
 \inf_{b\in\Pi}\|g-b\|_\infty
   =\inf_{c\in\mathbb R}\|g-c\|_\infty
   =\frac{\sup g-\inf g}{2}.
 \tag{14}
\]
Every nonconstant real polynomial is unbounded on the ray and has infinite uniform error against `g`; the midpoint of the range is the optimal constant. This elementary fact is precisely where the bounded-window polynomial-density argument fails.

Each ordered prime-edit gap is strictly positive by (12), vanishes at both endpoints by (9) and (13), and is continuous. Its finite positive supremum `D_(i,j)` is therefore attained in the interior. The distance between the corresponding two polynomial-calibrated full-curve classes is `D_(i,j)/2`. Observation balls of radius `epsilon` intersect at half that distance; the optimally constant-shifted midpoint is an explicit common noisy observation at `epsilon=D_(i,j)/4`.

A nonadjacent gap is a sum of positive adjacent gaps. Hence the smallest `D_(i,j)` is exactly `d(S)`, proving the second equality of (3). This recovers [[research/arithmetic_fidelity/findings/AF-568-free-output-offset-costs-third-adaptive-prime-edit-probe|AF-568]]'s full-curve constant-offset radius despite admitting every finite polynomial degree. It does **not** recover that finding's finite-query result, whose nuisance is restricted to constants.

## Exact controls and falsification boundaries

The rational analytic pair `F_0(a)=0`, `F_1(a)=a/(1+a)^2` provides a complete non-arithmetic control. Its gap is positive with maximum `1/4` at `a=1`, and vanishes at both endpoints. Thus its full-ray polynomial-quotient noise radius is `1/16`. Under (6) its transformed gap is the polynomial
\[
 H_1(x)=x(1-x)^N,
\]
which is smooth through both endpoints and lies outside `Pi_(N-1)`. Its cap-`N` minimax error is `1/2`. That the transformed source is polynomial of higher degree causes no problem: the lower bound uses only smoothness and degree-`N-1` nuisance.

A scratch-only Python `fractions.Fraction` check used caps `N=1,...,6`, the basis map (7), this rational control, and three node families for each cap: `a_j=(j+1)/(N+2)`, `a_j=10^6+j/10^6`, and `a_j=10^(3j-6)`, `j=0,...,N-1`. All **291 exact checks** passed over 18 complete node paths and 63 prefixes. They checked polynomial round trips, exact transformed values, interpolation coefficient bounds, orthogonal innovation energy, and reconstruction of every preceding value by its minimum-norm coefficient projection. These are finite algebra checks, not numerical evidence for the universal probability or prime-tail statements; those follow from the proofs.

The load-bearing distinctions are:

- The polynomial transformation depends on the cap. It is used for a lower bound on the subclass `Pi_(N-1)`, not to transform the whole unknown-degree class into one fixed bounded-degree class.
- The source condition (5) is sufficient, not a classification of all ray experiments. Bounded gaps alone do not guarantee its endpoint differentiability.
- The invertible exact-response rescaling in (6) changes noise bounds. The unweighted full-ray margin is proved separately by (14), not transported from a bounded-window noisy experiment.
- No query at infinity, derivative oracle, symbolic access to the unknown polynomial, coefficient bound, or finite-precision implementation is included.
- The positive radius depends on the fixed finite source set and need not stay positive as the prime locations or candidate family vary. It does not identify the ordinary-prime system against every generalized-prime control.

## Prior art and mathematical delta

The polynomial map (7) is classical [[research/prior_art/incremental/PA-polynomial-homogenization-linear-fractional-action|homogenization and linear fractional change of coordinate]]: Peter J. Olver, *Classical Invariant Theory*, London Mathematical Society Student Texts 44, Cambridge University Press (1999), Chapter 2, pp. 13–14, equations (2.4)–(2.7), Theorem 2.2 ([monograph](https://www.math.utoronto.ca/~ila/ClassicalInvariantTheory.pdf)). No new invariant-theoretic construction is claimed.

The interpolation/Gaussian lower-bound machinery is already derived in AF-578 and anchored in de Boor's *Divided Differences* ([2005 paper](https://arxiv.org/abs/math/0502036)), Wasilkowski's conditional Gaussian adaptive-information theorem (1986), and Arias-Castro, Candes and Davenport's adaptive-testing arguments ([author paper](https://arxiv.org/abs/1111.4646)). Equation (14), positive Dirichlet-series tail dominance, and the analytic implicit function theorem are classical elementary ingredients. These sources do not by themselves assert the prime-edit identification result.

The local addition is the exact unbounded-domain experiment reduction, the all-derivative prime-gap estimate validating it, and the resulting separation between **positive full-curve robustness** and **blind-guess finite-cap recovery** under the same unknown-polynomial calibration. This answers AF-578's explicitly excluded ray case without changing its bounded-window theorem. It closes unbounded query location as a repair for this registered source family; it does not settle recovery with quantitative calibration restrictions or finite-precision noise.
