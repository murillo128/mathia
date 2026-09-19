# PL-379 — Infinite-prime doubly commuting shifts can fail to globalize finite Wold decompositions

**Evidence:** `LITERATURE+EXACT-SPECIALIZATION + PRIOR-ART-REDIRECT + DECISIVE-BOUNDARY`.

**Parent finding:** `PL-378`.

**Related findings:** `PL-023`, `PL-024`, `PL-197`, `PL-203`, `PL-377`, `PL-378`.

**Status:** `ONE-SIDED-NONINVERTIBILITY-REMAINS-A-GENUINELY-INFINITE-DIMENSIONAL-ESCAPE-FROM-THE-SCALARIZATION-RESULTS: EVEN-DOUBLY-COMMUTING-ISOMETRIC-REPRESENTATIONS-OF-THE-COUNTABLE-FREE-COMMUTATIVE-PRIME-SEMIGROUP-NEED-NOT-ADMIT-A-GLOBAL-PURE/UNITARY-WOLD-DECOMPOSITION, ALTHOUGH-EVERY-FINITE-PRIME-RESTRICTION-DOES. THIS-FAILURE-IS-GENERIC-TO-N_0^(N), USES-NO-LOG-P-WEIGHTS-OR-RATIONAL-PRIME-ARITHMETIC, AND-THEREFORE-IS-A-ROUTE-BOUNDARY-RATHER-THAN-AN-RH-MECHANISM`.

## Claim

Enumerate the rational primes as `p_1,p_2,...`. Unique factorization identifies the positive-integer exponent semigroup exactly with

\[
\mathbb N_{>0}
\simeq
\mathbb N_0^{(\mathcal P)}
\simeq
\mathbb N_0^\infty
:=
\{(n_i)_{i\ge1}: n_i\in\mathbb N_0,\ n_i=0\text{ eventually}\},
\tag{PL379-1}
\]

through

\[
n=\prod_i p_i^{v_{p_i}(n)}
\longleftrightarrow
(v_{p_i}(n))_{i\ge1}.
\tag{PL379-2}
\]

C. H. Namitha, S. Sundar, and Shankar Veerabathiran prove that the familiar finite-dimensional Wold classification for doubly commuting isometries does **not** automatically globalize to this countably generated semigroup. Their Remark 4.8 gives the discrete `N_0^\infty` analogue explicitly: there exists a doubly commuting isometric representation

\[
V:\mathbb N_0^\infty\longrightarrow B(\mathcal K)
\tag{PL379-3}
\]

which admits no Wold decomposition of the form

\[
\mathcal K
=
\bigoplus_{g\in\{0,1\}^{\mathbb N}}\mathcal K_g,
\tag{PL379-4}
\]

with every `K_g` reducing for all coordinate isometries and with coordinate `i` pure on `K_g` when `g(i)=1` and unitary when `g(i)=0`.

At the same time, the restriction to **every finite set of coordinates** has the ordinary finite Wold decomposition. Hence the implication

\[
\text{all finite-prime restrictions are Wold-classifiable}
\quad\Longrightarrow\quad
\text{the full prime family has a global Wold decomposition}
\tag{PL379-5}
\]

is false.

For `prime_lattice`, this closes a tempting continuation of `PL-378`: one cannot eliminate the surviving intrinsically one-sided/noninvertible case merely by classifying every finite tuple of prime shifts into pure and unitary sectors and passing to the limit.

The result is nevertheless **not positive RH structure**. The counterexample depends only on the abstract countable free commutative monoid. It uses neither the arithmetic weights `log p`, the distinguished rational-prime sequence, analytic continuation of zeta, the functional equation, nor any zero-sensitive observable. Thus the infinite-coordinate pathology enlarges the admissible representation theory but supplies no rational-prime selectivity by itself.

## 1. The paper's infinite-coordinate obstruction matches the exponent semigroup exactly

Namitha--Sundar--Veerabathiran define Wold decomposition for a countably generated doubly commuting isometric semigroup by assigning to each binary type

\[
g\in\{0,1\}^{\mathbb N}
\tag{PL379-6}
\]

a reducing sector on which each coordinate is either unitary or pure. Immediately before Proposition 4.7 they state that the same definition applies to representations of

\[
\mathbb N_0^\infty
=
\{(m_i):m_i\in\mathbb N_0,\ m_i=0\text{ eventually}\}.
\tag{PL379-7}
\]

This is not merely analogous to the prime-exponent cone; after choosing the enumeration `p_i`, it **is** the prime-exponent cone as a semigroup.

Their Proposition 4.7 first constructs a continuous `R_+^\infty` example without Wold decomposition. Remark 4.8 then gives the discrete construction required here. Start with a strongly pure doubly commuting representation `S` of `N_0^\infty`, a unitary representation `U` that doubly commutes with it, and the Bernoulli type space

\[
X=\{0,1\}^{\mathbb N}
\tag{PL379-8}
\]

with a non-atomic infinite product measure `mu` (for example the fair Bernoulli product). On the fiber indexed by `x in X`, define coordinate `i` by

\[
V_i(x)=
\begin{cases}
S_i,&x_i=1,\\
U_i,&x_i=0.
\end{cases}
\tag{PL379-9}
\]

Taking the corresponding decomposable operators on

\[
\mathcal K=L^2(X,\mathcal H)
\tag{PL379-10}
\]

gives a doubly commuting isometric representation of `N_0^\infty`.

The decisive point is measure-theoretic rather than spectral. For the first `d` coordinates, the finite Wold decomposition is the cylinder decomposition

\[
X_{g,d}
=
\{x\in X:x_i=g(i),\ 1\le i\le d\},
\qquad g\in\{0,1\}^d.
\tag{PL379-11}
\]

Each cylinder has positive measure, so every finite-coordinate restriction decomposes normally. If a global decomposition (PL379-4) existed, uniqueness of every finite Wold decomposition would force

\[
\mathcal K_g
\subseteq
L^2\!\left(\bigcap_{d\ge1}X_{g,d},\mathcal H\right)
=
L^2(\{g\},\mathcal H).
\tag{PL379-12}
\]

But every singleton has product measure zero:

\[
\mu(\{g\})=0.
\tag{PL379-13}
\]

Therefore every putative `K_g` is zero, contradicting (PL379-4). The finite classifications are all correct; what fails is their atomic globalization over infinitely many coordinate types.

This is exactly the kind of infinite-prime obstruction that no fixed finite-prime audit can see.

## 2. Consequence for the one-sided escape left by PL-378

`PL-377` scalarized bounded normal completely multiplicative representations. `PL-378` then removed normality when the representation extends invertibly and uniformly boundedly to the full rational group `Q_{>0}^x`: Day--Dixmier unitarization reduces that case to a spectral measure of scalar torus characters.

A natural next hope is that the remaining noninvertible semigroup case is still harmless because isometries have Wold decompositions. For a fixed finite set of prime generators this is a powerful classification principle. The present prior art shows that this argument is not valid for the full countably infinite prime family, even after imposing the strong relation of **double commutativity**.

Consequently, the route

\[
\text{noninvertible prime isometries}
\to
\text{finite-prime Wold models}
\to
\text{global pure/unitary sector decomposition}
\to
\text{scalar/standard-shift reduction}
\tag{PL379-14}
\]

breaks at its third arrow. The obstruction is not a technical lack of a proof; an explicit counterexample exists.

This sharpens rather than contradicts `PL-203`. That finding showed that noninvertibility itself does not create arithmetic rigidity: broad noninvertible weighted-shift classes remain programmable. `PL-379` adds that even the very restrictive doubly commuting **isometric** subclass has genuinely infinite-coordinate representation behavior that cannot be reconstructed from all its finite coordinate Wold decompositions.

Thus one-sidedness is a real escape from the scalarization results, but it is also a very large and nonrigid escape. Merely moving from invertible/unitary prime actions to unilateral isometries does not supply the missing RH mechanism.

## 3. Why the counterexample is not arithmetic

Nothing in the construction distinguishes the rational primes from an arbitrary countable alphabet. Replacing `p_i` by any countable set of formal generators leaves (PL379-7)--(PL379-13) unchanged. In particular, the construction never uses

\[
E(v)=\sum_p v_p\log p=\log n,
\tag{PL379-15}
\]

or the Kronecker trajectory

\[
t\longmapsto(e^{-it\log p})_p.
\tag{PL379-16}
\]

It therefore passes the structural existence test but fails the line's arithmetic-selectivity test. One can manufacture the same global Wold failure before assigning any numerical frequency to a coordinate.

This matters for interpretation. The result must **not** be read as saying that a hidden infinite-prime sector is a plausible source of the Riemann zeros. It says instead that abstract operator theory leaves enough room that finite-prime classification cannot eliminate such sectors. Any RH-relevant use must add an arithmetic condition that rules out generic diffuse type fields like (PL379-8) while retaining a canonical representation tied to zeta.

Candidates for such extra conditions would have to be independently justified by the arithmetic problem: a canonical cyclic vacuum, exact `log p` energy covariance, a target-relative Mellin/Nyman condition, completed Fourier/Weil data, or another global constraint. But those conditions cannot simply be asserted as a repair. In particular, `PL-024` already records that the canonical vacuum/log-energy shift realization leads to the classical Bost--Connes system and its `beta=1` thermodynamic boundary rather than a new `1/2` selector.

## 4. Prior art and novelty audit

The decisive source is:

- **C. H. Namitha, S. Sundar, Shankar Veerabathiran**, “Doubly Commuting Semigroups of Isometries,” arXiv:2509.00409v2 [math.OA] (3 September 2025), https://arxiv.org/abs/2509.00409. Definition 4.6 defines the countably infinite pure/unitary Wold decomposition, Proposition 4.7 proves failure for `R_+^\infty`, and Remark 4.8 states the discrete `N_0^\infty` construction and the corresponding failure of Wold decomposition.

The operator theorem and counterexample are therefore **prior art**, not a Mathia discovery. The exact specialization

\[
\mathbb N_0^\infty\cong\mathbb N_0^{(\mathcal P)}
\tag{PL379-17}
\]

is elementary. The durable research delta is the recognition that this theorem closes a specific post-`PL-378` strategy: finite-prime Wold classification cannot be promoted to a general infinite-prime scalarization theorem.

A repository novelty search found no existing `prime_lattice` finding or local source entry using Wold decomposition or this countably infinite counterexample. The closest stored boundaries are `PL-197`/`PL-203` on weighted-shift programmability and `PL-377`/`PL-378` on scalarization of normal or uniformly group-like representations; none supplies the infinite-coordinate Wold obstruction above.

## 5. Boundary conditions and adversarial checks

The negative is intentionally narrow.

First, it does **not** say that every infinite doubly commuting family lacks a Wold decomposition. It gives existence of families for which the global binary-type decomposition fails.

Second, it does **not** say that the canonical prime shift on `ell^2(N)` is pathological. Under the identification `ell^2(N) ~= ell^2(N_0^(P))`, the coordinate shifts

\[
S_p e_n=e_{pn}
\tag{PL379-18}
\]

have the distinguished vacuum `e_1` and the usual monomial/Fock structure. The prior-art counterexample is a diffuse direct-integral representation designed so that the infinitely many pure/unitary type coordinates do not concentrate on atoms. A theorem exploiting the canonical vacuum or another arithmetic feature of the standard shift is outside this negative.

Third, no conclusion about analytic continuation follows from Wold failure. The source is pure operator theory. It neither constructs a continuation of an Euler product nor produces a functional equation, determinant, trace formula, resonance set, or zero divisor.

Fourth, finite-prime truncations remain completely legitimate local tools. What is forbidden is the unstated inference that compatible finite decompositions must assemble into an atomic global decomposition indexed by one binary sequence `g`.

Fifth, the obstruction persists before the frequencies `log p` are introduced, so it cannot by itself explain why `Re(s)=1/2` is distinguished. Any proposal that uses this pathology positively must exhibit a further rational-prime-specific bridge and survive the Beurling/Helson controls in the line mandate.

## Audit / falsification tests

This finding would need correction if any of the following fails:

1. Remark 4.8 of arXiv:2509.00409v2 does not give a doubly commuting isometric representation of the discrete finite-support semigroup `N_0^\infty` without Wold decomposition;
2. the semigroup `N_0^\infty` used there is not isomorphic to the positive-integer exponent semigroup under unique factorization;
3. some additional hypothesis already intrinsic to the **general** prime-lattice representation problem forces all admissible representations to avoid the diffuse construction, rather than being an extra structure of a particular zeta model;
4. the finite-coordinate restrictions in the construction fail the ordinary finite Wold theorem used in the source's contradiction argument.

Items 1, 2, and 4 are explicit/theorem-level. Item 3 is the live boundary: extra arithmetic structure may restore rigidity, but then that structure, rather than one-sided noninvertibility or double commutativity alone, is doing the mathematical work.

## Consequence for `prime_lattice`

The surviving operator-design space after `PL-378` should not be described simply as “classify unilateral prime shifts.” Countably many prime directions already admit non-atomic pure/unitary type fields that defeat the naive infinite Wold globalization, while finite-prime tests see no failure.

The useful target is narrower: identify **arithmetically canonical global conditions** that exclude this generic `N_0^\infty` representation freedom and still retain genuinely one-sided information. A candidate that only assumes exact complete multiplicativity, isometricity, and double commutativity remains too universal; it can exhibit infinite-coordinate pathology with no zeta content whatsoever. Conversely, once enough structure is imposed to force the standard vacuum/log-energy model, the prior-art gate must be checked against `PL-024` and the established Bost--Connes/adelic completions rather than treating that canonicalization as new RH structure.