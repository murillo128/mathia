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
More precisely, their unnormalized variation decays at the square-root
perturbation scale. Explicit endpoint layers supply the matching lower
bound and explain the failure of a finite-measure first derivative.

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
The sharper estimate, proved by resolving the endpoint layers below, is

\[
 \boxed{\|\nu_\sigma\|_{\rm TV}\asymp_r\sqrt{\tau_\sigma}.}
 \tag{8a}
\]

Here both comparison constants are positive and independent of
`sigma` once it is sufficiently large at the fixed `r`. Thus the
unnormalized variation tends to zero, whereas its ratio to `tau_sigma`
has order `tau_sigma^(-1/2)`.

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

## Endpoint layers determine the sharp variation scale

Write `tau=tau_sigma`, `e=e_sigma`, and let `tilde nu_sigma` be the
pushforward of `nu_sigma` under `x -> (x-mu_sigma)/b_sigma`. Define
`eta_tau=(psi_tau)_#(w du dv/(2pi)^2)`, so its cumulative function is
`D_tau` from (11). The needed full-source comparison in variation is

\[
 \|\widetilde\nu_\sigma-\eta_\tau\|_{\rm TV}
       =O_r(\sqrt e)=o_r(\sqrt\tau).
 \tag{21}
\]

Its constants must be uniform in the parameter; merely using WI-467's
fixed-parameter conclusion does not give (21). Here is that uniform
check. Keeping `u` and all remaining prime angles fixed, differentiation
in `v` acts only on powers of `z_3`. The remainder in (9) satisfies

\[
 \max_{0\le j\le2}\|\partial_v^jR_\sigma\|_\infty=O_r(e).
 \tag{22}
\]

Indeed each derivative multiplies a character by its `3`-exponent,
whose absolute value is at most `(log n+log m)/log 3` for a pair
`n,m`. The tail argument for (9) therefore remains valid with squared
logarithmic weights: for `sigma>=2`,
`sum_(n>=5) (log n)^3 n^(-sigma)=O(5^(-sigma))`, by factoring
`5^(2-sigma)` and comparing the remaining sum at exponent two.
The full normalized logarithmic moments through order two stay
bounded, while their `n>=5` tails are `O((2/5)^sigma)`.
Expanding `(log n+log m)^2` in the double sum and dividing by
`b_sigma asymp_r (2/3)^sigma` gives the claimed tail bound.
The `3,4` character has `v`-frequency one and retains its
`O_r(2^(-sigma))` bound. This proves (22).

Both `Y_sigma` and `psi_tau`, as functions of `v`, consequently have
their first two derivatives within `1/100` of those of `cos v` for
large `sigma`. Apply the elementary weighted circle lemma (9) of
WI-467 with weight `w(u,v)`. Its `C^1` norm in `v` is bounded uniformly
in `u`, and its stability constant is absolute after this scaling.
The combined `p=2,3` pushforwards differ by `O_r(sqrt(e))` in variation.

For `p>=5`, compare `Y_sigma` with `(Q^(-p)-mu_sigma)/b_sigma`.
Their `C^1` distance in `v` is `O(w_p/b_sigma)`, by WI-467 (13);
the factor `sum_k k a_(3^k)` there stays bounded as `sigma` grows.
Both maps have the same uniform cosine derivative geometry, including
after deletion. The weight `h_p` is constant along the smoothing
coordinate, and the deleted map has zero `h_p`-weighted pushforward.
The uniform tail cost is therefore

\[
 \sum_{p\ge5}B_p\sqrt{w_p/b_\sigma}
 \ll_r 3^{\sigma/2}\sum_{p\ge5}(\log p)^{3/2}
                           p^{-(\sigma+1)/2}
 =O_r((3/5)^{\sigma/2}),\qquad \sigma\ge4.
 \tag{23}
\]

For the last estimate factor `5^(-(sigma-4)/2)` and compare the
remaining sum with `sum_(n>=5) (log n)^(3/2)n^(-5/2)`.
Here `w_p/b_sigma <<_r (log p)(3/p)^sigma`, using
`A=O(2^(-sigma))`. Summing these individually defined measures proves
(21), with no infinite signed torus density or growing hidden
smoothing constant.

For a real number `t`, write `t_+=max(t,0)` and set

\[
 w_+(u)=h_2(u)+h_3(u),\qquad
 w_-(u)=h_2(u)+h_3(u-\pi),
\]
\[
 F_+(x)=-\frac{\sqrt2}{\pi}
       \int w_+(u)\sqrt{(\cos u-x)_+}\,\frac{du}{2\pi},
 \qquad
 F_-(x)=\frac{\sqrt2}{\pi}
       \int w_-(u)\sqrt{(x-\cos u)_+}\,\frac{du}{2\pi}.
 \tag{24}
\]

For every fixed compact interval `K` of real `x`, the endpoint formulas
are uniform on `K`:

\[
 \boxed{\begin{aligned}
  \frac{\widetilde C_\sigma(1+\tau x)}{\sqrt\tau}
       &=F_+(x)+O_{r,K}(\tau+\sqrt{e/\tau}),\\
  \frac{\widetilde C_\sigma(-1+\tau x)}{\sqrt\tau}
       &=F_-(x)+O_{r,K}(\tau+\sqrt{e/\tau}).
 \end{aligned}}
 \tag{25}
\]

These are boundary layers of width `b_sigma tau_sigma` in the original
response coordinate, centered at `mu_sigma +/- b_sigma`. They are not
evaluations of the divergent profile `P` at its endpoints.

To prove (25) for the model, use its zero total mass. At the upper
endpoint the complement of the sublevel set, for fixed `u`, is the
arc `|v|<alpha`, where
`alpha=arccos(1-tau(cos u-x)_+)`. Uniformly for `x in K`,

\[
 \alpha=\sqrt{2\tau}\sqrt{(\cos u-x)_+}+O_K(\tau^{3/2}).
\]

Integrating the smooth weight over this symmetric arc gives
`alpha w_+(u)/pi+O_K(alpha^3)`. After averaging over `u`, the
zero total mass makes the cumulative function the negative of this
arc mass; no conditional zero-mass assertion is needed. At the lower
endpoint the sublevel set itself is an arc
about `v=pi`, with half-width
`arccos(1-tau(x-cos u)_+)` and weight `w_-(u)`. These two expansions
give (25) for `D_tau` with error `O_K(tau)` after division by
`sqrt(tau)`. Equation (21) transfers them uniformly to the full
coefficient. Its normalized error tends to zero because `e/tau->0`.

The upper profile is nonzero without a numerical sign test. Writing
`q=p^(-1/2)` and `c=cos u`,

\[
 h_p(u)=\log p\left(1-\frac{1-q^2}{1-2qc+q^2}\right)
\]

is strictly decreasing in `c`. Thus `w_+` is strictly decreasing in
`c` and has zero Haar mean, whereas `sqrt(c_+)` is increasing and
nonconstant. Their covariance is strictly negative. Explicitly,
for independent arcsine variables `X,X'`, twice that covariance is
`E[(w_+(X)-w_+(X'))(sqrt(X_+)-sqrt(X'_+))]<0`, where `w_+(c)`
denotes the displayed function of `c`. Hence `F_+(0)>0` and (25)
gives

\[
 \|\nu_\sigma\|_{\rm TV}
 \ge2|\widetilde C_\sigma(1)|
 =2\sqrt\tau\{F_+(0)+o_r(1)\}.
 \tag{26}
\]

The factor two uses the zero total mass of the signed measure: the
chosen half-line and its complement have opposite masses.

For the matching upper bound, the density of `eta_tau` is
`k_tau(y)=int H_u(y-tau cos u) du/(2pi)`, with `H_u` from (14).
Its zero-parameter density vanishes almost everywhere. Therefore (15)
gives `||eta_tau||_TV<=int ||H_u(.-tau cos u)-H_u||_1 du/(2pi)
=O(sqrt(tau))`. Combining this with (21) proves (8a).

As matching checks, the profiles vanish on their outer sides:
`F_+(x)=0` for `x>=1` and `F_-(x)=0` for `x<=-1`. On their inner
sides, expansion of the square roots and the zero means gives

\[
 F_+(x)=\frac{A_2+A_3}{\pi\sqrt{-2x}}+O(|x|^{-3/2})
       \quad(x\to-\infty),\qquad
 F_-(x)=\frac{A_2-A_3}{\pi\sqrt{2x}}+O(x^{-3/2})
       \quad(x\to+\infty).
 \tag{27}
\]

The signs and constants agree with the two singular ends of `P`.
This checks separate formulas, without asserting uniformity of (25)
on growing `K`. In particular the lower endpoint layer need not have
the upper layer's sign; no stochastic ordering is restored.

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
For neighboring prior art on fractional regularity and variation
stability of nonlinear image laws, see V. I. Bogachev, E. D. Kosov and
G. I. Zelenov, *Fractional smoothness of distributions of polynomials
and a fractional analog of the Hardy–Landau–Littlewood inequality*,
**Trans. AMS 370** (2018), 4401–4432,
[introduction and §§5–6](https://arxiv.org/abs/1602.05207).
That paper treats Gaussian polynomial images, including the familiar
inverse-square-root density at a quadratic critical point. Its
hypotheses do not directly cover the signed infinite Euler-torus
coefficient. The arc expansions (24)–(27), the uniform summed tail
(23), and both bounds for this coefficient are proved here.

The local delta is a full-source, controlled profile at the first
prime-square scale, including the summed tail (10), interior sign
location (19), and failure of a parameter-uniform finite-measure
expansion (8). WI-466 proved existence of opposite signs through a
polynomial witness; it did not locate the coefficient at fixed scaled
interior levels. WI-467 proved finite variation at each fixed parameter;
it did not control variation relative to the vanishing perturbation.
The endpoint layers sharpen the relative divergence to the exact order
in (8a), while showing that the unnormalized variation actually vanishes.
An interior first derivative in `L^1` and a square-root response in
variation coexist for the same full-source coefficient.

The endpoint singularities explain why uniform convergence cannot be
extended to all scaled thresholds, and why a finite scalar measure at
each parameter does not yield a finite-measure derivative in this
parameter limit. The main term is not to be evaluated at `y=+/-1`.
Equation (25) supplies the separate endpoint description; the constants
in (7) still deteriorate there and at varying `r`.
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
prime tails (10) and (23), the derivative uniformity in (22), the minus
signs in (16) and (24), and distinguishing the limits in prime cutoff,
`sigma`, and sampling height. The result is an analytic
derivation, without numerical, Lean, or independent-review certification.
No separate finite formalization target with a material fertility gain
is identified by the elementary circle algebra.
