# AF-405 — full Euler log is strictly sign-regular through order four

**Status:** `EXACT-DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `SOURCE-COMPLEXITY-GATE`, `TOTAL-POSITIVITY`, `CONFLUENT-CERTIFICATE`, `EXACT-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
L(x):=-\log(1-e^{-x}),\qquad x>0,
\]

and in logarithmic coordinates put

\[
f(t):=L(e^t),\qquad K(u,v):=f(u-v).
\]

Then `K` is **strictly totally positive through order four**. Thus for every `1<=m<=4` and every strictly increasing tuples

\[
u_1<\cdots<u_m,\qquad v_1<\cdots<v_m,
\]

one has

\[
\boxed{\det[K(u_i,v_j)]_{i,j=1}^m>0.}
\]

Equivalently, for

\[
E_s(q):=-\log(1-q^{-s}),\qquad s>0,\ q>1,
\]

and increasing `s_1<...<s_m`, `q_1<...<q_m`,

\[
\boxed{
(-1)^{m(m-1)/2}
\det[E_{s_i}(q_j)]_{i,j=1}^m>0,
\qquad 1\le m\le4.
}
\]

AF-217 proves that the same kernel is **not** totally nonnegative at all orders. Therefore the smallest bad order is now known to satisfy

\[
\boxed{m_{\rm fail}\ge5.}
\]

The new work is the exact positivity of the fourth fully confluent determinant. AF-403 then globalizes the complete strict confluent flag to arbitrary separated node placements.

A direct source-complexity consequence is that a nonzero finite full-Euler signed source with at most three ordered sign changes cannot annihilate four distinct positive real samples. Prime support is allowed but is not needed for this finite-order theorem.

## 1. AF-404 reduces the fourth-order gate to one local determinant

For `m>=1` define the oriented fully confluent determinant

\[
H_m(t):=(-1)^{m(m-1)/2}
\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
\]

AF-218 and AF-219 give

\[
H_1>0,\qquad H_2>0,\qquad H_3>0
\]

on the whole real line. AF-404 shows that, writing

\[
g=\log f,\qquad q=-g'',\qquad S=2q^3-qq''+(q')^2,
\]

one has

\[
H_2=f^2q,
\qquad
H_3=f^3S,
\]

and

\[
\frac{H_4}{f^4}
=\frac{S^2}{q}\Bigl(3q-(\log S)''\Bigr).
\]

Hence the unresolved full-Euler order-four question in AF-404 is exactly `H_4(t)>0` for every `t`.

The proof below evaluates this determinant directly in the natural variable

\[
x=e^t>0,
\qquad y=e^{-x}\in(0,1),
\qquad \ell=L(x)=-\log(1-y).
\]

No numerical sign sampling is used in the theorem.

## 2. Exact fourth-determinant decomposition

Using `d/dt=x d/dx`, differentiating `L(x)`, and simplifying the `4 x 4` determinant gives the exact identity

\[
\boxed{
H_4(t)
=
\frac{x^6e^{-10x}}{(1-e^{-x})^{12}}
\left[
\frac{e^{-x}}{1-e^{-x}}\,\mathcal P(x)
+
\left(
\frac{e^{-x}}{1-e^{-x}}-L(x)
\right)\mathcal U(x)
\right].
}
\tag{1}
\]

The two auxiliary exponential polynomials are

\[
\begin{aligned}
\mathcal U(x)={}&
(2x^3-6x^2+12x-12)e^{7x}\\
&+(2x^5-25x^4+64x^3-96x^2+48x+60)e^{6x}\\
&+(32x^5-60x^4+6x^3+234x^2-396x-108)e^{5x}\\
&+(-24x^6+44x^5+33x^4-232x^3+120x^2+840x+60)e^{4x}\\
&+(-56x^5+152x^4-2x^3-690x^2-780x+60)e^{3x}\\
&+(-14x^5-39x^4+336x^3+576x^2+288x-108)e^{2x}\\
&+(-8x^5-60x^4-166x^3-114x^2+12x+60)e^x\\
&-x^4-8x^3-24x^2-24x-12,
\end{aligned}
\tag{2}
\]

and

\[
\begin{aligned}
\mathcal P(x)={}&12e^{7x}
+(-2x^3+24x^2-108x-60)e^{6x}\\
&+(-x^5+13x^4-74x^3+192x^2+504x+108)e^{5x}\\
&+(-19x^5+77x^4-132x^3-960x^2-900x-60)e^{4x}\\
&+(12x^6-34x^5+42x^4+828x^3+1440x^2+720x-60)e^{3x}\\
&+(4x^6-14x^5-358x^4-922x^3-840x^2-180x+108)e^{2x}\\
&+(8x^6+67x^5+217x^4+270x^3+96x^2-72x-60)e^x\\
&+x^5+9x^4+32x^3+48x^2+36x+12.
\end{aligned}
\tag{3}
\]

Identity `(1)` is useful because the logarithm occurs only through the elementary positive gap

\[
\frac{y}{1-y}+\log(1-y)
=
\frac{y}{1-y}-[-\log(1-y)]>0,
\qquad 0<y<1.
\tag{4}
\]

Indeed `(4)` follows termwise from

\[
\frac{y}{1-y}=\sum_{n\ge1}y^n,
\qquad
-\log(1-y)=\sum_{n\ge1}\frac{y^n}{n},
\]

with strict inequality because all coefficients from `n=2` onward are strictly larger in the first series.

Thus `(1)` will be strictly positive once

\[
\boxed{\mathcal U(x)>0,\qquad \mathcal P(x)>0\qquad(x>0).}
\tag{5}
\]

The rest of the proof establishes `(5)` exactly.

## 3. Positivity of `mathcal U`

Write the Maclaurin expansion

\[
\mathcal U(x)=\sum_{n\ge0}u_n\frac{x^n}{n!},
\qquad
u_n:=\mathcal U^{(n)}(0).
\]

Direct differentiation of the explicit exponential polynomial `(2)` gives

\[
\nu_0=\cdots=\nu_{12}=0.
\tag{6}
\]

For `13<=n<=99`, exact integer evaluation of the derivative formula gives

\[
\nu_n>0,
\qquad
\min_{13\le n\le99}\nu_n
=\nu_{13}=103783680.
\tag{7}
\]

This finite check is exact arithmetic on `(2)`, not floating-point evidence.

For the infinite tail, differentiate each `P(x)e^{kx}` term in `(2)`. For `n>=100`, the `k=5,6,7` contributions are nonnegative. The `k=7` contribution is

\[
\nu_n^{(7)}
=
\frac{2\,7^n}{343}
\bigl(n^3-24n^2+317n-2058\bigr)
\ge
\frac{7^n n^3}{343}.
\tag{8}
\]

The four potentially negative lower-base contributions satisfy the elementary bounds

\[
|\nu_n^{(1)}|\le10n^5,
\qquad
|\nu_n^{(2)}|\le\frac12\,2^n n^5,
\]

\[
|\nu_n^{(3)}|\le\frac13\,3^n n^5,
\qquad
|\nu_n^{(4)}|\le\frac1{128}\,4^n n^6.
\tag{9}
\]

For example, `(8)` follows from

\[
n^3-24n^2+317n-2058\ge\frac12n^3
\]

for `n>=100`; the bounds in `(9)` follow by dividing each exact coefficient polynomial by its leading power of `n` and using `n>=100`. The `k=5` polynomial is positive already under the coarse lower bound

\[
16n^5-310n^4-136941n-168750>0,
\]

and the `k=6` polynomial is positive under

\[
n^5-85n^4-14699n^2>0.
\]

Relative to the lower bound in `(8)`, the sum of the four bounds in `(9)` is at most

\[
\frac{3430n^2}{7^n}
+
\frac{343}{2}n^2\left(\frac27\right)^n
+
\frac{343}{3}n^2\left(\frac37\right)^n
+
\frac{343}{128}n^3\left(\frac47\right)^n.
\tag{10}
\]

Each term in `(10)` is decreasing for `n>=100`, and at `n=100` their sum is less than `1.34 x 10^{-18}`. Hence the positive `k=7` contribution alone strictly dominates all potentially negative lower-base terms for every `n>=100`. Therefore

\[
\nu_n>0\qquad(n\ge13).
\tag{11}
\]

Together with `(6)`,

\[
\boxed{\mathcal U(x)>0\qquad(x>0).}
\tag{12}
\]

## 4. Positivity of `mathcal P`

Similarly write

\[
\mathcal P(x)=\sum_{n\ge0}p_n\frac{x^n}{n!},
\qquad
p_n:=\mathcal P^{(n)}(0).
\]

From `(3)`,

\[
p_0=\cdots=p_9=0.
\tag{13}
\]

Exact integer evaluation on the finite range gives

\[
p_n>0\quad(10\le n\le99),
\qquad
\min_{10\le n\le99}p_n
=p_{10}=1209600.
\tag{14}
\]

For `n>=100`, the `k=1,2,3` derivative contributions are positive by the direct lower bounds on their coefficient polynomials

\[
8n^6-53n^5-487n^3-282n-60>0,
\]

\[
n^6-22n^5-203n^4-166n^3-1142n^2>0,
\]

\[
2n^6-47n^5-7290>0.
\tag{15}
\]

The positive `k=7` contribution is exactly

\[
p_n^{(7)}=12\,7^n.
\tag{16}
\]

The only contributions that need to be dominated may be bounded by

\[
|p_n^{(4)}|
\le\frac{25}{1024}n^5 4^n,
\qquad
|p_n^{(5)}|
\le\frac{3}{3125}n^5 5^n,
\]

\[
|p_n^{(6)}|
\le\frac1{54}n^3 6^n.
\tag{17}
\]

For `n>=100`, each right-hand side in `(17)` is less than `4\,7^n`. At `n=100`, after division by `4\,7^n`, the three ratios are respectively less than

\[
3.1\times10^{-17},
\qquad
5.9\times10^{-9},
\qquad
9.4\times10^{-4},
\tag{18}
\]

and each ratio decreases thereafter because its exponential base ratio is respectively `4/7`, `5/7`, or `6/7`, while its polynomial factor grows only as `n^5` or `n^3`.

Therefore the `12\,7^n` term strictly dominates the entire potentially negative tail, while the lower-base positive terms only increase the coefficient. Hence

\[
p_n>0\qquad(n\ge10),
\tag{19}
\]

and

\[
\boxed{\mathcal P(x)>0\qquad(x>0).}
\tag{20}
\]

## 5. The fourth confluent determinant is strictly positive

Every prefactor in `(1)` is positive for `x>0`. Equations `(4)`, `(12)`, and `(20)` therefore imply

\[
\boxed{H_4(t)>0\qquad(t\in\mathbb R).}
\tag{21}
\]

Combining `(21)` with AF-218/AF-219 gives the complete strict confluent flag

\[
H_1(t),H_2(t),H_3(t),H_4(t)>0
\qquad(t\in\mathbb R).
\tag{22}
\]

AF-403 applies directly to `(22)` and yields strict total positivity of `K(u,v)=f(u-v)` through order four for arbitrary separated row and column nodes.

Returning to Euler variables uses

\[
v_q=-\log\log q,
\qquad
K(\log s,v_q)=E_s(q).
\]

Increasing `q` reverses the `v` ordering. Reversing `m` columns contributes `(-1)^{m(m-1)/2}`, giving the stated checkerboard sign through `m=4`.

## 6. Arithmetic-fidelity consequence

AF-217 established a qualitative all-order obstruction: nontrivial zeta zeros force some finite failure of full-Euler total positivity. AF-218 and AF-219 then showed that the failure does not occur at orders two or three. The present result moves the exact boundary again:

\[
\boxed{
\text{full Euler aggregation preserves ordered-sign fidelity through order }4,
\text{ but not through all orders.}
}
\tag{23}
\]

So a source class with at most three ordered sign changes retains an exact four-sample collision barrier after **all** Euler harmonics have been aggregated. This is stronger than the first-harmonic theorem in the sense that it is genuinely full Euler, but weaker than an all-order variation-diminishing law.

The result is deliberately source-agnostic. Rational primes can be used as source nodes, but primality is not what forces `(23)`: the finite-order fidelity is a property of the Euler-log observation kernel itself. Any RH-facing use still needs a separate arithmetic theorem forcing the relevant discrepancy into a bounded-sign source class.

## Prior art and novelty audit

The globalization step is classical ECT/total-positivity theory and is already isolated in AF-403, with Karlin--Studden and Karlin as standard references. The Toda/Hankel reduction used to identify the local order-four frontier is classical and is already audited in AF-404. AF-217 records Schoenberg's classical Pólya-frequency theorem and Gröchenig's modern zeta/total-positivity bridge.

A targeted search for the exact Euler-log profile `L(e^t)`, its finite Pólya-frequency order, and the transform `Gamma(w) zeta(w+1)` did not locate a prior theorem asserting `PF_4`/`STP_4` for this specific kernel. That absence is not a novelty proof, so no novelty is claimed here. The durable statement is the explicit exact order-four certificate `(1)`--`(22)` and its placement inside the already-audited classical finite-order framework.

## Controls and boundaries

- **Not all-order positivity.** AF-217 remains decisive: some finite order fails. AF-405 only raises the first possible failure from four to five.
- **Finite exact arithmetic is part of the proof.** Equations `(7)` and `(14)` are finite exact checks of explicit integer formulas, followed by analytic dominance for the infinite tails. They are not numerical sampling of `H_4` over `x`.
- **No conditioning theorem.** Strict positivity can become arbitrarily small in asymptotic regimes. AF-405 proves sign fidelity, not a uniform determinant margin.
- **No arithmetic discriminator is created.** The proof works for arbitrary positive generator norms. A prime-specific application must supply additional source structure independently.
- **AF-403's complete-flag hypothesis is satisfied, not bypassed.** Lower orders are supplied by AF-218/AF-219 and order four by `(21)`; arbitrary-node positivity is not inferred from `H_4` alone.
- **The exact first failing order remains open.** AF-217 gives existence of a finite bad order but does not identify it. After AF-405 the next unresolved local gate is `H_5`, equivalently the next Toda/log-concavity condition for `H_4`.