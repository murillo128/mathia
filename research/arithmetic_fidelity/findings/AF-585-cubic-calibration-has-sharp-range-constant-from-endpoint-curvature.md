# AF-585 — Cubic calibration has a sharp range constant from endpoint curvature

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · SHARP-RANGE-CONSTANT · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

Retain the binary observation experiment of
[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]]:
the sources are `0` and `f(x)=x exp(1-x)` on `0<x<=B`, each input has one shared polynomial calibration of known degree at most three, and errors are arbitrary functions bounded in absolute value. Competing labels may choose different calibrations. Put
\[
 E_3(B)=\inf_{p\in\Pi_3}\|f-p\|_{C[0,B]},\qquad
 \varepsilon_3(B)=E_3(B)/2,\qquad
 \Delta_3(B)=1-2E_3(B).
 \tag{1}
\]
The continuous extension to zero leaves the norm unchanged. The supremal whole-window unique-identification radius is `epsilon_3`; the factor two is the intersection threshold of two bounded-error balls. The full-ray radius is `1/4`, because only constant polynomials stay bounded against `f`, whose range has closure `[0,1]`.

**Theorem.** As `B->infinity`,
\[
 \boxed{\Delta_3(B)\sim\frac{27}{2}\frac{\log B}{B^2}.}
 \tag{2}
\]
Consequently, if `R_3(delta)=inf{B>1: Delta_3(B)<=delta}`, then
\[
 \boxed{R_3(\delta)\sim\frac{3\sqrt3}{2}
          \sqrt{\frac{\log(1/\delta)}{\delta}},
          \qquad\delta\downarrow0.}
 \tag{3}
\]
If `p_B` is the best cubic approximant, its rescaled polynomial converges coefficientwise, and hence with all derivatives on `[0,1]`, to
\[
 \boxed{p_B(By)\longrightarrow
 P_*(y)=\frac12-\frac{27}{4}y^2(1-y)
       =-\frac12T_3\!\left(\frac{1-3y}{2}\right).}
 \tag{4}
\]
Here `T_3(z)=4z^3-3z`. This is a classical affinely transformed Chebyshev polynomial. Its appearance is not a new polynomial family.

AF-583 and
[[research/arithmetic_fidelity/findings/AF-584-growing-calibration-degree-has-sharp-quadratic-range-cost|AF-584]]
establish the fixed- and growing-degree orders but leave higher-degree sharp coefficients open. Equations (2)--(4) settle the cubic coefficient and identify the extremal geometry responsible for it. Compared with the sharp quadratic coefficient `2` from AF-582, the margin-loss coefficient increases by `27/4`, and the required range increases by `3 sqrt(3)/2`. The order remains unchanged.

## The constrained endpoint curvature

The sharp constant comes from a smaller polynomial class than the unconstrained Markov inequality sees.

**Lemma.** If `P in Pi_3`, `|P|<=1/2` on `[0,1]`, and `P(0)=1/2`, then
\[
 P''(0)\ge-27/2.
 \tag{5}
\]
Equality holds only for `P=P_*`.

Write `P(y)=1/2+d y+a y^2+b y^3`. Endpoint maximality gives `d<=0`. The two values at `1` and `2/3` give
\[
 d+a+b\le0,\qquad \frac23d+\frac49a+\frac8{27}b\ge-1.
\]
Combining them yields
\[
 -1\le\frac23d+\frac49a+\frac8{27}b
       \le\frac{10}{27}d+\frac4{27}a,
 \qquad a\ge-27/4-5d/2\ge-27/4.
 \tag{6}
\]
Equality in (5) forces `d=0`, both value constraints to be tight, and `b=27/4`. Conversely,
`max_[0,1] y^2(1-y)=4/27`, attained at `2/3`, proves that `P_*` satisfies the full interval constraint. This proves the lemma, including uniqueness, without importing a sharper derivative inequality.

The endpoint saturation is load-bearing: `-T_3(1-2y)/2` satisfies the same norm bound but has endpoint second derivative `-48` and value `-1/2`, so it is outside the lemma. Zero slope need not be assumed in (5); it follows at equality. A general norm bound alone does not select this extremal.

## Every best approximant enters that constrained class

Let `P_B(y)=p_B(By)`. Since the constant `1/2` is admissible, `E_3(B)<=1/2`, and therefore `||P_B||_[0,1]<=3/2`. Values at four fixed distinct points bound all four coefficients by a fixed inverse Vandermonde matrix. Hence every sequence `B->infinity` has a subsequence along which `E_3(B)->E` and `P_B->P` coefficientwise.

For each fixed `y>0`, `f(By)->0`, so `|P(y)|<=E`; continuity gives the same bound at zero. At the source peak,
\[
 P_B(1/B)=p_B(1)\ge1-E_3(B).
\]
Coefficient convergence therefore gives `P(0)>=1-E`. Together with `|P(0)|<=E` and `E<=1/2`, this forces
\[
 E=1/2,\qquad P(0)=1/2.
 \tag{7}
\]
In particular `E_3(B)->1/2` for the full sequence. Also `p_B(0)<=E_3(B)`, whence
\[
 P_B(1/B)-P_B(0)\ge1-2E_3(B)\ge0.
\]
The mean-value theorem and coefficient convergence give `P'(0)>=0`. Since `P(0)` is the maximum allowed value on the right-hand interval, `P'(0)<=0`. Thus `P'(0)=0`, and the lemma applies to every subsequential limit.

This argument does not assume that zero is an exact finite-`B` alternation node or that the finite-`B` slope vanishes. It proves the required constraints only after rescaling and taking the limit.

## Sharp upper bound for the deficit

On a subsequence with limit `P(y)=1/2+a y^2+b y^3`, set
\[
 s_B=2\log B+\log\log B.
\]
For sufficiently large `B`, `1<s_B<B`, and coefficient convergence implies
\[
 p_B''(x)=\frac{2a+o(1)}{B^2}
 \quad\text{uniformly for }0\le x\le s_B.
 \tag{8}
\]
The interpolation remainder at `x=1` between `0` and `s_B` gives, for some `xi in (0,s_B)`,
\[
 p_B(1)=\left(1-\frac1{s_B}\right)p_B(0)
     +\frac{p_B(s_B)}{s_B}
     -\frac{s_B-1}{2}p_B''(\xi).
\]
Use `p_B(1)>=1-E_3`, `p_B(0)<=E_3`, and `p_B(s_B)<=E_3+f(s_B)`. Then
\[
 \Delta_3(B)\le e^{1-s_B}
       -\{a+o(1)\}\frac{s_B-1}{B^2}.
 \tag{9}
\]
Here `e^(1-s_B)=e/(B^2 log B)`. Multiplying (9) by `B^2/log B` gives subsequential upper limit at most `-2a<=27/2`. Compactness covers every sequence, so
\[
 \limsup_{B\to\infty}\frac{B^2\Delta_3(B)}{\log B}\le27/2.
 \tag{10}
\]
The shrinking source layer enforces a saturated endpoint with zero slope in the macroscopic limit. That extra constraint, rather than the generic degree-three Markov constant, is load-bearing.

## A cubic witness matching the constant over the whole window

For sufficiently large `B`, define
\[
 \eta=B^{-1/2},\qquad
 c_B=\frac{27}{4B^2}(1-\eta),\qquad
 t_B=2+\log(1/c_B),
\]
\[
 Q_B(x)=c_B x(t_B-x)(1-x/B),\qquad
 H_B(x)=f(x)-Q_B(x).
 \tag{11}
\]
We have `1<t_B<B` and `t_B=2 log B+O(1)`.

For `0<x<=t_B`, `Q_B>=0`, and
\[
 \frac{Q_B(x)}{f(x)}
 =c_B(t_B-x)(1-x/B)e^{x-1}
 \le c_B e^{t_B-2}=1.
 \tag{12}
\]
The elementary maximum used here is
`max_[0,t] (t-x)e^(x-1)=e^(t-2)` for `t>1`. Thus `0<=H_B<=f` on `[0,t_B]`, including the zero endpoint.

For `t_B<=x<=B`, `Q_B<=0`, and the same extremal cubic from the lemma gives
\[
 0\le-Q_B(x)
   =c_B x(x-t_B)(1-x/B)
   \le c_B x^2(1-x/B)\le1-\eta.
\]
Since `f` is decreasing after one,
\[
 0\le H_B(x)\le1-\eta+f(t_B)
       =1-\eta+c_Bt_B/e.
 \tag{13}
\]
This is a whole-window bound, including the macroscopic negative lobe and the final endpoint. Because `c_Bt_B=o(eta)`, (13) is eventually smaller than
\[
 H_B(1)=1-c_B(t_B-1)(1-1/B).
 \tag{14}
\]

Let `M_B=max_[0,B] H_B` and choose a maximizing point `x_B`. Equations (13)--(14) place it in `[0,t_B]`. There `H_B<=f<=1`, while `M_B>=H_B(1)->1`. The profile has a unique maximum at one and tends to zero at infinity, so `x_B->1`. Consequently
\[
 \frac{Q_B(x_B)}{c_Bt_B}
   =x_B(1-x_B/t_B)(1-x_B/B)\longrightarrow1.
\]
Using `f(x_B)<=1` gives
`1-M_B>=Q_B(x_B)=(1+o(1))c_Bt_B`, while (14) gives the reverse asymptotic inequality. Hence
\[
 1-M_B\sim c_Bt_B\sim\frac{27}{2}\frac{\log B}{B^2}.
 \tag{15}
\]
Equations (12)--(13) establish `min H_B=H_B(0)=0`. The explicit cubic `Q_B+M_B/2` therefore has uniform error `M_B/2`, so `Delta_3(B)>=1-M_B`. Combined with (10), this proves (2). This witness is asymptotically extremal; it is not asserted to be the exact best cubic at finite `B`.

Finally, (2) and the subsequential inequality (9) force every limit coefficient `a` to equal `-27/4`. The equality case of (6) then forces `b=27/4`. Thus all subsequential limits equal `P_*`, proving (4). Its macroscopic minimum at `y=2/3` is the additional tail geometry behind the larger cubic coefficient. No exact finite-window alternation positions or second-order asymptotic expansion are asserted.

## Range inversion, finite probes, and the arithmetic instance

The error `E_3(B)` is nondecreasing with the interval, so `Delta_3(B)` is nonincreasing. At `B=C sqrt(log(1/delta)/delta)`, equation (2) gives
\[
 \frac{\Delta_3(B)}{\delta}\longrightarrow\frac{27}{4C^2}.
\]
Constants just below and above `3 sqrt(3)/2` bracket the minimum range and prove (3).

Whole-window failure obstructs every adaptive policy confined to that window. Conversely classical alternation supplies five fixed nodes whose divided-difference weights annihilate `Pi_3`. Normalizing these weights to total variation one gives contrast magnitude `E_3(B)` and noise cost at most `epsilon`; hence every strict radius below `E_3(B)/2` is attainable. If a node is zero, move it to a positive coordinate and take the limit. Four or fewer deterministic adaptive queries cannot guarantee identification even without noise: feed a fixed transcript and interpolate each label's required nuisance with a cubic. These are deterministic statements; ideal continuously randomized zero-noise validation is a different experiment.

For the concrete registered controls, let
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 Q_j(s)=P(s)-j^{-s}+(j+1)^{-s},\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
\]
For odd rational-prime edit labels `p<q`, put
`D_(p,q)=sup_(a>0)(Phi_q-Phi_p)(a)` and `c=exp(B_1)`, where `B_1` is the reciprocal-prime Meissel--Mertens constant. AF-583, equation (10), supplies
\[
 \left\|\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}}
                   -f(x)\right\|_{(0,\infty)}
       \le C_0/\log p,
 \tag{16}
\]
uniformly over `q>p`. This is an existing source estimate, not a new assertion of derivative convergence. The exact full-ray radius is `D_(p,q)/4`. If `Delta_(3;p,q)(B)` denotes the fractional loss from that radius on `0<a<=B/(c log p)`, invariance of `Pi_3` under dilation and the 1-Lipschitz property of distance to a fixed subspace imply
\[
 |\Delta_{3;p,q}(B)-\Delta_3(B)|\le2C_0/\log p.
 \tag{17}
\]
Thus, in the simultaneous limit `delta->0`, `p->infinity`, with `delta log p->infinity`, the minimum normalized prime range obeys
\[
 \boxed{R_{3;p,q}(\delta)\sim\frac{3\sqrt3}{2}
                 \sqrt{\frac{\log(1/\delta)}{\delta}},}
 \tag{18}
\]
uniformly in the larger prime label. Indeed (17) sandwiches that range between `R_3(delta+2C_0/log p)` and `R_3(delta-2C_0/log p)`. The physical endpoint is (18) divided by `c log p`. The scale condition is sufficient, not asserted necessary. These are the exact limiting source curves; no simultaneous finite-critical-index estimate is added.

## Prior art, validation, and evidence boundary

The approximation/discrimination dictionary, alternation and divided-difference dual certificates are classical; see [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) and Dette--Titoff, [*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912). Shadrin's [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §§1.1 and 1.4, supplies the surrounding derivative-extremal and Zolotarev theory, including affine images of Chebyshev polynomials. The elementary lemma (5) is proved here; its cubic and its general extremal-polynomial setting are not claimed new.

Wu--Yang, [*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317), Theorem 3.3.4 and its proof, explicitly approximate `exp(-x)x^j/j!` on `[0,Lambda]`. Thus even the profile family is established approximation-theoretic material. That theorem controls a sum of approximation errors for Poisson-mixture comparison, with useful bounds when degree is large relative to the interval; it does not supply (2)'s fixed-cubic deficit from half-range error as the interval diverges. The contribution retained here is the proved sharp coefficient and limiting shape for this registered source-discrimination experiment, not a general approximation or priority claim.

A scratch-only 70-digit Python `decimal` check evaluated (11)--(14) at 4,833 points across `B=10^3,10^4,10^6,10^8,10^12,10^20`, including both endpoints, the moving tail point, its neighboring critical scale, the peak, and the macroscopic lobe. All nonnegativity, upper-bound and tail-slack checks passed. Bisection of the witness's local peak gave loss coefficients `(1-M_B)B^2/log B` approximately `12.2302,12.7111,13.0430,13.1654,13.2778,13.3667`, consistent with `13.5`. Exact rational arithmetic separately checked the endpoint certificate and Chebyshev identity. These are normalization and falsification checks, not interval-certified numerical proofs or computations of the exact minimax error. The continuum proof is (5)--(15).

The result assumes one shared unrestricted-coefficient cubic, a common coordinate, and absolute bounded noise. It does not address unknown degree, independently recalibrated probes, relative error, bit complexity, a common optimal multiway design, or sharp constants for degree four and above. The finite-probe statements are supremal and require strict noise allowances for uniqueness.

The analytic control already exhibits the obstruction. The arithmetic instance concerns generalized-prime matched controls indexed by rational-prime edit locations, with remotely vanishing absolute margins. It does not identify ordinary-prime provenance, exclude any zeta zero, or imply RH.
