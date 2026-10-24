---
type: theorem
research_line: xi_flow
finding_id: XF-204
status: canonical
---

# XF-204 — Randomized Jacobi detection has a sharp error–stopping tail

**Evidence:** EXACT-DERIVED + CLASSICAL-TWO-POINT-COUPLING + SYNTHETIC-ACQUISITION-BOUNDARY. Unknown strictly positive calibration slack permits exact finite stopping on each input, as in XF-203, but randomization cannot give a uniform finite resource guarantee. Every finite row cap has minimax binary error exactly `1/2`. Requiring error at most `alpha<1/2` forces worst-case probability of exceeding each finite cap to be at least `1-2 alpha`, and this constant is attained. The new destination-specific step is an endpoint-preserving complex interpolation: the two hard inputs are fixed before the seed and agree even at the queryable critical endpoint. The statement covers noiseless observations and a known total squared-noise budget. It supplies no physical Xi acquisition interface or zero-exclusion implication.

## Experiment and quantifiers

Fix sufficiently large integer \(Q\), \(0<\tau_0\le1/4\), and
\[
T=[-1/4,-\tau_0]\cup[\tau_0,1/4],\qquad I=[Q,2Q].
\]
Use the complete response of XF-201/203,
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),\quad G_r=|x_r|^{-1/2},\\
F_\tau(r)&=\frac2{G_r}
 (e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r})
 -\frac{2x_r^{-1/2}}{G_r}
 (e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}).
\end{aligned}
\tag{1}
\]
The square root is principal; \(G_r>1\) on this interval. Keep the exact threshold
\[
D=\min_{\tau\in T}|F_\tau'(Q)|
 =\min_{\tau\in T}\|F_\tau'\|_{C(I)}>0,
\qquad L_*=D/2.
\tag{2}
\]
[[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]] proves, for the full response, that \(v_\tau(r)=|F_\tau'(r)|\) is strictly decreasing on \(I\). In particular the maximum is attained only at \(Q\). Its reciprocal term has a differentiated exponentially small envelope; it is included in this exact conclusion, rather than deleted from (1). Compactness of \(T\) gives a minimizer \(\tau_Q\) in (2). The proof below uses no guess about its sign or precise location.

For known \(\sigma\ge0\), an input \(x\in\mathcal X_\sigma\) fixes a label \(i\in\{0,1\}\), a displacement \(\tau\in T\) when \(i=1\), one baseline and one noise sequence:
\[
f_0=0,\quad f_1=F_\tau,\quad
B\in C^1(I;\mathbb C),\quad \|B'\|_\infty<L_*,\quad
 e\in\ell^2(\mathbb N;\mathbb C),\quad \sum_j|e_j|^2\le\sigma^2.
\tag{3}
\]
At the \(j\)-th distinct value query \(r_j\in I\), including potentially \(r_j=Q\), the response is \(f_i(r_j)+B(r_j)+e_j\). The baseline constant is unrestricted. Its actual slack \(\delta=L_*-\|B'\|_\infty>0\) is not supplied. The input, including the noise sequence indexed by query number, is fixed independently of the policy's seed. There is no independent or identically distributed noise assumption.

A policy's query, stopping and output rules are measurable functions of its seed and the finite observation history, defined on every finite history. Only value queries are counted. Write \(\nu_x\) for its row count and \(\widehat i_x\) for its output. For every finite integer \(N\ge0\),
\[
\boxed{\inf_{\mathcal A:\,\nu\le N}
 \sup_{x\in\mathcal X_\sigma}\mathbb P_x(\widehat i_x\ne i)
 =\frac12.}
\tag{4}
\]
Let \(\mathfrak A_{\alpha,\sigma}\) contain policies terminating almost surely on each input and satisfying error at most \(\alpha\) on every input, with \(0\le\alpha<1/2\). Then
\[
\boxed{\inf_{\mathcal A\in\mathfrak A_{\alpha,\sigma}}
 \sup_{x\in\mathcal X_\sigma}\mathbb P_x(\nu_x>N)=1-2\alpha.}
\tag{5}
\]
One policy attains (5) simultaneously for all finite \(N\). Every policy in this class has
\[
\sup_{x\in\mathcal X_\sigma}\mathbb E_x\nu_x=\infty,
\tag{6}
\]
while the attaining policy has finite expected row count on every particular input.

## A strict complex join that preserves the critical endpoint

Write \(F=F_{\tau_Q}\). For every \(0<u<Q\), there exists
\[
J_u\in C^1(I;\mathbb C),\quad \|J_u'\|_\infty<D,
\quad J_u(Q)=F(Q),\quad J_u=F\text{ on }[Q+u,2Q].
\tag{7}
\]
The endpoint value in (7) is essential; a Taylor extension from \(Q+u\) need not preserve it.

Here is an explicit construction. Set
\[
s=\frac{F(Q+u)-F(Q)}u,\qquad v=F'(Q+u),\qquad
\gamma=D-|s|>0.
\tag{8}
\]
Strictness follows from
\[
|s|\le\frac1u\int_0^u |F'(Q+t)|\,dt<D;
\]
the equality \(|F'(Q)|=D\) at a single endpoint cannot saturate a positive-length integral. Also \(|v|<D\). Put
\[
a=\frac\gamma{4D}\in(0,1/4],\quad \beta=2a,\qquad
c=\frac{s-av}{1-a}.
\tag{9}
\]
Then
\[
|c|\le\frac{D-\gamma+aD}{1-a}
 =D-\frac{\gamma-2aD}{1-a}
 =D-\frac\gamma{2(1-a)}<D.
\tag{10}
\]
For \(0\le t\le u\), let \(\eta(t)=0\) on \([0,(1-\beta)u]\) and let it increase linearly from zero to one on \([(1-\beta)u,u]\). Thus \(\eta\) is continuous, takes values in \([0,1]\), and \(\int_0^u\eta(t)\,dt=au\). Define
\[
w(t)=(1-\eta(t))c+\eta(t)v,\qquad
J_u(Q+t)=F(Q)+\int_0^t w(z)\,dz\quad(0\le t\le u).
\tag{11}
\]
On the rest of \(I\), set \(J_u=F\). Since
\[
\int_0^u w(t)\,dt=u[(1-a)c+av]=us=F(Q+u)-F(Q),
\quad w(u)=v,
\tag{12}
\]
both value and first derivative match at \(Q+u\). The corner in \(\eta\) does not spoil continuity of \(w\); only \(C^1\) regularity of \(J_u\) is required. Convexity of the complex disk gives
\[
\sup_{0\le t\le u}|w(t)|\le\max\{|c|,|v|\}<D.
\]
On the tail, monotonicity gives \(\sup_{[Q+u,2Q]}|F'|=|v|<D\), proving (7). No ordering of complex phases or control of tangent rotation is needed. More generally, the same construction works for a normed-vector curve whenever its chord and tail derivative norms are strictly below \(D\).

The two noiseless inputs
\[
x_{0,u}:\ f=0,\ B=J_u/2;
\qquad
x_{1,u}:\ f=F,\ B=-J_u/2
\tag{13}
\]
are admissible with strict derivative budgets. Their observations agree with the fixed midpoint \(M=F/2\) on
\[
\{Q\}\cup[Q+u,2Q].
\tag{14}
\]
They are fixed functions across the entire experiment, independent of the random seed.

## Coupling an arbitrary capped randomized policy

Fix the policy and its finite cap \(N\), and run it against the hypothetical midpoint \(M\). This is only a device for defining a seed-indexed query list; \(M\) need not itself be an admissible full input. Let
\[
q_N(u)=\mathbb P\{\text{some midpoint query among the first }N
                    \text{ lies in }(Q,Q+u)\}.
\tag{15}
\]
Ignore nonexistent queries after stopping. For each seed, its finite list has a positive minimum distance from \(Q\) among the coordinates strictly greater than \(Q\), if any. Queries exactly at \(Q\) never enter the open interval. Consequently the decreasing events in (15) have empty intersection as \(u\downarrow0\), and
\[
q_N(u)\longrightarrow0.
\tag{16}
\]
For \(N=0\), \(q_0=0\). There is no assumed density or quantitative law for the random coordinates near the endpoint.

Couple runs on \(M,x_{0,u},x_{1,u}\) by using the same seed. On the complement of (15), induction over the finite history makes every query, response, stopping decision and output identical. Agreement at \(Q\) follows from (7), including when the policy chooses it deterministically. The common binary output is wrong on exactly one of the two inputs, so
\[
\frac{\mathbb P_{x_{0,u}}(\widehat i\ne0)
      +\mathbb P_{x_{1,u}}(\widehat i\ne1)}2
\ge\frac{1-q_N(u)}2.
\tag{17}
\]
Choose one deterministic \(u\) after fixing the policy and cap, but before drawing its seed. Equations (16)–(17) prove the lower bound in (4). A zero-query fair guess proves the upper bound. This is a supremum-over-inputs statement; a single input need not attain error exactly one half.

The argument covers adaptive positions and stopping. A cap that holds almost surely on each admitted input can be made a cap on every history by truncation without changing any admitted-input law. No seed-dependent choice of baseline is used.

## Stopping tails, sharpness, and total noise

Take \(\mathcal A\in\mathfrak A_{\alpha,\sigma}\). Truncate after \(N\) rows and return an independent fair guess on nontermination. Its error on an input is
\[
\mathbb P_x(\widehat i_x\ne i,\nu_x\le N)
 +\tfrac12\mathbb P_x(\nu_x>N)
\le\alpha+\tfrac12\mathbb P_x(\nu_x>N).
\tag{18}
\]
Combining with (4) yields \(\sup_x\mathbb P_x(\nu_x>N)\ge1-2\alpha\). Also \(\mathbb E_x\nu_x\ge N\mathbb P_x(\nu_x>N)\), so (6) follows by taking suprema and then arbitrarily large \(N\). There is no interchange of a pointwise limit with a supremum.

For sharpness use [[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]]'s deterministic exact procedure \(\mathcal A_0\). To recall why it covers the present noise class, at scale \(0<h\le1/(4Q)\) it averages \(n\) disjoint-coordinate difference pairs to obtain a contrast \(Z\) with coefficient norm \(\sqrt{2/n}/h\). Set
\[
t=\frac\sigma h\sqrt{\frac2n},\qquad a(h)=A Q^{-3/2}h,
\]
where \(A\) is a certified full-source bound. Its sound stopping certificates are
\[
|Z|>L_*+t\ \Rightarrow\ \text{active},\qquad
|Z|<L_*-a(h)-t\ \Rightarrow\ \text{null}.
\tag{19}
\]
For the actual \(\delta>0\), the correct test succeeds once \(a(h)+2t<\delta\). A preassigned sequence \(h_k\downarrow0\) with sufficiently many distinct pairs per scale makes \(t_k\le a(h_k)\to0\); thus the row count \(\nu_0(x)\) is finite for every input. The single global energy cap bounds every block's error by Cauchy–Schwarz. There is no replenished per-block budget, stochastic averaging assumption or prior on \(B\).

With probability \(2\alpha\), guess a fair binary label immediately; otherwise run \(\mathcal A_0\). This policy has error exactly \(\alpha\) on every input, and
\[
\mathbb P_x(\nu_x>N)=(1-2\alpha)\mathbf1_{\{\nu_0(x)>N\}},
\qquad \mathbb E_x\nu_x=(1-2\alpha)\nu_0(x)<\infty.
\tag{20}
\]
The deterministic counts \(\nu_0(x)\) are unbounded over the noiseless subfamily by (4), so the supremum in (20) equals \(1-2\alpha\) for every finite \(N\). This deliberate allocation of allowed error proves sharpness of the criterion; it is not a practical sensing recommendation.

For every \(\sigma>0\), the same noiseless fixed pair proves the lower bounds because \(\mathcal X_0\subset\mathcal X_\sigma\). The upper bound is separately justified by (19), not inferred from this inclusion. The result also remains valid if noise is supplied by a fixed causal rule responding to the current query and past observations, with a pathwise total-energy cap, while the source and baseline remain fixed before the seed. The lower bound uses the zero rule; the certificate is pathwise and its sufficient finite block depends only on the baseline slack and \(\sigma\). This extension supplies no permission to vary the baseline or source after seeing the seed.

## Checks, prior art, and consequences

An exact rational control used
\[
F(t)=t-t^2/2+i t^2/4,\qquad 0\le t\le1/2.
\]
Here \(|F'(t)|^2=1-2t+5t^2/4\) decreases strictly, and the chord at \(u\) satisfies \(|s|\le1-u/4\). Using the certified slack floor \(u/4\) in place of \(\gamma\) in (9) preserves (10). Rational checks at \(u=2^{-k}\), \(1\le k\le16\), with three exact unit rotations and two positive scalings verified 96 joins: exact displacement preservation, endpoint derivative matching, and strict derivative bounds. A separate enumeration of 263 sampling designs, comprising 8,754 subsets, checked endpoint-safe no-hit probabilities for distinct grid queries with an additional mandatory endpoint query. For the positive grid \(j/m\), \(1\le j\le m\), an open hidden interval \((0,k/m)\), and \(n\) distinct uniform grid queries, the no-hit probability is \(\binom{m-k+1}{n}/\binom mn\), interpreted as zero if the numerator has too few available nodes. These checks audit the join algebra and coupling constants; the arbitrary-policy theorem follows from (7)–(20), not finite sampling.

[[research/prior_art/incremental/PA-le-cam-two-point-testing|Two-point testing through total variation]] is classical; see [Bin Yu, *Assouad, Fano, and Le Cam*, in Festschrift for Lucien Le Cam (1997), 423–435](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf). Equation (17) proves the needed coupling directly. [Kunsch, Novak and Rudolf, *Solvable integration problems and optimal sample size selection*, Journal of Complexity 53 (2019), 40–67](https://doi.org/10.1016/j.jco.2018.10.007), [author manuscript, §§1 and 3.4](https://arxiv.org/abs/1805.08637), already distinguish per-input finite cost from infinite worst-case cost and use transcript comparison, truncation and rarely observed smooth perturbations. Their integration unsolvability conclusions are not imported into this solvable binary experiment. The complex join uses elementary convexity and integration; scalar Lipschitz-extension theory, such as [Gutev, *Lipschitz Extensions and Approximations*, §2](https://arxiv.org/abs/2002.07205), is background rather than a black-box endpoint-and-derivative interpolation theorem.

The local Master clue granted bounded reading of [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]] for the fixed-input coupling and truncation question. The Jacobi transfer requires the new join (7), because its endpoint is queryable and its response is complex. The source-specific speed fact comes from XF-201, and per-input noisy termination comes from XF-203. No general novelty is claimed for interpolation, two-point testing, randomization lower bounds, or varying-cardinality information. The mathematical delta is the exact randomized resource boundary for this complete Jacobi experiment, beyond XF-203's deterministic finite-prefix witnesses.

Strict chord and tail slack matter. For the control \(F(r)=D(r-Q)\), the required join is impossible: the two fixed endpoint values force average speed \(D\). In that noiseless affine experiment two value queries distinguish the labels using the threshold \(D/2\) on chord magnitude. The present witnesses are \(C^1\), and no analogous claim is made for an analytic nuisance class: agreement with \(F\) on a tail interval would force agreement everywhere. An endpoint derivative oracle also changes the experiment. A supplied positive slack floor restores a uniform certificate via (19).

The theorem closes the possibility of uniform probabilistic row guarantees under the stated unknown-slack interface, while preserving exact finite detection on each input. It gives no optimal slack-dependent randomized rate, Bayesian average-cost statement, finite-precision result, physical Xi source access, bound on \(\Lambda\), or RH conclusion.
