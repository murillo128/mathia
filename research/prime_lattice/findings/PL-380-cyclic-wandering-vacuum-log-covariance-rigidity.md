# PL-380 — Cyclic wandering vacuum plus log-prime covariance rigidifies to the canonical prime shift

**Evidence:** `DERIVED+CLASSICAL-MODEL-IDENTIFICATION + DECISIVE-BOUNDARY`.

**Parent finding:** `PL-379`.

**Related findings:** `PL-001`, `PL-004`, `PL-007`, `PL-023`, `PL-024`, `PL-203`, `PL-379`.

**Status:** `THE-MOST-CANONICAL-GLOBAL-RIGIDITY-REPAIRS-LEFT-BY-PL-379-DO-EXCLUDE-THE-DIFFUSE-INFINITE-WOLD-PATHOLOGY, BUT-THEY-CLOSE-BACK-TO-THE-STANDARD-PRIME-MULTISHIFT-AND-DIAGONAL-LOG-N-ENERGY. A-GENERATING-JOINT-WANDERING-VACUUM-MAKES-A-DOUBLY-COMMUTING-PRIME-ISOMETRY-FAMILY-UNITARILY-EQUIVALENT-TO-THE-LEFT-REGULAR-SHIFT-OF-THE-FREE-COMMUTATIVE-MONOID; EXACT-COMMUTATOR-WEIGHTS-LOG-P-THEN-FORCE-ENERGY-C-PLUS-LOG-N. THIS-REMOVES-GENERIC-REPRESENTATION-FREEDOM-BUT-SUPPLIES-NO-NEW-ANALYTIC-CONTINUATION-OR-CRITICAL-LINE-RIGIDITY`.

## Claim

Let `P` be the rational primes and let

\[
\{V_p:p\in\mathcal P\}
\tag{PL380-1}
\]

be a commuting, doubly commuting family of isometries on a Hilbert space `H`:

\[
V_pV_q=V_qV_p,
\qquad
V_p^*V_q=V_qV_p^*
\quad(p\ne q).
\tag{PL380-2}
\]

Write

\[
W=\bigcap_{p\in\mathcal P}\ker V_p^*
\tag{PL380-3}
\]

for the joint wandering subspace, and for a finite-support exponent vector `alpha` write

\[
V^\alpha=\prod_p V_p^{\alpha_p}.
\tag{PL380-4}
\]

Assume that `W` is generating:

\[
\mathcal H
=
\overline{\operatorname{span}}
\{V^\alpha W:\alpha\in\mathbb N_0^{(\mathcal P)}\}.
\tag{PL380-5}
\]

Then the orbit subspaces are mutually orthogonal,

\[
V^\alpha W\perp V^\beta W
\qquad(\alpha\ne\beta),
\tag{PL380-6}
\]

and the map

\[
U:\ell^2(\mathbb N_0^{(\mathcal P)})\otimes W\to\mathcal H,
\qquad
U(e_\alpha\otimes w)=V^\alpha w,
\tag{PL380-7}
\]

extends to a unitary satisfying

\[
U^*V_pU=S_p\otimes I_W,
\tag{PL380-8}
\]

where `S_p e_alpha=e_{alpha+e_p}` is the coordinate unilateral shift.

In the multiplicity-one case `W=C Omega`, unique factorization identifies

\[
\ell^2(\mathbb N_0^{(\mathcal P)})\simeq\ell^2(\mathbb N),
\qquad
e_\alpha\leftrightarrow e_n,
\quad
n=\prod_p p^{\alpha_p},
\tag{PL380-9}
\]

and (PL380-8) becomes exactly

\[
V_pe_n=e_{pn}.
\tag{PL380-10}
\]

Thus a **cyclic joint wandering vacuum** removes the diffuse global Wold freedom of `PL-379`, but it does so by forcing the ordinary left-regular prime shift already underlying the Bohr/Dirichlet coefficient model.

If one further introduces a symmetric/self-adjoint energy operator `A` whose algebraic orbit span is an invariant core, assumes

\[
A\Omega=c\Omega,
\tag{PL380-11}
\]

and imposes the exact prime covariance

\[
[A,V_p]=(\log p)V_p
\tag{PL380-12}
\]

on that core, then induction gives

\[
AV^\alpha\Omega
=
\left(c+\sum_p\alpha_p\log p\right)V^\alpha\Omega
=
(c+\log n)V^\alpha\Omega.
\tag{PL380-13}
\]

Hence the second natural repair suggested after `PL-379` also rigidifies to the classical diagonal `log n` Hamiltonian, up to an additive constant.

This is a **representation-rigidity boundary, not an RH mechanism**. The wandering-vacuum argument is valid for any countable free commutative monoid, and the covariance argument works verbatim with arbitrary assigned real weights `lambda_p`, producing energy `c+sum alpha_p lambda_p`. Rational-prime arithmetic enters only by externally selecting `lambda_p=log p`. Neither step produces analytic continuation, the functional equation, a completed trace formula, a zero-sensitive determinant, or a reason for `Re(s)=1/2`.

## 1. Orthogonality of the joint wandering orbit

Take `alpha != beta` and set

\[
\gamma_p=\min(\alpha_p,\beta_p),
\qquad
r=\alpha-\gamma,
\qquad
s=\beta-\gamma.
\tag{PL380-14}
\]

The supports of `r` and `s` are disjoint and at least one is nonzero. Because `V^gamma` is an isometry, it is enough to compare `V^rW` and `V^sW`. Suppose `r != 0` and choose `p` with `r_p>0`. Then `s_p=0`. Double commutativity lets every adjoint occurring in `(V^r)^*` pass through every factor of `V^s`, so for `w,y in W`,

\[
\langle V^rw,V^sy\rangle
=
\langle w,(V^r)^*V^sy\rangle
=
\langle w,V^s(V^r)^*y\rangle.
\tag{PL380-15}
\]

But `(V^r)^*` contains a factor `V_p^*`, and `V_p^*y=0` by the definition of `W`. Therefore (PL380-15) vanishes, proving (PL380-6).

Every `V^alpha` is an isometry, so each map `w -> V^alpha w` preserves the norm on `W`. Together with orthogonality, this makes (PL380-7) an isometry on the algebraic direct sum. The generating assumption (PL380-5) makes its range dense; an isometry has closed range, so the extension is onto and hence unitary. Equation (PL380-8) follows on basis vectors.

No countable-infinite limiting Wold theorem is needed. The strong global hypothesis (PL380-5) has directly selected the pure regular sector and excluded every unitary or diffuse type component by assumption.

## 2. Exact log-prime covariance has no residual freedom on the cyclic orbit

Assume now `W=C Omega`, normalize `Omega`, and impose (PL380-11)--(PL380-12). For one prime,

\[
AV_p\Omega
=
V_pA\Omega+(\log p)V_p\Omega
=
(c+\log p)V_p\Omega.
\tag{PL380-16}
\]

Iterating the commutator relation yields

\[
[A,V_p^k]=k(\log p)V_p^k
\tag{PL380-17}
\]

on the invariant algebraic core. Since the prime shifts commute, applying (PL380-17) one coordinate at a time gives (PL380-13).

Under (PL380-9), the resulting diagonal is therefore

\[
Ae_n=(c+\log n)e_n.
\tag{PL380-18}
\]

If the algebraic orbit is a core for `A`, this determines the self-adjoint operator itself rather than only its restriction to a dense invariant domain. Thus the pair

\[
(\text{cyclic wandering prime shifts},\ \text{exact }\log p\text{ covariance})
\tag{PL380-19}
\]

has essentially no representation-theoretic freedom left: it is the canonical prime multishift with the canonical additive logarithmic energy.

This is precisely why the result is negative for the research route. The two obvious global conditions that repair the diffuse counterexample of `PL-379` do not reveal an intermediate arithmetic structure; together they return to the standard coefficient/occupation-number model already present in the classical Bohr and Bost--Connes/primon-gas prior art recorded earlier in this line.

## 3. Generic-frequency adversarial control

The first half of the argument never mentions numerical prime values. Replace the coordinate set `P` by any countable alphabet `J`. A doubly commuting isometric family `{V_j}` with a generating joint wandering subspace again has the model

\[
\ell^2(\mathbb N_0^{(J)})\otimes W.
\tag{PL380-20}
\]

For the second half, choose arbitrary real numbers `lambda_j` and impose

\[
[A,V_j]=\lambda_jV_j,
\qquad
A\Omega=c\Omega.
\tag{PL380-21}
\]

Exactly the same induction gives

\[
AV^\alpha\Omega
=
\left(c+\sum_j\alpha_j\lambda_j\right)V^\alpha\Omega.
\tag{PL380-22}
\]

Consequently, neither the wandering-vacuum rigidity nor additive energy covariance distinguishes rational primes from a generic frequency tuple. The arithmetic statement

\[
\sum_p\alpha_p\log p=\log\!\left(\prod_pp^{\alpha_p}\right)
\tag{PL380-23}
\]

is exact and important, but once the weights `log p` have been supplied it is simply the additive character of the free commutative exponent monoid. No zero localization follows from this algebra alone.

This passes the line's generic-frequency falsification test in the **negative** direction: the proposed repair is too universal to explain a specifically zeta-theoretic critical line.

## 4. Prior art and novelty audit

The model reached in (PL380-7)--(PL380-10) is classical rather than new. Hedenmalm--Lindqvist--Seip's Hilbert space of Dirichlet series identifies square-summable Dirichlet coefficients with the Hardy/Bohr coefficient model in which multiplication by a prime monomial acts as the corresponding coordinate shift. The standard exponent-vector/Bohr representation is baseline prior art under the research mandate and is not claimed as a discovery here.

Likewise, the diagonal energy `log n=sum_p v_p(n)log p` and its prime-shift covariance are already part of the established primon-gas/Bost--Connes side of the literature recorded in `SOURCES.md`; `PL-024` already audits the canonical vacuum/log-energy completion against that prior art.

The elementary derivation above is included only to close the exact escape left open by `PL-379`. A repository novelty search found no stored `PL-*` finding making this specific implication from **generating joint wandering vacuum** to the regular prime multishift and then from exact `log p` covariance to the diagonal `log n` energy. The durable delta is therefore not a new multishift theorem. It is the route conclusion:

\[
\text{diffuse infinite-prime Wold freedom}
\xrightarrow{\text{generating wandering vacuum}}
\text{canonical regular shift}
\xrightarrow{[A,V_p]=\log p\,V_p}
\text{canonical }\log n\text{ energy},
\tag{PL380-24}
\]

with no new RH-sensitive structure created at either arrow.

## 5. Boundary conditions and falsification tests

This conclusion is intentionally narrow.

First, the generating hypothesis (PL380-5) is strong. It does not follow from double commutativity alone and is exactly what removes the unitary/diffuse sectors exhibited by `PL-379`. A representation with an additional reducing component outside the orbit of `W` is not covered.

Second, double commutativity is essential to the simple orthogonality proof. Mere commutativity of the isometries does not imply (PL380-6).

Third, if `dim W>1`, the conclusion is the regular prime shift with multiplicity `dim W`, not the scalar coefficient model.

Fourth, the energy conclusion requires a common invariant algebraic orbit core, the vacuum eigenvector condition (PL380-11), and the exact commutator law (PL380-12). Without those domain and covariance hypotheses, many other self-adjoint operators can coexist with the same shifts.

Fifth, the result does not say that the canonical prime shift is irrelevant to RH. It says only that **forcing that representation is not itself new RH structure**. Any successful use must add an observable or global relation not already determined by the free-monoid shift plus additive log-energy and must survive the line's Helson/Beurling/generic-frequency controls.

This finding should be corrected if the orthogonality implication (PL380-6) fails under (PL380-2)--(PL380-5), if the generating map (PL380-7) can fail to be unitary, or if exact covariance on a genuine operator core leaves self-adjoint energy freedom beyond (PL380-18). Each point is an elementary operator calculation rather than an unverified literature assertion.

## Consequence for `prime_lattice`

`PL-379` showed that finite-prime Wold classification cannot be globalized in general. The present result says that the most obvious way to restore global rigidity is **too strong to be informative**: a cyclic joint wandering vacuum selects the universal regular representation, and exact rational-prime energy covariance then selects the universal logarithmic Hamiltonian attached to the chosen weights.

Accordingly, the next useful condition cannot merely be “canonical vacuum” or “exact `log p` commutator.” A genuinely new mechanism must sit between the two extremes already audited by the line: it must exclude generic diffuse `N_0^infinity` representation freedom without collapsing all the way to the baseline regular shift/log-energy model, or it must add target-relative/global analytic data to that canonical model that is not reproducible for an arbitrary countable frequency tuple. Mellin/Nyman coupling, completed Weil data, or another source-forced relation remain admissible targets only if they supply that extra arithmetic content rather than restating (PL380-24).