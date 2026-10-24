---
type: theorem
research_line: xi_flow
finding_id: XF-206
status: canonical
---

# XF-206 — Noiseless analytic calibration retains sharp stopping tails

**Evidence:** EXACT-DERIVED + CLASSICAL-GAUSSIAN-INFORMATION-LOWER-BOUND + SYNTHETIC-ACQUISITION-BOUNDARY. In the full holomorphic calibration class, even noiseless exact value queries have capped minimax error `1/2` when positive derivative slack is unknown. Small random polynomials whose derivative vanishes at the critical endpoint replace XF-204's nonanalytic tail joins and XF-205's observation noise. The sharp worst-case stopping tail remains `1-2 alpha`, while exact finite stopping on each input is possible. This closes the noiseless analytic-class boundary left by XF-205; it supplies no physical Xi access or zero-exclusion theorem.

## Experiment and statement

Fix sufficiently large integer \(Q\), \(0<\tau_0\le1/4\),
\(I=[Q,2Q]\), and \(T=[-1/4,-\tau_0]\cup[\tau_0,1/4]\).
Use the complete singleton response
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),&G_r&=|x_r|^{-1/2},\\
F_\tau(r)&=\frac2{G_r}
 \bigl(e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r}\bigr)
 -\frac{2x_r^{-1/2}}{G_r}
 \bigl(e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}\bigr).
\end{aligned}
\tag{1}
\]
The square root for real \(r>0\) is principal. The full reciprocal term is
retained. By [[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]],
\[
D=\min_{\tau\in T}\|F_\tau'\|_{C(I)}
 =\min_{\tau\in T}|F_\tau'(Q)|>0,\qquad L_*=D/2.
\tag{2}
\]
An input fixes its label \(\ell\in\{0,1\}\), its source \(f=0\) or
\(F_\tau\), and a baseline \(B\), independently of the policy's seed.
The baseline is holomorphic on the fixed right half-plane and satisfies
\(\|B'\|_{C(I)}<L_*\). Its constant is unrestricted; neither a positive
slack floor nor any bound outside \(I\) is supplied. Denote this noiseless
class by \(\mathcal X^{\mathrm{hol}}_0\). Queries are distinct exact
values
\[
y_j=f(r_j)+B(r_j),\qquad r_j\in I.
\tag{3}
\]
Endpoints and arbitrarily close positions are allowed. Policies are
measurable functions of their seed and previous answers, defined on all
finite histories. A finite cap may be enforced by truncation on every
history, including histories outside the promised input class.

For every finite cap \(N\),
\[
\boxed{\inf_{\mathcal A:\nu\le N}
 \sup_{x\in\mathcal X^{\mathrm{hol}}_0}
 \Pr_x(\widehat\ell\ne\ell)=\tfrac12.}
\tag{4}
\]
The lower bound holds even if the active displacement is fixed to a known
minimizer \(\tau_Q\) in (2) and its entire source \(F=F_{\tau_Q}\) is
supplied to the policy.

For \(0\le\alpha<1/2\), let \(\mathfrak A_\alpha\) consist of policies
terminating almost surely on each admitted input and having error at most
\(\alpha\) on each input. For every finite \(N\ge0\),
\[
\boxed{\inf_{\mathcal A\in\mathfrak A_\alpha}
 \sup_{x\in\mathcal X^{\mathrm{hol}}_0}\Pr_x(\nu>N)=1-2\alpha.}
\tag{5}
\]
Every such policy has \(\sup_x\mathbb E_x\nu=\infty\), although one
policy attains all the tail equalities and has finite expectation on each
particular input. These statements extend to a known total squared-noise
allowance \(\sigma\ge0\), with one fixed noise sequence, by the same
lower subfamily and XF-203's separate upper certificate.

## Endpoint-flat polynomial uncertainty fits inside the derivative budget

For the chosen full source set \(v(r)=|F'(r)|\). XF-201, (6), gives
\[
v(Q)=D,\qquad v_{\min}:=\min_I v>0,\qquad
\kappa:=\min_I(-v')>0.
\tag{6}
\]
In particular \(D-v(r)\ge\kappa(r-Q)\). These are exact fixed-\(Q\)
properties, including the differentiated reciprocal contribution; no
asymptotic error is compared with an arbitrarily small slack.
XF-205 proves that \(F\) extends holomorphically to the right half-plane:
use \(G_r=\sqrt\pi\,r(1+r^2)^{-1/4}\) and matching analytic branches
of its nonvanishing factors there.

Fix \(N\ge1\), write \(s=(r-Q)/Q\in[0,1]\), and use the polynomial
space
\[
P_a(r)=\sum_{k=0}^{N-1}a_k s^{2k},\qquad a\in\mathbb C^N.
\tag{7}
\]
Its derivative is zero at \(Q\). Define the coefficient event
\[
E=\left\{\sum_{k=1}^{N-1}2k|a_k|\le\kappa Q^2/4\right\}.
\tag{8}
\]
For \(a\in E\),
\[
|P_a'(r)|\le\frac{s}{Q}\sum_{k=1}^{N-1}2k|a_k|
 \le\frac{\kappa(r-Q)}4\le\frac{D-v(r)}4.
\tag{9}
\]
Here \(s^{2k-1}\le s\); at \(N=1\) the derivative and sum are zero.

For any \(0<\varepsilon<1\), take baselines
\[
B_{0,\varepsilon,a}=\frac{1-\varepsilon}{2}F+P_a,
\qquad
B_{1,\varepsilon,a}=-\frac{1-\varepsilon}{2}F+P_a.
\tag{10}
\]
Both are holomorphic on the fixed domain, and
\[
|B_{\ell,\varepsilon,a}'(r)|
\le\frac{(1-\varepsilon)v(r)}2+\frac{D-v(r)}4
=\frac D2-\frac{\varepsilon v(r)}2-\frac{D-v(r)}4
\le L_*-\frac{\varepsilon v_{\min}}2<L_*.
\tag{11}
\]
Their noiseless observation curves are
\[
g_{-,\varepsilon,a}=\frac{1-\varepsilon}{2}F+P_a,
\qquad
g_{+,\varepsilon,a}=\frac{1+\varepsilon}{2}F+P_a.
\tag{12}
\]
A whole polynomial is drawn once, before the seed; it is not new noise at
each query. The coefficient region (8) does not shrink with
\(\varepsilon\). The strict decrease in source speed is what makes this
possible despite the saturated derivative at the limiting midpoint.

## Finite adaptive Gaussian transcripts are continuous in the mean shift

First leave the coefficients unconditioned. Let \(a_k\) be independent
circular complex Gaussians with \(\mathbb E|a_k|^2=b^2>0\). Thus their
real and imaginary parts have variance \(b^2/2\). For a real scalar
\(c\), consider the auxiliary oracle \(cF+P_a\), with covariance kernel
\[
K(r,t)=b^2\sum_{k=0}^{N-1}s_r^{2k}s_t^{2k}.
\tag{13}
\]
These auxiliary priors need not be supported on admissible baselines;
conditioning onto (8) will enforce that before the testing lower bound.

Every \(j\le N\) distinct nodes in \(I\) give linearly independent
evaluation rows. Indeed the first \(j\) columns form a Vandermonde
matrix in the distinct nonnegative squares \(s_i^2\), with determinant
\[
\prod_{i<k}(s_k^2-s_i^2)\ne0.
\tag{14}
\]
This includes a node at \(Q\). As a result each new distinct evaluation,
through the \(N\)-th one, has positive conditional Gaussian variance.
No uniform lower bound on that variance is asserted.

Include the policy's complete independent seed in the history. At a fixed
common non-stopped history \(h=(\text{seed},y_1,\ldots,y_{j-1})\), all
past nodes and the next node \(r\) are fixed. Put
\[
\begin{aligned}
K_-&=(K(r_i,r_k))_{i,k<j},& k&=(K(r,r_i))_{i<j},\\
F_-&=(F(r_i))_{i<j},& y_-&=(y_i)_{i<j}.
\end{aligned}
\]
Gaussian conditioning gives the next-answer mean and variance
\[
\begin{aligned}
\mu_c(h)&=cF(r)+kK_-^{-1}(y_--cF_-),\\
V(h)&=K(r,r)-kK_-^{-1}k^*>0.
\end{aligned}
\tag{15}
\]
For \(j=1\), the products involving the empty matrix are zero.
Although the nodes are adaptive, (15) remains the conditional law: at
each step the next row is a measurable function of the already fixed
history, and conditioning the remaining Gaussian coefficient vector on
that one linear equation gives the next affine Gaussian slice.
Induction proves (15). The choices of nodes add no constraint beyond
the answers that determined them. This argument does not differentiate
or assume continuity of any policy rule.

For every fixed history,
\[
\mu_c(h)-\mu_{1/2}(h)
=(c-1/2)\bigl(F(r)-kK_-^{-1}F_-\bigr)\longrightarrow0
\quad(c\to1/2).
\tag{16}
\]
The variance in (15) is independent of \(c\). The densities of two
nondegenerate Gaussians with the same variance converge in \(L^1\)
when their means converge. Thus the total variation distance
\(d_c(h)\) between the two next-answer laws tends to zero at every
non-stopped history and is bounded by one. At a stopped history both
transitions are the same absorbing state, so take \(d_c(h)=0\).

Let \(\mathsf P_c^j\) be the law of the seed and the first \(j\)
answers, with absorption after stopping. Total variation is
\(\operatorname{TV}(P,Q)=\sup_A|P(A)-Q(A)|\). The kernel inequality
\[
\operatorname{TV}(\mathsf P_c^j,\mathsf P_{1/2}^j)
\le\operatorname{TV}(\mathsf P_c^{j-1},\mathsf P_{1/2}^{j-1})
 +\int d_c(h)\,\mathsf P_{1/2}^{j-1}(dh)
\tag{17}
\]
follows by changing the history distribution first and the transition
kernel second. Dominated convergence and induction from the common seed
law prove, for every fixed capped policy and every fixed \(b>0\),
\[
\operatorname{TV}(\mathsf P_c^N,\mathsf P_{1/2}^N)\to0.
\tag{18}
\]
The comparison is always at a common history, not at two trajectories
assumed close. Hence discontinuous decisions, seed-dependent positions,
and arbitrarily close nodes are all covered. There is no policy-uniform
rate in (18); none is needed for a minimax supremum over unknown slack.

## Condition the priors, then take the testing limit

Fix any \(\eta>0\). The Gaussian scale \(b>0\) can be chosen small
enough that \(\Pr(E^c)\le\eta\). For example, for \(N\ge2\),
Cauchy–Schwarz and Markov give
\[
\Pr(E^c)\le\frac{4bN(N-1)}{\kappa Q^2},
\tag{19}
\]
since \(\mathbb E|a_k|\le b\). For \(N=1\), \(E\) has probability
one. Fix this positive \(b\) before sending \(\varepsilon\) to zero.

Under each label draw the coefficients conditional on \(E\), independently
of the policy's seed, and use (10). Every input in either mixture is now
admissible and noiseless by (11). Denote the resulting transcript laws
by \(\mathsf Q_{-,\varepsilon}\) and
\(\mathsf Q_{+,\varepsilon}\). Conditioning a law on an event of
probability at least \(1-\eta\) changes total variation by at most
\(\eta\), and passing to a transcript cannot increase it. Consequently,
\[
\operatorname{TV}(\mathsf Q_{-,\varepsilon},\mathsf Q_{+,\varepsilon})
\le2\eta+
\operatorname{TV}(\mathsf P_{(1-\varepsilon)/2}^N,
                  \mathsf P_{(1+\varepsilon)/2}^N)
=2\eta+o_{\varepsilon\to0}(1).
\tag{20}
\]
No Gaussian conditional formula is applied to the truncated prior.
Gaussian conditioning was used only for the auxiliary untruncated law;
(20) transfers the result to supported priors.

For equal label weights, any binary decision has average error at least
\((1-\operatorname{TV})/2\). Worst-case error over fixed inputs dominates
this prior average. For each fixed policy and cap, first let
\(\varepsilon\downarrow0\) in (20), then \(\eta\downarrow0\). Its
worst-case error is at least \(1/2\). Fair guessing gives equality,
proving (4); the zero-query case is immediate.

The coefficients and \(\varepsilon\) may depend on the policy and cap,
but never on its realized seed. The polynomial dimension grows with the
cap. No pair of distinct analytic curves agrees on an interval; the
identity theorem is fully respected. The obstruction concerns overlap
of finite transcript **mixtures**, rather than exact equality of two
analytic functions on a tail.

## Per-input stopping and sharp tails

Truncate a policy in \(\mathfrak A_\alpha\) at \(N\), guessing fairly
if it has not stopped. For each input the truncated error is at most
\(\alpha+\Pr_x(\nu>N)/2\). Equation (4) therefore implies
\[
\sup_x\Pr_x(\nu>N)\ge1-2\alpha,\qquad
\sup_x\mathbb E_x\nu\ge N(1-2\alpha).
\tag{21}
\]
The last inequality for every \(N\) yields an infinite supremum of
expectations, not one fixed input with infinite expected cost.

[[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]]
gives a deterministic exact procedure on the larger \(C^1\) class. With
actual slack \(\delta=L_*-\|B'\|_\infty>0\), its distinct short-chord
certificate succeeds once
\[
A Q^{-3/2}h+\frac{2\sigma}{h}\sqrt{\frac2n}<\delta,
\tag{22}
\]
where \(A\) is a certified full-source constant, \(h\downarrow0\), and
\(n\) is the number of distinct pairs. At zero noise one pair per scale
suffices. Thus it terminates in finitely many rows on each holomorphic
input. Run it with probability \(1-2\alpha\), otherwise guess fairly
without queries. This policy has per-input error \(\alpha\), finite
per-input expected cost, and tail at most \(1-2\alpha\). Its exact
branch has unbounded counts by (4), so equality holds in (5) for every
finite cap, for this same policy.

For any known \(\sigma>0\), the noiseless subfamily proves the same
lower bounds; (22) proves finite stopping under one global squared-noise
cap and the same mixture proves sharpness. It neither assumes independent
measurement errors nor supplies new noise energy at each block.

## Controls, prior art, and consequence

A scratch audit using exact rational arithmetic checked (14) on 264 node
banks with \(1\le N\le6\), including the endpoint and separations as
small as \(2^{-60}\). All 1,023 successive Gram Schur complements were
positive. Another 680 rational cases checked the strict envelope in
(11) for the analytic rotating control
\(F'(t)=(1-t/2)e^{it}\), \(0\le t\le1\), with polynomial derivative
bound \(t/8\) and \(\varepsilon=2^{-k}\), \(1\le k\le40\).
These finite checks test algebra and endpoint degeneracy; the proofs
(9), (14), and (15)–(20) establish the arbitrary-cap, arbitrary-policy
claim. They do not certify new Xi source estimates or constitute Lean
verification.

The probability method is classical. [Robert J. Kunsch,
*High-Dimensional Function Approximation: Breaking the Curse with Monte
Carlo Methods* (2017), §2.2 and Lemma 2.2 in §2.2.1, pp. 18–22](https://arxiv.org/pdf/1704.08213)
uses truncated Gaussian input measures for adaptive randomized lower
bounds and derives the conditional Gaussian law for adaptive linear
information. Equations (15)–(20) give the needed mean-continuity argument
and transfer to admissible calibration priors explicitly; that work's
linear approximation theorem is not asserted for this binary experiment.
[Bin Yu, *Assouad, Fano, and Le Cam* (1997), §29.2, Lemma 1](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf)
provides the classical mixture-testing boundary. No novelty is claimed
for Gaussian conditioning, truncated-prior lower bounds, Vandermonde
interpolation, or total variation. The tail argument and per-input
certificate are inherited from XF-203–XF-205.

The mathematical delta is the source-compatible polynomial space (7):
it simultaneously has zero derivative at the critical endpoint, enough
independent value directions for an arbitrary finite cap, and fixed
positive coefficient room furnished by the complete source's strict
speed decrease. This removes the positive-noise assumption from the
full analytic-class obstruction. It does not remove it from XF-205's
one-dimensional restricted witness.

The boundaries are substantive:

- For the affine control \(F(r)=D(r-Q)\), \(\kappa=0\) and (8) supplies
  no nonconstant polynomial room. Two noiseless endpoint values already
  distinguish the two derivative-budget classes.
- In the supplied-source class \(B=cF\), real \(|c|<1/2\), one nonzero
  noiseless value identifies the label as in XF-205. The present lower
  bound uses additional polynomial directions; it does not contradict
  finite-dimensional identification with a fixed supplied model.
- A derivative oracle at \(Q\) identifies the label by comparing the
  derivative modulus with \(L_*\). Value queries at distinct real points
  are the information class proved insufficient uniformly here.
- A supplied positive slack floor gives a finite uniform certificate
  from (22). Holomorphy on a fixed domain without additional quantitative
  or structural restrictions does not supply that floor. The result
  makes no blanket assertion about smaller prescribed analytic classes,
  off-interval complex queries, or other oracle interfaces.

Thus analyticity alone does not repair unknown-margin acquisition, even
with exact noiseless answers. A physical Xi calibration law that excludes
these source-plus-polynomial directions or quantitatively separates the
labels remains a separate required input. No bound on \(\Lambda\),
exclusion of an off-critical zero, or new arithmetic source law follows.
