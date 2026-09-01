# AF-033 — Marginal scenarios form an exact simplicial fidelity lattice

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let

\[
\Omega_d=\{-1,+1\}^d,
\]

let `M(\Omega_d)` be the real vector space of finite signed measures on `\Omega_d`, and let

\[
\mathcal H\subseteq 2^{[d]}
\]

be any family of coordinate sets whose marginals are retained. Write

\[
\Delta(\mathcal H)
=
\{S\subseteq[d]: S\subseteq A\text{ for some }A\in\mathcal H\}
\]

for its downward closure. When `\mathcal H` is nonempty, `\Delta(\mathcal H)` is an abstract simplicial complex containing `\varnothing`. Define

\[
\mathsf M_{\mathcal H}(\mu)
=
\bigl((\pi_A)_*\mu\bigr)_{A\in\mathcal H},
\]

where `\pi_A` is coordinate projection.

For `S\subseteq[d]`, let

\[
\chi_S(x)=\prod_{i\in S}x_i,
\qquad
m_S(\mu)=\int_{\Omega_d}\chi_S(x)\,d\mu(x),
\]

and define the Walsh basis signed measures

\[
\eta_S(\{x\})=2^{-d}\chi_S(x).
\]

Then the exact information content of an arbitrary coordinate-marginal scenario is classified by the simplicial complex `\Delta=\Delta(\mathcal H)`.

1. **Only the downward closure matters.** Retaining a marginal on `A` automatically determines every submarginal on `S\subseteq A`. Hence
   \[
   \boxed{
   \mathsf M_{\mathcal H}
   \quad\text{and}\quad
   \mathsf M_{\Delta}
   \text{ induce exactly the same fibers.}
   }
   \]
   Equivalently, the maximal faces `\operatorname{Fac}(\Delta)` are an irredundant coordinate-channel description of the same information state: every nonmaximal retained marginal is already a deterministic pushforward of a facet marginal.

2. **Arbitrary-scenario Walsh theorem.** For any signed measures `\mu,\nu`,
   \[
   \boxed{
   \mathsf M_{\mathcal H}(\mu)=\mathsf M_{\mathcal H}(\nu)
   \iff
   m_S(\mu)=m_S(\nu)
   \quad\forall S\in\Delta.
   }
   \]
   Thus the retained interaction coordinates are exactly the faces of the downward-closed scenario.

3. **Exact kernel.** Since `m_R(\eta_S)=\delta_{R,S}`,
   \[
   \boxed{
   \ker\mathsf M_{\mathcal H}
   =
   \operatorname{span}\{\eta_S:S\notin\Delta\}.
   }
   \]
   Every missing face is therefore an independent ambient ambiguity direction.

4. **Every missing face gives a genuine probability collision.** For any nonempty `S\notin\Delta` and `0<\theta\le1`, define
   \[
   P_{S,\theta}^{\pm}(\{x\})
   =
   2^{-d}\bigl(1\pm\theta\chi_S(x)\bigr).
   \]
   Then `P_{S,\theta}^{+}` and `P_{S,\theta}^{-}` are distinct probability measures with
   \[
   \boxed{
   \mathsf M_{\mathcal H}(P_{S,\theta}^{+})
   =
   \mathsf M_{\mathcal H}(P_{S,\theta}^{-}),
   }
   \]
   while their `S`-moments have opposite sign. The kernel classification is therefore not a signed-measure artifact.

5. **Factorization order is exactly simplicial inclusion.** For two downward-closed scenarios `\Delta_1,\Delta_2`,
   \[
   \boxed{
   \mathsf M_{\Delta_1}
   \text{ factors deterministically through }
   \mathsf M_{\Delta_2}
   \iff
   \Delta_1\subseteq\Delta_2.
   }
   \]
   Consequently coordinate-marginal information states, modulo deterministic equivalence, form the distributive lattice of abstract simplicial complexes on `[d]` under inclusion. The joint observation of two states is their union `\Delta_1\cup\Delta_2`; their greatest common marginal coarsening is `\Delta_1\cap\Delta_2`.

6. **Nested loss has an exact quotient.** If `\Delta_1\subseteq\Delta_2`, then
   \[
   \ker\mathsf M_{\Delta_2}
   \subseteq
   \ker\mathsf M_{\Delta_1}
   \]
   and
   \[
   \boxed{
   \ker\mathsf M_{\Delta_1}/\ker\mathsf M_{\Delta_2}
   \cong
   \operatorname{span}\{\eta_S:S\in\Delta_2\setminus\Delta_1\}.
   }
   \]
   Discarding from `\Delta_2` to `\Delta_1` loses exactly the interaction coordinates indexed by the removed faces and no others.

7. **Target-relative fidelity is a support test.** Let
   \[
   g=\sum_{S\subseteq[d]}\widehat g(S)\chi_S
   \]
   and define the linear discriminator
   \[
   D_g(\mu)=\int g\,d\mu.
   \]
   Then on all signed measures, and likewise on all probability measures,
   \[
   \boxed{
   D_g\text{ is exactly recoverable from }\mathsf M_{\Delta}
   \iff
   \operatorname{supp}_{W}(g)
   :=\{S:\widehat g(S)\ne0\}
   \subseteq\Delta.
   }
   \]
   For a family of target observables, exact recovery is equivalent to containing the union of their Walsh supports.

8. **Minimal marginal lifts reduce exactly to set cover.** Suppose the current scenario is `\Delta`, let `\mathcal G` be a target family, and put
   \[
   R=\bigcup_{g\in\mathcal G}\operatorname{supp}_{W}(g),
   \qquad
   U=R\setminus\Delta.
   \]
   Let `\mathcal A_{\rm adm}` be a declared family of admissible new marginal channels with positive costs `c(A)`. Adding marginals on `\mathcal L\subseteq\mathcal A_{\rm adm}` recovers every target in `\mathcal G` iff
   \[
   \boxed{
   \forall S\in U\ \exists A\in\mathcal L:\ S\subseteq A.
   }
   \]
   Therefore the minimum-cost exact marginal lift is precisely the weighted set-cover problem with universe `U` and cover sets
   \[
   C_A=\{S\in U:S\subseteq A\}.
   \]
   It is enough to cover the inclusion-maximal members of `U`, because covering a maximal missing interaction automatically covers every missing target interaction below it.

   If every coordinate set is admissible and the resource is only the largest arity of any added marginal, then for `U\ne\varnothing` the exact minimum is
   \[
   \boxed{
   r_*=\max_{S\in U}|S|.
   }
   \]
   No smaller-arity marginal can reveal a missing `S` of size `r_*`, while adding the missing maximal supports themselves attains the bound.

9. **Proper marginals can never recover the full ambient law.** If every retained and added marginal is a proper subset of `[d]`, then `[d]\notin\Delta`. The parity pair
   \[
   P_{[d],1}^{\pm}(\{x\})
   =2^{-d}(1\pm\chi_{[d]}(x))
   \]
   remains indistinguishable. Hence
   \[
   \boxed{
   \text{ambient full-law fidelity requires retaining the full joint face }[d].
   }
   \]
   This does not prevent a target-specific discriminator from being recoverable from much smaller faces.

10. **Restricted source classes remain a separate gate.** For an admissible family `\mathcal S\subseteq M(\Omega_d)`, exact source fidelity is
    \[
    \boxed{
    (\mathcal S-\mathcal S)
    \cap
    \operatorname{span}\{\eta_S:S\notin\Delta\}
    =\{0\}.
    }
    \]
    Product families, graphical models, deterministic constraints, or another structured source class may therefore be identifiable from a sparse marginal scenario only because that class excludes the ambient missing-interaction directions.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{a coordinate-marginal compression is completely specified by the interactions it closes downward over,}
}
\]

and its composition, loss, target fidelity, and minimal marginal lift can all be computed on that simplicial information state.

## Why the downward closure is canonical

Fix `A\subseteq[d]`. Fourier inversion on the marginal `\mu_A=(\pi_A)_*\mu` gives

\[
\mu_A(\{y\})
=
2^{-|A|}
\sum_{S\subseteq A}m_S(\mu)\chi_S(y).
\]

Thus the complete marginal on `A` is equivalent to the collection of moments indexed by all subsets of `A`. Taking all `A\in\mathcal H` retains exactly

\[
\bigcup_{A\in\mathcal H}2^A
=\Delta(\mathcal H).
\]

This proves both the downward-closure reduction and the arbitrary-scenario Walsh theorem. Since the `\eta_S` form the basis dual to the Walsh moment coordinates, the kernel statement follows immediately.

The facet reduction is also exact. If `A` is not maximal in `\Delta`, choose a facet `F\supsetneq A`; then

\[
(\pi_A)_*\mu
=
(\pi_{F\to A})_*\bigl((\pi_F)_*\mu\bigr).
\]

So retaining both `F` and `A` does not create a stronger information state.

## Factorization lattice and composition law

If `\Delta_1\subseteq\Delta_2`, every marginal indexed by `\Delta_1` is already one of the marginals retained by `\Delta_2` (or a submarginal of one of its facets), so there is an explicit deterministic marginalization/projection map

\[
\mathsf M_{\Delta_2}
\longrightarrow
\mathsf M_{\Delta_1}.
\]

Conversely suppose `S\in\Delta_1\setminus\Delta_2`. The positive collision pair `P_{S,\theta}^{\pm}` has the same `\Delta_2` data but different `S`-marginals, hence different `\Delta_1` data. No deterministic map from the `\Delta_2` destination can therefore reproduce `\mathsf M_{\Delta_1}`.

This proves the exact equivalence

\[
\mathsf M_{\Delta_1}\preceq\mathsf M_{\Delta_2}
\iff
\Delta_1\subseteq\Delta_2.
\]

Because unions and intersections of downward-closed families are again downward closed, these information states form a distributive lattice. More importantly for sequential compression, the basis decomposition makes the loss between comparable states literal:

\[
\ker\mathsf M_{\Delta_1}
=
\operatorname{span}\{\eta_S:S\notin\Delta_1\},
\]

so modding out the smaller kernel `\ker\mathsf M_{\Delta_2}` leaves exactly the coordinates in `\Delta_2\setminus\Delta_1`.

This is an exact finite model of the line's composition question: once a face has disappeared at an intermediate marginalization step, no later deterministic processing can manufacture its coefficient from the retained destination.

## Target support and minimal lifts

For

\[
g=\sum_S\widehat g(S)\chi_S,
\]

we have

\[
D_g(\mu)
=
\sum_S\widehat g(S)m_S(\mu).
\]

If the Walsh support lies in `\Delta`, the retained marginals determine every term. If instead `S\notin\Delta` with `\widehat g(S)\ne0`, perturbing the uniform law by `\pm\theta\eta_S` leaves every retained marginal fixed while changing `D_g` by

\[
2\theta\widehat g(S).
\]

Hence support containment is both sufficient and necessary even on genuine probability laws.

Adding one marginal on `A` enlarges the information state by the whole simplex `2^A`. Therefore it repairs precisely the missing target interactions `S` satisfying `S\subseteq A`. Once an admissible channel family and cost have been declared, the minimal-lift problem has no hidden analytic content: it is exactly the stated covering problem.

This also prevents a common false notion of minimality. Without a declared admissible channel class or resource measure, one can always retain the full joint law and recover everything. A nontrivial minimal lift exists only relative to a constrained family of allowed retained structures, as already required abstractly by AF-001.

## Relation to AF-030, AF-031, and AF-032

AF-030 says that any linear-test compression is classified by the closed linear span of the tests actually retained. In the present finite setting, the span is explicit:

\[
V_{\Delta}
=
\operatorname{span}\{\chi_S:S\in\Delta\}.
\]

The annihilator theorem of AF-030 therefore becomes the missing-face kernel above.

AF-031 isolates the difference between complete separate marginal laws and the joint feature law. The present result generalizes that one-step distinction to an arbitrary marginal scenario: the entire hierarchy of which joint relations are retained is encoded by a downward-closed family.

AF-032 treats the symmetric special case

\[
\Delta_k=\{S\subseteq[d]:|S|\le k\}.
\]

Its degree filtration is exactly the chain

\[
\Delta_0\subset\Delta_1\subset\cdots\subset\Delta_d
\]

inside the larger simplicial lattice. AF-033 shows that interaction order is only one possible compression hierarchy; sparse or anisotropic systems retain arbitrary downward-closed patterns of relations, and the same exact kernel/composition calculus still applies.

## Prior art and novelty assessment

The mathematical ingredients and the simplicial organization of marginal information are classical.

- František Matúš, **“Discrete marginal problem for complex measures,”** *Kybernetika* 24(1), 36–46 (1988), MR 936552. Role: direct classical prior art for finite/discrete marginal operators, their linear structure, and inversion questions. This prevents treating arbitrary marginal scenarios as a new object.
- John N. Darroch, Steffen L. Lauritzen, and Terence P. Speed, **“Markov Fields and Log-Linear Interaction Models for Contingency Tables,”** *The Annals of Statistics* 8(3), 522–539 (1980), DOI `10.1214/aos/1176345006`. Role: foundational hierarchical log-linear/graphical-model prior art in which interaction families are organized hierarchically; it is a classical statistical home for downward-closed interaction structure.
- Jane Ivy Coons, Joseph Cummings, Benjamin Hollering, and Aida Maraj, **“Generalized Cut Polytopes for Binary Hierarchical Models,”** *Algebraic Statistics* 14(1), 17–36 (2023), DOI `10.2140/astat.2023.14.17`. Role: explicit modern evidence that binary marginal polytopes for hierarchical models are naturally indexed by arbitrary simplicial complexes. No novelty can be claimed for using a simplicial complex as the combinatorial carrier of a binary marginal scenario.
- Ryan O'Donnell, ***Analysis of Boolean Functions***, Cambridge University Press (2014), corrected electronic version arXiv:`2105.10386`. Role: standard Walsh-Fourier basis, inversion, degree, and interaction language on the Boolean cube, already used in AF-032.

No novelty is claimed for discrete marginal problems, hierarchical log-linear models, simplicial-complex indexing, Walsh analysis, or weighted set cover. The factorization criterion and kernel formulas are elementary consequences of those classical structures.

The Arithmetic Fidelity contribution is the **compression calculus** obtained by putting them in one exact information-state statement: coordinate-marginal destinations are classified up to deterministic equivalence by their downward-closed interaction sets; deterministic factorization is simplicial inclusion; nested loss is the explicit missing-face quotient; and target-relative minimal lifts are obtained by covering only the missing interaction support. This is a reusable audit package rather than a claim to a new marginal theory.

## Boundaries and failure modes

- The exact Walsh basis uses the Boolean product structure. Finite nonbinary product spaces admit analogous tensor/contrast decompositions, but the corresponding theorem must be written in the correct basis rather than assumed from this binary case.
- The result characterizes **fibers of a marginal map given a global source measure**. It does not solve the distinct marginal compatibility problem of deciding whether an arbitrary collection of local marginals admits a global extension.
- Interaction support is representation-dependent. A nonlinear change of coordinates can move information between faces. An application must justify that its coordinates/subsystems and allowed marginal channels are intrinsic before the simplicial audit has structural meaning.
- Ambient non-fidelity does not imply non-fidelity on a structured source class. The restricted-class intersection criterion is mandatory before applying a no-go theorem to product laws, graphical models, arithmetic measures, or another constrained family.
- The theorem is exact, not quantitative. Approximate/noisy marginal recovery needs stability estimates and may behave very differently near restricted models.
- Full-law recovery on unrestricted probabilities requires the top face `[d]`, but target-specific recovery can require far less. Do not replace the support test by the stronger full-law criterion.
- The set-cover minimality statement is relative to a declared admissible family and cost. If arbitrary side information is allowed, the lift problem trivializes, exactly as AF-001 warns.
- No arithmetic-specific conclusion follows merely because a proposed prime representation has many channels. One must first prove an intrinsic channel decomposition and locate the rational-prime discriminator in the corresponding interaction basis.

## Consequences for the research line

AF-032 supplied an exact warning that bounded interaction order can erase a global bit. AF-033 turns that warning into a compositional audit for arbitrary subsystem patterns:

\[
\boxed{
\text{identify the intrinsic marginal scenario }\Delta,
\quad
\text{locate the target interaction support},
\quad
\text{and compute the missing faces before any downstream operation.}
}
\]

If the target support lies outside `\Delta`, every deterministic analytic, spectral, positive, scalar, or asymptotic operation applied only after that marginal compression still factors through the same lost-information fiber. A viable lift must retain a marginal containing each missing target interaction, or a separately proved source constraint must force those interactions from the retained ones.

For eventual rational-prime use, this gives a precise form to the hypothesis that prime-specific provenance could live in relations among many individually well-preserved channels. It does not establish that the primes possess such an intrinsic Walsh/simplicial decomposition. The next arithmetic application must first identify the relevant coordinates and prove that the rational-prime discriminator has a component in a genuinely missing relational sector rather than importing the finite model by analogy.