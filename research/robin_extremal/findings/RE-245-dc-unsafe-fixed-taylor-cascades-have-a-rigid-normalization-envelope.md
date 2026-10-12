# RE-245 — DC-unsafe fixed Taylor cascades have a rigid normalization envelope

**Status:** EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + MULTI-CENTER-COUPLED-PREDICTION + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDIT.

**Parent findings:** RE-218, RE-237, RE-242, RE-243, RE-244.

RE-244 gives a necessary-and-sufficient factorwise prediction criterion for fixed finite Taylor cascades in the geometric first-omitted-term regime, but assumes that each factor is *DC safe*: its Taylor-error exponent at the normalizing point is nonpositive. A factor with positive exponent at DC has an exponentially large denominator, so the RE-244 proof does not exclude the possibility that normalization rescues an otherwise growing product. Here the denominator is retained exactly at exponential scale. A finite positive logarithmic-potential rigidity argument proves that this normalization cannot produce uniform prediction, even when it reduces the final exponential growth rate to zero.

## 1. The normalized envelope without DC safety

Fix \(I_\alpha=\{e^{i\theta}:|\theta|\le\alpha\}\), \(0<\alpha<\pi/2\), and a fixed integer \(J\ge1\). For each \(j\) fix \(a_j=\rho_j e^{i\varphi_j}\ne0\), \(s_j>0\), and \(\lambda_j>0\). Put \(m_j=\lceil s_jT\rceil\), \(N_j=\lceil\lambda_jm_j\rceil\), and

\[
Q_{j,T}(z)=z^{m_j}a_j^{-m_j}
\sum_{k=0}^{N_j}\binom{m_j+k-1}{k}(1-z/a_j)^k,
\qquad
G_T(z)=\prod_{j=1}^{J}\frac{Q_{j,T}(z)}{Q_{j,T}(1)}.
\tag{1}
\]

Let \(u_j(\theta)=1-e^{i\theta}/a_j\),
\(r_j=\max_{|\theta|\le\alpha}|u_j(\theta)|\), and

\[
h(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda,
\qquad
\tau_j(\theta)=-\log\rho_j+h(\lambda_j)
+\lambda_j\log|u_j(\theta)|.
\tag{2}
\]

As in RE-244, assume **only** the strict geometric-tail hypothesis

\[
\boxed{\qquad \frac{1+\lambda_j}{\lambda_j}\,r_j<1
\quad\text{for every }j.\qquad}
\tag{3}
\]

Interpret \(\tau_j=-\infty\) at zeros of \(u_j\). Define the continuous function and two nonnegative numbers

\[
F(\theta)=\sum_{j=1}^{J}s_j[\tau_j(\theta)]_+,
\qquad
D=F(0),\qquad
M=\max_{|\theta|\le\alpha}F(\theta)\ge D.
\tag{4}
\]

**Theorem.** For all sufficiently large \(T\), every \(Q_{j,T}(1)\ne0\). At each fixed \(\theta\in[-\alpha,\alpha]\),

\[
\boxed{\quad
\lim_{T\to\infty}\frac1T\log|G_T(e^{i\theta})|
=F(\theta)-D.
\quad}
\tag{5}
\]

The exact uniform exponential envelope is

\[
\boxed{\quad
\lim_{T\to\infty}\frac1T
\log\!\left(1+\sup_{z\in I_\alpha}|G_T(z)-1|\right)
=M-D.
\quad}
\tag{6}
\]

More strongly, *even without DC safety*,

\[
\boxed{\quad
\sup_{z\in I_\alpha}|G_T(z)-1|\longrightarrow0
\quad\Longleftrightarrow\quad
\max_{|\theta|\le\alpha}\tau_j(\theta)\le0
\ \text{for every }j.
\quad}
\tag{7}
\]

When the right side of (7) holds, the error is \(O(T^{-1/2})\). If \(M>D\), the error instead grows as \(\exp(T(M-D)+o(T))\). If \(M=D\) but some \(\tau_j(0)>0\), the exponential envelope is zero yet the uniform error does **not** tend to zero: at a fixed point of the arc, \(|G_T|\to0\) and the error tends to one. Thus a zero exponential rate must not be mistaken for prediction.

## 2. Pointwise rates and uniform envelope

Write \(E_{j,T}(z)=1-Q_{j,T}(z)\). The exact negative-binomial remainder and the uniform geometric-tail estimates from RE-244 (its equations (8)--(15)) apply under (3), with no DC assumption. At each fixed \(\theta\) with \(u_j(\theta)\ne0\),

\[
|E_{j,T}(e^{i\theta})|
=\Theta_{\theta,j}\!\left(
T^{-1/2}e^{m_j\tau_j(\theta)}
\right);
\tag{8}
\]

the corresponding upper bound is uniform over the arc, and at \(u_j=0\) the remainder is exactly zero. In particular, if \(\tau_j(\theta)>0\), then
\(Q_{j,T}(e^{i\theta})=-E_{j,T}(e^{i\theta})(1+o(1))\);
if \(\tau_j(\theta)\le0\), then \(Q_{j,T}(e^{i\theta})=1+o(1)\).
It follows, including at zeros of \(u_j\), that

\[
\lim_{T\to\infty}T^{-1}
\log|Q_{j,T}(e^{i\theta})|
=s_j[\tau_j(\theta)]_+.
\tag{9}
\]

Taking \(\theta=0\) proves that all denominators eventually exist and that

\[
|Q_{j,T}(1)|
=\exp\{Ts_j[\tau_j(0)]_++o(T)\}.
\tag{10}
\]

For \(\tau_j(0)>0\), this follows from the lower as well as the upper bound in (8); it is not an inference from a one-sided estimate. Subtracting the logarithms of (10) from (9), then summing over the fixed number \(J\) of factors, proves (5).

Uniformly in \(\theta\), the arc-wide upper estimate in (8) yields

\[
|Q_{j,T}(e^{i\theta})|
\le 1+C_jT^{-1/2}e^{m_j\tau_j(\theta)}
\le \exp\{Ts_j[\tau_j(\theta)]_++o(T)\},
\tag{11}
\]

where the final \(o(T)\) is uniform; near \(u_j=0\), the first remainder is even smaller, so no lower bound there is needed. Dividing by (10) gives
\(\sup_{I_\alpha}|G_T|\le\exp\{T(M-D)+o(T)\}\).
Since \(M\ge D\), this proves the upper half of (6) for \(1+\sup|G_T-1|\). If \(M>D\), choose a fixed maximizer \(\theta_*\). Equation (5) gives
\(|G_T(e^{i\theta_*})|=\exp\{T(M-D)+o(T)\}\),
and \(|G_T-1|\ge|G_T|-1\) gives the matching lower bound. If \(M=D\), the lower bound \(1+\sup|G_T-1|\ge1\) already yields (6).

## 3. A finite positive logarithmic potential cannot be locally flat

**Elementary rigidity lemma.** Given finitely many nonzero finite complex numbers \(a_j\) and strictly positive real weights \(w_j\), the function

\[
H(\theta)=\sum_jw_j\log|1-e^{i\theta}/a_j|
\tag{12}
\]

cannot be constant on any nonempty open interval where all its summands are finite.

For each center define
\(b_j=1/a_j\) when \(|a_j|\ge1\), and
\(b_j=\overline{a_j}\) when \(|a_j|<1\).
Then \(0<|b_j|\le1\), and on the unit circle
\(\log|1-z/a_j|=\log|1-b_jz|+c_j\)
for a constant \(c_j\) independent of \(z\). (For \(|a_j|<1\), use
\(|1-z/a_j|=|1-\overline{a_j}z|/|a_j|\).)
With \(z=e^{i\theta}\), direct differentiation gives

\[
H'(\theta)=\frac{i}{2}\,\mathcal R(e^{i\theta}),
\quad
\mathcal R(z)=\sum_jw_j
\left(\frac{z}{z-1/b_j}
+\frac{\overline{b_j}}{z-\overline{b_j}}\right).
\tag{13}
\]

If \(H\) were constant on an open interval, the rational function
\(\mathcal R\) would vanish on infinitely many regular points of the circle, hence identically. But at \(z_0=1/b\) for any value \(b\) among the \(b_j\), the residue is

\[
\operatorname{Res}_{z=z_0}\mathcal R(z)=
\begin{cases}
z_0\sum_{j:b_j=b}w_j,& |b|<1,\\
2z_0\sum_{j:b_j=b}w_j,& |b|=1.
\end{cases}
\tag{14}
\]

Indeed the second family of poles lies in the closed unit disk, so it cannot cancel a pole with \(|z_0|>1\); on the unit circle the two contributions coincide and **reinforce**. Every displayed residue is nonzero because the weights are positive. This contradiction proves the lemma. Positivity, finite support, and fixed centers are essential here: this is not a rigidity assertion for arbitrary signed or continuous potentials.

Now suppose some factor is DC unsafe: \(\tau_j(0)>0\). By continuity, that factor is active throughout a small neighborhood of zero. Since each equation \(\tau_k(\theta)=0\) has only isolated solutions on the arc (a nonzero finite center cannot have constant distance from a nontrivial circular subarc), choose a smaller open interval where the active index set \(A=\{k:\tau_k(\theta)>0\}\) is fixed and nonempty. There,

\[
F(\theta)=\sum_{k\in A}s_k
\bigl(-\log\rho_k+h(\lambda_k)\bigr)
+\sum_{k\in A}s_k\lambda_k
\log|1-e^{i\theta}/a_k|.
\tag{15}
\]

All weights \(s_k\lambda_k\) are strictly positive. The rigidity lemma makes \(F\) nonconstant on that interval, hence \(F(\theta)\ne D=F(0)\) at some fixed point of the observed arc. By (5), if \(F(\theta)>D\) the normalized product diverges in modulus there; if \(F(\theta)<D\) it tends to zero, so its distance from one tends to one. Uniform prediction is impossible.

If instead every factor is DC safe but some \(\tau_j\) is positive elsewhere on the arc, then \(D=0<M\) and (6) prevents prediction. If every \(\tau_j\le0\) on the arc, RE-244's uniform remainder estimate and finite-product expansion prove \(G_T=1+O(T^{-1/2})\). This finishes (7).

## 4. Controls, prior art, and scope of the obstruction

The unsafe regime in the theorem is nonempty. Take a single real center \(\rho=0.9\), arc half-width \(\alpha=0.1\), and \(\lambda=0.2\). Direct evaluation gives
\(r\approx0.153126\), \(cr\approx0.918755<1\),
\(\tau(0)\approx0.206589>0\), and
\(\tau(\alpha)\approx0.270735>\tau(0)\).
Thus DC normalization subtracts a positive exponent but leaves exponential arc failure; the example is diagnostic, not a substitute for (13)--(15).

The two logically different failure modes matter. When \(M>D\), a pointwise exponential blowup certifies failure. When \(M=D\) with DC-unsafe factors, the exponential error rate in (6) vanishes but (15) forces a pointwise amplitude deficit: the normalized product still cannot approach one. This is why the proof does **not** infer non-prediction from (6) alone in the zero-rate case.

The negative-binomial tail estimates are inherited from RE-244 and are instances of classical incomplete-beta/Taylor asymptotics (NIST DLMF section 8.18; Nemes--Olde Daalhuis, *Uniform Asymptotic Expansion for the Incomplete Beta Function*, SIGMA 12 (2016), 101). Non-flatness of finite positive logarithmic potentials is an elementary rational-function rigidity phenomenon; the neighboring classical boundary theory of constant-modulus functions and finite Blaschke products is discussed, for example, by Stephenson--Sundberg, *Level Curves of Inner Functions*, Proc. London Math. Soc. s3-51 (1985), 77--94, DOI 10.1112/plms/s3-51.1.77. That paper is context, not an imported lemma or a novelty claim. Equations (12)--(14) are a self-contained proof for the precise weights and centers here. No new external theorem is load-bearing, so SOURCES.md need not change.

This result has **fixed** \(J\), centers, scales and truncation ratios, and requires the strict first-omitted-term geometric regime (3). It does not cover moving or growing constellations, signed/additive combinations, saddle-point tail regimes, non-Taylor approximants, or any inverse bounds converting prediction into optimal Wiener cost. In particular it neither proves a new bound for the Robin divisor-sum functional nor establishes the Riemann hypothesis.

## Research consequence

RE-244's DC-safety condition is removable without weakening its factorwise necessity-and-sufficiency conclusion. A finite Taylor product cannot be rescued by an exponentially large normalizing denominator: the exact normalized growth envelope is \(M-D\), and the only apparent zero-rate loophole is closed by rigidity of the positive finite source potential. This closes the fixed-parameter, finite-stage, strictly geometric coupled-normalization escape, not the broader multi-center, source-specific Robin/RH problem.
