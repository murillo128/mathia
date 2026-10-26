# WI-468 — first prime-square correction has a singular arcsine profile

**Status:** EXACT-DERIVED + CLASSICAL-PERTURBATION-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the exhaustion-independent cumulative coefficient; [WI-466](WI-466-full-euler-sampling-bias-changes-sign-on-increasing-tests.md), for the full-series first-prime-square expansion; [WI-467](WI-467-far-right-euler-correction-is-an-absolutely-continuous-signed-measure.md), for finite scalar variation at each sufficiently large fixed safe-line parameter.

## Claim and limits

Fix `r>0` and let `sigma=1+epsilon` tend to infinity. The full coherent
Euler response's cumulative prime-axis coefficient has an explicit
first perturbation profile after centering and scaling its response.
The profile is integrable, changes sign at an explicit interior level,
and is unbounded at the two limiting endpoints. Consequently the scalar
signed correction measures of WI-467, although finite at every
sufficiently large fixed `sigma`, have **unbounded total variation
relative to the first perturbation scale** as `sigma` tends to infinity.

This is a parameter limit of the already-defined Haar coefficient.
It is not a first arithmetic sampling law for indicators. In particular,
neither a zero-sampling height limit nor a joint height/parameter limit
occurs in this result.

## Definitions and statement

All torus integrations use probability Haar measure `m`. Put

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\quad
 a_n=\Lambda(n)n^{-\sigma}/A,\quad
 G(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r},
\]
\[
 Q=\left\|\sum_{p,k\ge1}a_{p^k}z_p^kv_{p^k}\right\|^2,
 \qquad \langle v_n,v_m\rangle=G(n,m),\qquad \|v_n\|\le1.
 \tag{1}
\]

The vector sum is absolutely convergent and retains its original
normalization. Define the full Haar mean and the two scales

\[
 \mu_\sigma=\int Q\,dm=\sum_n a_n^2G(n,n),\qquad
 b_\sigma=2a_2a_3G(2,3)>0,
\]
\[
 \tau_\sigma=\frac{a_4G(2,4)}{a_3G(2,3)}
 =\frac{\log2}{\log3}\frac{G(2,4)}{G(2,3)}(3/4)^\sigma>0,
 \qquad Y_\sigma=\frac{Q-\mu_\sigma}{b_\sigma}.
 \tag{2}
\]

For each prime write

\[
 h_p(\theta)=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta),\qquad
 B_p=\frac{2\log p}{\sqrt p-1},\qquad
 w_p=\frac{\log p}{A(p^\sigma-1)}.
 \tag{3}
\]

Thus `int h_p=0` and `||h_p||_1<=B_p`. Let `C_sigma` be WI-464's
cumulative coefficient, extended by zero to the real line. For all
sufficiently large `sigma`, use its unique absolutely continuous
representative from WI-467:

\[
 \nu_\sigma=\sum_p Q_\#(h_p m),\qquad
 C_\sigma(x)=\nu_\sigma(({-\infty},x]),\qquad
 \widetilde C_\sigma(y)=C_\sigma(\mu_\sigma+b_\sigma y).
 \tag{4}
\]

The series in (4) converges absolutely in total variation at each such
fixed parameter. It does not define an infinite signed torus density.
Set `A_p=(log p)/sqrt(p)` and

\[
 P(y)=\frac{A_2+A_3y}{\pi\sqrt{1-y^2}}\,
       \mathbf1_{\{-1<y<1\}},\qquad
 e_\sigma=2^{-\sigma}+(3/5)^\sigma.
 \tag{5}
\]

The conclusions are

\[
 \boxed{\|\widetilde C_\sigma-\tau_\sigma P\|_{L^1(\mathbb R)}
       =O_r(\tau_\sigma^{3/2}+e_\sigma),}
 \tag{6}
\]

and, for every fixed compact interval `J` in `(-1,1)`,

\[
 \boxed{\sup_{y\in J}|\widetilde C_\sigma(y)-\tau_\sigma P(y)|
       =O_{r,J}(\tau_\sigma^2+e_\sigma).}
 \tag{7}
\]

Since `e_sigma/tau_sigma=O_r((4/5)^sigma)`, the normalized cumulative
coefficient converges to `P` in `L^1` and uniformly on every such `J`.
In contrast,

\[
 \boxed{\|\nu_\sigma\|_{\rm TV}/\tau_\sigma\longrightarrow\infty.}
 \tag{8}
\]

Total variation here is the full mass of the variation measure.
Equation (8) is a relative statement; it does not assert divergence
of the unnormalized variation as `sigma` grows.

## The infinite tail is small at the perturbation scale

Use the Haar-preserving coordinates
`u=theta_2`, `v=theta_2-theta_3`. WI-466's expansion gives

\[
 Y_\sigma=\cos v+\tau_\sigma\cos u+R_\sigma,
 \qquad \|R_\sigma\|_\infty\le\|R_\sigma\|_{\rm W}=O_r(e_\sigma).
 \tag{9}
\]

Here the Wiener norm sums absolute rational-character coefficients.
For clarity, the remainder estimate retains every prime power:
`sum_(n>=5) Lambda(n)n^(-sigma)=O(5^(-sigma))` and
`A=O(2^(-sigma))` for `sigma>=2`. The off-diagonal coefficient mass
involving `n>=5`, divided by `b_sigma`, is `O_r((3/5)^sigma)`.
The only other omitted off-diagonal pair among `2,3,4` is `3,4`, of
scaled size `O_r(2^(-sigma))`. The full mean removes all diagonal
terms. Thus (9) is not a three-term truncation assumption.

The additional budget needed for the signed prime tail is

\[
 \frac1{b_\sigma}\sum_{p\ge5} B_pw_p=O_r((3/5)^\sigma).
 \tag{10}
\]

Indeed, for `sigma>=2`,
`B_pw_p << A^(-1)(log p)^2 p^(-sigma-1/2)`, while
`1/(A b_sigma)=O_r(3^sigma)`. Factoring `5^(-sigma)` from the
prime sum leaves a uniformly bounded sum, by comparison at `sigma=2`
with `sum_(n>=5)(log n)^2 n^(-5/2)`. This proves (10) without a
prime number theorem or a zero hypothesis.

Let `psi_tau=cos v+tau cos u` and define the finite, signed model

\[
 D_\tau(y)=\iint\mathbf1_{\{\psi_\tau\le y\}}
       [h_2(u)+h_3(u-v)]\,\frac{du\,dv}{(2\pi)^2}.
 \tag{11}
\]

For any real `x,x'`, the integral over all thresholds of
`|1_(x<=y)-1_(x'<=y)|` is `|x-x'|`. Applying this to (9) controls
the `p=2,3` terms by `(B_2+B_3)||R_sigma||_infinity` in `L^1`.
For `p>=5`, delete all powers of `p` from `Q`, obtaining `Q^(-p)`.
Its weighted pushforward by `h_p` is zero, and
`||Q-Q^(-p)||_infinity<=2w_p`. Therefore

\[
 \|\widetilde C_\sigma-D_{\tau_\sigma}\|_1
 \le(B_2+B_3)\|R_\sigma\|_\infty
       +\frac2{b_\sigma}\sum_{p\ge5}B_pw_p
 =O_r(e_\sigma).
 \tag{12}
\]

This comparison sums separately defined coordinate corrections, using
their cancellation. Multiplying a uniform response error by the
divergent sum `sum_p B_p` would not prove (12).

There is also a pointwise version on each fixed interior interval `J`:

\[
 \sup_{y\in J}|\widetilde C_\sigma(y)-D_{\tau_\sigma}(y)|
 =O_{r,J}(e_\sigma).
 \tag{13}
\]

For the two anchor primes, condition on `u`. The density of `cos v`
is bounded on a fixed neighborhood of `J` for small `tau`, so the
indicator displacement caused by `R_sigma` costs `O_J(||R_sigma||)`;
the fixed weights `h_2,h_3` are bounded. For every other prime, condition
on all angles except `theta_3`. WI-467's estimates (5)–(8) give two
monotone branches and first and second derivatives within `o_r(1)` of
those of the shifted cosine, also after deleting that prime. By (9)
and `2w_p/b_sigma=O_r((3/5)^sigma)`, the scaled deleted response is
uniformly within `o_r(1)` of `cos v`. Every preimage of a small fixed
neighborhood of `J` consequently has derivative bounded below by a
positive `J`-dependent constant. Change of variables bounds its
conditional density there uniformly in the deleted prime and all
conditioned angles. The indicator displacement costs
`O_J(w_p/b_sigma)`; multiplying by `|h_p|` and then summing uses (10).
This proves (13). Mere absolute continuity would not supply this
uniform interior bound.

## Differentiate the weighted arcsine primitive, not the indicator

Write `w(u,v)=h_2(u)+h_3(u-v)`. For fixed `u`, the weighted image of
`cos v` has density

\[
 H_u(y)=\frac{w(u,\arccos y)+w(u,-\arccos y)}
              {2\pi\sqrt{1-y^2}}\mathbf1_{\{|y|<1\}},
 \qquad S_u(y)=\int_{-\infty}^y H_u(x)\,dx.
 \tag{14}
\]

The smoothness of `h_2,h_3` gives a uniform `L^1` bound for `H_u` and
the translation estimate

\[
 \sup_u\|H_u(\cdot-s)-H_u\|_1=O(\sqrt{|s|}),\qquad |s|\le1.
 \tag{15}
\]

To check (15), the `2|s|` endpoint collars have integral
`O(sqrt(|s|))`, using `|H_u(y)|<< (1-|y|)^(-1/2)`.
Off those collars, `|H_u'(y)|<< (1-|y|)^(-3/2)` uniformly in `u`.
Integrating the derivative over a translation of length `|s|` gives
the same bound. Constants here depend only on the fixed two weights.

Since `int w(u,v) du/(2pi)=0` at every `v`, `D_0(y)=0` for every
threshold. Equation (11) is exactly

\[
 D_\tau(y)=\int [S_u(y-\tau\cos u)-S_u(y)]\,\frac{du}{2\pi}
 =-\tau\int\cos u\int_0^1H_u(y-s\tau\cos u)\,ds\,\frac{du}{2\pi}.
 \tag{16}
\]

This uses absolutely continuous primitives and Fubini, with (15)
justifying the global `L^1` derivative. On a compact interior `J`,
the first derivatives of `H_u` are uniformly bounded instead, giving
an `O_J(tau^2)` remainder in (16). Thus

\[
 D_\tau=\tau P+O_{L^1}(\tau^{3/2}),\qquad
 D_\tau(y)=\tau P(y)+O_J(\tau^2)\quad(y\in J),
 \tag{17}
\]

where the sign and constant follow directly from Fourier orthogonality:

\[
 \int\cos u\,w(u,v)\,\frac{du}{2\pi}
 =-A_2-A_3\cos v,
 \qquad
 -\int\cos u\,H_u(y)\,\frac{du}{2\pi}=P(y).
 \tag{18}
\]

Combining (12)–(13) with (17) proves (6)–(7).

## Sign location and the failure of uniform variation

The function `log x/sqrt(x)` is increasing for `1<x<e^2`, so
`0<A_2<A_3`. The unique zero of the limiting interior profile is

\[
 y_0=-\frac{A_2}{A_3}
 =-\sqrt{\frac32}\frac{\log2}{\log3}\in(-1,0).
 \tag{19}
\]

On every compact interval strictly inside `(-1,y_0)`, the actual
`C_sigma(mu_sigma+b_sigma y)` is strictly negative for all sufficiently
large `sigma`. It is strictly positive on every compact interval in
`(y_0,1)`. Continuity guarantees at least one crossing converging to
`y_0`: choose zeros in a fixed small neighborhood of `y_0`; uniform
convergence there forces every accumulation point of those zeros to
be `y_0`. We do not claim uniqueness of the finite-parameter crossing.

As a normalization check, `int P=A_2`. Consequently (6) yields

\[
 \int C_\sigma(x)\,dx
 =b_\sigma\tau_\sigma A_2\{1+o_r(1)\}
 =2a_2a_4G(2,4)\frac{\log2}{\sqrt2}\{1+o_r(1)\},
 \tag{20}
\]

the leading `2,4` term of WI-464's positive integrated mean coefficient.

Finally `P(y)` tends to positive infinity as `y` approaches `1` from
below, and to negative infinity at `-1`. It is not essentially bounded
and is not a function of bounded variation. If a subsequence of
`||nu_sigma||_TV/tau_sigma` were bounded, the cumulative functions
`C_sigma/tau_sigma`, and hence their affine pullbacks, would be
uniformly bounded. Their `L^1` limit `P` would then be essentially
bounded, a contradiction. This proves (8). Equivalently the normalized
pushforward correction measures converge distributionally to `P'`,
which is not a finite signed measure. Affine rescaling of their scalar
coordinate does not change their total variation.

## Prior art, controls, and research consequence

Ford–Zaharescu, *On the distribution of imaginary parts of zeros of the
Riemann zeta function*, **J. reine angew. Math. 579** (2005), 145–158,
[equations (1.9)–(1.10)](https://ford126.web.illinois.edu/wwwpapers/fz.pdf),
give the classical prime-axis correction; the density here is their
density multiplied by `2pi` in the dyadic normalized convention.
Differentiation of integrals over moving sublevel sets is also classical;
see S. Uryasev, *Derivatives of probability functions and integrals over
sets given by inequalities*, **J. Comput. Appl. Math. 56** (1994),
197–223, [DOI 10.1016/0377-0427(94)90388-3](https://doi.org/10.1016/0377-0427(94)90388-3).
This is contextual prior art, not a theorem imported without checking
its hypotheses: (14)–(18) give the entire differentiation argument used
here. The arcsine density, translation continuity, and variation
obstruction are standard mechanisms; no literature priority is claimed.

The local delta is a full-source, controlled profile at the first
prime-square scale, including the summed tail (10), interior sign
location (19), and failure of a parameter-uniform finite-measure
expansion (8). WI-466 proved existence of opposite signs through a
polynomial witness; it did not locate the coefficient at fixed scaled
interior levels. WI-467 proved finite variation at each fixed parameter;
it did not control variation relative to the vanishing perturbation.

The endpoint singularities explain why uniform convergence cannot be
extended to all scaled thresholds, and why a finite scalar measure at
each parameter does not yield a finite-measure derivative in this
parameter limit. The main term is not to be evaluated at `y=+/-1`.
The constants in (7) deteriorate at those endpoints and at varying `r`.
There is no conclusion near the pole `sigma=1`.

The prime-only control has zero correction by common-rotation
invariance. The `2,3` response alone has `D_0=0`; the coherent `2,4`
pair is exactly what activates (18). No independent torus density,
positive correction measure, or stochastic ordering is assumed.

Ford–Soundararajan–Zaharescu,
[*On the distribution … II*, §1](https://arxiv.org/pdf/0805.2745),
distinguish the fixed smooth-test correction from the interval problem.
The present parameter theorem supplies no missing arithmetic estimate
for thresholds; WI-463's obstruction remains. Nor does it couple the
observable to a single off-line zero, improve a critical-line proportion,
or imply RH. Its decisive checks are the full mean in (9), the weighted
prime tail (10), the minus sign in (16), and distinguishing the limits
in prime cutoff, `sigma`, and sampling height. The result is an analytic
derivation, without numerical, Lean, or independent-review certification.
No separate finite formalization target with a material fertility gain
is identified by the elementary circle algebra.
