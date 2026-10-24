# MI-014 — Endpoint-preserving calibration joins force sharp randomized stopping tails

**Evidence level:** supported synthesis of [XF-201](../../findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost.md), [XF-203](../../findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping.md), and [XF-204](../../findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail.md). These are exact synthetic acquisition results, with no physical Xi sampling or zero-exclusion conclusion.

Fix sufficiently large integer \(Q\), \(0<\tau_0\le1/4\), and \(T=[-1/4,-\tau_0]\cup[\tau_0,1/4]\). The complete singleton Jacobi response on \(I=[Q,2Q]\) is
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),\qquad G_r=|x_r|^{-1/2},\\
F_\tau(r)&=\frac2{G_r}\bigl(e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r}\bigr)
-\frac{2x_r^{-1/2}}{G_r}\bigl(e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}\bigr).
\end{aligned}
\]
Use the principal square root. XF-201 proves that the **full** speed \(v_\tau=|F_\tau'|\) decreases strictly from \(Q\), including the differentiated reciprocal term. Consequently
\[
D=\min_{\tau\in T}|F_\tau'(Q)|=\min_{\tau\in T}\|F_\tau'\|_\infty>0,
\qquad L_*=D/2.
\]
Observe \(f+B\) at distinct coordinates, where \(f=0\) or \(F_\tau\), \(B\in C^1(I;\mathbb C)\), and \(\|B'\|_\infty<L_*\). Its constant is unrestricted and its positive slack is unknown. The queryable endpoint \(Q\) prevents directly importing a Taylor-extension witness that only agrees on a tail.

The repair is a strict **value-and-derivative join**. Choose an exact minimizer \(\tau_Q\), set \(F=F_{\tau_Q}\), and for \(0<u<Q\) write
\[
s=\frac{F(Q+u)-F(Q)}u,\quad v=F'(Q+u),\quad
\gamma=D-|s|>0,\quad a=\frac\gamma{4D},\quad
c=\frac{s-av}{1-a}.
\]
Strict speed decrease gives \(|s|,|v|<D\), and
\[
|c|\le D-\frac\gamma{2(1-a)}<D.
\]
On \([0,u]\), take \(\eta=0\) until \((1-2a)u\), then increase linearly to one. It has integral \(au\). The velocity \(w=(1-\eta)c+\eta v\) stays strictly inside the complex disk of radius \(D\), ends at \(v\), and has integral \(us\). Integrate it from \(F(Q)\) and join to \(F\) at \(Q+u\). The resulting \(J_u\in C^1(I;\mathbb C)\) satisfies
\[
\|J_u'\|_\infty<D,\qquad J_u(Q)=F(Q),\qquad
J_u=F\text{ on }[Q+u,2Q].
\]
The null baseline \(J_u/2\) and active baseline \(-J_u/2\) therefore produce the same midpoint \(F/2\) at the endpoint and throughout the tail. Both inputs are fixed before the random seed. For every capped policy, the probability that its finite midpoint transcript enters \((Q,Q+u)\) tends to zero as \(u\downarrow0\); endpoint queries do not help.

Writing \(\nu_x\) for the row count, the shared transcript gives capped minimax binary error \(1/2\). Truncation followed by a fair guess then forces, for every almost-surely terminating policy with error at most \(\alpha<1/2\) on each input,
\[
\sup_x\mathbb P_x(\nu_x>N)\ge1-2\alpha\quad\text{for every finite }N,
\qquad \sup_x\mathbb E_x\nu_x=\infty.
\]
These are suprema over inputs; they do not assert one input with infinite expected cost.

XF-203 supplies the matching pointwise finite procedure even with known total noise \(\sum_j|e_j|^2\le\sigma^2\). Average \(n\) differences on distinct pairs \((Q+z_j,Q+z_j+h)\), \(0<z_j<h/4\), divided by \(h\), obtaining \(Z\). The noise bound is \(t=(\sigma/h)\sqrt{2/n}\). For \(h\le1/(4Q)\), each full-source chord projected onto \(F_\tau'(Q)/|F_\tau'(Q)|\) is at least \(D-a(h)\), where \(a(h)=C Q^{-3/2}h\) and \(C\) is a certified source constant. This common projection survives averaging, although its direction depends on the unknown \(\tau\). Sound certificates using only the modulus are
\[
|Z|>L_*+t\ \Rightarrow\ \text{active},\qquad
|Z|<L_*-a(h)-t\ \Rightarrow\ \text{null}.
\]
For the actual \(\delta=L_*-\|B'\|_\infty>0\), one succeeds when \(a(h)+2t<\delta\). Shrinking \(h\) and increasing \(n\) give finite stopping on every input without knowing \(\delta\). This uses one global energy cap, not independent noise or replenished block budgets. Mixing that exact procedure with a zero-query fair guess of probability \(2\alpha\) attains the tail constant \(1-2\alpha\) simultaneously for all finite \(N\), with finite expected cost at each input. The noiseless witnesses already prove the lower bound for every \(\sigma\ge0\).

The join exposes two precise boundaries. For the affine source \(F(r)=D(r-Q)\), the endpoint and tail values force average speed \(D\), so the strict join is impossible; two noiseless value queries distinguish the labels. Requiring analytic baselines also forbids this particular tail agreement by the identity theorem. [MI-015](MI-015-positive-noise-retains-analytic-calibration-stopping-obstruction.md) retains the different finite-transcript mixture mechanisms: XF-205 needs positive total noise only along the known direction \(B=cF\), whereas XF-206 obtains the same capped minimax and stopping-tail laws noiselessly in the full holomorphic class. The latter adds polynomials in \(((r-Q)/Q)^2\) whose derivatives vanish at \(Q\); the strict speed decrease supplies coefficient room independent of the shrinking slack. Analyticity blocks exact tail gluing but not this transcript-mixture obstruction. A supplied positive slack floor, a derivative oracle, fixed precision, or constrained coordinate access changes the experiment.
