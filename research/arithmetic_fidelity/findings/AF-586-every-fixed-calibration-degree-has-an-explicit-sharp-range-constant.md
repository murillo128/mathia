# AF-586 — Every fixed calibration degree has an explicit sharp range constant

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · SHARP-FIXED-DEGREE-CLASSIFICATION · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

For the binary sources `0` and `f(x)=x exp(1-x)` on `0<x<=B`, each input has one shared real polynomial calibration of known degree at most `r`, with unrestricted coefficients, and an arbitrary absolute error bounded by `epsilon`. Different source labels may choose different calibrations. Define
\[
 E_r(B)=\inf_{p\in\Pi_r}\|f-p\|_{C[0,B]},\qquad
 \Delta_r(B)=1-2E_r(B),\qquad
 R_r(\delta)=\inf\{B>1:\Delta_r(B)\le\delta\}.
 \tag{1}
\]
Continuity at zero preserves the observation norm. The supremal whole-window unique-identification radius is `E_r(B)/2`; the full-ray radius is `1/4`. Thus `Delta_r` is the fractional loss of noise margin. These are the same experiment and normalization as
[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]].

**Theorem.** For every **fixed** integer `r>=2`, put
\[
 c_r=\cos(\pi/r),\qquad
 \kappa_r=\frac{r^2}{2}\frac{1+c_r}{1-c_r}
          =\frac{r^2}{2}\cot^2\!\frac{\pi}{2r}.
\]
Then
\[
 \boxed{\Delta_r(B)\sim\kappa_r\frac{\log B}{B^2},\qquad
 R_r(\delta)\sim\frac r2\cot\!\frac{\pi}{2r}
                 \sqrt{\frac{\log(1/\delta)}{\delta}}.}
 \tag{2}
\]
If `p_B` is the best degree-at-most-`r` approximant, then coefficientwise, and hence with every fixed derivative on `[0,1]`,
\[
 \boxed{p_B(By)\longrightarrow
 P_r^*(y)=-\frac12T_r\big(c_r-(1+c_r)y\big).}
 \tag{3}
\]
Here `T_r(cos theta)=cos(r theta)` is the classical Chebyshev polynomial.

This closes the fixed-degree leading-constant question left by AF-583 and
[[research/arithmetic_fidelity/findings/AF-585-cubic-calibration-has-sharp-range-constant-from-endpoint-curvature|AF-585]]. It reproduces `kappa_2=2` and `kappa_3=27/2`, and gives, for example, `kappa_4=8(3+2 sqrt(2))`. One interpolation certificate and one whole-window construction handle all fixed degrees; separate higher-degree alternation equations are unnecessary. The proof is not uniform in growing `r` and does not replace AF-584's uniform order theorem.

## A finite certificate for the endpoint curvature

Consider the constrained class
\[
 \mathcal C_r=\{P\in\Pi_r:\ |P|\le1/2\text{ on }[0,1],\quad
                    P(0)=1/2,\quad P'(0)=0\}.
\]
Its exact extremum is
\[
 \boxed{P''(0)\ge-\kappa_r\quad(P\in\mathcal C_r),}
 \tag{4}
\]
with equality only for `P=P_r^*`.

First, the argument of `T_r` in (3) ranges from `c_r` to `-1`, so `P_r^*` belongs to the class. At `c_r`, `T_r=-1` and `T_r'=0`. Differentiating the trigonometric identity, or using
`(1-z^2)T_r''-z T_r'+r^2 T_r=0`, gives
\[
 (P_r^*)''(0)=-\frac{(1+c_r)^2r^2}{2(1-c_r^2)}=-\kappa_r.
 \tag{5}
\]

For the converse, let `D=P-P_r^*`. The two endpoint conditions imply `D(y)=y^2 V(y)` with `V in Pi_(r-2)`. Use the `r-1` distinct positive nodes
\[
 y_j=\frac{c_r-\cos(j\pi/r)}{1+c_r},\qquad j=2,\ldots,r.
 \tag{6}
\]
They satisfy `0<y_2<...<y_r=1` and
`P_r^*(y_j)=(-1)^(j+1)/2`. The norm constraint therefore says
\[
 (-1)^jD(y_j)\ge0.
\]
Lagrange interpolation of `V` at these nodes, evaluated at zero, gives
\[
 V(0)=\sum_{j=2}^r\ell_j(0)\frac{D(y_j)}{y_j^2},\qquad
 \ell_j(0)=\prod_{\substack{2\le k\le r\\k\ne j}}
                         \frac{-y_k}{y_j-y_k}.
 \tag{7}
\]
The sign of `ell_j(0)` is `(-1)^(j-2)=(-1)^j`, so every summand is nonnegative. Hence `D''(0)=2V(0)>=0`, proving (4). Equality forces every summand to vanish. Then `V`, of degree at most `r-2`, has `r-1` distinct zeros, so `V=0`. This also proves uniqueness. For `r=2`, the product is empty and equals one, and the argument remains valid.

This is a classical interpolation/alternation mechanism. The zero slope is a hypothesis of this general-degree lemma, not a consequence of endpoint maximality alone. Its validity for the approximation problem is proved next.

## Why every limiting approximant has those endpoint constraints

Write `P_B(y)=p_B(By)`. The constant `1/2` is admissible, so `E_r(B)<=1/2` and `||P_B||<=3/2`. At fixed degree, values at `r+1` fixed distinct nodes bound all coefficients. Consequently any sequence `B->infinity` has a subsequence on which `E_r(B)->E` and `P_B->P` coefficientwise.

For each fixed `y>0`, `f(By)->0`, so `|P(y)|<=E`. Continuity includes zero. At the source peak,
\[
 P_B(1/B)\ge1-E_r(B).
\]
Thus `P(0)>=1-E`, and `|P(0)|<=E<=1/2` forces `E=1/2` and `P(0)=1/2`. In particular the full sequence satisfies `E_r(B)->1/2`.

Also `p_B(0)<=E_r(B)`, whence
\[
 P_B(1/B)-P_B(0)\ge\Delta_r(B)\ge0.
\]
The mean-value theorem and coefficient convergence imply `P'(0)>=0`. Since `P(0)=1/2` and `P<=1/2` on the right, `P'(0)<=0`. Therefore `P in C_r`.

For a subsequence with limit `P`, choose `s_B=2 log B+log log B`. Uniformly for `0<=x<=s_B`,
\[
 p_B''(x)=B^{-2}\{P''(0)+o(1)\}.
\]
Linear interpolation of `p_B` between zero and `s_B`, evaluated at one, gives
\[
 p_B(1)=(1-s_B^{-1})p_B(0)+s_B^{-1}p_B(s_B)
                 -\tfrac12(s_B-1)p_B''(\xi_B)
\]
for some `0<xi_B<s_B`. Using the three approximation bounds yields
\[
 \Delta_r(B)\le e^{1-s_B}
      -\frac{s_B-1}{2B^2}\{P''(0)+o(1)\}.
 \tag{8}
\]
Since `e^(1-s_B)=e/(B^2 log B)`, equations (4) and (8) prove
\[
 \limsup_{B\to\infty}\frac{B^2\Delta_r(B)}{\log B}\le\kappa_r.
 \tag{9}
\]
This argument does not assume finite-window alternation nodes, a zero finite-window slope, or a rate of convergence of `P_B`.

## One polynomial witness controls the entire window

Set
\[
 A_r(y)=\frac12-P_r^*(y),\qquad \alpha_r=\kappa_r/2.
\]
Then `0<=A_r<=1`, and the double zero at zero gives the polynomial factorization
\[
 A_r(y)=\alpha_r y^2 H_r(y),\qquad
 H_r\in\Pi_{r-2},\quad H_r(0)=1,\quad H_r\ge0\text{ on }[0,1].
 \tag{10}
\]
Choose any fixed finite `C_r>=max(1, ||H_r||_[0,1])`; the sum of the absolute monomial coefficients of `H_r` is one explicit choice.

For sufficiently large `B`, define
\[
 \eta_B=B^{-1/2},\quad k_B=(1-\eta_B)\alpha_r/B^2,\quad
 t_B=2+\log\frac1{k_B C_r},
\]
\[
 Q_B(x)=k_B x(t_B-x)H_r(x/B),\qquad G_B(x)=f(x)-Q_B(x).
 \tag{11}
\]
Here `Q_B in Pi_r`, `1<t_B<B`, and `t_B=2 log B+O_r(1)`.

For `0<x<=t_B`,
\[
 0\le\frac{Q_B(x)}{f(x)}
   =k_B(t_B-x)H_r(x/B)e^{x-1}
   \le k_B C_r e^{t_B-2}=1,
 \tag{12}
\]
using the maximum of `(t-x)e^(x-1)` on `[0,t]`, attained at `t-1` when `t>1`. Thus `0<=G_B<=f` throughout this interval, including its continuous zero endpoint.

For `t_B<=x<=B`, the equivalent expression
\[
 -Q_B(x)=(1-\eta_B)(1-t_B/x)A_r(x/B)
\]
gives `0<=-Q_B<=1-eta_B`. Because `f` decreases after one,
\[
 0\le G_B(x)\le1-\eta_B+f(t_B)
      =1-\eta_B+t_B k_B C_r/e.
 \tag{13}
\]
On the other hand,
\[
 G_B(1)=1-k_B(t_B-1)H_r(1/B)=1-O_r(\log B/B^2).
\]
Since `k_B t_B=o(eta_B)`, the bound in (13) is eventually below `G_B(1)`. Therefore a maximizer `x_B` of `G_B` lies in `[0,t_B]`. There `G_B<=f<=1`, while `G_B(1)->1`, so the unique peak and vanishing tail of `f` force `x_B->1`.

Let `M_B=max G_B`. Now
\[
 \frac{Q_B(x_B)}{k_Bt_B}
  =x_B(1-x_B/t_B)H_r(x_B/B)\longrightarrow1.
\]
The inequalities `M_B<=1-Q_B(x_B)` and `M_B>=G_B(1)` give
\[
 1-M_B\sim k_Bt_B\sim\kappa_r\frac{\log B}{B^2}.
 \tag{14}
\]
Equations (12)--(13) prove `min G_B=G_B(0)=0`, so the polynomial `Q_B+M_B/2` has error exactly `M_B/2`. Consequently `Delta_r(B)>=1-M_B`. This and (9) prove the first formula in (2).

Applying (8) to any subsequential limit now forces `P''(0)=-kappa_r`. The uniqueness in (4) forces `P=P_r^*`; compactness then proves (3) for the full sequence. The witness is asymptotically optimal, not asserted to be the exact best polynomial at finite `B`.

Finally `E_r(B)` is nondecreasing, so `Delta_r(B)` is nonincreasing. Substituting `B=C sqrt(log(1/delta)/delta)` in the first formula of (2) gives `Delta_r(B)/delta -> kappa_r/(2C^2)`. Bracketing with constants on either side of `sqrt(kappa_r/2)` proves the range formula.

## Arithmetic instance and the exact scope of transfer

Use the registered generalized-prime edit controls
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 Q_j(s)=P(s)-j^{-s}+(j+1)^{-s},\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
\]
For odd rational-prime labels `p<q`, let
`D_(p,q)=sup_(a>0)(Phi_q-Phi_p)(a)` and `c=exp(B_1)`, with `B_1` the reciprocal-prime Meissel--Mertens constant. AF-583, equation (10), proves the gap-relative source estimate
\[
 \left\|\frac{(\Phi_q-\Phi_p)(x/(c\log p))}{D_{p,q}}
                       -f(x)\right\|_{(0,\infty)}
           \le C_0/\log p,
 \tag{15}
\]
uniformly over `q>p`. This previously derived estimate is the arithmetic input; no new prime-counting assertion is needed here.

Let `Delta_(r;p,q)(B)` be the fractional loss from the actual full-ray radius `D_(p,q)/4`, restricting observations to `0<a<=B/(c log p)` with one shared degree-at-most-`r` polynomial per input. Dilation preserves the polynomial subspace, and distance to a fixed subspace is 1-Lipschitz, so
\[
 |\Delta_{r;p,q}(B)-\Delta_r(B)|\le2C_0/\log p.
 \tag{16}
\]
Thus for each fixed `r>=2`, in the joint limit `delta->0`, `p->infinity` with `delta log p -> infinity`,
\[
 \boxed{R_{r;p,q}(\delta)\sim\frac r2\cot\!\frac{\pi}{2r}
                    \sqrt{\frac{\log(1/\delta)}{\delta}},}
 \tag{17}
\]
uniformly in `q>p`. Indeed (16) sandwiches the minimum normalized range between `R_r(delta+2C_0/log p)` and `R_r(delta-2C_0/log p)`. The physical endpoint is (17) divided by `c log p`. The scale condition is sufficient, not asserted necessary.

The whole-window radius bounds every policy confined to that window. Classical alternation supplies `r+2` fixed probes approaching it: the normalized divided-difference weights annihilate `Pi_r`, have total variation one, and attain contrast `E_r(B)`. Strict noise allowances below `E_r(B)/2` are therefore attainable. A zero alternation node can be moved to a positive coordinate with a vanishing loss. This inherited duality does not establish a common optimal design for multiway source sets or a finite-bit implementation.

## Prior art, checks, and remaining boundary

Chebyshev polynomials, their trigonometric representation, polynomial alternation, and signed Lagrange interpolation are classical. See [NIST DLMF §18.5(i)](https://dlmf.nist.gov/18.5.E1), [DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i), and Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), especially §1.4 on Zolotarev polynomials and affine Chebyshev extremals. Equation (3) is an affine Chebyshev extremal with its first retained stationary point placed at the left endpoint; it is not a new polynomial family. The constrained certificate (4)--(7) is proved explicitly rather than inferred from the unrestricted Markov bound.

Wu--Yang, [*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317), Theorem 3.3.4 and its proof, already treat polynomial approximation of the Poisson kernels `exp(-x)x^j/j!` on finite intervals. Their mixture comparison bound does not state the fixed-degree half-range deficit in (2). The discrimination/approximation connection is also established prior art, including Dette--Titoff, [*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912). The retained contribution is the proved all-fixed-degree sharp constant, limiting shape, and calibrated-source transfer for the present experiment. No theorem-level priority claim is based on a failed wording search.

A scratch-only standard-library Python `decimal` audit used 90-digit precision and degrees `2,3,4,5,8,12`. It checked the curvature formula, contact values, signs and monomial reproduction of (7), and (12)--(13) at endpoints, contact nodes, peak/tail points, and two 250-point meshes for each of `B=10^8,10^12,10^20`: 9,248 sampled/certificate checks passed. With `C_r` chosen as the absolute coefficient sum, bisection at the witness's local peak gave loss/predicted-loss ratios approaching one; for degree four they were `0.898603,0.932459,0.959476`, and for degree twelve `0.498511,0.665705,0.799423`. The slower approach at larger degree reflects the conservative fixed witness constant. These are numerical normalization/falsification checks, not interval certificates, exact minimax computations, or substitutes for the continuum proof.

The theorem requires fixed supplied degree, one shared calibration, a common coordinate, and absolute bounded errors. The asymptotic relation `kappa_r~2r^4/pi^2` as `r->infinity` is an algebraic consequence of the formula; exchanging that degree limit with the window limit is **not** justified by this proof. Exact finite-window alternation locations, second-order terms, growing-degree sharp constants, and quotient-specific improvements to (15) remain outside the result.

The non-arithmetic analytic control already realizes the range obstruction. The arithmetic transfer concerns generalized-prime matched controls indexed by rational-prime edit locations, with vanishing absolute margins. It does not certify ordinary-prime provenance, exclude any zeta zero, or imply RH.
