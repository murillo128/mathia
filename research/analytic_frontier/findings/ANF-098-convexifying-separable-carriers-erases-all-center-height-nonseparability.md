# ANF-098 — convexifying separable carriers erases all center-height nonseparability

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CONVEX-RELAXATION-OBSTRUCTION + NONNEGATIVE-RANK + ANTI-ALIGNMENT-FRONTIER`. `ANF-097` isolates the only remaining physical escape from the central-notch near-extremizer gate: a fatal Montgomery--Taylor near-extremizer must be macroscopically destructively aligned with the defect from **every** compatible same-cardinality separable carrier. A tempting response is to convexify or conically relax the separable class and then invoke Hilbert-space metric projection to manufacture a favorable comparator. That route is impossible for a structural reason stronger than bad conditioning. The convex/conic hull of separable center-height carriers already contains every physical conjugation-invariant configuration. For even cardinality this remains true **without changing cardinality and without weakening the simple-real bookkeeping**.

Let

\[
S_W(\alpha)=\sum_{z\in W}e^{-2\pi i\alpha z}
\tag{1}
\]

for a finite conjugation-invariant multiset `W`, and let `Sep(W)` be the same-cardinality product class of `ANF-086`. Let `\mathscr S_*` denote the structure factors of all nonempty finite product/separable multisets covered by `ANF-085`, with no cardinality restriction.

Then:

\[
\boxed{
S_W\in\operatorname{cone}(\mathscr S_*)
\qquad\text{for every finite conjugation-invariant }W.
}
\tag{2}
\]

After mass normalization, if `N=|W|` and `s_W:=S_W/N`,

\[
\boxed{
s_W\in
\operatorname{conv}
\left\{\frac{S_P}{|P|}:P\text{ separable}\right\}
\qquad\text{for every }W.
}
\tag{3}
\]

More sharply, whenever `N` is even,

\[
\boxed{
S_W\in
\operatorname{conv}
\{S_P:P\in\operatorname{Sep}(W)\}.
}
\tag{4}
\]

Every carrier used in the explicit representation of (4) has `\sigma(P)=0`, so it satisfies the exact `ANF-086` affine admissibility condition `\sigma(P)\le\sigma(W)`.

Thus the positive distance `d_sep(W)` of `ANF-086` is an intrinsically **nonconvex** quantity. Replacing `Sep(W)` by its convex hull makes the distance identically zero for every even-cardinality configuration, including configurations that may be far from every individual product carrier.

There is also an exact source-interference identity. If an even-cardinality `W` is written using the canonical barycentric decomposition below,

\[
S_W=\sum_a\theta_a S_{P_a},
\qquad
P_a\in\operatorname{Sep}(W),
\qquad
\theta_a\ge0,
\qquad
\sum_a\theta_a=1,
\tag{5}
\]

then the Montgomery--Taylor interference from `ANF-097` satisfies

\[
\boxed{
\sum_a\theta_a\,
\mathcal I_{\rm MT}(W\mid P_a)
=
-\sum_a\theta_a
\|S_{P_a}-S_W\|_{\rm MT}^2
\le0.
}
\tag{6}
\]

So convexification does not merely fail to produce the favorable sign needed by `ANF-097`; its canonical barycentric identity points in the opposite direction. A convex projection or separating-hyperplane argument cannot prove the required existence of one physical `P` with `\mathcal I_{\rm MT}(W\mid P)=-o(L(P))`. The nonconvex/equal-weight selection problem is load-bearing.

## 1. Every conjugacy orbit is already a separable carrier

Write `W` as a disjoint union of its conjugacy orbits with multiplicity. A real site `x` contributes

\[
m_x e^{-2\pi i\alpha x}.
\tag{7}
\]

A nonreal orbit `z=x+iy`, `\bar z=x-iy`, with common multiplicity `m_z`, contributes

\[
m_z e^{-2\pi i\alpha x}
\left(e^{2\pi\alpha y}+e^{-2\pi\alpha y}\right).
\tag{8}
\]

But a real singleton is a product carrier with horizontal support `{x}` and vertical profile `{0}`, while a conjugate pair is a product carrier with horizontal support `{x}` and vertical profile `{-y,+y}`. Hence (7)--(8) write `S_W` as a nonnegative integer combination of elements of `\mathscr S_*`, proving (2).

Equivalently, group `W` by horizontal centers `x_i` and nonnegative vertical orbit levels `y_j`. Its occupation array is nonnegative. Product carriers are rank-one nonnegative occupation arrays, and each coordinate array is itself rank one. Therefore the conic hull of the product arrays is the whole nonnegative occupation cone. This is the elementary nonnegative-rank reason that the cone relaxation loses all center-height correlation.

For (3), normalize each real orbit by its mass one and each nonreal conjugate orbit by its mass two. Explicitly,

\[
\frac{S_W}{N}
=
\sum_{x\in W\cap\mathbb R}
\frac{m_x}{N}\,e^{-2\pi i\alpha x}
+
\sum_{z\in W/\!\sim,\ \Im z>0}
\frac{2m_z}{N}\,
\frac{e^{-2\pi i\alpha z}+e^{-2\pi i\alpha\bar z}}2.
\tag{9}
\]

The coefficients are nonnegative and sum to one. Each normalized summand is the normalized structure factor of a separable singleton or conjugate pair, proving (3) for arbitrary cardinality and parity.

## 2. Even cardinality preserves the full `ANF-086` comparison class

Assume now that `N=|W|` is even. For every distinct real site `x` occurring with multiplicity `m_x`, define the `N`-point separable carrier

\[
P_x:=N\{x\}.
\tag{10}
\]

For every distinct nonreal conjugate pair `z=x+iy`, `\bar z=x-iy`, occurring with multiplicity `m_z` on each side, define

\[
P_z:=\frac N2\{z\}\uplus\frac N2\{\bar z\}.
\tag{11}
\]

Both carriers have cardinality `N`, both are product fibers of the form treated in `ANF-085`, and both have no simple real sites:

\[
\sigma(P_x)=\sigma(P_z)=0\le\sigma(W).
\tag{12}
\]

Thus `P_x,P_z\in Sep(W)`. Set

\[
\theta_x:=\frac{m_x}{N},
\qquad
\theta_z:=\frac{2m_z}{N}.
\tag{13}
\]

The total mass identity gives

\[
\sum_x\theta_x+\sum_z\theta_z=1.
\tag{14}
\]

Moreover,

\[
\theta_x S_{P_x}
=m_xe^{-2\pi i\alpha x},
\tag{15}
\]

and

\[
\theta_z S_{P_z}
=m_z\left(
e^{-2\pi i\alpha z}
+e^{-2\pi i\alpha\bar z}
\right).
\tag{16}
\]

Summing (15)--(16) over all conjugacy orbits is exactly `S_W`, proving (4).

The parity condition in this fixed-cardinality statement is genuine. A symmetric nonreal vertical multiset of odd total cardinality must contain an odd zero-height multiplicity, so a pure nonreal orbit cannot in general be blown up to odd cardinality without introducing real mass. Nothing in (2)--(3) requires even cardinality, but (4) is stated only where the explicit same-cardinality orbit blow-up is exact.

## 3. Barycentric convexity gives the wrong interference sign

Use the Montgomery--Taylor inner product from `ANF-097`. For any barycentric representation (5),

\[
\begin{aligned}
\sum_a\theta_a\mathcal I_{\rm MT}(W\mid P_a)
&=
\operatorname{Re}
\left\langle
\sum_a\theta_aS_{P_a},S_W
\right\rangle_{\rm MT}
-
\sum_a\theta_a\|S_{P_a}\|_{\rm MT}^2\\
&=
\|S_W\|_{\rm MT}^2
-
\sum_a\theta_a\|S_{P_a}\|_{\rm MT}^2.
\end{aligned}
\tag{17}
\]

The Hilbert variance identity gives

\[
\sum_a\theta_a
\|S_{P_a}-S_W\|_{\rm MT}^2
=
\sum_a\theta_a\|S_{P_a}\|_{\rm MT}^2
-
\|S_W\|_{\rm MT}^2,
\tag{18}
\]

and (6) follows exactly.

This matters because the route suggested by generic metric-projection geometry would be to enlarge the nonlinear separable set to a convex set, project `S_W` onto it, and use first-order optimality to obtain a nonnegative or orthogonal cross term. Equations (2)--(4) show that the projection is then `S_W` itself. The relaxation has consumed the very center-height correlation that `d_sep` was designed to measure. Equation (6) further shows that decomposing that projected point back into physical product carriers does not restore the desired sign by averaging.

## 4. Relation to the anti-alignment frontier

`ANF-097` proves that a fatal Montgomery--Taylor near-extremizer must anti-align macroscopically with **every individual** compatible separable carrier. The present result explains why ordinary convex Hilbert geometry cannot contradict that requirement.

The set of individual product carriers is nonconvex, but its positive mixtures are already universal at the occupation level. Hence any argument that proves only closeness to a mixture of separable carriers, membership in a convex hull of product profiles, or orthogonality to a convexified product cone is vacuous for the `ANF-086` distance. The required theorem must select at least one **single physical product carrier** with controlled interference, or else retain a genuinely nonconvex statistic that prevents a configuration from distributing its mass among many incompatible product factors.

The same observation rules out a continuous ray-scaling shortcut. Allowing arbitrary positive linear combinations or arbitrary mass-normalized mixtures of separable carriers does not produce a useful relaxed comparison class: every `W` is already in it by (2)--(3). Any successful relaxation must therefore retain an additional restriction such as bounded mixture complexity, common marginals, an equal-weight/cardinality realization constraint, or another nonlinear compatibility condition strong enough that nonseparability survives convexification.

## 5. Adversarial audit and prior-art boundary

The proof was checked against the bookkeeping that is load-bearing in `ANF-086`--`ANF-097`. The fixed-cardinality statement uses only even `N`; no odd-cardinality interpolation is claimed. The explicit carriers (10)--(11) have exactly `N` points and `sigma=0`, so there is no hidden affine-normalization loss. Multiplicities of `W` enter only through the barycentric weights and need not be one. No topology or closure is required: all representations are finite exact identities. The result also does not say that `W` is itself separable, nor that `d_sep(W)=0`; it says only that convexification destroys the distinction between a single product factor and a mixture of factors.

The neighboring mathematics is classical. In nonnegative matrix factorization, nonnegative rank is the minimum number of nonnegative rank-one summands, and arbitrary nonnegative arrays are positive sums of rank-one coordinate arrays. In probability, unrestricted mixtures of product distributions are universal for the same elementary reason that point masses are product distributions. A targeted prior-art check against the nonnegative-rank/NMF and mixture-of-products literature found this general convex-geometric principle, but no external theorem is needed for (2)--(18): the Mathia statement is the explicit conjugation-orbit specialization together with the same-cardinality even-`N` lift and the Montgomery--Taylor interference identity. No new literature dependency is load-bearing, so `SOURCES.md` is unchanged.

The finding is a negative structural reduction, not a proof of the central-notch certificate on all complex multisets. It does not rule out a nonconvex nearest-product theorem, a bounded-mixture relaxation, an integrality argument, or an explicit family satisfying the anti-alignment condition. It rules out only the natural strategy of removing the nonconvexity before applying Hilbert projection/separation.

## Research consequence

The remaining `ANF-097` gate is now sharper. **Convexity is not a free source of the missing favorable comparator.** The product/separable class must remain discrete/nonconvex at the decisive step. A proof should either construct one physical `P\in Sep(W)` whose Montgomery--Taylor interference is `-o(L(P))`, or show that the exact projection taxes of `ANF-088` force bounded product-mixture complexity that can then be rounded to one factor. A counterexample, conversely, must exploit precisely this nonconvex gap: it must be a near-extremal positive multiset that is a harmless convex mixture of product-orbit atoms while staying a fixed `J_s`-distance from every individual compatible product carrier and anti-aligning with each of them in the source metric.