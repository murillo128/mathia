# RE-276 — Affine-direction count forbids all balanced polynomial Euler repairs

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-PARTIAL-FRACTION-MECHANISM; independent adversarial review pending.

**Dependency:** RE-274 supplies the motivating conditional positive triple and its prime-supply boundary. The algebraic theorem here is proved independently.

A universal polynomial repair of `k` affine Euler labels with pairwise nonparallel gradients must contain **at least `k` affine insertion labels**, regardless of how many nonlinear polynomials are allowed or their degrees. Consequently every such repair with at most `k` insertions is trivial. Several nonlinear compensators cannot make a balanced construction compatible with the finite-complexity affine prime-supply regime.

The stronger invariant is a sharp count: if there are `h` nonlinear insertions, there must be at least `k+h` total insertions. This closes the polynomial-construction escape completely under the stated nonparallel hypothesis. Rational labels, identities restricted to a proper parameter subvariety, and pointwise integer repairs remain outside it. The theorem is an elementary consequence of first-order scaling and classical independence of reciprocal linear forms, not a new prime theorem or a Robin sign result.

## 1. Statement and exact count

Let
\[
R=\mathbb Q[X_1,\ldots,X_d],\qquad F(Z)=\frac Z{Z-1},
\]
where `d>=1`, and fix integers `k,m>=1`. Let
\[
L_i=\ell_i+b_i,\qquad 1\le i\le k,
\]
be nonconstant affine polynomials, with nonzero homogeneous linear parts `ell_i` that are pairwise nonproportional. Let `P_1,...,P_m` be arbitrary nonconstant polynomials. Suppose
\[
\prod_{i=1}^k F(L_i)=\prod_{j=1}^m F(P_j)
\quad\text{in }\operatorname{Frac}(R).
\tag{1}
\]
Write `a=#{j:deg P_j=1}` and `h=#{j:deg P_j>=2}`, so `m=a+h`. Then
\[
\boxed{a\ge k,\qquad m\ge k+h.}
\tag{2}
\]
If `m<=k`, necessarily
\[
\boxed{m=k,\qquad \{P_1,\ldots,P_k\}
=\{L_1,\ldots,L_k\}\text{ as polynomial multisets}.}
\tag{3}
\]
No positivity, primality, integrality, insertion distinctness, coefficient bound, or degree bound is required. Pairwise nonproportional does **not** mean that all `ell_i` are linearly independent: there may be arbitrarily many distinct directions even when `d=2`. In one variable the hypothesis permits only `k=1`.

## 2. Scaling isolates the affine labels

Introduce a formal variable `z` and work over the coefficient field
`K=Q(X_1,...,X_d)`. For a nonconstant polynomial `P` of total degree `r`, let `P_r` denote its top homogeneous part. Then
\[
P(X/z)=z^{-r}\bigl(P_r(X)+zP_{r-1}(X)+\cdots\bigr).
\]
Since `P_r` is nonzero in `K`, formal inversion gives
\[
F(P(X/z))=1+\frac1{P(X/z)-1}
=1+\frac{z^r}{P_r(X)}+O(z^{r+1}).
\tag{4}
\]
Here `O(z^s)` means membership in `z^s K[[z]]`. This is a formal coefficient calculation; there is no numerical limit or assertion uniform over rays on which a leading homogeneous part vanishes.

Every factor has constant term one. Taking the coefficient of `z` in (1), and writing `p_j` for the homogeneous linear part of an affine `P_j`, yields
\[
\boxed{\sum_{i=1}^k\frac1{\ell_i}
=\sum_{\deg P_j=1}\frac1{p_j}.}
\tag{5}
\]
All nonlinear insertion labels disappear from this identity. Products of their corrections cannot contribute at order one either.

We use the elementary fact that for pairwise nonproportional nonzero linear forms `lambda_1,...,lambda_s` and every fixed integer `q>=1`,
\[
\sum_{v=1}^s\frac{c_v}{\lambda_v^q}=0,\quad c_v\in\mathbb Q
\quad\Longrightarrow\quad c_v=0\text{ for every }v.
\tag{6}
\]
Multiply by `prod_v lambda_v^q` and reduce modulo `(lambda_u)`. All summands except the `u`th vanish. The quotient by this nonzero linear polynomial is an integral domain; all the other linear forms remain nonzero there. Thus `c_u=0`. This proves (6), including `s=1`.

Group the denominators in (5) by proportionality class. If `p_j=c_j ell_i` in the class of `ell_i`, (6) gives
\[
\sum_{j:p_j\parallel\ell_i}\frac1{c_j}=1.
\tag{7}
\]
Every one of the `k` classes must therefore contain an affine insertion. These classes are disjoint, proving `a>=k` and (2). Extra insertion directions can have cancelling coefficients, but cannot replace any required class. The argument does not assume that those coefficients are positive.

## 3. Equality forces the original labels, including their constants

If `m<=k`, (2) implies `a=m=k` and `h=0`. There is precisely one insertion in each deletion direction and none elsewhere. Equation (7) makes its proportionality constant exactly one. After relabelling,
\[
P_i=\ell_i+c_i.
\]
To recover the affine constants, expand one order further:
\[
F(\ell_i/z+b_i)
=1+\frac z{\ell_i}
+\frac{(1-b_i)z^2}{\ell_i^2}+O(z^3).
\tag{8}
\]
The cross terms `sum_(i<j)1/(ell_i ell_j)` agree in the two products because the linear parts have already been matched. Equality of the second coefficients therefore gives
\[
\sum_i\frac{c_i-b_i}{\ell_i^2}=0.
\tag{9}
\]
Apply (6) with `q=2`: `c_i=b_i` for every `i`. This proves (3). First-order data alone determine the direction count and slopes; the second order is needed to fix the additive constants.

## 4. Sharpness and boundaries

**The count in (2) is sharp for every number of nonlinear labels.** The rational identity
\[
F(Z)=F(Z+1)F(Z^2)
\]
iterates, for any integer `h>=1`, to
\[
F(Z)=F(Z+h)\prod_{r=0}^{h-1}F((Z+r)^2).
\tag{10}
\]
Apply (10) to `L_1` and leave `L_2,...,L_k` unchanged. The result has exactly `k` affine insertions, `h` quadratic insertions, and `k+h` labels. It is nontrivial and attains (2). The elementary split follows by cancelling `(Z+1)(Z-1)=Z^2-1`; induction proves (10) for every `h`. This is polynomial sharpness, not an assertion that all its specialized labels are new composite integers at a desired prime tuple.

**Nonparallel gradients are essential.** RE-274 has the exact polynomial identity
\[
F(14t+1)F(42t+1)F(140t+1)
=F(15t+1)F(28t+1)F((14t+1)(42t+1)(140t+1)).
\tag{11}
\]
There are three deletions but only two affine insertions. All deletion gradients are parallel, so (5) supplies only one scalar direction equation. Indeed
\[
\frac1{14}+\frac1{42}+\frac1{140}
=\frac1{15}+\frac1{28}.
\]
Its nontrivial balanced identity is compatible with the invariant. RE-274's prime-supply hypothesis remains unproved and unaffected.

**A rational label can carry several first-order pole directions.** For independent `x,y`,
\[
F(x)F(y)
=F\!\left(\frac{xy-1}{x+y-2}\right)F(xy).
\tag{12}
\]
The first insertion is rational, with homogeneous scaling term `xy/(x+y)`. Its reciprocal is `1/x+1/y`, exactly the two required directions. This explains why the polynomial hypothesis cannot be dropped: a degree-one polynomial has only one linear pole direction, while a rational label of scaling degree one need not. Cross multiplication proves (12). At prime integer arguments, integrality and composite/distinct insertion constraints remain separate requirements; (12) alone does not supply an unconditional balanced integer family.

**Specialization is a genuine boundary.** An identity on a proper algebraic subvariety need not be (1). Restricting parameter space may turn nonparallel linear parts into parallel ones, or turn polynomial labels into rational ones after solving constraints. Infinitely many matching specializations are insufficient to infer (1) unless they are Zariski dense in the full parameter space. Likewise, scaling along one exceptional numerical ray can lower total degree; (4) deliberately keeps `X` indeterminate.

## 5. Exact audit and prior art

The proof is the formal expansion (4), the pole-separation argument (6), and the equality calculation (8)--(9). It does not depend on finite search. Supplementary exact rational-arithmetic checks tested:

- (10), by sparse polynomial cross multiplication in `Q[x,y]`, for `h=1,...,5` with deletion forms `x+2`, `y+3`, `x+y+5`;
- the full bivariate rational identity (12) and the univariate parallel control (11), again by polynomial cross multiplication;
- rank `k` of the numerator families obtained by clearing denominators in (6), for `lambda_i=x+i y`, `0<=i<k`, `1<=k<=8`, and `q=1,2` (16 exact rank checks);
- 196 formal expansions through order two, for degrees `1,...,7`, leading coefficients in `{-3,-1,1,2}`, and constant terms in `{-3,...,3}`. For degree above one the tested polynomial was `a T^r+2T^(r-1)+b`; for degree one it was `aT+b`. Division of the reversed numerator and denominator confirmed the first coefficient `1/a` only at degree one, and the second coefficient `(1-b)/a^2`, `1/a`, or zero at degrees one, two, or at least three respectively.

All checks passed. They use neither floating-point estimates nor primality assumptions and are not a Lean proof.

Reciprocal-linear-form independence is classical. Hiroaki Terao, [*Algebras generated by reciprocals of linear forms*, Journal of Algebra **250** (2002), 549--558](https://arxiv.org/pdf/math/0105095), Definition 1.1 and Proposition 2.1, studies the graded algebra of these reciprocals and decomposes it by intersections of the hyperplanes. Equation (6) is an elementary instance of that separation; the direct proof above is sufficient. No novel general partial-fraction or hyperplane-arrangement theorem is claimed.

For the prime-supply comparison, Ben Green and Terence Tao, [*Linear equations in primes*, Annals of Mathematics **171** (2010), 1753--1850](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p08-p.pdf), Lemmas 1.3 and 1.6, identify the finite-complexity condition with pairwise nonparallel linear parts. Tamar Ziegler's [*Linear equations in primes and dynamics of nilmanifolds*](https://arxiv.org/pdf/1404.0775), Theorem 1.1 and footnote 2, states the resulting prime-counting theorem and explains this convention. No prime-counting result is used in proving (2)--(3).

Comparison with reciprocal-linear-form algebras, polynomial Euler-factor replacements, and totient-ratio identities identifies the proof mechanism as classical. The repair-specific consequence is derived here; absence of an identical formulation from the targeted search is not a global novelty claim.

## 6. Consequence for the Robin source construction

For the finite source repairs motivated by RE-274, count balance and a universal polynomial identity are incompatible with nonparallel deletion gradients unless every label remains unchanged. Increasing the number or degree of nonlinear compensators cannot help: each is an additional label beyond the `k` affine insertions already forced by (5). Thus a finite-complexity prime theorem cannot rescue a balanced polynomial construction of this type, even if it supplies abundant prime parameters.

The theorem does not say that the prime-tuple hypothesis in RE-274 is necessary for every positive critical-budget repair. A rational construction with an independent integrality theorem, a different parameter variety, or repairs selected at individual prime tuples could evade this obstruction. Parallel-form admissible panels are not excluded. These alternatives need their own source and sign arguments.

The result concerns synthetic Euler atoms `F(P)`, not ordinary divisor-sum factors of composite integers. It gives no CA realization, selected-prime tail estimate, ordinary-prime Robin counterexample, or RH conclusion.
