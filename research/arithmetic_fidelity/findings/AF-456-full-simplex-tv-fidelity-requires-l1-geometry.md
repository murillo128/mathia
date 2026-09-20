# AF-456 — Full-simplex TV fidelity requires ℓ¹ geometry

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `QUANTITATIVE-FIDELITY`, `SOURCE-LAW`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-454 and AF-455 show that a bounded infinite alphabet can retain a positive total-variation margin at the level of **individual atoms** if its carrier remains non-precompact. That is not enough once the admissible source class contains arbitrary mixtures of those atoms.

Let `A` be a countably infinite alphabet and let

\[
\Delta(A)=\left\{\mu\in\ell^1(A):\mu(a)\ge0,\ \sum_{a\in A}\mu(a)=1\right\}.
\tag{1}
\]

Use the total-variation norm convention

\[
\|\mu-\nu\|_{TV}=\|\mu-\nu\|_1,
\tag{2}
\]

so distinct Dirac masses have distance `2`. Let `Y` be a Banach space and let

\[
T:\ell^1(A)\to Y
\tag{3}
\]

be bounded linear. Equivalently, `T` is the barycentric extension of the bounded feature map `\phi(a)=T e_a`.

Define the full-simplex TV conditioning modulus

\[
\kappa_{\Delta}^{TV}(T)
:=
\inf_{\mu\ne\nu\in\Delta(A)}
\frac{\|T(\mu-\nu)\|_Y}{\|\mu-\nu\|_1}.
\tag{4}
\]

Then:

1. **The full probability simplex tests exactly the zero-mass `ℓ¹` subspace.** With
   \[
   \ell^1_0(A)
   :=
   \left\{h\in\ell^1(A):\sum_{a\in A}h(a)=0\right\},
   \tag{5}
   \]
   one has the exact identity
   \[
   \boxed{
   \kappa_{\Delta}^{TV}(T)
   =
   \inf_{0\ne h\in\ell^1_0(A)}
   \frac{\|Th\|_Y}{\|h\|_1}.
   }
   \tag{6}
   \]
   Thus uniform TV fidelity on arbitrary mixtures is equivalent to `T|_{\ell^1_0(A)}` being bounded below.

2. **Positive full-simplex TV fidelity is possible exactly in target spaces containing `ℓ¹`.** Since `A` is countably infinite, `\ell^1_0(A)` is isomorphic to `\ell^1`. Consequently
   \[
   \boxed{
   \exists\,T:\ell^1(A)\to Y\text{ bounded with }\kappa_{\Delta}^{TV}(T)>0
   \iff
   Y\text{ contains an isomorphic copy of }\ell^1.
   }
   \tag{7}
   \]
   This is an existence/category statement for bounded linear or barycentric observations.

3. **Reflexive targets therefore have zero full-simplex TV margin.** A reflexive Banach space cannot contain an isomorphic copy of the nonreflexive space `\ell^1`. Hence every bounded linear
   \[
   T:\ell^1(A)\to Y
   \tag{8}
   \]
   with reflexive target `Y` satisfies
   \[
   \boxed{\kappa_{\Delta}^{TV}(T)=0.}
   \tag{9}
   \]
   In particular this applies to Hilbert spaces and to classical `L^p` / `\ell^p` targets for `1<p<\infty`.

4. **Canonical `ℓ^p` one-hot embeddings have an exact sparse-mixture law.** Let `1\le p<\infty`, let `T_p:\ell^1(A)\to\ell^p(A)` be the canonical coordinate inclusion, and restrict `(4)` to probability measures supported on at most `k` atoms. Then
   \[
   \boxed{
   \kappa_{k,p}^{TV}
   =(2k)^{1/p-1}.
   }
   \tag{10}
   \]
   For Hilbert geometry,
   \[
   \boxed{\kappa_{k,2}^{TV}=\frac1{\sqrt{2k}}.}
   \tag{11}
   \]
   Thus the one-hot Hilbert carrier separates every pair of atoms uniformly, and every fixed-sparsity class remains quantitatively stable, but the margin necessarily collapses as mixture complexity grows.

The reusable Arithmetic Fidelity conclusion is therefore sharper than “infinite dimension can rescue a bounded discrete mark”:

\[
\boxed{
\text{atomwise separation needs non-precompactness, while uniform TV fidelity for arbitrary mixtures needs an }\ell^1\text{-type target geometry.}
}
\tag{12}
\]

## Derivation

### Every zero-mass `ℓ¹` secant is a scaled difference of probability laws

Take nonzero `h\in\ell^1_0(A)` and write its positive and negative parts as

\[
h=h^+-h^-.
\tag{13}
\]

Because `\sum_a h(a)=0`, the two masses agree:

\[
r:=\|h^+\|_1=\|h^-\|_1=\frac12\|h\|_1>0.
\tag{14}
\]

Define

\[
\mu=\frac{h^+}{r},
\qquad
\nu=\frac{h^-}{r}.
\tag{15}
\]

Then `\mu,\nu\in\Delta(A)` and

\[
h=r(\mu-\nu).
\tag{16}
\]

Conversely every difference of two probability laws lies in `\ell^1_0(A)`. Since the quotient in `(4)` is homogeneous, `(16)` proves `(6)` exactly. No density or limiting argument is involved.

Equation `(6)` changes the geometry of the problem. Pairwise atom separation only probes the special secants `e_a-e_b`; full-simplex fidelity probes **every** zero-sum absolutely summable direction.

### The target-space classification is `ℓ¹` containment

Enumerate `A` as `\{a_0,a_1,a_2,\ldots\}`. The map

\[
J:\ell^1(\mathbb N)\to\ell^1_0(A),
\qquad
J(x_1,x_2,\ldots)
=
\left(-\sum_{n\ge1}x_n,x_1,x_2,\ldots\right)
\tag{17}
\]

is a linear bijection. Moreover

\[
\|x\|_1
\le
\|Jx\|_1
=
\left|\sum_{n\ge1}x_n\right|+\|x\|_1
\le
2\|x\|_1.
\tag{18}
\]

Hence `\ell^1_0(A)\cong\ell^1`.

If `\kappa_{\Delta}^{TV}(T)=c>0`, `(6)` gives

\[
\|Th\|_Y\ge c\|h\|_1
\qquad(h\in\ell^1_0(A)).
\tag{19}
\]

Thus `T|_{\ell^1_0(A)}` is an isomorphic embedding with closed range, so `Y` contains a subspace isomorphic to `\ell^1`.

Conversely, if `Y` contains an isomorphic copy of `\ell^1(A)`, choose a bounded-below embedding

\[
E:\ell^1(A)\hookrightarrow Y.
\tag{20}
\]

Then `E` is bounded below on `\ell^1_0(A)` as well, and `(6)` gives `\kappa_{\Delta}^{TV}(E)>0`. This proves `(7)`.

### Reflexive targets fail categorically

Closed subspaces of reflexive Banach spaces are reflexive, while `\ell^1` is not reflexive. Therefore a reflexive `Y` cannot contain the subspace forced by `(19)`, proving `(9)`.

This is a stronger obstruction than AF-455's compact-postprocessing theorem. A noncompact map into a Hilbert space can preserve a positive margin on the discrete atom set, but **no** bounded linear map into any Hilbert space can preserve a fixed positive TV gain over the entire infinite probability simplex.

### Exact sparse-mixture degradation in `ℓ^p`

Let `\mu,\nu` each have support size at most `k` and put `h=\mu-\nu`. Then

\[
|\operatorname{supp}h|\le2k.
\tag{21}
\]

For every vector supported on at most `m` coordinates, Hölder's inequality gives

\[
\|h\|_1\le m^{1-1/p}\|h\|_p.
\tag{22}
\]

Using `m\le2k`,

\[
\frac{\|h\|_p}{\|h\|_1}
\ge
(2k)^{1/p-1}.
\tag{23}
\]

The constant is attained. Choose disjoint `k`-element sets `E,F\subset A` and let `\mu,\nu` be uniform on `E,F`, respectively. Then `h` has `2k` nonzero coordinates of magnitude `1/k`, so

\[
\|h\|_1=2,
\qquad
\|h\|_p=2^{1/p}k^{1/p-1},
\tag{24}
\]

and therefore

\[
\frac{\|h\|_p}{\|h\|_1}
=2^{1/p-1}k^{1/p-1}
=(2k)^{1/p-1}.
\tag{25}
\]

This proves `(10)` and `(11)`.

## Bounded kernel mean embeddings: injectivity is weaker than TV fidelity

A bounded feature map `\phi:A\to H` into a Hilbert space defines the mean embedding

\[
M_\phi(\mu)=\sum_{a\in A}\mu(a)\phi(a),
\tag{26}
\]

which is a bounded linear map from `\ell^1(A)` to `H`. Characteristic kernels can make such an embedding injective on probability measures; injectivity only requires

\[
M_\phi(\mu)=M_\phi(\nu)\Longrightarrow\mu=\nu.
\tag{27}
\]

AF-456 shows that on a countably infinite full simplex no bounded Hilbert-valued mean embedding can satisfy the much stronger uniform estimate

\[
\|M_\phi(\mu)-M_\phi(\nu)\|_H
\ge
c\|\mu-\nu\|_1
\qquad(c>0)
\tag{28}
\]

for all probability laws. Thus **exact identifiability and quantitative TV recoverability are distinct resources**. A characteristic RKHS representation may distinguish every law while arbitrarily different TV directions become arbitrarily close in Hilbert norm.

This does not contradict kernel-embedding results that metrize weak convergence: TV is strictly stronger than weak topology on an infinite alphabet, and `(28)` asks for a uniform lower Lipschitz comparison in that stronger source metric.

## Arithmetic specialization: distributions over rational primes

Let `A=\mathbb P` be the rational primes. AF-454/455's one-hot map

\[
p\mapsto e_p\in\ell^2(\mathbb P)
\tag{29}
\]

retains a fixed positive TV margin for individual prime labels. AF-456 identifies the exact boundary of that escape.

If the admissible source objects are arbitrary probability laws on primes and the downstream representation is the barycentric extension of a bounded prime feature map into a Hilbert or other reflexive Banach space, then

\[
\boxed{\kappa_{\Delta(\mathbb P)}^{TV}=0.}
\tag{30}
\]

So a Hilbert spectral carrier cannot uniformly preserve **all prime-weight information in TV**, even when it is injective and even when its action on individual prime atoms is perfectly separated.

There are three mathematically distinct escapes:

- weaken the source metric from TV to one compatible with the chosen target topology;
- restrict source complexity, for example to `k`-sparse prime mixtures, accepting the quantitative law `(10)`;
- retain a target geometry containing an isomorphic `\ell^1` copy rather than forcing the information through a reflexive/Hilbert representation.

None of these escapes is automatically prime-specific. They are category constraints on what a proposed prime discriminator can preserve before any RH-facing mechanism is considered.

## Relationship to AF-452–AF-455

AF-452 identifies conditioning with the lower gain on completed source-law secants. AF-456 computes those secants exactly for the full probability simplex with TV geometry: their linear span is the whole zero-mass space `\ell^1_0(A)`.

AF-453 shows how weakly collapsing source secants force zero TV conditioning under weakly continuous observations. AF-456 strengthens the message in the bounded linear/barycentric category: even without exhibiting one special collapsing sequence in advance, the target space itself can forbid positive TV gain because it has no `\ell^1` subspace.

AF-454 proves that finite-dimensional bounded images cannot support a uniformly TV-discrete infinite atom family, while infinite-dimensional one-hot Hilbert geometry escapes that atomwise obstruction. AF-456 shows that the escape stops at mixtures: Hilbert geometry can retain the vertices of the probability simplex with fixed separation but cannot retain the entire simplex with fixed TV conditioning.

AF-455 then becomes the atom-level version of a broader category gate. Compactness can destroy even the vertex margin; reflexivity already rules out the stronger full-simplex margin whether or not the downstream map is compact.

## Prior art and novelty audit

All Banach-space and kernel-embedding ingredients are classical. **No theorem-level novelty is claimed.**

- Joram Lindenstrauss and Lior Tzafriri, ***Classical Banach Spaces I and II: Sequence Spaces and Function Spaces***, Classics in Mathematics, Springer (1996 reissue of the classical volumes), DOI `10.1007/978-3-662-53294-2`. Role: standard structural background for classical sequence spaces, `\ell^1`, subspaces, and reflexivity.
- Bharath K. Sriperumbudur, Arthur Gretton, Kenji Fukumizu, Bernhard Schölkopf, and Gert R. G. Lanckriet, **“Hilbert Space Embeddings and Metrics on Probability Measures,”** *Journal of Machine Learning Research* 11 (2010), 1517–1561. Role: direct prior art for embedding probability measures as RKHS mean elements, characteristic kernels, and comparison of the induced Hilbert metric with weak convergence.
- Bharath K. Sriperumbudur, Kenji Fukumizu, and Gert R. G. Lanckriet, **“Universality, Characteristic Kernels and RKHS Embedding of Measures,”** *Journal of Machine Learning Research* 12 (2011), 2389–2410. Role: established injectivity/characteristic-kernel theory for measure embeddings; supplies the precise neighboring notion that AF-456 separates from uniform TV conditioning.

The equivalence `(7)` is an elementary repackaging of classical Banach-space facts: differences of probability measures form the zero-sum `\ell^1` subspace, that subspace is isomorphic to `\ell^1`, and a positive lower gain is exactly an isomorphic embedding. The sparse constant `(10)` is the sharp finite-support `\ell^1`/`\ell^p` norm comparison.

The durable Arithmetic Fidelity contribution is the **source-law interpretation** of those classical ingredients and their placement after AF-454/455: retaining a bounded infinite set of labels and retaining arbitrary mixtures of those labels are categorically different tasks. Non-precompact Hilbert geometry suffices for the former; the latter forces `\ell^1` geometry if TV is the source metric.

## Boundary and falsification audit

- **The theorem is category-specific.** Equation `(7)` concerns bounded linear observations on signed `\ell^1` measures, equivalently bounded-feature barycentric embeddings. A nonlinear encoder on probability laws is not covered.
- **Countable infinitude is load-bearing.** Finite alphabets are finite-dimensional and admit positive margins in many target geometries. The obstruction concerns a uniform constant independent of mixture complexity on an infinite alphabet.
- **TV convention matters only by scale.** Using the probabilists' `\tfrac12\|\mu-\nu\|_1` convention multiplies all displayed conditioning constants by `2` but does not alter any zero/nonzero conclusion.
- **Reflexivity is sufficient for failure, not necessary.** A nonreflexive target can still fail if it contains no isomorphic copy of `\ell^1`; `(7)` gives the exact existence criterion.
- **Containing `ℓ¹` is an ambient possibility, not source-relative sufficiency for a given map.** A particular `T` still needs its restriction to `\ell^1_0(A)` to be bounded below.
- **Characteristic does not mean TV-coercive.** Injective bounded RKHS embeddings are compatible with zero uniform TV margin; there is no contradiction with characteristic-kernel theory.
- **Sparse stability is not full-simplex stability.** Equation `(10)` quantifies precisely how the canonical `\ell^p` route degrades as `k` grows. No fixed positive constant survives for `p>1`.
- **Arithmetic content is not supplied by `ℓ¹`.** An `\ell^1` carrier can preserve arbitrary labels. Any RH-facing application must still identify a natural rational-prime discriminator and show that the relevant downstream operation preserves the required `\ell^1_0` secants rather than merely generic mixture identity.

The next useful question is now more precise: if a natural arithmetic pipeline insists on Hilbert/reflexive spectral geometry, which weaker source metric or restricted family of prime-weight perturbations is actually intrinsic to the target theorem? Conversely, if TV-strength recovery is genuinely required, where can an `\ell^1`-type nonreflexive component survive naturally through the full compression chain?