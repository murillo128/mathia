# PL-459 — The PL-458 integrated first-moment hypothesis already carries a Dirichlet zero-free gate

**Evidence/status:** EXACT-DERIVED + CLASSICAL PNT/EXPLICIT-FORMULA BRIDGE / NEGATIVE-OBSTRUCTION TO AN INDEPENDENT COVARIANCE ROUTE.

**Parent findings:** PL-458 (assumption A and conditional mod-5 covariance transfer), PL-421 (normalized local-factor image cone).

## Claim

For each reduced class \(a\bmod 5\), write
\[
\psi_a(x)=\sum_{\substack{n\le x\\n\equiv a\ (5)}}\Lambda(n),\qquad
E_a(x)=\psi_a(x)-x/4.
\]
Fix \(0<\theta<1/2\), put \(H=\lfloor X^\theta\rfloor\), and set
\[
P_a(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n).
\]
Suppose the [[research/prime_lattice/findings/PL-458-mod5-singular-series-matrix-second-order-transfer|PL-458]] first-moment input (A) holds **for every sufficiently large real \(X\)**, simultaneously for \(a=1,2,3,4\):
\[
\max_a\left|\int_X^{2X}P_a(y)\,dy-XH/4\right|
=o(X\log X). \tag{A_\theta}
\]
Then
\[
\boxed{\ E_a(x)=o(x^{1-\theta}\log x)\quad(a=1,2,3,4),\ } \tag{1}
\]
and every Dirichlet \(L\)-function modulo \(5\), including the principal factor containing \(\zeta\), has **no zero in**
\[
\boxed{\ \Re s>1-\theta.\ } \tag{2}
\]
In particular, if \((A_{\theta_j})\) holds for a sequence of fixed exponents \(\theta_j\uparrow1/2\), then **joint GRH for all characters modulo \(5\), including ordinary RH, follows**.

Conversely, joint GRH modulo \(5\) implies \((A_\theta)\) for every fixed \(0<\theta<1/2\). Thus the *entire family* of first-moment hypotheses along any fixed sequence \(\theta_j\uparrow1/2\) is equivalent to joint GRH modulo \(5\). This equivalence is a diagnosis of the strength of an **unproved hypothesis**, not a proof of GRH or RH. The hypothesis (B) of PL-458 is not used anywhere in this deduction.

The original PL-458 application takes \(1/6<\theta<1/2\); the argument here applies to the slightly wider range \(0<\theta<1/2\). A claim about a single exponent is only the zero-free half-plane (2), not RH. The all-\(X\) quantifier is essential: merely verifying \((A_\theta)\) on a sparse sequence of \(X\)'s would not justify (1).

## Exact window-to-dyadic transfer

For \(X\) large and \(1\le H\le X/2\), interchange the nonnegative finite sum and integral:
\[
I_a(X,H):=\int_X^{2X}P_a(y)\,dy
=\sum_{n\equiv a(5)}\Lambda(n)\,
  \big|[X,2X]\cap[n-H,n)\big|.
\]
Every \(X+H<n\le2X\) carries exactly weight \(H\). The discrepancy from \(H(\psi_a(2X)-\psi_a(X))\) is confined to the two endpoint strips of length at most \(H\) near \(X\) and \(2X\), where each overlap differs from the flat weight by at most \(H\). The elementary bound \(\Lambda(n)\le\log(3X)\), with \(O(H+1)\) integers per strip, yields, uniformly over the four channels,
\[
\boxed{\ I_a(X,H)=H\{\psi_a(2X)-\psi_a(X)\}
+O(H(H+1)\log(3X)).\ } \tag{3}
\]
No prime-pair hypothesis, short-interval prime theorem, or GRH is used in (3).

For \(H=\lfloor X^\theta\rfloor\), the boundary remainder in (3) is
\(O(X^{2\theta}\log X)=o(X\log X)\) because \(\theta<1/2\).
Consequently \((A_\theta)\) implies
\[
H\{E_a(2X)-E_a(X)\}=o(X\log X)
\quad\Longrightarrow\quad
E_a(2X)-E_a(X)=o(X^{1-\theta}\log X). \tag{4}
\]
Repeatedly bisect \(x\) down to a fixed large baseline. The errors in (4)
sum as a geometric series since \(1-\theta>0\): after separating finitely
many small dyadic scales, one obtains (1). This step requires (4) for all
large \(X\), not an averaged-in-\(X\) or subsequential statement.

## From progression errors to zero exclusion

For each character \(\chi\bmod 5\), orthogonality gives
\[
\psi(x,\chi):=\sum_{n\le x}\chi(n)\Lambda(n)
=\sum_{a=1}^4\chi(a)\psi_a(x)
=\delta_\chi x+o(x^{1-\theta}\log x), \tag{5}
\]
where \(\delta_\chi=1\) for the principal character and \(0\) otherwise.
For \(\Re s>1\), the classical Mellin/logarithmic-derivative identity reads
\[
-\frac{L'}{L}(s,\chi)
=s\int_{1^-}^{\infty}\psi(x,\chi)x^{-s-1}\,dx.
\]
Subtracting the principal main term \(\delta_\chi s/(s-1)\), (5) makes the
remaining integral locally uniformly convergent, hence holomorphic,
throughout \(\Re s>1-\theta\). Since \(-L'/L\) has a pole at every zero of
\(L(s,\chi)\), no such zero can lie in this half-plane. The principal
character satisfies \(L(s,\chi_0)=\zeta(s)(1-5^{-s})\); the added Euler
factor has its zeros on \(\Re s=0\), outside the half-plane in question.
This establishes (2).

If (A) holds for \(\theta_j\uparrow1/2\), every point with
\(\Re s>1/2\) lies in \(\Re s>1-\theta_j\) for some \(j\); thus all
modulo-5 \(L\)-functions are zero-free to the right of the critical line.
Their classical functional equations and zero symmetries then give
joint GRH. No analytic continuation is *constructed* by the lattice
covariance: it is the classical continuation and functional equation
that are used in this implication.

## Converse under GRH and the strict endpoint restriction

Joint GRH modulo \(5\), via the classical Dirichlet explicit formula,
gives the fixed-modulus bounds
\[
E_a(x)=O(x^{1/2}\log^2(2x))\qquad(a\in U_5).
\]
Insert these into (3) to find, for each fixed \(\theta<1/2\),
\[
I_a(X,H)-XH/4
=O(HX^{1/2}\log^2 X+H^2\log X)
=o(X\log X). \tag{6}
\]
Thus GRH implies every \((A_\theta)\) in the stated range, completing
the equivalence for a family approaching \(1/2\).

At \(\theta=1/2\), the crude endpoint bound (3) no longer gives an
\(o(X\log X)\) remainder, and the GRH error in (6) is no longer
\(o(X\log X)\). Therefore **the present equivalence is stated for
fixed exponents strictly below \(1/2\)**. Neither the reverse
implication at the endpoint nor an equivalence for merely one fixed
\(\theta<1/2\) is asserted.

## Prior art, falsification, and consequence for Prime Lattice

The correspondence between PNT remainder bounds, Mellin continuation
of \(-L'/L\), zero-free half-planes, and GRH-conditional explicit-formula
bounds is classical; see Montgomery--Vaughan, *Multiplicative Number
Theory I*, Chapters 10--14 (source 120). The finite geometric transfer
from the specific PL-458 dyadic integrated-window assumption to
\(E_a(x)\), and the identification of that assumption as an independent
RH-strength gate when \(\theta\uparrow1/2\), are the line-level deductions.
No claim of a new zero-free theorem or a proved prime-distribution
estimate is made.

The decisive scope checks are: retain all four progression channels
(including their principal combination); retain the all-\(X\) and
little-\(o\) quantifiers; retain the endpoint error in (3); do not
replace the signed first moment (A) by qualitative fixed-modulus PNT;
do not infer a fixed-exponent converse solely from zero-free geometry;
and do not treat covariance hypothesis (B) or positivity at \(t=0\) as
providing (A). A proposed proof of PL-458 through both (A) and (B)
therefore cannot be claimed to avoid the classical Dirichlet zero problem
unless it finds an **independent weaker first-moment input** or a
different centering/cancellation transfer. This is a logical obstruction
to that proof strategy, not a falsification of the conditional
implication PL-458 and not RH.
