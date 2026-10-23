# PL-467 — A relative covariance frame admits sparse common off-critical poles

**Evidence/status:** EXACT-DERIVED + CLASSICAL FOURIER/HURWITZ TOOLS; SOURCE-REALIZABLE NEGATIVE CONTROL; NO EXTERNAL NOVELTY CLAIM.

**Local dependencies:** PL-421 (the `1/4` image-cone floor), PL-465 (relative-frame transfer between character zero bounds), PL-466 (absolute variance and sparse poles).

## Claim and the precise control class

For every fixed \(1/2<\beta<1\), there is a **single**, bounded, nonnegative sequence \(b_n\), supported on integers coprime to 5, with the following properties. Set
\[
P_a(y;H)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}b_n,
\qquad a\in U_5.
\]
For every fixed \(1-\beta<\theta<1\), with \(H=\lfloor X^\theta\rfloor\), and every sufficiently large **real** \(X\), either center
\[
R_a=P_a-H/4,\qquad\text{or}\qquad
R_a=P_a-X^{-1}\int_X^{2X}P_a(y;H)\,dy
\]
gives
\[
S_X=\int_X^{2X}R(y)R(y)^Tdy
\succeq\frac14\operatorname{Diag}S_X,
\qquad
\lambda_{\min}(S_X)\asymp\lambda_{\max}(S_X)
\asymp H^2X^{2\beta-1}.
\tag{1}
\]
The constants and starting scales may depend on \(\beta,\theta\). The source itself does not depend on either \(X\) or \(\theta\).

Nevertheless the four character transforms
\[
\mathcal D_\chi(s)=\sum_n b_n\chi(n)n^{-s}
\]
extend meromorphically to the plane and each has poles on \(\Re s=\beta\), with residue \(-1\). Apart from the principal pole at 1, their entire combined pole set is finite. It respects conjugation between conjugate characters and reflection \(\rho\mapsto1-\overline\rho\) within each character. For the identity residue,
\[
\mathcal D_1^{\rm res}(s):=\sum_{n\equiv1(5)}b_nn^{-s}
=\frac14\sum_\chi\mathcal D_\chi(s),
\tag{2}
\]
every off-critical pole has residue \(-1/4\); cancellation cannot hide one.

Thus the relative frame, integer/residue support, positivity, correct leading density, sublinear off-critical pole count, and these divisor symmetries/residue signs **together do not exclude a common off-critical frontier in this broader source class**. This realizes the common-supremum escape left by PL-465, beyond the simple observation that a covariance can be rescaled.

These coefficients are not von Mangoldt coefficients. The construction supplies neither rational-prime support, prime-pair laws, an Euler product, nor a completed Dirichlet functional equation. It is not a counterexample to RH/GRH or to a theorem using those additional arithmetic inputs.

## 1. One positive source with twelve prescribed poles

Order residues as \((1,2,4,3)\), and choose \(\chi(2)=i\). Write \(\eta=\chi^2\), and fix any \(M\ge1000\). Define the pole sets
\[
\begin{aligned}
Z_{\chi_0}&=\{\beta\pm iM,\ 1-\beta\pm iM\},\\
Z_\eta&=\{\beta\pm2iM,\ 1-\beta\pm2iM\},\\
Z_\chi&=\{\beta+3iM,\ 1-\beta+3iM\},\\
Z_{\bar\chi}&=\overline{Z_\chi}.
\end{aligned}
\tag{3}
\]
For \(x\) sufficiently large put
\[
g_a(x)=\frac14-\frac14\sum_\xi\overline{\xi(a)}
                      \sum_{\rho\in Z_\xi}x^{\rho-1}
=\frac14+(x^{\beta-1}+x^{-\beta})f_a(\log x),
\tag{4}
\]
where the real vector \(f\) is
\[
f_a(t)=-\frac12\left[
\cos Mt+\eta(a)\cos2Mt+
\Re\bigl(\overline{\chi(a)}e^{3iMt}\bigr)\right].
\tag{5}
\]
Since \(|f_a|\le3/2\), choose an integer \(n_0\) so large that
\((3/2)(x^{\beta-1}+x^{-\beta})\le1/8\) for all \(x\ge n_0\).
Set
\[
b_n=\begin{cases}
0,&5\mid n,\\
5/4,&5\nmid n,\ n<n_0,\\
5g_a(n),&n\equiv a\ (5),\ n\ge n_0.
\end{cases}
\tag{6}
\]
In particular \(5/8\le b_n\le15/8\) on the tail support. The sequence is fixed, positive there, and bounded.

Let
\[
A_a(s)=\sum_{n\equiv a(5)}n^{-s}=5^{-s}\zeta(s,a/5).
\]
The classical Hurwitz continuation has its sole pole at 1, with residue \(1/5\) after this normalization (source 130). Finite initial changes contribute an entire Dirichlet polynomial \(E_a\), so
\[
\mathcal D_a^{\rm res}(s)=\frac54 A_a(s)
-\frac54\sum_\xi\overline{\xi(a)}\sum_{\rho\in Z_\xi}
 A_a(s+1-\rho)+E_a(s).
\tag{7}
\]
At \(\rho\in Z_\xi\) its residue is \(-\overline{\xi(a)}/4\).
Character orthogonality now gives exactly
\[
\operatorname{Res}_{s=\rho}\mathcal D_\kappa(s)
=-\mathbf1_{\kappa=\xi},\qquad
\operatorname{Res}_{s=1}\mathcal D_\kappa(s)
=\mathbf1_{\kappa=\chi_0}.
\tag{8}
\]
There are no other poles. Equation (2) and its noncancellation follow; in the open critical strip every character has the same rightmost pole abscissa \(\beta\). The principal pole at 1 is separate.

Even the abstract logarithmic-derivative representation can be supplied. The difference
\[
E_\kappa^*(s)=\mathcal D_\kappa(s)
-\frac{\mathbf1_{\kappa=\chi_0}}{s-1}
+\sum_{\rho\in Z_\kappa}\frac1{s-\rho}
\]
is entire. If \(B_\kappa'=E_\kappa^*\), then
\[
\mathcal L_\kappa(s)=e^{-B_\kappa(s)}
\frac{\prod_{\rho\in Z_\kappa}(s-\rho)}
     {(s-1)^{\mathbf1_{\kappa=\chi_0}}}
\quad\text{satisfies}\quad
-\mathcal L_\kappa'/\mathcal L_\kappa=\mathcal D_\kappa.
\tag{9}
\]
These artificial meromorphic functions have the stated finite zero divisors. No finite-order bound, Euler product or functional equation for them is asserted; the reflection symmetry of a divisor is a strictly weaker property.

## 2. The atomic windows approach a finite oscillatory Gram matrix

Summation on a progression of spacing 5, or elementary Euler summation, gives uniformly for \(X\le y\le2X\), \(1\le H=o(X)\),
\[
P_a(y;H)=\int_y^{y+H}g_a(x)\,dx+O_{\beta,M}(1).
\tag{10}
\]
Indeed the endpoint error is bounded by \(\sup|g_a|\) and the integral error by \(\int_y^{y+H}|g_a'|\); from (4) this derivative is \(O_{\beta,M}(X^{\beta-2}+X^{-\beta-1})\).
This also yields \(\sum_{n\le x,n\equiv a(5)}b_n=x/4+O_{\beta,M}(x^\beta)\) and the correct leading window density.

With \(y=Xu\), subtracting \(H/4\) gives
\[
\frac{P_a(Xu;H)-H/4}{HX^{\beta-1}}
=u^{\beta-1}f_a(\log X+\log u)+O_{\beta,M}(\epsilon_X),
\tag{11}
\]
uniformly on \([1,2]\), where
\[
\epsilon_X=H/X+X^{1-2\beta}+X^{1-\beta}/H=o(1)
\quad(1-\beta<\theta<1).
\tag{12}
\]
The three errors are respectively the finite window derivative error, the reflected pole modes, and integer discretization. For empirical centering, subtract the integral of both sides over \([1,2]\); the uniform error remains \(o(1)\). No estimate of the empirical mean is assumed.

## 3. A uniform spectral margin, including empirical centering

Use the real orthonormal residue basis
\[
e_0=\tfrac12(1,1,1,1),\quad
e_2=\tfrac12(1,-1,1,-1),\quad
e_c=\tfrac1{\sqrt2}(1,0,-1,0),\quad
e_s=\tfrac1{\sqrt2}(0,1,0,-1).
\]
In that basis the vector on the right of (11), up to a common minus sign, has coordinates
\[
u^{\beta-1}\left(
\cos(M\log u+\phi_0),\ \cos(2M\log u+\phi_2),\
2^{-1/2}\cos(3M\log u+\phi_1),\
2^{-1/2}\sin(3M\log u+\phi_1)\right),
\tag{13}
\]
where \(\phi_r\) are the phases induced by \(X\). The following bounds hold even for arbitrary phases.

Put \(I_\beta=\int_1^2u^{2\beta-2}du\), so \(\log2<I_\beta<1\). For \(t\ne0\),
\[
\left|\int_1^2u^{2\beta-2+it}du\right|
=\left|\frac{2^{2\beta-1+it}-1}{2\beta-1+it}\right|
\le\frac3{|t|}.
\tag{14}
\]
Every nonconstant product frequency in (13) has modulus at least \(M\). The product-to-sum formulas therefore bound each entry of the uncentered Gram error relative to
\[
K_0=\operatorname{diag}(I_\beta/2,I_\beta/2,I_\beta/4,I_\beta/4)
\]
by \(3/M\), hence its operator norm by \(12/M\).
Also \(|\int_1^2u^{\beta-1+it}du|\le3/|t|\); the four coordinate means have modulus at most \(3/M\). Empirical centering subtracts their outer product, of norm at most \(36/M^2\). Thus both limiting Gram matrices \(K_X\) satisfy
\[
\|K_X-K_0\|_{\rm op}\le12/M+36/M^2<I_\beta/16,
\tag{15}
\]
and consequently
\[
\lambda_{\min}(K_X)\ge3I_\beta/16,
\qquad \lambda_{\max}(K_X)\le9I_\beta/16.
\tag{16}
\]
The phases may vary with \(X\); the margin is uniform, so convergence of those phases is unnecessary.

Equation (11) implies, after the orthogonal change of basis,
\(S_X/(H^2X^{2\beta-1})=K_X+o_{\rm op}(1)\).
For sufficiently large \(X\), take the error norm below \(I_\beta/80\).
Then its smallest eigenvalue is at least \(14I_\beta/80\), and its largest at most \(46I_\beta/80\). Every diagonal entry is at most the largest eigenvalue, so
\[
S_X\succeq\frac7{23}\operatorname{Diag}S_X
\succ\frac14\operatorname{Diag}S_X.
\tag{17}
\]
This proves (1) for either center, at all sufficiently large real scales, without vertical averaging.

## 4. Why absolute variance and arithmetic identification still matter

The empirical variance of every residue is comparable with \(H^2X^{2\beta-1}\). If \(\theta>2(1-\beta)\), then for every fixed finite \(A\),
\[
\frac{\int_X^{2X}|P_1-\overline P_1|^2dy}
     {XH(\log X)^A}
\asymp\frac{X^{\theta+2\beta-2}}{(\log X)^A}\longrightarrow\infty.
\tag{18}
\]
Thus this control passes the relative gate but fails the absolute premise used in PL-466 precisely in a regime where that premise would exclude its poles. Sparse pole count and real residue signs cannot supply the missing variance scale by themselves. The pole count here is even bounded, not merely sublinear.

There is no conflict with PL-465: all four character frontiers equal \(\beta\), and no one channel supplies an independent RH-strength upper bound. There is also no conflict with PL-457: that control has sparse heavy atoms and sieve-order pair upper bounds but fails the relative gate; this one deliberately supplies a relative gate and a meromorphic pole model, and does not supply those sieve properties.

The result closes the proposed generic inference from a relative frame plus sparse symmetric logarithmic-derivative poles to critical-line location. It leaves open whether the **actual prime** frame, combined with an independently proved arithmetic input absent here, has stronger consequences. The full Euler/functional-equation structure cannot be replaced silently by the much weaker divisor symmetries in (3).

## Prior art and audit boundary

Separated-frequency Gram bounds are classical nonharmonic Fourier analysis (Ingham, source 63); (14)--(16) give the elementary finite calculation required here. Hurwitz continuation and progression decomposition are classical (source 130). Ford--Konyagin's finite hypothetical-zero barriers for prime races (source 131, Section 1) are close prior art for controlling real residue observables through specified off-critical modes. Their ordering problem is different from this centered matrix floor, and their work is not cited as constructing the sequence (6).

The derived contribution is the simultaneous positive integer-supported realization, exact character-pole residue selection, and uniform relative-cone admission for a family of window exponents approaching one. It strengthens the control class beyond arbitrary covariance rescaling or an unspecified finite zero model. No new general Fourier theorem, actual-prime construction, or external novelty is claimed.

Auxiliary checks at \(M=1000\) verified all four character residue projections exactly and evaluated the closed-form Gram integrals at \(\beta\in\{0.5001,0.51,0.75,0.99,0.9999\}\) and phases \(M\log X=2\pi j/257\), \(0\le j<257\), for both centers (2,570 matrices). The smallest sampled Gershgorin lower bound for the correlation matrices exceeded 0.6627. These are formula/sign checks only: (14)--(17), not sampling, prove the uniform floor. Scratch calculations are outside Git. No Lean verification is claimed.

The restrictions \(\beta>1/2\), \(\theta>1-\beta\), fixed frequencies, and eventual scale quantifiers are load-bearing: they make the reflected modes and integer errors negligible. No claim is made at either exponent boundary, for arbitrary small windows, for prime-support weights, or for a true Dirichlet Euler product with this zero divisor.
