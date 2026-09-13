# AF-305 — Joint cap-support slack still allows Dirichlet collisions

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `SIMPLEX`, `SPARSITY`, `COEFFICIENT-CAPS`, `KRONECKER-WEYL`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-303 rules out a fixed source-independent coefficient cap by itself, while AF-304 rules out a fixed nontrivial support bound by itself. Their natural joint repair has an exact saturation boundary.

For integers `N>=k>=2` and `alpha>0`, define

\[
\Delta_N^{\le k,\alpha}
=
\left\{
 c\in\mathbb R_+^N:
 \sum_{n=1}^N c_n=1,
 \quad |\operatorname{supp}c|\le k,
 \quad c_n\le\alpha\ \forall n
\right\},
\]

and

\[
P_c(s)=\sum_{n=1}^N c_n n^{-s}.
\]

Then:

1. if `k alpha<1`, the source class is empty;
2. if `k alpha=1`, necessarily `alpha=1/k` and every admissible source is exactly a uniform `k`-subset,
   \[
   c=\frac1k\mathbf 1_A,
   \qquad |A|=k;
   \tag{1}
   \]
3. if `k alpha>1`, then for every fixed real `sigma` there are finite rational-prime coordinate sets, a coordinate-deletion compression `q_D`, arbitrarily large heights `t`, and
   \[
   c^*,\widetilde c\in\Delta_N^{\le k,\alpha}
   \]
   such that
   \[
   q_D(c^*)=q_D(\widetilde c),
   \qquad
   P_{c^*}(\sigma+it)=0,
   \qquad
   P_{\widetilde c}(\sigma+it)\ne0.
   \tag{2}
   \]

Therefore **combining a fixed coefficient cap with a fixed support cap does not uniformly repair coordinate-deletion fidelity anywhere in the strict-slack regime `k alpha>1`**. The only nonempty parameter boundary not already defeated by the AF-303/AF-304 mechanisms is the saturated class `k alpha=1`, where all coefficient freedom disappears and the problem becomes discrete support combinatorics.

This is a sharp boundary for the geometry of the admissible source class, not a theorem that the saturated class is faithful. The saturated family can still fail through collisions between different support patterns. What is eliminated there is the continuous barycentric freedom used by the previous no-go arguments.

## Exact feasibility and saturation geometry

For any `c\in\Delta_N^{\le k,\alpha}`,

\[
1=\sum_n c_n
\le |\operatorname{supp}c|\,\alpha
\le k\alpha.
\tag{3}
\]

Hence `k alpha<1` is impossible.

Suppose now that `k alpha=1`. Equality must hold at both inequalities in (3). Therefore

\[
|\operatorname{supp}c|=k
\]

and every nonzero coefficient must attain the cap:

\[
c_n=\alpha=\frac1k
\qquad(n\in\operatorname{supp}c).
\tag{4}
\]

Thus the entire source class is the finite family

\[
\Delta_N^{\le k,1/k}
=
\left\{
\frac1k\mathbf1_A:
A\subseteq\{1,\ldots,N\},\ |A|=k
\right\}.
\tag{5}
\]

After multiplication by `k`, these are precisely the `0/1` incidence vectors of `k`-subsets, i.e. the vertices of the classical hypersimplex / uniform-matroid base polytope. The present source class contains the vertices only; it does not contain their convex hull.

When `k alpha>1`, by contrast, at least one support size admitted by the class carries genuine coefficient slack. The arithmetic collision below shows that this slack is enough to reactivate one of the already identified cancellation mechanisms.

## Strict slack with `alpha>1/2`: two terms already suffice

Assume first

\[
\alpha>\frac12.
\tag{6}
\]

Fix `sigma\in\mathbb R`. Choose distinct primes

\[
p<q<r
\]

with `q/p` sufficiently close to `1` that the AF-304 two-term zero weights

\[
A=\frac{q^{-\sigma}}{p^{-\sigma}+q^{-\sigma}},
\qquad
B=\frac{p^{-\sigma}}{p^{-\sigma}+q^{-\sigma}}
\tag{7}
\]

satisfy

\[
A<\alpha,
\qquad
B<\alpha.
\tag{8}
\]

Such prime pairs exist arbitrarily far out because every fixed relative interval `[X,(1+eta)X]` contains multiple primes for sufficiently large `X`; as `q/p\to1`, both weights tend to `1/2`.

Put `p` in the retained set and `q,r` in the deleted set. For

\[
t_\ell=\frac{(2\ell+1)\pi}{\log(q/p)},
\qquad \ell\ge0,
\tag{9}
\]

the responses of `p` and `q` are antiparallel and (7) equalizes their magnitudes. Hence

\[
c^*=A e_p+B e_q
\]

satisfies

\[
P_{c^*}(\sigma+it_\ell)=0.
\tag{10}
\]

Replace only the deleted coordinate:

\[
\widetilde c=A e_p+B e_r.
\tag{11}
\]

Both sources have support `2<=k`, obey the cap, and have the same retained state `A e_p`. As in AF-304,

\[
P_{\widetilde c}(\sigma+it_\ell)
=
B\left(r^{-\sigma-it_\ell}-q^{-\sigma-it_\ell}\right)
\ne0.
\tag{12}
\]

For `sigma\ne0`, nonvanishing follows from the unequal moduli of the `q` and `r` terms. For `sigma=0`, equality would force

\[
\frac{\log(r/q)}{\log(q/p)}\in\mathbb Q,
\]

which would exponentiate to a nontrivial multiplicative relation among the distinct primes, contradicting unique factorization.

Thus every strict cap above `1/2` is already defeated by a two-sparse collision.

## Strict slack with `alpha<=1/2`: enough capped slots recreate the polygon

Assume now

\[
0<\alpha\le\frac12,
\qquad
k\alpha>1.
\tag{13}
\]

Set

\[
m=\left\lfloor\frac1\alpha\right\rfloor+1.
\tag{14}
\]

Then

\[
m\ge3,
\qquad
\frac1m<\alpha,
\qquad
m\le k,
\tag{15}
\]

where the final inequality follows from `k>1/alpha`.

AF-303 applies exactly in this regime. Choose `m` sufficiently comparable discarded rational primes `p_1,\ldots,p_m` so that

\[
\max_j
\frac{p_j^\sigma}{\sum_{a=1}^m p_a^\sigma}
<\alpha.
\tag{16}
\]

The prime number theorem supplies such a block inside a sufficiently short fixed relative interval. The inverse-radius weights therefore lie strictly inside the cap and can form the regular-polygon zero configuration used in AF-303. The implicit-function theorem preserves a capped zero representation on an open phase neighborhood, and rational independence of the prime logarithms plus Kronecker-Weyl recurrence makes that phase neighborhood recur at arbitrarily large heights.

Consequently there are `m`-sparse sources `c^*,\widetilde c`, supported entirely on deleted coordinates, with all coefficients strictly below `alpha`, identical retained state `0`, and the zero/safe separation (2). Since `m<=k`, they lie in `\Delta_N^{\le k,\alpha}`.

Thus the combined constraint does not create a new faithful regime whenever it leaves any strict mass slack above the saturation threshold.

## The saturated boundary is genuinely different

At

\[
k\alpha=1,
\]

the continuous perturbation mechanism is absent: every support is forced to carry equal coefficients `1/k`. A same-fiber collision must therefore come from different admissible support sets whose equal-weight exponential sums have different zero behavior. Neither AF-303's interior capped-polytope perturbation nor AF-304's freely chosen two-term barycentric weights survives unchanged.

The smallest case shows that this is not merely a proof artifact. For

\[
k=2,
\qquad
\alpha=\frac12,
\]

every source has the form

\[
P(s)=\frac12(a^{-s}+b^{-s}),
\qquad a\ne b.
\tag{17}
\]

A zero on `Re(s)=sigma` requires equal term moduli,

\[
a^{-\sigma}=b^{-\sigma}.
\]

For distinct positive coordinates this is possible only when

\[
\sigma=0.
\tag{18}
\]

Hence the saturated two-support class is zero-free on every fixed vertical line `sigma\ne0`, whereas on `sigma=0` each pair has the familiar periodic antipodal zeros. Saturation can therefore change the target geometry qualitatively; it is not just a parameter value missed by the previous constructions.

For `k>=3`, equal-weight support collisions are a separate exponential-sum problem and are not settled here.

## Prior art and novelty assessment

No novelty claim is made for any ingredient.

- The feasibility inequality and saturation statement are elementary capped-simplex geometry. After scaling by `k`, the saturated points are the incidence vectors of `k`-subsets, the vertices of the classical hypersimplex / base polytope of the uniform matroid. This polyhedral object is standard in matroid theory; Jack Edmonds' foundational polyhedral work on matroids and later standard treatments such as Schrijver's *Combinatorial Optimization* provide the surrounding language.
- AF-303 already records the classical continuous Kronecker-Weyl theorem and prime-number-theorem input used to build recurrent capped prime polygons.
- AF-304 already records the elementary two-term Dirichlet cancellation and the support-side convex geometry used above.

The durable Arithmetic Fidelity content is the exact **joint** phase boundary for the live repair attempt: support and coefficient caps do not accumulate independent protection. If `k alpha>1`, enough continuous mass freedom survives for an existing rational-prime cancellation mechanism to re-enter. Only exact saturation `k alpha=1` changes the source category from continuous sparse simplices to a discrete family of uniform supports.

## Boundaries and failure modes

- The theorem is a family-level no-go. A fixed finite coordinate set may avoid the required prime block or dangerous phase configuration.
- `k=1` is excluded. As in AF-304, the source then contains only monomials and has no finite zeros; it removes the cancellation target rather than protecting it nontrivially.
- The strict-slack collision is for a single complex point-zero discriminator over unbounded height. It does not by itself give an RH implication, analytic-continuation statement, or global zero-count theorem.
- The saturated boundary is **not proved faithful**. Its remaining fibers are discrete support families, and distinct support patterns may still collide.
- Geometry-adaptive caps, prescribed support families, arithmetic alphabets, multiplicative/nonlinear coefficient relations, and finite observation windows remain outside the theorem unless they reduce to the joint class above.
- The hypersimplex observation is a classification of the saturated source geometry, not a claim that matroid theory supplies the missing arithmetic theorem.

## Consequence for the research line

AF-303 and AF-304 left a joint cap/support law as an obvious next repair. AF-305 closes every nonsaturated version of that repair:

\[
\boxed{
 k\alpha>1
 \quad\Longrightarrow\quad
 \text{uniform coordinate-deletion fidelity still fails.}
}
\tag{19}
\]

The live boundary is now much narrower. If a source law is to beat the convex/barycentric obstruction by combining sparsity with coefficient control, it must reach the **saturated discrete regime** or impose genuinely additional structure. The next honest question is therefore not whether smaller caps plus smaller supports help continuously, but whether equal-weight or otherwise discrete prescribed-support Dirichlet families retain a rational-prime discriminator after deletion, and under which target geometry.

This isolates discreteness as a real categorical change rather than another quantitative tightening of the same continuous simplex fiber.