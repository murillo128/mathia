# AF-378 — Order reparameterization preserves sampling fibres but not translation geometry

## Status

`EXACT-DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `SAMPLING` · `REPRESENTATION-AUDIT` · `CLASSICAL-ADJACENT` · `NO-NOVELTY-CLAIM`

## Claim

The support-interaction obstruction in AF-376/AF-377 is expressed in a Euclidean coordinate, so its visible graph geometry can change drastically under a nonlinear order reparameterization. That does **not** mean the underlying sampled-total-positivity fibre has been repaired.

Let `X,Y` be totally ordered sets, let `E subset X`, and let

\[
K:X\times Y\to\mathbb R
\]

be a kernel. For order isomorphisms

\[
\phi:X\to X',\qquad \psi:Y\to Y',
\]

define the transported kernel

\[
K^{\phi,\psi}(u',x')
:=K\bigl(\phi^{-1}(u'),\psi^{-1}(x')\bigr),
\qquad E':=\phi(E).
\tag{1}
\]

Then the complete sampled determinant observation on `(K,E)` is identical, value for value, to the sampled determinant observation on `(K^{phi,psi},E')`. In particular:

\[
K\text{ is }E\text{-totally nonnegative}
\iff
K^{\phi,\psi}\text{ is }E'\text{-totally nonnegative},
\tag{2}
\]

and

\[
K\text{ is globally totally nonnegative}
\iff
K^{\phi,\psi}\text{ is globally totally nonnegative}.
\tag{3}
\]

Hence every sampled false positive survives exact order-coordinate transport. An order reparameterization can change gaps, densities, support-scale interaction graphs, and whether the displayed sample set is uniformly discrete, while leaving the actual observation fibre unchanged.

For Pólya-frequency kernels there is an additional rigidity. A translation kernel

\[
K_f(u,x)=f(u-x)
\tag{4}
\]

is transported by a common order isomorphism `phi:R->R` to

\[
K_f^\phi(s,t)
=f\bigl(\phi^{-1}(s)-\phi^{-1}(t)\bigr).
\tag{5}
\]

The underlying difference geometry in `(5)` depends only on `s-t` for every source profile `f` precisely when `phi` is positive affine. Equivalently, the full translation-kernel category is stable under common coordinate changes only under

\[
\phi(u)=au+b,\qquad a>0.
\tag{6}
\]

Thus a nonlinear coordinate change can make a sampling set look much richer in Euclidean spacing only by moving the transported object out of the translation-invariant Pólya-frequency model. Replacing `(5)` by a fresh kernel `g(s-t)` is not a coordinate repair of the old compression; it is a new mathematical model and needs independent source semantics.

## Exact observation-conjugacy proof

Choose increasing rows

\[
u_1<\cdots<u_n,\qquad u_i\in E,
\]

and increasing columns

\[
x_1<\cdots<x_n,\qquad x_j\in Y.
\]

Since `phi` and `psi` are order isomorphisms,

\[
\phi(u_1)<\cdots<\phi(u_n),
\qquad
\psi(x_1)<\cdots<\psi(x_n).
\]

By `(1)`, entrywise,

\[
K^{\phi,\psi}\bigl(\phi(u_i),\psi(x_j)\bigr)
=K(u_i,x_j).
\tag{7}
\]

Therefore

\[
\det\Bigl(K^{\phi,\psi}(\phi(u_i),\psi(x_j))\Bigr)_{i,j=1}^n
=
\det\bigl(K(u_i,x_j)\bigr)_{i,j=1}^n.
\tag{8}
\]

Every admissible ordered tuple on one side corresponds bijectively to an admissible ordered tuple on the other. Equations `(2)` and `(3)` follow immediately, and more strongly the entire family of determinant values is unchanged.

Consequently, if `K` is sampled-TN on `E` but not globally TN, then `K^{phi,psi}` is sampled-TN on `E'` but not globally TN. Coordinate transport conjugates the observation fibre; it cannot split it.

## Affine rigidity of translation geometry

Put `h=phi^{-1}`. The difference geometry in `(5)` is itself translation invariant exactly when there exists a function `q:R->R` such that

\[
h(s)-h(t)=q(s-t)
\qquad\text{for all }s,t\in\mathbb R.
\tag{9}
\]

Setting `t=0` gives

\[
h(s)=q(s)+h(0).
\tag{10}
\]

Substituting `(10)` back into `(9)` yields

\[
q(s)-q(t)=q(s-t).
\]

Taking `s=x+y` and `t=y`,

\[
q(x+y)=q(x)+q(y).
\tag{11}
\]

Because `h` is increasing, `q` is increasing. Every monotone additive function on `R` is linear, so

\[
q(x)=cx,\qquad c>0.
\]

Hence

\[
h(s)=cs+d,
\]

and `phi` is positive affine. Conversely, a positive affine `phi(u)=au+b` gives

\[
K_f^\phi(s,t)
=f\!\left(\frac{s-t}{a}\right)
=:g(s-t),
\tag{12}
\]

so the translation-kernel form is preserved.

This is a rigidity statement about the **representation class**, not about a particular profile. Special degenerate functions may hide some coordinate dependence. The claim is that the difference structure itself, and therefore the whole class of translation kernels, is preserved only by positive affine changes.

## Explicit metric-graph illusion

Take the uniformly discrete sampling set

\[
E=\mathbb Z
\]

and a compactly supported false-positive profile from AF-376, for example

\[
f(t)=\mathbf 1_{(0,1/2)}(t).
\tag{13}
\]

Because the support width is below the unit separation, AF-376 gives sampled total nonnegativity on `E`, while `f` is not a full Pólya-frequency function.

Now use the increasing homeomorphism

\[
\phi(u)=\operatorname{arsinh}(u).
\tag{14}
\]

The transformed sample set

\[
E'=\operatorname{arsinh}(\mathbb Z)
\]

has consecutive gaps tending to zero at both ends:

\[
\operatorname{arsinh}(n+1)-\operatorname{arsinh}(n)\to0.
\tag{15}
\]

For every fixed Euclidean scale `w>0`, sufficiently far out the consecutive gaps in `E'` are below `w`, so the naive graph `G_w(E')` has unbounded, indeed infinite-tail, connected components. The visible bounded-component obstruction from AF-377 has disappeared.

But the correctly transported kernel is

\[
K'(s,t)
=
\mathbf 1_{(0,1/2)}\bigl(\sinh(s)-\sinh(t)\bigr),
\tag{16}
\]

not a compactly supported translation kernel in the new difference `s-t`. By `(8)`, every sampled determinant in `(16)` is exactly an old sampled determinant for `(13)`, and every global negative witness transports as well. The false positive therefore survives unchanged.

There is no contradiction with AF-377: that theorem couples a **fixed-width support interval in the same translation coordinate** to the Euclidean interaction graph. After nonlinear pullback, the support neighborhoods have variable width and are the images of the old activity intervals. Computing a new fixed-width graph in the displayed coordinate changes the diagnostic without transporting the object it was designed to diagnose.

## Fidelity interpretation

AF-376/AF-377 identified sampling geometry as a genuine resource, but the present result separates two meanings of “geometry”:

1. the intrinsic ordered observation experiment, which is preserved by order conjugacy; and
2. metric features such as Euclidean gaps and fixed support radii, which belong to a chosen representation of that experiment.

A fidelity obstruction should survive a change of representation when the source, observation map, and target are transported together. If an apparent repair works only after changing coordinates and then silently reinstating a preferred structural class such as translation invariance, the repair has changed the source model rather than refined the original compression.

This gives a representation audit for metric compression arguments: transport the whole kernel first, then ask which structural properties remain. Do not transport only the sample locations and compare them against an untransported model class.

## Relation to AF-373 through AF-377

AF-373 showed that location sampling can be determining for full Pólya-frequency total positivity when the sampling set satisfies suitable hypotheses. AF-376 and AF-377 then exposed exact compact-support aliases when the actual translation-coordinate sampling geometry has insufficient local interaction.

AF-378 does not weaken those results. It identifies their covariance boundary. The determinant observation itself is invariant under arbitrary order isomorphism, while the translation-kernel specialization and its fixed support metric are only affine-covariant.

Accordingly, “make the sample set denser by taking logarithms” or any analogous nonlinear coordinate move is not by itself a response to AF-376/AF-377. Either the original kernel is transported, in which case the false-positive fibre persists exactly, or a fresh translation kernel is imposed in the new coordinate, in which case one has posed a different recovery problem.

## Riemann specialization

Arithmetic constructions often move among additive, multiplicative, logarithmic, valuation, or spectral coordinates. Those transformations may dramatically alter spacing: a set that is uniformly separated in one coordinate can have gaps tending to zero in another.

For an RH-facing total-positivity proposal, this spacing change cannot itself be counted as recovered arithmetic fidelity. If the proposed criterion is genuinely inherited from a kernel or operator in the original coordinate, that object must be transported with the coordinate map. If instead logarithmic or another nonlinear coordinates are mathematically intrinsic because multiplication has become addition, the resulting translation structure may be legitimate — but that is an independent structural input that must be derived from the arithmetic object, not inferred from the improved sampling density.

No statement about prime distribution or zero location follows here. The result is a gate against representation-induced false repairs of a sampling compression.

## Prior-art and novelty audit

The invariance in `(8)` is immediate from the standard definition of a totally nonnegative/positive kernel on totally ordered sets. Samuel Karlin, **Total Positivity, Vol. I** (Stanford University Press, 1968), is the classical general reference. Modern treatments explicitly formulate total positivity on arbitrary totally ordered domains; see Alexander Belton, Dominique Guillot, Apoorva Khare, and Mihai Putinar, **“Totally positive kernels, Pólya frequency functions, and their transforms,”** *Journal d'Analyse Mathématique* **150** (2023), 83–158, DOI `10.1007/s11854-022-0259-7`, and their related survey **“Preservers of totally positive kernels and Pólya frequency functions,”** *Mathematics Research Reports* **3** (2022), 35–56, DOI `10.5802/mrr.12`.

Michael I. Ganzburg, **“On E-Pólya Frequency Functions,”** *Journal of Mathematical Analysis and Applications* **346**(1) (2008), 1–8, DOI `10.1016/j.jmaa.2008.04.070`, remains the direct sampling framework behind AF-373 through AF-377.

A focused search for total-positive-kernel reparameterization, Pólya-frequency coordinate changes, translation-kernel transforms, and sampling-set transformations did not identify a separate theorem needed for `(8)` or `(9)`–`(12)`: both are elementary consequences of the definitions and the monotone Cauchy equation. No novelty is claimed. The durable Arithmetic Fidelity contribution is the **representation distinction**: an arbitrary order change preserves the sampled observation fibre, whereas only affine coordinate changes preserve the translation geometry in which fixed-width support-interaction arguments live.

## Boundaries and failure modes

Equation `(8)` requires transporting the kernel and both ordered domains together. Moving only the sampling set while holding `K` fixed is a different observation map and need not preserve anything.

The affine-rigidity claim concerns preservation of the difference geometry for the entire translation-kernel class. A special profile `f` can have accidental symmetries or degeneracies that make one nonlinear pullback representable in another way; such profile-specific coincidences are outside the universal statement.

The result also does not say that nonlinear coordinates are illegitimate. They may be the natural coordinates of a different intrinsic group law or arithmetic structure. It says only that a change of coordinates is not evidence of increased fidelity unless the mathematical object and admissible source class are transformed consistently.

Finally, the support-interaction graph from AF-377 remains a valid and useful diagnostic inside a fixed translation representation. AF-378 only prevents its Euclidean graph topology from being mistaken for an order-invariant property of the underlying observation experiment.

## Decisive audit rule

When a sampling obstruction seems to disappear after a nonlinear reparameterization, distinguish **transport** from **replacement**.

If the kernel, sampling set, and target are transported together, compare the determinant observation before and after the change: the fibre is conjugate and no false positive has been removed. If one instead restores a translation-invariant kernel in the new coordinate, treat that as a new source model and justify why the new group/difference structure is intrinsic.

For translation-kernel Pólya-frequency arguments, positive affine changes are the only universal coordinate changes that preserve the original difference geometry. Nonlinear densification of the sample set is therefore not, by itself, a fidelity repair.