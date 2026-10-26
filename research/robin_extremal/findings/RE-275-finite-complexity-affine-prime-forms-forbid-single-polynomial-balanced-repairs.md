# RE-275 — Finite-complexity affine prime forms forbid balanced repairs with one nonlinear insertion

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-FACTORIZATION-MECHANISM; independent adversarial review pending.

**Dependencies:** RE-274 (the conditional positive triple and its prime-supply boundary), RE-262 (the distinct integer valuation/counting obstruction). The algebraic theorem below is proved independently.

RE-274 obtains a positive reciprocal-height excursion from an identity with three affine deletion labels, two affine insertion labels, and one cubic insertion. Its three prescribed prime forms have parallel linear parts, so their simultaneous prime supply is not covered by the finite-complexity linear-equations-in-primes theorem. Adding parameter directions while retaining this polynomial shape cannot remove that obstacle: **with pairwise nonparallel deletion forms and no increase in the number of labels, every exact repair having at most one nonlinear polynomial insertion is trivial**.

This is an obstruction to a class of universal polynomial constructions. It does not rule out integer repairs chosen separately at individual parameters, rational insertion formulas with an additional integrality argument, or constructions with several nonlinear insertions. It supplies no Robin sign theorem for ordinary primes.

## 1. Exact polynomial statement

Work in
\[
R=\mathbb Q[X_1,\ldots,X_d],\qquad F(Z)=\frac{Z}{Z-1}.
\]
Let `L_1,...,L_k` be nonconstant affine polynomials whose nonzero gradients are pairwise nonproportional. Let `1<=m<=k`, let `A_1,...,A_(m-1)` be nonconstant affine polynomials, and let `C` be any nonconstant polynomial, with no degree bound. An empty list of `A_j` is permitted. Suppose the following equality holds in the fraction field of `R`:
\[
\prod_{i=1}^k F(L_i)
=F(C)\prod_{j=1}^{m-1}F(A_j).
\tag{1}
\]
Then
\[
\boxed{m=k,\qquad
\{A_1,\ldots,A_{k-1},C\}=\{L_1,\ldots,L_k\}
\text{ as polynomial multisets}.}
\tag{2}
\]
In particular `C` is affine after all. No positivity, primality, integer-valuedness, ordering, or bounded coefficients are assumed in this algebraic statement. Repeated insertions are allowed in the hypothesis and excluded by the conclusion.

Pairwise nonproportional gradients are stronger than distinct forms or nonproportional affine polynomials: `X` and `X+2` fail the hypothesis. This is precisely the pairwise condition relevant to finite-complexity prime systems.

## 2. Factorization proof

Clearing denominators in (1) gives
\[
\left(\prod_iL_i\right)(C-1)\prod_j(A_j-1)
=C\left(\prod_jA_j\right)\prod_i(L_i-1).
\tag{3}
\]

**First, `C-1` splits into affine factors over the rationals.** The polynomials `C` and `C-1` are coprime. Unique factorization in `R`, applied to (3), therefore gives
\[
C-1\ \bigm|\ \prod_j A_j\prod_i(L_i-1).
\tag{4}
\]
Every factor on the right is affine and nonconstant. Since `C-1` is nonconstant, it has at least one affine factor, and all its irreducible factors are affine.

**Second, a deleted form must divide `C`.** Each irreducible `L_i` divides the right side of (3). It cannot divide any `L_h-1`: for `h=i` the difference is one, and for `h!=i` the gradients are nonparallel. Thus every `L_i` divides `C` or one of the `A_j`. One affine `A_j` can be divisible by at most one of the pairwise nonassociate `L_i`. There are at most `k-1` such `A_j`, so some `L_s` divides `C`.

**Third, `C` depends on the single affine coordinate `L_s`.** Write `C=L_s H`. For any affine irreducible factor `ell` of `C-1`, reduce this equality modulo `ell`:
\[
\overline{L_s}\,\overline H=1
\quad\text{in}\quad
R/(\ell)\simeq\mathbb Q[Y_1,\ldots,Y_{d-1}].
\tag{5}
\]
The units of this polynomial ring are the nonzero rational constants. Hence `L_s` is a nonzero constant modulo `ell`. Since both polynomials are affine and nonconstant, their gradients are proportional; equivalently,
\[
\ell=u_\ell L_s+v_\ell,
\qquad u_\ell\ne0.
\]
All factors in (4) that occur in `C-1` consequently depend only on `L_s`. Therefore
\[
C\in\mathbb Q[L_s].
\tag{6}
\]
No `L_i` with `i!=s` divides `C`: modulo such an `L_i`, the coordinate `L_s` remains nonconstant affine, and a nonzero univariate polynomial in it remains nonzero. The same observation shows that no `L_i-1`, `i!=s`, divides `C` or `C-1`.

**Fourth, counting and poles force each remaining insertion to be unchanged.** Every `L_i`, `i!=s`, must divide an affine insertion. They require distinct insertions, so
\[
k-1\le m-1\le k-1.
\]
Thus `m=k`; relabel the insertions by these indices and write
\[
A_i=c_i L_i,\qquad c_i\in\mathbb Q^\times,
\qquad i\ne s.
\tag{7}
\]
Consider the valuation of the rational-function identity (1) at the irreducible polynomial `L_i-1`. Its left side has valuation `-1`. On the right, `F(C)` has valuation zero by (6), and all `F(A_h)` with `h!=i` have valuation zero by nonparallel gradients. The numerator `c_i L_i` is nonzero modulo `L_i-1`; its denominator reduces to `c_i-1`. It supplies the required pole only if `c_i=1`. Hence every `A_i=L_i`.

Cancel those common factors in (1). The remaining equation is
\[
\frac C{C-1}=\frac{L_s}{L_s-1},
\]
which gives `C=L_s` by cross multiplication. This proves (2).

The proof also covers `k=1`: there are no other gradients to compare, and injectivity of `F` gives the conclusion directly. For `d=1`, pairwise nonparallel gradients permit only this case.

## 3. Consequence for the positive triple construction

The RE-274 identity is
\[
\begin{gathered}
r=14t+1,\quad s=42t+1,\quad u=140t+1,\\
a=15t+1,\quad b=28t+1,\quad c=rsu,\\
F(r)F(s)F(u)=F(a)F(b)F(c).
\end{gathered}
\tag{8}
\]
Its deletion gradients are all parallel. By (2), there is no nontrivial universal identity of the same type with three pairwise nonparallel affine deletion forms, two affine insertion forms, and one polynomial insertion of **any** degree. Allowing more parameters, higher compensator degree, or a polynomial multiplier in the final product does not help within this class. The theorem does not require that the final insertion equal the product of the deletions.

More generally, a nontrivial universal polynomial repair with `m<=k`, nonconstant insertion labels, and finite-complexity affine deletion forms must have **at least two insertions of degree at least two**. This is a necessary condition, not a construction or a sufficiency result. No conclusion about the sign of those possible repairs is asserted.

This distinguishes two independent resources. A prime theorem may provide many realizations of a nondegenerate affine system, but the exact Euler identity must first exist on that system. Here it fails algebraically before any prime counting is invoked. The one-variable admissible-panel method in RE-264--RE-265 lies outside the nonparallel hypothesis and is unaffected.

## 4. Boundary controls and exact diagnostics

The restrictions are material.

- **Parallel forms:** (8) is nontrivial and exactly matched. Its certificate is `rsu-1=196t(15t+1)(28t+1)`. The prime instances and positive excursion are those of RE-274; the present result does not alter their conditional supply boundary.
- **Rational insertion:** for independent indeterminates `x,y`,
  \[
  F(x)F(y)=F\!\left(\frac{xy-1}{x+y-2}\right)F(xy).
  \tag{9}
  \]
  The first insertion is a rational function rather than a polynomial. At integer prime arguments its integrality and compositeness remain separate arithmetic conditions. In particular, (9) does not supply a finite-complexity integer repair automatically.
- **Count increase:** the exact identity `F(x)=F(x+1)F(x^2)` uses one affine and one nonlinear insertion but increases the count from one to two. At odd prime values both insertions are composite. This lies outside `m<=k`.
- **Pointwise equality:** equality on isolated parameter values or a proper algebraic subvariety need not be the rational-function identity (1). An affine reparametrization of such a subvariety must have its gradients checked anew; a nonlinear parametrization can leave the theorem's class entirely. Mere infinitude of matching specializations does not justify (1).

A supplementary exact two-variable diagnostic took `L_1=x`, `L_2=y` and all 336 nonconstant affine forms
\[
A=\alpha x+\beta y+\gamma,\qquad
\alpha,\beta,\gamma\in\{-2,-1,-1/2,0,1/2,1,2\}.
\]
Solving the equality for the remaining insertion gives
\[
C=\frac{xy(A-1)}{A(x+y-1)-xy}.
\tag{10}
\]
Exact division in `Q[x,y]` found a polynomial `C` only for `(A,C)=(x,y),(y,x)`. The check used rational-coefficient sparse polynomial arithmetic with lexicographic division and verified `numerator=quotient*denominator+remainder` for every case. It is a finite stress test, not the proof of (2).

Exact rational arithmetic also checked (8) for `1<=t<=1000`, the count-increasing identity for `2<=x<=1001`, and (9) for all `2<=x,y<=51`. Their general validity follows by cross multiplication; no simultaneous-primality claim was inferred from these checks. No floating-point estimate or Lean proof is used.

## 5. Prior art and evidence boundary

Unique factorization, the units of a polynomial ring over a field, restriction to an affine hyperplane, and irreducible-divisor valuations are classical algebra. The proof above records the complete elementary application; no novelty is claimed for those tools or for (9).

Ben Green and Terence Tao, [*Linear equations in primes*, Annals of Mathematics **171** (2010), 1753--1850](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf), Lemma 1.6, identifies finite complexity with the absence of pairwise affine dependence. Their terminology means pairwise nonparallel linear parts, as also stated in Lemma 1.3. Tamar Ziegler's [*Linear equations in primes and dynamics of nilmanifolds*](https://arxiv.org/pdf/1404.0775), Theorem 1.1 and footnote 2, gives the subsequent finite-complexity prime-counting theorem and explains the same boundary. These sources identify the proposed prime-supply route; they are not inputs to the algebraic proof and do not prove a prime-tuple conjecture for (8).

Targeted comparison with polynomial Euler-factor replacements, totient-ratio identities, products of affine factors minus one, and finite-complexity prime systems did not locate this repair-specific rigidity statement. That search does not establish global novelty. The durable delta is the exact exclusion of a universal polynomial replacement strategy for the unproved prime supply in RE-274, including arbitrary compensator degree and arbitrary fixed label count. It is different from RE-262's pointwise prime-valuation obstruction: no prime divisibility relations at specialized integer arguments enter this proof.

The result remains confined to a synthetic-source construction class. It does not imply that the RE-274 prime-supply hypothesis is necessary for all positive critical-budget repairs, that several nonlinear insertions suffice, or that arbitrary finite balanced integer sources obey a positive-excursion bound. It supplies no CA realization, selected ordinary-prime tail estimate, Robin counterexample, or RH conclusion.
