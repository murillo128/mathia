---
type: theorem
research_line: xi_flow
finding_id: XF-203
status: canonical
---

# XF-203 — Unknown Jacobi calibration slack admits finite certified stopping

**Evidence:** EXACT-DERIVED + CLASSICAL-SEQUENTIAL-CERTIFICATE + SYNTHETIC-ACQUISITION-BOUNDARY. In the complete singleton Jacobi experiment of XF-201/202, a promise of strictly subcritical calibration suffices for input-dependent finite detection, even under a known positive **total** squared-noise budget. The procedure needs no supplied calibration margin and uses finite, explicit inequalities rather than an oracle for nuisance-class feasibility. No uniformly bounded number of adaptive rows suffices, already without noise. In the small-slack regime at fixed source and positive noise budget, the procedure retains the known-slack quartic row-cost order. These are acquisition statements; physical Xi access and a zero-sensitive implication remain missing.

## Exact experiment and quantifiers

Fix \(0<\tau_0\le1/4\), sufficiently large integer \(Q\), and
\[
T=[-1/4,-\tau_0]\cup[\tau_0,1/4],\qquad I_Q=[Q,2Q].
\]
Keep the full response, including its reciprocal term,
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),&G_r&=|x_r|^{-1/2},\\
F_\tau(r)&=\frac2{G_r}
 \left(e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r}\right)
 -\frac{2x_r^{-1/2}}{G_r}
 \left(e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}\right).
\end{aligned}
\tag{1}
\]
The square root is principal. On this interval \(G_r>1\), so this is also the max-normalized convention of XF-201. Its exact threshold is
\[
D=\min_{\tau\in T}\|F_\tau'\|_\infty
 =\min_{\tau\in T}|F_\tau'(Q)|>0,\qquad L_*=D/2.
\tag{2}
\]
The equality in (2), not just positivity, is the source-specific input: all full-response speeds decrease strictly away from the same endpoint, as proved in XF-201.

Rows are observations
\[
y_j=f(r_j)+B(r_j)+e_j,\qquad
f=0\ \text{or}\ f=F_\tau,\qquad
B\in C^1(I_Q;\mathbb C),\quad L:=\|B'\|_\infty<L_*,
\quad \sum_{j\ge1}|e_j|^2\le\sigma^2.
\tag{3}
\]
Here \(\sigma\ge0\) is known. One baseline and one noise sequence serve the whole experiment. The constant of \(B\) is unrestricted, and competing labels may have different baselines. The actual margin
\[
\delta=L_*-L>0
\tag{4}
\]
is not supplied. Rows must be distinct and can be arbitrarily close. The source family and exact threshold are known in the same mathematical observation model as XF-201/202.

There is one deterministic procedure, independent of \(L\), that terminates with the correct label on every input (3). Its positions can be prescribed in advance; only stopping depends on the responses. For every finite \(N\), no deterministic procedure using at most \(N\) rows on every admitted input can do this. This remains true when \(\sigma=0\), and allows response-dependent positions and stopping.

## A uniform short-chord bound for the complete complex source

Put \(v_\tau=|F_\tau'|\) and \(u_\tau=F_\tau'/v_\tau\). The full-response bounds of XF-201, (6), give
\[
v_\tau\asymp Q^{-1/2},\qquad
0<-v_\tau'\le C Q^{-3/2},\qquad |u_\tau'|\le C.
\tag{5}
\]
They include the reciprocal term through its exponentially small, differentiated envelope; it is not dropped in (1). The unit-vector identity gives, for \(t\ge0\) close to zero,
\[
\begin{aligned}
\operatorname{Re}\bigl(F_\tau'(Q+t)\overline{u_\tau(Q)}\bigr)
&=v_\tau(Q+t)\left(1-\tfrac12|u_\tau(Q+t)-u_\tau(Q)|^2\right)\\
&\ge D-C_1Q^{-3/2}t-C_2Q^{-1/2}t^2.
\end{aligned}
\tag{6}
\]
Thus there is a known source-bound constant \(A>0\), depending only on the fixed \(\tau_0\), such that, whenever
\[
0<h\le h_0:=\frac1{4Q},\qquad 0<z<h/4,
\]
the normalized chord satisfies
\[
\operatorname{Re}\left(
 \frac{F_\tau(Q+z+h)-F_\tau(Q+z)}h
 \overline{u_\tau(Q)}\right)
\ge D-a(h),\qquad a(h):=A Q^{-3/2}h.
\tag{7}
\]
Indeed every integration point has \(t\le5h/4\), and \(Qh\le1/4\) absorbs the quadratic turning loss into the linear term. Increasing \(A\) preserves the assertion. The direction in (7) may depend on \(\tau\); the contrast, nodes and stopping thresholds below do not.

All these are exact inequalities for sufficiently large \(Q\). In particular no asymptotic error is subtracted from the unknown margin. For effective use at a specified \(Q\), the source bound \(A\) must be certified from (1) or the envelope bounds, rather than guessed from a floating-point sample.

## A finite exclusion certificate with total noise

At scale \(h\), take \(n\) pairs
\[
(Q+z_j,Q+z_j+h),\qquad 0<z_j<h/4,
\]
whose \(2n\) coordinates are distinct. Define the observed complex contrast
\[
Z=\frac1{nh}\sum_{j=1}^n
\bigl(y(Q+z_j+h)-y(Q+z_j)\bigr),\qquad
t=\frac{\sigma}{h}\sqrt{\frac2n}.
\tag{8}
\]
Its coefficient vector has squared norm \(2/(nh^2)\). Cauchy–Schwarz therefore bounds its noise contribution by \(t\), for arbitrary complex errors satisfying (3). The common baseline contributes a vector of modulus at most \(L<L_*\), by integrating \(B'\) in every pair. Averaging (7) preserves its common projection direction and hence gives a source contribution of modulus at least \(D-a(h)\).

Use the two tests
\[
\begin{array}{ll}
|Z|>L_*+t &\Longrightarrow\ \text{report active},\\[2mm]
|Z|<L_*-a(h)-t &\Longrightarrow\ \text{report null}.
\end{array}
\tag{9}
\]
Otherwise continue. The tests are disjoint. They are sufficient certificates, not a claimed exact characterization of all feasible labels.

The first test excludes every admissible null baseline, since a null input satisfies \(|Z|<L_*+t\). The second excludes every admissible active input, since an active input satisfies \(|Z|>D-a(h)-L_*-t=L_*-a(h)-t\). These are exclusions against the entire union of strictly subcritical budgets, not only a provisional guessed budget. The true experiment is never discarded.

For the actual margin (4), stronger bounds hold:
\[
\begin{array}{ll}
\text{null:}& |Z|\le L_*-\delta+t,\\
\text{active:}& |Z|\ge L_*+\delta-a(h)-t.
\end{array}
\tag{10}
\]
Consequently the correct test in (9) succeeds whenever
\[
a(h)+2t<\delta.
\tag{11}
\]
No continuity modulus for \(B'\), second derivative of \(B\), or real ordering of the source phases was used.

## One margin-independent procedure and its cost

Set \(h_k=h_0 2^{-k}\), \(a_k=AQ^{-3/2}h_k\), and
\[
n_k=\max\left\{1,\left\lceil\frac{2\sigma^2}{h_k^2a_k^2}\right\rceil\right\}.
\tag{12}
\]
For block \(k\), choose \(n_k\) distinct rational starts in \((0,h_k/4)\), excluding the finitely many starts that would duplicate a previously queried coordinate or its translate by \(h_k\). A fixed enumeration of rationals makes this deterministic and independent of the responses. There are always enough starts. This supplies one infinite bank of distinct rows; only a finite prefix is used on any promised input.

At each completed block evaluate (8)–(9). By (12), \(t_k\le a_k\to0\). Hence \(3a_k<\delta\) eventually, and (11) proves finite termination. At zero noise, \(n_k=1\) and the same argument applies.

The single bound \(\sum_{j\ge1}|e_j|^2\le\sigma^2\) implies the bound for every block. Reusing this upper bound in a conservative certificate does not grant fresh noise to the adversary: no proof step chooses a new noise sequence or resets its spent energy. Independence, zero mean and probabilistic cancellation are not assumed.

There is also a useful quantitative comparison. If \(0<\delta\le a_0\), the first \(k_*\) with \(3a_{k_*}<\delta\) has
\[
\delta/6\le a_{k_*}<\delta/3,\qquad
k_*+1=O\left(1+\log\frac{a_0}{\delta}\right).
\]
Since \(h_k=a_kQ^{3/2}/A\), (12) and summation of a geometric series give the sufficient total row bound
\[
\sum_{k=0}^{k_*}2n_k
\le C\left(1+\log\frac{a_0}{\delta}
              +\frac{\sigma^2 A^2}{Q^3\delta^4}\right).
\tag{13}
\]
For larger margins the same procedure still terminates; (13) is stated only in its near-threshold regime. With \(\varepsilon=\delta/L_*\), \(D\asymp Q^{-1/2}\) turns the last term into \(O(\sigma^2/(Q\varepsilon^4))\). For fixed sufficiently large \(Q\) and fixed \(\sigma>0\), as \(\varepsilon\downarrow0\) this dominates the logarithmic block overhead. XF-201's matching lower bound applies to the subfamily \(\|B'\|_\infty\le(1-\varepsilon)L_*\), on which any procedure for (3) must also be correct. Thus the unknown-margin procedure has the same quartic worst-case order on that subfamily in this limit. This does not assert optimal zero-noise depth or optimal unknown-margin cost throughout XF-202's larger-slack crossover regimes.

## Every uniform finite query cap fails

Choose an exact minimizer \(\tau_Q\) in (2), and write \(F=F_{\tau_Q}\). Run any deterministic policy along the hypothetical midpoint transcript \(y(r)=F(r)/2\). For any finite nonempty prefix, sort its distinct rows as \(r_1<\cdots<r_m\). If \(m\ge2\),
\[
K=\max_{j<m}\frac{|F(r_{j+1})-F(r_j)|}{r_{j+1}-r_j}<D.
\tag{14}
\]
Indeed \(|F'(r)|<D\) for every \(r>Q\), and its value \(D\) at the single endpoint does not saturate any positive-length integral. This remains true when a queried row is exactly \(Q\).

There is a complex \(C^1\) interpolant \(b\) with \(b(r_j)=F(r_j)\) and \(\|b'\|_\infty<D\). For completeness, linearly interpolate the data and extend constantly outside the extreme nodes. This gives a global \(K\)-Lipschitz complex function. Convolution with a smooth nonnegative approximate identity does not increase its Lipschitz bound and converges uniformly. Correct its finitely many interpolation errors by fixed smooth cardinal functions. Their derivative contribution tends to zero, so (14) leaves room to keep the final derivative norm below \(D\). Restrict to \(I_Q\). For \(m=1\), use a constant interpolant.

Two fixed admissible noiseless experiments then realize the whole prefix:
\[
\text{null: }B_0=b/2,\qquad
\text{active: }B_1=-b/2,\ f=F.
\tag{15}
\]
Both return \(F(r_j)/2\). The chosen baseline is fixed across all queries in its realization. A deterministic policy follows the same path and cannot stop correctly on this prefix. If it has not stopped by a purported uniform cap \(N\), either realization of its first \(N\) rows violates that cap. This proves the lower assertion even for adaptive positions and even without noise.

The witness in (15) may depend on the finite prefix. The infinite midpoint curve would require critical calibration, which is excluded. The argument therefore rules out a uniform bound, not input-dependent finite termination. It is consistent with (9) never stopping on the inadmissible infinite midpoint transcript.

## Effective stopping, checks and prior art

In the exact-value model, (8)–(12) are finite arithmetic and strict inequalities. No optimization over all \(C^1\) nuisances or over the unknown displacement is required at a stopping step. If observations instead come with arbitrarily refinable certified value enclosures, the same conclusion is effective provided the source threshold and bounds also have such certified access. These enclosures refine the same observed values, rather than taking fresh noisy measurements at old coordinates. At block \(k\), enclose \(Z\) and \(L_*\) with errors tending to zero, for example at most \(a_k/10\), and stop only when one strict inequality is certified. Do a finite refinement at each block and continue if undecided; do not wait forever on a possible equality. Equations (10)–(11) give a fixed positive true margin eventually, so the extra enclosure widths cannot prevent termination. Integer multiplicities can be rounded upward using certified upper bounds. A fixed precision floor or coordinate error is a different observation model and is not covered.

A scratch 55-decimal audit evaluated the complete expression (1) and projected short chords at \(Q\in\{32,64,128\}\), \(\tau\in\{-1/4,-1/10,1/10,1/4\}\), \(h=(4Q)^{-1}2^{-k}\) for \(k\in\{0,4,12\}\), and \(z/h\in\{0,1/8,1/4\}\). The 108 scaled losses \(Q^{3/2}(v_\tau(Q)-\operatorname{Re}(\mathrm{chord}\,\overline{u_\tau(Q)}))/h\) ranged from approximately 0.0619995 to 0.246702. This checks the scale and sign of the loss in (7), not a uniform certified value of \(A\). The analytic estimates (5)–(7) carry the theorem, including the reciprocal contribution. All 2,592 exact rational certificate cases passed. These checks on the control \(F(t)=t-t^2/2\), \(0\le t\le1/2\), tested the contrast norm, the two exclusions, and the sufficient stopping inequality with bounded constant-slope baselines and extreme-sign contrast errors. Neither control establishes a physical Xi interface.

The distinction between fixed and response-dependent information cardinality is classical: [G. W. Wasilkowski, *Information of varying cardinality*, Journal of Complexity 2 (1986), 204–228](https://doi.org/10.1016/0885-064X(86)90002-6), studies it for linear problems on Banach spaces. Those general optimality conclusions are not imported into this discrete-label union of open nuisance classes. Finite-difference differentiation with noise is also classical; [Jorge J. Moré and Stefan M. Wild, *Estimating Derivatives of Noisy Simulations*, ANL/MCS-P1785-0810](https://optimization-online.org/wp-content/uploads/2010/11/2787.pdf), uses an iid stochastic noise model and balances differencing error against noise. Here the coefficient estimate is a deterministic Cauchy–Schwarz bound for one global squared-noise budget. No general novelty is claimed for sequential testing, differentiation, interpolation or averaging.

The local clue's authorized AF-575 transfer supplies the finite-transcript question, not an imported theorem about this complex source. Its positive supremum-noise obstruction does not apply to (3). The destination proof combines the common endpoint speed of the complete Jacobi response with increasingly populated distinct-row clusters and an explicit exclusion certificate. The mathematical change from XF-201/202 is that a supplied slack is unnecessary for eventual reliable detection. Arbitrarily fine coordinate access, a known total-noise cap, and certified source constants remain essential interface assumptions. This result neither excludes an off-critical Xi zero nor constrains the transition time \(\Lambda\).
