# WI-467 — far-right Euler correction is an absolutely continuous signed measure

**Status:** EXACT-DERIVED + CLASSICAL-SMOOTHING-SPECIALIZATION + NO-NOVELTY-CLAIM + NON-RH.

**Local dependencies:** [WI-464](WI-464-full-euler-correction-has-an-integrable-threshold-primitive.md), for the cumulative coefficient and the infinite-torus measure obstruction; [WI-465](WI-465-analytic-euler-observables-have-a-full-first-zero-sampling-correction.md), for the separate arithmetic transport boundary.

## Claim and evidence boundary

For every fixed width `r>0`, at all sufficiently large fixed
`sigma=1+epsilon`, the full Euler response's prime-axis correction is
represented by an **absolutely continuous finite signed measure on the
response interval**. The finite-panel signed measures converge to it in
total variation, for every finite prime-power exhaustion with vanishing
omitted coefficient mass and without renormalization. Their cumulative
coefficients converge uniformly at all thresholds. The limit is an
absolutely continuous representative of WI-464's `L^1` coefficient `C`.

An explicit sufficient condition is (6) below. In particular it holds
for `r=1, sigma>=12`. This is a sufficient far-right regime, not a sharp
parameter boundary or a statement near the pole.

The scalar projection therefore can regularize the correction even
though WI-464 excludes any finite signed measure with the prescribed
marginals on the full prime torus. The result concerns the **coefficient**:
it does not prove a first arithmetic sampling law for indicators or
arbitrary Lipschitz tests. No zero-sampling-height limit is taken here.

## Definitions and a uniform one-angle condition

Use product probability Haar measure `m` on the prime torus and set

\[
 A=\sum_{n\ge2}\Lambda(n)n^{-\sigma},\qquad
 a_n=\frac{\Lambda(n)n^{-\sigma}}A,\qquad
 G_r(n,m)=e^{-r|\log(n/m)|}-(nm)^{-r}.
 \tag{1}
\]

Let `v_n` be Hilbert vectors with Gram kernel `G_r`, as in WI-464.
One explicit realization in `L^2([0,infinity),ds)` is
`v_n(s)=sqrt(2r) exp(-r(log n-s)) 1_[0,log n](s)`; direct integration
gives (1), and `||v_n||<=1`. Define

\[
 V=\sum_{p,k\ge1}a_{p^k}z_p^k v_{p^k},\qquad Q=\|V\|^2,
 \qquad w_p=\sum_{k\ge1}a_{p^k}
 =\frac{\log p}{A(p^\sigma-1)}.
 \tag{2}
\]

The Euler vector series converges absolutely. For a finite set `F` of
prime powers, retain its terms in `V` to obtain `V_F,Q_F`. No coefficient
is rescaled. Write `delta_F=sum_(n notin F) a_n`; then
`||Q-Q_F||_infinity<=2 delta_F`. Put

\[
 h_p(\theta_p)=-2\log p\sum_{j\ge1}p^{-j/2}\cos(j\theta_p),
 \qquad b_p=\frac{2\log p}{\sqrt p-1},\qquad
 \|h_p\|_1\le b_p,\quad \int h_p=0.
 \tag{3}
\]

For a scalar map `q`, `q_#` denotes pushforward of a signed measure.
The total variation norm is the full mass `|nu|(R)`, equivalently the
supremum against tests of absolute value at most one. Define

\[
 \nu_F=(Q_F)_\#\left(\sum_{p\in P(F)}h_p\,m\right),
 \qquad C_F(t)=\nu_F(({-\infty},t]),
 \tag{4}
\]

where `P(F)` is the set of base primes in `F`. These are exactly the
finite coefficients of WI-464.

The smoothing coordinate will be `theta_3`, with every other angle
conditioned on. The following quantities depend only on `sigma,r`:

\[
 b=2a_2a_3G_r(2,3)>0,\quad
 R=1-a_2-w_3,\quad D=\sum_{k\ge2}k^2a_{3^k},
\]
\[
 E=2a_3R+2D(1-w_3)+8a_3D+4D^2.
 \tag{5}
\]

Our sufficient condition is

\[
 \boxed{E\le b/100.} \tag{6}
\]

It holds uniformly for all sufficiently large `sigma` at each fixed
`r>0`. Indeed `a_2->1`, `R=O(2^(-sigma))`, and
`D/a_3=O(3^(-sigma))`, so `E/b=O_r(2^(-sigma))`.

To prove what (6) supplies, decompose any panel containing `2,3` as

\[
 V_F=W_F+a_3z_3v_3+U_F,\quad
 W_F=a_2z_2v_2+W_F^0,\quad
 U_F=\sum_{\substack{k\ge2\\3^k\in F}}a_{3^k}z_3^kv_{3^k}.
 \tag{7}
\]

Here `||W_F^0||<=R`, `||W_F||<=1-w_3`, and
`||partial_(theta_3)^j U_F||<=D` for `j=0,1,2`. Expanding its squared
norm, and writing `c_F=||W_F||^2+a_3^2||v_3||^2`, gives

\[
 Q_F=c_F+b\cos(\theta_3-\theta_2)+e_F(\theta_3),\qquad
 \max_{0\le j\le2}\|e_F^{(j)}\|_\infty\le E.
 \tag{8}
\]

The four error bounds in (5) respectively come from the cross terms
`a_3 z_3 v_3` with `W_F^0`, `U_F` with `W_F`, `U_F` with `a_3 z_3 v_3`,
and the square of `U_F`. The product rule costs at most `4` at derivative
order two. These estimates also apply to the full series and to any
panel after deleting a prime `p>=5`. They are uniform over all the
conditioned angles and all such panels.

## Elementary total-variation smoothing lemma

Suppose two real `C^2` circle functions `f,g` have first and second
derivatives within `1/100` of those of the same shifted cosine. Their
constant terms may differ. For any real `C^1` circle weight `rho`,

\[
 \|f_\#(\rho\,d\theta/2\pi)
       -g_\#(\rho\,d\theta/2\pi)\|_{\rm TV}
 \le K\|\rho\|_{C^1}\|f-g\|_{C^1}^{1/2},
 \tag{9}
\]

with an absolute constant `K`; all these pushforwards are absolutely
continuous. We use the maximum of the indicated derivative suprema for
the `C^j` norms.

Here is a direct proof, including the square-root exponent needed below.
The derivative of each function has exactly two simple zeros. Near the
two cosine critical points its second derivative has a fixed sign and
magnitude bounded below; outside these neighborhoods its first
derivative is bounded away from zero. Consequently, uniformly in this
class,

\[
 m\{|f'|\le h\}\ll h,\qquad
 \int_{|f'|\ge h}|f'|^{-2}\,d\theta\ll h^{-1},\quad 0<h<1.
 \tag{10}
\]

Absolute continuity follows by the change-of-variables formula on the
two open monotonicity intervals; the critical points themselves have
zero circle measure.

Set `d=g-f`, `delta=||d||_(C^1)`. It suffices to consider small positive
`delta`; the trivial bound `2||rho||_1` handles larger values. Choose a
`C^1` cutoff `chi` equal to zero on `|f'|<=h` and one on `|f'|>=2h`,
with derivative `O(|f''|/h)` in the intervening set. For a smooth real
test `phi` with `||phi||_infinity<=1`, the part of
`integral [phi(g)-phi(f)] rho` where `1-chi` occurs is
`O(||rho||_infinity h)` by (10). On the other part use
`f_s=f+s d`, `0<=s<=1`, and integrate by parts on the circle:

\[
 \int[\phi(g)-\phi(f)]\rho\chi\,d\theta
 =-\int_0^1\int\phi(f_s)
       \partial_\theta\left(\frac{d\rho\chi}{f_s'}\right)
       d\theta\,ds.
 \tag{11}
\]

Take `h>=2 delta`. On the cutoff support `|f_s'|>=|f'|/2`. In (11),
derivatives on `d` or `rho` cost `O(delta||rho||_(C^1)/h)`; a derivative
on `chi` has the same bound since its support has measure `O(h)`; and
a derivative on the reciprocal denominator is bounded by (10), since
`f_s''` is uniformly bounded. Thus the entire expression is

\[
 O\bigl(\|\rho\|_{C^1}[h+\delta/h]\bigr).
 \tag{12}
\]

Choose `h=sqrt(delta)` for sufficiently small `delta`. Taking the
supremum over smooth bounded tests yields (9); these tests determine
the total variation of finite measures. This proof works for signed
`rho`, and makes no lower bound assumption on a response density.

Applied to (8) after scaling the scalar output by `1/b`, the lemma has
a constant depending only on the fixed `sigma,r`. Additive constants
`c_F/b` do not affect its derivative hypotheses.

## Prime deletion makes the scalar variation summable

Let `Q^(-p)` delete all powers of prime `p` from `V`. For `p>=5`, both
`Q` and `Q^(-p)` satisfy the uniform condition (8). Since the deleted
vector is independent of `theta_3`,

\[
 \|Q-Q^{(-p)}\|_\infty\le2w_p,\qquad
 \|\partial_{\theta_3}(Q-Q^{(-p)})\|_\infty
 \le2w_p\sum_{k\ge1}k a_{3^k}.
 \tag{13}
\]

Exactly the same inequalities hold for a finite panel containing `2,3`,
with its smaller deleted mass. Condition on all coordinates except
`theta_3` and apply (9) with `rho=1`. The resulting conditional laws
differ in total variation by `O_(sigma,r)(sqrt(w_p))`, uniformly over
the conditioned coordinates. Multiplication by `h_p` costs `||h_p||_1`.
The deleted map is independent of `z_p`, so its pushforward weighted by
`h_p` is zero. Hence, defining `nu_p=Q_#(h_p m)`,

\[
 \boxed{\|\nu_p\|_{\rm TV}\le K_{\sigma,r}b_p\sqrt{w_p},
 \qquad p\ge5.} \tag{14}
\]

The same bound holds for `nu_(F,p)=(Q_F)_#(h_p m)`, interpreted as zero
when `p` is unused. For `p=2,3`, the elementary bound `||nu_p||<=b_p`
suffices. All these measures have densities: condition on `theta_3`
and use the monotone change of variables from the lemma, with the smooth
weight `h_3` when `p=3`.

The new summability budget is

\[
 \sum_p b_p\sqrt{w_p}<\infty,\qquad
 b_p\sqrt{w_p}\ll_\sigma
 (\log p)^{3/2}p^{-(\sigma+1)/2}.
 \tag{15}
\]

It converges even by comparison with all integers because `sigma>1`.
This summability fact alone is valid for all `sigma>1`; its application
in (14) requires (6). It follows that

\[
 \nu=\sum_p\nu_p
 \quad\hbox{converges absolutely in total variation},\qquad
 \nu=k(x)\,dx\quad\hbox{for some }k\in L^1(\mathbb R).
 \tag{16}
\]

It has total mass zero and support in `[0,q_*]`, where `q_*=Q(1)<=1`.
We have summed individually defined scalar pushforwards, not pushed
forward a nonexistent infinite signed torus measure.

## Cutoff independence, uniform thresholds, and the same coefficient

For any finite exhaustion with `delta_F->0`, the terms `2,3` are
eventually present. Uniform absolute convergence of the `3`-power
derivative series also gives

\[
 \eta_F:=\max_{j=0,1}\|
       \partial_{\theta_3}^j(Q-Q_F)\|_\infty\longrightarrow0.
 \tag{17}
\]

For example, with `D_1=sum_(k>=1) k a_(3^k)` and
`d_(F,1)=sum_(3^k notin F) k a_(3^k)`, a valid bound is
`eta_F<=2(1+D_1)delta_F+2d_(F,1)`. The latter tail tends to zero for
every such exhaustion, including nonnested ones.

For each fixed `p!=3`, condition on the other angles and apply (9)
to `Q,Q_F`; integrating `|h_p|` bounds
`||nu_(F,p)-nu_p||` by `K_(sigma,r)b_p sqrt(eta_F)`. For `p=3` use the
weighted version with `rho=h_3`; its fixed `C^1` norm is finite. Thus,
for every real cutoff `P>=3`,

\[
 \|\nu_F-\nu\|_{\rm TV}\le K_{\sigma,r}\left[
 \sqrt{\eta_F}\left(\|h_3\|_{C^1}
       +\sum_{\substack{p\le P\\p\ne3}}b_p\right)
       +2\sum_{p>P}b_p\sqrt{w_p}\right].
 \tag{18}
\]

First choose `P` by (15), then use (17). This proves total-variation
convergence for all the stated exhaustions. In particular

\[
 \sup_{t\in\mathbb R}|C_F(t)-C_*(t)|\longrightarrow0,
 \qquad C_*(t)=\int_{-\infty}^t k(x)\,dx.
 \tag{19}
\]

The continuous function `C_*` is absolutely continuous, zero off
`[0,q_*]`, and belongs to `W^(1,1)(R)`. Its restriction to `[0,1]`
equals WI-464's `C` almost everywhere, because (19) also implies its
previously proved `L^1` convergence. This identifies the same coefficient,
including its sign and normalization. In particular for Lipschitz `f`,

\[
 \mathcal L(f)=\int f(x)k(x)\,dx
             =-\int f'(x)C_*(x)\,dx,
 \qquad \int C_*(x)\,dx=B_\varepsilon(r)>0.
 \tag{20}
\]

The coefficient now acts on every bounded Borel test by integration
against `k`; this is not an extension of the arithmetic theorem to
every such test. Uniform convergence in (19) concerns panel size only.

## A concrete nonempty parameter regime

For `sigma>=2`, integer-sum comparison yields

\[
 \sum_{n\ge5}\Lambda(n)n^{-\sigma}
 \le5^{2-\sigma}\int_4^\infty\frac{\log x}{x^2}\,dx
 <19\,5^{-\sigma},\qquad A<5\,2^{-\sigma}.
 \tag{21}
\]

For the second bound, separate `2,3,4` and use
`log2<1`, `log3<4/3` and the tail bound at `sigma=2`. The resulting
coefficient is `1+16/27+1/4+76/25<5`. Also `log2>2/3`, for example
from the first term of its positive artanh series. Consequently

\[
 a_2^{-1}<8,\qquad a_3/a_2<1,\qquad
 R/a_2\le2^{-\sigma}+29(2/5)^\sigma.
 \tag{22}
\]

Writing `x=3^(-sigma)<=1/9`,

\[
 \frac D{a_3}=\sum_{k\ge2}k^2x^{k-1}
 =\frac{1+x}{(1-x)^3}-1
 \le\frac{4x}{(1-x)^3}<6x.
 \tag{23}
\]

At `r=1`, `G_r(2,3)=1/2` and `b=a_2a_3`. Equations (5), (22), (23)
give

\[
 \frac Eb\le2\,2^{-\sigma}+58(2/5)^\sigma
            +144\,3^{-\sigma}+144\,3^{-2\sigma}.
 \tag{24}
\]

Each term decreases in `sigma`. At `sigma=12` their exact rational sum is
`27181045151806503401 / 15690529804500000000000 < 1/100`.
This verifies (6) for every real `sigma>=12`. The displayed rational
inequalities were also checked with exact fraction arithmetic; no phase
quadrature, zero table, or numerical tail assumption is used.

## Prior art, falsification controls, and consequence

Conditioning on one-dimensional fibers to prove absolute continuity is
classical. N. V. Smorodina, *The absolute continuity of distributions of
functionals of diffusion processes*, **Russian Math. Surveys 37:6**
(1982), 205–213, [introduction, p. 205](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=3950&what=fullteng),
describes that method in the diffusion setting. Fractional regularity
and total-variation stability of nonlinear image laws are also classical;
see V. I. Bogachev, E. D. Kosov and G. I. Zelenov, *Fractional smoothness
of distributions of polynomials and a fractional analog of the
Hardy–Landau–Littlewood inequality*, **Trans. AMS 370** (2018), 4401–4432,
[Theorem 5.7 and §§5–6](https://arxiv.org/abs/1602.05207).
Their Gaussian-polynomial hypotheses are not being imposed on this
infinite prime-torus response. The circle lemma (9) and its Euler
application are proved directly here; no general smoothing novelty is
claimed.

The substantive local delta is the uniform conditional cosine geometry
(8), the square-root prime-deletion estimate (14), and its summable
variation budget (15). WI-464 had only a Lipschitz-dual limit and left
finite scalar variation open; these estimates resolve it in a nonempty
source-family regime, despite divergent variation before projection.

Several boundaries are load-bearing:

- Mere absolute continuity of the Haar response law would not imply
  (14). The derivative and curvature bounds must hold uniformly after
  conditioning and prime deletion. They have been proved here only
  under (6); the argument does not cover small `epsilon` by continuity.
- The square-root exponent is adequate because
  `(sigma+1)/2>1`. Replacing it by an unspecified continuity modulus
  would not justify the infinite prime sum. The budget degenerates as
  `sigma` approaches one, and constants also depend on `b,r`.
- Truncation preserves the original normalization and eventually the
  two anchor terms. The estimates do not assert a uniform rate for
  arbitrary panels before those terms are present.
- Prime-only and diagonal controls still give zero correction, as in
  WI-464. Scalar smoothing does not create a prime-axis coefficient in
  those controls or force a sign for the coherent coefficient.
- A regular candidate coefficient does not control the scaled signed
  errors of the actual discrete sampling laws. WI-465's fixed analytic
  transport and WI-463's hard-threshold obstruction remain separate.
  No stochastic ordering, individual off-line-zero detection, stronger
  critical-line proportion, or RH implication follows.

The coherent investigation closes at scalar coefficient regularity in
the specified regime. Its analytic stability proof supplies no separate
finite formalization target with a currently identified fertility gain.
No Lean verification or independent adversarial approval is claimed.
