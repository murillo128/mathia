# RE-240 — Symmetric mixed phases have a sharp exponential Wiener discount

**Status:** EXACT-DERIVED + MULTI-CENTER-SERIAL-COMPOSITION + MIXED-PHASE-INTERFERENCE + WIENER-NORM-ASYMPTOTIC + PRIOR-ART-AUDIT.

**Parent findings:** RE-237, RE-239.

RE-237 shows that same-ray factors have no Wiener discount. RE-239 bounds the discount under small phase changes by the square of the displacement times the truncation degree. A conjugate two-center pair provides a complementary *sharp* formula: its discount has a strictly positive exponential rate at every sufficiently small fixed nonzero phase separation. The theorem identifies that rate and controls its error uniformly in the truncation order; it does **not** claim that the paired product is a better predictor.

## 1. Sharp two-center theorem

Fix \(R<\infty\). For \(m\ge1\), \(N\ge0\), \(0<\rho\le R\), and a common base angle \(\varphi_*\), take the RE-237 polynomials \(Q_\pm\) with the same \(m,N,\rho\) and centers

\[
a_\pm=\rho e^{i(\varphi_*\pm\beta)}.
\]

When \(Q_\pm(1)\ne0\), put \(F_\pm=Q_\pm/Q_\pm(1)\).
The **relative Wiener cost**, invariant under these nonzero scalar normalizations, is

\[
W_{m,N,\rho}(\beta)
:=\frac{\|F_+F_-\|_A}{\|F_+\|_A\|F_-\|_A}.
\tag{1}
\]

Set

\[
p=\frac1{1+\rho},\quad q=\frac{\rho}{1+\rho},\qquad
b(\rho,\beta)
=q^2+p^2+2pq\cos\beta
=1-4pq\sin^2(\beta/2).
\tag{2}
\]

There exist \(\beta_0(R)>0\) and \(C_R<\infty\), independent of \(m,N,\rho\), for which

\[
\boxed{
\left|\log W_{m,N,\rho}(\beta)
-N\log b(\rho,\beta)\right|
\le C_R\beta^2
\qquad (|\beta|\le\beta_0(R)).
}
\tag{3}
\]

In particular, the Wiener discount \(D=-\log W\) satisfies

\[
\boxed{
D=-N\log b(\rho,\beta)+O_R(\beta^2)
=Npq\,\beta^2+O_R(N\beta^4+\beta^2).
}
\tag{4}
\]

For every *fixed* \(0<\rho\le R\) and nonzero \(\beta\) in the theorem's interval,

\[
\lim_{N\to\infty}\frac{D}{N}
=-\log b(\rho,\beta)>0
\tag{5}
\]

along any sequence of \(m\ge1\) and admissible nonzero normalizations. The gain is exponential rather than a mere polynomial prefactor. The full angular separation of the two centers is \(2|\beta|\), so the rate can also be written
\(-\log[1-4pq\sin^2(\Delta/4)]\).

Equation (4) makes the quadratic bound of RE-239 asymptotically sharp in a concrete serial architecture. The uniform \(O_R(\beta^2)\) remainder also covers the crossover \(\beta\asymp N^{-1/2}\).

## 2. Reduce the relative norm to a rotated positive-coefficient polynomial

RE-237's exact coefficient formula, reconstructed in RE-239, gives the positive probability polynomial

\[
P(z)=\sum_{j=0}^{N}p_jz^j
=\mathbb E(q+pz)^K,
\qquad
\Pr(K=k)\ \propto\
\binom{m+k-1}{k}(1+\rho^{-1})^k.
\tag{6}
\]

If \(E=N-K\), then

\[
P(z)=(q+pz)^N h((q+pz)^{-1}),
\quad
h(u)=\mathbb E u^E,
\quad
\Pr(E=d)\le q_R^d,\qquad
q_R=\frac{R}{1+R}<1.
\tag{7}
\]

The phases, monomial shifts, and normalization scalars do not affect the norm ratio (1). After a common rotation of the polynomial variable,

\[
\boxed{
W_{m,N,\rho}(\beta)
=
\big\|P(e^{i\beta}z)P(e^{-i\beta}z)\big\|_A.
}
\tag{8}
\]

This is the exact, finite-dimensional object whose Wiener norm is to be estimated.

## 3. The upper bound pairs the two conjugate binomial factors

Write \(A_\pm(z)=q+p e^{\pm i\beta}z\). Their product has the special form

\[
H_\beta(z)=A_+(z)A_-(z)
=q^2+2pq\cos\beta\,z+p^2z^2.
\tag{9}
\]

For \(|\beta|<\pi/2\), all its coefficients are nonnegative, so

\[
\|H_\beta^t\|_A=H_\beta(1)^t=b(\rho,\beta)^t
\quad(t\ge0).
\tag{10}
\]

Also \(\|A_\pm^s\|_A=(q+p)^s=1\). If \(E=d\), \(E'=e\) are independent reverse-depth variables from (7), their mixture term factors into
\(H_\beta^{N-\max(d,e)}\) times an unpaired power of one \(A_\pm\). Submultiplicativity and the triangle inequality give

\[
\begin{aligned}
W_{m,N,\rho}(\beta)
&\le\mathbb E\, b^{N-\max(E,E')}\\
&=b^N\mathbb E\, b^{-\max(E,E')}.
\end{aligned}
\tag{11}
\]

Choose \(\beta_0(R)\) small enough that
\(s=-\log b\ge0\) is small uniformly in \(\rho\le R\), and \(q_Re^{2s}<1\).
The geometric tail in (7) then bounds the exponential moment of
\(T=\max(E,E')\) and its first derivative uniformly. Since

\[
\mathbb E e^{sT}
\le1+s\,\mathbb E(Te^{sT})
\le1+C_Rs,
\quad
s=O_R(\beta^2),
\]

we obtain

\[
\boxed{
\log W_{m,N,\rho}(\beta)
\le N\log b+C_R\beta^2.
}
\tag{12}
\]

## 4. A common-circle evaluation supplies the matching lower bound

Because \(P\) has real coefficients, evaluating (8) at \(z=1\) gives

\[
W_{m,N,\rho}(\beta)
\ge |P(e^{i\beta})|^2
=b^N\left|h((q+p e^{i\beta})^{-1})\right|^2.
\tag{13}
\]

The geometric majorant in (7) makes \(h\) analytic with uniformly bounded first and second derivatives in a fixed neighborhood of \(u=1\); \(h(1)=1\), so it is uniformly zero-free in a smaller neighborhood. Its logarithm can be chosen there. The derivative at \(\beta=0\) of the *real part* of
\(\log h((q+p e^{i\beta})^{-1})\) vanishes: the derivative of the inner argument is purely imaginary, and \(h'(1)=\mathbb E E\) is real. Taylor's theorem thus gives

\[
\left|\log\left|
h((q+p e^{i\beta})^{-1})\right|\right|
\le C_R\beta^2
\quad(|\beta|\le\beta_0(R)).
\tag{14}
\]

Equations (13)--(14) imply

\[
\boxed{
\log W_{m,N,\rho}(\beta)
\ge N\log b-C_R\beta^2.
}
\tag{15}
\]

Together with (12), this proves (3). As
\(b=1-pq\beta^2+O(\beta^4)\) uniformly, (4) follows.

## 5. Falsification controls and predictive scope

At \(\beta=0\), \(b=1\), and RE-237 gives \(W=1\) exactly; (3) agrees without a spurious constant loss. For \(N=0\), both factors are monomials and \(W=1\), also consistent with (3). Direct finite coefficient convolutions at \(\rho=2.29\), \(m\approx N/3.992\), and \(\beta=0.2,0.4,0.7\) give positive ratios \(W/b^N\) close to one (for example, at \(N=60,\beta=0.4\), \(W\approx0.130407\) versus \(b^{60}\approx0.130247\)). These are private algebraic checks, not the proof. The argument uses (7)--(15) and does not assume a normal approximation or fixed \(m/N\).

The small-angle restriction is load-bearing. If \(\cos\beta<0\), the middle coefficient of \(H_\beta\) becomes negative and the identity (10) fails. When \(\rho\to\infty\), the edge-defect tail bound ceases to be uniform. The theorem does not assert its exponential rate uniformly as \(\rho\to0\), where \(pq\to0\); equation (3) itself remains uniform.

**Predictor status is separate.** Both factors here have identical truncation and conjugate center phases, but (3) concerns coefficient cancellation alone. For either factor to approximate one uniformly on the observed arc, its off-center Taylor tail must still contract. If the arc has half-width \(\alpha\), a center at \(\rho e^{\pm i\beta}\) experiences the worst contraction radius

\[
r_{\max}(\rho,\alpha,\beta)
=
\frac{\sqrt{\rho^2+1-2\rho\cos(\alpha+|\beta|)}}{\rho}
\tag{16}
\]

when \(\alpha+|\beta|<\pi\); this is larger than the same-ray radius at fixed \(\rho,\alpha\). The extra prediction cost can outweigh the Wiener discount. Therefore (3) is **not** a proof that the global separated-prediction constant \(C_{\rm sep}\le5.996390\) improves, nor a new Robin inequality. A coupled product need not obey factorwise prediction and would require its own uniform approximation analysis.

The generic tools are elementary positive-coefficient polynomial multiplication, the Wiener algebra triangle/submultiplicative estimates, and analytic probability-generating functions with exponential moments; no novelty is claimed for those ingredients individually. The line-specific result is the sharp cancellation exponent for the particular truncated negative-binomial predictor law of RE-237/RE-239. Targeted searches of polynomial norm and Wiener-algebra literature did not identify a load-bearing external theorem; the derivation is self-contained, so SOURCES.md does not need a new dependency.

## Research consequence

The live serial multi-center search now has both sides of a sharp local contrast. Same-ray stages have **zero** discount (RE-237), a general coalescing family has **at most quadratic** discount (RE-239), while a symmetric two-ray family has the **exact leading exponential rate** (4). The next unresolved question is no longer whether mixed phases can cancel coefficients: they can. It is whether the cancellation survives the uniform predictor-error and fixed-support-corridor constraints strongly enough to lower the normalized spectral exponent, or whether a coupled or parallel construction is needed.
