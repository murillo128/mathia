# PC-437 — Periodic analytic masks preserve sharp prime-log thinning beyond finite Fourier support

**Status:** EXACT-DERIVED + CLASSICAL-REDUCTION + CONTROL-ONLY. PC-436 proves sharp log-sample completeness for finite exponential-polynomial masks, but its translated-Blaschke proof does not cover a general infinite Fourier expansion. For every nonzero real-analytic periodic mask, even one with infinitely many nonzero Fourier coefficients and infinitely many real zeros, the same sharp criterion holds. The reason is not an infinite-frequency Blaschke construction: the real zero divisor has only finitely many generators modulo a period, and the remaining multiplier is bounded above and away from zero. This is an elementary zero-factorization and weighted-norm-equivalence consequence of PC-436, not a new zeta-zero condition.

## 1. Exact theorem

Fix \(a>0\) and \(0<\sigma<1\). Let \(w:\mathbb R\to(0,\infty)\) satisfy the PC-435 two-sided envelope, for \(c,C>0\), \(K\ge0\):
\[
c\min\{|t|,1\}e^{-a|t|}
\le w(t)\le C(1+|t|)^K e^{-a|t|}\quad\text{a.e.}
\tag{1}
\]
Let \(D:\mathbb R\to\mathbb C\) be nonidentically zero, real analytic, and periodic with period \(T>0\). Set
\[
W_D(t)=w(t)|D(t)|^2,\qquad
\mathscr H_D=L^2(\mathbb R,W_D(t)\,dt).
\tag{2}
\]
For distinct \(X\subset[2,\infty)\) tending to infinity, write
\[
q_x(t)=e^{it\log x},\qquad
v_{x,\sigma}(t)=1-x^{1-\sigma}e^{it\log x}.
\tag{3}
\]
**Theorem.** Regardless of the number of nonzero Fourier coefficients of \(D\),
\[
\boxed{
\overline{\operatorname{span}}\{q_x:x\in X\}=\mathscr H_D
\iff
\overline{\operatorname{span}}\{v_{x,\sigma}:x\in X\}=\mathscr H_D
\iff
\sum_{x\in X}x^{-\pi/a}=\infty .
}
\tag{4}
\]
If the sum converges, the orthogonal complements of both systems contain a common infinite-dimensional subspace. The exact Blaschke endpoint is included, even when \(D\) has infinitely many real zeros or arbitrarily large but finite orders of vanishing within one period.

## 2. Finite real-zero divisor, despite infinite Fourier support

Put \(\beta=2\pi/T\). Because \(D\) is nonzero and real analytic, it has only finitely many distinct zeros \(t_1,\ldots,t_r\) modulo \(T\), each of positive finite order \(m_1,\ldots,m_r\). With \(P=1\) when \(r=0\), define the finite exponential polynomial
\[
P(t)=\prod_{j=1}^{r}
       (e^{i\beta t}-e^{i\beta t_j})^{m_j}.
\tag{5}
\]
Since the derivative of \(e^{i\beta t}\) is nonzero on the real axis, \(P\) has precisely the same real zeros and orders as \(D\). The quotient
\[
E(t)=D(t)/P(t)
\tag{6}
\]
has removable singularities at these zero classes and extends to a continuous, nowhere-zero \(T\)-periodic function. Compactness of one period gives
\[
0<m\le |E(t)|\le M<\infty
\quad\text{for every real }t.
\tag{7}
\]
Set \(W_P=w|P|^2\). Equation (7) gives
\[
m^2W_P\le W_D\le M^2W_P
\tag{8}
\]
and therefore identical weighted \(L^2\) vector spaces with equivalent norms:
\[
m\|f\|_{L^2(W_P)}
\le\|f\|_{L^2(W_D)}
\le M\|f\|_{L^2(W_P)}.
\tag{9}
\]
Every fixed linear span is dense in one space if and only if it is dense in the other. PC-436 applies to the finite exponential polynomial \(P\), proving (4). This proof never expands the infinite Fourier series of \(E\).

## 3. Joint infinite-codimension nullspace

For a convergent sampling sum, PC-436 §3 constructs an infinite-dimensional linear space \(\mathcal N_P\subset L^2(W_P)\) such that
\[
\int_{\mathbb R}h(t)W_P(t)\,dt=0,\qquad
\int_{\mathbb R}h(t)W_P(t)e^{-it\log x}\,dt=0
\quad(x\in X,\ h\in\mathcal N_P).
\tag{10}
\]
The map
\[
(Th)(t)=h(t)/|E(t)|^2
\tag{11}
\]
is injective and bounded from \(L^2(W_P)\) into \(L^2(W_D)\), because
\[
(Th)W_D=hW_P,\qquad
\|Th\|_{L^2(W_D)}^2
=\int_{\mathbb R}\frac{|h(t)|^2W_P(t)}{|E(t)|^2}\,dt
\le m^{-2}\|h\|_{L^2(W_P)}^2.
\tag{12}
\]
The Fourier moment conditions (10) pass unchanged to \(Th\). Hence \(T\mathcal N_P\) is one infinite-dimensional subspace simultaneously orthogonal to both the marked and unmarked sample families in (3). The proof is insensitive to zeros of \(D\), because it divides only by the nonvanishing \(E\).

## 4. Infinite-Fourier control and Prime-Circle application

For \(b>0\) and real \(\kappa\ne0\),
\[
D(t)=(1-e^{ibt})e^{\kappa\cos(bt)}
\tag{13}
\]
is an entire periodic function with infinitely many nonzero Fourier harmonics and real zeros at \(2\pi k/b\). Here \(P(t)=1-e^{ibt}\), while the residual multiplier obeys
\[
e^{-|\kappa|}\le |D(t)/P(t)|\le e^{|\kappa|}.
\tag{14}
\]
Thus the infinite Fourier tail changes no completeness threshold and no sparse-family codimension.

For the zero-free matched PC-424/PC-435 Hilbert control \(g_{0,\sigma}\) with \(w_{0,\sigma}\) of exponential-envelope exponent \(a=\pi\), the PC-433 Hilbert--Schmidt embedding \(\mathcal J\) gives, for every prime subset \(\mathcal P\),
\[
\boxed{
\overline{\operatorname{span}}\{
\mathcal J[(1-p^{1-\sigma}e^{it\log p})Dg_{0,\sigma}]:
p\in\mathcal P\}
=\mathcal A
\iff
\sum_{p\in\mathcal P}p^{-1}=\infty.
}
\tag{15}
\]
The masked marked translates obey the same criterion. The sparse case has infinite codimension for both. This mask is only an auxiliary matched control, not asserted to arise intrinsically from the regular-polygon construction.

For the genuine zeta-weighted seed, boundedness of periodic \(D\) preserves divergent-sum **sufficiency**, but the corresponding sparse-family converse is not proved: the unmasked genuine weight lacks the two-sided lower envelope. The full zeta factor cannot be treated as a nonvanishing bounded periodic residual multiplier.

## 5. Mathematical delta, prior art and boundaries

PC-436's direct finite-mask argument prescribes zeros at finitely many translates of every log-sample. Extending that construction term by term to infinite Fourier support would generally require infinitely many translates and can fail. The new exact boundary is that **periodic real-analytic masks can have infinite Fourier support without this obstruction**: finitely many real zero classes are removed by \(P\), and the rest is a bounded change of Hilbert norm. It is the finitely generated real zero divisor, not finite Fourier support, that matters for this class.

The ingredients are classical analytic zero isolation, finite factorization on the circle, and equivalence of weighted Hilbert norms, combined with PC-436. The deeper classical strip Blaschke and Paley--Wiener inputs are already anchored in the line's SOURCES.md (Duren, Remmert, Paley--Wiener). Neither the factorization nor the derived threshold is presented as a new general theorem beyond those dependencies.

**Audit and limitations:** verify one common period, finite-order zeros, complete multiplicities in (5), and the uniform **global** bounds (7). The argument does not cover quasiperiodic/nonperiodic masks with infinitely many inequivalent real zero positions, smooth masks with flat zeros, masks vanishing on a real interval, or unbounded residual multipliers. The nonarithmetic PC-434 cusp control obeys the same masked theorem, so no critical-line selection or RH implication follows.
