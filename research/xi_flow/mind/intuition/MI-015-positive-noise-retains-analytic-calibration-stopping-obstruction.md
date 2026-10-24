# MI-015 — Finite-transcript mixtures retain analytic calibration stopping obstructions

**Evidence level:** supported synthesis of [XF-205](../../findings/XF-205-analytic-jacobi-calibration-retains-the-noisy-stopping-obstruction.md), [XF-206](../../findings/XF-206-noiseless-analytic-calibration-retains-sharp-stopping-tails.md), [XF-207](../../findings/XF-207-complex-value-queries-retain-the-analytic-calibration-stopping-obstruction.md), and [XF-203](../../findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping.md). These are exact synthetic observation boundaries using classical testing methods; they supply no physical Xi acquisition or zero-exclusion theorem.

Use the complete singleton Jacobi response and threshold of [MI-014](MI-014-endpoint-preserving-calibration-joins-force-sharp-randomized-stopping-tails.md): on \(I=[Q,2Q]\), fix a minimizing displacement \(\tau_Q\), put \(F=F_{\tau_Q}\), \(D=\|F'\|_\infty>0\), \(L_*=D/2\), and \(K=\|F\|_\infty>0\). Distinct queries observe
\[
y_j=f(r_j)+B(r_j)+e_j,\qquad f=0\text{ or }F_\tau,
\quad \|B'\|_\infty<L_*,\quad \sum_{j\ge1}|e_j|^2\le\sigma^2,
\quad\sigma>0.
\]
The baseline and entire noise sequence are fixed before the policy's seed. Baselines may be required to be holomorphic on the fixed right half-plane. The full source extends there too: on the real axis its normalization is \(G_r=\sqrt\pi\,r(1+r^2)^{-1/4}\), and the nonvanishing factors admit matching analytic branches on that half-plane.

Analyticity excludes the tail joins of MI-014, but the one-dimensional nuisance \(B=cF\), \(c\in\mathbb R\), \(|c|<1/2\), already gives
\[
B_{0,\varepsilon}=(1-\varepsilon)F/2,\quad
B_{1,\varepsilon}=-(1-\varepsilon)F/2,
\qquad (F+B_{1,\varepsilon})-B_{0,\varepsilon}=\varepsilon F
\quad(0<\varepsilon<1).
\]
Both baselines are strictly subcritical and have uniformly bounded holomorphic norms on every fixed compact subset. The two observation classes approach the same excluded midpoint without increasing analytic complexity.

For an arbitrary policy capped at \(N\ge1\) rows, put a prior on fixed noise sequences: independent real and imaginary components uniform on \([-a,a]\) for the first \(N\) rows, zero thereafter, with \(a=\sigma/\sqrt{2N}\). Every sequence obeys the total energy cap. At any common adaptive history the next laws differ by a translation of magnitude at most \(\varepsilon K\). Writing \(U_a\) for the uniform law on that complex square, the overlap bound
\[
\operatorname{TV}(U_a,U_a+d)\le |d|/(\sqrt2a)
\]
and sequential coupling give, for the two prior-averaged transcript laws,
\[
\operatorname{TV}(P_{0,\varepsilon}^{\mathcal A},P_{1,\varepsilon}^{\mathcal A})
\le\min\{1,N^{3/2}\varepsilon K/\sigma\}.
\]
These are mixtures of allowed deterministic inputs, drawn independently of the policy's seed. The worst-case error dominates their average error. Sending \(\varepsilon\downarrow0\) at **fixed** \(N,\sigma>0\) gives capped binary minimax error \(1/2\), even if \(\tau_Q\) and the nuisance direction \(F\) are supplied. The power \(N^{3/2}\) is a sufficient coupling estimate, not an optimal slack-dependent sample rate.

Writing \(\nu\) for the row count, every almost-surely terminating policy with error at most \(0\le\alpha<1/2\) on every input satisfies, by truncation and a fair guess,
\[
\sup_x\Pr_x(\nu>N)\ge1-2\alpha\quad\text{for every finite }N,
\qquad \sup_x\mathbb E_x\nu=\infty.
\]
XF-203 still supplies deterministic finite stopping on each input: for \(n\) distinct short-chord pairs of length \(h\), the source loss \(a(h)=C Q^{-3/2}h\), with certified source constant \(C\), and total-noise contrast bound \(t=(\sigma/h)\sqrt{2/n}\) obey \(a(h)+2t<\delta\) eventually, where \(\delta=L_*-\|B'\|_\infty>0\). Mixing that procedure with an immediate fair guess of probability \(2\alpha\) attains the tail constant with finite expectation on every fixed input. Shrinking the contrast noise uses one global energy allowance, not refreshed noise budgets.

The positive-noise premise is essential to this **one-dimensional** witness. In the restricted known-direction model at \(\sigma=0\), one query at \(F(r_*)\ne0\) yields \(y/F(r_*)=\ell+c\); thresholding at \(1/2\) recovers the label. XF-206 supplies a separate noiseless obstruction in the full holomorphic class by adding polynomial directions that respect the same derivative budget.

For the complete fixed-\(Q\) source, put \(v(r)=|F'(r)|\), \(v(Q)=D\), \(v_{\min}=\min_Iv>0\), and \(\kappa=\min_I(-v')>0\), as proved in XF-201 and retained in MI-014. For a cap \(N\), set \(s=(r-Q)/Q\) and
\[
P_a(r)=\sum_{k=0}^{N-1}a_k s^{2k},\qquad
E=\left\{\sum_{k=1}^{N-1}2k|a_k|\le\kappa Q^2/4\right\}.
\]
On \(E\),
\[
P_a'(Q)=0,\qquad |P_a'(r)|\le\kappa(r-Q)/4\le(D-v(r))/4.
\]
Therefore the holomorphic baselines \(B_{0,\varepsilon,a}=(1-\varepsilon)F/2+P_a\) and \(B_{1,\varepsilon,a}=-(1-\varepsilon)F/2+P_a\) have
\[
\|B_{\ell,\varepsilon,a}'\|_\infty
\le L_*-\varepsilon v_{\min}/2<L_*.
\]
The coefficient room in \(E\) is independent of \(\varepsilon\). Strict decrease of the source speed, rather than holomorphy alone, supplies it.

Draw the complex coefficients once, before the policy's seed, from independent circular Gaussians of variance \(b^2\). Every at-most-\(N\) distinct value bank in the real interval \(I\) has independent evaluation rows: the first square minor is Vandermonde in the distinct \(s_j^2\), including \(s=0\). At every common adaptive history, the next conditional Gaussian variance is positive and the conditional mean varies continuously with the source multiplier in \((1\pm\varepsilon)F/2+P_a\). Kernel total variation and dominated convergence then give convergence of the capped transcript laws as \(\varepsilon\to0\) for each fixed policy and \(b>0\). No uniform lower variance, separated nodes, continuous decision rule or policy-uniform convergence rate is needed.

Choose \(b>0\) small enough that \(\Pr(E^c)\le\eta\), and condition the coefficient prior onto \(E\). Conditioning costs at most \(\eta\) per label in total variation, so the two **admissible noiseless** transcript mixtures satisfy
\[
\operatorname{TV}(Q_{-,\varepsilon},Q_{+,\varepsilon})
\le2\eta+o_{\varepsilon\to0}(1).
\]
First send \(\varepsilon\to0\) at fixed \(b\), then \(\eta\to0\). Every fixed cap has minimax error \(1/2\) even without noise. The same truncation and XF-203 certificate above give the sharp tail \(1-2\alpha\) and finite per-input expectation for an attaining policy for every \(\sigma\ge0\). The polynomial dimension grows with the cap; no fixed pair of analytic curves agrees on an interval, and no input is selected after the realized seed.

Complex queries require a different polynomial space: the even powers agree at reflected points \(s,-s\). XF-207 allows every finite \(z\) in \(\mathbb H=\{\Re z>0\}\), puts \(s=(z-Q)/Q\), and uses
\[
\mathcal P_N=\operatorname{span}_{\mathbb C}\{1,s^2,s^3,\ldots,s^{N+1}\}
=\{P:\deg P\le N+1,\ P'(0)=0\}.
\]
For any \(j\le N\) distinct complex nodes, let \(H\) be the degree-at-most-\(j-1\) interpolant of arbitrary values and \(W(s)=\prod_i(s-s_i)\). Take \(R=W\) if a node is zero, and \(R=sW\) otherwise. Then \(R'(0)\ne0\) and
\[
P=H-\frac{H'(0)}{R'(0)}R
\]
has the prescribed values and zero endpoint derivative, with degree at most \(j+1\le N+1\). Thus every value bank through cap \(N\) remains independent, including reflected pairs, while the derivative at the critical endpoint is unobserved.

For \(P_a=a_0+\sum_{k=2}^{N+1}a_ks^k\), the coefficient region
\(\sum_{k=2}^{N+1}k|a_k|\le\kappa Q^2/4\)
again implies \(|P_a'(r)|\le(D-v(r))/4\) on \(I\). It supplies the same positive room independent of \(\varepsilon\) for the two near-midpoint baselines. Even a supplied compact bound \(\|B\|_{\mathcal K}\le M\), with fixed compact \(\mathcal K\subset\mathbb H\) and \(M>\|F\|_{\mathcal K}/2\), leaves this room: impose additionally
\[
|a_0|+\sum_{k=2}^{N+1}A_{\mathcal K}^k|a_k|
\le M-\|F\|_{\mathcal K}/2,\qquad
A_{\mathcal K}=\max\{1,\sup_{z\in\mathcal K}|(z-Q)/Q|\}.
\]
A sufficiently small positive Gaussian scale satisfies both constraints with probability at least \(1-\eta\). Positive conditional variances and the same fixed-history limit then give \(\operatorname{TV}\le2\eta+o_{\varepsilon\to0}(1)\), even for unbounded adaptive complex locations. Only pointwise convergence at finite queried coordinates is used. Hence the noiseless capped error \(1/2\) and sharp tail \(1-2\alpha\) persist, also with that fixed compact-norm bound. The real-axis certificate remains an allowed attaining procedure.

The smaller known-direction class still admits its one-query noiseless test. For the affine control \(F(r)=D(r-Q)\), \(\kappa=0\) and two endpoint values distinguish the derivative-budget classes; this polynomial-room argument does not apply. A supplied positive slack floor gives a uniform finite short-chord certificate, while a derivative oracle at \(Q\) distinguishes by the threshold \(L_*\). An exact Cauchy contour integral can supply that derivative, but a finite value quadrature only approximates it. A compact analytic norm bound can control the approximation error without supplying a positive label margin. The obstruction does not cover a bound excluding the midpoint, a different global analytic restriction, or every prescribed finite-dimensional calibration law.
