---
id: WP-301
title: Frustration-free non-scalar holonomy selectors reduce to common-kernel tests, and their harmonic projection cannot see archimedean positive spectrum
branch: weil_positivity
status: supported
kind: frustration-free-holonomy-kernel-classification-and-archimedean-no-go
claim_strength: exact kernel theorem for arbitrary noncommuting positive plaquette defects, classification of the resulting prime-power harmonic selector by two-prime fixed spaces, generalized-prime control, and an exact obstruction to extracting nonconstant archimedean spectral data through the same zero-mode projection
created: 2026-09-14
related: [WP-005, WP-019, WP-029, WP-030, WP-300]
prior_art:
  - D. Aharonov, I. Arad, Z. Landau, U. Vazirani, The Detectability Lemma and Quantum Gap Amplification, STOC 2009, DOI 10.1145/1536414.1536472
  - D. Aharonov, I. Arad, Z. Landau, U. Vazirani, Quantum Hamiltonian complexity and the detectability lemma, arXiv:1011.3445
  - A. Anshu, I. Arad, T. Vidick, Simple proof of the detectability lemma and spectral gap amplification, Phys. Rev. B 93 (2016) 205142, DOI 10.1103/PhysRevB.93.205142
---

# WP-301 — Frustration-free non-scalar holonomy selectors reduce to common-kernel tests, and their harmonic projection cannot see archimedean positive spectrum

## Claim

`WP-300` classifies the fully prime-relabeling-invariant **scalar** projective commutator law: its only nonflat branch is the universal fermionic sign, whose positive plaquette defect gives the prime-power support selector already implicit in Prime Lattice's Boolean geometry. The immediate escape is to replace scalar holonomy by genuinely operator-valued/non-scalar holonomy and hope that the richer internal geometry carries new arithmetic information.

For the most direct positive realization of that escape — a frustration-free sum of plaquette/boundary squares followed by the zero-energy projection — the additional matrix structure does **not** enrich the selector. If

\[
H_S=\sum_{j\in J(S)} c_j B_j^*B_j,
\qquad c_j>0,
\tag{1}
\]

then, with no commutativity assumption,

\[
\boxed{\ker H_S=\bigcap_{j\in J(S)}\ker B_j.}
\tag{2}
\]

For unitary plaquette holonomies `K_{pq}` and `B_{pq}=I-K_{pq}`, this becomes

\[
\boxed{\ker H_S=\bigcap_{\{p,q\}\subset S}\operatorname{Fix}(K_{pq}).}
\tag{3}
\]

Consequently an exact prime-power harmonic selector is already determined on every **two-prime** restriction:

\[
\boxed{
P_S:=\mathbf 1_{\{0\}}(H_S)
\text{ vanishes for every }|S|\ge2
\iff
\operatorname{Fix}(K_{pq})=\{0\}
\text{ for every distinct }p,q.
}
\tag{4}
\]

Once (4) holds, no higher non-scalar coherence is visible to the support selector. Every positive reweighting of the same defects has exactly the same kernel. Thus replacing the fermionic scalar sign by richer matrices creates a large family of positive realizations of the **same Boolean statement** `omega(n)<=1`; it does not by itself create rational-prime specificity.

There is a second exact obstruction. If an archimedean positive operator is included as another summand of the same frustration-free Hamiltonian, the harmonic projection sees only its kernel. If `Q_infty>=0` is a summand and `P_S=1_{0}(H_S)`, then

\[
P_S Q_\infty P_S=0,
\qquad
P_S f(Q_\infty)P_S=f(0)P_S
\tag{5}
\]

for every bounded Borel `f`. Hence all nonzero archimedean spectral data are invisible to the zero-mode readout. Positive scalar reweighting of `Q_infty` cannot change this. A fixed-kernel frustration-free harmonic selector therefore cannot simultaneously explain the exact Mangoldt support and obtain the nonconstant Gamma/polar contribution from the positive spectrum of the same archimedean sector.

This does **not** exclude operator-valued source geometry in general. It closes a specific but natural continuation of `WP-300`: enriching the holonomy while retaining a sum-of-squares sign theorem and reading arithmetic through its harmonic nullspace. A surviving route must make the kernel itself move canonically, retain nonzero spectral information through a different boundary/cohomological readout, or form a genuinely non-frustration-free global coupling before the final positivity theorem.

**Classification:** `EXACT-DERIVED + NONCOMMUTATIVE-DEFECT-KERNEL-THEOREM + TWO-PRIME-SELECTOR-CLASSIFICATION + POSITIVE-REWEIGHTING-RIGIDITY + GENERALIZED-PRIME-CONTROL + ARCHIMEDEAN-HARMONIC-SPECTRUM-BLINDNESS + FRUSTRATION-FREE-PRIOR-ART-CLASSICALIZATION + DIRECT-NONSCALAR-HOLONOMY-ESCAPE-NARROWED + NOT-WEIL-POSITIVITY`.

## 1. The kernel theorem does not require commuting defects

Let `H` be a Hilbert space and let `B_1,...,B_m` be bounded operators. For strictly positive real weights `c_j`, put

\[
H=\sum_{j=1}^m c_j B_j^*B_j\succeq0.
\tag{6}
\]

For every vector `v`,

\[
\langle v,Hv\rangle
=\sum_{j=1}^m c_j\|B_jv\|^2.
\tag{7}
\]

Every summand on the right is nonnegative. Therefore the sum is zero exactly when every summand is zero, which proves

\[
\boxed{
\ker H=\bigcap_{j=1}^m\ker B_j.
}
\tag{8}
\]

No pair of `B_j` needs to commute, and no simultaneous diagonalization is used. This is precisely the elementary structural fact behind frustration-free Hamiltonians: a zero-energy state satisfies every positive local constraint individually.

The consequence important here is **weight rigidity**. If `c_j(t)>0` varies with a scale, Mellin parameter, prime length, or other external variable while the operators `B_j` remain fixed, then

\[
\boxed{
\ker\sum_j c_j(t)B_j^*B_j
=\bigcap_j\ker B_j
}
\tag{9}
\]

throughout the region where all weights stay positive. The nonzero spectrum can move dramatically while the harmonic subspace does not move at all.

## 2. Arbitrary non-scalar plaquette holonomy collapses to fixed spaces

Let

\[
S(n)=\{p:p\mid n\}
\tag{10}
\]

be the occupied-prime support. Allow each distinct pair `p,q` to carry an arbitrary unitary holonomy `K_{pq}` on the relevant internal fiber; it may be matrix-valued and the different holonomies need not commute. Define the normalized positive defect

\[
Q_{pq}
:=\frac14(I-K_{pq})^*(I-K_{pq})\succeq0
\tag{11}
\]

and, with arbitrary strictly positive weights `c_{pq}`,

\[
H_S:=\sum_{\{p,q\}\subset S}c_{pq}Q_{pq}.
\tag{12}
\]

Because

\[
\ker Q_{pq}
=\ker(I-K_{pq})
=\operatorname{Fix}(K_{pq}),
\tag{13}
\]

equation (8) gives the exact identity

\[
\boxed{
\ker H_S
=\bigcap_{\{p,q\}\subset S}\operatorname{Fix}(K_{pq}).
}
\tag{14}
\]

The scalar fermionic case of `WP-300` is just `K_{pq}=-I`, for which every fixed space is zero and each normalized defect equals `I`. Equation (14) shows that the Boolean support mechanism is much less special than that realization suggests: any fixed-point-free two-prime holonomy gives the same zero-mode selector.

## 3. Exact prime-power support is equivalent to a two-prime fixed-point test

For `|S|=0` or `1`, equation (12) is an empty sum, so `H_S=0`. In particular every prime power has nonzero harmonic space automatically.

Now require exact mixed-prime rejection:

\[
\mathbf 1_{\{0\}}(H_S)=0
\qquad\text{for every }|S|\ge2.
\tag{15}
\]

Apply this first to a two-element support `S={p,q}`. Equation (14) reduces to

\[
\ker H_{\{p,q\}}
=\operatorname{Fix}(K_{pq}).
\tag{16}
\]

Thus (15) forces

\[
\operatorname{Fix}(K_{pq})=\{0\}
\qquad(p\ne q).
\tag{17}
\]

Conversely, if (17) holds for every pair, then any support with at least two primes contains one pair whose fixed space is already zero, so the full intersection (14) is zero. Therefore

\[
\boxed{
\text{exact prime-power harmonic support}
\iff
\text{every two-prime holonomy has no fixed vector}.
}
\tag{18}
\]

This is the main collapse. Higher braid/Yang--Baxter/coherence data, matrix size, noncommutativity between different pair defects, and the detailed nonzero spectra of the `K_{pq}` may matter to the excited states, but **none of them is visible to the support predicate once the readout is the zero-energy projection**.

With the intrinsic Prime-Lattice radius

\[
A(n)=\left(\sum_{p\mid n}(\log p)^2\right)^{1/2},
\tag{19}
\]

any normalized state `omega_n` on the harmonic fiber gives

\[
m(n)
:=A(n)\,\omega_n(P_n),
\qquad P_n=\mathbf1_{\{0\}}(H_{S(n)}).
\tag{20}
\]

Under (17), `omega_n(P_n)=1` on a one-prime support and `0` on mixed support, hence

\[
\boxed{m(n)=\Lambda(n).}
\tag{21}
\]

This reproduces the same finite coefficient extraction as `WP-030` and `WP-300`, but now for an arbitrary non-scalar frustration-free holonomy family satisfying only (17).

## 4. The generalized-prime control becomes stronger, not weaker

Replace rational primes by generators `q_j` of an arbitrary free commutative monoid. Transport the same internal fibers and pair holonomies to the new labels, and assign arbitrary positive generator lengths `a_j`. Equations (12)--(18) are unchanged. With

\[
A_Q(S)=\left(\sum_{j\in S}a_j^2\right)^{1/2},
\tag{22}
\]

the same harmonic readout is nonzero exactly on one-generator powers and returns `a_j` there.

Thus the non-scalar upgrade does not defeat the matched control. If the holonomy kernels are specified only by a relabeling-covariant incidence rule, the positive selector is a universal statement about **support cardinality and common fixed spaces**. Rational-prime arithmetic enters only if the source geometry itself forces pair kernels that cannot be transported to the generalized-prime control.

This is stronger than saying that the fermionic sign is generic. The entire frustration-free zero-mode mechanism is generic. A complicated matrix holonomy can contain rich internal information, but that information is discarded by the exact Mangoldt support readout unless it changes whether eigenvalue `1` is present on a two-prime restriction.

## 5. A positive archimedean summand contributes only its kernel

Now add a fixed archimedean positive term to the same global sign mechanism. Write, schematically,

\[
H_S^{\rm tot}
=Q_\infty
+\sum_{p\in S}Q_{p\infty}
+\sum_{\{p,q\}\subset S}Q_{pq},
\qquad
Q_*\succeq0.
\tag{23}
\]

Each positive term may itself be written as `B_*^*B_*` after taking a square root. Therefore

\[
\boxed{
\ker H_S^{\rm tot}
=\ker Q_\infty
\cap\bigcap_{p\in S}\ker Q_{p\infty}
\cap\bigcap_{\{p,q\}\subset S}\ker Q_{pq}.
}
\tag{24}
\]

Let

\[
P_S^{\rm tot}=\mathbf1_{\{0\}}(H_S^{\rm tot}).
\tag{25}
\]

Its range lies inside `ker Q_infty`. Hence for every `v` in that range,

\[
Q_\infty v=0.
\]

It follows immediately that

\[
P_S^{\rm tot}Q_\infty P_S^{\rm tot}=0.
\tag{26}
\]

More generally, by the spectral calculus, for every bounded Borel function `f`,

\[
\boxed{
P_S^{\rm tot}f(Q_\infty)P_S^{\rm tot}
=f(0)P_S^{\rm tot}.
}
\tag{27}
\]

Therefore the harmonic projection does not see the location, multiplicity, or density of any positive archimedean eigenvalue. It sees only the zero eigenspace.

This is fatal to the most direct attempt to let the same fixed positive archimedean Hamiltonian both participate in the frustration-free sign theorem and contribute the nonconstant Gamma spectral term. If the Gamma information is stored in the positive spectrum of `Q_infty`, equation (27) erases it. If `ker Q_infty={0}`, the harmonic selector is erased instead. If the kernel is nonzero, the selector can survive, but the compressed archimedean spectral function is just the scalar `f(0)`.

## 6. Positive reweighting cannot turn that kernel into the Gamma factor

One might try to retain a fixed archimedean operator but vary its coefficient with a Mellin/spectral parameter:

\[
H_S(t)
=c_\infty(t)Q_\infty
+\sum_j c_j(t)Q_j,
\qquad c_\infty(t),c_j(t)>0.
\tag{28}
\]

Equation (9) gives

\[
\ker H_S(t)
=\ker Q_\infty\cap\bigcap_j\ker Q_j,
\tag{29}
\]

independently of `t`. The harmonic projector is therefore constant throughout every region in which the coefficients remain strictly positive. The nonconstant digamma/Gamma contribution of the completed zeta explicit formula cannot emerge from the changing **positive weights** of a fixed frustration-free family while the readout remains `1_{0}(H_S(t))`.

Allowing a coefficient to vanish can make the kernel jump, but this merely removes a constraint at selected parameter values; it does not produce the smooth/nonlocal archimedean distribution without an additional source theorem. Allowing the operators' kernels themselves to move with the global parameter is a genuinely different mechanism and remains open.

This obstruction is distinct from `WP-019`. There the nonzero archimedean spectrum cancels under a supersymmetric **supertrace** and only an index remains. Here there is no grading and no cancellation: the information is discarded because a frustration-free **zero-mode projection** restricts every positive summand to its kernel.

## 7. Why this still does not give the global Weil sign

Even when (18) and (21) hold, the output is only the positive Mangoldt coefficient selector. Critical attenuation recovers `Lambda(n)/sqrt(n)`, but `WP-005` shows that the required Weil autocorrelation lift converts those coefficients into off-diagonal translations and is indefinite on the compactly supported test space.

Thus richer matrix holonomy does not alter the already-established distinction

\[
\boxed{
\text{positive coefficient/support extraction}
\ne
\text{positive Weil quadratic form}.
}
\tag{30}
\]

The frustration-free theorem strengthens that boundary: if the proposed global sign is obtained merely by summing positive local defects and then keeping their common zero space, all nonzero curvature and archimedean spectral information is absent from the final selector.

## 8. Prior-art and novelty audit

The algebraic lemma (8) is classical and no novelty is claimed for it. It is the defining ground-space property of frustration-free Hamiltonians and local quantum constraint systems. Aharonov--Arad--Landau--Vazirani's detectability-lemma program and the later Anshu--Arad--Vidick treatment are representative sources in which the common local ground space of positive constraints is the basic object. The present argument does not require their deeper gap or projector-product estimates.

A targeted literature search for combinations of frustration-free Hamiltonians with the Weil criterion, zeta explicit-formula positivity, and prime-power support did not identify a credible established construction that changes this boundary. That negative search is not itself a novelty theorem. The claim here is deliberately Mathia-specific: once `WP-300` motivates non-scalar source holonomy as the next escape, equations (14), (18), and (27) show exactly what the most natural sum-of-squares/harmonic realization can and cannot retain.

The result also does not compete with classical Weil positivity, Hodge-index/cohomological approaches, Hilbert--Polya, Connes trace formulas, or scattering constructions. It is a **route exclusion**: any successful use of those richer structures must do more than implement the arithmetic selector as the ground space of fixed positive local constraints.

## 9. Adversarial falsification gates

This finding must be narrowed or withdrawn if any of the following fails:

1. for strictly positive scalar weights, `ker(sum_j c_j B_j^*B_j)=intersection_j ker B_j` without a commutativity assumption;
2. for unitary `K`, `ker((I-K)^*(I-K))=Fix(K)`;
3. exact rejection of every two-prime support is equivalent to `Fix(K_pq)={0}` for each pair;
4. pairwise fixed-point-freeness is sufficient to reject every support with at least two distinct primes;
5. strictly positive reweighting leaves the harmonic subspace unchanged;
6. the same construction transports unchanged to a free generalized-prime monoid when its holonomy data are only incidence/relabeling-covariant;
7. if `Q_infty` is a positive summand of `H_tot`, then `Ran 1_{0}(H_tot) subset ker Q_infty`;
8. consequently `P f(Q_infty) P=f(0)P` for bounded Borel `f`;
9. a fixed-kernel positive reweighting cannot make the harmonic projector carry a nonconstant archimedean spectral function;
10. after scalar Mangoldt extraction, the independent `WP-005` autocorrelation obstruction remains applicable.

Items 1--5 and 7--9 are elementary operator identities. Item 6 is an explicit matched-control statement, not a claim that every conceivable prime-dependent holonomy is transportable. Item 10 is an internal dependency. No zero data, RH assumption, arbitrary regularization, or hand-picked Weil kernel enters the derivation.

## 10. Consequence for the research frontier

`WP-300` left genuinely richer non-scalar/projective/cohomological source geometry as an open escape from the scalar-holonomy classification. The present result splits that escape.

Merely replacing scalar plaquette phases by matrices while keeping the sign theorem **frustration free** and the arithmetic readout **harmonic** does not create a new global mechanism. Exact prime-power support reduces to the two-prime statement that every pair holonomy lacks eigenvalue `1`; after that, the internal nonzero spectra and higher coherence are invisible to the selector. Adding a fixed positive archimedean sector to the same sum-of-squares architecture makes its nonzero spectrum invisible for the same reason.

The surviving non-scalar route must therefore violate at least one of those simplifications in a source-forced way. Plausible remaining categories are:

- a canonically **moving nullspace** whose dependence on the global/Mellin variable itself carries arithmetic and archimedean data;
- a boundary/cohomological observable that reads nonzero spectrum while its sign follows from an independent theorem rather than from zero-energy projection;
- a genuinely **frustrated or indefinite intermediate coupling** in which finite and archimedean information interact before a later global positivity theorem;
- prime-dependent operator kernels forced intrinsically by Mathia rather than chosen after inspecting the desired coefficients;
- a higher categorical/global construction whose relevant invariant is not reducible to the common kernel of local positive defects.

Those mechanisms remain open. The fixed-defect frustration-free harmonic continuation of the non-scalar holonomy escape is closed.

## Internal dependencies

- `research/weil_positivity/findings/WP-005-prime-lattice-axis-positivity-does-not-survive-weil-autocorrelation-lift.md`
- `research/weil_positivity/findings/WP-019-decoupled-supersymmetric-archimedean-completion-collapses-to-an-index.md`
- `research/weil_positivity/findings/WP-029-even-commutator-energies-radialize-but-positive-one-sided-parts-retain-orientation.md`
- `research/weil_positivity/findings/WP-030-incidence-gram-volume-recovers-von-mangoldt-positively-but-is-a-rank-test.md`
- `research/weil_positivity/findings/WP-300-prime-symmetric-projective-source-curvature-is-fermionic-and-boolean.md`
