# AF-473 — Any positive tail budget destroys scale-free Hilbert fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `SOURCE-RESTRICTION`, `APPROXIMATE-SPARSITY`, `NEGATIVE/OBSTRUCTION`, `SHARP-BOUNDARY`, `NO-NOVELTY-CLAIM`

## Claim

AF-472 proves that a **hard** support cap is a genuine positive Hilbert-fidelity resource: the full `s`-sparse probability simplex has exact total-variation/`ell^1` Hilbert distortion `sqrt(s)`, uniformly in the ambient alphabet. A natural next question is whether an approximate support constraint gives a softened version of the same theorem.

It does not, for scale-free multiplicative fidelity.

Let `A` be an infinite alphabet, let `s>=1`, and fix any `epsilon in (0,1)`. Define the soft-sparse class

\[
\Delta_{s,\varepsilon}^{\mathrm{soft}}(A)
=
\left\{
\mu\in\operatorname{Prob}(A):
\exists S\subset A,\ |S|\le s,\ \mu(S)\ge 1-\varepsilon
\right\}
\]

with source metric

\[
d_1(\mu,\nu)=\|\mu-\nu\|_1.
\]

Then

\[
\boxed{
 c_2\!\left(\Delta_{s,\varepsilon}^{\mathrm{soft}}(A),d_1\right)=\infty.
}
\tag{1}
\]

In fact the obstruction already lies inside the `s=1` subclass. For every `k>=1`, `\Delta_{1,\varepsilon}^{\mathrm{soft}}(A)` contains an exact scaled copy of the `k`-dimensional Hamming cube, so every Hilbert embedding of the whole class has distortion at least `sqrt(k)`. Since `k` is arbitrary, no finite bi-Lipschitz distortion exists.

Therefore the positive result in AF-472 has a **singular boundary**: a hard support cap controls metric-cube dimension, whereas allowing an arbitrarily diffuse tail of any fixed positive total mass restores unbounded cube dimension at arbitrarily small absolute scale.

## Exact soft-tail cube

Choose one anchor atom `a_0 in A`. For arbitrary `k`, choose `2k` further distinct atoms

\[
b_1^0,b_1^1,\ldots,b_k^0,b_k^1
\]

disjoint from `a_0`. For each bit vector `sigma in {0,1}^k`, set

\[
q_\sigma
=
\frac1k\sum_{j=1}^k\delta_{b_j^{\sigma_j}}
\]

and

\[
\mu_\sigma
=
(1-\varepsilon)\delta_{a_0}
+\varepsilon q_\sigma.
\tag{2}
\]

Every `mu_sigma` belongs to `\Delta_{1,\varepsilon}^{\mathrm{soft}}(A)`: the one-point set `{a_0}` carries mass exactly `1-epsilon`.

If `sigma,tau` differ in `r` coordinates, then for each differing coordinate a mass `epsilon/k` moves between two disjoint tail atoms. Hence

\[
\boxed{
\|\mu_\sigma-\mu_\tau\|_1
=
\frac{2\varepsilon}{k}\,d_H(\sigma,\tau).
}
\tag{3}
\]

Thus the `2^k` laws in `(2)` are an exact metric copy of the Hamming cube multiplied by the scalar `2epsilon/k`. Bi-Lipschitz distortion is invariant under multiplication of the source metric by a positive scalar.

Enflo's classical cube inequality gives

\[
c_2(\{0,1\}^k,d_H)=\sqrt{k}.
\tag{4}
\]

Therefore any map of `\Delta_{1,\varepsilon}^{\mathrm{soft}}(A)` into Hilbert space that is bi-Lipschitz on the whole class has distortion at least `sqrt(k)` for every `k`. This proves `(1)`. Since

\[
\Delta_{1,\varepsilon}^{\mathrm{soft}}(A)
\subset
\Delta_{s,\varepsilon}^{\mathrm{soft}}(A),
\]

the conclusion holds for every `s>=1`.

The argument is fully nonlinear: it constrains arbitrary Hilbert-valued embeddings, not merely affine, barycentric, coordinate, kernel-mean, or spectral encodings.

## Finite-alphabet quantitative form

The same construction gives an exact finite-size lower bound. If the alphabet has at least `2k+1` atoms, then

\[
\boxed{
 c_2\!\left(\Delta_{s,\varepsilon}^{\mathrm{soft}}(A),d_1\right)
\ge \sqrt{k}
\qquad (s\ge1).
}
\tag{5}
\]

Equivalently, with `m=|A|`, one may take

\[
k\le \left\lfloor\frac{m-1}{2}\right\rfloor.
\]

The lower bound is independent of how small the positive tail mass `epsilon` is. Shrinking `epsilon` shrinks every bad-cube distance by the same factor, but multiplicative distortion does not see that common scale.

This is the exact point at which approximate sparsity differs from hard sparsity for the present fidelity notion.

## Relation to AF-464 and AF-472

AF-464 shows that a source class containing paired-mixture Hamming cubes cannot have complexity-independent nonlinear Hilbert fidelity. AF-472 then identifies a positive source restriction that cuts those cubes off: if every law has support at most `s`, the largest paired-support cube has dimension at most the support resource being paid for, and the elementary coordinate embedding achieves the matching `sqrt(s)` distortion.

AF-473 shows that replacing the hard support condition by

\[
\text{“at least }1-\varepsilon\text{ of the mass lies on }s\text{ atoms”}
\]

does **not** interpolate continuously between the unrestricted and hard-sparse cases. The small tail can encode arbitrarily many independent binary choices. Those choices live at source scale `O(epsilon)`, but their metric dimension is unbounded.

Consequently,

\[
\boxed{
\varepsilon=0
\text{ and }
\varepsilon>0
\text{ are qualitatively different for uniform multiplicative TV fidelity.}
}
\tag{6}
\]

For `epsilon=0`, AF-472 gives the finite sharp cost `sqrt(s)`. For every fixed `epsilon>0` on an infinite alphabet, `(1)` gives infinite distortion.

This is not a contradiction with ordinary approximation intuition. Approximate sparsity controls **absolute tail mass**; bi-Lipschitz fidelity asks for a uniform multiplicative comparison at **every nonzero scale**. The tail cube becomes small in diameter as `epsilon->0`, but remains geometrically just as non-Hilbertian after rescaling.

## Prior-art and novelty audit

The metric ingredient is classical. **No novelty is claimed for Hamming-cube distortion, Enflo's inequality, or general sparse-approximation theory.** The same metric-embedding sources already audited in AF-464 and AF-472 apply here:

- Per Enflo, **“On the nonexistence of uniform homeomorphisms between `L_p`-spaces,”** *Arkiv för Matematik* 8 (1969), 103--105, DOI `10.1007/BF02589549`, supplies the classical cube obstruction behind the Hilbert lower bound.
- Paata Ivanisvili, Ramon van Handel, and Alexander Volberg, **“Rademacher type and Enflo type coincide,”** *Annals of Mathematics* 192(2), 665--678 (2020), DOI `10.4007/annals.2020.192.2.8`, gives the modern metric-type framework used in AF-464.
- Standard approximate-sparsity and compressed-sensing literature studies recovery under small tails, but generally with additive approximation terms, restricted signal classes, or scale-dependent guarantees rather than a uniform all-scales bi-Lipschitz embedding of this full soft-sparse TV class.

A targeted prior-art search recovered the classical Hamming-cube/Hilbert obstruction and extensive approximate-sparsity literature, but did not identify a reason to promote the elementary anchored-tail construction `(2)` as a new theorem of metric geometry. The Arithmetic Fidelity contribution is the boundary statement it gives for the live source question: **a nonzero tail budget is not a weakened hard-support certificate for scale-free multiplicative Hilbert fidelity.**

## Boundary and falsification audit

- **Infinite ambient supply is load-bearing for the infinite-distortion conclusion.** A finite alphabet admits only finitely many disjoint tail pairs; equation `(5)` is the corresponding finite lower bound.
- **Positive tail mass is load-bearing.** At `epsilon=0` the construction collapses and AF-472's hard-support theorem applies.
- **The theorem is scale-free and multiplicative.** It does not rule out additive-error recovery of the form `d_1 <= C d_Hilbert + O(epsilon)`, nor guarantees that deliberately ignore distinctions below a declared absolute resolution.
- **The obstruction lives at small absolute scale.** Every cube in `(2)` has diameter `2epsilon`. A coarse embedding whose lower-control requirement begins only above that scale is outside the claim.
- **The source class is the full soft-sparse family.** A narrower arithmetic subclass may forbid independent tail switches. Such a prohibition would be genuine source rigidity and requires its own positive theorem.
- **The target is Hilbert.** Type-1 targets, metric transforms such as the square-root repair classified in AF-467--AF-471, or enriched marked targets that change the represented distance require separate audits.
- **No collision is forced.** As in AF-464, the result is about conditioning. Injective encodings may exist while their inverse Lipschitz constant degenerates on increasingly fine tail structure.
- **Entropy or decay assumptions are not settled by this theorem.** They may restrict the number or weight pattern of independent tail switches. The correct question is whether they impose a quantitative bound on metric-cube dimension at the scale consumed by the downstream theorem.

## Arithmetic-fidelity consequence

For a prime-derived probability carrier, saying that “almost all mass sits on finitely many important primes” is insufficient to justify a scale-free Hilbert compression. If the residual arithmetic tail can independently redistribute even an arbitrarily small fixed mass across indefinitely many prime pairs, it can carry Hamming cubes of unbounded dimension and the inverse TV conditioning must diverge.

This sharpens the source-side gate after AF-472. A viable approximate-sparsity argument must now specify what kind of fidelity the downstream mathematics really needs. If it needs uniform multiplicative recovery down to arbitrarily small scales, the tail must be eliminated or structurally constrained, not merely made small in total mass. If additive error, finite resolution, anchored recovery, or another scale-aware criterion is sufficient, the positive theorem must price that weaker requirement explicitly.

The general lesson is that **small amount of lost mass does not imply small amount of lost structural complexity**. A compression theorem must control both amplitude and the number of independently variable relations that can hide inside that amplitude.