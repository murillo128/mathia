# PL-456 — Quantitative pointwise centered-prime frame from isolated jumps

**Evidence/status:** LITERATURE+EXACT-DERIVED + QUANTITATIVE POINTWISE LOWER FRAME / GENERIC ATOMIC CONTROL.

**Parent findings:** PL-421, PL-445, PL-452, PL-453, PL-454, PL-455.

## Claim

For the four reduced residue classes \(U_5=\{1,2,3,4\}\), \(X>1\), \(1\le H\le X/2\), and every \(t\in\mathbb R\), use the *phase-matched* centered prime windows of PL-452--PL-455:
\[
P_{a,t}(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n)n^{-it},\qquad
Q_t(y)=\int_y^{y+H}x^{-it}\,dx,\qquad
R_{a,t}(y)=P_{a,t}(y)-\tfrac14Q_t(y).
\]
Write \(S^R_X(t)_{ab}=\int_X^{2X}R_{a,t}(y)\overline{R_{b,t}(y)}\,dy\). There is an absolute \(X_0\) such that for **all** \(X\ge X_0\), **all** \(1\le H\le X/2\), and **all** real \(t\),
\[
\boxed{S^R_X(t)\succeq \frac{X\log X}{512}\,I_4.}\tag{1}
\]
The particular positive constant is inessential. Consequently, for **any** finite, nonzero positive Borel measure \(\omega\) on the frequency axis, including a single point mass,
\[
\int_{\mathbb R}S^R_X(t)\,d\omega(t)\succeq
\frac{\omega(\mathbb R)X\log X}{512}\,I_4.\tag{2}
\]
This is a uniform **absolute quantitative lower eigenvalue bound**, improving PL-455's qualitative pointwise rank-four result. It does **not** establish a frame lower bound comparable to the full diagonal self-pair mass \(XH\log X\) for growing \(H\), nor the \(1/4\) threshold for the diagonal-normalized PL-421 inverse-dephasing cone.

## A density of unpaired atomic endpoints

Set \(m=\lfloor H\rfloor\ge1\), \(I_X=(5X/4,7X/4)\), and for each \(a\in U_5\) define
\[
G_a(H)=\{p\in I_X:\ p\text{ prime},\ p\equiv a\pmod5,\
\Lambda(p+m)=\Lambda(p+m+1)=0\}.
\tag{3}
\]
The fixed-modulus prime number theorem supplies
\[
\#\{p\in I_X:p\equiv a\pmod5\}
=\left(\frac18+o(1)\right)\frac{X}{\log X}.\tag{4}
\]
For every integer \(1\le k\le X/2+1\), the uniform two-prime Selberg upper bound and singular-series estimate (Lichtman--Teräväinen 2022, Lemmas 2.3--2.4) give
\[
\#\{p\in I_X:\ p,p+k\text{ both prime}\}
\ll \frac{X}{(\log X)^2}
\left(\frac{k}{\varphi(k)}\right)^2
\ll \frac{X(\log\log(3X))^2}{(\log X)^2}.
\tag{5}
\]
The total number of proper prime powers below \(3X\) is \(O(\sqrt X\log X)\). For each fixed translate \(k\), at most that many additional primes \(p\) have \(p+k\) a proper prime power. Apply these bounds to \(k=m,m+1\). Uniformly in \(H\), the excluded \(p\) are \(o(X/\log X)\), even before restriction to a residue class, so for all large enough \(X\)
\[
\#G_a(H)\ge \frac{X}{16\log X}\quad(a\in U_5),\qquad
\#G(H)\le\frac{X}{\log X},\quad G(H)=\bigcup_aG_a(H).
\tag{6}
\]
The last bound follows from the prime number theorem on \(I_X\).

Let \(h=1/4\). For any \(p\in G(H)\), the **only jump** of the four functions \(P_{a,t}(y)\) on \((p-h,p+h)\) is the outgoing prime \(p\) at \(y=p\), in its own residue class. Indeed outgoing jumps occur at integers; another integer cannot lie in this neighborhood. Incoming jumps occur at \(y=n-H\) for prime-power integers \(n\); if \(|n-H-p|<h\), then \(n\) is either \(p+m\) or \(p+m+1\), and neither is a prime power by (3). This checks both integral and nonintegral \(H\), including lengths arbitrarily close to integers. All these neighborhoods are disjoint and contained in \((X,2X)\).

## Local jump means force a uniform \(L^2\) floor

For \(c=(c_a)_{a\in U_5}\in\mathbb C^4\), set
\[
F_c(y)=\sum_a\overline{c_a}R_{a,t}(y),\qquad
\kappa=\tfrac14\sum_a\overline{c_a},\qquad
|\kappa|\le\tfrac12\|c\|_2.
\]
Let \(\mu_p^-\) and \(\mu_p^+\) be the means of \(F_c\) over \((p-h,p)\) and \((p,p+h)\); let \(\overline Q_p^\pm\) be the corresponding means of \(Q_t\). Because the atomic source is constant on each half-neighborhood and has one outgoing jump at \(p\),
\[
D_p:=\mu_p^+-\mu_p^-
=-\overline{c_{a(p)}}(\log p)p^{-it}
-\kappa(\overline Q_p^+-\overline Q_p^-).
\tag{7}
\]
The key uniformity is elementary:
\[
Q_t'(y)=(y+H)^{-it}-y^{-it},\qquad |Q_t'(y)|\le2
\quad(t\in\mathbb R).
\]
Consequently \(|\overline Q_p^+-\overline Q_p^-|\le2h\); the centering error in (7) has modulus at most \(h\|c\|_2\) regardless of \(t,H\).

Jensen's inequality on the two half-neighborhoods gives
\[
\int_{p-h}^{p+h}|F_c(y)|^2\,dy
\ge h(|\mu_p^-|^2+|\mu_p^+|^2)
\ge\tfrac h2|D_p|^2.
\tag{8}
\]
Use \(|z+w|^2\ge\tfrac12|z|^2-|w|^2\), sum (8) over the disjoint neighborhoods, and apply (6):
\[
\begin{aligned}
c^*S^R_X(t)c
&\ge \tfrac h2\sum_{p\in G(H)}|D_p|^2\\
&\ge \tfrac h2\left[
\tfrac12\sum_{p\in G(H)}|c_{a(p)}|^2(\log p)^2
-h^2\#G(H)\|c\|_2^2\right]\\
&\ge \tfrac h2\left[
\frac{X\log X}{32}-\frac{h^2X}{\log X}\right]\|c\|_2^2\\
&\ge \frac{X\log X}{512}\,\|c\|_2^2
\qquad(h=1/4,\ X\text{ sufficiently large}).
\end{aligned}\tag{9}
\]
The last line uses \(X\) sufficiently large that \(h^2/\log X\le(\log X)/64\). This proves (1), and integrating its Loewner inequality proves (2).

## Prior art, falsification, and limits

The arithmetic input is solely the fixed-modulus prime number theorem and **upper-bound** Selberg sieve, not a prime-pair asymptotic. The latter is already recorded as source 115 of SOURCES.md: J. D. Lichtman and J. Teräväinen, “On the Hardy--Littlewood--Chowla conjecture on average,” *Forum of Mathematics, Sigma* **10** (2022), e57, Lemmas 2.3--2.4. The local jump/Jensen estimate is elementary analysis. No new prime-distribution theorem or independent novelty of these classical ingredients is claimed. The line-specific mathematical delta from PL-455 is the explicit uniform absolute scale \(X\log X\) for a **single vertical frequency**, not just nonvanishing rank.

The proof requires many separated, unpaired **atomic** endpoints in each channel and a centering profile with an \(O(1)\) frequency-uniform Lipschitz constant. Matched generalized atomic sources with those properties satisfy the same mechanism; diffuse sources need not. The exclusion of **both** \(p+\lfloor H\rfloor\) and \(p+\lfloor H\rfloor+1\) is needed for a fixed-width neighborhood for arbitrary real \(H\).

At polynomial \(H\), the bound may lie a factor \(H\) below diagonal shot noise \(XH\log X\). It does **not** prove a normalized \(1/4\) frame, the PL-418/PL-435 source-subtracted signed cone, any arithmetic cancellation, a continuation/zero-divisor bridge, or RH. Absolute quantitative rank stability is weaker than a scale-invariant lower Riesz/frame inequality.
