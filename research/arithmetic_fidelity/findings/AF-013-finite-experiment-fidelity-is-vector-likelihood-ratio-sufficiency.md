# AF-013 — Finite-experiment fidelity is vector likelihood-ratio sufficiency

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite sets. Let

\[
P_0,P_1,\ldots,P_m
\]

be strictly positive probability distributions on `X`, and let

\[
K(y\mid x)\ge 0,
\qquad
\sum_{y\in Y}K(y\mid x)=1
\]

be a stochastic compression channel. Write

\[
\bar P_i=P_iK.
\]

Relative to the reference distribution `P_0`, define the **vector likelihood ratio**

\[
L(x)=
\left(
\frac{P_1(x)}{P_0(x)},\ldots,
\frac{P_m(x)}{P_0(x)}
\right)
\in (0,\infty)^m,
\]

and, for every `y` with `\bar P_0(y)>0`,

\[
\bar L(y)=
\left(
\frac{\bar P_1(y)}{\bar P_0(y)},\ldots,
\frac{\bar P_m(y)}{\bar P_0(y)}
\right).
\]

Let `F:(0,\infty)^m\to\mathbb R` be convex on a convex set containing `L(X)`, with

\[
F(1,\ldots,1)=0,
\]

and define the finite multidistribution `F`-divergence

\[
D_F(P_1,\ldots,P_m\|P_0)
=
\sum_x P_0(x)F(L(x)).
\]

Then:

1. under the joint law `P_0(x)K(y|x)`, the retained likelihood-ratio vector is exactly
   \[
   \bar L(Y)=\mathbb E_{P_0}[L(X)\mid Y];
   \]
2. the divergence loss under compression is the conditional Jensen gap
   \[
   \Delta_F(K)
   :=D_F(P_1,\ldots,P_m\|P_0)
   -D_F(\bar P_1,\ldots,\bar P_m\|\bar P_0)
   \]
   \[
   =\mathbb E_{P_0}\!\left[
   F(L)-F(\mathbb E_{P_0}[L\mid Y])
   \right]
   \ge 0;
   \]
3. if `F` is strictly convex on `conv(L(X))`, then
   \[
   \Delta_F(K)=0
   \]
   if and only if every retained output mixes only states with the same **entire** likelihood-ratio vector:
   \[
   K(y\mid x)>0,\ K(y\mid x')>0
   \Longrightarrow
   L(x)=L(x');
   \]
4. that condition is equivalent to statistical sufficiency of `K` for the whole finite experiment: there exists a single reverse channel `R:X\leftarrow Y` satisfying
   \[
   (P_iK)R=P_i
   \qquad
   \text{for every }i=0,1,\ldots,m;
   \]
5. consequently, equality for **one** multidistribution divergence whose generator is strictly convex on the relevant likelihood-ratio hull already certifies preservation of the complete finite experiment. It then forces equality for every convex multidistribution `F`-divergence;
6. full finite-experiment sufficiency is equivalent to simultaneous sufficiency of every binary subexperiment `(P_i,P_0)`. Thus preserving one selected prime-versus-control comparison is weaker than preserving a whole matched-control family, while preserving all reference-relative binary likelihood ratios is exactly enough;
7. for a deterministic compression `T:X\to Y`, sufficiency holds exactly when the vector `L` factors through `T`. Hence the partition
   \[
   x\sim x'
   \iff
   L(x)=L(x')
   \]
   is the coarsest deterministic representation that is lossless for the finite experiment, up to relabeling;
8. if `F` is `\mu`-strongly convex on `conv(L(X))` with respect to the Euclidean norm, then the scalar divergence defect quantitatively controls the full vector recovery defect:
   \[
   \Delta_F(K)
   \ge
   \frac{\mu}{2}
   \mathbb E_{P_0}\!\left[
   \|L-\mathbb E_{P_0}[L\mid Y]\|_2^2
   \right].
   \]
   For the quadratic generator
   \[
   F(u)=\|u-\mathbf 1\|_2^2,
   \]
   this is an equality without the factor ambiguity:
   \[
   \Delta_F(K)
   =
   \mathbb E_{P_0}\!\left[
   \|L-\mathbb E_{P_0}[L\mid Y]\|_2^2
   \right];
   \]
9. for a chain of garblings `X -> Y -> Z`, the multidistribution divergence loss is additive and each stage contributes a nonnegative term. Once a strictly convex finite-experiment divergence has dropped, later processing of the retained output alone cannot restore full experiment fidelity.

The multidistribution `f`-divergence and comparison-of-experiments ingredients are classical. The Arithmetic Fidelity consequence is the exact audit boundary they impose: **a family of competing upstream models survives a compression precisely when the full vector of reference-relative likelihood ratios survives.** A single strictly convex scalar multidistribution divergence can certify that whole vector condition because strict convexity tests all directions on the actual likelihood-ratio hull.

## Derivation

### The retained vector is a conditional expectation

Under the reference law `P_0`, the joint distribution of `(X,Y)` is

\[
J_0(x,y)=P_0(x)K(y\mid x).
\]

For `\bar P_0(y)>0`,

\[
P_0(x\mid y)
=
\frac{P_0(x)K(y\mid x)}{\bar P_0(y)}.
\]

For coordinate `i`,

\[
\mathbb E_{P_0}[L_i(X)\mid Y=y]
=
\sum_x
\frac{P_0(x)K(y\mid x)}{\bar P_0(y)}
\frac{P_i(x)}{P_0(x)}
\]

\[
=
\frac{\sum_x P_i(x)K(y\mid x)}{\bar P_0(y)}
=
\frac{\bar P_i(y)}{\bar P_0(y)}
=\bar L_i(y).
\]

Therefore, coordinatewise and hence vectorwise,

\[
\boxed{
\bar L(Y)=\mathbb E_{P_0}[L(X)\mid Y].
}
\]

This is the multi-hypothesis analogue of AF-012's binary likelihood-ratio identity.

### Data processing is multivariate conditional Jensen

The compressed divergence is

\[
D_F(\bar P_1,\ldots,\bar P_m\|\bar P_0)
=
\mathbb E_{P_0}\!\left[
F(\mathbb E_{P_0}[L\mid Y])
\right].
\]

Subtracting from

\[
D_F(P_1,\ldots,P_m\|P_0)
=
\mathbb E_{P_0}[F(L)]
\]

gives

\[
\boxed{
\Delta_F(K)
=
\mathbb E_{P_0}\!\left[
F(L)-F(\mathbb E_{P_0}[L\mid Y])
\right]
\ge 0.
}
\]

Conditional Jensen supplies the inequality. The scalar defect is therefore not measuring generic upstream complexity: it measures the convexity gap created by averaging the **likelihood-ratio vector** inside retained-output supports.

### Strict convexity makes zero loss equivalent to vector monochromaticity

Assume `F` is strictly convex on `conv(L(X))`. Every conditional Jensen gap is nonnegative. The total gap vanishes exactly when Jensen is an equality for every `y` with positive `\bar P_0(y)`.

Strict convexity gives equality exactly when `L(X)` is constant under the conditional law `P_0(\cdot\mid y)`. Because every `P_0(x)>0`, this is equivalent to

\[
K(y\mid x)>0,\ K(y\mid x')>0
\Longrightarrow
L(x)=L(x').
\]

Thus

\[
\boxed{
\Delta_F(K)=0
\iff
L(X)\text{ is exactly recoverable from }Y.
}
\]

The requirement is joint: every coordinate of the likelihood-ratio vector must agree on each output support.

### Vector monochromaticity constructs one reverse channel for all hypotheses

Define the reference-posterior channel

\[
R(x\mid y)
=
\frac{P_0(x)K(y\mid x)}{\bar P_0(y)}
\]

for `\bar P_0(y)>0`, with arbitrary values on outputs that never occur under `P_0`.

By construction,

\[
(\bar P_0R)(x)=P_0(x).
\]

Now assume vector monochromaticity. Whenever `K(y|x)>0`,

\[
\bar L_i(y)=L_i(x)
\]

for every coordinate `i`. Hence

\[
(\bar P_iR)(x)
=
\sum_y \bar P_i(y)
\frac{P_0(x)K(y\mid x)}{\bar P_0(y)}
\]

\[
=
P_0(x)
\sum_y \bar L_i(y)K(y\mid x)
=
P_0(x)L_i(x)
=P_i(x).
\]

The same `R` therefore reconstructs the whole experiment:

\[
\boxed{
(P_iK)R=P_i
\quad\forall i=0,\ldots,m.
}
\]

Conversely, if such an `R` exists, apply multidistribution data processing first through `K` and then through `R`:

\[
D_F(P_1,\ldots,P_m\|P_0)
\ge
D_F(P_1K,\ldots,P_mK\|P_0K)
\]

\[
\ge
D_F(P_1KR,\ldots,P_mKR\|P_0KR)
=
D_F(P_1,\ldots,P_m\|P_0).
\]

Thus every convex multidistribution divergence is preserved by a sufficient channel. Combining the two directions gives

\[
\boxed{
\text{equality for one strictly convex }F
\iff
\text{finite-experiment sufficiency}
\iff
\text{equality for every convex }F.
}
\]

### Full experiment sufficiency is exactly simultaneous binary sufficiency

For each `i`, AF-012 applied to the pair `(P_i,P_0)` says that binary sufficiency is equivalent to constancy of

\[
L_i(x)=\frac{P_i(x)}{P_0(x)}
\]

on every output support of `K`.

If the whole experiment is sufficient, every binary subexperiment is sufficient by restriction. Conversely, if every pair `(P_i,P_0)` is sufficient under the same compression, then every coordinate `L_i` is constant on every output support. Hence the vector `L` is constant there, and the reference-posterior reverse channel above reconstructs all hypotheses simultaneously.

Therefore

\[
\boxed{
K\text{ sufficient for }\{P_0,\ldots,P_m\}
\iff
K\text{ sufficient for every }(P_i,P_0).
}
\]

This gives two equivalent audit modes: one genuinely multivariate strictly convex divergence, or a complete panel of reference-relative binary sufficiency tests.

### Deterministic compression has a canonical minimal quotient

If `K` is induced by `T:X\to Y`, each channel output support is exactly a fiber of `T`. The criterion reduces to

\[
T(x)=T(x')
\Longrightarrow
L(x)=L(x').
\]

Equivalently, there is a map `\ell` on `T(X)` with

\[
L=\ell\circ T.
\]

Thus every sufficient deterministic representation refines the partition into equal vector-likelihood-ratio classes. Conversely, the statistic `x\mapsto L(x)` is itself sufficient because its fibers are vector-monochromatic. Hence the vector likelihood-ratio partition is the coarsest deterministic sufficient representation for this finite dominated experiment, up to relabeling.

### Strong convexity turns scalar loss into a vector recovery bound

Suppose `F` is `\mu`-strongly convex on the relevant hull. For any random vector `V` supported there,

\[
\mathbb E[F(V)]-F(\mathbb E[V])
\ge
\frac{\mu}{2}
\mathbb E\|V-\mathbb E[V]\|_2^2.
\]

Apply this conditionally with `V=L(X)` given `Y` and average over `Y`:

\[
\boxed{
\Delta_F(K)
\ge
\frac{\mu}{2}
\mathbb E_{P_0}
\|L-\mathbb E_{P_0}[L\mid Y]\|_2^2.
}
\]

For

\[
F(u)=\|u-\mathbf1\|_2^2,
\]

the Pythagorean identity for conditional expectation gives exactly

\[
\Delta_F(K)
=
\mathbb E_{P_0}
\|L-\mathbb E_{P_0}[L\mid Y]\|_2^2.
\]

So AF-009's conditional-variance fidelity defect extends naturally from one discriminator to the whole vector of hypothesis discriminators. Strict convexity gives the exact zero set; strong convexity additionally calibrates approximate loss.

### Loss localizes irreversibly along a chain

Let `M:Y\rightsquigarrow Z` be a second stochastic channel. Algebraically,

\[
\Delta_F(KM)
=
\Delta_F(K)
+
\Delta_F(M;P_0K,\ldots,P_mK),
\]

and both terms are nonnegative by data processing. Therefore positive loss at the first stage cannot be cancelled by later garbling.

This is a finite-experiment version of the recurring Arithmetic Fidelity rule: once the relevant discriminator family has been averaged inside a compression fiber/support, downstream processing of the compressed object alone cannot manufacture the missing distinction.

## Why strict convexity across the full vector hull is necessary

A scalar multidistribution divergence can ignore an entire discriminator direction when its generator is degenerate.

Take

\[
X=\{a,b,c\},
\qquad
P_0=(1/3,1/3,1/3),
\]

and define likelihood-ratio coordinates

\[
L_1=(0.8,0.8,1.4),
\qquad
L_2=(0.5,1.1,1.4).
\]

Both coordinates have `P_0`-mean `1`, so

\[
P_1=P_0L_1,
\qquad
P_2=P_0L_2
\]

are strictly positive probability distributions. Let a deterministic compression merge `a` and `b` while retaining `c` separately.

Choose

\[
F(u,v)=(u-1)^2.
\]

This `F` is convex but is completely flat in the `v` direction. Since `L_1(a)=L_1(b)`, its divergence is unchanged by the merge:

\[
\Delta_F=0.
\]

But

\[
L_2(a)=0.5\ne1.1=L_2(b),
\]

so the full vector likelihood ratio is not recoverable and the three-distribution experiment is not sufficient.

Thus

\[
\boxed{
\text{equality of a degenerate convex multidistribution divergence}
\not\Rightarrow
\text{finite-experiment fidelity}.
}
\]

The certification theorem needs strict convexity on the actual likelihood-ratio hull, not merely convexity or sensitivity to one selected coordinate.

## Prior art and novelty assessment

Multidistribution extensions of Csiszár `f`-divergence and their relationship to multiclass Bayes risk and comparison of statistical experiments are established prior art. In particular:

- Dario García-García and Robert C. Williamson, **“Divergences and Risks for Multiclass Experiments,”** *Proceedings of Machine Learning Research* 23, 28.1–28.20 (COLT 2012), develops multidistribution `f`-divergences explicitly through the comparison-of-experiments framework.
- John C. Duchi, Khashayar Khosravi, and Feng Ruan, **“Multiclass Classification, Information, Divergence and Surrogate Risk,”** *Annals of Statistics* 46(6B), 3246–3275 (2018), DOI `10.1214/17-AOS1657`, uses the same multivariate likelihood-ratio / multidistribution-divergence setting for multiclass experiments and quantized representations.
- Classical sufficiency and minimal-sufficiency theory for finite dominated families identifies the collection of reference-relative likelihood ratios as a minimal sufficient statistic; this is standard material in mathematical statistics, including Lehmann and Casella, *Theory of Point Estimation*, 2nd ed. (1998).
- Blackwell comparison of experiments supplies the decision-theoretic meaning of a reversible garbling.

No novelty is claimed for multidistribution `f`-divergence, data processing, likelihood-ratio minimal sufficiency, conditional Jensen, or Blackwell equivalence. I did not locate a source during this audit that makes the exact Arithmetic Fidelity packaging the headline theorem — one strictly convex multidistribution scalar equality as a certificate for the entire finite experiment, together with the explicit vector conditional-expectation and strong-convexity defect bridge — but these statements follow directly from classical ingredients and should be treated as a derived synthesis rather than a new theorem claim.

## Boundary conditions and falsification tests

- Strict positivity is used to avoid support bookkeeping and to make all reference-relative likelihood ratios finite. With zeros, the statement requires the usual extended-value / absolute-continuity conventions.
- Strict convexity is required only on the convex hull of likelihood-ratio vectors actually mixed by the experiment; global strict convexity is stronger than necessary.
- A generator that is strict only in selected coordinates can certify only those discriminator directions, as the explicit three-state counterexample shows.
- The reverse channel is not an arbitrary side-information lift: it is constructed solely from the retained channel and the reference distribution `P_0`.
- Changing the reference from `P_0` to another full-support member reparameterizes the same finite experiment. Sufficiency is reference-independent even though the likelihood-ratio coordinates change.
- The theorem concerns preservation of a declared finite experiment. It does not say that a finite control family captures every mathematically relevant distinction in an upstream object.
- For future arithmetic use, a proposed control family must be fixed independently enough that passing its finite-experiment fidelity test cannot be achieved by encoding the desired prime label directly into the controls or retained mark.

A decisive audit of any attempted application is therefore: specify the finite family of matched upstream models, compute or characterize its vector likelihood-ratio statistic at the information layer immediately before compression, and prove that the proposed retained representation factors that vector. If even one coordinate varies inside a retained fiber/support, no downstream garbling-only mechanism can recover full fidelity for that family.

## Consequences for Arithmetic Fidelity

AF-012 showed that a binary experiment has one canonical decision discriminator, the scalar likelihood ratio. AF-013 shows that a finite family has an equally canonical joint object: the **vector** of reference-relative likelihood ratios.

This matters for the eventual rational-prime stage. A compression may preserve a prime-versus-one-control discriminator while still erasing distinctions against other matched controls. A serious arithmetic fidelity test can therefore be strengthened from

\[
\text{prime model vs one control}
\]

to

\[
\text{prime model vs a finite adversarial control family},
\]

with one exact structural criterion: preserve the whole likelihood-ratio vector before the next compression. The result does not establish any prime-specific theorem, but it gives a rigorous way to prevent success against one convenient control from being mistaken for preservation of the broader arithmetic discriminator.