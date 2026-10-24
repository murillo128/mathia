# AF-578 — Continuous randomness retains the fixed-budget polynomial-calibration obstruction

## Claim and evidence boundary

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · SHARP-MINIMAX · ORACLE-MODEL-BOUNDARY · NO-GENERAL-NOVELTY-CLAIM

[[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]] separates finite-bit policies from ideal continuously randomized policies under polynomial output calibration of unknown, unbounded degree. Its continuous-random procedure identifies each fixed input almost surely within its actual degree plus two value queries. The fixed-query minimax question was left open there.

Here every finite query cap has exact minimax error equal to blind guessing, **even with continuous-real randomness and adaptive exact observations**. For a cap of \(N\ge1\), the obstruction already uses calibration polynomials of degree at most \(N-1\), with unrestricted coefficients. The result requires bounded source derivatives through order \(N-1\) on the observation window. The prime-edit curves satisfy this condition.

The decisive estimate is uniform over adaptive query locations, including arbitrarily close nodes. A broad Gaussian distribution on polynomial coefficients hides the source in transcript total variation. This is an averaging device over fixed admissible calibrations, not measurement noise, a changing calibration, or an adversary observing the realized random seed.

## Experiment and sharp statements

After an affine coordinate change let the observation window be \(J=[0,1]\). Endpoints may be excluded without changing the lower bound. Let known sources \(F_1,\ldots,F_m\), \(m\ge2\), satisfy
\[
 y(t)=F_i(t)+b(t),\qquad b\in\Pi:=\bigcup_{d\ge0}\Pi_d,
 \tag{1}
\]
where \(\Pi_d\) is the real polynomials of degree at most \(d\). One fixed \(b\) is shared by every observation of an input. Assume pairwise gaps are nonpolynomial when interpreting the label as a uniquely defined full-curve property; the lower-bound argument itself does not need this assumption.

Policies are measurable oracle procedures. They may choose each coordinate from all previous responses and independent randomness on a standard probability space, including exact continuously distributed coordinates. They receive only point values of \(y\); all other computation and known-source evaluations are free. A policy with cap \(N\) returns one label after at most \(N\) queries. Define
\[
 R_N=\inf_{\mathcal A:\,T\le N}\ \sup_{\substack{1\le i\le m\\ b\in\Pi}}
          \Pr_{F_i+b}\{\widehat i\ne i\},\qquad c_m=1-1/m.
\]

**Fixed-cap theorem.** If \(F_i\in C^{N-1}[0,1]\), then
\[
 \boxed{R_N=c_m.} \tag{2}
\]
The same equality holds if the supremum is restricted to \(b\in\Pi_{N-1}\), even if that degree bound is supplied to the policy. Uniform blind guessing attains the upper bound with no queries.

Consequently, for sources in \(C^d[0,1]\) that are analytic on the interior with nonpolynomial gaps, and a **known** degree bound \(d\), \(d+1\) queries have minimax error \(c_m\), whereas \(d+2\) queries permit zero error almost surely on every fixed input: fit each candidate residual at \(d+1\) deterministic interior nodes and validate at one independent continuous interior coordinate, as in AF-577. This is an exact threshold for a uniform query cap in that oracle model, not a claim that every individual input requires \(d+2\) queries.

**Stopping-tail consequence.** Suppose the sources are \(C^\infty\) on the closed window. For a variable-length policy, let \(T\) be the query count at its label return, or infinity on nonreturn, and let
\[
 e=\sup_{i,b}\Pr_{F_i+b}\{T<\infty,\widehat i\ne i\},\qquad
 q_N=\sup_{i,b}\Pr_{F_i+b}\{T>N\}.
\]
Then, for every finite \(N\),
\[
 \boxed{e+c_m q_N\ge c_m.} \tag{3}
\]
In particular zero error forces \(q_N=1\) for every finite cap. Any policy with \(e<c_m\) has nonuniformly tight stopping tails and infinite worst-case expected query count. These are suprema over inputs; no one input is asserted to fail to terminate.

When the sources are also analytic with nonpolynomial gaps, (3) is sharp among policies returning almost surely on every input, for every \(0\le e\le c_m\). With probability \(e/c_m\), return a uniform label immediately; otherwise run AF-577's zero-error continuous-random procedure. That procedure has \(q_N=1\) by (3), so the mixture has error \(e\) and \(q_N=1-e/c_m\) for every \(N\). This sharpness uses the ideal continuous-random oracle model. AF-577's finite-bit obstruction still rules out its zero-error branch in the finite-bit model.

## A uniform interpolation lift

For \(g\in C^{N-1}[0,1]\), put
\[
 B_N(g)=\sum_{k=0}^{N-1}\frac{2^k}{k!}\|g^{(k)}\|_\infty.
 \tag{4}
\]
At any \(r\le N\) distinct nodes \(t_1,\ldots,t_r\), let \(p\in\Pi_{r-1}\) interpolate \(g\). Write \(c\in\mathbb R^N\) for its monomial coefficient vector, padded with zeros. Then
\[
 \|c\|_2\le\|c\|_1\le B_N(g). \tag{5}
\]
Indeed, its Newton representation is
\[
 p(t)=\sum_{k=0}^{r-1}g[t_1,\ldots,t_{k+1}]
                       \prod_{\ell=1}^{k}(t-t_\ell).
\]
The divided-difference mean-value formula bounds the coefficient of the \(k\)th product by \(\|g^{(k)}\|_\infty/k!\); the product's monomial coefficient \(\ell^1\)-norm is at most \(\prod_{\ell=1}^k(1+|t_\ell|)\le2^k\). This proves (5), without a lower bound on node spacing and without assuming chronological node order is increasing.

The point is not a well-conditioned inversion of arbitrary sampled data. These particular data come from a smooth **source gap**, so their polynomial lifts remain bounded even when the Vandermonde matrix becomes ill-conditioned.

## Adaptive Gaussian transcript bound

Fix \(N\). Draw one coefficient vector \(\beta\sim N(0,L^2 I_N)\), independently of the policy's seed, and use the fixed nuisance
\[
 b(t)=v(t)^T\beta,\qquad v(t)=(1,t,\ldots,t^{N-1})^T.
 \tag{6}
\]
Let \(P_i^L\) be the law of the entire capped transcript, including the seed and returned label, for source \(i\) under this prior. We prove, for \(g=F_i-F_j\),
\[
 D_{\rm KL}(P_i^L\|P_j^L)\le\frac{B_N(g)^2}{2L^2},
 \qquad
 \|P_i^L-P_j^L\|_{\rm TV}\le\frac{B_N(g)}{2L}.
 \tag{7}
\]
Here total variation is \(\sup_E|P(E)-Q(E)|\).

Condition on the common seed and an identical history under the two source hypotheses. Its distinct previous nodes give a matrix \(V\) whose rows are \(v(t_\ell)^T\). Until \(N\) distinct nodes have been observed, these rows are independent. Put
\[
 H=V^T(VV^T)^{-1}V,\qquad w=(I-H)v(t)
\]
for a new distinct node \(t\). With no previous nodes take \(H=0\). Standard [[research/prior_art/incremental/PA-gaussian-conditioning-adaptive-linear-information|Gaussian conditioning]] gives common conditional variance \(L^2\|w\|_2^2>0\). The difference of the two conditional response means is
\[
 \delta=g(t)-v(t)^TV^T(VV^T)^{-1}g_{\rm prev}.
 \tag{8}
\]
Although coordinates depend on past responses, conditioning on that history fixes them. Inductively, each new observation conditions the remaining Gaussian coefficient vector on one linear equation. No additional constraint on the coefficients is supplied by a coordinate already determined from the observed history. This justifies the same conditional formulas for adaptive policies.

For any realized complete transcript with \(r\le N\) distinct nodes, interpolate \(g\) at **all** those nodes, obtaining the vector \(c\) in (5). At each earlier step it satisfies both \(Vc=g_{\rm prev}\) and \(v(t)^Tc=g(t)\). Thus
\[
 \delta=w^Tc.
\]
The vectors \(u_\ell=w_\ell/\|w_\ell\|_2\) from the successive distinct nodes are orthonormal: they are precisely Gram–Schmidt innovations of the evaluation vectors. Therefore, pathwise,
\[
 \sum_{\ell=1}^{r}\frac{\delta_\ell^2}{\|w_\ell\|_2^2}
 =\sum_{\ell=1}^{r}|u_\ell^Tc|^2
 \le\|c\|_2^2\le B_N(g)^2.
 \tag{9}
\]
The interpolant here can depend on the complete transcript. It is used only in a pathwise inequality, not as an admissible prior chosen after the seed.

A repeated node returns its already recorded value under both hypotheses and contributes zero conditional divergence. Stops can be padded with identical dummy symbols. Query and stopping decisions are the same functions of the same seed and history, so only response kernels contribute to the KL chain rule. Two normal laws with equal variance have divergence \(\delta^2/(2L^2\|w\|_2^2)\). Summing and taking expectation in (9) proves the first bound in (7); Pinsker's inequality proves the second. Appending the output label cannot increase divergence. This argument also covers randomized query kernels by including their independent random seed.

## From transcript proximity to minimax error

Average the label uniformly and the calibration according to (6). For any policy, the average success probability satisfies
\[
 \frac1m\sum_{i=1}^m P_i^L(\widehat i=i)
 \le\frac1m\sum_{i=1}^m P_1^L(\widehat i=i)
       +\frac1m\sum_{i=1}^m\|P_i^L-P_1^L\|_{\rm TV}
 \le\frac1m+\frac1{2mL}\sum_{i=1}^m B_N(F_i-F_1).
 \tag{10}
\]
Worst-case error over fixed inputs is at least this prior-average error. Let \(L\to\infty\) to get (2). Every finite \(L\) is a probability measure supported on admissible, fixed degree-at-most-\(N-1\) calibrations. The proof does not use an improper uniform prior, does not require the worst input to attain the supremum, and never chooses an input after the policy's actual seed.

For (3), truncate a variable-length policy at \(N\) observations and return a fresh uniform label if it has not returned. On each input the error is at most its original unconditional error plus \(c_m\Pr(T>N)\). Apply (2) to the truncated policy. The expectation conclusion follows from \(\sup_{i,b}\mathbb E T\ge Nq_N\) for every \(N\).

## Arithmetic instance and exact controls

For distinct odd prime edit locations, retain
\[
 P(s)=\sum_{\ell\ {\rm prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-u}\frac{du}{u}.
\]
AF-577 proves analyticity on \(a>0\) and that every pairwise gap is nonpolynomial: it is strictly positive in the ordered direction and tends to zero at infinity, so the identity theorem excludes a polynomial gap on any interval. On any compact positive window \([a_-,a_+]\), all derivatives are bounded, and the affine coordinate change preserves the polynomial calibration class. Thus (2), (3), and their continuous-random sharpness apply to these same generalized-prime matched controls.

The result also applies on \((0,A]\): [[research/arithmetic_fidelity/findings/AF-571-polynomial-drift-has-exact-small-window-probe-saturation|AF-571]]'s analytic implicit equation
\[
 B_p(a)=a\exp\{\gamma+R(B_p(a))-h_p(1+B_p(a))-E(a)\},
 \quad B_p=\Phi_p-1,
\]
has analytic \(R(x)=P(1+x)+\log x\) and \(E(a)=E_1(a)+\gamma+\log a\) near zero. Its left side minus right side has derivative one with respect to \(B_p\) at \((0,0)\). The analytic implicit function theorem extends \(\Phi_p\) across zero. Together with analyticity on the positive ray this bounds each fixed derivative on \([0,A]\). This uses no large-prime or shrinking-window asymptotic.

An elementary control is \(F_0=0\), \(F_1(t)=1/(1+t)\), \(F_2(t)=1/(2+t)\) on \([0,1]\). Its gaps are nonpolynomial, all endpoint derivatives are bounded, and
\[
 B_N\bigl((a+t)^{-1}\bigr)=\sum_{k=0}^{N-1}2^k/a^{k+1}\quad(a=1,2).
\]
Exact rational checks of (8)–(9) used caps \(N=1,\ldots,6\), four rational polynomial backgrounds
\(b(t)=\sum_{k=0}^{N-1}(-1)^{k+h}(h+1)t^k/(k+1)\), \(h=0,1,2,3\), and adaptive nodes
\[
 t_r=\frac{r+(1/3\ \text{if }z_{r-1}>0,\ 2/3\ \text{otherwise})}{N+1},
 \quad z_r=b(t_r)+(1+t_r)^{-1},\quad z_{-1}=(-1)^h.
\]
Across 48 complete paths and 168 prefixes, 672 exact identities/inequalities checked the innovation mean shift, cumulative innovation energy, minimum-norm interpolation coefficient vector, and bound (5). Eight additional exact inequalities used nodes \(1/2+j/10^6\) for caps two through five. These validate the finite algebra and clustered-node control; the probabilistic and minimax statements follow from the proof, not a simulation of continuous randomness.

## Prior art, delta, and limits

- Carl de Boor, *Divided Differences* (2005), §§1 and 8, especially equation (44), supplies the Newton representation and normalized derivative bound used in (5): [author paper](https://arxiv.org/abs/math/0502036).
- G. W. Wasilkowski, *Optimal algorithms for linear problems with Gaussian measures*, **Rocky Mountain Journal of Mathematics** 16(4), 727–749 (1986), Theorem 3.1 and equation (3.14), gives the classical conditional Gaussian measure under adaptive linear information: DOI [10.1216/rmj-1986-16-4-727](https://doi.org/10.1216/rmj-1986-16-4-727), [primary-paper text mirror](https://paperzz.com/doc/7208297/optimal-algorithms-for-linear-problems-with). Its linear-approximation optimality results are not assumed to prove this discrete-label theorem.
- Ery Arias-Castro, Emmanuel J. Candès, and Mark A. Davenport, *On the Fundamental Limits of Adaptive Sensing*, **IEEE Transactions on Information Theory** 59(1), 472–481 (2013), §2, equations (2.1), (2.3), and the proof of Theorem 3, use testing bounds, adaptive likelihood factorization, and Gaussian KL calculations: [author paper](https://arxiv.org/abs/1111.4646). Their noise model differs; here uncertainty comes from a single polynomial calibration sampled before the observations.

These are classical ingredients. No priority claim is made for Gaussian-prior lower bounds, polynomial interpolation, Pinsker's inequality, or the broad distinction between fixed and variable information cardinality. The local mathematical addition is the uniform interpolation-energy estimate (9) for this source quotient and its exact **continuous-random** fixed-cap and stopping-tail conclusions. It fills the explicitly unasserted fixed-budget case in AF-577, without importing [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]]'s smooth gluing construction into the polynomial class.

The hypotheses are load-bearing. There is no coefficient bound, and the masking variance can grow without restriction. Known degree bounds cease to mask once enough observations exceed that degree; the theorem says precisely where. The window is bounded and source-gap derivatives through the required order are bounded; this proof does not establish the same bound for arbitrary analytic functions with singular derivatives at excluded endpoints, or on an unbounded observation ray. Full-curve information, derivative queries, and symbolic access to the unknown polynomial are different channels.

No nuisance distribution is asserted to describe real measurements. The conclusion concerns uniform minimax guarantees over deterministic admissible inputs. Exact full-curve identification and per-input almost-sure finite recovery survive, but neither supplies a uniform finite or expected resource budget. The prime instantiation distinguishes registered generalized-prime edit candidates, not ordinary primes from every matched control, and gives no RH implication.
