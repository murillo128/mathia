# PL-236 — Fixed-color exchangeable completion forces finite-prime separability

## Claim

`PL-235` closes fixed finite arithmetic colorings only for **normal trace-class equilibrium on the finite-support integer Hilbert space**. Its explicit boundary leaves open the ordinary quasi-local tensor completion, where nonnormal permutation-invariant states exist. In the most direct completed model, however, independent exchangeability inside infinite color classes still cannot create irreducible quantum coupling among finitely observed nonexceptional prime coordinates.

Let

\[
\mathcal P=E\sqcup\bigsqcup_{j\in J} C_j,
\]

where every `C_j` used below is infinite, and let a finite-dimensional one-prime Hilbert space `h` be attached to each nonexceptional prime. This includes the square-free/hard-core sector `h=C^2` and every fixed finite occupation cutoff. Form the ordinary quasi-local tensor product over the prime sites, and let `Phi` be a state invariant under every finite permutation of sites inside each `C_j`.

Then for every finite set of nonexceptional primes

\[
F=\{p_1,\ldots,p_N\}\subset\mathcal P\setminus E,
\]

the marginal `rho_F` on `h^{\otimes N}` is **fully separable**. Equivalently, it lies in the closed convex hull of product states

\[
\rho_F\in\operatorname{conv}
\{\rho_1\otimes\cdots\otimes\rho_N\}.
\]

The reason is exact: infinite within-color permutation symmetry supplies locally symmetric extensions of `rho_F` to arbitrarily many copies of each of its first `N-1` parties, and the multipartite completeness theorem of Doherty--Parrilo--Spedalieri says that this property alone forces full separability. Their theorem does **not** require the extensions to satisfy the stronger PPT condition.

For the full exponent one-site space `h=ell^2(N_0)`, the same construction still gives complete bipartite extendability. The infinite-dimensional theorem of Bhat--Parthasarathy--Sengupta therefore implies a rigorous weaker statement without any finite-occupation cutoff: if `A` is any finite block of primes contained in one infinite color class and `B` is any disjoint finite block, the marginal `rho_{A:B}` is separable across the cut `A|B`. The finite-dimensional result above is stronger because multipartite local symmetric extendability upgrades this to full separability of every finite nonexceptional marginal.

Thus the most direct completion escape left by `PL-235` is closed for the square-free prime hypercube and for every fixed finite occupation model: **fixed arithmetic colors plus exact within-color exchangeability cannot hide finite-prime quantum entanglement in the completed tensor system.**

**Evidence/status:** `EXACT-DERIVED + LITERATURE-ANCHORED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

No novelty is claimed for local symmetric extensions, their completeness as a separability criterion, quantum de Finetti/shareability, or the abstract colored-site specialization. The durable value is the exact application to the live completion boundary of `PL-235`.

## 1. Infinite color classes manufacture arbitrary local symmetric extensions

Fix a finite nonexceptional set

\[
F=\{p_1,\ldots,p_N\}
\]

and write `c(i)` for the color index with `p_i in C_{c(i)}`. Choose any integer `k>=1`. For each `i<N`, choose `k` distinct sites

\[
p_i^{(1)},\ldots,p_i^{(k)}\in C_{c(i)}
\]

so that all chosen sites are pairwise distinct, including when several of the original `p_i` have the same color. This is possible because every relevant color class is infinite and only finitely many replicas are required. Keep `p_N` unreplicated.

Restrict `Phi` to the finite tensor product carried by these replicas and `p_N`. Denote the resulting density matrix by `rho_(k,...,k,1)`. Every permutation of the `k` replicas belonging to one fixed party `i` is realized by a finite permutation inside `C_{c(i)}` that fixes all other selected sites. Hence

\[
\rho_{(k,\ldots,k,1)}
\]

is invariant under the independent copy-permutation groups required for a locally symmetric extension.

Its one-copy marginal is `rho_F`. To see this when several parties share the same color, note that the finite symmetric group of one infinite class is highly transitive on finite ordered tuples of distinct sites: a finite within-color permutation can send the chosen representative tuple back to the original tuple while fixing every site outside that color. Therefore the restriction to one replica of each party has exactly the same joint state as the original `F`-marginal.

Consequently `rho_F` has a locally symmetric extension with copy vector

\[
(k,k,\ldots,k,1)
\]

for **every** `k>=1`.

## 2. Multipartite completeness converts extendability into full separability

Doherty, Parrilo and Spedalieri define a locally symmetric extension (LSE) of an `N`-partite state precisely by the two properties just obtained: invariance under permutations of the copies of each party and recovery of the original state after tracing the extra copies. Their Theorem 1, “Multipartite Completeness,” proves:

> If a finite-dimensional multipartite state has LSEs with copy vectors `(k,k,...,k,1)` for all `k>=1`, then the state is fully separable.

The source is Andrew C. Doherty, Pablo A. Parrilo and Federico M. Spedalieri, “Detecting multipartite entanglement,” *Physical Review A* **71** (2005), 032333, DOI `10.1103/PhysRevA.71.032333`, arXiv `quant-ph/0407143`. The distinction from their stronger finite-level PPT tests matters here: their completeness theorem is explicitly stated for ordinary LSEs, so no unproved positivity-under-partial-transpose assumption is being imported into the prime model.

Applying that theorem to the extensions constructed in Section 1 gives

\[
\boxed{\rho_F\ \text{is fully separable for every finite }F\subset\mathcal P\setminus E.}
\]

This is a local statement about every finite set of prime coordinates. The global quasi-local state itself need not be normal with respect to a chosen infinite tensor-product representation, and no Gibbs trace is assumed. The conclusion therefore survives precisely the completion move that evades the trace-class orbit argument of `PL-235`.

Full separability does **not** mean statistical independence. A decomposition

\[
\rho_F=\sum_r t_r\,\rho_{1,r}\otimes\cdots\otimes\rho_{N,r}
\]

may have a nontrivial classical mixing variable `r`, and connected classical correlations can remain. What disappears is finite-prime quantum entanglement or any irreducible finite-prime correlation that requires a nonseparable density matrix.

## 3. Fixed congruence and Frobenius colors inherit the obstruction

For a fixed modulus `m`, take

\[
E=\{p:p\mid m\},
\qquad
C_a=\{p\nmid m:p\equiv a\pmod m\},
\]

with `a` a reduced residue class. Dirichlet's theorem makes every `C_a` infinite. Therefore every finite marginal involving primes away from `m` is fully separable in any finite-dimensional local completion that is invariant under arbitrary permutations inside each residue class.

For a fixed finite Galois extension `L/Q`, take `E` to be the finite ramified set and color each unramified prime by its Frobenius conjugacy class. Chebotarev gives positive density, hence infinitude, for every conjugacy class that occurs. The same conclusion follows for finite marginals supported on unramified primes.

The exceptional finite set `E` is deliberately not overclaimed. If a finite marginal also includes exceptional sites, they may be grouped into one unextended final party in the Doherty--Parrilo--Spedalieri theorem. This still forces separability between the replicated nonexceptional prime parties and that composite exceptional block, but it does not force the exceptional sites to be mutually separable inside their finite block. A finite exceptional sector is therefore the only place where this fixed-color argument can leave genuinely quantum finite-site structure.

## 4. The full exponent completion still loses every one-color entanglement cut

The exact prime lattice has the infinite-dimensional one-site Hilbert space

\[
h=\ell^2(\mathbb N_0),
\]

so the finite-dimensional multipartite theorem above should not be silently extrapolated to it. There is nevertheless a direct infinite-dimensional consequence.

Let `A` be any finite collection of sites contained in a single infinite color class `C_j`, and let `B` be any disjoint finite collection of prime sites. Regard the local Hilbert space of `A` as one composite subsystem. For every `k`, choose `k` disjoint copies of the entire finite block `A` inside `C_j`. Within-color exchangeability makes the restriction invariant under permutations of these `k` block copies and leaves the `A:B` marginal unchanged. Hence `rho_{A:B}` is completely extendable with respect to `A`.

B. V. Rajarama Bhat, K. R. Parthasarathy and Ritabrata Sengupta, “On the equivalence of separability and extendability of quantum states,” *Reviews in Mathematical Physics* **29** (2017), 1750012, DOI `10.1142/S0129055X1750012X`, arXiv `1601.02365`, prove that complete extendability is equivalent to bipartite separability in the relevant general Hilbert-space setting, extending the finite-dimensional de Finetti argument. Therefore

\[
\boxed{\rho_{A:B}\ \text{is separable whenever }A\text{ is a finite block from one infinite color}.}
\]

This rules out every entanglement cut that isolates finitely many coordinates of one color from a finite complement in the untruncated exponent completion. It does **not** by itself prove a single fully separable decomposition for an arbitrary finite marginal spanning three or more colors in infinite local dimension; that stronger infinite-dimensional multipartite statement is not used here.

## 5. Prior-art and matched-control audit

The mechanism is established quantum-information/operator-algebra prior art, not a new arithmetic theorem. The exact finite-dimensional theorem used above is already the main completeness result of Doherty--Parrilo--Spedalieri. Their proof is built from the strengthened quantum de Finetti machinery of Fannes--Lewis--Verbeure and related work. Bhat--Parthasarathy--Sengupta supplies the infinite-dimensional bipartite extension used only for the explicit boundary statement.

A bounded literature search did not identify a separate RH or rational-prime application of this multipartite extendability theorem. That absence is not evidence of novelty. More importantly, the argument has a perfect generic control: replace rational primes by any countable set partitioned into infinite color classes, keep the same ordinary tensor product and the same within-class permutation symmetry, and every step goes through unchanged.

Therefore the separability conclusion contains no zeta continuation, no zero divisor, no functional equation and no prime-norm information. Its role is purely falsificatory: it shows that completion does not turn fixed-color exchangeability into the missing rational-prime coupling.

## 6. Exact boundaries and decisive tests

The result requires **exact** finite-permutation invariance inside each relevant infinite color class. Approximate exchangeability, a symmetry subgroup too small to generate arbitrarily deep extensions, or a scale-dependent symmetry can evade the argument.

The full finite-marginal separability conclusion uses finite-dimensional one-site spaces. It therefore covers the square-free `{0,1}` hypercube exactly and every fixed finite exponent cutoff, but not the complete `N_0` one-site space. For the latter, only the rigorously stated bipartite one-color-cut consequence is claimed here.

A fixed finite coloring is the canonical application, but finiteness of the global color set is not the real mathematical input. For any particular finite marginal, the proof only needs each color class from which replicas are drawn to be infinite. What fails for scale-growing residue/Galois labels is that no fixed infinite exchangeability block need persist in the limit.

Nonlocal algebras, crossed products, adelic relations, exact `log p` weights, prime order/gap relations, or other source-forced couplings imposed **before** state selection are outside the theorem. So are constructions in which different primes of the same arithmetic color remain individually distinguishable by an injective label.

The finding should be withdrawn or narrowed if any of the following fails: (1) the global within-color symmetry does not yield an LSE for arbitrarily large `k`; (2) the representative marginal changes when replicas are chosen inside a color class; (3) the multipartite completeness theorem does not apply to the finite-dimensional local state constructed here; (4) a relevant residue or Frobenius class is finite; or (5) complete bipartite extendability fails to imply separability in the infinite-dimensional boundary statement. The first two follow from the permutation action and infinitude of the classes; the third is exactly Theorem 1 of Doherty--Parrilo--Spedalieri; the arithmetic applications use Dirichlet and Chebotarev; and the fifth is the cited complete-extendability theorem.

## Consequence for the research line

`PL-233` showed that full prime exchangeability collapses normal finite-support states to the vacuum; `PL-234` showed that the ordinary fully exchangeable completion becomes a de Finetti product mixture; and `PL-235` showed that fixed finite arithmetic coloring still cannot support normal trace-class equilibrium because every color block remains infinite.

The natural remaining repair was to combine the two escapes: keep a fixed arithmetic coloring **and** move to the quasi-local completion, hoping that nonnormal quantum correlations between the color sectors recover the source information lost by normality. In the finite-dimensional local models relevant to the square-free hypercube, that route is now closed at every finite observational scale: separate within-color exchangeability supplies arbitrary local symmetric extensions, and arbitrary local symmetric extendability forces full separability.

A surviving source-before-equilibrium mechanism must therefore break the replica supply itself or leave the ordinary tensor-product setting: retain the exact prime norm or another injective label, refine arithmetic colors with scale, impose a genuinely nonlocal arithmetic relation, or use a target-relative structure whose finite marginals are not generated by fixed-color exchangeability. Fixed finite labels followed by exchangeable completion do not provide the missing RH-sensitive coupling.