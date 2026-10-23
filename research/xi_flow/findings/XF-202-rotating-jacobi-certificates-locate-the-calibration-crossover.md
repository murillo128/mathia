---
type: theorem
research_line: xi_flow
finding_id: XF-202
status: canonical
---

# XF-202 — Rotating Jacobi certificates locate the calibration crossover

**Evidence:** EXACT-DERIVED + CLASSICAL-NONSTATIONARY-PHASE + SYNTHETIC-ACQUISITION-BOUNDARY. For the complete singleton complex Jacobi experiment of XF-201, the separation of the null and active smooth-calibration classes is controlled by
\[
\mathfrak d(Q,\varepsilon)
:=\frac{\sqrt Q\,\varepsilon^2}{1+Q\varepsilon}.
\tag{1}
\]
The full-curve class distance is comparable to (1). For every fixed positive total noise budget, the sharp deterministic row cost as the relative slack tends to zero is comparable to its inverse square. The quartic regime therefore extends to \(\varepsilon\asymp Q^{-1}\), not just the \(Q^{-2}\) range established by XF-201's single-chord proof. Above that crossover the cost is quadratic in inverse slack. The finite bank and the adaptive lower bound are proved below. This concerns a synthetic source interface, not an upper bound on the de Bruijn–Newman constant.

## Experiment and quantified conclusions

Fix \(0<\tau_0\le1/4\), and let
\[
T=[-1/4,-\tau_0]\cup[\tau_0,1/4],\qquad I_Q=[Q,2Q].
\]
For sufficiently large integer \(Q\), set
\[
\begin{aligned}
x_r&=\pi^{-1}(r^{-2}+i/r),&G_r&=|x_r|^{-1/2},\\
F_\tau(r)&=\frac2{G_r}
 (e^{-\pi(Q+\tau)^2x_r}-e^{-\pi Q^2x_r})
 -\frac{2x_r^{-1/2}}{G_r}
 (e^{-\pi(Q+\tau)^2/x_r}-e^{-\pi Q^2/x_r}).
\end{aligned}
\tag{2}
\]
The square root is principal. Here \(G_r=\max\{1,|x_r|^{-1/2}\}\) on the entire permitted interval. The labels are null and active, with sources \(0\) and \(F_\tau\), respectively. Observations are
\[
y_j=f(r_j)+B(r_j)+e_j,\qquad
 B\in C^1(I_Q;\mathbb C),\quad \|B'\|_\infty\le L,
 \quad\sum_j|e_j|^2\le\sigma^2.
\tag{3}
\]
One baseline is shared by all rows of an experiment; different labels may choose different baselines. Its constant is unrestricted. Distinct rows may be arbitrarily close. As in XF-201, use the exact threshold
\[
D_Q=\min_{\tau\in T}\|F_\tau'\|_\infty,
\qquad L_* =D_Q/2,\qquad
L=(1-\varepsilon)L_*,\qquad \ell=2L=(1-\varepsilon)D_Q.
\tag{4}
\]
Define
\[
d_\infty=\inf_{\tau\in T}\inf_{b\in C^1,\ \|b'\|_\infty\le\ell}
 \|F_\tau-b\|_{C(I_Q)}.
\]
Let \(M_*\) denote the smallest worst-case row cap of an always-correct deterministic detector, allowing adaptive queries. Constants below depend only on \(\tau_0\). There exist \(Q_0,\varepsilon_0,c,C>0\) such that for all \(Q\ge Q_0\), \(0<\varepsilon\le\varepsilon_0\),
\[
c\mathfrak d\le d_\infty\le C\mathfrak d,
\tag{5}
\]
and, for every \(\sigma>0\),
\[
c\left(1+\frac{\sigma^2}{\mathfrak d^2}\right)
\le M_*\le
C\left(1+Q\sqrt\varepsilon+\frac{\sigma^2}{\mathfrak d^2}\right).
\tag{6}
\]
In particular, whenever \(\varepsilon^{5/2}\le\sigma^2\),
\[
M_*\asymp1+\frac{\sigma^2(1+Q\varepsilon)^2}{Q\varepsilon^4}.
\tag{7}
\]
This covers every fixed \(\sigma>0\) for all sufficiently small \(\varepsilon\), uniformly in large \(Q\). It gives quartic cost \(1+\sigma^2/(Q\varepsilon^4)\) for \(Q\varepsilon\le1\), and quadratic cost \(1+\sigma^2Q/\varepsilon^2\) for \(Q\varepsilon\ge1\). The overhead in (6) is a sufficient finite-design cost; it is not asserted necessary in the remaining very-low-noise joint regime. No efficient fitting algorithm is asserted.

## Full-response speed and phase control

Write \(v_\tau=|F_\tau'|\), \(u_\tau=F_\tau'/v_\tau=e^{i\theta_\tau}\), using a continuous phase on \(I_Q\). XF-201, (6)–(11), proves uniformly
\[
v_\tau\asymp Q^{-1/2},\quad
-v_\tau'\asymp Q^{-3/2},\quad |u_\tau'|\le C,
\quad D_Q=\min_\tau v_\tau(Q)\asymp Q^{-1/2}.
\tag{8}
\]
An additional consequence of its exact envelope is
\[
c\le\theta_\tau'(r)\le C,
\qquad |\theta_\tau''(r)|\le C/Q.
\tag{9}
\]
To check this without discarding the reciprocal source, put \(s=r/Q\) and
\[
E_{Q,\tau}(s)=\sqrt Q\,e^{iQ/s}F_\tau'(Qs).
\]
The exact direct envelope \(A_{Q,\tau}\) in XF-201, (8), converges in every fixed \(C^k[1,2]\) norm to
\[
A_\tau(s)=\frac{2e^{-1/s^2}}{\sqrt{\pi s}}(e^{-2i\tau/s}-1).
\]
Differentiating its exact expression gives
\[
E_{Q,\tau}=(i/s^2)A_{Q,\tau}+Q^{-1}A_{Q,\tau}'
 +O_{C^2}(Q^K e^{-cQ^2}).
\tag{10}
\]
Indeed the reciprocal exponent is \(-(Q+\tau)^2w(r)\) or \(-Q^2w(r)\), with
\(w(r)=\pi^2(1-ir-(1+ir)^{-1})\), \(\Re w\ge\pi^2/2\). Every fixed number of differentiations and demodulations costs only powers of \(Q\), so XF-201's \(C^1\) estimate extends to \(C^2\). The limiting envelope is bounded away from zero since \(|\tau|\ge\tau_0\). Thus \(E,E',E''\) are uniformly bounded and \(|E|\ge c\). The exact logarithmic derivative yields
\[
\theta_\tau'(r)=\frac{Q^2}{r^2}
 +\frac1Q\operatorname{Im}\frac{E'(s)}{E(s)},\qquad
\theta_\tau''(r)=-\frac{2Q^2}{r^3}
 +\frac1{Q^2}\operatorname{Im}\left(\frac{E''}{E}-\frac{(E')^2}{E^2}\right).
\tag{11}
\]
This proves (9). These estimates establish exact qualitative inequalities once \(Q\) is large. No asymptotic error is subtracted from \(\varepsilon D_Q\), so arbitrarily small slack is allowed.

## A rotating dual certificate survives beyond one chord

Choose a small constant \(a>0\), and put \(H=aQ\varepsilon\). By (8), uniformly in \(\tau\),
\[
v_\tau(r)-\ell\ge \tfrac34\varepsilon D_Q
\qquad(Q\le r\le Q+H).
\tag{12}
\]
For any admissible difference baseline \(b\), write \(R=F_\tau-b\). Since \(|b'|\le\ell\),
\[
\operatorname{Re}\int_Q^{Q+H}R'(r)\overline{u_\tau(r)}\,dr
\ge\int_Q^{Q+H}(v_\tau-\ell)\,dr
\ge c\varepsilon D_Q H.
\tag{13}
\]
Integration by parts bounds the absolute value on the left by
\[
\|R\|_\infty\left(2+\int_Q^{Q+H}|u_\tau'|\,dr\right)
\le C(1+H)\|R\|_\infty.
\tag{14}
\]
Combining (12)–(14) gives the lower bound in (5). Unlike a fixed-direction chord, the test follows the tangent. Its cost is the total variation \(O(1+H)\) of that tangent, rather than the quadratic turning loss of one long chord.

## Oscillatory clipping gives the matching full-curve adversary

Choose an exact minimizer \(\tau_Q\) of \(v_\tau(Q)\). Write its speed and direction as \(v,u=e^{i\theta}\), and let
\[
q(r)=(v(r)-\ell)_+.
\]
For sufficiently small fixed \(\varepsilon_0\), (8) gives a unique end of the excess-speed interval, at \(Q+H_*<2Q\), with
\[
H_*\asymp Q\varepsilon,\quad q(Q)=\varepsilon D_Q,
\quad \int_Q^{2Q}q\asymp\sqrt Q\,\varepsilon^2.
\tag{15}
\]
Define the same global clipped baseline as in XF-201:
\[
b(Q)=F_{\tau_Q}(Q),\qquad b'(r)=\min(v(r),\ell)u(r).
\tag{16}
\]
It belongs to \(C^1\) and has derivative bound \(\ell\). Its residual is
\[
R(r)=\int_Q^r q(t)e^{i\theta(t)}\,dt.
\tag{17}
\]
The area estimate gives \(\|R\|_\infty\le C\sqrt Q\,\varepsilon^2\). For the other bound, apply integration by parts on \([Q,y]\), \(y\le Q+H_*\):
\[
\int_Q^y q e^{i\theta}
=\left[\frac{q e^{i\theta}}{i\theta'}\right]_Q^y
 -\int_Q^y e^{i\theta}\left(\frac{q}{i\theta'}\right)'dt.
\tag{18}
\]
The function \(q\) is nonincreasing and absolutely continuous. By (9),
\[
\left|\int_Q^y q e^{i\theta}\right|
\le C\left(q(Q)+\int_Q^y|q'|+Q^{-1}\int_Q^yq\right)
\le Cq(Q)\le C\varepsilon/\sqrt Q.
\tag{19}
\]
Here \(H_*\le Q\); beyond it the residual is constant. Taking the smaller of (15) and (19) proves \(\|R\|_\infty\le C\mathfrak d\) and the upper bound in (5).

This fixes two complete experiments: null baseline \(b/2\), active baseline \(-b/2\). Return the common transcript \(F_{\tau_Q}(r)/2\). The two error vectors have entries \(\pm R(r_j)/2\), and total squared norm at most \(CM\mathfrak d^2\). Consequently every deterministic policy with \(M\le c\sigma^2/\mathfrak d^2\) fails, regardless of its adaptive row choices or early stopping. One row also fails because an arbitrary constant is allowed. This proves the lower bound in (6), without choosing a new baseline after each query.

## Finite rows realize the rotating certificate

The integral certificate is not assumed to be an observable. Here is a bank using only the point samples (3).

Partition \([Q,Q+H]\) into \(n\) equal intervals with nodes \(r_j\), choosing
\[
n=\max\{1,\lceil H/(b_0\sqrt\varepsilon)\rceil\},
\qquad \delta=H/n,
\tag{20}
\]
for a sufficiently small constant \(b_0>0\). Let \(u_j=u_\tau(r_j)\), \(0\le j<n\). The unit-vector identity and (8) give
\[
\operatorname{Re}(F_\tau'(r)\overline{u_j})
\ge v_\tau(r)-C Q^{-1/2}\delta^2
\quad(r_j\le r\le r_{j+1}).
\]
By (12), after choosing \(b_0\), every admissible \(b\) satisfies
\[
\mathcal L_\tau(R):=
\operatorname{Re}\sum_{j=0}^{n-1}(R(r_{j+1})-R(r_j))\overline{u_j}
\ge \tfrac12\varepsilon D_QH=:S.
\tag{21}
\]
The coefficients after summation by parts are
\[
c_0=-\overline{u_0},\quad
c_j=\overline{u_{j-1}}-\overline{u_j}\ (0<j<n),\quad
c_n=\overline{u_{n-1}}.
\]
They sum to zero. With a uniform constant \(C_u\) from (8), set
\[
w_0=w_n=1,\qquad w_j=C_u\delta\ (0<j<n),\qquad
W=\sum_j w_j\le2+C_uH.
\tag{22}
\]
Then \(|c_j|\le w_j\). Crucially these upper weights, the nodes, and all ensuing multiplicities are independent of the unknown \(\tau\).

First imagine taking \(k_j\) copies at each node, where
\[
k_j=\max\{1,\lceil64\sigma^2 Ww_j/S^2\rceil\}.
\tag{23}
\]
Replace each value in (21) by its cluster average. The squared Euclidean norm of the resulting coefficient vector is at most
\[
\sum_j|c_j|^2/k_j\le S^2/(64\sigma^2),
\qquad
\sum_j k_j\le n+1+64\sigma^2W^2/S^2.
\tag{24}
\]
The copies can be replaced by **distinct** points within distance \(\eta\) of their respective nodes, with disjoint clusters inside \(I_Q\). All residuals obey \(\|R'\|_\infty\le C/\sqrt Q\), so this changes (21) by at most \(CW\eta/\sqrt Q\). Choose positive \(\eta\) small enough that this is at most \(S/2\) and that the clusters remain disjoint. Endpoint clusters are one-sided. Arbitrarily fine placement is explicitly permitted in (3).

For this prechosen distinct bank, (21)–(24) imply
\[
\|R|_{\mathcal R}\|_2\ge
\frac{S/2}{S/(8\sigma)}=4\sigma>2\sigma.
\tag{25}
\]
Thus the null and every active noiseless class have disjoint radius-\(\sigma\) noise neighborhoods. A feasible-label rule detects the correct label. The coefficient used to prove separation may depend on \(\tau\); the actual bank does not.

Since \(n+1=O(1+Q\sqrt\varepsilon)\) and \(W/S=O(1/\mathfrak d)\), this proves the upper bound in (6). Finally,
\[
Q\sqrt\varepsilon\,\mathfrak d^2
=\frac{Q^2\varepsilon^{9/2}}{(1+Q\varepsilon)^2}
\le\varepsilon^{5/2}.
\]
The condition in (7) absorbs the mesh overhead. Fixed total noise and unrestricted row precision are essential to this conclusion.

## Prior art, audit, and consequence

The integration-by-parts and nonstationary-phase mechanisms are classical; [Terence Tao, *Lecture Notes 8 for 247B* (2007), Lemma 2.3](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf), gives the phase-derivative estimate behind (18)–(19), including why a first-derivative lower bound alone is insufficient without variation control. The weighted version used here is derived explicitly. [Holger Dette and Stefanie Titoff, *Optimal discrimination designs*, Annals of Statistics 37 (2009), Theorem 2.1](https://arxiv.org/abs/0908.1912), relates classical T-optimal discrimination to best uniform approximation. That finite-parameter real regression framework does not itself prove (6) for this complex derivative-bounded nuisance class and adversarial total noise. Wiens's model-neighborhood analysis and Gutev's scalar Lipschitz machinery, cited in XF-201, remain prior-art boundaries. No new general approximation, duality, or experimental-design principle is claimed.

The source-specific result is the exact full-Jacobi phase control (9) and its combination with decreasing endpoint speed to obtain (5)–(7). The \(Q^{-2}\) restriction in XF-201 was a sufficient one-chord regime. Following the tangent removes that proof restriction. The actual crossover occurs when the excess-speed interval \(H_*\asymp Q\varepsilon\) spans order-one phase, at \(\varepsilon\asymp Q^{-1}\). After that point, oscillatory clipping caps the adversary's residual at \(O(\varepsilon/\sqrt Q)\).

A scratch 45-decimal mpmath audit differentiated the full expression (2) through order three for \(Q\in\{32,64,128,256\}\), \(\tau\in\{-1/4,-1/10,1/10,1/4\}\), and \(r/Q\in\{1,1.2,1.5,2\}\). The 64 phase speeds ranged from approximately \(0.2496\) to \(1.0122\), and \(Q|\theta''|\le2.022\) on that grid. In 36 separate finite-certificate checks with \(Q\in\{32,128,512\}\), the same displacements, \(\varepsilon\in\{Q^{-2},Q^{-1},0.03\}\), \(H=0.05Q\varepsilon\), and mesh cap \(0.05\sqrt\varepsilon\), each certificate exceeded \(0.9619\,v_\tau(Q)\varepsilon H\). These checks used each source's own exact endpoint speed, not a numerical claim about the minimizing displacement. They are finite floating-point diagnostics; the full-response envelope proof supplies the uniform bounds and exponentially small reciprocal control.

The constants and theorem concern \(\alpha=1\), first-derivative calibration after normalization, one edited unit-weight symmetric pair, and null-versus-active detection. They do not cover multiple support labels, unknown weights, per-row stochastic or adversarial noise, coordinate errors, or optimal row geometry in every simultaneous zero-noise limit. No scalar Lipschitz envelope formula is imposed on a complex curve. Calibration neighborhoods and total observation-noise balls contribute separate factors of two. The physical Xi source-access and source-to-zero bridges remain missing, so this acquisition crossover gives neither an RH implication nor an upper bound on \(\Lambda\).
