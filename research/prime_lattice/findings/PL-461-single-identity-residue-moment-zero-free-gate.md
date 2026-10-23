# PL-461 — A single identity-residue raw prime-window moment already forces the full mod-5 zero-free gate

**Evidence/status:** EXACT-DERIVED + CLASSICAL LANDAU-POSITIVITY / CONDITIONAL ZERO-FREE OBSTRUCTION.

**Parent findings:** PL-458 (diagonal pair-to-raw-moment calculation), PL-459 (integrated signed first-moment gate), PL-460 (four-channel raw-moment zero-free gate).

## Precise claim

Let \(0<\theta\le 1/2\) be fixed, \(H=\lfloor X^\theta\rfloor\), and
\[
P_1(y)=\sum_{\substack{y<n\le y+H\\n\equiv1\pmod5}}\Lambda(n),\qquad
Q_{11}(X,H)=\int_X^{2X}P_1(y)^2\,dy.
\]
Suppose **for every sufficiently large real \(X\)** that
\[
\boxed{Q_{11}(X,H)\le \frac{XH^2}{16}+C_\theta XH\log(2X)}
\tag{M_{1,\theta}}
\]
with a constant independent of \(X\). Then **every** Dirichlet \(L(s,\chi)\) modulo 5 is zero-free in
\[
\boxed{\Re s>1-\theta}
\]
apart from the principal factor's known pole at \(s=1\). In particular, this *single uncentered diagonal moment upper bound* at \(\theta=1/2\) implies joint GRH modulo 5, including RH. The same implication follows if \((M_{1,\theta_j})\) holds for each of a sequence of fixed \(\theta_j\uparrow1/2\).

For \(1/6<\theta<1/2\), the **single diagonal \(a=b=1\) instance** of [[research/prime_lattice/findings/PL-458-mod5-singular-series-matrix-second-order-transfer|PL-458]]'s unproved signed second-order pair remainder (B), together with its unconditional prime-number and singular-series calculations, already implies \((M_{1,\theta})\). Therefore just that instance of (B), assumed for all large \(X\), excludes all mod-5 Dirichlet zeros in \(\Re s>1-\theta\). The other three diagonal pair bounds, all off-diagonal pair bounds, and PL-458's first-moment assumption (A) are unnecessary for this zero-free consequence.

These are implications **from unproved estimates**. Neither the moment hypothesis, the pair remainder, GRH, nor RH is established here.

## 1. A single diagonal ceiling implies a one-sided progression error

Set \(\psi_1(x)=\sum_{n\le x,\ n\equiv1(5)}\Lambda(n)\), \(E_1(x)=\psi_1(x)-x/4\), and \(I_1(X,H)=\int_X^{2X}P_1(y)\,dy\). Cauchy–Schwarz and the nonnegativity of \(P_1\) yield
\[
I_1^2\le XQ_{11}
 \le \frac{X^2H^2}{16}+C_\theta X^2H\log(2X),
\quad
I_1\le \frac{XH}{4}+O_\theta(X\log(2X)).
\tag{1}
\]
The second inequality uses \(\sqrt{u^2+v}\le u+v/(2u)\), not an assumption about the signed first moment. Counting the intersection lengths of prime windows with the dyadic interval gives the exact endpoint transfer from [[research/prime_lattice/findings/PL-459-integrated-first-moment-zero-free-gate|PL-459]]:
\[
I_1(X,H)=H\{\psi_1(2X)-\psi_1(X)\}
         +O(H(H+1)\log(3X)).
\tag{2}
\]
Consequently, for \(H=\lfloor X^\theta\rfloor\),
\[
E_1(2X)-E_1(X)
 \le O_\theta((X/H+H+1)\log(3X))
 =O_\theta(X^{1-\theta}\log(3X)),
\tag{3}
\]
because \(\theta\le1/2\). Dyadic telescoping from any sufficiently large fixed base to arbitrary \(x\) yields
\[
\boxed{E_1(x)\le C'_\theta x^{1-\theta}\log(2x)}
\quad(x\ge x_0).
\tag{4}
\]
This bound is genuinely **one-sided**. No lower bound, little-\(o\) estimate, or assertion for any other residue class has been inferred.

## 2. The identity residue sees the full Dedekind zeta zero divisor

Put \(\sigma=1-\theta\ge1/2\). Choose \(C>0\) sufficiently large that
\(f(x)=Cx^\sigma\log x-E_1(x)\ge0\) for \(x\ge x_0>1\).
Its Mellin transform
\[
F(s)=\int_{x_0}^\infty f(x)x^{-s-1}\,dx
\tag{5}
\]
converges for \(\Re s>1\) by the classical fixed-modulus PNT (or a Chebyshev bound), and the Mellin transform of \(Cx^\sigma\log x\) is holomorphic for \(\Re s>\sigma\).

For \(\Re s>1\), character orthogonality at the *identity residue* gives
\[
\sum_{\chi\bmod5}\chi(n)=4\,\mathbf1_{n\equiv1(5)},\qquad
\prod_{\chi\bmod5}L(s,\chi)
 =(1-5^{-s})\zeta_{\mathbb Q(\zeta_5)}(s),
\tag{6}
\]
and hence
\[
\int_1^\infty E_1(x)x^{-s-1}\,dx
=\frac{1}{4s}\sum_{\chi\bmod5}\left(-\frac{L'}{L}(s,\chi)\right)
 -\frac{1}{4(s-1)}.
\tag{7}
\]
Passing from lower limit \(1\) to \(x_0\) adds an entire function. At \(s=1\), the pole of the principal logarithmic derivative cancels the explicit main-term pole. Any zero \(\rho\) of any \(L(s,\chi)\) with \(\Re\rho>\sigma\) instead creates a nonremovable pole in (7): the residues of the logarithmic derivatives at common zeros have the **same sign**, equal to minus their positive multiplicities. No cancellation among different characters is possible. The factor \(1/s\) is nonzero and regular in this half-plane.

To apply Landau's positivity principle to (5), verify absence of **real** \(L\)-zeros there, rather than assuming it for arbitrary moduli. For real \(0<s<1\), \(\zeta(s)<0\) by the positive alternating eta function, and \(1-5^{-s}>0\). For the quadratic character modulo 5,
\[
L(s,\chi_2)=\sum_{k\ge0}
\bigl[(5k+1)^{-s}-(5k+2)^{-s}-(5k+3)^{-s}+(5k+4)^{-s}\bigr]>0
\tag{8}
\]
by strict convexity of \(u^{-s}\). For either order-four character, the real part is
\[
\Re L(s,\chi_4)=\sum_{k\ge0}
\bigl[(5k+1)^{-s}-(5k+4)^{-s}\bigr]>0.
\tag{9}
\]
The grouped series converge for \(s>0\). At real \(s\ge1\), nonprincipal \(L\)-functions are nonzero (the values at \(s=1\) also follow by the positive convergent series), and the Euler products are nonzero for \(s>1\). Thus the meromorphic expression for \(F\) obtained from (5)–(7) has **no singularity on the real interval \(s>\sigma\)**.

Landau's theorem for Mellin transforms of nonnegative functions (the Laplace-transform form of its nonnegative Dirichlet-series argument) says that a finite real abscissa of convergence must be a singularity. Since \(F\) has no real singularity to the right of \(\sigma\), the integral (5) converges, and defines a holomorphic function, throughout \(\Re s>\sigma\). Subtracting \(F\) from the elementary \(Cx^\sigma\log x\) transform makes the Mellin transform of \(E_1\) holomorphic there. Formula (7) then forbids any nonreal zero of \(\prod_\chi L(s,\chi)\) in this half-plane, completing the proof.

At \(\theta=1/2\), the functional equations of the primitive characters modulo 5 and of \(\zeta\) reflect an off-line nontrivial zero into \(\Re s>1/2\), which is impossible. The extra Euler-factor zeros of the imprimitive principal \(L(s,\chi_0)\) lie on \(\Re s=0\); the GRH conclusion concerns its primitive zeta component.

## 3. Pair-hypothesis reduction, prior art, and limits

PL-458's diagonal calculation, repeated in PL-460, uses only the same-residue \(a=b\) pair remainder and gives, for fixed \(1/6<\theta<1/2\),
\[
Q_{aa}(X,H)=\frac{XH^2}{16}
 +\frac{XH}{4}\log(X/H)+o(XH\log X).
\tag{10}
\]
Choosing \(a=1\) supplies \((M_{1,\theta})\). No other entry of the covariance matrix enters the proof above. The advance over [[research/prime_lattice/findings/PL-460-raw-window-moment-landau-zero-free-gate|PL-460]] is thus a reduction from **four independent diagonal raw-moment hypotheses to one**, and, separately, from all diagonal instances of PL-458(B) to the identity-residue instance.

The analytic ingredients are classical: Cauchy–Schwarz, the Mellin/logarithmic-derivative identity, [[research/prior_art/incremental/PA-landau-nonnegative-dirichlet-series-singularity|Landau's nonnegative-transform singularity principle]] (source 121), and Dirichlet factorization/functional equations (source 120). Harcos–Soundararajan (2023, source 122) independently demonstrates, in the more general Chebotarev setting, that power-saving control of completely split primes can govern other Frobenius classes; its hypothesis and conclusion are **not** identified with the one-sided raw-moment theorem proved here. The special identity-character projection and explicit mod-5 real-axis nonvanishing explain the reduction, but no broad novelty of the classical analytic method or an unconditional advance on zeros is claimed.

This result does **not** certify the prime-source dephased covariance cone, and the moment ceiling is stronger than an unconditional sieve upper bound. The leading coefficient \(1/16\), the uncentered raw moment, the all-large-real-\(X\) quantifier, the real-axis nonvanishing check, and the strict \(1/6<\theta<1/2\) transfer from PL-458(B) are load-bearing. A generic residue \(a\ne1\) weights characters by different phases, so the no-cancellation step for the product does not automatically follow. In a general modulus, a possible real exceptional zero prevents this Landau argument from being transplanted without a separate real-axis analysis.
