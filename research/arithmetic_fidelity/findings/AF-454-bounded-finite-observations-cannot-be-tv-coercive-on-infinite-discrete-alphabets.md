# AF-454 — Bounded finite observations cannot be TV-coercive on infinite discrete alphabets

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `QUANTITATIVE-FIDELITY`, `SOURCE-LAW`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-453 shows that total-variation conditioning fails whenever admissible atoms can move continuously while finite continuous observations coalesce. A natural escape is to make the source alphabet genuinely discrete. That removes the moving-atom witness, but it is not enough by itself: **an infinite discrete alphabet still cannot have a positive uniform total-variation margin through a bounded finite-dimensional observation.** The output must itself retain a uniformly discrete mark.

Let `A` be an infinite set of admissible atom locations and let `Y` be a metric space. For a feature map

\[
\Phi:A\to Y,
\]

consider one-atom probability sources `\delta_x` and the source total-variation norm

\[
\|\delta_x-\delta_y\|_{TV}=2\qquad(x\ne y).
\tag{1}
\]

Define the one-atom total-variation conditioning modulus

\[
\kappa_A^{TV}(\Phi)
=
\inf_{x\ne y\in A}
\frac{d_Y(\Phi(x),\Phi(y))}
{\|\delta_x-\delta_y\|_{TV}}
=
\frac12\inf_{x\ne y\in A}d_Y(\Phi(x),\Phi(y)).
\tag{2}
\]

Then:

1. **Exact classification.**
   \[
   \boxed{
   \kappa_A^{TV}(\Phi)>0
   \iff
   \Phi(A)\text{ is uniformly discrete in }Y
   }
   \tag{3}
   \]
   with the understood requirement that `Phi` be injective on `A`.

2. **Precompact-target obstruction.** If `\Phi(A)` is totally bounded, then
   \[
   \boxed{
   \kappa_A^{TV}(\Phi)=0.
   }
   \tag{4}
   \]
   Thus exact injectivity of `Phi` on the entire infinite alphabet can coexist with zero uniform total-variation conditioning.

3. **Bounded finite-dimensional corollary.** Let `Y` be a real normed space of finite dimension `d>=1`. If `\Phi(A)` is bounded, then it is totally bounded, so `(4)` applies. Therefore no bounded finite list of real-valued features can be uniformly TV-coercive on an infinite one-atom alphabet. The same statement for `m` complex features uses real dimension `d=2m`.

4. **Quantitative packing law.** Suppose `x_1,\ldots,x_N` are distinct admissible atoms and the observation vectors lie in one norm ball
   \[
   \Phi(x_i)\in B_Y(y_0,R)
   \qquad(1\le i\le N)
   \tag{5}
   \]
   in a `d`-dimensional real normed space. Then
   \[
   \boxed{
   \min_{i\ne j}
   \|\Phi(x_i)-\Phi(x_j)\|_Y
   \le
   \frac{2R}{N^{1/d}-1}
   }
   \tag{6}
   \]
   for `N>1`, hence
   \[
   \boxed{
   \kappa_{\{x_1,\ldots,x_N\}}^{TV}(\Phi)
   \le
   \frac{R}{N^{1/d}-1}.
   }
   \tag{7}
   \]
   Equivalently, if a bounded `d`-dimensional observation has TV margin at least `c>0` on `N` distinct atoms, then necessarily
   \[
   \boxed{
   N\le\left(1+\frac Rc\right)^d.
   }
   \tag{8}
   \]

5. **Fixed-source-law version.** If an infinite subset `A` lies in one source-law level set `A\subseteq\Psi^{-1}(v)`, the same obstruction holds inside that one-atom source-law fiber. More generally, if a common background `rho` and fixed `tau in (0,1]` complete all atoms in `A` into another prescribed source-law fiber,
   \[
   \mu_x=\tau\delta_x+(1-\tau)\rho,
   \tag{9}
   \]
   then the normalized TV gain is unchanged:
   \[
   \frac{\left\|\int\Phi\,d(\mu_x-\mu_y)\right\|_Y}
   {\|\mu_x-\mu_y\|_{TV}}
   =
   \frac{\|\Phi(x)-\Phi(y)\|_Y}{2}.
   \tag{10}
   \]
   Thus common-background completion can transport the obstruction between source-law fibers but cannot repair it.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{discreteness of the source removes AF-453's moving-atom obstruction, but positive TV fidelity on an infinite alphabet requires the retained representation itself to carry an infinite uniformly discrete mark.}
}
\tag{11}
\]

In particular, a bounded finite-dimensional compression cannot do this. One must instead spend another resource: restrict to a finite source class, allow an unbounded finite-dimensional mark, retain an infinite-dimensional bounded representation with a uniformly separated image, or weaken the source metric.

## Exact derivation

### 1. Total variation turns distinct Dirac atoms into a discrete source metric

For distinct points `x,y`, the signed measure `delta_x-delta_y` has positive and negative parts `delta_x` and `delta_y`, so

\[
\|\delta_x-\delta_y\|_{TV}=2.
\]

Therefore every distinct pair has exactly the same source distance and `(2)` follows. A positive lower gain is consequently equivalent to the existence of `eta>0` such that

\[
d_Y(\Phi(x),\Phi(y))\ge2\eta
\qquad\forall x\ne y\in A.
\tag{12}
\]

That is exactly uniform discreteness of the image. This proves `(3)` and also makes the representation requirement explicit: source discreteness does not survive merely because `A` is discrete; it survives only if the observation image remains uniformly separated.

### 2. Total boundedness forbids an infinite uniformly separated image

Suppose `Phi(A)` is totally bounded and assume for contradiction that `(12)` holds for some `eta>0`. Total boundedness supplies a finite cover of `Phi(A)` by balls of radius `eta/2`. Each such ball can contain at most one point of `Phi(A)`, because two points in the same ball would be at distance strictly below `eta`, hence below the required `2eta` separation after reducing constants if necessary.

Thus `Phi(A)` would be finite. If `Phi` is injective this contradicts infinitude of `A`; if `Phi` is not injective, `(2)` already has numerator zero for a distinct source pair. In either case `kappa_A^{TV}(Phi)=0`, proving `(4)`.

This argument uses no topology on the source alphabet. `A` may be uniformly discrete, countable with no finite accumulation point, or an arithmetic set such as the rational primes. The obstruction lives entirely in the mismatch between the discrete TV source geometry and a precompact output geometry.

### 3. Boundedness becomes precompactness in finite dimension

Every bounded subset of a finite-dimensional normed space is totally bounded. Therefore if `Y` has finite real dimension and `Phi(A)` is bounded, `(4)` applies immediately.

The finite-dimensional hypothesis is load-bearing. A bounded subset of an infinite-dimensional normed space need not be totally bounded. For example the orthonormal sequence `(e_n)` in `ell^2` is bounded and uniformly separated, so the map

\[
x_n\mapsto e_n
\tag{13}
\]

can preserve a positive discrete margin for infinitely many labels while keeping the output norm bounded. This is not a counterexample to `(4)`: the image in `(13)` is not totally bounded.

Hence the actual resource boundary is **precompactness**, not bounded amplitude by itself. Finite dimensionality converts bounded amplitude into precompactness automatically.

### 4. Volumetric packing gives the finite-capacity law

Let

\[
\rho
=
\min_{i\ne j}
\|\Phi(x_i)-\Phi(x_j)\|_Y.
\tag{14}
\]

If `rho=0`, `(6)` is immediate. Otherwise the open norm balls

\[
B_Y(\Phi(x_i),\rho/2)
\]

are pairwise disjoint. By `(5)` they all lie inside

\[
B_Y(y_0,R+\rho/2).
\]

Choose any Lebesgue measure on the `d`-dimensional vector space. Volumes of norm balls scale as the `d`-th power of their radius, so disjointness gives

\[
N\left(\frac\rho2\right)^d
\le
\left(R+\frac\rho2\right)^d.
\tag{15}
\]

Taking `d`-th roots and rearranging,

\[
\left(N^{1/d}-1\right)\rho
\le2R,
\]

which is `(6)`. Division by the Dirac TV distance `2` gives `(7)`. If the TV lower gain is at least `c`, then every output pair is separated by at least `2c`; combining this with `(6)` yields `(8)`.

Equation `(8)` is a finite-dimensional representation-capacity bound. It is not a statement about computation or decoder quality. It says that a bounded target region has only finite packing capacity at any fixed positive fidelity margin.

## Source-law and common-background audit

Let `Psi:A->R^q` be a source-law map. If infinitely many atoms share the same value `v`, then the one-atom sources `delta_x` for `x in Psi^{-1}(v)` all belong to one fixed source-law fiber, and the theorem applies there without modification.

Suppose instead that the desired prescribed law is `u` and there is one common probability background `rho` such that for fixed `tau`

\[
\tau\Psi(x)+(1-\tau)\int\Psi\,d\rho=u
\qquad\forall x\in A.
\tag{16}
\]

This requires `Psi` to be constant on the transported atom family `A`; it is not automatic for arbitrary source laws. For completed sources `(9)`, subtraction gives

\[
\mu_x-\mu_y
=
\tau(\delta_x-\delta_y).
\]

Absolute homogeneity of total variation and linearity of the feature readout give

\[
\|\mu_x-\mu_y\|_{TV}=2\tau,
\qquad
\left\|\int\Phi\,d(\mu_x-\mu_y)\right\|_Y
=
\tau\|\Phi(x)-\Phi(y)\|_Y,
\]

proving `(10)`. This is the discrete-alphabet counterpart of AF-452's completed-secant identity.

The conclusion must not be overstated: a source law that already assigns a distinct retained value to every atom can make each relevant level set finite or singleton. In that case the source law itself has already retained the identity that the theorem says a bounded finite observation cannot recover uniformly from an infinite TV-discrete fiber.

## Arithmetic specialization: bounded finite prime features

Take an infinite arithmetic alphabet such as the rational primes `P` or their logarithms. Give distinct one-prime sources the TV geometry inherited from Dirac measures. Let

\[
\Phi(p)
=
(\phi_1(p),\ldots,\phi_m(p))
\tag{17}
\]

be any finite family of bounded real or complex features. Then the image lies in a bounded finite-dimensional set and

\[
\boxed{
\inf_{p\ne q}
\frac{\|\Phi(p)-\Phi(q)\|}{\|\delta_p-\delta_q\|_{TV}}
=0.
}
\tag{18}
\]

This applies, for example, to any finite collection of unit-modulus phase marks

\[
p\mapsto(e^{-it_1\log p},\ldots,e^{-it_m\log p})
\tag{19}
\]

and to finite families of other bounded normalized kernels. Exact injectivity of the joint feature map, if it happens, does not change `(18)`.

The statement is deliberately about the declared observation resource. It does **not** say that the primes cannot be uniformly separated by any finite-dimensional map. The raw mark `p` itself is unbounded and separates distinct primes by at least `1`; an integer label or another unbounded coordinate can therefore evade the bounded-target obstruction. But such a mark is not a compression that forgot location identity: it retains an ever-growing absolute label. Likewise an infinite-dimensional bounded one-hot representation can separate all primes, but it spends dimension rather than amplitude.

Thus the arithmetic question becomes sharper. If a proposed prime discriminator uses finitely many bounded global/spectral coordinates while the physical source metric is TV on an unbounded discrete prime alphabet, a positive uniform margin is impossible before any deeper number theory enters. A viable TV formulation must declare which additional resource prevents output precompactness or else weaken the source metric.

## Relationship to AF-452 and AF-453

AF-452 shows that for difference-homogeneous source metrics, common backgrounds do not change the normalized conditioning ratio; they only determine which residual secants can be completed into the prescribed source-law fiber. Equation `(10)` is exactly that mechanism on one-atom discrete secants.

AF-453 then proves that TV conditioning vanishes whenever a source fiber contains weakly collapsing secants of nonzero TV size, with nearby moving atoms as the canonical witness. It explicitly leaves a discrete/quantized source alphabet as a possible escape.

AF-454 closes one part of that escape:

\[
\boxed{
\begin{array}{ll}
\text{non-discrete source fiber:}
&\text{continuous atom motion already kills TV gain (AF-453);}\\[1mm]
\text{infinite discrete source fiber + precompact output:}
&\text{output packing already kills TV gain (AF-454).}
\end{array}}
\tag{20}
\]

Therefore a positive TV margin on an infinite discrete arithmetic source requires more than source discreteness. The retained observation must have non-precompact range on that source class. In finite dimension this means, at minimum, that its amplitude cannot remain uniformly bounded.

This is compatible with AF-210 rather than contradictory to it. AF-210 obtains finite norming observations only after compactifying a normalized source class in a weaker geometry where the continuum observation already has a positive coercivity margin. Here the source itself is an infinite uniformly discrete TV family. Such a family is not precompact in TV, so a bounded finite-dimensional image cannot preserve its discrete separation.

## Prior art and novelty audit

The mathematical ingredients are classical, and no theorem-level novelty is claimed.

- Dmitri Burago, Yuri Burago, and Sergei Ivanov, *A Course in Metric Geometry*, Graduate Studies in Mathematics 33, American Mathematical Society (2001), ISBN `978-0-8218-2129-9`, is standard background for total boundedness, compactness, finite nets, separated sets, and metric packing. The implication used in `(4)` -- a totally bounded metric space cannot contain an infinite uniformly separated subset -- is elementary metric-space theory.
- A. N. Kolmogorov and V. M. Tikhomirov, **“epsilon-entropy and epsilon-capacity of sets in function spaces,”** *Uspekhi Mat. Nauk* 14(2) (1959), 3--86; English translation *American Mathematical Society Translations*, Series 2, 17 (1961), 277--364, is foundational prior art for describing compactness and finite-dimensional representation capacity through covering and packing numbers. Equation `(6)` is only the elementary volume-packing estimate for a finite-dimensional norm ball, not a new entropy theorem.
- Mathias Hockmann and Stefan Kunis, **“Weak Sparse Superresolution Is Well-Conditioned,”** *SIAM Journal on Imaging Sciences* 16(1), SC1--SC13 (2023), DOI `10.1137/22M1521353`, supplies a useful neighboring contrast: replacing strong atomic norms by Wasserstein geometry can restore global Lipschitz conditioning under sparse-source assumptions. AF-454 concerns the opposite choice -- retaining TV on a discrete alphabet -- and identifies the output packing resource then required.

A targeted prior-art search found the relevant pieces under standard total-boundedness, metric-entropy, packing, and metric-embedding language. Search absence is not used as a novelty claim. The durable Arithmetic Fidelity contribution is the exact resource accounting relative to AF-453: **discretizing the source fixes the local topology mismatch but does not make bounded finite compression uniformly faithful; the missing discriminator must reappear as output separation, which costs amplitude, dimension, or a finite source restriction.**

## Boundaries and falsification checks

- **The theorem concerns uniform lower-Lipschitz TV fidelity.** It does not rule out exact injectivity, pointwise recovery, nonuniform conditioning, or finite-prefix guarantees whose margin decays with prefix size.
- **Total boundedness, not boundedness alone, is the abstract obstruction.** Bounded infinite-dimensional targets can contain infinite uniformly separated sets.
- **Finite-dimensional boundedness is sufficient, not necessary, for failure.** An unbounded finite-dimensional image may still have zero separation; non-precompactness merely removes this particular no-go.
- **Discrete source topology is not assumed.** The theorem only uses the TV geometry of distinct Dirac measures. Calling the alphabet “discrete” refers to the admissible location class having no continuous source motion; the proof itself works for any infinite set of distinct atoms.
- **The packing law depends on target dimension and radius.** It is not invariant under arbitrary nonlinear rescaling of the observation. Such rescaling changes the declared observation geometry and therefore the physical fidelity question.
- **A finite source class is different.** Any injective map on finitely many atoms has a positive minimum output separation, although that margin can shrink with source-class size according to `(7)` when the target remains bounded.
- **A uniquely identifying source-law coordinate is an upstream mark.** If `Psi` already isolates every source atom, the theorem should not be presented as a downstream failure inside singleton fibers.
- **No rational-prime specificity follows.** Equation `(18)` applies equally to any infinite discrete alphabet. Its role is to eliminate a universal compression regime before asking whether arithmetic structure can supply a stronger non-precompact mark.

## Research consequence

AF-453 left “use an intrinsically discrete arithmetic source” as one plausible way to keep total variation as the physical metric. AF-454 shows that this is only half of the requirement. For an infinite discrete source, the output representation must also resist precompactness.

The next arithmetic-fidelity test can therefore be made falsifiable: for any proposed finite prime representation intended to support a **uniform** TV margin, first classify the range of the retained features. If that range is bounded in finite dimension, the route is closed by `(4)` before testing primes against non-prime controls. If the range is non-precompact, identify exactly which resource creates that non-precompactness -- growing amplitude, increasing dimension, a retained discrete label, or another structural mark -- and then test whether matched non-prime systems possess the same resource.

This turns “discrete primes might save TV conditioning” into a sharper gate. **Source discreteness prevents continuous atom collapse; output non-precompactness is additionally necessary to preserve that discreteness through compression.**