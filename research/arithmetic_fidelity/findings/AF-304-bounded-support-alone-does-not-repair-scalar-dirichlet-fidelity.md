# AF-304 — Bounded support alone does not repair scalar Dirichlet fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SIMPLEX`, `SPARSITY`, `CARATHEODORY`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-303 leaves bounded support size as a possible way to stop the normalized positive fiber from building the barycentric cancellations used by the full simplex. Sparsity does reduce the fixed-point correction geometry, but **a fixed support bound is not, by itself, a uniform repair for coordinate deletion at one complex Dirichlet observation**.

Let

\[
\Delta_N^{\le k}
=
\left\{
 c\in\mathbb R_+^N:
 \sum_{n=1}^N c_n=1,
 \quad |\operatorname{supp}c|\le k
\right\},
\qquad k\ge1,
\]

and

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s}.
\]

Split the indices into retained coordinates `S` and discarded coordinates `D`, and let

\[
q_D(c)=c_S.
\]

For a fixed observation point `z=\sigma+it`, write

\[
v_n(z)=n^{-z}\in\mathbb C\simeq\mathbb R^2.
\]

For a finite set `V\subset\mathbb C`, define its `m`-sparse convex hull by

\[
\operatorname{conv}_{\le m}(V)
=
\left\{
 \sum_{j=1}^r\lambda_j w_j:
 1\le r\le m,
 \ w_j\in V,
 \lambda_j\ge0,
 \sum_{j=1}^r\lambda_j=1
\right\}.
\tag{1}
\]

Fix a retained state `y=q_D(c)`. Put

\[
s(y)=|\operatorname{supp}y|,
\qquad
M(y)=1-\|y\|_1,
\qquad
r_S(y;z)=\sum_{n\in S}y_n v_n(z).
\]

Whenever `M(y)>0` and `s(y)<k`, the exact evaluation set of the sparse normalized fiber is

\[
\boxed{
\{P_c(z):c\in\Delta_N^{\le k},\ q_D(c)=y\}
=
r_S(y;z)
+M(y)\operatorname{conv}_{\le k-s(y)}\{v_d(z):d\in D\}.
}
\tag{2}
\]

If `M(y)=0`, the fiber evaluation is the singleton `{r_S(y;z)}`. Thus support size does not create a new kind of invariant; it replaces AF-302's full discarded convex hull by its bounded-cardinality convex skeleton.

Two consequences are sharp for the present scalar target.

First, since `\mathbb C\simeq\mathbb R^2`, Carathéodory's theorem gives

\[
\boxed{
\operatorname{conv}_{\le m}(V)=\operatorname{conv}(V)
\qquad(m\ge3).
}
\tag{3}
\]

Therefore, once a fiber has at least three unused support slots, **the support cap is completely invisible to a single complex scalar observation**: its reachable correction set is exactly the same convex hull as in AF-302.

Second, the small-support cases do not provide a uniform arithmetic repair either. Suppose `S` contains a rational prime `p` and `D` contains two distinct rational primes `q,r`, with `p<q<r`. Then for every real `\sigma` and every support bound `k\ge2`, there are arbitrarily large heights `t` and sources

\[
c^*,\widetilde c\in\Delta_N^{\le k}
\]

such that

\[
q_D(c^*)=q_D(\widetilde c),
\qquad
P_{c^*}(\sigma+it)=0,
\qquad
P_{\widetilde c}(\sigma+it)\ne0.
\tag{4}
\]

The construction already uses total support exactly `2`. Hence **no fixed nontrivial support bound `k\ge2` can make coordinate deletion uniformly faithful for the point-zero discriminator over unbounded height**. The remaining case `k=1` contains only monomials, so `P_c(s)` never vanishes at finite `s`; it avoids the collision only by eliminating cancellation and making the point-zero discriminator identically false.

This closes bounded support cardinality as a standalone escape from AF-303. Sparsity can still matter when combined with a finite height window, coefficient caps, a discrete alphabet, multiplicative constraints, or another source law. What fails is the claim that a finite cardinality bound by itself protects the rational-prime discriminator after coordinate deletion.

## Exact sparse-fiber geometry

Let `y` be a retained state realized by some `c\in\Delta_N^{\le k}`. Every completion in its fiber has

\[
c_n=y_n\quad(n\in S),
\qquad
x_d=c_d\ge0\quad(d\in D),
\]

with

\[
\sum_{d\in D}x_d=M(y).
\tag{5}
\]

The retained support already consumes `s(y)` of the total `k` slots. If `M(y)>0`, at most

\[
m=k-s(y)
\]

discarded coefficients may be nonzero. Writing `x_d=M(y)\lambda_d` on those nonzero coordinates gives a convex combination of at most `m` response vectors. Hence

\[
\sum_{d\in D}x_d v_d(z)
\in
M(y)\operatorname{conv}_{\le m}V_D(z),
\]

where

\[
V_D(z)=\{v_d(z):d\in D\}.
\]

Conversely, every element of this sparse convex hull defines a completion with at most `m` nonzero discarded coefficients. Adding the fixed retained response proves (2).

The exact failure criterion is therefore

\[
\boxed{
0\in r_S(y;z)
+M(y)\operatorname{conv}_{\le k-s(y)}V_D(z).
}
\tag{6}
\]

This is the sparse version of AF-302's mass-scaled convex-hull criterion. It also shows why counting source coordinates without conditioning on the retained support can be misleading: the relevant budget is the number of **unused support slots inside the actual compression fiber**.

## Planar Carathéodory makes three slots equivalent to the full hull

Carathéodory's theorem states that every point of the convex hull of a subset of `\mathbb R^d` is a convex combination of at most `d+1` points of that set. Applying it in

\[
\mathbb C\simeq\mathbb R^2
\]

gives

\[
\operatorname{conv}(V)
=
\operatorname{conv}_{\le3}(V).
\tag{7}
\]

Since the sparse hulls are nested in `m`, equation (3) follows immediately.

Thus a support constraint with three or more available forgotten slots cannot shrink the reachable body seen by a **single complex evaluation**. This is not an asymptotic statement and does not depend on Dirichlet structure. It is a target-dimension statement: a two-real-dimensional scalar response has Carathéodory number at most three.

The result also exposes a broader design rule. A source constraint can only buy fidelity through sparsity if its allowed support is small relative to the real dimension and geometry of the downstream observable. Merely saying that the source is sparse is not enough; the support budget must be compared with the Carathéodory number of the actual response set.

## Two-term prime cancellation defeats every nontrivial total support cap

The stronger arithmetic obstruction needs no three-point convex combination.

Fix distinct primes

\[
p<q<r,
\qquad
p\in S,
\qquad
q,r\in D.
\]

For every integer `\ell\ge0`, set

\[
t_\ell
=
\frac{(2\ell+1)\pi}{\log(q/p)}.
\tag{8}
\]

Then

\[
e^{-it_\ell\log(q/p)}=-1,
\]

so the two response vectors `p^{-\sigma-it_\ell}` and `q^{-\sigma-it_\ell}` are antiparallel.

Let

\[
R_p=p^{-\sigma},
\qquad
R_q=q^{-\sigma},
\]

and choose

\[
A=\frac{R_q}{R_p+R_q},
\qquad
B=\frac{R_p}{R_p+R_q}.
\tag{9}
\]

Then `A,B>0`, `A+B=1`, and

\[
A R_p=B R_q.
\tag{10}
\]

Define the two-sparse source

\[
c^*=A e_p+B e_q.
\tag{11}
\]

At `z_\ell=\sigma+it_\ell`, antipodality and (10) give

\[
\boxed{P_{c^*}(z_\ell)=0.}
\tag{12}
\]

Now replace only the forgotten coordinate `q` by the other forgotten prime `r`:

\[
\widetilde c=A e_p+B e_r.
\tag{13}
\]

The retained state is unchanged:

\[
q_D(c^*)=q_D(\widetilde c)=A e_p.
\tag{14}
\]

Using (12),

\[
P_{\widetilde c}(z_\ell)
=B\left(r^{-z_\ell}-q^{-z_\ell}\right).
\tag{15}
\]

This never vanishes.

If `\sigma\ne0`, the two terms in parentheses have different moduli because `r\ne q`. If `\sigma=0`, equality would require

\[
t_\ell\log(r/q)\in2\pi\mathbb Z,
\]

or

\[
(2\ell+1)
\frac{\log(r/q)}{\log(q/p)}
\in2\mathbb Z.
\tag{16}
\]

But the logarithmic ratio in (16) is irrational. If it were rational, exponentiation would produce a nontrivial multiplicative relation among the three distinct primes `p,q,r`, contradicting unique factorization. Hence

\[
P_{\widetilde c}(z_\ell)\ne0
\]

for every `\ell`.

As `t_\ell\to\infty`, equations (12)--(15) prove (4) at arbitrarily large heights. No equidistribution theorem is needed: one retained prime and one forgotten prime form an exact two-frequency cancellation, while a second forgotten prime supplies a safe source in the same compression fiber.

Because both sources have total support `2`, the counterexample belongs to every `\Delta_N^{\le k}` with `k\ge2`.

## The support-one boundary is real but vacuous for zero formation

For `k=1`, normalization forces every source to be a coordinate vector:

\[
\Delta_N^{\le1}=\{e_1,\dots,e_N\}.
\]

Therefore

\[
P_{e_n}(s)=n^{-s}\ne0
\]

at every finite complex `s`. The point-zero discriminator is constant on the entire source class.

So support `1` does create exact factorization, but only because the class no longer contains any cancellation mechanism capable of generating a zero. In the present program that is not a useful fidelity repair: the downstream event being protected has been removed from the admissible source family.

The sharp cardinality boundary for the explicit obstruction is therefore:

\[
\boxed{
\begin{array}{ll}
k=1:&\text{no finite zeros exist;}\\
k\ge2:&\text{same-fiber zero/safe collisions recur at arbitrarily large height.}
\end{array}}
\tag{17}
\]

This boundary is source-specific and target-specific. It does not say that every two-sparse family or every compression fails; it says that **support cardinality alone** cannot certify fidelity once ordinary two-term Dirichlet cancellation is admitted.

## Local zero-count collision

The failing two-term source has a simple zero at each `z_\ell`. Differentiate

\[
P_{c^*}(s)=A p^{-s}+B q^{-s}.
\]

At a zero, `Bq^{-z_\ell}=-Ap^{-z_\ell}`, hence

\[
P_{c^*}'(z_\ell)
=
-A(\log p)p^{-z_\ell}
-B(\log q)q^{-z_\ell}
=
A p^{-z_\ell}\log(q/p)
\ne0.
\tag{18}
\]

Thus the zero is isolated and simple. Since `P_{\widetilde c}(z_\ell)\ne0`, choose a sufficiently small disk centered at `z_\ell` whose boundary contains no zero of either function, which contains the simple zero of `P_{c^*}` and no zero of `P_{\widetilde c}`. The two sources therefore also have different local zero counts while remaining indistinguishable under `q_D`.

So the support-only obstruction is not an artifact of asking for exact equality at one point. It transfers directly to a local contour zero-count discriminator.

## Prior art and novelty assessment

The ingredients are classical; no novelty claim is made for sparse convex representation, Carathéodory's theorem, or two-term exponential-sum zeros.

- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton Mathematical Series 28, Princeton University Press (1970), Theorem 17.1, gives the classical Carathéodory theorem: in `\mathbb R^d`, `d+1` points suffice for an exact convex-hull representation. Its specialization to `\mathbb C\simeq\mathbb R^2` is equation (7).
- Alexander Barvinok, *A Course in Convexity*, Graduate Studies in Mathematics 54, American Mathematical Society (2002), is a standard modern convexity reference covering the Carathéodory/Helly/Radon framework.
- The two-term cancellation in (8)--(12) is the elementary zero equation for an exponential sum. General zero geometry for exponential polynomials is classical; no general zero-distribution theorem is needed here.
- Irrationality of `\log(r/q)/\log(q/p)` for three distinct primes is the direct unique-factorization argument given above.

A targeted prior-art search confirmed that the sparse-convex representation step is exactly classical Carathéodory-number mathematics. It did not provide grounds for claiming novelty for the two-term Dirichlet cancellation either. The durable Arithmetic Fidelity content is the specialization to the current source-restriction question: **at one complex scalar target, three available support slots already recover the full convex hull, while even two total source terms suffice to break coordinate-deletion fidelity recurrently in a rational-prime instance.**

## Boundaries and failure modes

- The source class is the normalized nonnegative `k`-sparse simplex. Signed, complex, integral, multiplicatively coupled, or nonlinear source laws have different feasible fibers.
- The compression is coordinate deletion. A representation that also retains the identity of the forgotten active coordinate, or another support mark, changes the fiber and can distinguish (11) from (13).
- Equation (3) is specific to one complex scalar observation, hence two real target dimensions. A vector of several observations has a larger real response dimension and a correspondingly larger Carathéodory bound.
- The recurrent collision in (8)--(16) uses an unbounded vertical observation family. It does not imply failure inside an arbitrary prescribed compact height window.
- The explicit `k\ge2` counterexample assumes at least one retained prime and two forgotten primes. If the compression deletes only one simplex coordinate, normalization recovers that coefficient from the retained mass and the map is injective.
- `k=1` is faithful for the point-zero discriminator only vacuously: all admissible Dirichlet polynomials are monomials and have no finite zeros.
- A combined constraint can still matter. A coefficient cap together with a support bound, a discrete coefficient alphabet, a finite height window, a support pattern restriction, or a nonlinear arithmetic coupling may exclude the two-term weights (9) or the dangerous heights (8).
- The result concerns finite Dirichlet polynomials and local zero discrimination. It gives no analytic continuation statement, zero matching with `\zeta`, asymptotic coefficient law, or RH implication.

## Consequence for the research line

AF-303 listed bounded discarded support as a possible way to keep the feasible correction polytope from reaching the failure value. AF-304 closes **pure cardinality sparsity** as a standalone repair.

At a fixed scalar observation, the exact sparse correction body is now known: it is the mass-scaled `m`-sparse convex hull in (2), and Carathéodory makes every `m\ge3` fiber indistinguishable from the unrestricted convex hull. More strongly, uniform factorization already fails with total support `2` in a three-prime retained/forgotten configuration, by the explicit arithmetic progression of dangerous heights (8).

The live source-relative escape must therefore use more than a fixed support count. The next useful questions are whether **which supports are admissible**, how coefficients are coupled on those supports, discreteness/integrality, or a finite observation window can force the actual sparse correction set to avoid the target failure value. A bare statement that the source is sparse no longer carries fidelity evidence.