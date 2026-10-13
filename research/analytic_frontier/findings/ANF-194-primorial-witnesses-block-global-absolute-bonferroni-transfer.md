# ANF-194 — Primorial witnesses obstruct global absolute-error Bonferroni transfer

**Status:** EXACT-DERIVED + CLASSICAL-BONFERRONI-IDENTITY + CLASSICAL-PRIMORIAL-ASYMPTOTIC + NECESSARY-DEPTH-METHOD-OBSTRUCTION. This is not a lower bound for the oscillatory rough sum or for the prime–rough residual.

## 1. Exact absolute-error witness

Use the actual counterterm of ANF-193, with
\[
R=\exp((\log X)^{1/10}),\quad P(R)=\prod_{p<R}p,\quad
Q_R(n)=c_R\mathbf1_{(n,P(R))=1},\qquad
c_R=\frac{P(R)}{\varphi(P(R))}\ge1.
\]
Set \(w_R(n)=\#\{p<R:p\mid n\}\). For an **even** integer \(2\le m\le\pi(R)\), let
\[
B_{m-1}(n)=\sum_{j=0}^{m-1}(-1)^j\binom{w_R(n)}j,\qquad
d_m=\prod_{j=1}^m p_j,
\]
where \(p_j\) is the \(j\)-th prime. The finite alternating-binomial identity is
\[
\boxed{\quad
\mathbf1_{\{w_R(n)=0\}}-B_{m-1}(n)
=\mathbf1_{\{w_R(n)\ge m\}}\binom{w_R(n)-1}{m-1}\ge0.
\quad}\tag{1}
\]
Indeed, for \(w\ge1\), the partial sum equals
\(\sum_{j=0}^{m-1}(-1)^j\binom wj=(-1)^{m-1}\binom{w-1}{m-1}\)
if \(w\ge m\), and is zero for \(1\le w<m\). For \(w=0\) the indicator and polynomial both equal one. The parity of \(m\) fixes the nonnegative sign in (1).

Every multiple of \(d_m\) has \(w_R(n)\ge m\), since \(p_m<R\). Thus each such integer contributes at least \(c_R\) to the positive truncation error. In **every** interval \(I\subset[X,3X]\) containing \(H\) consecutive integers,
\[
\boxed{\quad
\mathcal E_m(I):=\sum_{n\in I}|Q_R(n)-c_RB_{m-1}(n)|
\ge c_R\#\{n\in I:d_m\mid n\}
\ge c_R\left(\frac H{d_m}-1\right).
\quad}\tag{2}
\]
Neither the position of \(I\) nor any oscillatory phase enters this lower bound.

## 2. Necessary depth for the full bow interval

Fix \(1/2<\alpha<1\), a full bow length \(K=X^{\alpha+o(1)}\), and target amplitude \(a_X=\sqrt{\Delta X\log X}\), where \(\Delta>0\) is fixed. Mathia's distinguished regime has \(\alpha=1-2\varepsilon\) with \(0<\varepsilon<1/16\).

For any fixed \(0<\delta<\alpha-\tfrac12\), define
\[
M_\delta=\left\lfloor\left(\alpha-\tfrac12-\delta\right)
\frac{\log X}{\log\log X}\right\rfloor.
\]
The prime-number theorem implies
\[
\log d_M=\sum_{j\le M}\log p_j=(1+o(1))M\log M,
\]
so
\[
d_{M_\delta}=X^{\alpha-1/2-\delta+o(1)}.
\tag{3}
\]
Also \(p_{M_\delta}\asymp\log X<R\) eventually, because
\(\log R=(\log X)^{1/10}\gg\log\log X\).
For **every even** \(2\le m\le M_\delta\), monotonicity of \(d_m\), (2) and \(c_R\ge1\) yield uniformly for \(|I|=K\)
\[
\boxed{\quad
\mathcal E_m(I)\ge X^{1/2+\delta-o(1)}
\gg a_X.
\quad}\tag{4}
\]
In particular, if an even depth \(m(X)\) has
\(\mathcal E_{m(X)}(I_X)=o(a_X)\) on full bow intervals \(I_X\), a **necessary**, not sufficient, condition is
\[
\boxed{\quad
\liminf_{X\to\infty}\frac{m(X)\log\log X}{\log X}
\ge\alpha-\tfrac12.
\quad}\tag{5}
\]
To verify (5), assume the liminf is smaller, choose a fixed \(\delta>0\) leaving a gap, and apply (4) along the subsequence where \(m(X)\le M_\delta\).

ANF-193 instead uses even
\(m=2\lfloor(\log X)^{1/20}/2\rfloor\). Then
\(d_m=\exp(o(\log X))=X^{o(1)}\), so the same actual-source witness gives the stronger failure
\[
\boxed{\quad
\mathcal E_m(I)\ge X^{\alpha-o(1)}
\quad (|I|=K).
\quad}\tag{6}
\]
Its \(o(H)\) critical-block cancellation theorem remains intact: a relative \(o(H)\) bound on a block \(H=O(a_X)\) is categorically different from an **absolute** \(o(a_X)\) error after extending to \(K\gg a_X\).

## 3. The precise method boundary

ANF-193 uses shallow Bonferroni truncation so every surviving divisor is bounded by \(D=R^m=X^{o(1)}\) and termwise third-derivative cancellation is inexpensive. At the depth required by (5),
\(m\asymp(\log X)/\log\log X\), its **same crude support ceiling** instead obeys
\[
\log(R^m)\asymp
\frac{(\log X)^{11/10}}{\log\log X}\gg\log X.
\tag{7}
\]
Thus the *specific* divisor-count and progression-error argument in ANF-193 cannot be extended unchanged to the needed absolute prefix scale. This says nothing about the true number of useful divisors, nor about a differently weighted sieve.

For any weights \(|z_n|=1\), including the distinguished phase \(z_n=(n/X)^{-iU}\), the triangle inequality gives only
\[
\left|\sum_{n\in I}
(Q_R(n)-c_RB_{m-1}(n))z_n\right|
\le\mathcal E_m(I).
\]
A **large absolute error is not a large twisted error**. Equations (4)–(6) exclude one way of discarding the omitted sieve terms; they do not preclude cancellation among them, another divisor decomposition, or prime–rough correlation at the original height.

### Genuine retained divisors obstruct the same cubic estimate when \(\alpha>5/6\)

The ceiling \(R^m\) in (7) is deliberately crude. The difficulty is not
merely that this ceiling exceeds \(X\): **some divisors that really occur**
in the lower Bonferroni polynomial already defeat the termwise
third-derivative estimate used by ANF-193.

Suppose \(5/6<\alpha<1\), \(K=X^{\alpha+o(1)}\), and an even depth
\(m=m(X)\le\pi(R)\) satisfies
\(\mathcal E_m(I_X)=o(a_X)\) on a full bow interval \(I_X\) of
length \(K\). By the necessary condition (5),
\[
\liminf_{X\to\infty}\frac{m\log\log X}{\log X}
\ge\alpha-\tfrac12.
\tag{8}
\]
Choose \(0<\xi<\alpha-5/6\) and put
\[
q=\left\lfloor(\tfrac13+\xi)\frac{\log X}{\log\log X}\right\rfloor,
\qquad d=\prod_{j=1}^{q}p_j.
\]
The prime-number theorem yields
\[
q<m,\quad p_q<R,\quad
d=X^{1/3+\xi+o(1)}=o(X^{\alpha-1/2}).
\tag{9}
\]
Here \(q<m\) follows from
\(1/3+\xi<\alpha-1/2\), and \(p_q<R\) because
\(p_q\asymp\log X\) whereas
\(R=\exp((\log X)^{1/10})\gg\log X\).
Thus **\(d\) is a genuine squarefree retained divisor**
in the exact expansion of \(B_{m-1}\), with coefficient
\(\mu(d)=(-1)^q\), rather than an artifact of the support bound \(R^m\).

On its progression \(n=dk\) inside \(I_X\) the number of sites and
the cubic derivative at every fixed-annulus height
\(A_0X^2\le |U|\le B_0X^2\) satisfy
\[
N=\frac Kd+O(1)
 =X^{\alpha-1/3-\xi+o(1)}
 \gg a_X,
\qquad
|f_d'''(k)|\asymp\frac{d^3}{X}
 =X^{3\xi+o(1)}\gg1.
\tag{10}
\]
The \(N|f_d'''|^{1/6}\) contribution in the *specific* ANF-193
third-derivative bound (its equation (11)) exceeds the trivial
\(N\) bound by a power of \(X\). Replacing it by \(N\) still
leaves an individual absolute upper-bound allowance
\(\gg a_X\). Consequently, **no choice of Bonferroni depth can both
make its omitted terms \(o(a_X)\) by absolute value and prove the
full-interval \(o(a_X)\) estimate by summing precisely those
termwise cubic-derivative bounds** throughout the retained divisor
family. This is stronger than observing that the *maximum permitted*
divisor may be too large.

This is an obstruction to that **combination of upper-bound methods**,
not a lower bound for any one oscillatory progression or for their
signed sum. Better progression bounds, cancellation between divisors,
retention of omitted-term phases, or a different sieve decomposition
remain outside the obstruction. The threshold \(5/6\) concerns the
cubic-derivative method; it is not an intrinsic critical exponent of
the prime-minus-rough residual.

## 4. Prior art, audit and implication

Both ingredients are classical: finite Bonferroni/inclusion-exclusion (cf. D. R. Heath-Brown, *Lectures on sieves*, arXiv:math/0209360, 2002) and the prime-number-theorem primorial asymptotic. The cubic test used in (10) is the classical third-derivative estimate already stated and applied in ANF-193; no new general exponential-sum estimate is asserted. Heath-Brown is already anchored in this line's SOURCES.md. The Mathia-specific delta is the **uniform positive witness on the actual rough counterterm** together with the explicit bow-depth threshold (5), not a new general sieve theorem.

The decisive audit checks are the parity and truncation sign in (1), translated-interval multiple counting in (2), \(p_{M_\delta}<R\), and the power gap in (4), plus actual inclusion \(q<m\), \(p_q<R\), the fixed-annulus cubic scale and \(N\gg a_X\) in (9)--(10). No statement about the size of the genuinely oscillatory residual, the prime contribution, the required signed high-pass, zeta-zero exclusion, or RH follows. A useful continuation must retain phase information in the omitted large-\(w_R\) terms or change the analytic decomposition; increasing the error budget by absolute values cannot cross the displayed threshold.
