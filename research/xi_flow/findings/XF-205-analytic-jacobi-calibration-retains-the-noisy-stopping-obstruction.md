---
type: theorem
research_line: xi_flow
finding_id: XF-205
status: canonical
---

# XF-205 — Analytic Jacobi calibration retains the noisy stopping obstruction

**Evidence:** EXACT-DERIVED + CLASSICAL-TWO-POINT-TESTING + SYNTHETIC-ACQUISITION-BOUNDARY. For every positive total noise allowance, replacing the unknown strictly subcritical calibration by a holomorphic function does not restore a uniform randomized row bound. The obstruction already occurs in one known scalar calibration direction. It does not require the nonanalytic tail joins of XF-204. Exact finite stopping on each input survives, with the same sharp worst-case stopping-tail constant. No physical Xi acquisition or zero-exclusion conclusion follows.

## Experiment and claim

Fix sufficiently large integer \(Q\), \(0<\tau_0\le1/4\),
\(I=[Q,2Q]\), and \(T=[-1/4,-\tau_0]\cup[\tau_0,1/4]\).
Retain the complete response
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
The square root on real \(r>0\) is principal. By
[[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]],
\[
D=\min_{\tau\in T}\|F_\tau'\|_{C(I)}
 =\min_{\tau\in T}|F_\tau'(Q)|>0,\qquad L_*=D/2,
\tag{2}
\]
and a minimizer \(\tau_Q\) exists. Write \(F=F_{\tau_Q}\) and
\(K=\|F\|_{C(I)}>0\).

Fix \(\sigma>0\). An input fixes a label \(\ell\in\{0,1\}\), a source \(f=0\) or
\(f=F_\tau\), a baseline \(B\), and a complex sequence \(e\), before the
policy's random seed is drawn. Its distinct value queries return
\[
y_j=f(r_j)+B(r_j)+e_j,\qquad r_j\in I,\qquad
\sum_{j\ge1}|e_j|^2\le\sigma^2.
\tag{3}
\]
Restrict baselines to functions holomorphic on the **fixed** right half-plane,
with \(\|B'\|_{C(I)}<L_*\). Their positive derivative slack is not supplied.
Call this input class \(\mathcal X^{\mathrm{hol}}_\sigma\). No bound outside
\(I\) is assumed. The result also holds for baselines holomorphic only on a
fixed neighborhood of \(I\) to which all the sources extend.

For every finite row cap \(N\), measurable adaptive randomized policies obey
\[
\boxed{\inf_{\mathcal A:\nu\le N}
 \sup_{x\in\mathcal X^{\mathrm{hol}}_\sigma}
 \mathbb P_x(\widehat\ell\ne\ell)=\tfrac12.}
\tag{4}
\]
Here probability for a fixed input is over the policy's seed only. For
\(0\le\alpha<1/2\), let \(\mathfrak A_\alpha\) be the policies that terminate
almost surely on each input and have error at most \(\alpha\) on each input.
Then, for every finite \(N\ge0\),
\[
\boxed{\inf_{\mathcal A\in\mathfrak A_\alpha}
 \sup_{x\in\mathcal X^{\mathrm{hol}}_\sigma}
 \mathbb P_x(\nu>N)=1-2\alpha,}
\qquad
\sup_x\mathbb E_x\nu=\infty\quad(\mathcal A\in\mathfrak A_\alpha).
\tag{5}
\]
One policy attains the tail equality for all finite \(N\) and has finite
expected cost on every particular input.

## One analytic calibration direction suffices

The apparently nonholomorphic normalization in (1) causes no obstacle. On
positive real \(r\),
\[
G_r=\sqrt\pi\,r(1+r^2)^{-1/4}.
\tag{6}
\]
On \(\operatorname{Re}r>0\), the functions \(r\), \(1+r^2\), and
\(x_r=(1+ir)/(\pi r^2)\) are holomorphic and nonzero. This simply connected
domain admits analytic logarithms, with branches matching (6) and the
principal \(x_r^{-1/2}\) on the positive real axis. Thus every full
\(F_\tau\), including its reciprocal exponential, extends holomorphically
to that same domain.

For \(0<\varepsilon<1\), choose the two fixed baselines
\[
B_{0,\varepsilon}=(1-\varepsilon)F/2,
\qquad B_{1,\varepsilon}=-(1-\varepsilon)F/2.
\tag{7}
\]
Their derivative norms are \((1-\varepsilon)L_*<L_*\). Null and active
noiseless observations are respectively
\[
m_{0,\varepsilon}=(1-\varepsilon)F/2,
\qquad m_{1,\varepsilon}=(1+\varepsilon)F/2,
\qquad \|m_{1,\varepsilon}-m_{0,\varepsilon}\|_{C(I)}=\varepsilon K.
\tag{8}
\]
They approach the same excluded midpoint. These baselines are scalar
multiples of a known function, with uniform holomorphic bounds on every
fixed compact subset of the half-plane. Neither the domain nor analytic
complexity degenerates as \(\varepsilon\downarrow0\).

In particular the lower bound will still apply if \(\tau_Q\) is revealed
and the entire nuisance class is restricted to
\(B=cF\), \(c\in\mathbb R\), \(|c|<1/2\).

## Fixed bounded-energy noise defeats every capped adaptive policy

For \(N\ge1\), put \(a=\sigma/\sqrt{2N}\). Under either label use a prior
on **fixed input sequences**: for \(1\le j\le N\), take independent real
and imaginary parts of \(e_j\), uniform on \([-a,a]\), and set \(e_j=0\)
afterwards. Every sequence in its support satisfies
\[
\sum_j|e_j|^2\le 2Na^2=\sigma^2.
\tag{9}
\]
The sequence is drawn before and independently of the policy's seed. This
is a lower-bound mixture of allowed deterministic inputs, not a change to
the experiment's noise assumptions.

If \(U_a\) is uniform on the complex square \([-a,a]+i[-a,a]\), then
for any \(d\in\mathbb C\), direct intersection of the two squares gives
\[
\operatorname{TV}(U_a,U_a+d)
\le\min\left\{1,\frac{|\operatorname{Re}d|+|\operatorname{Im}d|}{2a}\right\}
\le\min\{1,|d|/(\sqrt2a)\}.
\tag{10}
\]
Total variation here is \(\sup_A|P(A)-Q(A)|\), half the density \(L^1\)
distance.

Include the seed in the transcript. At an identical history, both policies
make the same next query or stopping decision. The fresh noise coordinate
has law \(U_a\) independently of that history. Conditional observation
laws differ only by the shift \(\varepsilon F(r_j)\), so (10) bounds their
total variation by \(\varepsilon K\sqrt N/\sigma\), uniformly over every
possible common history. Couple these transition kernels successively,
or telescope their total variations. Stopped histories are absorbing and
have identical next transitions. The two prior-averaged full transcript
laws therefore satisfy
\[
\operatorname{TV}(P_{0,\varepsilon}^{\mathcal A},
                  P_{1,\varepsilon}^{\mathcal A})
\le\min\{1,N^{3/2}\varepsilon K/\sigma\}.
\tag{11}
\]
No continuity of the policy's decision boundaries or query map is used.
Its rules are defined measurably on every finite history, as in XF-204.
An almost-sure cap on all admitted inputs can first be enforced on all
histories by truncation.

For any binary decision, its average error under equal prior label weights
is at least \((1-\operatorname{TV})/2\). Thus
\[
\sup_{x\in\mathcal X^{\mathrm{hol}}_\sigma}
 \mathbb P_x(\widehat\ell\ne\ell)
\ge\frac{1-\min\{1,N^{3/2}\varepsilon K/\sigma\}}2.
\tag{12}
\]
The left side dominates the average over the fixed noise sequences; no
sequence is selected after seeing the seed. Letting \(\varepsilon\downarrow0\)
proves (4). For \(N=0\), the labels are indistinguishable without this
construction. A fair guess supplies the upper bound in all cases.

The exponent in (11) is only a convenient finite-cap estimate, not an
optimal slack-dependent lower rate. Its purpose is convergence to zero at
each fixed \(N\).

## Finite stopping and the sharp tail

For any policy with per-input error at most \(\alpha\), truncate at \(N\)
and guess fairly if it has not stopped. On each fixed input its error is
at most \(\alpha+\tfrac12\mathbb P_x(\nu>N)\). Equation (4) forces the
lower bound \(1-2\alpha\) in (5). Also
\(\mathbb E_x\nu\ge N\mathbb P_x(\nu>N)\), giving the infinite supremum
of expectations. This does not assert infinite expected cost on one input.

For the upper bound restrict
[[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]]'s
deterministic certificate to the holomorphic subclass. With \(n\) distinct
short-chord pairs of length \(h\), its contrast \(Z\) has error at most
\(t=\sigma\sqrt{2/n}/h\). The full source has chord loss
\(a(h)=A Q^{-3/2}h\), with a certified source constant \(A\). Its tests are
\[
|Z|>L_*+t\Rightarrow\text{active},\qquad
|Z|<L_*-a(h)-t\Rightarrow\text{null}.
\tag{13}
\]
For the fixed input's \(\delta=L_*-\|B'\|_{C(I)}>0\), one succeeds once
\(a(h)+2t<\delta\). A predetermined sequence \(h\downarrow0\) with enough
distinct pairs per scale meets this condition in finitely many rows.
Holomorphic baselines obey all hypotheses of that proof. It uses the one
global energy cap; there is no replenished noise allowance.

Run this exact finite procedure with probability \(1-2\alpha\), and
otherwise guess fairly without querying. Its error is exactly \(\alpha\)
and its tail is at most \(1-2\alpha\). Its deterministic branch must have
unbounded counts on the present subclass, by (4), so the tail supremum
equals \(1-2\alpha\) for every finite \(N\). Per-input expectation remains
finite. The same reasoning applies to the restricted \(B=cF\) experiment.

## Audit, prior art, and the remaining boundary

An exact rational scratch check verified (10) for 19,683 translated-square
cases. A separate adaptive control used \(F(r)=(1+r)(1+i)\) on \([0,1]\),
first query \(r=0\), and second query \(r=1\) if
\(\operatorname{Re}y_1\ge1/2\), otherwise \(r=1/2\). With square half-width
\(1/2\), both noise coordinates together have energy at most one.
For \(\varepsilon=2^{-k}\), \(1\le k\le12\), exact integration of the two
piecewise-constant joint densities verified the bound
\(\operatorname{TV}\le\min\{1,8\varepsilon\}\) from (11).
These checks test the overlap constants and a response-dependent policy;
the arbitrary-policy claim follows from the kernel argument, not the
finite cases or the affine control.

The testing mechanism is classical. [Bin Yu, *Assouad, Fano, and Le Cam*
(1997), §29.2, Lemma 1, pp. 424–425](https://web.stanford.edu/class/stats300a/REFS/yu1997assouad.pdf)
uses separation of mixtures and probability affinity for lower bounds.
Equations (9)–(12) give the bounded-total-energy adaptive realization here.
[Kunsch, Novak and Rudolf, *Solvable integration problems and optimal
sample size selection* (2019), §§1 and 3.4](https://arxiv.org/abs/1805.08637)
already separate finite cost for each input from infinite worst-case cost.
Their integration theorem is not substituted for this binary experiment.
No novelty is claimed for total variation, the mixture lower bound,
sequential coupling, or the truncation argument inherited from XF-204.

The mathematical delta is the analytic-class boundary. XF-204's noiseless
tail join is excluded by the identity theorem, but positive noise supplies
a different obstruction using only a scalar multiple of the complete
source. Requiring a known analytic domain, or analytic bounds that still
admit (7), is therefore insufficient for uniform noisy detection. A
source-derived calibration law must separate the two observation classes
quantitatively or exclude this near-critical direction.

The assumption \(\sigma>0\) is essential to this proof. Indeed, in the
restricted known-source experiment \(B=cF\), \(|c|<1/2\), a single noiseless
query at any known \(r_*\) with \(F(r_*)\ne0\) returns
\(y/F(r_*)=\ell+c\). Thresholding at \(1/2\) determines the label exactly.
Such a point exists because \(D>0\). Thus this one-dimensional witness
does **not** prove a noiseless analytic-class lower bound. The theorem also
does not cover prescribed smaller calibration classes excluding (7), a
supplied positive slack floor, derivative oracles, or a different precision
interface. It supplies no new physical Xi source law or bound on
\(\Lambda\).
