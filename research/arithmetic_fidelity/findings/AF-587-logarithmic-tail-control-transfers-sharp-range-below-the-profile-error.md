# AF-587 — Logarithmic tail control transfers sharp range below the profile error

## Status and claim

EXACT-DERIVED · LITERATURE+DERIVED · POLYNOMIAL-NUISANCE · RELATIVE-TAIL-TRANSPORT · PRIME-EDIT-MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

The absolute uniform source error in
[[research/arithmetic_fidelity/findings/AF-583-fixed-polynomial-degrees-share-algebraic-range-order|AF-583]]
is not the necessary accuracy scale for transferring the sharp fixed-degree range law of
[[research/arithmetic_fidelity/findings/AF-586-every-fixed-calibration-degree-has-an-explicit-sharp-range-constant|AF-586]].
A relative exponential envelope up to a logarithmic tail distance suffices, even when the observation window extends much farther and the global profile error exceeds the target margin loss.

Use the registered generalized-prime edit curves
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 Q_j(s)=P(s)-j^{-s}+(j+1)^{-s},\quad
 \Phi_j(a)=Q_j^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\,du/u.
\]
For odd rational-prime labels `p<q`, set
\[
 L=\log p,\quad c=e^{B_1},\quad
 D_{p,q}=\sup_{a>0}(\Phi_q-\Phi_p)(a),\quad
 g_{p,q}(x)=\frac{(\Phi_q-\Phi_p)(x/(cL))}{D_{p,q}},
 \tag{1}
\]
where `B_1` is the reciprocal-prime Meissel--Mertens constant. For a fixed supplied integer `r>=2`, define
\[
 E_{r;p,q}(B)=\inf_{v\in\Pi_r}\|g_{p,q}-v\|_{C[0,B]},\qquad
 \Delta_{r;p,q}(B)=1-2E_{r;p,q}(B),
\]
\[
 R_{r;p,q}(\delta)=\inf\{B>1:\Delta_{r;p,q}(B)\le\delta\},\qquad
 \kappa_r=\frac{r^2}{2}\cot^2\!\frac{\pi}{2r}.
 \tag{2}
\]
The experiment permits one shared degree-at-most-`r` polynomial calibration per input, with unrestricted coefficients, and arbitrary absolute bounded errors. Competing source labels can choose different calibrations. The whole-window radius is `D_(p,q) E_(r;p,q)(B)/2`, and the full-ray radius is exactly `D_(p,q)/4`; thus `Delta` is the fractional loss. Continuity permits inclusion of the unobserved zero endpoint in the norm.

**Theorem.** Along every sequence with `p->infinity`, `B->infinity`, and
\[
 \boxed{\log B=o(\log p),}
 \tag{3}
\]
we have, uniformly over all larger prime labels `q>p`,
\[
 \boxed{\Delta_{r;p,q}(B)\sim\kappa_r\frac{\log B}{B^2}.}
 \tag{4}
\]
Consequently, for `delta->0`, `p->infinity`, and
\[
 \boxed{\log(1/\delta)=o(\log p),}
 \tag{5}
\]
\[
 \boxed{R_{r;p,q}(\delta)\sim
 \frac r2\cot\!\frac{\pi}{2r}
 \sqrt{\frac{\log(1/\delta)}{\delta}},}
 \tag{6}
\]
uniformly in `q>p`. The physical upper observation coordinate is (6) divided by `c log p`.

The sufficient condition (5) includes every `delta=(log p)^(-A)` for fixed `A>0`, and `delta=exp(-(log p)^theta)` for `0<theta<1`. In particular it permits `delta log p -> 0`, excluded by the previous sufficient transport argument. Neither (3) nor (5) is asserted necessary. Growing degree, the regime `log B` comparable to `log p`, and fixed-prime limits are outside this theorem.

## A reusable robustness lemma

Let `B_n->infinity` and let `g_n` be continuous nonnegative functions on `[0,infinity)` satisfying

- `g_n(0)=0`, `max g_n=1`, and `g_n(x)->0` as `x->infinity` for each `n`;
- `||g_n-f||_[0,infinity)->0`, where `f(x)=x exp(1-x)`;
- for every fixed `0<epsilon<1/2`, eventually throughout `0<x<=5 log B_n`,
\[
 e^{-(1+\epsilon)x}\le\frac{g_n(x)}x
       \le e^2 e^{-(1-\epsilon)x}.
 \tag{7}
\]
No rate relating the global uniform convergence to `log B_n/B_n^2` is assumed. Then for each fixed `r>=2`,
\[
 1-2\operatorname{dist}_{C[0,B_n]}(g_n,\Pi_r)
       \sim\kappa_r\frac{\log B_n}{B_n^2}.
 \tag{8}
\]
The two-sided envelope in (7) is extra structure, not a consequence of uniform convergence. The number five is only a convenient fixed bound for the tail locations used below.

### Upper bound from endpoint curvature

Suppress the index `n`. Let `v_B` be a best approximant, `E_B` its error, and `V_B(y)=v_B(By)`. A constant `1/2` gives `E_B<=1/2`, and `||V_B||_[0,1]<=3/2`. Fixed-degree coefficient compactness permits a subsequence with `V_B->V` coefficientwise and `E_B->E`.

Any maximizer `m_n` of `g_n` tends to one: uniform convergence to the uniquely peaked `f` excludes both fixed distance from one and escape to infinity. For every fixed `y>0`, `g_n(B_n y)->0`. Hence `|V(y)|<=E`, including at zero by continuity. At the peak,
\[
 v_B(m_n)\ge1-E_B,
\]
so `V(0)>=1-E`, which forces `E=1/2` and `V(0)=1/2`. Moreover,
\[
 v_B(m_n)-v_B(0)\ge1-2E_B\ge0.
\]
Applying the mean-value theorem in the `y` coordinate and coefficient convergence gives `V'(0)>=0`; endpoint maximality gives `V'(0)<=0`. Therefore
\[
 |V|\le1/2,\qquad V(0)=1/2,\qquad V'(0)=0.
 \tag{9}
\]
AF-586 proves the sharp constrained curvature bound
\[
 V''(0)\ge-\kappa_r,
 \tag{10}
\]
with unique extremal
`V_r^*(y)=-T_r(c_r-(1+c_r)y)/2`, `c_r=cos(pi/r)`. Its proof uses the sign-definite Lagrange certificate for `(V-V_r^*)/y^2` at the remaining `r-1` Chebyshev contacts; no unrestricted Markov constant is substituted for (10).

Fix `epsilon` in (7), and take
\[
 s_B=\frac{2\log B+2\log\log B}{1-\epsilon}<5\log B.
\]
Eventually `m_n<s_B<B`. Linear interpolation between zero and `s_B`, evaluated at `m_n`, gives
\[
 1-2E_B\le \frac{m_n}{s_B}g_n(s_B)
 -\frac{m_n(s_B-m_n)}{2B^2}\{V''(0)+o(1)\}.
 \tag{11}
\]
Indeed the second-derivative remainder is
`-m_n(s_B-m_n) v_B''(xi)/2`; coefficient convergence and `s_B/B->0` give the displayed derivative. The first term in (11) is at most
`m_n e^2/[B^2(log B)^2]` by (7). Thus (10) implies
\[
 \limsup\frac{B^2(1-2E_B)}{\log B}
       \le\frac{\kappa_r}{1-\epsilon}.
 \tag{12}
\]
Every subsequence admits the same compactness argument, so this is a full limsup bound.

### A witness with enough slack for the uncontrolled far tail

AF-586 supplies
\[
 A_r(y)=\frac12-V_r^*(y)
       =\alpha_r y^2 H_r(y),\qquad \alpha_r=\kappa_r/2,
 \tag{13}
\]
where `0<=A_r<=1`, `H_r` is a nonnegative polynomial on `[0,1]` of degree at most `r-2`, and `H_r(0)=1`. Fix `C_r>=max(1,||H_r||_[0,1])`.

Define
\[
 \beta_n=\sup_{x\ge\log B_n}g_n(x),\qquad
 \eta_n=\sqrt{\beta_n+\log B_n/B_n^2}.
 \tag{14}
\]
Uniform convergence implies `beta_n->0`, hence `eta_n->0`, and
`beta_n+log B_n/B_n^2=o(eta_n)`. This is where the whole-ray convergence is used; its rate need not be smaller than the target loss.

For fixed `epsilon` put `lambda=1+epsilon` and
\[
 k_B=(1-\eta_n)\alpha_r/B^2,\qquad
 t_B=\lambda^{-1}\log\frac{e\lambda}{k_B C_r},\qquad
 Q_B(x)=k_B x(t_B-x)H_r(x/B).
 \tag{15}
\]
Eventually `log B<t_B<5 log B<B`, and
`t_B~2 log B/(1+epsilon)`.
For `0<x<=t_B`, (7) gives
\[
 0\le\frac{Q_B(x)}{g_n(x)}
 \le k_B C_r(t_B-x)e^{\lambda x}
 \le\frac{k_B C_r}{\lambda}e^{\lambda t_B-1}=1.
 \tag{16}
\]
The middle maximum is at `x=t_B-1/lambda`, which lies in the interval for large `B`. Thus `G_B=g_n-Q_B` is nonnegative and at most `g_n` there.

For `t_B<=x<=B`, (13) instead gives
\[
 -Q_B(x)=(1-\eta_n)(1-t_B/x)A_r(x/B),\qquad
 0\le G_B(x)\le1-\eta_n+\beta_n.
 \tag{17}
\]
At an exact source peak `m_n->1`,
\[
 G_B(m_n)=1-Q_B(m_n)=1-O_r(\log B/B^2).
\]
By (14), this exceeds the upper bound in (17) eventually. Therefore every maximizer `x_n` of `G_B` over `[0,B]` lies in `[0,t_B]`. There `G_B<=g_n`, while its maximum tends to one, so uniform convergence to `f` forces `x_n->1`.

Writing `M_B=max G_B`, the exact normalization `g_n<=1` gives
\[
 Q_B(x_n)\le1-M_B\le Q_B(m_n),\qquad
 \frac{Q_B(x_n)}{k_Bt_B}\to1,\quad
 \frac{Q_B(m_n)}{k_Bt_B}\to1.
 \tag{18}
\]
Also `min G_B=G_B(0)=0`, by (16)--(17). The degree-at-most-`r` polynomial `Q_B+M_B/2` therefore has error `M_B/2`, yielding
\[
 \liminf\frac{B^2(1-2E_B)}{\log B}
       \ge\frac{\kappa_r}{1+\epsilon}.
 \tag{19}
\]
Letting the arbitrary fixed `epsilon` decrease to zero in (12) and (19) proves (8). It is not necessary to differentiate `g_n`, locate its exact finite-window alternation set, or approximate its far tail to the scale of the final deficit.

## The prime source satisfies the logarithmic envelope

AF-583 proves, uniformly in `q>p`,
\[
 \|g_{p,q}-f\|_\infty=O(L^{-1}),\qquad
 D_{p,q}=\frac{H}{eL}\{1+O(L^{-1})\},\qquad
 H=p^{-2}-q^{-2}.
 \tag{20}
\]
The gap is positive, continuous, zero at both limiting endpoints, and has a positive attained maximum. Thus the first two hypotheses of the lemma hold.

For the stronger local information, use AF-583's gap-relative inverse estimate, rather than subtracting individual response asymptotics. Let
`rho_j(s)=Q_j^{-1}(P(s))` and define `a(z)` by `E_1(a(z))=P(1+z)`. For `0<z<=z_0` with fixed small `z_0`, that finding proves
\[
 \rho_q(1+z)-\rho_p(1+z)
       =Hz e^{-Lz}\{1+O(z+p^{-1})\},\qquad
 ca(z)=z\{1+O(z)\}.
 \tag{21}
\]
The constants are independent of `q>p`, including neighboring labels. The relative estimate follows from the positive double integral for
`[p^(-s)-(p+1)^(-s)]-[q^(-s)-(q+1)^(-s)]`, its inverse-displacement bound, and the analytic regular part of `P` near one. There is no cancellation of two separately estimated small responses.

Set `u=Lz` and `x=cLa(z)`. Then
\[
 u=x\{1+O(x/L)\},\qquad |u-x|=O(x^2/L).
\]
After dividing (21) by the **exact** maximum in (20), taking logarithms gives
\[
 \boxed{\log\frac{g_{p,q}(x)}x
   =1-x+O\!\left(\frac{1+x+x^2}{L}+\frac1p\right).}
 \tag{22}
\]
This is uniform for `0<x<=5 log B` whenever `log B=o(L)`. To see the endpoint control explicitly, the logarithm contains `log(u/x)`, which is `O(x/L)` even as `x` decreases to zero, together with the relative error `O(z+1/p)` and the peak-normalization error `O(1/L)`.

For every fixed `epsilon>0`, the error in (22) has absolute value at most `1+epsilon x` on this interval eventually: the constant part tends to zero and the remaining coefficient of `x` is `O((1+log B)/L)`. Exponentiation gives precisely (7). Applying the lemma proves (4), with uniformity understood along every sequence of choices `q>p`.

The scale constraint concerns the tail point `x=O(log B)`, whose physical coordinate is `a=O(log B/L)=o(1)`. The upper endpoint `B/(cL)` itself may diverge. At the distant polynomial contacts, (17) needs only an `o(1)` source bound; the vanishing slack absorbs it without altering the leading coefficient.

For (6), set `B=C sqrt(log(1/delta)/delta)`. Condition (5) gives (3), and (4) gives
\[
 \frac{\Delta_{r;p,q}(B)}\delta\longrightarrow
       \frac{\kappa_r}{2C^2}.
\]
Since best approximation error is nondecreasing with the window, the deficit is nonincreasing. Bracketing with constants on either side of `sqrt(kappa_r/2)` proves the minimum-range asymptotic. This does not apply a Lipschitz perturbation bound with an additive `O(1/L)` error.

## Prior art, falsification checks and boundaries

Best uniform polynomial approximation, uniqueness and alternation are classical; [NIST DLMF §3.11(i)](https://dlmf.nist.gov/3.11.i) supplies that framework. The affine Chebyshev extremal and its relation to constrained polynomial extrema belong to the classical theory surveyed in Shadrin, [*Twelve Proofs of the Markov Inequality*](https://www.damtp.cam.ac.uk/user/na/people/Alexei/papers/markov.pdf), §1.4. AF-586 supplies the precise constrained curvature certificate used here. No new polynomial family or general alternation theorem is claimed.

Wu--Yang, [*Polynomial methods in statistical inference: theory and practice*](https://arxiv.org/abs/2104.07317), Theorem 3.3.4 and its proof, use polynomial approximation of `exp(-x)x^j/j!` for Poisson-mixture comparison. Dette--Titoff, [*Optimal discrimination designs*](https://arxiv.org/abs/0908.1912), establish the broader discrimination/approximation connection. These are neighboring classical mechanisms; their stated results do not supply the variable-source, fixed-degree, near-half-range robustness lemma (8) or the arithmetic scale condition (5). The present contribution is that proved transport result and the enlarged regime for the registered experiment, without a theorem-priority claim based on search absence.

The source input is unconditional and local on the real side of `s=1`. Fröberg's prime-zeta/Möbius formula is already anchored in `SOURCES.md`; Kawalec's [recent preprint, equations (2)--(3)](https://arxiv.org/html/2603.21535v1) explicitly records the analytic regular part. No zero-free estimate or conditional prime-counting error from elsewhere in that literature is imported.

A scratch-only standard-library `decimal` check at 90-digit precision used the analytic controls
\[
 \widetilde g_L(x)=\frac{x\exp(-x-x^2/L)}
 {m_L\exp(-m_L-m_L^2/L)},\qquad
 m_L=\frac{2}{1+\sqrt{1+8/L}},\qquad B=L^2.
\]
They converge uniformly to `f`, satisfy the logarithmic envelopes, and have an `O(1/L)` profile perturbation much larger than `log B/B^2`: direct expansion gives `g_tilde_L(2)-f(2)=-6/(eL)+O(L^(-2))`. For degrees `2,3,4,5` and `L=10^3,10^6,10^12`, 14,424 sampled inequalities checked (16)--(17) and the exponential envelopes on two 300-step meshes per case. Peak bisection for the witness gave loss/predicted-loss ratios `0.901748,0.998853,0.999999` at degree two and `0.683147,0.877771,0.939388` at degree five. The point error at `x=2` already exceeded the predicted loss in every case. These are finite-precision consistency checks, not continuum certificates, actual-prime computations, or exact minimax evaluations. The proof is (9)--(22).

The exact peak normalization, zero left endpoint, positivity and relative tail envelope all enter the proof. An arbitrary uniformly small perturbation is not licensed by this theorem. The fixed-degree compactness and fixed `H_r` estimates do not establish a growing-degree extension. A relative envelope out to `O(log B)` has not been proved here when `log B` is comparable to `log p`; no failure or transition law in that regime is asserted.

As before, classical alternation supplies `r+2` fixed probes approaching the binary whole-window radius, with a zero node moved to a positive coordinate at vanishing loss. This does not supply one common optimal multiway design, finite-bit error control, or a positive absolute margin as `p` grows. The arithmetic objects remain generalized-prime matched controls indexed by rational-prime edit locations. The result does not certify ordinary-prime provenance, exclude any zeta zero, or imply RH.
