# AF-588 — Fixed-prime tails change the sharp range constant and limit order

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · NONCOMMUTING-LIMITS · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

The near-full recovery law of
[[research/arithmetic_fidelity/findings/AF-587-logarithmic-tail-control-transfers-sharp-range-below-the-profile-error|AF-587]]
does not extend with the same constant to arbitrary observation ranges. Keeping the prime-edit pair fixed and sending the window to infinity gives a different coefficient. The retained source quantities are its **first global peak location** and its **far-tail exponential rate**, rather than its normalized peak profile alone.

Use the registered generalized-prime controls
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_j(s)=j^{-s}-(j+1)^{-s},\quad Q_j=P-h_j,\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\qquad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
 \tag{1}
\]
Fix odd rational primes `p<q`, and define
\[
 d(a)=\Phi_q(a)-\Phi_p(a),\quad D=\max_{a>0}d(a),\quad
 a_* =\min\{a>0:d(a)=D\},\quad
 \nu_p=\frac{\log(p/2)}{\log2}>0.
 \tag{2}
\]
The maximum exists and `a_*>0`; uniqueness is not assumed. For a fixed supplied degree `r>=2`, let
\[
 E^{\rm phys}_{r;p,q}(A)=\operatorname{dist}_{C[0,A]}(d/D,\Pi_r),
 \qquad \Delta^{\rm phys}_{r;p,q}(A)=1-2E^{\rm phys}_{r;p,q}(A),
 \qquad \kappa_r=\frac{r^2}{2}\cot^2\frac{\pi}{2r}.
 \tag{3}
\]
There is one unrestricted-coefficient polynomial calibration per input, shared across that input's observations, and an arbitrary absolute error bounded by `epsilon`. Different labels can choose different calibrations. The supremal whole-window unique-identification radius is `D E^{phys}/2`, and the full-ray radius is `D/4`. The continuous zero endpoint does not alter the observation norm on `0<a<=A`.

**Fixed-pair theorem.** With `p,q,r` fixed, as `a->infinity` and `A->infinity`, respectively,
\[
 \boxed{d(a)\sim\frac{E_1(a)^{\nu_p}}{\log2}
       \sim\frac{a^{-\nu_p}e^{-\nu_p a}}{\log2},\qquad
 \Delta^{\rm phys}_{r;p,q}(A)
       \sim\kappa_r\frac{a_*}{\nu_p}\frac{\log A}{A^2}.}
 \tag{4}
\]
Consequently the least physical window attaining fractional loss at most `delta` satisfies
\[
 \boxed{\inf\{A>0:\Delta^{\rm phys}_{r;p,q}(A)\le\delta\}
 \sim\sqrt{\frac{\kappa_r a_*}{2\nu_p}}
                \sqrt{\frac{\log(1/\delta)}{\delta}}.}
 \tag{5}
\]
These are pointwise asymptotics in the pair, not a uniform large-prime theorem.

To compare with AF-586/587 in exactly the same coordinate, let `B_1` be the reciprocal-prime Meissel--Mertens constant, put `c=exp(B_1)`, `L=log p`, and
\[
 g_{p,q}(x)=d(x/(cL))/D,\qquad
 \Delta_{r;p,q}(B)=1-2\operatorname{dist}_{C[0,B]}(g_{p,q},\Pi_r).
\]
Dilation preserves the polynomial space. For each fixed pair,
\[
 K_{p,q}:=\lim_{B\to\infty}
 \frac{B^2\Delta_{r;p,q}(B)}{\kappa_r\log B}
       =\frac{c^2L^2a_*}{\nu_p}.
 \tag{6}
\]
For every choice of larger prime `q=q(p)>p`, the two iterated limits are
\[
 \boxed{\lim_{p\to\infty}\lim_{B\to\infty}
 \frac{B^2\Delta_{r;p,q(p)}(B)}{\kappa_r\log B}
       =e^{B_1}\log2\simeq0.900310380639,}
 \tag{7}
\]
\[
 \boxed{\lim_{B\to\infty}\lim_{p\to\infty}
 \frac{B^2\Delta_{r;p,q(p)}(B)}{\kappa_r\log B}=1.}
 \tag{8}
\]
Thus the order dependence occurs for the actual registered source, even though its normalized profiles converge uniformly on the entire positive ray. No transition formula when `log B` is comparable with `log p` is asserted.

## Recovery from a positive profile with a prescribed tail rate

Here is the reusable statement. Suppose `g` is continuous on `[0,infinity)`, strictly positive on `(0,infinity)`, and
\[
 g(0)=0,\quad \max g=1,\quad
 \lim_{x\downarrow0}g(x)/x\in(0,\infty),\quad
 \lim_{x\to\infty}\frac{-\log g(x)}x=\lambda\in(0,\infty).
 \tag{9}
\]
Let `m=min{x:g(x)=1}`. The peak set is nonempty and compact, so `m>0`. For every fixed `r>=2`,
\[
 \boxed{1-2\operatorname{dist}_{C[0,B]}(g,\Pi_r)
       \sim\kappa_r\frac m\lambda\frac{\log B}{B^2}.}
 \tag{10}
\]
Neither differentiability nor unimodality is required. The exact earliest maximizer matters if several peaks attain the same height.

For every fixed `0<epsilon<lambda/4`, positivity, the two endpoint limits and compactness supply constants `b_-,b_+>0` such that, for every `x>0`,
\[
 b_-x e^{-(\lambda+\epsilon)x}\le g(x)
       \le b_+x e^{-(\lambda-\epsilon)x}.
 \tag{11}
\]
Indeed the corresponding ratios tend to positive limits at zero; at infinity the lower-envelope ratio tends to infinity and the upper-envelope ratio tends to zero. This uses a relative tail condition; uniform closeness to another profile does not imply it.

### Upper bound: peak, tail and constrained curvature

Let `v_B` be a best degree-at-most-`r` approximant, `E_B` its error, and `V_B(y)=v_B(By)`. The constant `1/2` gives `E_B<=1/2` and `||V_B||<=3/2`. At fixed degree the coefficients are bounded. Along any sequence one can pass to a subsequence with coefficientwise convergence `V_B->V` and `E_B->E`.

For fixed `y>0`, `g(By)->0`, so `|V(y)|<=E`. Continuity includes zero. At the fixed peak, `v_B(m)>=1-E_B`, hence `V(0)>=1-E`. Therefore `E=1/2` and `V(0)=1/2`. Also
\[
 V_B(m/B)-V_B(0)\ge1-2E_B\ge0.
\]
The mean-value theorem gives `V'(0)>=0`; the bound `V<=1/2` to the right gives the opposite inequality. Thus
\[
 |V|\le1/2,\qquad V(0)=1/2,\qquad V'(0)=0.
 \tag{12}
\]
The exact constrained-curvature certificate of
[[research/arithmetic_fidelity/findings/AF-586-every-fixed-calibration-degree-has-an-explicit-sharp-range-constant|AF-586]], equations (4)--(7), gives `V''(0)>=-kappa_r`. Its extremal is
\[
 V_r^*(y)=-\tfrac12T_r(c_r-(1+c_r)y),\qquad c_r=\cos(\pi/r).
 \tag{13}
\]
That certificate follows by writing `V-V_r^*=y^2W` and evaluating its Lagrange interpolant at zero on the remaining `r-1` alternating contacts; every weighted term has nonnegative sign. This is a constrained bound, not the unrestricted Markov constant.

Choose `s_B=(2 log B+2 log log B)/(lambda-epsilon)`. Eventually `m<s_B<B`. Interpolation at the peak between zero and `s_B` yields
\[
 1-2E_B\le\frac m{s_B}g(s_B)
       -\frac{m(s_B-m)}{2B^2}\{V''(0)+o(1)\}.
 \tag{14}
\]
Coefficient convergence justifies the second-derivative remainder uniformly on `0<=x<=s_B`; no rate for `V_B->V` is assumed. By (11), the first term is at most `m b_+/[B^2(log B)^2]`. Hence
\[
 \limsup_{B\to\infty}\frac{B^2(1-2E_B)}{\log B}
       \le\frac{\kappa_r m}{\lambda-\epsilon}.
 \tag{15}
\]
The compactness argument applies on every sequence.

### Lower bound: one whole-window witness and selection of the first peak

AF-586 also gives the polynomial factorization
\[
 A_r(y)=\tfrac12-V_r^*(y)=\alpha_r y^2H_r(y),\quad
 \alpha_r=\kappa_r/2,\quad H_r(0)=1,\quad H_r\ge0,
 \quad0\le A_r\le1\quad(0\le y\le1).
 \tag{16}
\]
Fix `C_r>=max(1,||H_r||)`, and write `lambda_+=lambda+epsilon`, `lambda_-=lambda-epsilon`. Set
\[
 \eta_B=B^{-1/2},\quad k_B=(1-\eta_B)\alpha_r/B^2,\quad
 t_B=\lambda_+^{-1}\log\frac{e\lambda_+ b_-}{k_B C_r},\quad
 Q_B(x)=k_Bx(t_B-x)H_r(x/B).
 \tag{17}
\]
For large `B`, `t_B~2 log B/lambda_+`, `0<t_B<B`, and `Q_B in Pi_r`. On `0<x<=t_B`,
\[
 0\le\frac{Q_B(x)}{g(x)}
 \le\frac{k_B C_r}{b_-}(t_B-x)e^{\lambda_+x}
 \le\frac{k_B C_r}{b_-\lambda_+}e^{\lambda_+t_B-1}=1.
 \tag{18}
\]
On `t_B<=x<=B`, instead,
\[
 -Q_B(x)=(1-\eta_B)(1-t_B/x)A_r(x/B)\in[0,1-\eta_B].
 \tag{19}
\]
The upper envelope in (11) implies
\[
 \sup_{x\ge t_B}g(x)
 =O(\log B\,B^{-2\lambda_-/\lambda_+})=o(\eta_B),
 \tag{20}
\]
since `2lambda_-/lambda_+>6/5`. Thus `G_B=g-Q_B` is nonnegative on the whole window, is at most `g` before `t_B`, and is at most `1-eta_B+o(eta_B)` after it. At the first source peak,
\[
 G_B(m)=1-Q_B(m)=1-O(\log B/B^2).
\]
Every maximizer `x_B` of `G_B` therefore lies before `t_B`. Writing `M_B=max G_B`, we have `M_B->1` and `g(x_B)>=M_B`. Since `g` vanishes at infinity, these maximizers stay in a compact set and all their accumulation points belong to the peak set of `g`.

The decisive squeeze is
\[
 Q_B(x_B)\le1-M_B\le Q_B(m).
 \tag{21}
\]
On every bounded set, `Q_B(x)/(k_B t_B)->x` uniformly. Every accumulation point of `x_B` is at least `m`, while the right side of (21), divided by `k_Bt_B`, tends to `m`. It follows that `x_B->m` and
\[
 1-M_B\sim m k_Bt_B
       \sim\frac{\kappa_r m}{\lambda+\epsilon}\frac{\log B}{B^2}.
 \tag{22}
\]
Because `min G_B=G_B(0)=0`, the polynomial `Q_B+M_B/2` has error exactly `M_B/2`. Therefore `1-2E_B>=1-M_B`. Combine (15) and (22), then let `epsilon` decrease to zero, to prove (10). Monotonicity of best approximation error and substitution of `B=C sqrt(log(1/delta)/delta)` give the corresponding range constant `sqrt(kappa_r m/(2lambda))`.

## The fixed arithmetic source has exactly the required endpoints

Positivity can be checked without estimating a difference of inverse errors. Interpolate the sources by
\[
 Q_\tau=(1-\tau)Q_p+\tau Q_q,\quad k=h_p-h_q>0,\quad
 s_\tau(a)=Q_\tau^{-1}(E_1(a)),\quad0\le\tau\le1.
\]
Here `h_j(s)=s integral_j^(j+1) u^(-s-1)du` decreases strictly with `j`. All `Q_tau` are decreasing positive Dirichlet series mapping `(1,infinity)` onto `(0,infinity)`, and
\[
 d(a)=\int_0^1\frac{k(s_\tau(a))}{-Q_\tau'(s_\tau(a))}\,d\tau>0.
 \tag{23}
\]
This is the exact interpolation identity used in
[[research/arithmetic_fidelity/findings/AF-579-unbounded-query-locations-preserve-polynomial-budget-obstruction|AF-579]].

At the left endpoint, the classical prime-zeta regular part and exponential-integral series give
\[
 P(1+z)=-\log z+B_1-\gamma+O(z),\qquad
 E_1(a)=-\log a-\gamma+O(a).
\]
The analytic implicit equation, or direct substitution into these expansions, yields
\[
 \Phi_j(a)=1+c e^{-h_j(1)}a+O_j(a^2),\qquad
 d(a)/a\longrightarrow c\{e^{-h_q(1)}-e^{-h_p(1)}\}>0.
 \tag{24}
\]
These expansions are unconditional near the real side of `s=1`; AF-583 records the analytic remainder justification.

At the other endpoint, every interpolated source retains generator `2` with coefficient one. Absolute convergence at a fixed real `sigma_0>1` bounds the remaining terms and their first derivatives uniformly in `tau`:
\[
 Q_\tau(s)=2^{-s}\{1+O((2/3)^s)\},\qquad
 -Q_\tau'(s)=(\log2)2^{-s}\{1+O((2/3)^s)\}.
 \tag{25}
\]
For the **fixed** pair, `k(s)=p^{-s}(1+o(1))`. Put `s_0(a)=-log E_1(a)/log2`. Equation (25) gives
\[
 s_\tau(a)=s_0(a)+o(1),\qquad
 \frac{k(s_\tau(a))}{-Q_\tau'(s_\tau(a))}
       =\frac{(2/p)^{s_0(a)}}{\log2}\{1+o(1)\},
 \tag{26}
\]
uniformly in `tau`. The fixed exponent `log(p/2)` is essential when replacing `s_tau` by `s_0(a)` in the relative estimate. Integrating (26) proves the first asymptotic in (4). The classical `E_1(a)~e^{-a}/a` proves the second.

Thus `g=d/D` satisfies (9) with `m=a_*` and `lambda=nu_p`. Its two vanishing endpoints, positivity and continuity give an attained positive maximum and a first maximizer. Applying (10) proves the remaining part of (4) and (5). Only constants can approximate a bounded source with finite uniform error on the entire ray, so the distance there is `D/2` and the noise radius is `D/4`, as used above.

## Why the orders of limits differ

[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]], equation (10), proves
\[
 \|g_{p,q}-f\|_{[0,\infty)}=O(1/\log p),\qquad f(x)=xe^{1-x},
 \tag{27}
\]
uniformly in `q>p`. Since `f` has unique maximum one at one and vanishes at both endpoints, every maximizer of `g_{p,q}` tends to one, uniformly. In particular `cL a_*->1`. Substitution in (6) gives
\[
 K_{p,q}=(cL a_*)\frac{cL\log2}{L-\log2}\longrightarrow c\log2,
\]
which proves (7). For each fixed `B`, distance to the fixed polynomial subspace is 1-Lipschitz in the uniform norm. Equation (27) therefore gives `Delta_{r;p,q}(B)->Delta_r(B)`, and AF-586's sharp formula gives (8).

The difference is structural, not an inconsistent change of units. In the coordinate `x=cLa`, the far-tail rate of a fixed source is `nu_p/(cL)`, which tends to `1/(c log2)` as the edit location escapes. The limiting profile `f` instead has rate one. Whole-ray **absolute** convergence in (27) can discard this relative far-tail distinction. The polynomial quotient tests the tail at distances of order `log B`, where that discarded distinction changes the leading deficit. AF-587 controls this test only in its stated `log B=o(log p)` regime.

## Controls, prior art and evidence boundary

The elementary dilation control `g(x)=f(x/a)` has `m=a`, `lambda=1/a`, and predicts coefficient `kappa_r a^2`, agreeing with exact dilation of AF-586. More sharply, `g(x)=max(f(x),f(x/3))` has equal global peaks at one and three, tail rate `1/3`, and coefficient `3kappa_r`; using the later peak would incorrectly give `9kappa_r`. This continuous, non-arithmetic example satisfies every hypothesis of (9) and tests the peak-selection step without assuming unimodality. The single profile `f(x/3)` does have coefficient `9kappa_r`.

Minimax polynomial approximation and alternation are classical; see [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i). The constrained affine Chebyshev polynomial (13) belongs to the classical extremal framework surveyed by Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.4; AF-586 supplies the precise finite certificate used here. Wu--Yang, [*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317), Theorem 3.3.4 and its proof, treat finite-interval approximation of the Poisson kernels `e^{-x}x^j/j!` for moment-matched mixtures. This is close target-family prior art, but its mixture bound does not provide (10) or the iterated-limit comparison. Dette--Titoff, [*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912), supplies the established discrimination/approximation connection, with a statistical design criterion distinct from the deterministic bounded-error radius here.

[DLMF §6.6, equation (6.6.2)](https://dlmf.nist.gov/6.6.E2), and [§6.12, equation (6.12.1)](https://dlmf.nist.gov/6.12.E1), supply the classical `E_1` endpoint expansions. Fröberg's prime-zeta source is already recorded in `SOURCES.md`; Kawalec's [recent-preprint equations (2)--(4)](https://arxiv.org/html/2603.21535v1) explicitly display the local regular part used in (24). The far-tail comparison (25)--(26) is proved directly from the positive Dirichlet series, without a prime-counting estimate or a zero-free hypothesis. No novelty is claimed for these analytic ingredients, the Chebyshev family, or general approximation theory. The retained result is (10), its fixed-source instantiation, and the resulting failure to exchange the two recovery limits.

A scratch-only Python `decimal` audit at 110-digit precision checked whole-window witness inequalities at 21,610 sampled points for the one- and two-peak controls, degrees `2,3,4`, and `B=10^6,10^12,10^24`. Local peak optimization gave two-peak witness-loss/predicted-loss ratios `0.979854,0.990398,0.995200` for degree two and `0.865998,0.933415,0.966708` for degree four; the selected peak approached one. A separate fixed-source tail check used the Dirichlet series over primes up to 1000 for pairs `(3,5)` and `(11,13)`. At `a=5,10,20,40`, the ratios `d(a)log2/E_1(a)^nu_p` were respectively `0.914076,0.993282,0.999928,0.999999987` and `0.438377,0.749708,0.941015,0.995835`. The integer-tail estimate `1000^(1-s)/(s-1)` makes the omitted-tail inverse-shift bound less than `3.3e-17` of the computed gap in these cases. Decimal roundoff was not interval-certified. These are consistency checks of the derived witness and source asymptotic, not exact minimax computations, continuum numerical proofs or a substitute for (11)--(26).

The theorem needs strict source positivity, a linear nonzero left endpoint and a finite positive logarithmic tail rate. It does not assert the same law for interior zeros, faster/slower tails, growing degree, independently recalibrated probes, finite-bit implementations, or one common optimal design for a multiway source set. The pointwise constants and starting windows can depend on `p,q`; (7) is an iterated limit and cannot be promoted to an unspecified joint limit. The matched controls remain generalized-prime systems indexed by rational-prime edit locations. No ordinary-prime provenance discriminator, zeta-zero exclusion or RH conclusion follows.
