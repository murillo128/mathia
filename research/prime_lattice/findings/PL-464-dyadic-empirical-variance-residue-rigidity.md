# PL-464 — Dyadic empirical variance still forces a zero-free half-plane through residue rigidity

**Evidence/status:** EXACT-DERIVED + CLASSICAL DYADIC MELLIN FACTORIZATION / CONDITIONAL ZERO-FREE OBSTRUCTION.

**Parent finding:** PL-463 (empirical variance at every large real scale).

## Claim and changed scale hypothesis

Fix \(0<\theta<1\) and a finite \(A\ge0\). For integers \(j\), set
\[
X_j=2^j,\qquad H_j=\lfloor X_j^\theta\rfloor,\qquad
P_j(y)=\sum_{\substack{y<n\le y+H_j\\n\equiv1\ (5)}}\Lambda(n),
\qquad \overline P_j=X_j^{-1}\int_{X_j}^{2X_j}P_j(y)\,dy.
\]
Suppose the **unproved** bound
\[
V_j:=\int_{X_j}^{2X_j}|P_j(y)-\overline P_j|^2\,dy
\ll_{\theta,A}X_jH_j(\log(2X_j))^A
\tag{1}
\]
holds for every sufficiently large integer \(j\), with no assumption at other values of the scale parameter. Then every Dirichlet \(L(s,\chi)\) modulo 5 is zero-free in
\[
\boxed{\Re s>\sigma_\theta,\qquad
\sigma_\theta:=\max\{1-\theta/2,\theta\}.}
\tag{2}
\]
In particular, for \(0<\theta\le2/3\), dyadic scales alone give the same half-plane \(\Re s>1-\theta/2\) as PL-463's all-large-real-scale hypothesis. At \(\theta=1/2\) this is \(\Re s>3/4\). The best half-plane supplied by (2) over this family is \(\Re s>2/3\), at \(\theta=2/3\); this theorem does **not** yield GRH by taking \(\theta\uparrow1\).

The empirical means remain arbitrary and unestimated. The integration over the full base-point interval \([X_j,2X_j]\) remains part of (1): this is sparse sampling of the **scale parameter**, not pointwise sampling of prime windows. Any other constant center at each scale also suffices because the empirical mean minimizes the integral.

The new mechanism is that the unconstrained dyadic block masses generate a vertically periodic meromorphic function. A surviving zero would force two logarithmic-derivative poles whose residue ratio is nonreal. The actual identity-residue logarithmic derivative cannot have that ratio. No zero-density theorem, rightmost-zero hypothesis, or zero simplicity assumption is used. Neither (1) nor a new unconditional zero-free region is proved here.

## 1. The variance controls the shape inside each dyadic block

Write \(a_n=\Lambda(n)\mathbf1_{n\equiv1\ (5)}\), and temporarily abbreviate \(X=X_j\), \(H=H_j\). For \(s\in\mathbb C\), define the entire function
\[
I(s)=\int_1^2u^{-s}\,du
=\frac{2^{1-s}-1}{1-s},\qquad I(1)=\log2,
\]
and the mean-zero test on \([1,2]\)
\[
f_s(u)=u^{-s}-I(s),\qquad \int_1^2f_s(u)\,du=0.
\tag{3}
\]
For every compact \(K\subset\mathbb C\), both \(f_s\) and its first \(u\)-derivative are bounded uniformly for \(s\in K\), \(1\le u\le2\). Mean cancellation and Cauchy--Schwarz give
\[
\begin{aligned}
B_j(s)&:=\frac1H\int_X^{2X}f_s(y/X)P_j(y)\,dy\\
&=\frac1H\int_X^{2X}f_s(y/X)(P_j(y)-\overline P_j)\,dy,\\
|B_j(s)|&\ll_K\frac{\sqrt X}{H}\sqrt{V_j}
\ll_{K,\theta,A}\frac X{\sqrt H}(\log(2X))^{A/2}.
\end{aligned}
\tag{4}
\]
The test may be complex; the scalar Cauchy--Schwarz inequality applies to its modulus without any new hypothesis.

Here it is useful to keep the **sharp dyadic block**, rather than use a compactly supported interior test. Swapping the finite sum and integral gives
\[
B_j(s)=\sum_{X<n\le2X+H}a_n\frac1H
\int_{[X,2X]\cap[n-H,n)}f_s(y/X)\,dy.
\tag{5}
\]
For \(X+H<n\le2X\), the averaged weight differs from \(f_s(n/X)\) by \(O_K(H/X)\). The elementary bound \(0\le a_n\le\log(3X)\) makes the sum of these errors \(O_K(H\log(3X))\). The lower and upper endpoint layers have at most \(2H+O(1)\) integers and bounded weights, and have the same error bound. Thus
\[
E_j(s):=\sum_{X_j<n\le2X_j}a_nf_s(n/X_j)
=B_j(s)+O_K(H_j\log(3X_j)).
\tag{6}
\]
Each \(E_j\) is entire. With \(B=\max\{A/2,1\}\), (4)--(6) imply the locally uniform estimate
\[
\sup_{s\in K}|E_j(s)|
\ll_{K,\theta,A}2^{j\sigma_\theta}(j+1)^B.
\tag{7}
\]
This is the precise endpoint cost. For \(\theta\le2/3\), \(H_j\log X_j\) is no larger in power than \(X_j/\sqrt{H_j}\); for larger \(\theta\) it determines (2). No claim is made that this loss is optimal. PL-463's finite inverse of an interior box average does not directly remove the jump of this sharp-block test at its endpoints.

## 2. The unknown block masses form a periodic meromorphic factor

Choose an integer \(J\ge1\) after which (1) holds, and put
\[
M_j=\sum_{2^j<n\le2^{j+1}}a_n,\qquad
F(s)=\sum_{j\ge J}M_j2^{-js},\qquad
G(s)=\sum_{j\ge J}2^{-js}E_j(s).
\tag{8}
\]
The bound \(M_j\ll2^j(j+1)\) makes \(F\) absolutely convergent for \(\Re s>1\). Bound (7) makes \(G\) holomorphic for \(\Re s>\sigma_\theta\), by normal convergence on every compact subset. The finitely many omitted coefficients give an entire Dirichlet polynomial \(Q(s)=\sum_{n\le2^J}a_nn^{-s}\).

The intervals \((2^j,2^{j+1}]\) partition all integers greater than \(2^J\), so (3), (6) and (8) give the exact identity
\[
D_1(s):=\sum_{n\ge1}\frac{a_n}{n^s}
=Q(s)+I(s)F(s)+G(s)\qquad(\Re s>1).
\tag{9}
\]
Character orthogonality also gives
\[
D_1(s)=\frac14\sum_{\chi\bmod5}-\frac{L'}{L}(s,\chi).
\tag{10}
\]
Consequently \(D_1\) has its classical meromorphic continuation. The quotient
\[
\widetilde F(s)=\frac{D_1(s)-Q(s)-G(s)}{I(s)}
\tag{11}
\]
is meromorphic on \(\Re s>\sigma_\theta\), including the isolated zeros of \(I\) as possible poles, and agrees with \(F\) on \(\Re s>1\).

Let \(\tau=2\pi/\log2\). The series (8) is exactly periodic:
\[
F(s+i\tau)=F(s)\qquad(\Re s>1).
\]
The identity theorem for meromorphic functions extends this equality to
\[
\boxed{\widetilde F(s+i\tau)=\widetilde F(s)
\quad\text{on }\Re s>\sigma_\theta.}
\tag{12}
\]
In particular, simple poles of \(\widetilde F\) have equal residues at vertically translated points. Neither \(G\) nor \(D_1\) was assumed periodic; (12) concerns only the continued block-mass factor.

## 3. Real arithmetic residues rule out every surviving pole

Suppose some mod-5 character has a zero \(\rho=\beta+i\gamma\) with \(\sigma_\theta<\beta<1\). At that point (10) has a simple pole with residue
\[
r_\rho=-\frac14\sum_{\chi\bmod5}m_\chi(\rho)<0,
\tag{13}
\]
where \(m_\chi\) is the zero multiplicity, taken as zero when that factor is nonzero. The identity residue is essential: all character coefficients in (10) equal \(1/4\), so common zeros cannot cancel. Every pole of \(D_1\) in this open strip has a nonzero **real** residue.

The zeros of \(I(s)\) are \(1+ik\tau\), \(k\in\mathbb Z\setminus\{0\}\), and hence \(I\) is nonzero at \(\rho\) and \(\rho+i\tau\). Equations (11)--(12) force a pole of \(D_1\) at \(\rho+i\tau\) with residue
\[
\begin{aligned}
r_{\rho+i\tau}
&=r_\rho\frac{I(\rho+i\tau)}{I(\rho)}\\
&=r_\rho\frac{1-\rho}{1-\rho-i\tau}.
\end{aligned}
\tag{14}
\]
But, writing \(a=1-\beta>0\),
\[
\Im\frac{1-\rho}{1-\rho-i\tau}
=\frac{a\tau}{a^2+(\gamma+\tau)^2}>0.
\tag{15}
\]
Thus (14) is nonreal, contradicting (13) at the translated pole. This excludes every zero in the open strip in question, including any real zero. The usual Euler-product nonvanishing for \(\Re s>1\) and classical nonvanishing on \(\Re s=1\) complete (2). The extra zeros of \(L(s,\chi_0)=(1-5^{-s})\zeta(s)\) lie on \(\Re s=0\) and do not enter the argument.

The principal pole at \(s=1\) is consistent with (12): its translates occur at zeros of \(I\), so the multiplier can cancel them. This is why the strict \(\beta<1\) check is load-bearing. No attained horizontal frontier or control of infinite zero sums is needed; a single alleged pole and one of its translates suffice.

## 4. A positive source can hide a dyadic bias without arithmetic residue rigidity

The following control is neither rational primes nor a Beurling prime system. Fix \(3/4<\beta<1\) and \(0<c<1/4\). On each interval \([2^j,2^{j+1})\), \(j\ge0\), define a positive density
\[
d\mu(x)=c_j\,dx,\qquad c_j=\frac14-c\,2^{j(\beta-1)}.
\tag{16}
\]
Take \(X=2^j\), \(H=\lfloor\sqrt X\rfloor\). Its window mass equals \(Hc_j\) until \(y>2X-H\); on the last \(H\) units of the block it differs by
\((c_{j+1}-c_j)(y+H-2X)\). Therefore its empirical variance obeys
\[
V_j^\mu\le\int_X^{2X}|\mu((y,y+H])-Hc_j|^2\,dy
=\frac{H^3}{3}(c_{j+1}-c_j)^2
\ll H^3X^{2\beta-2}=o(XH).
\tag{17}
\]
Nevertheless its Mellin transform is
\[
\int_1^\infty x^{-s}\,d\mu(x)
=\frac1{4(s-1)}-\frac{cI(s)}{1-2^{\beta-s}}
\qquad(\Re s>1),
\tag{18}
\]
with a pole at \(s=\beta>3/4\). The poles at \(\beta+ik\tau\) have residues \(-cI(\beta+ik\tau)/\log2\), which have exactly the nonreal phase ratios in (14). Thus the arithmetic contradiction is absent. Positivity, the leading density \(1/4\), and small empirically centered variance at all dyadic scales do not alone exclude such a pole. The real logarithmic-derivative residues supply the information distinguishing (10) from this control.

## Prior art, audit boundary and consequence

Variance-to-zero implications are classical; Zaccagnini (2016), Section 3.3, is the existing source 123 and uses a different, deterministically centered multiplicative Selberg integral. The Dirichlet logarithmic derivative and character orthogonality in (10) are standard (source 120). Geometric dilation producing vertical Mellin pole families and logarithmic oscillations is standard Mellin analysis: Flajolet--Gourdon--Dumas, *Mellin transforms and asymptotics: Harmonic sums* (1995), especially the discussion of regularly spaced poles, is source 124. No novelty is claimed for these tools.

Targeted comparison with those literatures and the local sparse-sampling findings did not locate this precise empirically centered, single-residue dyadic implication. This is not a claim of external novelty. PL-158's fixed-step Suzuki aliasing control concerns point samples of a different zero-screw observable; it does not supply the full within-block shape information (4)--(7). The durable mathematical delta here is the weaker scale hypothesis, the explicit endpoint tariff, and the residue-phase argument (11)--(15) that removes the otherwise possible dyadic bias.

The proof is exact conditional mathematics, not numerical evidence or a formalized Lean theorem. Its direct audit points are the two endpoint layers in (6), locally uniform convergence of \(G\), continuation of periodicity for \(\widetilde F\), and the imaginary-part sign in (15). The control (16)--(18) tests the arithmetic hypothesis rather than pretending that an arbitrary positive source has a Dirichlet zero divisor.

The estimate must hold at **every sufficiently large dyadic scale**; an arbitrary subsequence is not covered. The full base-point variance, fixed \(\theta\), finite log power, and identity residue remain essential to this proof. The \(\theta\) endpoint term is a limitation of the present estimate, not an optimality theorem. No assertion is made about zeros on the boundary \(\Re s=\sigma_\theta\), the truth of (1), the mod-5 relative lower-frame cone, or signed covariance cancellation. The result closes a specific sparse-scale escape from the absolute upper-moment prerequisite while leaving the direct relative lower-frame problem open.
