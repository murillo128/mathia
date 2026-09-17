# AF-393 — Positive-curvature PF3 is exactly local differential fidelity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `PF3` · `TOEPLITZ` · `LOCAL-TO-GLOBAL` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f:\mathbb R\to(0,\infty)
\]

be `C^4`, put

\[
g=\log f,
\qquad
q=-g'',
\qquad
r=(\log q)'=\frac{q'}q,
\]

and assume

\[
q(t)>0
\qquad\text{for every }t\in\mathbb R.
\]

Then the following are equivalent:

1. the translation kernel `K_f(x,y)=f(x-y)` is totally nonnegative through order three;
2. for every `t`,

\[
\boxed{(\log q)''(t)\le 2q(t)};
\tag{1}
\]

3. for one, hence every, base point `t_0`, the mass-normalized drift

\[
H(t)
:=
\frac{q'(t)}{q(t)}
-2\int_{t_0}^{t}q(s)\,ds
\tag{2}
\]

is nonincreasing.

Thus the finite adjacent-window criterion of AF-392 contains no additional information in the strictly positive smooth-curvature interior: after changing from physical position to accumulated curvature mass, the full order-three placement condition is exactly the integrated form of the infinitesimal inequality `(1)`.

In particular, the strictly positive branch left open in AF-388 is closed. If the shrinking-mesh solid `PF_2/PF_3` hypotheses of AF-388 hold and the resulting curvature satisfies `q>0` everywhere, then AF-388 supplies `(1)`, and therefore the full continuum kernel is `TN_3`. The remaining multiscale recognition problem is a boundary problem at zeros of `q`, not a finite-window problem in the positive interior.

## Mass-coordinate reduction

Fix `t\in\mathbb R` and adjacent positive gaps `a,b`. Use the AF-392 notation

\[
A=\int_{t-a}^{t}q(s)\,ds,
\qquad
B=\int_{t-a-b}^{t-a}q(s)\,ds.
\tag{3}
\]

AF-392 proves that order-three total nonnegativity is equivalent to

\[
A+B+\frac{B'}B-\frac{A'}A\ge0
\tag{4}
\]

for every `t,a,b>0`, where

\[
\frac{A'}A
=
\frac1A\int_{t-a}^{t}q(s)r(s)\,ds,
\qquad
\frac{B'}B
=
\frac1B\int_{t-a-b}^{t-a}q(s)r(s)\,ds.
\tag{5}
\]

Introduce accumulated curvature mass with origin at the common window boundary,

\[
Q(x)=\int_{t-a}^{x}q(s)\,ds.
\tag{6}
\]

Because `q>0`, `Q` is strictly increasing. It maps the left window onto `[-B,0]` and the right window onto `[0,A]`. Moreover the measure `q(x)\,dx` is carried exactly to Lebesgue measure `du=dQ`.

Condition `(1)` is

\[
r'(x)\le 2q(x).
\tag{7}
\]

Hence for every `x` in the left window and every `y` in the right window,

\[
r(y)-r(x)
\le
2\int_x^y q(s)\,ds
=
2\bigl(Q(y)-Q(x)\bigr).
\tag{8}
\]

Average `(8)` with respect to the product of the normalized curvature-mass measures

\[
\frac{q(x)\,dx}{B}
\quad\text{and}\quad
\frac{q(y)\,dy}{A}.
\]

The left side becomes

\[
\frac{A'}A-\frac{B'}B.
\tag{9}
\]

Under `Q`, the two normalized measures are uniform on `[-B,0]` and `[0,A]`, so

\[
\mathbb E_R Q=\frac A2,
\qquad
\mathbb E_L Q=-\frac B2.
\tag{10}
\]

Therefore

\[
\frac{A'}A-\frac{B'}B
\le
2\left(\frac A2+\frac B2\right)
=A+B,
\tag{11}
\]

which is exactly `(4)`.

Thus the pointwise differential condition implies every finite adjacent-window test.

## Converse and exact equivalence

AF-392 already gives the converse by shrinking the two windows. Let `a,b\downarrow0`. Then

\[
\frac{B'}B-\frac{A'}A
=-\frac{a+b}{2}r'(t)+o(a+b),
\]

and

\[
A+B=(a+b)q(t)+o(a+b).
\]

Dividing `(4)` by `a+b` gives

\[
r'(t)\le2q(t),
\]

which is `(1)`.

Finally,

\[
H'(t)=r'(t)-2q(t),
\]

so `(1)` is equivalent to monotonicity of `H`. This proves all three equivalences.

The same argument also shows that if

\[
(\log q)''<2q
\qquad\text{everywhere},
\]

then every AF-392 finite-window inequality is strict, so all non-colliding minors through order three are strictly positive.

## What changes in the AF-388--AF-392 picture

AF-388 extracted `(1)` from shrinking solid order-three minors but treated it only as an infinitesimal necessary condition. AF-392 then derived the exact adjacent-window criterion and interpreted the difference between `(1)` and `(4)` as a remaining finite-placement information gap.

The mass-coordinate calculation above closes that gap in the positive-curvature interior. The factor `2` in `(1)` is exactly the constant required for this to work: a slope bound `dr/dQ\le2` implies that the difference between the right- and left-window averages of `r` is at most twice the distance between the two uniform mass centroids, namely `A+B`.

This also explains why AF-391's log-concavity hypothesis was sufficient but unnecessarily strong. Log-concavity gives `r'\le0`; order-three fidelity only requires the larger cone `r'\le2q`.

The genuinely unresolved regime is where `q` reaches zero. There the mass coordinate ceases to be locally bi-Lipschitz, `r=q'/q` may be singular, and the AF-392 ratios can require limiting analysis. AF-389--AF-391 provide two sufficient boundary closures, but AF-393 makes clear that no extra finite-window hypothesis is needed away from that boundary.

## Falsification and boundaries

- Strict positivity of `q` is essential to the stated proof. It makes `Q` strictly increasing and keeps `r`, `A^{-1}`, and `B^{-1}` regular. The theorem does not classify curvature zeros.
- `C^4` is a convenient sufficient regularity level so that `q\in C^2` and `(\log q)''` is classical. The mass-coordinate implication itself can be weakened to an absolutely continuous formulation of `r` with `r'\le2q` almost everywhere, but that extension is not claimed here.
- The result concerns translation kernels and order three. It does not assert an analogous one-point differential characterization at higher total-positivity orders.
- The theorem does not supply the shrinking solid signs. In an arithmetic application those signs still have to come from the source; the result only says that, once they yield `(1)` with `q>0`, no independent finite-placement certificate is missing.
- No RH consequence is asserted.

## Prior art and novelty audit

The ambient classification problem is classical. H. F. Weinberger's 1983 paper is explicitly a characterization of Pólya-frequency functions of order three, while Schoenberg's work and Karlin's monograph provide the surrounding translation-kernel and total-positivity theory. Current publisher and University of Minnesota metadata verify the Weinberger paper and its bibliographic identity, but the primary article text remains inaccessible in this literature pass. The exact theorem above may therefore be a smooth reformulation or specialization of Weinberger's characterization, and **no novelty claim is made**.

The durable Arithmetic Fidelity contribution is the internal correction and mechanism: the AF-392 adjacent-window test, when rewritten in curvature-mass coordinates, is exactly the integrated AF-388 differential inequality. This removes a spurious positive-interior information gap from the current research corpus and isolates curvature-zero boundary strata as the actual remaining recognition obstruction.

Primary neighboring sources:

- H. F. Weinberger, **“A Characterization of the Polya Frequency Functions of Order 3,”** *Applicable Analysis* 15(1--4) (1983), 53--69, DOI `10.1080/00036818308839439`.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* 1 (1951), 331--374, DOI `10.1007/BF02790092`.
- Samuel Karlin, ***Total Positivity, Vol. I***, Stanford University Press (1968).