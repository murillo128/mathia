# MI-015 — Positive noise retains the analytic calibration stopping obstruction

**Evidence level:** supported synthesis of [XF-205](../../findings/XF-205-analytic-jacobi-calibration-retains-the-noisy-stopping-obstruction.md) and [XF-203](../../findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping.md). This is an exact synthetic observation boundary; it supplies no physical Xi acquisition or zero-exclusion theorem.

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

The positive-noise premise is essential to this witness. In the restricted known-direction model at \(\sigma=0\), one query at \(F(r_*)\ne0\) yields \(y/F(r_*)=\ell+c\); thresholding at \(1/2\) recovers the label. Thus the result neither settles the noiseless full analytic class nor rules out smaller classes excluding the near-critical direction, a supplied positive slack floor, or another precision interface. A fixed analytic domain alone does not provide the required quantitative separation.
