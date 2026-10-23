---
type: theorem
research_line: xi_flow
finding_id: XF-201
status: canonical
---

# XF-201 — Vanishing Jacobi calibration slack has quartic row cost

**Evidence:** EXACT-DERIVED + CLASSICAL-APPROXIMATION-MECHANISM + SYNTHETIC-ACQUISITION-BOUNDARY. In XF-200's singleton experiment with first-derivative calibration and \(\alpha=1\), the near-critical total-noise row cost is sharp in the joint regime \(0<\varepsilon\le Q^{-2}\). The surviving curve separation is \(\asymp\sqrt Q\,\varepsilon^2\), and deterministic detection costs \(\asymp\sigma^2/(Q\varepsilon^4)\) rows for fixed \(\sigma>0\). The lower bound allows adaptive sampling. This resolves a shrinking-slack regime, not the intervening phase-rotation regimes or physical Xi access.

## Exact experiment and theorem

Fix \(0<\tau_0\le1/4\), and put
\[
T=[-1/4,-\tau_0]\cup[\tau_0,1/4],\qquad I_Q=[Q,2Q].
\]
For an integer \(Q\) sufficiently large, retain the complete normalized response
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),\qquad G_r=\max\{1,|x_r|^{-1/2}\},\\
F_\tau(r)&=\frac2{G_r}
 \bigl(e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r}\bigr)
 -\frac{2x_r^{-1/2}}{G_r}
 \bigl(e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}\bigr).
\end{aligned}
\tag{1}
\]
The square root is principal. The labels are null, with response zero, and active, with response \(F_\tau\) for unknown \(\tau\in T\). There is exactly one edited symmetric unit-weight pair. An observation is
\[
y_j=f(r_j)+B(r_j)+e_j,\qquad
B\in C^1(I_Q;\mathbb C),\quad\|B'\|_\infty\le L,
\quad\sum_j|e_j|^2\le\sigma^2.
\tag{2}
\]
The baseline is shared across rows within each experiment, its constant is unrestricted, and competing labels may use different baselines. Rows must be distinct but may be arbitrarily close. The derivative budget is in \(r\), after normalization.

Use the **exact finite-\(Q\)** threshold and relative slack
\[
D_Q:=\min_{\tau\in T}\|F_\tau'\|_\infty=2L_*(Q),\qquad
L=(1-\varepsilon)L_*(Q),\qquad \ell:=2L=(1-\varepsilon)D_Q.
\tag{3}
\]
Let \(M_*\) be the smallest worst-case row cap of an always-correct deterministic procedure, allowing adaptive row choice. There are constants \(c,C,Q_0>0\), depending only on \(\tau_0\), such that for \(Q\ge Q_0\), \(0<\varepsilon\le Q^{-2}\), and \(\sigma>0\),
\[
c\left(1+\frac{\sigma^2}{Q\varepsilon^4}\right)
\le M_*(Q,\varepsilon,\sigma)
\le C\left(1+\frac{\sigma^2}{Q\varepsilon^4}\right).
\tag{4}
\]
The upper bound uses a prechosen bank. No efficient model-fitting algorithm is asserted.

Also, with the same joint regime,
\[
\inf_{\tau\in T}\ \inf_{\|b'\|_\infty\le\ell}
 \|F_\tau-b\|_{C(I_Q)}\asymp\sqrt Q\,\varepsilon^2.
\tag{5}
\]
Here \(b\in C^1(I_Q;\mathbb C)\). This is a distance between noiseless model classes, before comparing two noise balls. Both (4) and (5) use the factor two for competing baselines in (3).

## Full-response speed decreases from the left endpoint

Write \(v_\tau=|F_\tau'|\) and \(u_\tau=F_\tau'/v_\tau\). Uniformly for \(\tau\in T\), \(r\in I_Q\), and sufficiently large \(Q\),
\[
c_0Q^{-1/2}\le v_\tau(r)\le C_0Q^{-1/2},\qquad
c_1Q^{-3/2}\le-v_\tau'(r)\le C_1Q^{-3/2},\qquad
|u_\tau'(r)|\le C_2.
\tag{6}
\]
In particular the maximum speed is at \(r=Q\), exactly, and
\[
D_Q=\min_{\tau\in T}v_\tau(Q)\asymp Q^{-1/2}.
\tag{7}
\]
The minimum is attained. No assertion that its minimizer is exactly \(+\tau_0\) or \(-\tau_0\) is needed.

Here is the additional derivative argument beyond XF-200's absolute threshold expansion. Set \(r=Qs\). Its exact direct envelope is
\[
A_{Q,\tau}(s)=\frac{2e^{-1/s^2}}{\sqrt{\pi s}}
(1+Q^{-2}s^{-2})^{1/4}
\left(e^{-(2Q\tau+\tau^2)(Q^{-2}s^{-2}+iQ^{-1}s^{-1})}-1\right).
\tag{8}
\]
In every fixed \(C^k[1,2]\) norm it equals
\(A_\tau(s)=2e^{-1/s^2}(e^{-2i\tau/s}-1)/\sqrt{\pi s}\)
plus \(O(Q^{-1})\), uniformly in \(\tau\). Thus
\[
E_{Q,\tau}(s):=\sqrt Q\,e^{iQ/s}F_\tau'(Qs)
=\frac{i}{s^2}A_{Q,\tau}(s)+Q^{-1}A_{Q,\tau}'(s)
+R_{Q,\tau}(s),\qquad
\|R_{Q,\tau}\|_{C^1}\le C Q^K e^{-cQ^2}
\tag{9}
\]
for fixed constants \(K,c>0\). The remainder is the reciprocal term, not an omitted source component. Explicitly, with
\[
w(r)=\pi/x_r=\pi^2\left(1-ir-\frac1{1+ir}\right),\qquad
U(r)=x_r^{-1/2}|x_r|^{1/2},
\]
that term is \(-2U(r)(e^{-(Q+\tau)^2w(r)}-e^{-Q^2w(r)})\).
On \(r\ge Q\ge1\), \(\Re w\ge\pi^2/2\), while every fixed positive-order derivative of \(w\) and \(U\) is bounded. Differentiation, the change to \(s\), and demodulation in (9) therefore cost only fixed powers of \(Q\). This proves its stated exponential bound, including the rapidly rotating reciprocal phase.

The nonzero limiting envelope in (9) has modulus
\[
V_\tau(s)=\frac4{\sqrt\pi}s^{-5/2}e^{-1/s^2}|\sin(\tau/s)|.
\]
For \(t=|\tau|/s\),
\[
\frac{V_\tau'(s)}{V_\tau(s)}
=\frac{-5/2+2/s^2-t\cot t}{s}<0.
\tag{10}
\]
Indeed \(0<t\le1/4\), \(t\cot t>0\), and \(-5/2+2/s^2\le-1/2\). Compactness and \(\tau_0>0\) give uniform positive lower bounds for \(V_\tau\) and \(-V_\tau'\). Since the modulus is smooth away from zero, (9) implies
\[
\sqrt Q\,v_\tau(Qs)=V_\tau(s)+O_{C^1}(Q^{-1}).
\tag{11}
\]
This proves the first two estimates in (6). Differentiating the exact response twice gives \(|F_\tau''|\le C Q^{-1/2}\), as also proved by XF-200's full-response derivative bound. Hence
\(|u_\tau'|\le2|F_\tau''|/v_\tau\le C_2\).

The errors in (11) establish exact qualitative bounds (6) once \(Q\) is large; they are **not** subtracted from the tiny slack \(\varepsilon D_Q\). All subsequent comparisons use the exact \(D_Q\). Thus \(\varepsilon\) may be arbitrarily smaller than any asymptotic threshold error.

## A short complex chord supplies a uniform bank

For \(t\ge0\) small, the identity for unit complex numbers
\(\operatorname{Re}(u_\tau(Q+t)\overline{u_\tau(Q)})
=1-|u_\tau(Q+t)-u_\tau(Q)|^2/2\)
and (6) give
\[
\operatorname{Re}\bigl(F_\tau'(Q+t)\overline{u_\tau(Q)}\bigr)
\ge D_Q-C_3Q^{-3/2}t-C_4Q^{-1/2}t^2.
\tag{12}
\]
The quadratic turning loss matters: bounding the complex derivative difference only linearly would give an unnecessarily short stencil.

Choose a sufficiently small constant \(a>0\), depending only on \(\tau_0\), and set \(h=aQ\varepsilon\). For \(0\le t\le5h/4\),
\[
\frac{t}{Q}=O(a\varepsilon),\qquad
t^2=O(a^2Q^2\varepsilon^2)\le O(a^2\varepsilon).
\]
By (7), (12) is at least \((1-\varepsilon/2)D_Q\) after fixing \(a\). For every \(0\le z\le h/4\), integrate on \([Q+z,Q+z+h]\):
\[
|F_\tau(Q+z+h)-F_\tau(Q+z)|-\ell h
\ge\frac12D_Q\varepsilon h
\ge c_3\sqrt Q\,\varepsilon^2=:\mu.
\tag{13}
\]
The projection direction in this proof may depend on \(\tau\); the row bank does not. For every admissible difference baseline \(b\), its increment has modulus at most \(\ell h\), so
\[
|(F_\tau-b)(Q+z+h)-(F_\tau-b)(Q+z)|\ge\mu.
\tag{14}
\]

Take \(n\) distinct \(z_j\in(0,h/4)\), for example \(z_j=hj/[4(n+1)]\), and query both endpoints of every pair. These are \(2n\) distinct rows in two disjoint clusters. Even though their spatial intervals overlap, their vectors of row coordinates have disjoint supports, and
\[
\|(F_\tau-b)|_{\mathcal R}\|_2^2
\ge\frac12\sum_{j=1}^n
 |(F_\tau-b)(Q+z_j+h)-(F_\tau-b)(Q+z_j)|^2
\ge n\mu^2/2.
\tag{15}
\]
Choose \(n>8\sigma^2/\mu^2\). Then every active/null class pair is separated by more than \(2\sigma\). A feasible label is unique, proving the upper bound in (4). Applying (14) to one pair proves the lower bound in (5). The construction uses arbitrary row precision and a fixed **total** noise budget; it does not average away an unrestricted shared calibration.

## Clipped complex velocity gives a transcript-consistent lower bound

Choose an exact minimizer \(\tau_Q\) in (7), and abbreviate its response, speed, and direction by \(F,v,u\). By (6), there is a unique \(t_\varepsilon\in(0,Q)\) with
\[
v(Q+t_\varepsilon)=\ell,
\qquad t_\varepsilon\asymp Q\varepsilon.
\tag{16}
\]
Indeed \(v(Q)-\ell=\varepsilon D_Q\) and \(-v'\asymp Q^{-3/2}\). Its excess-speed integral obeys
\[
H_\varepsilon:=\int_Q^{Q+t_\varepsilon}(v(r)-\ell)\,dr
\asymp\sqrt Q\,\varepsilon^2.
\tag{17}
\]
For example, integrating the upper and lower linear bounds following from (6) bounds this area by constant multiples of \((\varepsilon D_Q)^2/Q^{-3/2}\).

Define on the **whole** permitted interval
\[
b(Q)=F(Q),\qquad b'(r)=\min\{v(r),\ell\}\,u(r).
\tag{18}
\]
The derivative is continuous, including at \(Q+t_\varepsilon\), and \(\|b'\|_\infty\le\ell\). Its residual satisfies
\[
R(r):=F(r)-b(r)
=\int_Q^r(v(t)-\ell)_+u(t)\,dt,
\qquad\|R\|_\infty\le H_\varepsilon.
\tag{19}
\]
This proves the upper bound in (5). It does not claim that speed clipping is the exact complex Chebyshev optimizer.

For the adaptive lower bound, fix these two complete admissible experiments before querying:
\[
\text{null baseline }B_0=b/2,\qquad
\text{active baseline }B_1=-b/2.
\]
At every row return the common transcript value \(y(r)=F(r)/2\). The required errors are respectively \(+R(r)/2\) and \(-R(r)/2\). Along any path of at most \(M\) rows their squared norms are at most \(MH_\varepsilon^2/4\). A deterministic procedure chooses the same subsequent rows on the two transcripts, including when it stops early. Therefore no always-correct procedure with
\[
M\le4\sigma^2/H_\varepsilon^2
\tag{20}
\]
can distinguish the labels. This is a global-baseline adversary, not a choice of a different drift at each row. Equations (17) and (20) give the lower rate in (4). One row always fails because the baseline constant is unrestricted; combining this with (20) supplies its \(1+\cdot\) form.

## Placement must respond to the slack

For the least favorable displacement, the excess-speed region has length \(\asymp Q\varepsilon\). Any bank lying entirely to the right of \(Q+t_\varepsilon\) aliases exactly: set \(b=F\) there and extend left with constant derivative \(F'(Q+t_\varepsilon)\), which has modulus \(\ell\). This gives a \(C^1\) difference baseline on the whole interval.

More generally, every **fixed finite bank** aliases at some strictly subcritical budget. Order its rows \(r_1<\cdots<r_M\). For the same minimizing response,
\[
K_{\mathcal R}:=\max_{j<M}
\frac{|F(r_{j+1})-F(r_j)|}{r_{j+1}-r_j}<D_Q,
\tag{21}
\]
because \(|F'|<D_Q\) except at the single endpoint \(Q\). When \(\ell>K_{\mathcal R}\), piecewise linear interpolation of these complex data, extended constantly outside the extreme nodes, has Lipschitz constant \(K_{\mathcal R}\). Convolve with a nonnegative smooth kernel and correct the finitely many node errors with fixed smooth cardinal functions. The convolution preserves the derivative bound, and the correction's derivative tends uniformly to zero with the smoothing scale. Strict slack therefore gives a \(C^1\) interpolant with derivative norm below \(\ell\), yielding exact aliases via \(\pm b/2\). For a single row, a constant already suffices.

Thus a bank fixed independently of \(\varepsilon\) cannot stay identifiable all the way to the threshold, even if it contains \(Q\). Equations (13)--(15) exhibit sufficient localization and refinement. They do not characterize every rate-optimal design.

## Prior art, audit, and mathematical boundary

The general mechanisms are classical. [Wiens, *Robust discrimination designs* (2009), §2](https://sites.ualberta.ca/~dwiens/home%20page/pubs/discriminationDesign.pdf) explicitly separates uncertain model neighbourhoods and optimizes discrimination over them; its stochastic KL criterion is not (2). [Gutev, *Lipschitz Extensions and Approximations* (2020), §2](https://arxiv.org/abs/2002.07205) reconstructs the classical scalar Pasch–Hausdorff and McShane–Whitney machinery. The real ordered-curve formula from the authorized AF-573 source motivates clipping, but is not imported as a complex approximation identity. The complex chord estimate, radial velocity clipping, and finite interpolation argument above are proved directly. No new general optimal-recovery or Lipschitz-extension principle is claimed.

The source-specific delta from XF-200 is (6), followed by a uniform near-critical acquisition law with a matching adaptive obstruction. Its fixed-relative-slack \(\Theta(Q)\) statement has constants depending on the slack and does not imply (4). The \(\varepsilon^4\) cost is the square of a quadratic surviving amplitude, arising from a derivative excess \(\asymp\varepsilon/\sqrt Q\) confined to length \(\asymp Q\varepsilon\).

A scratch floating-point audit independently differentiated (1) twice at \(Q\in\{32,64,128,256\}\), \(\tau\in\{-1/4,-1/10,1/10,1/4\}\), and \(s\in\{1,1.2,1.5,2\}\). All 64 scaled slopes \(-Q^{3/2}v_\tau'(Qs)\) were positive (range approximately \(0.0232\)–\(0.3071\)). With each source's own exact endpoint speed for this diagnostic, all 48 chords using \(\varepsilon Q^2\in\{0.01,0.1,1\}\) and \(h=0.05Q\varepsilon\) had positive excess; its ratio to \(\sqrt Q\varepsilon^2\) ranged approximately \(0.00397\)–\(0.00995\). A central-difference check agreed with the analytic first derivative to relative error below \(3.1\cdot10^{-9}\). These checks are not interval proofs, do not locate the exact minimizing displacement, and cannot numerically certify the underflow-scale reciprocal contribution; (9) supplies that analytic control.

The regime \(\varepsilon\le Q^{-2}\) controls turning through \((Q\varepsilon)^2\lesssim\varepsilon\). No sharp rate is established here when \(Q^2\varepsilon\to\infty\). Other \(\alpha\), interior derivative maxima, higher-derivative nuisance bounds, multiple supports, coordinate error, and per-row noise are outside this theorem. The synthetic normalized complex interface is assumed available. A physical Xi calibration theorem and a source-to-zero implication remain missing; neither (4) nor (5) supplies an upper bound on \(\Lambda\).
