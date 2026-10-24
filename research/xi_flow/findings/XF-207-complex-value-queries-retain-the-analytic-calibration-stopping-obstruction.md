---
type: theorem
research_line: xi_flow
finding_id: XF-207
status: canonical
---

# XF-207 — Complex value queries retain the analytic calibration stopping obstruction

**Evidence:** EXACT-DERIVED + CLASSICAL-HERMITE-INTERPOLATION + SYNTHETIC-ACQUISITION-BOUNDARY. In the complete Jacobi calibration experiment, allowing exact adaptive value queries anywhere in the fixed right half-plane still leaves capped minimax error `1/2` when the positive derivative slack is unknown. The same obstruction survives a supplied bound on the baseline on any fixed compact complex neighborhood, provided that bound has positive room around the critical source midpoint. The sharp stopping tail is `1-2 alpha`. These are stronger information and regularity regimes than XF-206, not physical Xi access or a bound on the de Bruijn–Newman constant.

## Source and information class

Use sufficiently large integer \(Q\), \(I=[Q,2Q]\), and the complete
normalized response of
[[research/xi_flow/findings/XF-206-noiseless-analytic-calibration-retains-sharp-stopping-tails|XF-206]], (1).
Choose and reveal a minimizing displacement \(\tau_Q\) from its compact
admissible set, and write \(F=F_{\tau_Q}\). The exact source facts are
\[
D=|F'(Q)|=\max_I|F'|>0,\qquad L_*=D/2,\qquad
v=|F'|>0,\qquad \kappa=\min_I(-v')>0.
\tag{1}
\]
They are proved for the full direct **and reciprocal** response in
[[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]], (6)–(11).
In particular \(D-v(r)\ge\kappa(r-Q)\).

Let \(\mathbb H=\{z:\operatorname{Re}z>0\}\). The continuation used here is
unambiguous: set
\[
x(z)=\frac{1+iz}{\pi z^2},\qquad
\Gamma(z)=\sqrt\pi\,z(1+z^2)^{-1/4},
\]
and replace \(x_r,G_r\) in the full response formula by
\(x(z),\Gamma(z)\), using holomorphic branches agreeing with the positive
real-axis values. The factors have no zeros on the simply connected
\(\mathbb H\), so the branches and the resulting holomorphic \(F\) exist,
as established in
[[research/xi_flow/findings/XF-205-analytic-jacobi-calibration-retains-the-noisy-stopping-obstruction|XF-205]].
This is continuation in the normalized **row coordinate**. It does not
assert physical access to every continued value or identify this oracle
with unrestricted raw theta evaluation.

An input fixes \(\ell\in\{0,1\}\) and a holomorphic baseline \(B\) on
\(\mathbb H\), with
\[
\|B'\|_{C(I)}<L_*.
\tag{2}
\]
The positive slack is not supplied. A measurable randomized policy queries
finitely many distinct finite points \(z_j\in\mathbb H\), adaptively from
its independent seed and previous answers, and receives exact values
\[
y_j=\ell F(z_j)+B(z_j).
\tag{3}
\]
There is no bound on query magnitude or proximity to another query or to
the boundary. Policies are defined on all finite histories; a cap is
enforced there by truncation.

Call this class \(\mathcal X\). All statements below also hold for the
smaller class \(\mathcal X_{K,M}\) obtained by supplying a fixed nonempty compact
\(K\subset\mathbb H\) and imposing
\[
\|B\|_K\le M,\qquad M>\tfrac12\|F\|_K.
\tag{4}
\]
For example, \(K\) may be the closure of a bounded complex neighborhood
of \(I\). Queries need not lie in \(K\). Both \(K\) and \(M\) are fixed
before the policy and query cap, not chosen anew for a hard input.

For either input class and every finite \(N\),
\[
\inf_{\mathcal A:\nu\le N}\sup_x
 \Pr_x(\widehat\ell\ne\ell)=\tfrac12.
\tag{5}
\]
If \(\mathfrak A_\alpha\) consists of policies terminating almost surely
and having error at most \(0\le\alpha<1/2\) on every input, then
\[
\inf_{\mathcal A\in\mathfrak A_\alpha}\sup_x
 \Pr_x(\nu>N)=1-2\alpha,\qquad
\sup_x\mathbb E_x\nu=\infty\quad(\mathcal A\in\mathfrak A_\alpha).
\tag{6}
\]
One policy attains the tail equality at every finite cap and has finite
expected cost on each individual input. Revealing the active source makes
the lower assertion stronger; a model allowing unknown \(\tau\) contains
this known-source subproblem.

## The endpoint derivative is independent of every finite complex value bank

The even powers in XF-206 cannot simply be reused. At normalized positions
\(s\) and \(-s\), their evaluation rows coincide. A symmetric two-point
contrast cancels that whole polynomial nuisance. Complex access therefore
requires a different finite interpolation space.

For cap \(N\ge1\), put \(s=(z-Q)/Q\), and use
\[
\mathcal P_N=\{P:\deg P\le N+1,\ P'(0)=0\}
=\operatorname{span}_{\mathbb C}\{1,s^2,s^3,\ldots,s^{N+1}\}.
\tag{7}
\]
Here the derivative in (7) is with respect to \(s\). For any \(j\le N\)
distinct complex nodes \(s_1,\ldots,s_j\), evaluation from \(\mathcal P_N\)
onto \(\mathbb C^j\) is surjective.

Indeed, interpolate arbitrary prescribed values by a Lagrange polynomial
\(H\) of degree at most \(j-1\), and put \(W(s)=\prod_i(s-s_i)\).
If zero is one of the nodes, take \(R=W\), for which \(R'(0)\ne0\).
Otherwise take \(R=sW\), for which \(R'(0)=W(0)\ne0\). In both cases
\[
P(s)=H(s)-\frac{H'(0)}{R'(0)}R(s)
\tag{8}
\]
preserves every prescribed value, has \(P'(0)=0\), and has degree at most
\(j+1\le N+1\). This includes the endpoint, reflected pairs, arbitrary
complex contours, and arbitrarily close nodes. It also proves directly
that the derivative at zero cannot be synthesized from this finite bank
of value functionals on all polynomials.

## The larger polynomial space retains fixed admissible coefficient room

Write
\[
P_a(z)=a_0+\sum_{k=2}^{N+1}a_k((z-Q)/Q)^k.
\]
On the real interval \(I\), \(0\le s\le1\), so the event
\[
E_1=\left\{\sum_{k=2}^{N+1}k|a_k|\le\kappa Q^2/4\right\}
\tag{9}
\]
implies
\[
|P_a'(r)|\le\frac{s}{Q}\sum_{k=2}^{N+1}k|a_k|
\le\frac{D-v(r)}4.
\tag{10}
\]
For \(0<\varepsilon<1\), use the two baselines
\[
B_{0,a}=\tfrac{1-\varepsilon}{2}F+P_a,\qquad
B_{1,a}=-\tfrac{1-\varepsilon}{2}F+P_a.
\tag{11}
\]
Their derivative norms are strictly below \(L_*\), since pointwise
\[
|B_{\ell,a}'(r)|\le L_*
 -\tfrac{\varepsilon v(r)}2-\tfrac{D-v(r)}4
\le L_*-\tfrac\varepsilon2\min_Iv<L_*.
\tag{12}
\]

For the optional compact bound (4), set
\(R_0=M-\|F\|_K/2>0\) and
\(A_K=\max\{1,\sup_{z\in K}|(z-Q)/Q|\}\). Additionally impose
\[
E_2=\left\{|a_0|+\sum_{k=2}^{N+1}A_K^k|a_k|\le R_0\right\}.
\tag{13}
\]
Then \(\|P_a\|_K\le R_0\), hence (11) obeys (4). Both coefficient
constraints have positive room independent of \(\varepsilon\).
No claim is made for a bound tight at the midpoint or excluding it.

## Adaptive randomized values still have overlapping transcript laws

Take all \(N+1\) coefficients independently circular complex Gaussian
with \(\mathbb E|a_k|^2=b^2>0\), initially without conditioning. For
\(g_c=cF+P_a\), its polynomial covariance is
\[
K_N(z,w)=b^2\left(1+\sum_{k=2}^{N+1}s_z^k\overline{s_w^k}\right).
\tag{14}
\]
The surjectivity in (8) makes the Gram matrix positive definite for every
bank of at most \(N\) distinct points, wherever the policy puts them.
Consequently every next distinct value through the cap has positive
conditional variance.

At a fixed common history, including the seed, let \(K_-\) be the Gram
matrix of previous nodes, \(k=(K_N(z,z_i))_i\), and \(F_-,y_-\) the
previous source and answer vectors. The next conditional law is circular
Gaussian with
\[
\mu_c=cF(z)+kK_-^{-1}(y_--cF_-),\qquad
V=K_N(z,z)-kK_-^{-1}k^*>0.
\tag{15}
\]
For the first query the matrix terms are absent. Adaptive Gaussian
conditioning is justified exactly as in XF-206, (15)–(18): at a common
history all rows are fixed, and conditioning on the next complex linear
measurement leaves an affine Gaussian slice. Decisions and query maps
need only be measurable.

For each fixed history, \(\mu_c-\mu_{1/2}\to0\) as \(c\to1/2\), and
\(V\) is independent of \(c\). Thus the next-kernel total variation tends
to zero. It is bounded by one. The kernel telescoping inequality and
dominated convergence with respect to the fixed midpoint history law
prove
\[
\operatorname{TV}(\mathsf P_c^N,\mathsf P_{1/2}^N)\longrightarrow0.
\tag{16}
\]
Stopped histories are absorbing. Unbounded query locations cause no
problem: every selected point is finite, and convergence is pointwise
at a fixed history. No uniform lower covariance bound or policy-uniform
rate in (16) is needed or claimed.

Given \(\eta>0\), choose \(b>0\) small enough that
\(\Pr(E_1\cap E_2)\ge1-\eta\), omitting \(E_2\) in the unrestricted
class. This is possible since the finitely many weighted coefficient
norms tend to zero in probability with \(b\). Fix \(b\), then condition
the coefficient law on this event and use (11) under the respective
labels. These are mixtures of **fixed admissible analytic inputs**, all
drawn before the policy seed. Their observation curves are
\((1\mp\varepsilon)F/2+P_a\). Conditioning changes each transcript law
by at most \(\eta\), and (16) gives
\[
\operatorname{TV}(\mathsf Q_{0,\varepsilon},\mathsf Q_{1,\varepsilon})
\le2\eta+o_{\varepsilon\to0}(1).
\tag{17}
\]
Gaussian conditioning is used only before this truncation of the prior.
The equal-prior binary error is at least \((1-\operatorname{TV})/2\).
For each fixed capped policy take \(\varepsilon\downarrow0\), then
\(\eta\downarrow0\). Worst-case error over fixed inputs dominates this
average, proving (5). Fair guessing supplies equality. The zero-query
case is immediate.

## Stopping, derivative access, and the Cauchy-integral boundary

Truncating any policy of per-input error at most \(\alpha\) and guessing
fairly at cap \(N\) gives error at most
\(\alpha+\Pr_x(\nu>N)/2\). Equation (5) proves the lower part of (6).
The expectation conclusion follows from
\(\mathbb E_x\nu\ge N\Pr_x(\nu>N)\) for every finite \(N\); it does
not assert one input of infinite expected cost.

The deterministic real-axis certificate of
[[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]]
still applies to every baseline here and uses allowed queries in \(I\).
At zero noise its short-chord loss tends to zero, so it terminates exactly
on each strictly subcritical input. Run it with probability \(1-2\alpha\)
and otherwise guess fairly without queries. This proves sharpness in (6)
and finite expected cost on each particular input, also under (4).

In contrast, an exact derivative oracle at \(Q\) separates the classes in
one call: a null derivative has modulus below \(L_*\), whereas an active
derivative has modulus at least \(D-|B'(Q)|>L_*\). For any sufficiently
small circle in \(\mathbb H\), a supplied exact Cauchy contour integral
also returns that derivative. Such an integral is not a finite collection
of point evaluations. For a fixed finite contour rule, omitted Taylor
coefficients can alias into the first derivative. Equation (8) is the
arbitrary-node version of that missing-derivative freedom.

A known complex neighborhood bound can give arbitrarily accurate Cauchy
quadrature or derivative approximation. It does not supply a positive
label margin. This explains why (4) is consistent with rapid convergence
of complex numerical differentiation and with per-input termination.
A positive supplied slack floor, a prescribed finite-dimensional
calibration model, exact derivative/integral access, or a global analytic
restriction excluding (11) remains outside the obstruction.

## Checks, prior art, and mathematical delta

An exact scratch check over \(\mathbb Q(i)\) tested 96 banks with
\(1\le N\le8\), including 32 banks containing the endpoint and reflected
complex pairs. All evaluation matrices in (7) had full row rank, and all
432 cardinal interpolants constructed by (8) had the required values and
zero endpoint derivative. The old even-power two-row matrix had rank one
on a reflected pair; the repaired \(\{1,s^2,s^3\}\) matrix had rank two.
These checks test the algebra and degeneracies; (8) and (15)–(17) prove
the arbitrary-cap, arbitrary-policy statement. No Lean verification or
new numerical Xi source estimate is claimed.

[[research/prior_art/incremental/PA-hermite-polynomial-interpolation|Hermite interpolation]] is classical: [Carl de Boor, *Divided Differences*
(2005), Proposition 7](https://arxiv.org/pdf/math/0502036) gives its
polynomial formulation. Adaptive conditional Gaussian measures and
truncated-prior lower bounds are classical as well; see [Robert Kunsch,
*High-Dimensional Function Approximation* (2017), §2.2.1, Lemma 2.2](https://arxiv.org/pdf/1704.08213).
The complex Gaussian formula here is the finite-dimensional real Gaussian
formula applied to real and imaginary parts. The testing and stopping
arguments are inherited from XF-206, not claimed as new general theory.

[Folkmar Bornemann, *Accuracy and Stability of Computing High-Order
Derivatives of Analytic Functions by Cauchy Integrals* (2011), §2,
Theorem 2.1](https://arxiv.org/pdf/0910.1841) explicitly gives the
trapezoidal aliasing relation and approximation bound. It establishes
approximation of Taylor coefficients, not uniform exact classification
across a vanishing threshold margin. There is no conflict with that
positive numerical differentiation theory.

The additional result is the closure of XF-206's complex-query escape:
removing only the linear monomial preserves the critical endpoint guard
while leaving arbitrary finite complex values independent. The same
construction fits a fixed positive compact-norm allowance. The complete
Jacobi speed geometry supplies the admissibility budget, but all later
interpolation and probability steps are generic. This rules out these
oracle/regularity changes as uniform-margin repairs of this synthetic
experiment. It establishes neither a physical calibration law, nor an
arithmetic-source coercivity estimate, nor exclusion of a positive
transition time for the Xi flow.
