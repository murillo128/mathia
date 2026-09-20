# AF-457 — Bounded Hilbert marks have sharp `k^{-1/2}` sparse-mixture TV fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `QUANTITATIVE-FIDELITY`, `SOURCE-LAW`, `SHARP`, `NO-NOVELTY-CLAIM`

## Claim

AF-456 computes the exact `k`-sparse total-variation modulus of the canonical one-hot embedding into `ℓ²`, namely `1/√(2k)`, but by itself does not say whether a more ingenious bounded Hilbert feature map can do better. On a countably infinite alphabet, it cannot.

Let `A` be countably infinite, let `H` be a real or complex Hilbert space, and let

\[
\phi:A\to H,
\qquad
\sup_{a\in A}\|\phi(a)\|\le M<\infty.
\tag{1}
\]

Extend `φ` barycentrically to finitely supported probability laws by

\[
F_\phi(\mu)=\sum_{a\in A}\mu(a)\phi(a).
\tag{2}
\]

For `k\ge1`, let `\Delta_k(A)` denote the probability measures supported on at most `k` atoms, and use the AF-456 convention

\[
\|\mu-\nu\|_{TV}=\|\mu-\nu\|_1.
\tag{3}
\]

Define

\[
\kappa_k^{TV}(\phi)
:=
\inf_{\substack{\mu\ne\nu\\ \mu,\nu\in\Delta_k(A)}}
\frac{\|F_\phi(\mu)-F_\phi(\nu)\|_H}{\|\mu-\nu\|_1}.
\tag{4}
\]

Then every bounded Hilbert-valued atom mark satisfies the universal sharp ceiling

\[
\boxed{
\kappa_k^{TV}(\phi)\le \frac{M}{\sqrt{2k}}.
}
\tag{5}
\]

The constant is optimal. For the canonical orthogonal marking

\[
\phi(a)=M e_a\in\ell^2(A),
\tag{6}
\]

one has

\[
\boxed{
\kappa_k^{TV}(\phi)=\frac{M}{\sqrt{2k}}.
}
\tag{7}
\]

Thus, among all bounded Hilbert carriers with the same per-atom norm budget, orthogonal one-hot marking already maximizes the worst-case TV conditioning of `k`-sparse mixtures. The `k^{-1/2}` degradation is not an artifact of that representation: it is forced by Hilbert geometry on every infinite alphabet.

Equivalently, if `H` is allowed to be infinite dimensional,

\[
\boxed{
\sup_{\sup_a\|\phi(a)\|\le M}
\kappa_k^{TV}(\phi)
=
\frac{M}{\sqrt{2k}}.
}
\tag{8}
\]

For finite-dimensional `H`, the situation is strictly worse: bounded subsets are precompact, so already `\kappa_1^{TV}(\phi)=0` for every map from an infinite alphabet, in agreement with AF-454.

## Derivation

### A bounded infinite Hilbert family contains an asymptotically orthogonal centered subsequence

Choose pairwise distinct atoms `a_n\in A` and write

\[
x_n=\phi(a_n).
\tag{9}
\]

The sequence is bounded by `M`. Hilbert spaces are reflexive, so after passing to a subsequence,

\[
x_n\rightharpoonup x
\tag{10}
\]

weakly. Passing to a further subsequence if necessary, assume also that `\|x_n\|` converges to some `L\le M`. Put

\[
y_n=x_n-x.
\tag{11}
\]

Then `y_n\rightharpoonup0`, and

\[
\|y_n\|^2
=
\|x_n\|^2+\|x\|^2-2\operatorname{Re}\langle x_n,x\rangle
\longrightarrow
L^2-\|x\|^2
=:r^2.
\tag{12}
\]

Hence

\[
0\le r\le M.
\tag{13}
\]

Fix `k` and `\varepsilon>0`. Because `y_n` is weakly null, one can inductively choose `2k` terms, relabelled `y_1,\ldots,y_{2k}`, such that

\[
\|y_i\|^2\le r^2+\varepsilon,
\qquad
|\langle y_i,y_j\rangle|\le\varepsilon
\quad(i\ne j).
\tag{14}
\]

Indeed, after finitely many terms have been fixed, weak convergence makes the inner product of a sufficiently late term with every previously chosen vector arbitrarily small. Thus every bounded infinite Hilbert mark has arbitrarily large finite blocks which, after subtracting a common weak limit, are almost orthogonal.

### Two disjoint uniform `k`-mixtures force the ceiling

Use the corresponding `2k` atoms to define

\[
\mu=\frac1k\sum_{i=1}^{k}\delta_{a_i},
\qquad
\nu=\frac1k\sum_{i=k+1}^{2k}\delta_{a_i}.
\tag{15}
\]

Their supports are disjoint, so

\[
\|\mu-\nu\|_1=2.
\tag{16}
\]

Let `\sigma_i=1` for `1\le i\le k` and `\sigma_i=-1` for `k<i\le2k`. Since `\sum_i\sigma_i=0`, the common weak limit cancels exactly:

\[
F_\phi(\mu)-F_\phi(\nu)
=
\frac1k\sum_{i=1}^{2k}\sigma_i x_i
=
\frac1k\sum_{i=1}^{2k}\sigma_i y_i.
\tag{17}
\]

Using `(14)`,

\[
\begin{aligned}
\|F_\phi(\mu)-F_\phi(\nu)\|^2
&=
\frac1{k^2}
\left(
\sum_{i=1}^{2k}\|y_i\|^2
+2\sum_{i<j}\sigma_i\sigma_j\operatorname{Re}\langle y_i,y_j\rangle
\right)\\
&\le
\frac{2k(r^2+\varepsilon)+2\binom{2k}{2}\varepsilon}{k^2}.
\end{aligned}
\tag{18}
\]

For every `\varepsilon>0` there is such a pair `(\mu,\nu)`. Letting `\varepsilon\downarrow0` in the infimum gives

\[
\inf_{\mu\ne\nu\in\Delta_k(A)}
\|F_\phi(\mu)-F_\phi(\nu)\|
\le
\sqrt{\frac{2}{k}}\,r
\le
\sqrt{\frac{2}{k}}\,M
\tag{19}
\]

for pairs with source distance exactly `2`. Dividing by `(16)` proves `(5)`:

\[
\kappa_k^{TV}(\phi)
\le
\frac{M}{\sqrt{2k}}.
\tag{20}
\]

The proof is stronger than a dimension count. It identifies the geometric mechanism: after removing a common weak limit, bounded Hilbert families necessarily contain arbitrarily large almost-orthogonal blocks, and balanced barycentric averaging reduces their distinguishability by the square-root law.

### Orthogonal marking attains the bound exactly

For `(6)`, put `h=\mu-\nu`. If `\mu,\nu\in\Delta_k(A)`, then

\[
|\operatorname{supp}h|\le2k.
\tag{21}
\]

Cauchy--Schwarz therefore gives

\[
\|h\|_1\le\sqrt{2k}\,\|h\|_2,
\tag{22}
\]

and hence

\[
\frac{\|F_\phi(\mu)-F_\phi(\nu)\|_2}{\|\mu-\nu\|_1}
=
M\frac{\|h\|_2}{\|h\|_1}
\ge
\frac{M}{\sqrt{2k}}.
\tag{23}
\]

Equality is attained by two disjoint uniform `k`-point laws, for which `h` has `2k` coordinates of magnitude `1/k`. This proves `(7)` and the sharp envelope `(8)`.

## What this adds to AF-456

AF-456 established two facts: full-simplex TV fidelity forces an `ℓ¹` target geometry, while canonical one-hot `ℓ²` retains a `1/√(2k)` margin on `k`-sparse mixtures. AF-457 closes the obvious representation escape: **no alternative bounded Hilbert feature design can beat that worst-case scale or constant** on an infinite alphabet under the same atom-norm budget.

The distinction is important. AF-456 could still be read as saying that the one-hot carrier is merely a convenient Hilbert representation whose mixture conditioning happens to degrade. AF-457 shows that the degradation belongs to the target geometry itself. Orthogonality is already optimal; changing the Hilbert coordinates, kernel features, spectral marks, or other bounded atom vectors cannot produce a uniformly larger worst-case TV margin over `k`-sparse mixtures.

This also sharpens the separation between three resources:

- atomwise injectivity or separation;
- bounded-complexity mixture stability;
- full-simplex TV stability.

Hilbert space can provide the first and, for every fixed `k`, the second, but the best possible second resource decays exactly as `k^{-1/2}`; AF-456 shows the third vanishes altogether as complexity becomes unbounded.

## Prior art and novelty audit

The square-root scale is classical convex- and Banach-space geometry. **No novelty is claimed for the geometric rate.**

- Grigory Ivanov, **“No-dimension Tverberg's theorem and its corollaries in Banach spaces of type p,”** *Bulletin of the London Mathematical Society* 53(2), 631–641 (2021), DOI `10.1112/blms.12449`. Ivanov develops dimension-free Radon/Tverberg/Carathéodory statements from Banach-space type and Maurey's lemma. In the Hilbert/Euclidean case the neighboring approximate-Carathéodory scale is `O(k^{-1/2})`; the paper explicitly situates these results as no-dimension convex-geometry theorems.
- Vahab Mirrokni, Renato Paes Leme, Adrian Vladu, and Sam Chiu-wai Wong, **“Tight Bounds for Approximate Carathéodory and Beyond,”** *Proceedings of the 34th International Conference on Machine Learning*, PMLR 70, 2440–2448 (2017). Their approximate-Carathéodory bounds give sparse convex approximation with `O(1/\sqrt{k})` Euclidean error and establish tight sparse-approximation behavior in the relevant `ℓ_p` settings.

These results show that the dimension-free `k^{-1/2}` phenomenon is established mathematics, not an Arithmetic Fidelity discovery. The exact statement `(5)`--`(8)` is a line-specific reformulation: the source object is a pair of `k`-sparse probability laws, the source metric is `ℓ¹`/TV, the observation is an affine Hilbert mean map with a fixed per-atom norm budget, and the quantity optimized is its worst-case lower Lipschitz modulus. The weak-subsequence proof above is self-contained and makes the exact constant and the optimality of one-hot marking explicit in that language.

The broader Banach-space prior art also warns against treating the exponent as universal across target categories. Type-`p` spaces have related Maurey/no-dimension rates of order `k^{-1+1/p}`, while `ℓ¹` lies on the qualitatively different boundary already isolated by AF-456: full-simplex TV fidelity can remain bounded below there.

## Boundary and falsification audit

- **The alphabet must be infinite for the universal ceiling.** The proof uses an infinite bounded sequence and weak subsequential compactness. A fixed finite alphabet is a finite coding problem whose optimum can depend on its cardinality and target dimension.
- **The atom-norm budget is essential.** Without a bound such as `(1)`, arbitrary rescaling makes any absolute target margin meaningless. Equation `(5)` is homogeneous in `M`.
- **The result is specific to affine/barycentric observation.** A nonlinear encoding of an entire probability law is not constrained by this theorem merely because its codomain is Hilbert.
- **The result is a worst-case statement.** It does not say that every pair of `k`-sparse laws is distorted by `k^{-1/2}`. It says every bounded Hilbert feature family contains some pair whose gain is at most the sharp value.
- **Finite-dimensional Hilbert targets are worse, not counterexamples.** Bounded images are precompact, so an infinite atom family has zero atomwise TV modulus already at `k=1`.
- **Source-law restrictions can remove the bad secants.** AF-452 shows that a fixed affine source-law fiber tests only completable source-law secants. AF-457 transfers to such a fiber only when the balanced disjoint `k`-mixture cores used above are actually completable inside that fiber; this must be proved for the concrete source law rather than assumed.
- **Compact downstream processing cannot improve the margin.** AF-455 supplies the complementary postprocessing obstruction: once a Hilbert carrier is sent through a compact bounded operator, even atomwise infinite-alphabet margins collapse.
- **Pairwise atom separation is insufficient.** The optimal one-hot construction already has perfect orthogonal atom marking, yet its mixture margin still decays exactly as `(7)`.

## Arithmetic specialization

Take `A=\mathbb P`, the rational primes. For any bounded Hilbert-valued prime mark

\[
\phi:\mathbb P\to H,
\qquad
\sup_p\|\phi(p)\|\le M,
\tag{24}
\]

the affine representation of prime-weight distributions satisfies

\[
\boxed{
\kappa_k^{TV}(\phi)\le\frac{M}{\sqrt{2k}}.
}
\tag{25}
\]

Therefore a proposal that first assigns each rational prime a bounded Hilbert/spectral feature and later represents a `k`-term prime mixture only by its barycenter cannot maintain a complexity-independent TV discriminator. This remains true even if every individual prime is perfectly distinguishable and even if the feature space is infinite dimensional.

The result is **not prime-specific evidence** and does not advance RH by itself. Its role is a category gate. Any RH-facing mechanism that needs stable recovery of increasingly complex prime mixtures must either exploit a more restricted source-law secant family, weaken the source metric, leave the affine Hilbert category, or retain an `ℓ¹`-type geometry rather than expecting a better bounded Hilbert embedding to remove the square-root loss.

## Consequence for the line

The sparse-mixture branch now has an exact Hilbert benchmark rather than a representation-dependent example:

\[
\boxed{
\text{bounded Hilbert target} + \text{affine }k\text{-mixtures}
\Longrightarrow
\text{best possible worst-case TV gain}=\Theta(k^{-1/2}),
}
\tag{26}
\]

with the exact universal optimum `M/√(2k)` under the norm convention `(3)` and an infinite-dimensional target. The next meaningful question is therefore not whether a different bounded Hilbert mark can beat one-hot. It is whether the *actual admissible arithmetic source law* generates enough of these balanced sparse secants to force the same decay, or whether its completed secant family is genuinely thinner in a way that a downstream operator can exploit.