# RE-239 — Coalescing mixed phases give only quadratic Wiener discount

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-SERIAL-COMPOSITION + MIXED-PHASE-STABILITY + WIENER-NORM-OBSTRUCTION + PRIOR-ART-AUDIT.

**Parent findings:** RE-220, RE-237.

RE-237 proves exact multiplicativity of the Wiener norm for a cascade of single-center negative-binomial predictors whose centers lie on one common ray. Here the centers may have different, but nearby, phases. Their cancellation advantage is uniformly at most quadratic in those phase displacements. The statement is algebraic: factorwise prediction is not assumed.

## 1. Theorem

For \(1\le r\le J\) let \(m_r\ge1\), \(N_r\ge0\), and

\[
a_r=\rho_r e^{i\varphi_r},\qquad 0<\rho_r\le R<\infty.
\]

Define the off-center truncated predictor

\[
Q_r(z)=z^{m_r}a_r^{-m_r}
\sum_{k=0}^{N_r}\binom{m_r+k-1}{k}
\left(1-\frac{z}{a_r}\right)^k,
\qquad
F_r(z)=\frac{Q_r(z)}{Q_r(1)},
\]

where \(Q_r(1)\ne0\), and write \(G=\prod_{r=1}^J F_r\). Choose a common reference phase \(\varphi_*\), and let

\[
\delta_r=\operatorname{Arg}(e^{i(\varphi_r-\varphi_*)})
\in[-\pi,\pi].
\]

For every finite \(R>0\), there are \(\delta_0(R)>0\) and \(C_R<\infty\), independent of the number of factors and all \(m_r,N_r,\rho_r\), such that, if \(|\delta_r|\le\delta_0(R)\),

\[
\boxed{
0\le
\sum_{r=1}^J\log\|F_r\|_A-\log\|G\|_A
\le C_R\sum_{r=1}^J(N_r+1)\delta_r^2.
}
\tag{1}
\]

Here \(\|P\|_A\) is the sum of absolute values of the coefficients of a polynomial \(P\). This estimate recovers the exact equality of RE-237 at zero phase displacement.

Let \(M=\sum_r m_r\), and suppose \(N_r\le\Lambda m_r\) uniformly. For a common observed arc of half-width \(\alpha>0\),

\[
0\le
\sum_r\frac{m_r}{M}
\frac{\log\|F_r\|_A}{m_r\alpha}
-\frac{\log\|G\|_A}{M\alpha}
\le
\frac{C_R}{M\alpha}\sum_r(N_r+1)\delta_r^2.
\tag{2}
\]

Consequently the leading normalized Wiener rate is unchanged whenever

\[
\sum_r(N_r+1)\delta_r^2=o(M\alpha).
\tag{3}
\]

A sufficient condition under bounded truncation ratios is
\(\max_r\delta_r^2=o(\alpha)\). Thus every coalescing phase family has zero leading discount for a fixed positive \(\alpha\); when \(\alpha\to0\), phase coalescence alone is **not** enough and condition (3) is needed. At \(\max_r|\delta_r|=O(M^{-1/2})\), the *total* discount is \(O(1)\), hence normalized discount vanishes if \(M\alpha\to\infty\).

## 2. Reduction to positive coefficient distributions

Expanding the RE-237 single-center polynomial gives, for \(0\le j\le N_r\),

\[
[z^{m_r+j}]F_r
=\gamma_r\omega_r^j B_{r,j},
\quad
\gamma_r=\frac{a_r^{-m_r}}{Q_r(1)},
\quad
\omega_r=-e^{-i\varphi_r},
\]

with strictly positive weights

\[
B_{r,j}
=\rho_r^{-j}\sum_{k=j}^{N_r}
\binom{m_r+k-1}{k}\binom{k}{j}.
\]

Put \(S_r=\sum_j B_{r,j}\), \(p_{r,j}=B_{r,j}/S_r\), and
\(P_r(w)=\sum_j p_{r,j}w^j\). Thus

\[
\|F_r\|_A=|\gamma_r|S_r,\qquad
F_r(z)=\gamma_r S_r z^{m_r}P_r(\omega_r z).
\tag{4}
\]

At the common unit-circle point \(z_*=\omega_*^{-1}\), with
\(\omega_*=-e^{-i\varphi_*}\), one has
\(\omega_r z_*=e^{-i\delta_r}\). The Wiener norm dominates any
unit-circle evaluation; combining that fact with its submultiplicativity yields

\[
0\le
D:=\sum_r\log\|F_r\|_A-\log\|G\|_A
\le
\sum_r-\log|P_r(e^{-i\delta_r})|,
\tag{5}
\]

provided the characteristic functions on the right are nonzero. We next prove a uniform small-angle bound that ensures this.

## 3. An exact binomial mixture and a uniform thin edge defect

Suppress the factor index. Let

\[
p=\frac1{\rho+1},\qquad q=\frac{\rho}{\rho+1},\qquad
w_k=\binom{m+k-1}{k}(1+\rho^{-1})^k
\quad (0\le k\le N).
\]

Take \(K\) with \(\Pr(K=k)=w_k/\sum_{\ell=0}^N w_\ell\);
given \(K=k\), take \(L\mid K=k\sim\operatorname{Binomial}(k,p)\).
The binomial theorem and (4) give exactly

\[
P(z)=\mathbb E z^L
=\mathbb E(q+pz)^K.
\tag{6}
\]

Set \(E=N-K\). Since, for \(k\ge1\),

\[
\frac{w_{k-1}}{w_k}
=\frac{k}{m+k-1}\,q\le q,
\]

and \(w_N\le\sum_{\ell=0}^Nw_\ell\), the reverse-depth distribution obeys

\[
\Pr(E=d)\le q_R^d,\qquad
q_R:=\frac{R}{1+R}<1,\qquad d\ge0.
\tag{7}
\]

The inequality includes \(N=0\), when \(E=0\). All moments and a fixed exponential moment of \(E\) are therefore bounded uniformly in \(m,N,\rho\le R\).

Define \(h(u)=\mathbb E u^E\) and \(a(t)=q+p e^{-it}\). Equation (6) factors exactly as

\[
P(e^{-it})=a(t)^N h(a(t)^{-1}).
\tag{8}
\]

By (7), \(h\) and its first two derivatives are uniformly bounded in a fixed complex neighborhood of \(u=1\), while \(h(1)=1\). Shrinking that neighborhood uniformly makes \(h\) zero-free and provides an analytic logarithm there. Since \(a(0)=1\), \(a'(0)=-ip\), and \(h'(1)=\mathbb E E\) is real, the real derivative

\[
\left.\frac{d}{dt}
\log|h(a(t)^{-1})|\right|_{t=0}=0.
\]

Taylor's theorem with the uniform second-derivative bound gives

\[
\big|\log|h(a(t)^{-1})|\big|\le C_R t^2
\tag{9}
\]

for \(|t|\le\delta_0(R)\). Also

\[
|a(t)|^2=1-4pq\sin^2(t/2),
\]

so \(-\log|a(t)|\le C t^2\) for small \(|t|\), uniformly over \(0\le p\le1\). Combining with (8) and (9),

\[
\boxed{
-\log|P(e^{-it})|\le C_R(N+1)t^2.
}
\tag{10}
\]

Substitution into (5) proves (1), then division by \(M\alpha\) proves (2).

## 4. Scope, falsification, and prior art

The bound controls *Wiener cancellation*, not whether \(F_r\) or \(G\) predicts the constant on the observed arc. To compare the right-hand side of (2) to rates of **valid individual predictors**, the stages must separately satisfy the prediction-error constraint. A product that predicts only through coupling remains outside that interpretation, although (1) still applies to its algebraic norm.

The bounded-radius assumption is load-bearing: as \(\rho\to\infty\), the ratio \(q=\rho/(1+\rho)\) approaches one and the uniform exponential-tail control (7) disappears. Fixed angular separation also lies outside the *negligible-rate* regime (3). For very narrow arcs, the relevant scale is \(\delta^2/\alpha\), not simply whether \(\delta\to0\). Positive-real or same-ray centers (\(\delta_r=0\)) give the exact zero-discount check of RE-237.

The standard ingredients are the Banach-algebra inequality for absolutely summable Fourier coefficients, elementary binomial conditioning, and the second-order behavior of characteristic functions; none is claimed as a new general theorem. The specific contribution is their combination with RE-237's exact off-center coefficient-phase identity to obtain a constant uniform over any finite number of stages, degrees, and bounded center radii. The proof above is self-contained, with no load-bearing external theorem or new SOURCES.md dependency.

## Research consequence

A co-phased serial cascade cannot escape RE-237 merely by moving its centers by a vanishing angular amount. A leading reduction of the current explicit separated-prediction upper constant \(5.996390\) would require phase spread satisfying the opposite of (3), or a different representation such as genuinely nonperturbative phase interference, additive/minimax synthesis, or a coupled prediction mechanism. This finding neither determines \(C_{\rm sep}\) nor proves Robin's inequality.
