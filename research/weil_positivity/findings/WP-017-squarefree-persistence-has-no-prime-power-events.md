# WP-017 — Square-free persistence has no prime-power events

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the canonical persistent/relative-Hodge continuation of the Prime-Lattice square-free exponent filtration. Persistent Laplacians, their positivity, persistent-Betti nullity, and their Schur-complement/effective-resistance interpretation are standard prior art. The durable Mathia-specific obstruction is simpler and exact: the canonical square-free filtration changes only at square-free integers, so every standard persistence or relative-Hodge observable built only from that filtration is locally constant at every proper prime power `p^k`, `k>=2`. The finite Weil distribution instead has a nonzero atom at every such `p^k`. Persistence therefore cannot repair WP-016's support mismatch without first adding exponent/multiplicity data not present in the square-free complex.

## 1. The filtration has an exact event set

For `X>=1`, let

\[
\Delta_X
=
\left\{
S\subset\mathbb P\text{ finite}:
\prod_{p\in S}p\le X
\right\}.
\tag{1}
\]

This is the square-free Prime-Lattice energy cutoff from PL-022/WP-016, since

\[
\sum_{p\in S}\log p\le\log X
\quad\Longleftrightarrow\quad
\prod_{p\in S}p\le X.
\]

The filtration event at an integer `n` is completely rigid.

- If `n` is not square-free, then

\[
\boxed{\Delta_n=\Delta_{n-1}.}
\tag{2}
\]

Indeed, a simplex is indexed by a square-free integer, so no simplex has filtration value `n`.

- If

\[
n=q_1\cdots q_r
\]

is square-free, exactly one new simplex enters at `X=n`, namely

\[
\sigma_n=\{q_1,\ldots,q_r\}.
\tag{3}
\]

Every proper face of `sigma_n` corresponds to a proper divisor of `n`, hence is already in `Delta_{n-1}`.

Thus, with the continuous parameter `t=log X`, the complete critical-value set of the canonical square-free filtration is

\[
\boxed{\{\log n:n\text{ square-free}\}.}
\tag{4}
\]

In particular, for every prime `p` and every `k>=2`,

\[
\boxed{
\Delta_{p^k}=\Delta_{p^k-1},
}
\tag{5}
\]

so there is no filtration event at `k log p`.

## 2. This already contradicts the finite Weil support

The exact finite-place coefficient measure isolated in WP-004 is

\[
\mu_{\mathrm{Weil,fin}}
=
\sum_{p}\sum_{k\ge1}
\frac{\log p}{p^{k/2}}\,\delta_{k\log p}.
\tag{6}
\]

Every proper prime power contributes a strictly nonzero atom:

\[
\mu_{\mathrm{Weil,fin}}(\{k\log p\})
=
\frac{\log p}{p^{k/2}}>0,
\qquad k\ge2.
\tag{7}
\]

Now take any standard persistence/relative construction whose input is only the filtered simplicial complex `Delta_t` and its inclusion maps, and which is unchanged when those inputs are unchanged. This includes persistent homology, mapping-cone/relative homology, standard persistent Laplacians, and Schur-complement/effective-resistance responses derived from those Laplacians.

Across a threshold where (2) holds, both the object and the inclusion morphism are literally unchanged. Hence every such observable is locally constant there; any atomic jump or distributional derivative with respect to `t` can be supported only on (4).

At a proper prime power, the one-step relative object is especially explicit:

\[
C_*(\Delta_{p^k},\Delta_{p^k-1})=0,
\qquad k\ge2,
\tag{8}
\]

and the mapping cone of the identity inclusion is acyclic. Therefore the canonical square-free persistence channel has **zero local response exactly where the Weil finite distribution has the nonzero value (7)**.

This is a support obstruction, not an asymptotic mismatch or a failure of a particular normalization. No positive theorem for the same square-free persistence object can manufacture the missing `p^2,p^3,\ldots` events without importing additional data beyond that filtration.

## 3. The cross-level persistent Laplacian is positive but records the wrong local statistic

The persistence escape left open by WP-016 is not vacuous: standard persistent Laplacians really do provide a positive cross-level operator.

For an inclusion `K\hookrightarrow L`, write the standard degree-`q` persistent Laplacian schematically as

\[
\Delta_q^{K,L}
=
\partial_{q+1}^{L,K}(\partial_{q+1}^{L,K})^*
+
(\partial_q^K)^*\partial_q^K.
\tag{9}
\]

It is positive semidefinite because

\[
\langle x,\Delta_q^{K,L}x\rangle
=
\| (\partial_{q+1}^{L,K})^*x\|^2
+
\|\partial_q^Kx\|^2
\ge0.
\tag{10}
\]

Mémoli, Wan, and Wang show that its nullity equals the persistent Betti number and relate the operator to Schur complements and, in the graph case, effective resistance. Thus positivity, boundary elimination, and cross-scale topology are all genuinely available here without RH.

But the exact one-step update in the Prime-Lattice square-free filtration shows what that positivity sees. Let `n=q_1...q_r` be square-free with `r>=2`, put

\[
K=\Delta_{n-1},\qquad L=\Delta_n,
\qquad q=r-2,
\]

and orient the new `(r-1)`-simplex `sigma_n`. Since every face of `sigma_n` already lies in `K`, the persistent up-boundary domain gains precisely one basis vector. If

\[
b_n=\partial\sigma_n\in C_q(K),
\]

then the degree-`q` persistent Laplacian satisfies

\[
\boxed{
\Delta_q^{K,L}=\Delta_q^K+b_nb_n^*.
}
\tag{11}
\]

With the canonical orthonormal oriented-face basis,

\[
\boxed{
\operatorname{Tr}(b_nb_n^*)=\|b_n\|^2=r=\omega(n).
}
\tag{12}
\]

So the most immediate positive cross-level energy is a rank-one update at square-free `n`, of size `omega(n)`. At `p^k`, `k>=2`, there is no update at all. The local statistic is therefore square-free incidence/prime-factor count, not

\[
\Lambda(p^k)=\log p.
\]

Positive Schur complements can reorganize the response of an existing update, but they cannot create a filtration event at a parameter where the underlying complex and boundary matrix do not change.

## 4. Matched controls show the sign theorem is universal

The positivity in (10) does not use arithmetic. For any positive weights `(a_j)` on an abstract vertex set, the Boolean threshold filtration

\[
\Delta_t(a)
=
\left\{
S:\sum_{j\in S}a_j\le t
\right\}
\tag{13}
\]

has the same construction. When a single simplex enters, the corresponding persistent up-Laplacian receives the same positive rank-one boundary update.

Replacing

\[
a_p=\log p
\]

by generic, randomized, or density-matched positive weights preserves the sum-of-squares positivity theorem and the Schur-complement machinery. The arithmetic specialization controls **where** the subset-sum events occur, but the sign theorem itself does not distinguish primes from a generic weighted Boolean filtration.

This is the same structural warning seen repeatedly in this research line: a universal positive operator is not an arithmetic positivity mechanism merely because it is evaluated on prime-labelled data.

## 5. The full exponent multicomplex is a real escape, but it changes the problem

The obstruction above is deliberately specific to the canonical square-free simplicial filtration. Prime Lattice also has the full exponent down-set

\[
M_X
=
\left\{
\alpha\in\mathbb N_0^{(\mathbb P)}:
\sum_p\alpha_p\log p\le\log X
\right\},
\tag{14}
\]

which does change at every integer and therefore contains the proper prime-power events missing from `Delta_X`.

Björner gives a CW realization of this all-integer multicomplex, with one cell per integer and divisibility represented by cell inclusion. But his full CW realization depends on a choice of a well-connected CW string; unlike the square-free abstract simplicial complex, the detailed chain-level geometry is not uniquely supplied by the exponent poset alone. A Laplacian or persistent Laplacian on that realization therefore requires additional incidence/metric choices whose canonicity must be justified.

Even after such a choice, the generic positive-Hodge theorem remains universal and the full filtration has one event at **every** integer. Recovering exactly the von Mangoldt selector — zero off prime powers and `log p` on `p^k` — would still require an extra Mathia-native operation, such as a rigorously justified analogue of the WP-004 axis projection. Standard persistence positivity by itself supplies no such selector.

Thus (14) is not ruled out; rather, it identifies the price of escaping (5): one must reintroduce exponent multiplicity and then derive both a canonical chain-level geometry and the prime-power selector before any archimedean/global completion is addressed.

## 6. Prior art and novelty audit

The ingredients are classical or established.

- Anders Björner's number-theoretic complex is exactly the square-free filtration (1), and his all-integer multicomplex supplies the broader CW escape in (14).
- Facundo Mémoli, Zhengchao Wan, and Yusu Wang develop persistent Laplacians for inclusions/filtrations, prove persistent-Betti nullity, and establish the Schur-complement/effective-resistance connection. Therefore `persistent Laplacian -> positive cross-level response` is prior art, not a Mathia discovery.
- Searches combining Björner's number-theoretic complex with persistent homology/persistent Laplacians did not identify a reliable source making the exact support comparison (4)--(7). No novelty claim is made from that absence.

The durable contribution is only the **Mathia-specific no-go calculation**: the most canonical persistence refinement of the WP-016 square-free Hodge object has no events at proper prime powers and therefore cannot carry the finite Weil distribution even before the archimedean and polar terms are considered.

## 7. Boundary conditions and adversarial escape tests

### Use long persistence intervals instead of one-step jumps

This does not change the event set. Births, deaths, spectral changes, and inclusion maps can change only when `Delta_t` changes. A long interval can correlate different square-free events but cannot create a new critical value at `k log p` where the filtration is constant.

### Apply an explicit function of the scale parameter

Multiplying a persistence invariant by a hand-chosen function of `t`, differentiating an external kernel, or inserting atoms at prime-power scales can of course create new support. But then the support is supplied by that external operation rather than by the square-free persistence geometry. Such an operation remains admissible only if Mathia forces it independently and it survives the branch's no-hand-picked-kernel gate.

### Encode multiplicity by repeating vertices or using the full exponent lattice

This escapes the theorem because it changes the object. It is exactly the move from `Delta_X` to `M_X`. The burden then shifts to deriving a canonical positive chain complex and a prime-power/archimedean local-to-global structure from that richer object.

### Use a sheaf, local coefficients, or an adelic decoration

A decoration can attach nontrivial data to a filtration value where the underlying simplex set is unchanged, but that data is additional structure. Such a route remains live if the decoration is intrinsic and independently produces the missing prime-power and infinite-place terms. WP-017 does not rule it out.

## 8. Consequence for the Weil-positivity search

WP-016 showed that ordinary Hodge positivity cancels out of the Mertens supertrace and explicitly left cross-level persistence/mapping-cone constructions as a possible escape. The most canonical such escape is now closed:

```text
square-free Prime-Lattice filtration
    -> standard persistent/relative Hodge theory
    -> unconditional positive Laplacians / Schur complements
    -> events only at square-free integers
    -> no p^k event for k >= 2
    -> cannot equal the finite Weil prime-power distribution.
```

A surviving cohomological route must therefore use more than the square-free Björner filtration. At minimum it must retain exponent multiplicity, derive the prime-power selector and `log p / p^{k/2}` normalization from the geometry, and then produce the archimedean/polar sector from the same global object with an independent sign theorem.

## 9. Falsification checklist

Withdraw or narrow this finding if any of the following fails:

1. `Delta_X` is indexed exactly by square-free integers `<=X`;
2. therefore `Delta_n=Delta_{n-1}` for every nonsquare-free integer `n`;
3. at a square-free `n=q_1...q_r`, exactly one simplex enters and all its proper faces are already present;
4. the standard persistent Laplacian is positive semidefinite and depends only on the relevant chain spaces/boundary maps;
5. equation (11) is the one-simplex update for `r>=2`;
6. the finite Weil distribution has a nonzero atom `(log p)p^{-k/2}` at every proper prime power;
7. the full multicomplex escape indeed adds multiplicity data not contained in the square-free simplicial filtration.

All support statements above are exact and independent of RH, zeta zeros, numerical experiments, or analytic continuation.

## Internal dependencies

- `research/prime_lattice/findings/PL-022-bjorner-exponent-cell-complex-hodge-obstruction.md`
- `research/weil_positivity/findings/WP-004-prime-lattice-axis-compression-realizes-finite-weil-weight.md`
- `research/weil_positivity/findings/WP-016-prime-lattice-hodge-positivity-cancels-out-of-the-arithmetic-supertrace.md`
