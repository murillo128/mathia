# WI-395 — the square-root-prime Fourier norm strictly contracts coherent horizontal defect

**Status:** `EXACT-DERIVED + CLASSICAL-EXPLICIT-FORMULA + SHARP-STRUCTURAL-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

**Parent findings:** WI-392, WI-393, WI-394. Related internal barriers: WI-144, WI-321.

## Claim

WI-394 closes positive quadratic-form portfolios of the moving-carrier channel but deliberately leaves coherent scalar cross terms open. Those cross terms do not evade the square-root-prime wall if their prime side is still controlled by a componentwise absolute Fourier envelope. There is in fact a sharp strip-contraction inequality which applies to arbitrary scalar coherent Fourier shaping, not just to positive mixtures of the existing carrier trials.

Let `mu` be a finite complex Borel measure on `R` satisfying

\[
\|\mu\|_{1/2}
:=\int_{\mathbb R} e^{|u|/2}\,d|\mu|(u)<\infty,
\tag{1}
\]

and let

\[
h(z)=\int_{\mathbb R}e^{iuz}\,d\mu(u)
\tag{2}
\]

on the strip `|Im z|<=1/2`. For `0<=delta_*<1/2` define

\[
q(0):=0,
\]

and, for `0<delta_*<1/2`,

\[
\boxed{
q(\delta_*)
=
\left(\frac{1-2\delta_*}{1+2\delta_*}\right)^{\frac1{2\delta_*}-1}
\left(\frac{4\delta_*}{1+2\delta_*}\right)^2.
}
\tag{3}
\]

Then

\[
\boxed{
0\le q(\delta_*)<1
}
\tag{4}
\]

and, uniformly for every real `gamma` and every `|delta|<=delta_*`,

\[
\boxed{
|h(\gamma+i\delta)+h(\gamma-i\delta)-2h(\gamma)|
\le q(\delta_*)\,\|\mu\|_{1/2}.
}
\tag{5}
\]

The constant in (5) is sharp for each fixed `0<delta_*<1/2`: a two-frequency cosine already approaches equality, and equality is attained when its frequency separation is

\[
D_*(\delta_*)
=
\frac1{\delta_*}
\log\frac{1+2\delta_*}{1-2\delta_*}.
\tag{6}
\]

Equation (5) is exactly adapted to the functional-equation symmetry. If an off-line pair at one positive ordinate is written

\[
\rho_\pm=\frac12\pm\delta+i\gamma,
\]

then a centered analytic explicit-formula test receives the paired value

\[
h(\gamma-i\delta)+h(\gamma+i\delta),
\]

whereas two coincident critical-line copies at the same ordinate receive `2h(gamma)`. Thus the left side of (5) is the horizontal, symmetry-paired discrepancy between an off-line block and its critical-line double reference.

The weight `e^{|u|/2}` on the right is the same square-root exponent that appears on the prime side of Guinand--Weil: a Fourier band centered at `u=A` samples prime powers `n\asymp e^A` with coefficient `Lambda(n)/sqrt(n)`, whose componentwise absolute envelope is of size `e^{A/2}`. Therefore every fixed interior depth `|delta|<=delta_*<1/2` has a strict contraction factor in precisely the Fourier norm that pays for absolute prime control.

This closes a substantial part of the coherent escape left open in WI-394. Scalar coherent interference can only beat the barrier by making the **actual signed prime polynomial** appreciably smaller than its weighted absolute Fourier envelope, or by leaving the scalar explicit-formula architecture. Merely introducing coherent scalar cross terms while continuing to bound the resulting shifted prime bands in absolute value does not improve the defect/prime exponent balance.

No unconditional RH conclusion or improved simple-critical-zero proportion is claimed.

## 1. Exact strip contraction

From (2),

\[
\begin{aligned}
&h(\gamma+i\delta)+h(\gamma-i\delta)-2h(\gamma)\\
&\qquad=
2\int_{\mathbb R}
 e^{iu\gamma}
 \bigl(\cosh(\delta u)-1\bigr)
 \,d\mu(u).
\end{aligned}
\tag{7}
\]

Hence

\[
|\Delta_\delta h(\gamma)|
\le
\int_{\mathbb R}
2\bigl(\cosh(|\delta|\,|u|)-1\bigr)
\,d|\mu|(u).
\tag{8}
\]

For `D>=0` put

\[
r_\delta(D)
:=2(\cosh(\delta D)-1)e^{-D/2}.
\tag{9}
\]

For fixed `D`, this is increasing in `delta>=0`. Therefore the best uniform constant for `|delta|<=delta_*` is

\[
q(\delta_*)=\sup_{D\ge0}r_{\delta_*}(D).
\tag{10}
\]

Substituting

\[
x=e^{-\delta_*D},
\qquad
a=\frac1{2\delta_*}>1,
\]

gives the elementary identity

\[
r_{\delta_*}(D)=x^{a-1}(1-x)^2.
\tag{11}
\]

The unique interior maximizer is

\[
x_*=\frac{a-1}{a+1}
=\frac{1-2\delta_*}{1+2\delta_*},
\tag{12}
\]

which yields (3) and (6).

There is also a direct proof of the strict gap. For `0<=delta_*<1/2` and every `D>0`,

\[
2(\cosh(\delta_*D)-1)
<2(\cosh(D/2)-1),
\]

so

\[
r_{\delta_*}(D)
<(1-e^{-D/2})^2<1.
\tag{13}
\]

Since `r_delta(D)` tends to zero both at `D=0` and at `D=infinity` for every fixed interior depth, its maximum is attained and (4) follows. Combining (8)--(10) proves (5).

The limiting behavior is informative:

\[
q(\delta)=\frac{16}{e^2}\delta^2+O(\delta^3)
\qquad(\delta\to0),
\tag{14}
\]

while

\[
q(\delta)\to1
\qquad(\delta\uparrow1/2).
\tag{15}
\]

Thus the contraction is strong near the critical line and necessarily degenerates as the zero approaches the edge of the critical strip. This matches the near-edge escape already isolated in WI-394.

## 2. The constant is sharp and two frequencies suffice

Take

\[
h_D(z)=2\cos(Dz).
\tag{16}
\]

Its Fourier measure has unit atoms at `+D` and `-D`, so

\[
\|\mu_D\|_{1/2}=2e^{D/2}.
\tag{17}
\]

At `gamma=0`,

\[
\begin{aligned}
&h_D(i\delta)+h_D(-i\delta)-2h_D(0)\\
&\qquad=4(\cosh(\delta D)-1).
\end{aligned}
\tag{18}
\]

The ratio of (18) to (17) is exactly `r_delta(D)`. Choosing `D=D_*(delta)` proves sharpness of (5).

This matters for the route audit. The contraction cannot be improved by appealing only to the weighted absolute Fourier mass in (1): the obstruction is already saturated by the smallest nontrivial coherent system. Any stronger bound must use additional structure of the admissible tests, arithmetic information about prime samples, matrix/signature constraints not visible in a scalar Fourier measure, or distributional information about the exceptional zeros.

## 3. Arbitrary scalar coherent carrier cross terms fall into the same norm

Let

\[
Q(z)=\sum_{j=1}^J c_j e^{ia_jz}
\tag{19}
\]

with distinct real frequencies `a_j`. On the real axis,

\[
|Q(t)|^2
=
\sum_{j,k}c_j\overline{c_k}
 e^{i(a_j-a_k)t}.
\tag{20}
\]

Its analytic continuation is precisely the Hermitian phase product

\[
|Q|^2_{\rm an}(\gamma-i\delta)
=Q(\gamma-i\delta)
 \overline{Q(\gamma+i\delta)}.
\tag{21}
\]

Consequently the functional-equation-paired value at depths `+-delta` is the horizontal second-difference setting of (5).

The diagonal terms `j=k` have zero frequency and disappear from the horizontal discrepancy. Define the coherent off-diagonal square-root budget

\[
\boxed{
\mathcal B_{1/2}(Q)
=
\sum_{j\ne k}
 |c_jc_k|e^{|a_j-a_k|/2}.
}
\tag{22}
\]

Applying (5) to the off-diagonal Fourier measure gives the exact finite-dimensional inequality

\[
\boxed{
\begin{aligned}
&\bigl|
2\operatorname{Re}\bigl[
Q(\gamma-i\delta)
\overline{Q(\gamma+i\delta)}
\bigr]
-2|Q(\gamma)|^2
\bigr|\\
&\qquad\le
q(\delta_*)\,\mathcal B_{1/2}(Q)
\end{aligned}
}
\tag{23}
\]

for every `|delta|<=delta_*`.

No positivity assumption on the coefficients `c_j` is present. Arbitrary phases, signs, and coherent scalar cross terms are included. This is exactly the scalar class that WI-394 could not treat by positive portfolio summation.

## 4. Why the same budget appears in the Guinand--Weil prime term

Let `m` be any one fixed admissible bandlimited window, with

\[
\operatorname{supp}\widehat m\subset[-B,B],
\]

and form the coherent phase-count test

\[
H_{R,Q}(t)=m(t-R)|Q(t)|^2.
\tag{24}
\]

Expanding (20), every cross term `j,k` shifts the Fourier support of `m` to a band centered at

\[
d_{jk}=a_j-a_k.
\tag{25}
\]

In the Guinand--Weil explicit formula, a positive shifted band with center `d>0` samples prime powers with

\[
\log n=d+O_B(1).
\]

Treating that band in absolute value and using Chebyshev plus partial summation costs

\[
O_{m,B}(|c_jc_k|e^{|d_{jk}|/2}).
\tag{26}
\]

Summing componentwise therefore costs, up to the fixed-window constant, exactly the weighted coefficient norm in (22), plus the harmless fixed central-band diagonal contribution. Equivalently, at the Fourier-density level the submultiplicative weight gives

\[
\int e^{|u|/2}|\widehat H_{R,Q}(u)|\,du
\le
C_m
\sum_{j,k}|c_jc_k|e^{|a_j-a_k|/2},
\tag{27}
\]

where

\[
C_m=\int e^{|v|/2}|\widehat m(v)|\,dv<\infty.
\]

Equations (23), (26), and (27) expose the exact structural coincidence. The same frequency difference that amplifies an off-line pair by `cosh(delta d)` is charged on the no-cancellation prime side by the larger boundary exponent `e^{|d|/2}`. At every fixed interior depth the horizontal discrepancy is not merely asymptotically smaller at large `|d|`; its operator norm in the corresponding weighted Fourier space is the strict constant `q(delta_*)<1`.

This is stronger than the exponent comparison in WI-394 for scalar coherent shaping. There is no need to assume positive coefficients, a minimum carrier separation, a finite number of pre-existing quadratic-form channels, or termwise positivity of the cross terms. The only load-bearing arithmetic hypothesis is that the shifted prime bands are still paid for through the componentwise absolute envelope.

## 5. What this closes, and what remains open

WI-394 listed coherent signed/scalar cross terms among the routes not covered by its positive-cone argument. The present result splits that route cleanly.

The following scalar strategy is now closed: choose an arbitrary finite coherent superposition, exploit its cross terms to increase the functional-equation-paired horizontal response, but continue to certify the Guinand--Weil prime side by taking absolute values of the individual shifted Fourier bands. Equations (23) and (26) show that coherence alone cannot improve the square-root-prime exponent; at fixed interior depth there is even a sharp strict contraction in the natural weighted norm.

The genuinely open scalar escape is **arithmetic cancellation**. Different shifted bands can overlap, their coefficients can have opposite phases, and the actual prime polynomial can be much smaller than the componentwise norm (22). Fourier shaping can also arrange zeros or near-zeros at particular prime-power samples. None of that is contradicted by (23): it means that the true arithmetic cost is smaller than the absolute envelope used on the right. The accepted local clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` is conceptually in this surviving category; this finding does not resolve that clue.

Also still open are genuinely matrix-valued or indefinite source-justified couplings not representable by one scalar Fourier measure, aggregation mechanisms in which many exceptional zeros compensate for weak per-zero sensitivity, and near-edge zeros with `|delta|->1/2`, where (15) shows that no uniform contraction survives.

The result is deliberately a modulation/explicit-formula barrier. It does not construct a new cofinal source-exact test by itself, and it does not claim that every source-exact coherent architecture reduces to (24).

## 6. Prior art and novelty boundary

The explicit-formula ingredients are classical and already anchored for this research line: Guinand--Weil turns Fourier bands into prime-power samples, while WI-393 records the Beurling--Selberg and Landau--Gonek literature explaining why a band near frequency `A` has an absolute square-root-prime cost `e^{A/2}`. Weighted `l^1` Fourier norms with submultiplicative exponential weights are standard Wiener/Beurling harmonic-analysis objects. No novelty is claimed for those ingredients.

The line-local audit covered WI-144, WI-321, WI-392, WI-393, WI-394, the current research contract, the current mind frontier, and the accepted clue set. WI-144 concerns Fourier-positive Hilbert/Frobenius scalarizations, and WI-321 concerns Hilbert amplification of an already-known scalar semibound; neither gives the strip second-difference contraction (5). External searches covered weighted Wiener/Beurling algebras, analytic-strip Fourier norms, Guinand--Weil trigonometric-polynomial tests, and bandlimited explicit-formula optimization. No source located in that audit states the sharp constant (3) or this exact identification of the functional-equation-paired horizontal defect with the square-root-prime absolute Fourier norm. This is not a priority claim.

The durable Mathia contribution is the self-contained sharp inequality (3)--(6), its exact coherent-polynomial specialization (23), and the resulting closure of the no-cancellation scalar-coherence route left open by WI-394.

## Decisive audit test

The finding reduces to three independently checkable interfaces:

1. for a functional-equation pair `1/2+-delta+i gamma`, verify that the centered analytic test is evaluated at `gamma-i delta` and `gamma+i delta`, so the horizontal discrepancy is exactly the second difference in (5);
2. verify the scalar maximization in (9)--(12), including the sharp constant (3);
3. for the fixed-window coherent test (24), verify that each Fourier cross term is shifted by `a_j-a_k` and that componentwise absolute prime control costs `O(e^{|a_j-a_k|/2})` by the same Guinand--Weil/Chebyshev estimate used in WI-393.

If the actual signed prime polynomial admits cancellation beyond that componentwise envelope, the finding is not falsified; that is precisely its surviving escape route.

## Research consequence

The frontier after WI-394 is narrower than it appeared. Positive portfolios are blocked by WI-394, and now arbitrary **scalar coherent** phase shaping is blocked as long as its prime bands are controlled only through absolute values. The next useful scalar advance must therefore be genuinely arithmetic: prove cancellation or structured subtraction in the defect-anchored short prime polynomial, or build a source-exact Fourier shape whose prime-power samples are small for a reason stronger than triangle inequality. Otherwise the program has to leave the scalar channel through a new matrix/signature mechanism or aggregate exceptional mass before per-zero contraction becomes decisive.
