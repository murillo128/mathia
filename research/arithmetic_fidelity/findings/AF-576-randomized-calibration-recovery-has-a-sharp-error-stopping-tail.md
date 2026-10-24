# AF-576 — Randomized calibration recovery has a sharp error–stopping tail

## Status and question

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · RANDOMIZED-IDENTIFICATION · MATCHED-CONTROL · NO-GENERAL-NOVELTY-CLAIM

AF-575 separates finite termination on each input from a uniform deterministic query bound when calibration slack is unknown. Its seedwise adversary does not establish a lower bound for probabilistic success. Here two **fixed inputs, chosen independently of the realized random seed**, close that gap. In the binary experiment, every finite query budget has minimax error exactly one half. More strongly, error at most \(\alpha<1/2\) on every input forces the worst-case probability of exceeding **each** finite query budget to be at least \(1-2\alpha\), and that constant is sharp.

The obstruction is to uniform probabilistic resource guarantees. Exact identification with input-dependent finite termination remains possible.

## Experiment and sharp statements

Fix \(n\ge1\), \(A>0\), and two known real source curves \(F_0,F_1\in C^{n+1}[0,A]\). Assume their gap \(g=F_1-F_0\) satisfies
\[
 g^{(n)}(0)=d>0,\qquad g^{(n)}(a)>0,\qquad
 g^{(n+1)}(a)<0\quad(0\le a\le A).
\tag{1}
\]
The unknown input is \(x=(i,b)\) in
\[
 \mathcal X=\{0,1\}\times\mathcal B^\circ,
 \qquad \mathcal B^\circ=\{b\in C^n[0,A]:\|b^{(n)}\|_\infty<d/2\}.
\tag{2}
\]
An oracle returns exact noiseless values of \(y_x=F_i+b\) at positive coordinates \(a\in(0,A]\). The nuisance is fixed throughout the experiment. Its lower polynomial coefficients are unrestricted, and its positive slack \(\delta=d-2\|b^{(n)}\|_\infty\) is not supplied.

A randomized policy chooses each coordinate and its stopping/output decisions measurably from its internal randomness and past responses. These rules are defined on finite response histories; coordinates must remain in \((0,A]\). The random seed is independent of the input. No restriction on its distribution, density near zero, or computational power is imposed. Only value queries are counted. Write \(\tau_x\) for the number of queries and \(\widehat i_x\) for the binary output.

1. For every finite integer \(N\ge0\),
   \[
   \boxed{\inf_{\mathcal A:\,\tau\le N}
     \sup_{x=(i,b)\in\mathcal X}
     \mathbb P_x(\widehat i\ne i)=\frac12.}
   \tag{3}
   \]
   The cap can always be enforced on every history by truncating at \(N\); a cap holding almost surely on every admitted input gives the same conclusion.

2. Let \(\mathfrak A_\alpha\) consist of policies which terminate almost surely on every admitted input and have error at most \(\alpha\) on every input, for \(0\le\alpha<1/2\). Then for **each** finite \(N\),
   \[
   \boxed{\inf_{\mathcal A\in\mathfrak A_\alpha}
       \sup_{x\in\mathcal X}\mathbb P_x(\tau_x>N)=1-2\alpha.}
   \tag{4}
   \]
   One policy attains the right side simultaneously for all \(N\).

3. Every \(\mathcal A\in\mathfrak A_\alpha\) has
   \[
     \sup_{x\in\mathcal X}\mathbb E_x\tau_x=\infty.
   \tag{5}
   \]
   This does not require infinite expectation on any individual input. The policy attaining (4) has finite expectation on every input.

Thus even a uniformly high-probability query bound fails: error \(\le\alpha\) and \(\mathbb P_x(\tau>N)\le\beta\) uniformly in \(x\) require \(\beta\ge1-2\alpha\). Neither additional random sampling near the endpoint nor response adaptation removes this restriction.

## A fixed pair of inputs couples the randomized transcripts

For \(0<u<A\), define the Taylor extension
\[
 J_u(a)=
 \begin{cases}
 \displaystyle\sum_{r=0}^n\frac{g^{(r)}(u)}{r!}(a-u)^r,&0\le a\le u,\\
 g(a),&u\le a\le A.
 \end{cases}
\tag{6}
\]
The derivatives through order \(n\) match at \(u\). Since \(g^{(n)}\) is positive and strictly decreasing,
\[
 J_u\in C^n[0,A],\qquad
 \|J_u^{(n)}\|_\infty=g^{(n)}(u)<d.
\tag{7}
\]
Consequently
\[
 x_{0,u}=(0,J_u/2),\qquad x_{1,u}=(1,-J_u/2)
\tag{8}
\]
are both admitted, with the same slack \(\delta_u=d-g^{(n)}(u)>0\). Their oracle curves coincide with the known midpoint \(M=(F_0+F_1)/2\) everywhere on \([u,A]\).

Run any policy capped at \(N\) against the hypothetical oracle \(M\). Pad query lists after stopping by the harmless coordinate \(A\), and put
\[
 U_N=\min_{1\le j\le N}a_j^M,
 \qquad q_N(u)=\mathbb P(U_N<u).
\tag{9}
\]
For \(N=0\), set \(U_0=A\). Every finite list consists of strictly positive coordinates, so \(U_N>0\) almost surely and
\[
 q_N(u)\longrightarrow0\qquad(u\downarrow0).
\tag{10}
\]
This is continuity of probability for decreasing events; no quantitative law for endpoint access is assumed.

Use the same random seed for the runs on \(M,x_{0,u},x_{1,u}\). On \(\{U_N\ge u\}\), induction over queries shows that their queried coordinates, responses, stopping decisions, and final outputs are identical. Indeed the next coordinate is chosen from the same history, and all three oracles agree there. Thus the transcript laws of the two admitted inputs have total variation at most \(q_N(u)\). More directly, on that event the shared binary output is wrong for exactly one source. Therefore
\[
 \frac{\mathbb P_{x_{0,u}}(\widehat i\ne0)
       +\mathbb P_{x_{1,u}}(\widehat i\ne1)}2
 \ge\frac{1-q_N(u)}2.
\tag{11}
\]
After fixing the policy and \(N\), one chooses **one deterministic \(u\)** making \(q_N(u)\) arbitrarily small. Both nuisance functions in (8) are then fixed before drawing the seed. Taking the supremum over inputs proves the lower bound in (3); a fair guess without queries attains it. The worst-case error one half need only be a supremum, not an error attained by a particular witness.

The midpoint need not be an admitted full input. Only finite queries against it are used to construct the coupling. Excluding its critical-budget representation is consistent with the exact terminating procedure below. A seed-dependent choice of \(u\) would not prove (11) for probabilistic guarantees and is not used.

## The error–stopping tradeoff and its sharpness

Take any \(\mathcal A\in\mathfrak A_\alpha\). Truncate it after \(N\) queries, returning an independent fair guess if it has not stopped. For every input, the error of this capped policy is
\[
 \mathbb P_x(\widehat i\ne i,\tau\le N)
      +\tfrac12\mathbb P_x(\tau>N)
 \le\alpha+\tfrac12\mathbb P_x(\tau>N).
\tag{12}
\]
Applying (3) yields
\[
 \sup_x\mathbb P_x(\tau>N)\ge1-2\alpha.
\tag{13}
\]
Then \(\sup_x\mathbb E_x\tau\ge N(1-2\alpha)\) for every \(N\), proving (5). This argument never interchanges a pointwise limit with a supremum over inputs.

For the matching policy, use the noiseless exact certificate of [[research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth|AF-575]]. For completeness, let \(K=\|g^{(n+1)}\|_\infty\), and at scales \(h=A2^{-j}\) take the normalized divided difference \(D_h\) at \(n+1\) equally spaced positive nodes between \(h/(n+1)\) and \(h\). It has
\[
 |D_hb|\le\|b^{(n)}\|_\infty,\qquad D_hg\ge d-Kh.
\tag{14}
\]
Retain labels with \(|D_hy-D_hF_i|<d/2\), and stop when exactly one remains. The true label always remains; the false one is excluded once \(Kh<\delta/2\). Hence this deterministic policy \(\mathcal A_0\) stops correctly after finitely many queries on every input. Its query count \(\tau_0(x)\) is unbounded over \(x\), by (3).

With probability \(2\alpha\), guess a fair binary label immediately; with probability \(1-2\alpha\), run \(\mathcal A_0\). This single policy has error exactly \(\alpha\) on every input, finite expected cost \((1-2\alpha)\tau_0(x)\) at each input, and
\[
 \mathbb P_x(\tau>N)=(1-2\alpha)\mathbf1_{\{\tau_0(x)>N\}}.
\tag{15}
\]
Taking the supremum proves the upper bound in (4) for every finite \(N\). This deliberate allocation of allowed error establishes sharpness of the criterion; it is not proposed as a practical sampling strategy.

## Arithmetic instance and exact controls

The theorem applies directly to a sufficiently remote fixed pair of rational-prime edit locations \(p<q\) in AF-571/572/575. Retain
\[
 P(s)=\sum_{\ell\ \mathrm{prime}}\ell^{-s},\quad
 h_p(s)=p^{-s}-(p+1)^{-s},\quad
 \Phi_p(a)=(P-h_p)^{-1}(E_1(a)),\quad
 E_1(a)=\int_a^\infty e^{-v}\frac{dv}{v}.
\tag{16}
\]
Set \(F_0=(-1)^{n-1}\Phi_p\), \(F_1=(-1)^{n-1}\Phi_q\). Their analytic endpoint extensions obey (1) after choosing a sufficiently small fixed window. Specifically, with \(c=e^{B_1}\), \(B_1\) the Meissel–Mertens constant, and \(\Delta_{p,q}=1/[p(p+1)]-1/[q(q+1)]>0\), the boundary-jet derivation in AF-571 gives
\[
 d=nc^n\Delta_{p,q}(\log p)^{n-1}[1+O_n(1/\log p)],\quad
 k:=-g^{(n+1)}(0)=(n+1)c^{n+1}\Delta_{p,q}(\log p)^n[1+O_n(1/\log p)].
\tag{17}
\]
Thus \(\delta_u=ku+O_{p,q,n}(u^2)\). The random-transcript witness stays inside the same registered smooth-calibration class; no randomized prime model or varying nuisance within a run is introduced. The prime threshold and window are fixed before letting \(u\downarrow0\). For a larger finite source list, the weakest adjacent pair gives the same lower bounds; sharp equality (4) is asserted only for the binary experiment.

A transparent analytic control is \(F_0=0\), \(F_1=g=a^n/n!-a^{n+1}/(n+1)!\) on \([0,1/2]\). Here \(d=k=1\), \(\delta_u=u\), and on \(a<u\),
\[
 g(a)-J_u(a)=-\frac{(a-u)^{n+1}}{(n+1)!}.
\tag{18}
\]
The witnesses coincide exactly at and above \(u\) and differ at every point below it. For \(N\) independent uniform queries on \((0,A]\), their optimal equal-prior binary testing error, **when these two witness functions are known**, is exactly
\[
 \frac12(1-u/A)^N.
\tag{19}
\]
A query below \(u\) distinguishes the two known functions; otherwise the entire transcript is identical. This verifies sharpness of the coupling step for this sampling design, not an optimal \(u\)-dependent complexity law for arbitrary adaptive designs.

Exact rational checks covered (6)–(8), the derivative joins and (18) for orders \(1\) through \(6\) with \(u=2^{-(j+1)}\), \(1\le j\le8\). A separate enumeration used the eight nodes \(A\ell/8\), \(1\le\ell\le8\), thresholds \(u=Ak/8\), \(2\le k\le8\), and \(1\le N\le4\): all 28 designs, totaling 32,760 query sequences, gave no-hit probability \(((9-k)/8)^N\). Half that probability is the known-witness testing error. The \(u=A\) edge was included as a control. These checks verify the witness algebra and probability constants; the arbitrary-policy and continuous-randomness assertions rest on the coupling and truncation proofs.

## Prior art and boundary

[[research/prior_art/incremental/PA-le-cam-two-point-testing|Two-hypothesis testing through total variation]] is classical; [Yu (1997), *Assouad, Fano, and Le Cam*](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf) describes that framework. Equation (11) is proved directly by coupling, without a minimax interchange over an infinite input class.

[Kunsch, Novak and Rudolf (2019), *Solvable integration problems and optimal sample size selection*](https://doi.org/10.1016/j.jco.2018.10.007), [author manuscript, §§1, 3.1 and 3.4](https://arxiv.org/abs/1805.08637), already distinguish per-input finite expected cost from infinite worst-case cost. Proposition 3.13 uses transcript comparison and truncation of randomized adaptive algorithms; Theorem 3.15 uses rarely observed smooth perturbations. Their integration classes and targets differ from (2). Their unsolvability conclusion is not transferred here: the present binary problem has an exact per-input terminating procedure. Wasilkowski's varying-cardinality work, anchored under AF-575, is earlier background.

The mathematical addition is the fixed-input coupling for the prime-edit calibration class and its sharp binary error–stopping-tail law, beyond AF-575's seedwise guarantee. No general novelty is claimed for testing, randomization lower bounds, truncation, or variable-cardinality information. The proof is a classical-method specialization, not an RH mechanism.

Positive-coordinate value queries, an unknown slack with no positive lower bound, and the stated nuisance class are load-bearing. A known slack floor allows a uniform finite certificate from (14); an endpoint order-\(n\) derivative oracle distinguishes the sources immediately. The Taylor witnesses are \(C^n\), and the result is not asserted for an analytic nuisance class. Exact arithmetic and known source curves remain idealizations. The theorem gives no optimal slack-dependent query rate, precision-cost law, or Bayesian average over nuisances. These generalized-prime matched controls do not constitute an ordinary-prime discriminator or an RH implication.
