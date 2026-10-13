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

## 4. Prior art, audit and implication

Both ingredients are classical: finite Bonferroni/inclusion-exclusion (cf. D. R. Heath-Brown, *Lectures on sieves*, arXiv:math/0209360, 2002) and the prime-number-theorem primorial asymptotic. Heath-Brown is already anchored in this line's SOURCES.md. The Mathia-specific delta is the **uniform positive witness on the actual rough counterterm** together with the explicit bow-depth threshold (5), not a new general sieve theorem.

The decisive audit checks are the parity and truncation sign in (1), translated-interval multiple counting in (2), \(p_{M_\delta}<R\), and the power gap in (4). No statement about the size of the genuinely oscillatory residual, the prime contribution, the required signed high-pass, zeta-zero exclusion, or RH follows. A useful continuation must retain phase information in the omitted large-\(w_R\) terms or change the analytic decomposition; increasing the error budget by absolute values cannot cross the displayed threshold.
