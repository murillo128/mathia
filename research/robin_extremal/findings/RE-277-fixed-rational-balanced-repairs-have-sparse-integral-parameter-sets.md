# RE-277 — Fixed rational balanced repairs have sparse integral parameter sets

**Status:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION + CLASSICAL-DIVISIBILITY-MECHANISM; independent adversarial review pending.

**Dependency:** RE-276 supplies the polynomial repair rigidity theorem. The rational integrality estimate below is proved independently.

Rational labels evade RE-276's polynomial identity obstruction, but do not provide a repair on a positive fraction of the ambient affine prime tuples. For every fixed nontrivial balanced rational repair of pairwise nonparallel affine deletion labels, the integer-valued parameter set in `[-N,N]^d` has size `O_epsilon(N^(d-1+epsilon))`. This is much smaller than the full-dimensional affine prime supply `N^d/(log N)^k`.

This is a density obstruction, **not a nonexistence theorem**. Sparse integer solutions can be infinite and Zariski dense. Their prime supply needs a separate argument; the bound does not exclude enough solutions for a Robin-critical construction. No new general theorem about rational functions or prime distribution is claimed.

## 1. Repair theorem

Fix nonconstant affine polynomials
\[
L_i=\ell_i+b_i\in\mathbb Q[X_1,\ldots,X_d],\qquad 1\le i\le k,
\]
whose nonzero homogeneous linear parts are pairwise nonproportional. Put `F(Z)=Z/(Z-1)`. Fix `m<=k` nonconstant rational functions `R_1,...,R_m` such that
\[
\prod_{i=1}^k F(L_i)=\prod_{j=1}^m F(R_j)
\quad\text{in }\mathbb Q(X_1,\ldots,X_d).
\tag{1}
\]
Call (1) trivial when `m=k` and the two label multisets are equal as rational functions. For a nontrivial identity define
\[
\mathcal I(N)=\{n\in\mathbb Z^d:\|n\|_\infty\le N,
\ R_j(n)\text{ is defined and integral for every }j\}.
\]
Then, for every fixed `epsilon>0`,
\[
\boxed{\#\mathcal I(N)\ll_{R_1,\ldots,R_m,\epsilon}N^{d-1+\epsilon}.}
\tag{2}
\]
For `d=1`, the set of such parameters is actually finite. Bounds remain valid after imposing prime deletions, composite insertions, positivity, distinctness, prefix preservation, or fixed congruences, since these only select subsets. The same bound holds for any fixed finite menu of nontrivial identities.

Indeed, if every `R_j` were a polynomial, RE-276 would force triviality. At least one `R_j` is a nonpolynomial rational function. Its integer-valued inputs already satisfy the lemma in the next section; no simultaneous divisibility independence is required.

All formulas, coefficients, the menu size and `d,k,m` are fixed before `N` tends to infinity. The implicit constant is not asserted to be uniform in a growing or changing family. Constant insertion functions are outside the statement, just as in RE-276.

## 2. Integer values of one rational function

**Lemma.** If `R=A/B` is a nonpolynomial element of `Q(X_1,...,X_d)`, then
\[
\#\{n\in[-N,N]^d\cap\mathbb Z^d:B(n)\ne0,\ R(n)\in\mathbb Z\}
\ll_{R,\epsilon}N^{d-1+\epsilon}.
\tag{3}
\]
Use a reduced presentation with `A,B` in `Z[X]`, coprime over `Q[X]`, and `B` nonconstant. Choose a variable `t` in which `B` has positive degree `r`, and denote the remaining variables by `y`. Gauss's lemma makes `A,B` coprime in `Q(y)[t]`. A Bezout identity over that field, after clearing all denominators, gives
\[
U(t,y)A(t,y)+V(t,y)B(t,y)=D(y),
\quad U,V\in\mathbb Z[t,y],\quad0\ne D\in\mathbb Z[y].
\tag{4}
\]
One may also use a nonzero resultant in `t`. Let `c(y)` be the leading coefficient of `B` in `t`.

Fix an integer `y` with `D(y)c(y) != 0`. If `A(t,y)/B(t,y)` is an integer and `B(t,y) != 0`, (4) implies
\[
B(t,y)\mid D(y).
\tag{5}
\]
There are `2 tau(|D(y)|)` signed divisors. For each divisor `e`, the nonconstant degree-`r` polynomial equation `B(t,y)=e` has at most `r` integer roots. Consequently this fiber has at most
\[
2r\tau(|D(y)|)
\tag{6}
\]
admissible values of `t`, even without restricting their size.

For every `delta>0`, the elementary divisor bound is `tau(q) <<_delta q^delta`. To see it directly, write `q=prod p^a`. For sufficiently large primes, `a+1<=2^a<=p^(delta a)`; for each of the finitely many smaller primes, `sup_(a>=0) (a+1)/p^(delta a)` is finite. Multiplication proves the bound. Since the fixed polynomial `D` has `|D(y)| << (1+N)^M` on the box, choose `delta=epsilon/max(M,1)`. Equation (6), summed over the `O(N^(d-1))` nonexceptional fibers, contributes `O(N^(d-1+epsilon))`.

For `d>=2`, the nonzero polynomial `D(y)c(y)` vanishes at `O(N^(d-2))` integer points of the `(d-1)`-dimensional box. This elementary polynomial zero bound follows by induction: use the one-variable root bound outside the zero set of a nonzero leading coefficient, and count the exceptional fibers trivially. Each exceptional `y` has only `O(N)` possible `t` in the box. Their total contribution is `O(N^(d-1))`. In particular, neither cancellation after specialization nor a drop of the denominator degree has been discarded.

If `d=1`, `D` and `c` in (4) are nonzero constants. There are no exceptional fibers, and (6) is a fixed finite bound over all integers. This completes the lemma and (2).

## 3. What the affine prime theorem does and does not supply

Suppose, additionally, the `L_i` have integer coefficients and a fixed full-dimensional region has prime-tuple count
\[
\#\mathcal P(N)\asymp\frac{N^d}{(\log N)^k},
\qquad \mathcal P(N)\subseteq[-CN,CN]^d\cap\mathbb Z^d,
\tag{7}
\]
with fixed `C`, as in a locally admissible finite-complexity affine system in a region where the forms are positive and of size comparable to `N`. Then (2) gives, for every fixed `0<epsilon<1`,
\[
\frac{\#(\mathcal P(N)\cap\mathcal I(CN))}{\#\mathcal P(N)}
\ll N^{-1+\epsilon}(\log N)^k\longrightarrow0.
\tag{8}
\]
Thus even this full prime supply does not justify applying a fixed rational repair to a positive fraction of its tuples. Passing to any fixed full-rank congruence class with a positive prime-density constant does not change (8). The prime theorem counts the ambient tuples, whereas the missing source theorem must count those also satisfying (5).

The claim is deliberately limited. An upper bound of `N^(d-1+epsilon)` is not zero. For `d=2` and labels of order `N`, it remains larger than the `sqrt(N)/log N` number of repairs sought at a Robin-critical budget. The argument therefore does not exclude a sufficient sparse supply, establish a sign restriction, or show that RE-274's prescribed triple hypothesis is necessary. Nor does it identify every integral locus with one lower-dimensional algebraic variety.

## 4. A complete rational control: sparsity can coexist with Zariski density

RE-276's rational escape is
\[
F(x)F(y)=F\!\left(\frac{xy-1}{x+y-2}\right)F(xy).
\tag{9}
\]
For integers `x,y>=2`, its first insertion is integral exactly when
\[
x=1+t u(u+v),\qquad y=1+t v(u+v),
\quad t,u,v\in\mathbb Z_{\ge1},\quad\gcd(u,v)=1.
\tag{10}
\]
In that case the insertion equals `1+tuv`. Indeed, write `x-1=gu`, `y-1=gv` with coprime `u,v`. Then
\[
\frac{xy-1}{x+y-2}=1+\frac{g uv}{u+v}.
\]
Since `gcd(uv,u+v)=1`, integrality is equivalent to `g=t(u+v)`. This proves both necessity and sufficiency, with a unique ordered parametrization.

For `2<=x,y<=N`, the exact ordered-pair count is therefore
\[
\sum_{\substack{u,v\ge1\\(u,v)=1}}
\left\lfloor\frac{N-1}{\max(u,v)(u+v)}\right\rfloor.
\tag{11}
\]
Terms vanish unless `max(u,v)<=sqrt(N-1)`. For `v=max(u,v)`, there are at most `v` choices for `u`, each contributing at most `N/v^2`. Summing and doubling gives `O(N log N)`. Taking `u=1,v=2` already gives `Omega(N)` pairs. Hence the power `d-1` in (3) cannot be improved to `d-1-delta` uniformly over rational functions, for any fixed `delta>0`.

Nevertheless the integral locus in (10) is Zariski dense in the affine plane. For every coprime positive pair `u,v`, it contains infinitely many points on the line through `(1,1)` of slope `v/u`. A polynomial vanishing at every such point vanishes identically on each of infinitely many distinct lines, and hence is zero. Deleting the diagonal `u=v=1` does not affect this argument. This is density of **integer-valued algebraic controls**, not of prime-source repairs.

At `u=1,v=2,t=10`, (9) gives the genuine finite source repair
\[
\{31,61\}\longmapsto\{21,1891\},
\]
with two prime deletions and two distinct composite insertions, already present in RE-263. For fixed `u,v`, the two deletion labels in (10) are parallel affine forms in `t`. The parametrization thus explains how integral points can survive while leaving the original nonparallel prime-supply regime. No infinite prime supply for a prescribed pair in (10) is inferred.

## 5. Audit, prior art and consequence

The proof is exact and does not rely on search. Supplementary standard-library rational-arithmetic checks verified (9) at all `62001` ordered pairs `2<=x,y<=250`; the `510` integral pairs agreed exactly with enumeration by (10)--(11). They also recovered the `(31,61)` source control. These checks do not establish primality supply or asymptotics.

To audit the exceptional fibers in Section 2, two explicit Bezout identities were checked at all `|t|<=60`, `|y|<=30`:
\[
(t^2+y)-(t-y)(t+y)=y(y+1),
\qquad (yt+1)-y(t+y)=1-y^2.
\tag{12}
\]
All `14762` evaluations passed. On every nonexceptional fiber, integral quotient values satisfied (5) and the bound `2 tau(|D(y)|)` for the linear denominator. The first identity has `120` nonpole integral values at each of `y=-1,0`; the second has `120` at `y=-1,1` and `121` at `y=0`, where its denominator becomes constant. These are explicit checks that the exceptional contribution really can contain whole fibers. They are not a formal proof or an independent adversarial review.

The divisibility mechanism is classical. Arnaud Bodin, Pierre Debes and Salah Najib, [*Prime and coprime values of polynomials*, L'Enseignement Mathematique **66** (2020), 173--186](https://arnbod.github.io/fichiers/gcd22.pdf), Propositions 3.1--3.2, discuss the cleared Bezout identity and divisibility of common integer values. Arnaud Bodin and Pierre Debes, [*Coprime values of polynomials in several variables*, arXiv:2105.13883v3](https://arxiv.org/pdf/2105.13883), proof of Proposition 3.2, implication (ii) to (iii), gives the corresponding passage to `Q(y)[t]` and the nonzero polynomial `D(y)` after clearing denominators. The elementary divisor and fiber count above is supplied in full; no novelty is claimed for it or for the two-variable parametrization.

For (7), Tamar Ziegler, [*Linear equations in primes and dynamics of nilmanifolds*, arXiv:1404.0775](https://arxiv.org/pdf/1404.0775), Theorem 1.1 and footnote 2, states the finite-complexity prime theorem and its nonparallel convention. Neither that theorem nor the coprime-value density results assert prime supply subject to the full denominator divisibility (5). The prior-art comparison covers rational integer values, polynomial-value gcds, resultant divisibility and affine prime counting; it does not establish global novelty of the present formulation.

The line-specific delta is a quantitative restriction on the rational escape explicitly left by RE-276: any fixed nontrivial balanced rational construction must obtain its source supply from a set that loses almost one power of the ambient parameter scale. Fixed congruences or a fixed finite menu cannot restore the ambient prime-tuple density. This replaces a generic request for an integrality theorem by a sparse divisibility-conditioned prime-supply obligation, while preserving the possibility of such a theorem.

The result concerns synthetic Euler atoms `b/(b-1)`. It gives no ordinary composite divisor-sum identity, CA realization, selected-frontier signed-tail estimate, Robin counterexample, or RH conclusion. Changing formulas with the scale, extra insertion labels, parallel gradients, proper parameter subvarieties, and individually selected repairs remain separate regimes.
