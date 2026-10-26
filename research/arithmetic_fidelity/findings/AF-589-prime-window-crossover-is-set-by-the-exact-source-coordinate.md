# AF-589 — The prime-window crossover is set by the exact source coordinate

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · JOINT-LIMIT-CROSSOVER · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

The two different iterated recovery constants in
[[research/arithmetic_fidelity/findings/AF-588-fixed-prime-tail-changes-the-sharp-range-constant-and-limit-order|AF-588]]
are joined by an explicit **nonmonotone** crossover. In the intervening regime,
the polynomial quotient retains the exact prime-source coordinate at a finite
distance from its singular endpoint. Neither the universal peak profile nor the
smallest-generator tail alone determines the constant.

Use the registered generalized-prime controls
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_j(s)=j^{-s}-(j+1)^{-s},\quad Q_j=P-h_j,\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
 \tag{1}
\]
For odd rational primes `p<q`, set
\[
 L=\log p,\quad c=e^{B_1},\quad H=p^{-2}-q^{-2},\quad
 d(a)=\Phi_q(a)-\Phi_p(a),\quad D=\max_{a>0}d(a),
\]
\[
 g_{p,q}(x)=d(x/(cL))/D,\qquad
 \Delta_{r;p,q}(B)=1-2\operatorname{dist}_{C[0,B]}(g_{p,q},\Pi_r),
 \qquad \kappa_r=\frac{r^2}{2}\cot^2\frac{\pi}{2r}.
 \tag{2}
\]
Here `B_1` is the reciprocal-prime Meissel--Mertens constant, and `r>=2`
is a fixed supplied integer. Each input has one shared degree-at-most-`r`
polynomial calibration, with unrestricted coefficients, and arbitrary absolute
bounded errors. Competing labels may choose different calibrations. The
whole-window identification radius is
`D(1-Delta)/4`, as a supremum; the full-ray radius is `D/4`.
Continuity permits inclusion of the zero endpoint in the norm.

Define the increasing positive coordinate
\[
 \mathfrak a(z)=E_1^{-1}(P(1+z)),\qquad z>0,
 \qquad
 F(\tau)=\frac{c\,\mathfrak a(2\tau)}{2\tau}.
 \tag{3}
\]
Both inverses are real monotone inverses on their positive ranges.

**Joint-limit theorem.** For every sequence with `p->infinity`, `B->infinity`
and `log B/log p -> tau in (0,infinity)`, uniformly over all larger prime
labels `q>p`,
\[
 \boxed{\frac{B^2\Delta_{r;p,q}(B)}{\kappa_r\log B}
          \longrightarrow F(\tau).}
 \tag{4}
\]
Uniformity means that the limit holds for every such sequence of choices of
`q`; neither a relative prime-gap bound nor a restriction on `q/p` is needed.
The function satisfies
\[
 \boxed{F(0+)=1,\qquad F(+\infty)=c\log2,
             \qquad F(1/2)<c\log2<1.}
 \tag{5}
\]
In particular, interpolating monotonically between the two iterated constants
would give the wrong answer. For orientation, numerical evaluations give
`F(1/2)≈0.782361`, `F(1)≈0.739368`, and `F(2)≈0.723837`;
the strict inequality in (5) is proved separately below.

The crossover has only finitely many stationary points. It decreases strictly
for all sufficiently small positive `tau` and increases strictly for
`tau >= (1+2e)/(2 log 2)`. Every global minimizer lies strictly between zero
and that explicit upper threshold. Uniqueness of the minimum is not asserted.

There is an equivalent minimum-range consequence. Put
`R_(r;p,q)(delta)=inf{B>1:Delta_(r;p,q)(B)<=delta}`. If `delta->0`,
`p->infinity`, and `log(1/delta)/log p -> sigma in (0,infinity)`, then
\[
 \boxed{R_{r;p,q}(\delta)\sim
     \sqrt{\frac{\kappa_r F(\sigma/2)}2}
            \sqrt{\frac{\log(1/\delta)}{\delta}}.}
 \tag{6}
\]
The physical upper observation coordinate is this normalized range divided by
`c log p`. Thus polynomially small losses `delta=p^(-sigma+o(1))` have an
explicit source-dependent range constant, beyond AF-587's subpower regime.

## A compact-source relative estimate, uniform in the edit gap

Write
\[
 z(a)=P^{-1}(E_1(a))-1,\qquad a=\mathfrak a(z).
\]
For every fixed `a_0>0`, there are positive constants `C_-,C_+` and a starting
prime, depending only on `a_0`, such that for all `q>p` and `0<a<=a_0`,
\[
 \boxed{C_-e^{-Lz(a)}\le
       \frac{g_{p,q}(cLa)}{cLa}
       \le C_+e^{-Lz(a)}.}
 \tag{7}
\]
This relative bound survives to `a=0` and is stronger than absolute profile
convergence for the exponentially small tails used in (4).

Here is a direct derivation. Fix `M>1`, and restrict `1<s<=M`. For
`k=h_p-h_q`, the positive integral identity is
\[
 k(s)=s(s+1)\int_p^q\int_v^{v+1}u^{-s-2}\,du\,dv.
 \tag{8}
\]
Bounding the inner integral above by `v^(-s-2)` and below by
`(1+1/p)^(-s-2)v^(-s-2)` gives
\[
 s(1+1/p)^{-s-2}(p^{-s-1}-q^{-s-1})
 \le k(s)\le s(p^{-s-1}-q^{-s-1}).
\]
For `b=log(q/p)>0`,
\[
 1\le\frac{p^{-s-1}-q^{-s-1}}{H p^{-(s-1)}}
     =\frac{1-e^{-(s+1)b}}{1-e^{-2b}}
     \le\frac{s+1}{2}.
 \tag{9}
\]
The upper bound follows because `(1-e^(-tb))/t` decreases in `t>0`;
the lower bound uses `s+1>=2`. Thus
`k(s)` is bounded above and below by positive `M`-dependent multiples of
`H p^(-(s-1))`, uniformly even for neighboring labels.

Set `rho_j(s)=Q_j^{-1}(P(s))`. All these inverses exist on `(1,infinity)`:
`Q_j` is a positive decreasing Dirichlet series with limits infinity and zero.
The classical analytic regular part of `P` at one implies, on `1<u<=M`,
\[
 \frac{b_M}{u-1}\le-P'(u)\le\frac{B_M}{u-1}
 \tag{10}
\]
for some positive constants. Since `1<rho_j(s)<s` and
\[
 P(\rho_j(s))-P(s)=h_j(\rho_j(s))\le Mj^{-2},
\]
integration of (10) proves
\[
 0<s-\rho_j(s)\le C_M(s-1)/j^2.
 \tag{11}
\]
Indeed it first gives
`log((s-1)/(rho_j(s)-1))<=M/(b_M j^2)`.
Also `|h_p'(u)|<=C_M log p/p^2` throughout this interval, by differentiating
`h_p(u)=u integral_p^(p+1) v^(-u-1)dv`. Consequently, for every point `xi`
between `rho_p(s)` and `rho_q(s)`, `-Q_p'(xi)` is bounded above and below
by positive multiples of `1/(s-1)`, for sufficiently large `p`.

The exact mean-value identity is
\[
 \rho_q(s)-\rho_p(s)=\frac{k(\rho_q(s))}{-Q_p'(\xi)},
 \qquad \rho_p(s)<\xi<\rho_q(s).
 \tag{12}
\]
Differentiating (8) gives `|(log k)'|<=log(q+1)+2`. Apply (11) with
`j=q`, so that
\[
 \left|\log\frac{k(\rho_q(s))}{k(s)}\right|
       \le C_M\log(q+1)/q^2.
\]
This use of the larger label prevents an uncontrolled factor when `q/p` is
large. Combining (9)--(12) gives
\[
 \rho_q(s)-\rho_p(s)
       \asymp_M H(s-1)p^{-(s-1)},\qquad 1<s\le M.
 \tag{13}
\]
The constants in this notation are positive and independent of `p,q,s` in
the stated range.

At `s=1+z(a)`, the left side is exactly `d(a)`. The endpoint expansions give
`z(a)/a -> c` as `a->0`, so this ratio is bounded above and below on
`0<a<=a_0`. Finally,
[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]], equation (10), supplies
\[
 D=\frac{H}{eL}\{1+O(L^{-1})\},\qquad
 \|g_{p,q}-f\|_{[0,\infty)}=O(L^{-1}),\quad f(x)=xe^{1-x},
 \tag{14}
\]
uniformly in `q>p`. Divide (13) by `D cLa` to obtain (7). No subtraction
of individually estimated inverse responses or prime-counting error is used.

## The relative tail threshold determines the sharp deficit

Fix a sequence in (4), and fix `0<epsilon<2tau`. Define
\[
 a_-=\mathfrak a(2\tau-\epsilon),\quad
 a_+=\mathfrak a(2\tau+\epsilon),\qquad
 t_-=cLa_-,\quad t_+=cLa_+.
 \tag{15}
\]
They satisfy `t_±=Theta(L)=Theta(log B)=o(B)`. Equation (7) gives the two
decisive, quantitatively different statements:
\[
 \inf_{0<x\le t_-}\frac{g_{p,q}(x)}x
       \ge C_-e^{-(2\tau-\epsilon)L},\qquad
 \frac{g_{p,q}(t_+)}{t_+}
       \le C_+e^{-(2\tau+\epsilon)L}=o(B^{-2}).
 \tag{16}
\]
In the first inequality, `z(x/(cL))<=2tau-epsilon` by monotonicity.
Moreover `L B^(-2) e^((2tau-epsilon)L)->0`. These exponential separations
hold even when `log B-tau L` is unbounded but `o(L)`.

### Upper bound

Let `v_B` be a best approximant, `E_B` its error, and `V_B(y)=v_B(By)`.
The constant `1/2` gives `E_B<=1/2` and `||V_B||<=3/2`. At fixed degree,
pass along any sequence to a subsequence with coefficientwise limit `V`
and error limit `E`. By (14), every maximizer `m_p` of `g_(p,q)` tends to
one, and `g_(p,q)(By)->0` for each fixed `y>0`. Therefore
\[
 |V|\le1/2,\qquad E=1/2,\qquad V(0)=1/2,\qquad V'(0)=0.
 \tag{17}
\]
For completeness, the peak bound forces `V(0)>=1-E`, while the tail gives
`|V(0)|<=E`. The inequality
`V_B(m_p/B)-V_B(0)>=1-2E_B>=0` and the mean-value theorem give
`V'(0)>=0`; endpoint maximality gives the opposite inequality.

The constrained certificate in
[[research/arithmetic_fidelity/findings/AF-586-every-fixed-calibration-degree-has-an-explicit-sharp-range-constant|AF-586]], equations (4)--(7), now gives `V''(0)>=-kappa_r`.
Its proof writes the difference from the affine Chebyshev extremal as
`y^2 W(y)` and evaluates `W(0)` by signed Lagrange interpolation at the
remaining `r-1` alternating contacts. This uses the zero slope in (17),
rather than an unrestricted Markov constant.

Interpolate `v_B` at `m_p` between zero and `t_+`. Coefficient convergence
controls the second derivative uniformly on this shrinking rescaled interval,
giving
\[
 \Delta_{r;p,q}(B)\le
 \frac{m_p}{t_+}g_{p,q}(t_+)
 -\frac{m_p(t_+-m_p)}{2B^2}\{V''(0)+o(1)\}.
 \tag{18}
\]
Equations (16)--(18) imply
\[
 \limsup\frac{B^2\Delta_{r;p,q}(B)}{\kappa_r L}
       \le\frac{ca_+}{2}.
 \tag{19}
\]
The same compactness argument applies on every sequence.

### Matching whole-window witness

AF-586 supplies the fixed polynomial factorization
\[
 A_r(y)=\frac12+\frac12T_r(c_r-(1+c_r)y)
       =\alpha_r y^2H_r(y),\quad
 c_r=\cos(\pi/r),\quad\alpha_r=\kappa_r/2,
 \tag{20}
\]
where `0<=A_r<=1`, `H_r>=0`, and `H_r(0)=1` on `[0,1]`.
Put
\[
 \beta_p=\sup_{x\ge t_-}g_{p,q}(x),\quad
 \eta_p=\sqrt{\beta_p+L/B^2},\quad
 k_B=(1-\eta_p)\alpha_r/B^2,
\]
\[
 Q_B(x)=k_Bx(t_--x)H_r(x/B),\qquad G_B=g_{p,q}-Q_B.
 \tag{21}
\]
Whole-ray convergence in (14) gives `beta_p->0`, hence `eta_p->0`;
also `beta_p+L/B^2=o(eta_p)`.
For `0<x<=t_-`, (16) implies
\[
 0\le\frac{Q_B(x)}{g_{p,q}(x)}
       \le C_{r,\tau,\epsilon}\frac{L}{B^2}e^{(2\tau-\epsilon)L}=o(1).
 \tag{22}
\]
Thus `0<=G_B<=g_(p,q)` there eventually. For `t_-<=x<=B`,
\[
 -Q_B(x)=(1-\eta_p)(1-t_-/x)A_r(x/B)\in[0,1-\eta_p],
\]
so `0<=G_B<=1-eta_p+beta_p`. At an exact source peak `m_p->1`,
`G_B(m_p)=1-O_{r,\tau,\epsilon}(L/B^2)`, which is larger than that tail bound.
Every maximizer `x_p` of `G_B` therefore lies before `t_-`; since there
`G_B<=g_(p,q)` and its maximum tends to one, (14) forces `x_p->1`.
Writing `M_B=max G_B`, the squeeze
\[
 Q_B(x_p)\le1-M_B\le Q_B(m_p)
\]
and `Q_B(x)/(k_B t_-)->x` uniformly on bounded sets yield
\[
 1-M_B\sim k_Bt_-\sim\frac{\kappa_r ca_- L}{2B^2}.
 \tag{23}
\]
The polynomial `Q_B+M_B/2` has error exactly `M_B/2`, because
`min G_B=G_B(0)=0`. Hence (23) is a lower bound for the deficit.
Combining with (19) and letting `epsilon` decrease to zero proves (4),
using continuity of `mathfrak a` and `log B/L->tau`.

For (6), substitute `B=C sqrt(log(1/delta)/delta)` in (4).
Then `log B/L->sigma/2` and
`Delta(B)/delta -> kappa_r F(sigma/2)/(2C^2)`.
Monotonicity of best approximation error in the window, with constants `C`
on either side of the claimed value, brackets the minimum range. This does
not exchange an uncontrolled pair limit with a window limit.

## Endpoint matching and a strict undershoot

The classical expansions
\[
 P(1+z)=-\log z+B_1-\gamma+O(z),\qquad
 E_1(a)=-\log a-\gamma+O(a)
\]
give `mathfrak a(z)~z/c` at zero, and thus `F(0+)=1`.
At infinity, the smallest prime dominates:
`P(1+z)~2^(-1-z)`. Since `E_1(a)~e^(-a)/a`,
\[
 \mathfrak a(z)+\log\mathfrak a(z)
       =(1+z)\log2+o(1),\qquad
 \mathfrak a(z)/z\longrightarrow\log2.
 \tag{24}
\]
This proves the second endpoint in (5), matching AF-588's opposite iterated
limit. These are limits of the function `F` after (4); they do not assert
uniformity for an arbitrary sequence with `tau->infinity`.

The undershoot requires only a coarse rigorous inequality. The positive
prime series gives
\[
 P(2)>\frac14+\frac19+\frac1{25}=\frac{361}{900}>0.4.
\]
For `a=log2<1`, the alternating power series gives
\[
 E_1(a)<-\gamma-\log a+a-a^2/4+a^3/18<0.382.
 \tag{25}
\]
The last inequality follows already from
`0.6931<log2<0.6932`, `gamma>0.5772`, and `log(0.6931)>-0.367`.
Therefore `P(2)>E_1(log2)` and the decreasing inverse gives
`mathfrak a(1)<log2`. This proves `F(1/2)<c log2`.
The standard value `B_1≈0.2614972128` gives `c log2≈0.9003103806<1`.
Together with the endpoint limits, the strict undershoot proves
nonmonotonicity.

## The stationary-point problem is confined away from both endpoints

Write `a=mathfrak a(z)`, `ell=log 2`, and
\[
 M_j(z)=\sum_{p\ {\rm prime}}(\log p)^j p^{-1-z},\qquad z>0.
\]
These series and their derivatives converge locally uniformly. Implicit
differentiation of `E_1(a)=P(1+z)` gives the exact sign test
\[
 a'=a e^aM_1(z),\qquad
 F'(\tau)=\frac{2ca}{z^2}\{z e^aM_1(z)-1\},\qquad z=2\tau.
 \tag{26}
\]
Thus monotonicity of `P`, or its log-convexity alone, is not the derivative
inequality needed for this inverse-coordinate ratio.

At the singular endpoint, the next regular coefficient is
\[
 C_1=\gamma+\sum_{p\ {\rm prime}}\frac{\log p}{p(p-1)},\qquad
 P(1+z)=-\log z+B_1-\gamma+C_1z+O(z^2).
 \tag{27}
\]
To derive it without a prime-counting remainder, use the absolutely convergent
Euler-log identity
`P(s)=log zeta(s)-sum_(k>=2) P(ks)/k`. The latter sum is analytic near
`s=1`; its differentiated series is locally normally convergent, since it is
bounded by a convergent series of multiples of `log n/n^(2-epsilon)`.
The Laurent expansion of zeta gives the linear coefficient `gamma` of its
logarithmic regular part, and summing the geometric prime-power tails gives
(27). This is a classical coefficient, not a new prime-zeta constant.

The `E_1` power series and the analytic implicit function theorem, applied to
`a/z` after cancelling `-log z`, now give
\[
 \mathfrak a(z)=c^{-1}z\{1+(c^{-1}-C_1)z+O(z^2)\},\qquad
 F'(0+)=2(c^{-1}-C_1)<0.
 \tag{28}
\]
The sign does not rely on decimal evaluation of `C_1`. Indeed the same
Euler-log identity gives
\[
 B_1=\gamma-\sum_p\sum_{k\ge2}\frac{p^{-k}}k
 >\gamma-\sum_{n\ge2}\{-\log(1-1/n)-1/n\}
 =2\gamma-1>0,
\]
where the integer sum telescopes to `1-gamma`. Also
`C_1 > gamma+(log 2)/2+(log 3)/6 > 1`, using just
`gamma>0.57`, `log 2>0.69` and `log 3>1.09`. Therefore
`c^(-1)<1<C_1`. Analyticity of the regular expansion makes `F'` strictly
negative on some positive interval, rather than merely providing a negative
secant slope. No explicit size for that initial interval is claimed.

There is a simple explicit tail cutoff. For every `a>0`,
\[
 \frac1{a+1}<e^aE_1(a)<\frac1a.
 \tag{29}
\]
The integral `e^aE_1(a)=integral_0^infinity e^(-v)/(a+v)dv` proves the
upper bound directly and the strict lower bound by Jensen's inequality for
the exponential probability density. These are weaker than the classical
bounds in [DLMF (6.8.2)](https://dlmf.nist.gov/6.8.E2).
Put `b=z ell`. For `b>=1+2e`,
\[
 E_1(b-1)<\frac{e e^{-b}}{b-1}\le\tfrac12e^{-b}
       <P(1+z)=E_1(a).
\]
The decreasing inverse implies `a<b-1`. Since `M_1(z)>=ell P(1+z)`,
\[
 z e^aM_1(z)\ge b e^aE_1(a)>\frac b{a+1}>1.
 \tag{30}
\]
Equation (26) therefore proves strict increase for
`tau >= (1+2e)/(2 log 2)`; the endpoint is included. This cutoff is sufficient,
not sharp, and uses only positivity and the smallest prime for its tail step.

The two endpoint signs imply that all stationary points belong to a compact
subinterval of `(0,(1+2e)/(2 log 2))`. The function `F` is real analytic on
`(0,infinity)` because both defining functions are real analytic with
nonzero derivatives. Its derivative cannot have infinitely many zeros in that
compact interval without vanishing identically. Hence there are finitely many
stationary points. The strict undershoot in (5), together with both endpoint
limits, ensures that the global minimum is attained; (28)--(30) put every
minimizer strictly inside the stated interval.

For the remaining interior question, at a stationary point define
`G(z)=z e^aM_1(z)-1`. Differentiating before imposing `G=0` gives
\[
 G'(z)=\frac{1+a}{z}-\frac{M_2(z)}{M_1(z)}\quad\hbox{when }G(z)=0.
 \tag{31}
\]
Strict positivity of the right side at every root would force a unique root
and hence a unique global minimum: every crossing would be upward, while the
endpoint signs are opposite. Neither positivity of the prime terms nor
`M_2 M_0>=M_1^2` proves that inequality. Equations (26)--(31) confine and
specify the unresolved test; a sampled minimum does not settle it.

## Prior art, checks and evidence boundary

The minimax/alternation framework is classical; see
[NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i).
The affine Chebyshev extremal belongs to the classical family described in
Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.4.
AF-586 supplies the exact constrained certificate used here. Wu--Yang,
[*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317),
Theorem 3.3.4 and its proof, treat finite-interval approximation of Poisson
kernels for moment-matched mixtures. Dette--Titoff,
[*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912),
Theorem 2.1, supplies the established discrimination/approximation connection.
These are neighboring mechanisms, not imported theorems for (4).

[DLMF (6.6.2)](https://dlmf.nist.gov/6.6.E2) and
[(6.12.1)](https://dlmf.nist.gov/6.12.E1) provide the exponential-integral
expansions; [DLMF (5.2.3)](https://dlmf.nist.gov/5.2.E3) records Euler's
constant. Fröberg's prime-zeta source is already anchored in `SOURCES.md`;
Kawalec's [recent-preprint equations (2)--(4)](https://arxiv.org/html/2603.21535v1)
display the classical analytic regular part used in (10). Only this local
analytic input is used. The compact-source estimates and the crossover proof
above use no zero-free-region assumption.

For (27), [DLMF (25.2.4)](https://dlmf.nist.gov/25.2.E4) supplies the
classical Laurent expansion; Kawalec's equation (14) identifies the same
linear coefficient. The positive prime-power derivation above is independent
of that preprint's conditional prime-counting remainder. DLMF (6.8.2)
supplies neighboring sharper exponential-integral bounds. The derivative
confinement is an application of classical inverse calculus and these
inequalities to this registered crossover, not a new general monotonicity
theorem. It leaves the number of interior turning points unresolved.

The substantive delta is the compact-source relative estimate (7), the sharp
joint transition (4), its strict undershoot, and the finite interior
stationary-point restriction (26)--(31). The joint transition was explicitly
left outside AF-587/588. No new Chebyshev family, general approximation
principle, or theorem-priority claim based on search absence is asserted.

A scratch-only standard-library Python `decimal` audit at 75-digit precision
checked (9)'s resulting two-sided bound for `k(s)/(H p^(-(s-1)))` in 20 cases:
four edit pairs from neighboring to widely separated labels, and five real
exponents from `1.00001` to `8`. All passed. Numerical values of `F` were
computed with the Möbius/log-zeta formula through index 150, Euler--Maclaurin
zeta evaluation with 64 summands and 18 corrections, the `E_1` power series,
and real bisection. They give `F(0.001)≈0.998878`, `F(0.1)≈0.913803`,
`F(5)≈0.743636`, and `F(20)≈0.816871`, consistent with the proved endpoint
and undershoot statements. These are finite-precision consistency checks,
not interval certificates, actual minimax computations, or a proof of a
unique crossover minimum. Equations (7)--(25) supply the analytic argument.

A separate scratch-only `decimal` check at 55-digit precision used the primes
up to `10000` and the `E_1` power series. At `z=2,4,6,10`, the implicit
derivative of the finite-prime inverse agreed with a centered difference of
step `10^(-10)` to absolute error below `2*10^(-23)`, and (29) held.
The omitted positive series tails admit the integer-integral bounds
`N^(-z)/z` and `N^(-z)(log N/z+1/z^2)` for `M_0` and `M_1`, respectively,
at these parameters. This is a finite-prefix consistency check, not an
interval certificate for (31), a count of stationary points, or a proof of
uniqueness. Equations (26)--(30) give the endpoint sign proofs independently.

The theorem retains fixed degree and a positive finite limiting ratio
`log B/log p`. It gives neither a uniform supercritical joint limit nor
growing-degree sharp constants, finite-bit accuracy, or a common optimal
multiway design. Extra observations within the same window cannot exceed its
whole-window radius. The source controls remain generalized-prime systems
indexed by rational-prime edit locations, with a vanishing absolute margin;
this result supplies no ordinary-prime provenance discriminator, zeta-zero
exclusion or RH conclusion.
