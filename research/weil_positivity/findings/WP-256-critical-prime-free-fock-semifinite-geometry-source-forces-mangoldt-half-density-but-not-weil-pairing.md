# WP-256 — Critical prime free-Fock semifinite geometry source-forces the Mangoldt half-density as a positive simple-spectrum operator, but not the Weil pairing

**Status:** `EXACT-DERIVED + FREE-PRIME-FOCK + SEMIFINITE-KMS-WEIGHT + SIMPLE-SPECTRAL-MULTIPLICITY + PRIME-POWER-SELECTOR + SOURCE-WORD-LENGTH + EXACT-MANGOLDT-HALF-DENSITY + POSITIVE-COMPACT-OPERATOR + SHARP-SCHATTEN-2-BOUNDARY + WP255-SEMIFINITE-ESCAPE + DIAGONAL-CARRIER-ONLY + PASSIVE-TRANSPORT-REDIRECT + ARCHIMEDEAN-MISSING + PRIOR-ART-AUDITED + SUBSTANTIVE-INTERMEDIATE + NOT-A-WEIL-BRIDGE`.

`WP-255` proves that independent orthogonal prime isometries with arithmetic energies `log p` cannot support a **normalized** critical `KMS_1` state: KMS forces range masses `1/p`, and mutually orthogonal positive ranges cannot pack their divergent total mass into a state of mass one. That finding deliberately leaves a genuinely semifinite category open.

The canonical free-Fock realization of those same prime channels shows that this boundary is real rather than formal. On the full free Fock space over the prime alphabet, the critical Gibbs functional is a faithful normal semifinite KMS weight even though its value on the identity is infinite. More surprisingly, the same free-word geometry contains an intrinsic spectral-multiplicity selector that distinguishes prime powers without inserting `Lambda` as a scalar function of the Hamiltonian.

Let `H` be the arithmetic word Hamiltonian and `N` the word-length operator. The eigenspace of `H` at energy `log n` has dimension equal to the number of distinct orderings of the prime multiset of `n`,

\[
M(n)=\frac{\Omega(n)!}{\prod_p v_p(n)!}.
\]

For `n>1`, this multiplicity is one **if and only if `n` is a prime power**. Let `P_{\rm simp}` be the projection onto the non-vacuum simple eigenspaces of `H`, defined intrinsically by spectral multiplicity. Then, with `N^{-1}` set to zero on the vacuum,

\[
\boxed{
T
:=P_{\rm simp}\,H N^{-1}e^{-H/2}
\succeq0
}
\]

is a bounded compact positive operator and for every Fock word `w`, with commutative product `n(w)`, satisfies the exact identity

\[
\boxed{
T e_w
=\frac{\Lambda(n(w))}{\sqrt{n(w)}}e_w.
}
\]

Thus the live semifinite escape after `WP-255` can source-force the **entire finite-place Mangoldt half-density as a positive operator** from three structural ingredients: free-word spectral multiplicity, the canonical gauge length, and the square root of the critical Gibbs density. No zeta zeros, prime-power Borel set, or target-prescribed values are inserted into `T`.

This is nevertheless not a Weil-positivity mechanism. `T` is diagonal positivity on the free-word label space. The finite Weil term is an oriented translation/autocorrelation form on the Weil test space, with the same coefficients multiplying off-diagonal correlations with the opposite sign. Passing from the diagonal carrier to passive translation energy returns exactly the divergent positive self-energy obstruction of `WP-009`; passing through the Bost--Connes critical Gram returns the indefinite defect of `WP-216`. The free-Fock construction supplies no Gamma or polar sector and no source-derived map that turns its diagonal positivity into the completed Weil sign.

The result therefore changes the boundary in a precise way: **semifiniteness is sufficient to evade the `WP-255` normalization obstruction and to recover the exact finite coefficients canonically, but it does not solve the orientation problem.** The missing object is no longer a finite-prime coefficient carrier. It is a source-forced global pairing or coupling that transports those coefficients into the Weil test geometry while preserving an independent positivity theorem and simultaneously producing the archimedean and polar completion.

## 1. The free prime Fock system and its critical semifinite weight

Let

\[
\mathcal K=\ell^2(\mathbb P)
\]

with basis vectors `e_p`, and let

\[
\mathcal F
=\mathbb C\Omega
\oplus
\bigoplus_{m\ge1}\mathcal K^{\otimes m}
\]

be the full Fock space. Its canonical orthonormal basis is indexed by finite prime words

\[
w=(p_1,\ldots,p_m).
\]

Write

\[
|w|=m,
\qquad
n(w)=\prod_{j=1}^m p_j.
\tag{1}
\]

For every prime `p`, let `L_p` be the left creation isometry. The ranges of distinct `L_p` are orthogonal, exactly the independent one-sided category tested in `WP-255`:

\[
L_p^*L_q=\delta_{p,q}I.
\tag{2}
\]

Define the commuting diagonal operators

\[
H e_w=(\log n(w))e_w,
\qquad
N e_w=|w|e_w,
\qquad
H\Omega=N\Omega=0.
\tag{3}
\]

Then

\[
e^{itH}L_pe^{-itH}=p^{it}L_p,
\tag{4}
\]

so `H` implements the same arithmetic energy law as `WP-255`. The operator `N` is the generator of the canonical Fock gauge action `L_p\mapsto zL_p`.

For `beta>0`, the standard Gibbs expression

\[
\Psi_\beta(X)
:=\operatorname{Tr}\!\left(e^{-\beta H/2}Xe^{-\beta H/2}\right),
\qquad X\ge0,
\tag{5}
\]

defines a faithful normal semifinite weight on `B(F)`, with

\[
\Psi_\beta(|e_w\rangle\langle e_w|)
=n(w)^{-\beta}.
\tag{6}
\]

It is the standard semifinite Gibbs/KMS weight for the dynamics (4). It need not be finite on the identity. Indeed formally

\[
\Psi_\beta(I)
=
\sum_{m\ge0}
\left(\sum_p p^{-\beta}\right)^m
\tag{7}
\]

whenever the right side is interpreted as the word partition sum. At `beta=1` the one-letter contribution already diverges:

\[
\sum_p\frac1p=+\infty,
\tag{8}
\]

so

\[
\boxed{\Psi_1(I)=+\infty.}
\tag{9}
\]

There is therefore no normalized Gibbs state of this form at the critical point, in agreement with `WP-255`. But (5) remains a perfectly valid semifinite weight because every finite-rank word projection has finite weight.

This is the exact category change left open in `WP-255`: the critical masses do not have to pack into total mass one. The price is that positivity now lives in a semifinite von Neumann setting rather than in a normalized equilibrium state.

## 2. Spectral multiplicity intrinsically selects prime powers

Fix `n>=2` and write

\[
n=\prod_{j=1}^r p_j^{a_j},
\qquad
a_j\ge1,
\qquad
m:=\Omega(n)=\sum_{j=1}^r a_j.
\tag{10}
\]

A word has arithmetic energy `log n` exactly when its letters are an ordering of this prime multiset. Hence

\[
\boxed{
\dim\ker(H-\log n)
=M(n)
:=\frac{m!}{a_1!\cdots a_r!}.
}
\tag{11}
\]

This is the classical number of distinct permutations of a multiset. Equation (11) immediately gives

\[
\boxed{
M(n)=1
\quad\Longleftrightarrow\quad
n=p^k
\text{ for some prime }p\text{ and }k\ge1.
}
\tag{12}
\]

If only one prime occurs, every word is `p^k` and there is one ordering. If two distinct primes occur, swapping one occurrence of the two primes already gives two distinct words, so the multiplicity is at least two.

Define `P_simp` without naming prime powers:

\[
P_{\rm simp}
:=
\sum_{\substack{\lambda>0\\
\operatorname{rank}1_{\{\lambda\}}(H)=1}}
1_{\{\lambda\}}(H),
\tag{13}
\]

where the sum is the orthogonal strong sum of the non-vacuum rank-one spectral projections. This definition uses only the spectral multiplicity of the source Hamiltonian. By (12), its range is exactly

\[
\overline{\operatorname{span}}
\{e_{p^k}:p\text{ prime},\ k\ge1\}.
\tag{14}
\]

This is materially different from the target-coded scalar interpolation rejected by `WP-215`. There an arbitrary Borel/smooth function is prescribed from desired arithmetic values. Here the support is selected by a representation invariant — simplicity of the energy eigenspace — before any Weil coefficient is assigned.

The selector is not mysterious prior art. Equation (11) is simply unique factorization plus the multinomial count of ordered prime factorizations. The point is its operator-theoretic consequence in the precise semifinite escape opened by `WP-255`.

## 3. Word length extracts the primitive logarithmic scale

On a non-vacuum word, `HN^{-1}` is the mean one-letter energy:

\[
HN^{-1}e_w
=
\frac{\log n(w)}{|w|}e_w.
\tag{15}
\]

It is the permutation-invariant average of the one-particle prime energies over the tensor word. On a simple energy sector `n=p^k`, every letter is `p`, so

\[
\boxed{
HN^{-1}e_{p^k}
=\log p\,e_{p^k}.
}
\tag{16}
\]

Thus the repetition-independent Mangoldt scale does not need to be interpolated as an arbitrary function of `H`. It is recovered from the two canonical commuting source gradings: total arithmetic energy and Fock length.

This step has a clear boundary. The free-Fock category itself supplies many other diagonal functions of `(H,N)`, so (16) is not a uniqueness theorem saying that no other scalar readout is possible. Its canonicity is narrower: `H/N` is the ordinary intensive/mean energy associated with the additive word Hamiltonian and the standard length gauge, and on a one-generator repeated word it returns that generator's source energy exactly. The research claim below uses only this explicit source-derived choice, not an assertion that all alternatives are forbidden.

## 4. The critical Gibbs square root gives exactly the Mangoldt half-density

At the source-selected critical value `beta=1`, the square root of the Gibbs density is

\[
e^{-H/2}e_w=n(w)^{-1/2}e_w.
\tag{17}
\]

The three diagonal operators in (13), (15), and (17) strongly commute. Put

\[
\boxed{
T
:=P_{\rm simp}HN^{-1}e^{-H/2},
}
\tag{18}
\]

with `N^{-1}\Omega=0`. Then `T` is positive. If `n(w)=p^k`, equations (16)--(17) give

\[
Te_w
=(\log p)p^{-k/2}e_w.
\tag{19}
\]

If `n(w)` has at least two distinct prime factors, `P_simp e_w=0`, while `Lambda(n(w))=0`. The vacuum is also killed. Therefore for **every** Fock basis word,

\[
\boxed{
Te_w
=\frac{\Lambda(n(w))}{\sqrt{n(w)}}e_w.
}
\tag{20}
\]

Equation (20) is the substantive positive intermediate result. The exact finite-place Weil coefficient list is not inserted into `T`; it is reconstructed from:

- the universal free cover of the prime generators and its energy multiplicities;
- the arithmetic one-particle energies `log p`;
- the canonical word-length gauge;
- the critical Gibbs square root `e^{-H/2}`.

In particular, the source now distinguishes both parts of von Mangoldt: prime-power support comes from simple spectral multiplicity, and the repetition-independent value `log p` comes from mean word energy.

This also explains why the normalized-state obstruction of `WP-255` is not an obstruction to the coefficient carrier itself. `WP-255` forbids infinitely many orthogonal **positive range masses** `1/p` inside a state of mass one. Here the critical object is a semifinite weight and the coefficient operator (18) is formed after passing to its half-density; no finite-mass packing inequality is asserted.

## 5. The positive operator is compact but sits exactly beyond Hilbert--Schmidt class

The exact carrier has a sharp critical size boundary. From (19), the nonzero eigenvalues of `T` are

\[
a_{p,k}=(\log p)p^{-k/2}.
\tag{21}
\]

They tend to zero, and above any fixed positive threshold only finitely many pairs `(p,k)` occur. Hence

\[
\boxed{T\text{ is compact}.}
\tag{22}
\]

It is also bounded; for `k>=1`,

\[
a_{p,k}\le\frac{\log p}{\sqrt p}\le\frac2e,
\tag{23}
\]

using the continuous maximum of `log x/sqrt x`.

For every `q>0`,

\[
\operatorname{Tr}(T^q)
=
\sum_p\sum_{k\ge1}
(\log p)^q p^{-kq/2}
=
\sum_p
\frac{(\log p)^q}{p^{q/2}-1}.
\tag{24}
\]

Consequently

\[
\boxed{
T\in\mathcal S_q
\quad\Longleftrightarrow\quad
q>2.
}
\tag{25}
\]

For `q>2`, convergence follows by comparison with `sum_n (log n)^q n^{-q/2}`. For `q<=2`, the summand is eventually at least a positive multiple of `1/p`, so Euler's divergence of `sum_p1/p` gives divergence. In particular,

\[
T\notin\mathcal S_2
\quad\text{and}\quad
T\notin\mathcal S_1.
\tag{26}
\]

Thus the critical finite carrier is a bounded compact positive operator, but not a finite Hilbert--Schmidt or trace-class object. This is the same critical all-prime pressure seen in several earlier forms, now expressed as an exact Schatten boundary rather than as failure of the coefficient operator to exist.

## 6. Why this still does not yield the finite Weil quadratic form

The positivity in (18) is diagonal on the free-word label space. On its simple sector,

\[
\langle c,Tc\rangle
=
\sum_{p,k\ge1}
\frac{\log p}{p^{k/2}}|c_{p,k}|^2
\ge0.
\tag{27}
\]

The conventional finite-place Weil quadratic contribution has a different geometry. In the normalization used by `WP-005` and `WP-009`, the same coefficient multiplies a translation autocorrelation,

\[
W_{\rm fin}(f)
=
-2\sum_{p,k\ge1}
\frac{\log p}{p^{k/2}}
\operatorname{Re}\langle f,\tau_{k\log p}f\rangle,
\tag{28}
\]

with the support-dependent finite interpretation used there. Pointwise autocorrelations in (28) are not nonnegative coordinate masses, and their sign is precisely what diagonal positivity in (27) forgets.

There is therefore no implication

\[
T\succeq0
\quad\Longrightarrow\quad
W_{\rm fin}\succeq0.
\tag{29}
\]

The two known direct transports are already classified. Treating the eigenvalues (21) as passive jump conductances gives the positive Dirichlet energy of `WP-009`; it differs from (28) by a positive diagonal self-energy whose all-prime value diverges, and the untruncated jump form has infinite energy on every nonzero compactly supported Weil test. Using the critical Bost--Connes divisibility Gram instead gives `WP-216`: the same half-density appears in a genuine positive Gram, but the desired local Weil ray is the indefinite defect `log p(I-G_p)`.

Nor does a Hilbert norm of half-density vectors fix the problem. Squaring such norms changes the resolved coefficient to `(log p)^2p^{-k}`, the same loss of linear oriented amplitude exposed by the canonical self-pairing calculation in `WP-226`. Taking modewise square roots recovers magnitudes but is a nonlinear readout, not a quadratic-form sign theorem.

The free-Fock carrier therefore solves a **coefficient provenance** problem that `WP-255` left open, not the orientation problem posed by the research mandate.

## 7. Matched controls and aggressive falsification

The mechanism is not uniquely Riemann-specific. Replace primes by a countable alphabet `j` with positive one-particle energies `epsilon_j` and assume there are no nontrivial integer relations between distinct multisets of energies. In the corresponding free Fock space, energy multiplicity is again the number of word permutations of a multiset. Simple non-vacuum eigenspaces are the pure repeated-letter words, and the same construction gives positive eigenvalues

\[
\epsilon_j e^{-k\epsilon_j/2}.
\tag{30}
\]

Thus free-word multiplicity plus critical half-density is a **generic source architecture** for a multiplicatively independent alphabet. The Riemann input is that unique factorization makes `epsilon_p=log p` relation-free at the multiset level and identifies (30) with the actual Mangoldt half-density. This matched control prevents treating the positivity of `T` itself as an arithmetic sign theorem.

The result also depends genuinely on leaving the commutative multiplicative semigroup. In the ordinary integer/Bost--Connes multiplicative basis there is one state per integer energy, so the ordered-word multiplicity (11) has been quotiented away by commutativity. The free Fock system is the universal noncommutative word cover of the prime generators. It is natural in the exact independent-channel escape already tested by `WP-255`, but it is a category enlargement, not hidden structure newly discovered inside the commutative integer basis.

If additional additive resonances are introduced between generator energies, spectral multiplicity can exceed the permutation count and the simple-spectrum selector need not isolate pure powers. The clean identity (20) therefore uses the unique-factorization independence of prime logarithms essentially.

Finally, the semifinite weight does not secretly restore a state. Equation (9) is intrinsic: normalizing `Psi_1` by its value on the identity is impossible. Any finite normalization must restrict, condition, or renormalize the source and then pass the existing source-selection and target-coding audits.

## 8. Prior art and novelty boundary

The operator-algebraic ingredients are classical. Full Fock space, Toeplitz--Cuntz creation operators, quasi-free dynamics, Gibbs/KMS weights, and their finite-type versus infinite-weight behavior are standard. Laca and Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, J. Funct. Anal. 211 (2004), 457--482, give the general Toeplitz--Pimsner KMS framework and KMS-weight extension used as the appropriate prior-art class; `WP-255` already records this audit. KMS states and weights on Nica--Toeplitz/product-system algebras provide the broader modern equilibrium context.

The combinatorics in (11) are also classical: the number of ordered prime factorizations of `n` is the multinomial coefficient of its prime-factor multiset. No novelty is claimed for that identity, unique factorization, free Fock construction, semifinite Gibbs weights, or the Schatten comparison in isolation.

The durable Mathia-specific delta is the exact combination at the live `WP-255` boundary:

\[
\boxed{
\text{critical semifinite prime Fock geometry}
+\text{simple energy multiplicity}
+\text{mean word energy}
\Longrightarrow
P_{\rm simp}HN^{-1}e^{-H/2}
\text{ with spectrum }\frac{\Lambda(n)}{\sqrt n}.
}
\tag{31}
\]

A bounded literature search across Bost--Connes/prime-energy systems, quasi-free Toeplitz--Cuntz KMS weights, free prime semigroups, and ordered prime factorizations found the individual ingredients and the general equilibrium theory, but no independent global Weil-positivity theorem arising from this simple-spectrum operator. Historical novelty is not claimed. The contribution is the exact source dictionary and, equally importantly, the demonstration that even after the semifinite escape succeeds at coefficient provenance, the required Weil orientation and completion remain absent.

## 9. Consequence for the Weil-positivity mandate

`WP-255` should not be read as saying that orthogonal prime Fock geometry cannot carry the critical arithmetic data at all. It says that it cannot carry them as mutually orthogonal positive range masses inside a **normalized** `KMS_1` state. In the canonical semifinite Fock representation, the obstruction disappears and the exact finite Mangoldt half-density can be assembled into the positive compact operator (18).

This materially narrows the unresolved question. Finite-prime support, repetition-independent `log p`, and critical `p^{-k/2}` can all be recovered without zero data inside a single source-defined semifinite model. What is still missing is the difficult part of the research mandate: a source-derived map from that carrier into the Weil test-function geometry whose **own** positivity theorem produces the oriented translation term and at the same time supplies the Gamma and polar sectors.

Any proposed continuation should therefore be killed unless it does more than read off (20). A successful next step must couple or quotient the word carrier before scalarization in a way fixed independently of the desired sign, survive generalized-alphabet controls, avoid the divergent passive-jump diagonal, and yield a completed finite--archimedean form. `WP-256` supplies no such global operation and makes no RH claim.