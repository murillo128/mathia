# AF-377 — Bounded support-interaction components hide finite-order aliases

## Status

`EXACT-DERIVED` · `DECISIVE-NEGATIVE` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `SAMPLING` · `RELATIONAL-ARITY` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

AF-376 shows that a uniformly discrete row-sampling set cannot determine full Pólya-frequency total positivity on Ganzburg's broad exponentially decaying source class `L`: a compactly supported kernel narrower than the minimum row spacing makes every sampled minor essentially diagonal.

Uniform discreteness is not the real boundary. There are sampling sets with **arbitrarily small row gaps** and no finite accumulation point that are still non-determining on `L`.

The relevant obstruction is the size of the connected components seen at the support scale.

Let `f : R -> [0,infinity)` be integrable and supported in an interval of length at most `w>0`. For a sampling set `E subset R`, define the support-interaction graph

\[
G_w(E):\qquad
u\sim v
\quad\Longleftrightarrow\quad
u\ne v\ \text{ and }\ |u-v|\le w.
\tag{1}
\]

Suppose every connected component of `G_w(E)` has at most `r` vertices. If `f` is a Pólya-frequency function of order `r` (`PF_r`), then `f` is `E`-Pólya-frequency of **all sampled determinant orders**.

Therefore, whenever such a compactly supported `PF_r` kernel fails to be full `PF_infinity`, the sampling set `E` is not determining even though the `E`-PF observation retains determinants of arbitrary size.

In particular, there exists a discrete set `E` with

\[
\inf\{|u-v|:u,v\in E,\ u\ne v\}=0
\tag{2}
\]

and with no finite accumulation point, together with a bounded compactly supported `f in L`, such that `f` is `E`-PF but not PF.

Thus **vanishing minimum spacing is not sufficient to repair the AF-376 obstruction**. Sampling geometry can silently reduce nominally all-order total positivity to a bounded-order test when the support-scale interaction graph has uniformly bounded components.

## Support-interaction block lemma

Assume `supp(f)` is contained in an interval

\[
I\subset[\alpha,\beta],
\qquad \beta-\alpha\le w.
\tag{3}
\]

Fix increasing sampled rows

\[
u_1<\cdots<u_m,
\qquad u_i\in E,
\]

and increasing arbitrary columns

\[
x_1<\cdots<x_m.
\]

An entry `f(u_i-x_j)` can be nonzero only when

\[
x_j\in J_{u_i}:=[u_i-\beta,\,u_i-\alpha].
\tag{4}
\]

If two rows lie in distinct connected components of `G_w(E)`, then their distance is strictly greater than `w`; hence their activity intervals `(4)` are disjoint and occur in the same order as the rows. Consequently a column can interact with rows from at most one graph component.

Partition the selected rows by the connected components `C` of `G_w(E)`. Let `r_C` be the number of selected rows in `C`, and let `c_C` be the number of columns whose nonzero entries, if any, lie in rows of `C`.

If a column belongs to no component activity interval, it is zero and the determinant vanishes. Otherwise the matrix is an ordered direct sum of rectangular component blocks. If some `c_C\ne r_C`, then

\[
\operatorname{rank} A
\le
\sum_C \min(r_C,c_C)
<m,
\tag{5}
\]

because `sum_C r_C=sum_C c_C=m` and a mismatch forces a deficit in at least one block. Hence again `det A=0`.

The only potentially nonzero case has `c_C=r_C` for every participating component. Then the matrix is an ordered block diagonal matrix and

\[
\det A=\prod_C \det A_C.
\tag{6}
\]

Every block has size

\[
r_C\le |C|\le r,
\]

so `PF_r` gives `det A_C>=0`. Therefore `(6)` is nonnegative for every `m`, proving that `f` is `E`-PF.

This is an exact conversion of a **geometric bound on local interaction complexity** into an effective bound on relational arity.

## Explicit vanishing-gap false positive

Take

\[
f(t)=\mathbf 1_{(0,1)}(t).
\tag{7}
\]

This function is bounded, nonnegative, integrable, compactly supported, and therefore belongs to Ganzburg's exponentially decaying class `L`.

It is `PF_2`. This can be checked directly. For `u_1<u_2` and `x_1<x_2`, if the off-diagonal product

\[
f(u_1-x_2)f(u_2-x_1)
\]

is zero, the `2 x 2` determinant is automatically nonnegative. If that product equals one, then

\[
0<u_1-x_2<1,
\qquad
0<u_2-x_1<1.
\]

The order inequalities imply

\[
0<u_1-x_1<u_2-x_1<1,
\qquad
0<u_1-x_2<u_2-x_2<1,
\]

so both diagonal entries also equal one and the determinant is zero. Thus every minor of order at most two is nonnegative.

But `(7)` is not `PF_3`, hence not full PF. For example, with

\[
(u_1,u_2,u_3)=\left(0,\frac18,\frac38\right),
\qquad
(x_1,x_2,x_3)=\left(-\frac58,-\frac12,0\right),
\tag{8}
\]

one gets

\[
\bigl(f(u_i-x_j)\bigr)
=
\begin{pmatrix}
1&1&0\\
1&1&1\\
0&1&1
\end{pmatrix},
\qquad
\det=-1.
\tag{9}
\]

Now put

\[
\varepsilon_k=\frac{1}{|k|+3},
\qquad
E=\bigcup_{k\in\mathbb Z}\{3k,\,3k+\varepsilon_k\}.
\tag{10}
\]

The set `E` has no finite accumulation point, while `epsilon_k -> 0`; therefore its global minimum separation is zero. At support scale `w=1`, however, each pair in `(10)` is one connected component of `G_1(E)`, and distinct pairs are separated by at least

\[
3-\frac13=\frac83>1.
\tag{11}
\]

Every component therefore has exactly two vertices. The block lemma with `r=2` shows that `(7)` is `E`-PF of every sampled determinant order. Equation `(9)` shows that it is nevertheless not full PF.

So `(10)` is an explicit non-determining sampling skeleton with arbitrarily small gaps.

## Relation to AF-372 through AF-376

AF-372 established that a fixed determinant-order cutoff cannot certify the full PF target on an unrestricted translation-kernel class. AF-373 then showed from Ganzburg's determining theorems that location compression can nevertheless be exact when the sampling geometry is sufficiently rich, even though the sampled family remains countable.

AF-374 and AF-375 isolated and classified a separable periodic-gauge alias for fixed lattice sampling. AF-376 showed that killing that gauge with incommensurate phases is still insufficient whenever the actual row set is uniformly discrete: compact support can diagonalize the sampled minors.

The present result identifies a strictly wider mechanism. The quantity that matters for a compactly supported finite-order alias is not merely

\[
\Delta_E=\inf_{u\ne v}|u-v|,
\]

but the component complexity of `G_w(E)` at the kernel's support scale. One may have `Delta_E=0` while every support-scale component remains of bounded size.

In that regime the observation formally asks for determinants of every order, but those large determinants split into products of blocks of size at most `r`. **Sampling geometry has reintroduced a hidden arity cutoff.** This makes the AF-372 and AF-376 obstructions two manifestations of one mechanism rather than independent pathologies.

## Fidelity interpretation

For a target discriminator

\[
D(f)=\mathbf 1_{\{f\text{ is PF}\}},
\]

let `C_E(f)` retain all determinant signs with sampled rows in `E`. AF-373 shows that for some `E`, `D` factors through `C_E` on `L`; AF-376 gives uniformly discrete `E` for which it does not.

AF-377 sharpens the failure condition. At a source-dependent support scale `w`, the interaction graph `G_w(E)` determines how much of the nominal all-order relational structure can actually couple in one irreducible minor. If component size is bounded by `r`, then every compactly supported `PF_r` source is automatically a fixed point of the sampled positivity test, regardless of higher-order violations elsewhere.

Thus one should distinguish at least three sampling resources:

- raw point separation;
- algebraic generation of differences, as in AF-375;
- **support-scale interaction-component size**, which controls the effective determinant arity available to compact/local aliases.

Dense generated differences do not force large interaction components, and vanishing minimum gaps do not force them either.

## Riemann specialization

For an RH-facing Pólya-frequency criterion, replacing full translation total positivity by row-sampled all-order positivity cannot be justified merely because the sampling gaps become arbitrarily small somewhere.

If the admitted source class still contains compactly supported finite-order PF aliases and the chosen row set has uniformly bounded support-scale interaction components, the sampled certificate may have a hidden finite-order ceiling even though determinants of arbitrary nominal size are checked.

A faithful reduction therefore needs at least one additional ingredient: sampling geometry that creates unbounded interacting row clusters at every relevant source scale, a determining-set theorem such as Ganzburg's stronger hypotheses, or source-specific analytic rigidity that excludes the compact/local finite-order aliases entirely.

This is not an RH criterion and gives no zero-location information. It is a no-go test for one proposed compression of a PF-equivalent target.

## Prior-art and novelty audit

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1–8, DOI `10.1016/j.jmaa.2008.04.070`, is the direct prior-art framework. It defines `E`-PF functions, proves determining results for sampling sets with an accumulation point and for certain sufficiently dense unbounded symmetric sets, and gives compact-support false positives for `E=Z`.

Finite-order Pólya-frequency classes and their relation to total positivity are classical; see Samuel Karlin, **Total Positivity, Vol. I** (Stanford University Press, 1968). In particular, the `PF_2`/log-concavity connection is standard. The proof above does not rely on that characterization: `(7)` is verified directly at order two, and `(9)` directly witnesses failure at order three.

A focused search for `E`-Pólya-frequency sampling, finite-order PF functions, cluster sampling, uniformly discrete sampling, and bounded local multiplicity did not identify the support-interaction component lemma stated in this form. No novelty is claimed: the block decomposition is elementary, and it extends the same compact-support philosophy already explicit in Ganzburg's lattice counterexample. The durable Arithmetic Fidelity contribution is the exact **resource identification**: vanishing gaps can coexist with a bounded support-scale interaction graph, so nominally all-order sampled positivity may still reduce to finite-order positivity.

## Boundaries and failure modes

The component-size condition is sufficient for non-determination when a matching compactly supported `PF_r`-but-not-PF source is admitted; it is not a characterization of non-determining sets.

Unbounded components do not imply that `E` is determining. They only defeat this particular block-decoupling mechanism. Likewise, a source class that forbids compact support or imposes strong transform/quasianalytic constraints may exclude the explicit alias even when the sampling graph has bounded components.

The graph scale is source-dependent. A set may have bounded components at one support width and an infinite connected component at another. Any use of this obstruction must therefore couple the sampling geometry to an independently justified source class rather than choose a convenient support scale after the fact.

Finally, Ganzburg's positive determining theorems remain untouched. An accumulation point creates arbitrarily large interacting clusters at every fixed scale in its neighborhood, while his unbounded density condition supplies a different global uniqueness mechanism. AF-377 only closes the much weaker escape suggested by `Delta_E=0` alone.

## Decisive audit rule

For a row-sampled all-order total-positivity certificate, do not stop after checking that the sampling set is non-uniformly discrete or has gaps tending to zero.

Given an admissible compact/local source at scale `w`, form `G_w(E)`. If its connected components have uniformly bounded size `r` and the source class contains a compactly supported `PF_r` function that is not full PF, then the sampled certificate is not target-faithful: every nominally high-order determinant decomposes into blocks of size at most `r`.

Only after this support-scale component obstruction is excluded is vanishing spacing evidence for genuinely unbounded relational access rather than merely repeated small finite clusters.
