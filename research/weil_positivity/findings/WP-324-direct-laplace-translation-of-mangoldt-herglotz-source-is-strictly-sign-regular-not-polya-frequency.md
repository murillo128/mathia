---
id: WP-324
title: Direct Laplace translation of the Mangoldt Herglotz source is strictly sign-regular, not Pólya-frequency
branch: weil_positivity
status: supported
kind: source-laplace-translation-total-positivity-obstruction
claim_strength: exact all-order ordered-determinant sign law for the canonical positive-energy Mangoldt Laplace transform, with strict negative 2x2 and 3x3 translation minors, an exact one-sided-domain obstruction, and a matched-control proof that reversing orientation yields universal Hankel total positivity rather than arithmetic-selective positivity
created: 2026-09-16
related: [WP-304, WP-318, WP-322, WP-323]
prior_art:
  - I. J. Schoenberg, On Totally Positive Functions, Laplace Integrals and Entire Functions of the Laguerre-Polya-Schur Type, Proceedings of the National Academy of Sciences 33 (1947), 11-17, DOI 10.1073/pnas.33.1.11
  - I. J. Schoenberg, On Pólya frequency functions. I. The totally positive functions and their Laplace transforms, Journal d'Analyse Mathématique 1 (1951), 331-374, DOI 10.1007/BF02790092
  - I. J. Schoenberg and Anne Whitney, On Pólya Frequency Function. III. The Positivity of Translation Determinants With an Application to the Interpolation Problem by Spline Curves, Transactions of the American Mathematical Society 74 (1953), 246-259, DOI 10.2307/1990881
  - Samuel Karlin, Total Positivity, Vol. I, Stanford University Press, 1968, for the basic composition formula and sign-regular/total-positive kernel calculus
---

# WP-324 — Direct Laplace translation of the Mangoldt Herglotz source is strictly sign-regular, not Pólya-frequency

## Claim

`WP-322` and `WP-323` close finite Pick matrices and finite confluent Pick jets because their positivity is universal resolvent-Gram geometry. The live clue `CLUE-weil-positivity-translation-total-positivity-after-pick-universality` asks whether the same scalar source can escape that universality by passing canonically to Schoenberg-style ordered translation determinants.

The most direct source-native passage can now be classified exactly, and it fails before any Riemann-specific information is used.

Take the positive-energy pole-normalized Mangoldt measure already isolated in `WP-304`,

\[
\mu_+
=
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}\,\delta_{\log n},
\tag{1}
\]

and its ordinary Laplace transform

\[
L(s)
:=
\int_0^\infty e^{-sE}\,d\mu_+(E)
=
\sum_{n=p^k}
\frac{\Lambda(n)}{n+1}\,n^{-s},
\qquad s>0.
\tag{2}
\]

For every integer \(m\ge1\), every two strictly increasing real \(m\)-tuples

\[
x_1<\cdots<x_m,
\qquad
y_1<\cdots<y_m
\tag{3}
\]

with \(x_1>y_m\), so that every difference \(x_i-y_j\) lies in the Laplace domain, define the ordered translation determinant

\[
\Delta_m(x,y)
:=
\det\!\bigl[L(x_i-y_j)\bigr]_{i,j=1}^m.
\tag{4}
\]

Then

\[
\boxed{
\operatorname{sgn}\Delta_m(x,y)
=
(-1)^{m(m-1)/2}.
}
\tag{5}
\]

The inequality is strict because \(\mu_+\) has infinitely many distinct positive atoms. In particular,

\[
\boxed{\Delta_2<0,\qquad \Delta_3<0.}
\tag{6}
\]

Thus the direct Laplace translation kernel \(K(x,y)=L(x-y)\) fails even \(TP_2\), hence cannot be a Pólya-frequency kernel. The failure is not arithmetic: it holds for every nondegenerate positive measure for which the displayed Laplace values exist. At order two this is exactly the classical opposition between the strict **log-convexity** of a positive-measure Laplace transform and the **log-concavity** required for a \(PF_2\) translation profile.

The apparent orientation repair is also non-arithmetic. If instead one reverses the second translation orientation and forms the Hankel kernel

\[
H(x,y)=L(x+y),
\qquad x,y>0,
\tag{7}
\]

then every ordered minor is nonnegative, and for \(\mu_+\) every finite ordered minor is strictly positive:

\[
\boxed{
\det[L(x_i+y_j)]_{i,j=1}^m>0.
}
\tag{8}
\]

But (8) is universal for every positive measure with at least \(m\) support points. It is the basic total-positivity composition mechanism, not an arithmetic certificate.

There is a second exact obstruction. `WP-304` proves

\[
\mu_+([0,R])=R+O(1),
\tag{9}
\]

hence

\[
\boxed{
L(s)=\frac1s+O(1)
\qquad(s\downarrow0).
}
\tag{10}
\]

So the direct source transform has abscissa of convergence \(0\), blows up non-integrably at the boundary, and is unavailable for nonpositive differences. The canonical even source \(\mu_{\rm sym}=\mu_++\check\mu_+\) is worse for this purpose: its bilateral Laplace integral diverges at every real parameter. Therefore the actual Herglotz source does **not** itself provide the globally defined translation profile required by the Schoenberg Pólya-frequency theorem.

The clue is therefore narrowed sharply:

\[
\boxed{
\text{positive Herglotz source}
\;\xrightarrow{\text{direct Laplace/semigroup characters}}\;
\text{strict sign-regularity, not PF positivity}.
}
\tag{11}
\]

Reversing orientation gives universal Hankel total positivity. Any surviving translation-total-positivity route must therefore introduce a genuinely different, source-forced nonlinear operation or leave the positive Laplace-mixture category. Its sign can no longer be credited merely to positivity of the Herglotz representing measure, and the resulting operation must still derive the finite-prime and archimedean/global pieces without importing \(\Xi\), its zeros, or an RH-equivalent Pólya-frequency target.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SOURCE-NATIVE-LAPLACE + ALL-ORDER-SIGN-REGULARITY + TP2-FAILURE + PF2-LOG-CONCAVITY-OPPOSITION + HANKEL-TP-UNIVERSALITY + MATCHED-CONTROL + DOMAIN-OBSTRUCTION + SCHOENBERG-PRIOR-ART-REDIRECT + NOT-WEIL-POSITIVITY`.

## 1. The source Laplace transform is well-defined exactly on the positive half-line

From `WP-304`, the cumulative source mass satisfies (9). Stieltjes integration by parts gives, for every \(s>0\),

\[
L(s)
=
s\int_0^\infty e^{-sE}\,\mu_+([0,E])\,dE.
\tag{12}
\]

Substituting \(\mu_+([0,E])=E+O(1)\) yields

\[
L(s)
=
s\int_0^\infty E e^{-sE}\,dE
+
O\!\left(
s\int_0^\infty e^{-sE}\,dE
\right)
=
\frac1s+O(1),
\tag{13}
\]

which proves (10).

At \(s=0\), the total mass is infinite. For \(s<0\), the factor \(e^{-sE}\) grows exponentially while the cumulative mass is asymptotically linear, so the integral diverges. Hence

\[
\boxed{\operatorname{dom}L=(0,\infty)}
\tag{14}
\]

as an ordinary positive Laplace transform.

A finite shift \(L(s+a)\), \(a>0\), only moves this boundary to \(-a\); it never produces a profile defined on all real differences. Positive affine rescalings, exponential gauges, or positive powers likewise do not alter the determinant-sign obstruction below because they preserve strict convexity of the logarithm on their domain.

For the even explicit-formula carrier,

\[
\mu_{\rm sym}
=
\mu_++\check\mu_+,
\tag{15}
\]

the real bilateral Laplace integral would contain \(L(s)+L(-s)\). One term diverges whenever \(s\ne0\), while both masses diverge at \(s=0\). Thus there is no nonempty real strip of bilateral Laplace convergence from which a Schoenberg translation kernel could be read off directly.

This distinction matters. Schoenberg's theorem begins with a translation profile \(\Lambda\) and identifies the **bilateral Laplace transform of that profile** with the reciprocal of a Laguerre--Pólya entire function. Equation (2) is instead the one-sided Laplace transform of Mathia's positive spectral measure. Treating these two Laplace roles as interchangeable would import the desired Pólya-frequency object rather than derive it.

## 2. The \(2\times2\) ordered minor has the wrong sign by strict log-convexity

For \(s>0\), exponential damping justifies differentiation under the integral. Write

\[
\phi(s)=\log L(s).
\tag{16}
\]

The exponentially tilted probability measure

\[
d\nu_s(E)
=
\frac{e^{-sE}}{L(s)}\,d\mu_+(E)
\tag{17}
\]

gives

\[
\phi''(s)
=
\operatorname{Var}_{\nu_s}(E).
\tag{18}
\]

Because \(\mu_+\) has infinitely many support points,

\[
\boxed{\phi''(s)>0\quad(s>0).}
\tag{19}
\]

Thus \(L\) is strictly log-convex.

Now take \(x_1<x_2\), \(y_1<y_2\), and \(x_1>y_2\). Put

\[
a=x_1-y_2>0,\qquad
b=y_2-y_1>0,\qquad
c=x_2-x_1>0.
\tag{20}
\]

Then

\[
\Delta_2
=
L(a+b)L(a+c)-L(a)L(a+b+c).
\tag{21}
\]

Strict convexity of \(\phi\) implies

\[
\phi(a+b)+\phi(a+c)
<
\phi(a)+\phi(a+b+c),
\tag{22}
\]

and therefore

\[
\boxed{\Delta_2<0.}
\tag{23}
\]

This is already decisive. A nonnegative translation profile is \(PF_2\) exactly when the translation kernel \(\Lambda(x-y)\) is \(TP_2\); in the ordinary positive-support setting this is the familiar log-concavity condition. The source Laplace profile is forced by positivity into the opposite curvature class.

No prime-power support property entered (18)-(23). Replacing \(\mu_+\) by Lebesgue measure \(dE\) gives the matched control \(L_0(s)=1/s\), with the same strict negative \(2\times2\) translation minors. So the first nontrivial determinant already fails the clue's arithmetic-selectivity test.

## 3. Every ordered translation minor has a fixed alternating sign

The order-two argument extends exactly to all orders and also supplies the requested \(3\times3\) audit.

For (3) with \(x_1>y_m\),

\[
L(x_i-y_j)
=
\int_0^\infty
 e^{-x_iE}e^{y_jE}\,d\mu_+(E).
\tag{24}
\]

The continuous Cauchy--Binet/Andréief identity gives

\[
\Delta_m
=
\frac1{m!}
\int_{(0,\infty)^m}
\det[e^{-x_iE_k}]_{i,k}
\det[e^{y_jE_k}]_{j,k}
\prod_{k=1}^m d\mu_+(E_k).
\tag{25}
\]

On the chamber \(E_1<\cdots<E_m\), the exponential kernel \(e^{uE}\) is strictly totally positive. Since \(-x_1>\cdots>-x_m\), restoring increasing order in the first determinant requires \(m(m-1)/2\) row transpositions. Hence

\[
\operatorname{sgn}
\det[e^{-x_iE_k}]
=
(-1)^{m(m-1)/2},
\qquad
\det[e^{y_jE_k}]>0.
\tag{26}
\]

The product in (25) therefore has the fixed sign in (5). Since \(\mu_+\) has at least \(m\) distinct atoms of positive mass, a positive-measure set of distinct \(m\)-tuples contributes strictly, so \(\Delta_m\ne0\).

For the first two nontrivial orders,

\[
(-1)^{2(1)/2}=-1,
\qquad
(-1)^{3(2)/2}=-1,
\tag{27}
\]

hence both \(2\times2\) and \(3\times3\) ordered translation minors are strictly negative.

This is stronger than a single counterexample: the direct source transform is a classical **strictly sign-regular** kernel with an order-dependent sign pattern. The arithmetic masses affect magnitudes but not determinant signs.

The same proof applies after any positive spectral reweighting

\[
d\mu_+(E)\mapsto w(E)\,d\mu_+(E),
\qquad w(E)\ge0,
\tag{28}
\]

whenever the relevant Laplace values remain finite and at least \(m\) support points survive. Therefore positive linear preprocessing of the source measure cannot turn the direct semigroup-character construction into a Pólya-frequency kernel.

## 4. Reversing the orientation produces universal Hankel total positivity

One might try to repair (26) by reversing the sign in the second exponential. This gives

\[
H(x,y)
=
L(x+y)
=
\int_0^\infty e^{-xE}e^{-yE}\,d\mu_+(E).
\tag{29}
\]

For increasing \(x_i\) and \(y_j\), Andréief now gives

\[
\det[H(x_i,y_j)]
=
\frac1{m!}
\int
\det[e^{-x_iE_k}]
\det[e^{-y_jE_k}]
\prod_k d\mu_+(E_k).
\tag{30}
\]

Both determinants carry the same sign \((-1)^{m(m-1)/2}\), so their product is nonnegative. Infinite support makes it strict:

\[
\boxed{
\det[L(x_i+y_j)]>0.
}
\tag{31}
\]

This is the classical composition formula for total-positive kernels. Crucially, it holds for **every** positive measure with sufficiently many support points. The source has not acquired a Riemann-specific sign theorem; it has merely moved from a sign-regular translation kernel to a universal Hankel Gram/composition kernel.

The Lebesgue matched control again makes the point transparent:

\[
d\mu_0(E)=dE,
\qquad
L_0(s)=\frac1s,
\qquad
H_0(x,y)=\frac1{x+y}.
\tag{32}
\]

The Cauchy kernel \(1/(x+y)\) has the same ordered Hankel total positivity without any prime data.

## 5. Prior-art audit and novelty boundary

Schoenberg's 1947 and 1951 work classifies Pólya-frequency functions through total positivity of translation determinants and reciprocal bilateral Laplace transforms of Laguerre--Pólya entire functions. Schoenberg--Whitney 1953 develops the positivity of translation determinants, and Karlin's 1968 monograph systematizes the composition calculus used in (25) and (30).

Therefore neither "Laplace transforms of positive measures are log-convex" nor the determinant composition formula is new. The new Mathia content is the exact application to the canonical source left open after `WP-322`/`WP-323`:

1. the actual \(\mu_+\) produces strict **reverse** sign at orders \(2\) and \(3\), indeed the all-order law (5);
2. its linear-mass asymptotic makes the direct profile one-sided and singular at the origin, so it is not even in the global translation-function domain of the Schoenberg criterion;
3. the natural orientation reversal gives a Hankel-TP kernel whose positivity is a matched-control universal consequence of \(\mu\ge0\).

This is a prior-art redirect, not a new total-positivity theorem.

The result does **not** prove that no nonlinear functional of the exact source can ever produce a Pólya-frequency translation profile. For example, taking reciprocals, solving an inverse transform problem, or constructing a different boundary object leaves the positive Laplace-mixture category. Such a move must be justified independently and cannot inherit its sign from the simple positivity argument above. It must also survive the mandate's stronger test: derive the finite-prime and archimedean/global terms from one intrinsic structure and obtain nonnegativity before any RH-equivalent target identification.

## Consequence for the research line

Finite Pick/confluent positivity was universal because it was a resolvent Gram. Direct ordered translation total positivity does not provide an escape: the canonical positive source Laplace transform lands in the wrong sign class, and the obvious orientation repair lands in another universal positive class.

The next scalar candidate therefore cannot be merely

\[
\mu_+
\mapsto
\int e^{-sE}\,d\mu_+(E)
\mapsto
\text{translation/Hankel minors}.
\tag{33}
\]

A viable source-selective positivity mechanism must use an additional exact invariant that is not forced for arbitrary positive measures—most plausibly a nonlinear support/mass relation, an infinite-domain operator property with a genuine arithmetic existence theorem, or a change to matrix/operator-valued or nonseparable finite--archimedean geometry. Merely changing the ordered determinant family does not yet make the sign arithmetic.
