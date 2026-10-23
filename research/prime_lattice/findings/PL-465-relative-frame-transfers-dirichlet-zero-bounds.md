# PL-465 — A relative mod-5 frame transfers zero bounds between Dirichlet channels

**Evidence/status:** EXACT-DERIVED + CLASSICAL EXPLICIT-FORMULA / SELBERG INPUTS; CONDITIONAL ARITHMETIC-STRENGTH BOUNDARY.

**Parent findings:** PL-421 (image-cone floor), PL-436 (relative frame target), PL-458 (centered prime source), PL-463 (empirical variance and Mellin poles).

## Claim and scale quantifiers

Fix \(0<\theta<1\), put \(H=\lfloor X^\theta\rfloor\), and use the actual prime-power windows
\[
P_a(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n),
\qquad a\in U_5=\{1,2,3,4\},\quad X\le y\le2X.
\]
Choose either of the following centers, consistently for the whole vector:
\[
R_a=P_a-H/4,
\qquad\text{or}\qquad
R_a=P_a-\overline P_a,\quad
\overline P_a=X^{-1}\int_X^{2X}P_a(y)\,dy.
\tag{1}
\]
Let \(S_X=\int_X^{2X}R(y)R(y)^Tdy\) and \(D_X=\operatorname{Diag}S_X\). Assume the **unproved** relative frame hypothesis
\[
S_X\succeq c_\theta D_X
\quad\text{for every sufficiently large real }X,
\qquad c_\theta>0\text{ independent of }X.
\tag{F_\theta}
\]
The PL-421 local-factor gate is the special case \(c_\theta=1/4\). No inverse of a possibly singular \(D_X\) is required here.

For each character \(\chi\bmod5\), define
\[
\Theta_\chi=\sup\{\Re\rho: L(\rho,\chi)=0,\ 0<\Re\rho<1\},
\qquad
\Theta_{\min}=\min_\chi\Theta_\chi,\quad
\Theta_{\max}=\max_\chi\Theta_\chi.
\]
For the principal character, \(\Theta_{\chi_0}=\Theta_\zeta\): the additional Euler-factor zeros of \((1-5^{-s})\zeta(s)\) have real part zero. The functional equations give \(1/2\le\Theta_\chi\le1\).

The frame assumption implies
\[
\boxed{\Theta_{\max}-\Theta_{\min}\le1-\theta.}
\tag{2}
\]
Consequently, if \((F_{\theta_j})\) holds for a sequence of fixed exponents \(\theta_j\uparrow1\), then
\[
\boxed{\Theta_\chi\text{ is the same for all four characters modulo }5.}
\tag{3}
\]
The constants and large-scale thresholds may depend on \(j\); no uniformity as \(\theta_j\to1\) is assumed. Under this frame family, RH for **any one** of the four factors implies joint GRH modulo 5. Equality (3) concerns suprema, not equality of zero sets, multiplicities, or attained rightmost zeros. A common supremum larger than \(1/2\) is not excluded by (3).

There is a stronger fixed-exponent conclusion if RH for zeta is separately assumed:
\[
\boxed{\mathrm{RH}_\zeta+(F_\theta)
\ \Longrightarrow\quad
L(s,\chi)\ne0\quad(\Re s>1-\theta/2,\ \chi\bmod5).}
\tag{4}
\]
At \(\theta=1/2\), (4) excludes zeros only to the right of \(3/4\), not to the right of \(1/2\).

This is a consequence **of a hypothetical frame**, not a proof of the frame or of a zero-free region. The family in (3) reaches window exponents near one and is stronger in scale coverage than PL-458's fixed \(1/6<\theta<1/2\) regime. In that latter regime (2) alone is vacuous; (4) remains conditional on zeta RH. No converse from GRH to the frame is asserted.

## 1. Flat character probes turn the relative floor into energy domination

For a character \(\chi\), put
\[
Q_\chi(y)=\sum_{a\in U_5}\chi(a)R_a(y),
\qquad E_\chi(X,H)=\int_X^{2X}|Q_\chi(y)|^2dy.
\]
Each character has modulus one on \(U_5\). Applying \((F_\theta)\) to \(z_a=\overline{\chi(a)}\) gives
\[
\boxed{E_\chi\ge c_\theta\operatorname{tr}S_X.}
\tag{5}
\]
In particular, for the identity residue's empirical variance,
\[
V_1:=\min_{b\in\mathbb R}\int_X^{2X}|P_1(y)-b|^2dy
\le(S_X)_{11}\le\operatorname{tr}S_X
\le c_\theta^{-1}E_\chi.
\tag{6}
\]
The minimum makes this valid for both choices in (1). No mean estimate is needed. The principal probe is just \(\chi_0(a)=1\), so even the common-mode direction of the frame already carries a useful necessary condition.

Equation (5) supplies a **relative upper bound** once an independent upper estimate for one character energy is available. It does not supply an absolute upper bound on its own: multiplying any admissible covariance by an arbitrary positive scalar preserves the frame. Also, (5) is only a necessary consequence of the full frame and is not a replacement positivity criterion.

## 2. A scalar growth bound detects all mod-5 zero poles

We record the exponent version of PL-463's argument. Suppose, at every sufficiently large real scale,
\[
V_1(X,\lfloor X^\theta\rfloor)
\ll X^{1+2b}(\log(2X))^B,
\qquad 0\le b<\theta,\quad B\ge0\text{ fixed}.
\tag{7}
\]
Then all four factors are zero-free in \(\Re s>\alpha\), where
\[
\alpha=1+b-\theta.
\tag{8}
\]

Here is the finite-window detail, including the large-\(\theta\) boundary. For a real \(w\in C_c^\infty((1,2))\) with \(\int w=0\), set \(\tau=H/X\). Choose a fixed integer \(N\) such that
\[
N(1-\theta)>\theta-b.
\]
Let \(c_0=1\), \(c_j=-\sum_{k=1}^j(-1)^kc_{j-k}/(k+1)!\), and
\[
f_\tau=\sum_{j=0}^{N-1}c_j\tau^jw^{(j)},
\qquad
(B_\tau f)(u)=\tau^{-1}\int_0^\tau f(u-v)\,dv.
\]
Finite Taylor expansion gives \(B_\tau f_\tau=w+O_{w,N}(\tau^N)\), uniformly on the real line after zero extension. Also \(\int f_\tau=0\) and \(\|f_\tau\|_2=O_{w,N}(1)\). Thus exact interchange of the finite window sum and integral, followed by Cauchy--Schwarz, yields
\[
\begin{aligned}
\sum_{n\equiv1(5)}\Lambda(n)w(n/X)
&=H^{-1}\int_X^{2X}f_\tau(y/X)P_1(y)\,dy
 +O_{w,N}(X\tau^N\log(3X))\\
&\ll_{w,\theta,b,B}X^{1+b-\theta}(\log(2X))^{B/2}.
\end{aligned}
\tag{9}
\]
The compact interior support removes boundary layers; the unknown mean cancels exactly. The choice of \(N\) makes the error strictly smaller in power than the displayed bound. This is finite Taylor inversion, not an infinite inverse multiplier assumption.

With \(W(s)=\int_1^2w(u)u^{s-1}du\), the Mellin transform of the left side of (9), in the scale variable \(X\), is holomorphic for \(\Re s>\alpha\). In \(\Re s>1\) it equals
\[
W(s)D_1(s),\qquad
D_1(s)=\sum_{n\equiv1(5)}\Lambda(n)n^{-s}
=\frac14\sum_{\chi\bmod5}-\frac{L'}L(s,\chi).
\tag{10}
\]
The finite-scale part is entire. At a zero \(\rho\) in the open critical strip, the residue of \(D_1\) is
\[
-\frac14\sum_\chi m_\chi(\rho)<0,
\]
so common zeros cannot cancel. For any \(\rho\ne1\), a real mean-zero test with \(W(\rho)\ne0\) exists: take \(w=\varphi'\) for a positive smooth bump supported sufficiently near one point of \((1,2)\). Then
\[
W(\rho)=-(\rho-1)\int_1^2\varphi(u)u^{\rho-2}du\ne0.
\]
Uniqueness of meromorphic continuation contradicts holomorphy if \(\Re\rho>\alpha\). The principal pole is killed by \(W(1)=0\), and classical nonvanishing on and to the right of \(\Re s=1\) completes the assertion. There is no rightmost-zero or simplicity assumption.

## 3. Transfer a single character's horizontal zero bound

Let \(\Psi_\chi(x)=\sum_{n\le x}\Lambda(n)\chi(n)\), and let \(\delta_\chi=1\) for the principal character and zero otherwise. The classical truncated explicit formula and zero counting give, for every fixed \(b>\Theta_\chi\),
\[
\Psi_\chi(x)-\delta_\chi x=O_{\chi,b}(x^b).
\tag{11}
\]
For clarity, when \(\Theta_\chi<1\), truncate at height comparable with \(x\). The sum of \(1/|\rho|\) up to that height is \(O_\chi((\log x)^2)\); the finitely many low zeros only alter the constant. Each zero term is bounded by \(x^{\Theta_\chi}/|\rho|\), and the truncation and endpoint errors are logarithmic. Absorb logarithms using \(b>\Theta_\chi\). The principal character differs from zeta by the powers of 5, whose cumulative weight is \(O(\log x)\). If \(\Theta_\chi=1\), the conclusions below for that character are already trivial.

For deterministic centering,
\[
Q_\chi(y)=\Psi_\chi(y+H)-\Psi_\chi(y)-\delta_\chi H.
\tag{12}
\]
For empirical centering, it is this same function minus its mean on \([X,2X]\), an orthogonal projection which cannot increase its \(L^2\) norm. Consequently (11) gives
\[
E_\chi(X,H)\ll_{\chi,b}X^{1+2b}.
\tag{13}
\]
Combining (6), (13), and the scalar lemma proves
\[
\Theta_{\max}\le1+b-\theta\qquad
(\Theta_\chi<b<\theta).
\]
Let \(b\downarrow\Theta_\chi\). If \(\Theta_\chi\ge\theta\), the same upper bound \(\Theta_{\max}\le1+\Theta_\chi-\theta\) is automatic from \(\Theta_{\max}\le1\). Minimize over the four characters to prove (2), then let the fixed exponents tend to one to prove (3). This limit needs no interchange with a zero sum and no uniform frame constant across exponents.

## 4. The sharper fixed-exponent consequence under zeta RH

Selberg's classical RH bound, in the additive-window normalization, is
\[
J(X,H):=\int_X^{2X}|\psi(y+H)-\psi(y)-H|^2dy
\ll XH\bigl(\log(2X/H)\bigr)^2,
\qquad 1\le H\le X.
\tag{14}
\]
Languasco--Perelli--Zaccagnini state this bound explicitly in their introduction immediately before (1.12), attributing it to Selberg and Saffari--Vaughan; only RH is needed, not a pair-correlation conjecture (source 125).

For the principal mod-5 channel, (12) differs from the integrand in (14) by the window weight of powers of 5. For large \(X\), \(H=o(X)\); at most one such power lies in \([X,2X+H]\), and it affects a set of origins of measure at most \(H\). Its squared norm is therefore \(O(H)\). Hence
\[
E_{\chi_0}(X,H)\ll XH(\log(2X))^2
\]
for deterministic centering, and also for empirical centering by contraction. Equations (6)--(8), with \(b=\theta/2\) and \(B=2\), prove (4).

## Controls, prior art and consequence

The information transfer uses the actual character logarithmic derivatives, not just four positive covariance channels. A generic PSD matrix has no attached \(L\)-function zeros; a Helson twist or a generalized-prime source cannot inherit (10)--(14) without its own analytic input. Homogeneous rescaling confirms that the relative cone alone supplies no absolute variance scale. The four flat probes used in (5) also do not establish the full oriented cone from their scalar energies; PL-428 and PL-436's information-loss boundaries remain intact.

Classical explicit formulas and zero counting support (11): see Montgomery--Vaughan (source 120), and Kedlaya's accessible Chapters 8 and 11 (source 127). The variance/Mellin-pole method is classical and was adapted to this identity residue in PL-463. The Selberg input (14) is source 125. None of these tools is claimed as new.

There is also direct prior art for transferring one \(L\)-function's information to others: Banks, *The Generalized Riemann Hypothesis from zeros of a single L-function* (2023), Theorem 1.1, obtains full GRH from a strengthened single-factor hypothesis involving rationally twisted zero sums (source 126). That condition already contains RH for the selected factor and is different from the fixed-mod-5 relative frame here. It is not a proof that ordinary RH alone implies GRH, nor is its extra hypothesis supplied by this finding.

Targeted checks of short-interval covariance, Selberg variance converses, and single-factor GRH transfer did not identify the precise implication (2)--(4) from this local-factor frame. This is not an external novelty claim. The durable delta is a conditional restriction on the surviving **relative** frame route, after PL-459--PL-464 analyzed absolute moment hypotheses: a uniform relative floor can transfer independent upper information from one channel into zero control for all four. The frame is therefore not insulated from joint zero-location content merely because it avoids an entrywise covariance asymptotic.

Every conclusion retains its stated center, full base-point integral, \(t=0\), and all-large-real-scale hypothesis. No claim is made for isolated scales, a vertical-frequency average, arbitrary source-dependent centers, zeros on the displayed boundary, or the truth of the frame for actual primes. The near-one exponent family is an additional hypothesis, not a consequence of a frame at \(\theta\le1/2\). The proof is exact conditional mathematics, not numerical evidence or a Lean formalization. Its main audit points are the unit-modulus character test (5), finite box inversion (9), noncancelling identity-residue poles (10), and the distinction between a fixed exponent and a family approaching one.
