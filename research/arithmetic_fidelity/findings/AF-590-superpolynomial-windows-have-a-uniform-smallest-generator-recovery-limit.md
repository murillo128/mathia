# AF-590 — Superpolynomial windows have a uniform smallest-generator recovery limit

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · UNIFORM-JOINT-LIMIT · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

The large-window endpoint of
[[research/arithmetic_fidelity/findings/AF-589-prime-window-crossover-is-set-by-the-exact-source-coordinate|AF-589]]
holds along **every** joint path on which the normalized window grows faster
than every fixed power of the smaller edit location. This requires a uniform
logarithmic tail estimate; substituting the fixed-pair equivalent from AF-588
would not justify the conclusion.

Use the registered generalized-prime controls
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_j(s)=j^{-s}-(j+1)^{-s},\quad Q_j=P-h_j,\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
 \tag{1}
\]
For odd rational-prime labels `p<q`, put
\[
 L=\log p,\quad c=e^{B_1},\quad \ell_0=\log2,\quad H=p^{-2}-q^{-2},
 \quad d(a)=\Phi_q(a)-\Phi_p(a),\quad D=\max_{a>0}d(a),
\]
\[
 g_{p,q}(x)=d(x/(cL))/D,\quad
 \Delta_{r;p,q}(B)=1-2\operatorname{dist}_{C[0,B]}(g_{p,q},\Pi_r),
 \quad \kappa_r=\frac{r^2}{2}\cot^2\frac{\pi}{2r}.
 \tag{2}
\]
Here `B_1` is the reciprocal-prime Meissel--Mertens constant and `r>=2` is a
fixed supplied integer. Each input has one shared degree-at-most-`r`
polynomial calibration with unrestricted coefficients and arbitrary absolute
bounded error. Different labels may choose different calibrations. The
supremal whole-window identification radius is `D(1-Delta)/4`; the full-ray
radius is `D/4`. The continuous zero endpoint does not change the norm on
positive observation coordinates.

**Theorem.** For every sequence with `p->infinity`, `B->infinity` and
`log B/log p -> infinity`, uniformly over all larger prime labels `q>p`,
\[
 \boxed{\frac{B^2\Delta_{r;p,q}(B)}{\kappa_r\log B}
                   \longrightarrow c\ell_0.}
 \tag{3}
\]
There is no upper bound on `log B/log p`, and no restriction on `q/p`.
Consequently, if `delta->0`, `p->infinity` and
`log(1/delta)/log p -> infinity`, then the minimum normalized range satisfies
\[
 \boxed{R_{r;p,q}(\delta):=\inf\{B>1:\Delta_{r;p,q}(B)\le\delta\}
 \sim\sqrt{\frac{\kappa_r c\ell_0}{2}}
                \sqrt{\frac{\log(1/\delta)}{\delta}}.}
 \tag{4}
\]
The physical upper coordinate is this range divided by `c log p`. This closes
the unrestricted superpolynomial-window regime explicitly excluded from AF-589.
It agrees with the large-prime limit of AF-588's fixed-pair coefficient,
while AF-589's finite positive crossover ratios can have smaller coefficients.

## A logarithmic source estimate uniform in both labels and tail depth

Let `k=h_p-h_q`, and interpolate the sources:
\[
 Q_\theta=(1-\theta)Q_p+\theta Q_q,\qquad
 s_\theta(a)=Q_\theta^{-1}(E_1(a)),\qquad 0\le\theta\le1.
\]
Implicit differentiation gives the positive identity
\[
 d(a)=\int_0^1\frac{k(s_\theta(a))}{-Q_\theta'(s_\theta(a))}\,d\theta.
 \tag{5}
\]
All these sources retain generator `2` with coefficient one. Every other
coefficient is nonnegative and at most one: replacing an odd prime by its
even successor creates no collision with another prime or successor here.
For `s>=2`, comparison with the convergent integer series at exponent two
therefore gives, with absolute constants independent of `p,q,theta`,
\[
 Q_\theta(s)=2^{-s}\{1+O((2/3)^s)\},\qquad
 -Q_\theta'(s)=\ell_0 2^{-s}\{1+O((2/3)^s)\}.
 \tag{6}
\]
For example the residuals, after division by `2^(-s)`, are bounded by
`(2/3)^s sum_(n>=3)(3/n)^2` and
`(2/3)^s sum_(n>=3)log n (3/n)^2`, respectively. This makes the uniformity
explicit even when the edit labels themselves escape.

Set `s_0(a)=-log E_1(a)/ell_0`. For all sufficiently large `a`, (6) implies
\[
 0\le s_\theta(a)-s_0(a)\le C(2/3)^{s_0(a)}.
 \tag{7}
\]
Indeed `Q_theta(s)>=2^(-s)` first gives `s_theta>=s_0`, and taking logarithms
of (6) at `s_theta` gives the upper bound.

The numerator needs a different estimate. For **every** `s>=1`, the exact
positive integral
\[
 k(s)=s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv
\]
and integration of `v^(-s-2)` give
\[
 \boxed{s(1+1/p)^{-s-2}\le
       \frac{k(s)}{H p^{-(s-1)}}\le\frac{s(s+1)}2.}
 \tag{8}
\]
To check the gap normalization, write `b=log(q/p)>0`. The remaining ratio is
\[
 1\le\frac{1-e^{-(s+1)b}}{1-e^{-2b}}\le\frac{s+1}{2}.
\]
The upper inequality follows from the decrease of `(1-e^(-tb))/t` in `t`.
The inner integral lies between
`(1+1/p)^(-s-2)v^(-s-2)` and `v^(-s-2)`. No bounded-exponent assumption
enters (8). In particular,
\[
 \log(k(s)/H)=-(s-1)L+
                 O\big(\log(s+1)+s/p\big),\qquad s\ge2.
 \tag{9}
\]

Combining (6)--(9), uniformly in `theta`, gives
\[
 \log\!\left(\frac{k(s_\theta)}{-Q_\theta'(s_\theta)H}\right)
 =-s_0(L-\ell_0)+L+
 O\!\left(1+\log(s_0+1)+\frac{s_0}{p}+L(2/3)^{s_0}\right).
 \tag{10}
\]
For instance, replacing `s_theta` by `s_0` in `-(s_theta-1)L` costs at most
`CL(2/3)^s_0`; it need not be `o(1)`. The positive integral (5) lies between
the same two exponential bounds, so (10) also holds with its left side
replaced by `log(d(a)/H)`.

The load-bearing source normalization from
[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]], equation (10), is
\[
 D=\frac{H}{eL}\{1+O(L^{-1})\},\qquad
 \|g_{p,q}-f\|_{[0,\infty)}=O(L^{-1}),\quad f(x)=xe^{1-x},
 \tag{11}
\]
uniformly in `q>p`. Since `x=cLa`, the `log L` terms cancel in `log(g(x)/x)`:
\[
 \log\frac{g_{p,q}(cLa)}{cLa}
 =-s_0(L-\ell_0)+L-\log a+
 O\!\left(1+\log(s_0+1)+\frac{s_0}{p}+L(2/3)^{s_0}\right).
 \tag{12}
\]
The classical real-axis exponential-integral expansion gives
`s_0=(a+log a+O(1/a))/ell_0`. Dividing (12) by `cLa` proves the uniform bound
\[
 \boxed{\left|\frac{-\log(g_{p,q}(cLa)/(cLa))}{cLa}
                       -\lambda_0\right|
 \le C\left(\frac1{\log p}+\frac{\log a}{a}\right),\qquad
 \lambda_0=\frac1{c\ell_0},}
 \tag{13}
\]
for all sufficiently large `p` and all `a>=a_0`, with fixed `a_0>1` and
absolute constants. Neither `a/p`, `s_0/p`, nor the size of
`L(2/3)^s_0` is restricted. Their contributions after division by `La` are
absorbed by the right side of (13).

## Why the fixed-pair equivalent cannot replace this estimate

For fixed labels, AF-588 uses `k(s)~p^(-s)` as `s->infinity`. Along joint
paths this can fail by an arbitrarily large relative factor. Positivity and
`k<=h_p` give
\[
 0<\frac{k(s)}{p^{-s}}\le1-(1+1/p)^{-s}\le s/p.
 \tag{14}
\]
Thus the ratio tends to zero whenever `s->infinity` but `s/p->0`, for
example `s=log p`, independently of the choice of `q>p`. Such exponents
occur at relevant tail depths inside the regime of (3). Likewise (7)'s
inverse displacement cannot always be multiplied by `L` and called `o(1)`.

The successful retained quantity is the **logarithmic** rate after the
gap factor `H` has been removed. Equation (8) covers both `s/p->0` and
`s/p->infinity`, and (13) shows why these different relative-amplitude
regimes nevertheless have the same limiting window coefficient.

## Tail thresholds and the sharp polynomial quotient

Fix a joint sequence in (3) and `0<epsilon<1/2`. Put
\[
 t_- =\frac{2(1-\epsilon)}{\lambda_0}\log B,\qquad
 t_+ =\frac{2(1+\epsilon)}{\lambda_0}\log B.
 \tag{15}
\]
Both satisfy `t_±=Theta(log B)=o(B)` and `t_±/(cL)->infinity`.
Choose `A_epsilon` and then a starting prime so that (13), for
`x>=cL A_epsilon`, implies
\[
 e^{-\lambda_0(1+\epsilon/2)x}\le g_{p,q}(x)/x
           \le e^{-\lambda_0(1-\epsilon/2)x}.
 \tag{16}
\]
In particular `g(t_+)/t_+=o(B^(-2))`.

The lower bound must also cover the intervening and near-zero coordinates.
AF-589, equation (7), supplies for the fixed `A_epsilon`
\[
 g_{p,q}(x)/x\ge C_-\exp[-Lz(A_\epsilon)],
 \quad 0<x\le cL A_\epsilon,\quad
 z(A)=P^{-1}(E_1(A))-1.
 \tag{17}
\]
Since `L=o(log B)`, this is `B^(-o(1))` up to a constant. On
`cL A_epsilon<=x<=t_-`, (16) instead bounds the ratio below by
`B^(-2(1-epsilon)(1+epsilon/2))`. Consequently
\[
 \boxed{\frac{t_-}{B^2}\sup_{0<x\le t_-}\frac{x}{g_{p,q}(x)}\to0,
        \qquad \frac{g_{p,q}(t_+)}{t_+}=o(B^{-2}).}
 \tag{18}
\]
This is the precise discriminator-relative tail information used below.

Let `v_B` be a best polynomial and `V_B(y)=v_B(By)`. The constant `1/2`
gives error `E_B<=1/2` and `||V_B||<=3/2`. At fixed degree, pass on any
sequence to a coefficientwise limit `V` and an error limit `E`. Equation
(11) forces every exact peak `m_p` of `g_(p,q)` to tend to one and gives
`g_(p,q)(By)->0` for fixed `y>0`. The endpoint and peak constraints then give
\[
 E=1/2,\qquad |V|\le1/2,\qquad V(0)=1/2,\qquad V'(0)=0.
 \tag{19}
\]
For the slope, `V_B(m_p/B)-V_B(0)>=1-2E_B>=0` gives `V'(0)>=0`, while
endpoint maximality gives `V'(0)<=0`.

The constrained-curvature certificate of
[[research/arithmetic_fidelity/findings/AF-586-every-fixed-calibration-degree-has-an-explicit-sharp-range-constant|AF-586]], equations (4)--(7), now gives `V''(0)>=-kappa_r`.
Its finite proof interpolates `(V-V_r^*)/y^2` at the `r-1` remaining
alternating contacts of
`V_r^*(y)=-T_r(cos(pi/r)-(1+cos(pi/r))y)/2`.
All the signed interpolation contributions to the curvature difference are
nonnegative. The zero-slope constraint in (19) is essential.

Interpolating `v_B` at `m_p` between zero and `t_+` gives
\[
 \Delta_{r;p,q}(B)\le\frac{m_p}{t_+}g_{p,q}(t_+)
 -\frac{m_p(t_+-m_p)}{2B^2}\{V''(0)+o(1)\}.
 \tag{20}
\]
Coefficient convergence controls the second derivative uniformly on this
shrinking rescaled interval. Equations (18)--(20) prove
\[
 \limsup\frac{B^2\Delta_{r;p,q}(B)}{\kappa_r\log B}
                    \le(1+\epsilon)/\lambda_0.
 \tag{21}
\]

For a matching whole-window witness, AF-586 provides
\[
 A_r(y)=\tfrac12-V_r^*(y)=\alpha_r y^2H_r(y),\quad
 \alpha_r=\kappa_r/2,\quad H_r(0)=1,\quad H_r\ge0,\quad0\le A_r\le1
 \quad(0\le y\le1).
\]
Set
\[
 \beta_B=\sup_{x\ge t_-}g_{p,q}(x),\quad
 \eta_B=\sqrt{\beta_B+\log B/B^2},\quad
 k_B=(1-\eta_B)\alpha_r/B^2,
 \quad Q_B(x)=k_Bx(t_--x)H_r(x/B).
 \tag{22}
\]
Whole-ray convergence (11) gives `beta_B->0`, hence `eta_B->0`, and
`beta_B+log B/B^2=o(eta_B)`.
By (18), `0<=Q_B/g=o(1)` uniformly before `t_-`. After `t_-`,
\[
 -Q_B(x)=(1-\eta_B)(1-t_-/x)A_r(x/B)\in[0,1-\eta_B].
\]
Thus `G_B=g-Q_B` is nonnegative everywhere and its tail is at most
`1-eta_B+beta_B`. At an exact peak,
`G_B(m_p)=1-O(log B/B^2)`, exceeding that tail bound eventually. Every
maximizer `x_B` of `G_B` lies before `t_-`; since `G_B<=g` there and its
maximum tends to one, (11) gives `x_B->1`.

With `M_B=max G_B`,
\[
 Q_B(x_B)\le1-M_B\le Q_B(m_p),\qquad
 1-M_B\sim k_Bt_-\sim\frac{\kappa_r(1-\epsilon)}{\lambda_0}
                                  \frac{\log B}{B^2}.
 \tag{23}
\]
Here `Q_B(x)/(k_Bt_-)->x` uniformly on bounded sets. The polynomial
`Q_B+M_B/2` has error exactly `M_B/2`, since `min G_B=G_B(0)=0`.
This gives the matching liminf. Letting `epsilon` decrease to zero proves
(3). Substituting `B=C sqrt(log(1/delta)/delta)` into (3) and using the
monotonicity of approximation error in the window proves (4).

## Prior art, checks and evidence boundary

[NIST DLMF §6.12, equation (6.12.1)](https://dlmf.nist.gov/6.12.E1)
supplies the classical `E_1` expansion. The smallest-generator comparison is
proved directly by the absolutely convergent positive series in (6); no
prime-counting estimate or zero-free hypothesis is used.
[DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) supplies the classical minimax
framework. Shadrin's
[*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf),
§1.4, places the affine Chebyshev certificate in the classical extremal family.
The precise constrained certificate is proved in AF-586.

Wu--Yang,
[*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317),
§§2.1--2.2 and 3.3, provides the established approximation/moment-matching
framework. Dette--Titoff,
[*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912),
Theorem 2.1, connects discrimination design to uniform approximation under
a statistical design criterion. These are neighboring frameworks, not
theorems supplying the joint prime-source estimate (13) or its recovery
consequence. Searches by expanding-interval approximation, fixed degree,
exponential tails and prime-zeta asymptotics support this conservative
comparison; absence of an exact search match is not a priority claim.

The mathematical delta is the all-depth logarithmic estimate (10)--(13) and
the resulting unrestricted joint endpoint (3). The minimax witness and
curvature mechanism are reused from AF-586/589. Relative amplitude
equivalence is deliberately neither assumed nor needed, as (14) demonstrates.

A scratch-only standard-library Python `decimal` audit at 100-digit
precision checked (8) in 49 cases: seven prime pairs from neighboring to
widely separated labels, with exponents near one, fixed, logarithmic,
square-root, linear and quadratic in the smaller label. All sampled
inequalities passed. A separate 60-point check of the logarithm in (10)
used four pairs, `a=5,20,80`, and five interpolation parameters. The absolute
remainder divided by `1+log(s_0+1)+s_0/p+L(2/3)^s_0` was below `1.60` in
these samples. Source sums retained primes through 1000 and the edit labels;
the omitted positive series is bounded by `1000^(1-s)/(s-1)`.
`E_1` continued-fraction depths 512 and 1024 agreed to relative error below
`10^(-75)`. These are finite-precision consistency checks, not interval
certificates, actual minimax computations, or proofs of an asymptotic limit.
Equations (5)--(23) provide the analytic argument.

Fixed degree, common coordinate, one shared calibration per input and the
registered exact source are essential boundaries. The theorem gives no
second-order uniform expansion, growing-degree sharp constant, finite-bit
accuracy guarantee or common optimal multiway design. The absolute margin
still vanishes with remote edits. The controls are generalized-prime systems
indexed by rational-prime edit locations; this is not an ordinary-prime
provenance discriminator, zeta-zero exclusion or RH conclusion.
