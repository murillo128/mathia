# MC-163 — Cross-prime commutator Gram transport has factorized phase and trivial cycle holonomy

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue in the canonical number-state representation used in `MC-149`–`MC-162`,

\[
\mathcal H=\ell^2(\mathbb N),
\qquad
S_p\varepsilon_n=\varepsilon_{pn}.
\]

To test whether the first genuinely non-diagonal quadratic relation between distinct prime directions carries a new Möbius phase, it is useful to keep a matched local-phase family rather than only the actual sign choice. Fix unimodular numbers

\[
z_p\in\mathbb T
\]

for the primes and define the square-free multiplicative control

\[
f_z(n)=
\begin{cases}
\displaystyle\prod_{p\mid n}z_p,&n\text{ squarefree},\\
0,&n\text{ not squarefree}.
\end{cases}
\tag{1}
\]

Let `D_z` be the bounded diagonal `D_z\varepsilon_n=f_z(n)\varepsilon_n` and

\[
C_p^{(z)}:=[D_z,S_p].
\tag{2}
\]

The actual Möbius diagonal is the specialization `z_p=-1` for every prime.

For distinct primes `p\ne q`, define the cross-prime Gram operator

\[
G_{pq}^{(z)}:=\big(C_p^{(z)}\big)^*C_q^{(z)}.
\tag{3}
\]

Then there is an exact factorization

\[
\boxed{
G_{pq}^{(z)}=(1-z_p)(1-\overline{z_q})V_{p\to q},
\qquad p\ne q,
}
\tag{4}
\]

where `V_{p\to q}` is the phase-free partial isometry

\[
V_{p\to q}\varepsilon_n=
\begin{cases}
\varepsilon_{qn/p},&n\text{ squarefree},\ p\mid n,\ q\nmid n,\\
0,&\text{otherwise}.
\end{cases}
\tag{5}
\]

Thus the non-diagonal arithmetic action is only **prime-support replacement**. All dependence on the phase deformation separates into one factor attached to `p` and one conjugate factor attached to `q`.

The diagonal Gram term is equally local:

\[
\boxed{
G_{pp}^{(z)}\varepsilon_n=
\begin{cases}
0,&n\text{ not squarefree},\\
\varepsilon_n,&n\text{ squarefree and }p\mid n,\\
|1-z_p|^2\varepsilon_n,&n\text{ squarefree and }p\nmid n.
\end{cases}
}
\tag{6}
\]

Consequently every closed cycle of distinct prime replacements has trivial phase holonomy. If `p_0,\ldots,p_{r-1}` are distinct and `p_r=p_0`, then on the square-free sector where `p_0` is present and `p_1,\ldots,p_{r-1}` are absent,

\[
\boxed{
G_{p_{r-1}p_0}^{(z)}\cdots G_{p_1p_2}^{(z)}G_{p_0p_1}^{(z)}
=
\left(\prod_{j=0}^{r-1}|1-z_{p_j}|^2\right)P_{\rm cyc},
}
\tag{7}
\]

where `P_cyc` is the projection onto that admissible square-free support sector; the product vanishes off the corresponding path domain. The coefficient in `(7)` is nonnegative real. No relative prime phase survives around the cycle.

For Möbius, `z_p=-1`, equations `(4)` and `(7)` reduce to

\[
\boxed{
G_{pq}^{(\mu)}=4V_{p\to q},
\qquad
G_{p_{r-1}p_0}^{(\mu)}\cdots G_{p_0p_1}^{(\mu)}=4^rP_{\rm cyc}.
}
\tag{8}
\]

Hence the most immediate non-diagonal escape left by `MC-159` — pairwise commutator Gram/covariance data and its cycle holonomy — does not create a source-forced cross-prime Möbius phase. It is phase-sensitive only through separable one-prime amplitudes and otherwise transports square-free support.

This does **not** say that the entire noncommutative Bost–Connes route is phase-blind. It closes the quadratic Gram layer and the closed words generated solely by these pairwise replacement edges. Odd orientation-bearing words, twisted commutators, coefficient/semigroup mixed words not reducible to this Gram system, or another independently natural relational observable remain outside the theorem.

## 1. Exact commutator coefficients

Write

\[
b_p^{(z)}(n):=f_z(pn)-f_z(n).
\tag{9}
\]

Then

\[
C_p^{(z)}\varepsilon_n=b_p^{(z)}(n)\varepsilon_{pn}.
\tag{10}
\]

If `n` is not squarefree, both terms in `(9)` vanish. If `n` is squarefree, there are two cases:

\[
b_p^{(z)}(n)=
\begin{cases}
-f_z(n),&p\mid n,\\
(z_p-1)f_z(n),&p\nmid n.
\end{cases}
\tag{11}
\]

Since the image basis vectors are orthogonal, the adjoint satisfies

\[
\big(C_p^{(z)}\big)^*\varepsilon_m=
\begin{cases}
\overline{b_p^{(z)}(m/p)}\,\varepsilon_{m/p},&p\mid m,\\
0,&p\nmid m.
\end{cases}
\tag{12}
\]

Equation `(6)` follows immediately from `(10)`–`(12)` by taking `m=pn` and using `|f_z(n)|=1` on square-free integers.

## 2. The cross-prime coefficient separates exactly

Take distinct primes `p\ne q`. From `(10)`–`(12)`,

\[
G_{pq}^{(z)}\varepsilon_n=0
\]

unless `p\mid n`; when `p\mid n`,

\[
G_{pq}^{(z)}\varepsilon_n
=
b_q^{(z)}(n)\,
\overline{b_p^{(z)}(qn/p)}\,
\varepsilon_{qn/p}.
\tag{13}
\]

If `n` is nonsquarefree, the first coefficient is zero. Suppose now that `n` is squarefree and `p\mid n`.

If also `q\mid n`, then `qn/p` is not squarefree, so the second coefficient in `(13)` vanishes. Thus a nonzero cross term requires

\[
p\mid n,
\qquad q\nmid n.
\tag{14}
\]

Write `n=pm`, with `m` squarefree and coprime to `pq`. Then

\[
b_q^{(z)}(n)=(z_q-1)f_z(n),
\tag{15}
\]

while `qn/p=qm` is squarefree, `p\nmid qm`, and

\[
f_z(qm)=f_z(n)\frac{z_q}{z_p}.
\tag{16}
\]

Therefore

\[
\begin{aligned}
b_q^{(z)}(n)\,
\overline{b_p^{(z)}(qm)}
&=(z_q-1)f_z(n)\,
\overline{(z_p-1)f_z(n)z_q/z_p}\\
&=(1-z_p)(1-\overline{z_q}).
\end{aligned}
\tag{17}
\]

The accumulated phase `f_z(n)` cancels exactly. Combining `(13)`–`(17)` proves `(4)`–`(5)`.

For the Möbius specialization every local phase is `-1`, so `(17)` equals `4` independently of `n,p,q`. The apparent cross-prime operator therefore contains no alternating sign coefficient at all.

## 3. The normalized relation is a support-replacement partial isometry

The phase-free operator in `(5)` satisfies

\[
V_{p\to q}^*=V_{q\to p}.
\tag{18}
\]

Let `P_{p\bar q}^{\rm sf}` project onto square-free basis states divisible by `p` and not by `q`. Directly from the basis action,

\[
\boxed{
V_{p\to q}^*V_{p\to q}=P_{p\bar q}^{\rm sf},
\qquad
V_{p\to q}V_{p\to q}^*=P_{q\bar p}^{\rm sf}.
}
\tag{19}
\]

So, whenever `(1-z_p)(1-\overline{z_q})\ne0`, normalizing the cross Gram operator removes **all** phase dependence and leaves an exact partial bijection between two square-free prime-support sectors.

This is stronger than observing that a quadratic statistic loses one sign. The whole off-diagonal operator has a fixed geometric action independent of the phase assignment; the phase assignment contributes only the scalar edge weight

\[
a_p\overline{a_q},
\qquad a_p:=1-z_p.
\tag{20}
\]

Hence the matrix of cross-edge weights is rank one in the prime-local defect vector `a=(a_p)`. There is no additional pairwise interaction parameter.

The degeneracy `z_p=1` is also transparent: then `a_p=0`, so every outgoing cross edge from a state requiring the `p`-absent finite difference disappears. This is a local loss of sensitivity, not an emergent cross-prime cancellation effect.

## 4. Closed Gram paths have no phase holonomy

Consider a simple directed cycle

\[
p_0\to p_1\to\cdots\to p_{r-1}\to p_0
\tag{21}
\]

through distinct primes. On a square-free state whose support contains `p_0` but none of `p_1,\ldots,p_{r-1}`, the normalized replacement operators successively remove the current prime and insert the next. After `r` steps the original support is restored exactly.

Using `(20)`, the unnormalized scalar accumulated around the cycle is

\[
\prod_{j=0}^{r-1}a_{p_j}\overline{a_{p_{j+1}}}
=
\prod_{j=0}^{r-1}|a_{p_j}|^2,
\qquad p_r=p_0.
\tag{22}
\]

This proves `(7)`. In particular, the argument of the cycle coefficient is always zero whenever the coefficient is nonzero. The prime-local phases cannot generate a nontrivial Wilson-loop/holonomy-type phase at the Gram level.

For Möbius, `a_p=2`, so every admissible length-`r` cycle contributes precisely the positive scalar `4^r`. Any statistic built only from these closed Gram paths can certainly retain support/divisibility information and path multiplicities, but **its canonical cycle coefficient does not contain the alternating Möbius orientation**.

One can insert external signs or phase-dependent weights into a later aggregate, but then those weights are additional input. The pairwise Gram relation itself has not generated the desired global phase coupling.

## 5. Relation to the existing commutator boundary

`MC-149` showed that raw semigroup commutators lie between two useless endpoints: boundedness is universal for bounded diagonals, while compact/Schatten decay excludes Möbius. `MC-156`–`MC-159` then showed that scalar magnitude summaries lose orientation whereas finite signed scalarizations are either support-only or retain a complete Mertens channel across scales.

`MC-159` explicitly left genuinely noncommutative products as one possible escape because they are not scalar functions of the commuting pulled-back tuple `B_p=S_p^*[D_\mu,S_p]`.

The present calculation enters that residual class but closes its first quadratic member. The operators `C_p^*C_q` are genuinely off-diagonal when `p\ne q`, yet their noncommutativity is only the combinatorics of replacing one prime in a square-free support set by another. Their phase coefficient factorizes at the two endpoints and their closed-path phase is trivial.

This is also consistent with `MC-138`, which killed phase-sensitive covariance inside the **diagonal** divisibility algebra. `MC-163` is not a restatement of that product-state result: no KMS factorization is used here, and the operators in `(4)` are non-diagonal partial isometries. The new obstruction is algebraic cancellation of the accumulated square-free phase inside the cross Gram product itself.

## 6. Prior-art and novelty audit

The Bost–Connes system and its multiplicative semigroup action are classical. Bost and Connes introduced the number-theoretic quantum statistical mechanical system in *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica **1** (1995), 411–457, DOI `10.1007/BF01589495`. Semigroup crossed-product structure and dilations of the Bost–Connes Hecke C*-algebra are standard; see Marcelo Laca, *From Endomorphisms to Automorphisms and Back: Dilations and Full Corners*, Journal of the London Mathematical Society **61** (2000), 893–904, DOI `10.1112/S0024610799008492`. Twisted spectral-triple constructions related to Bost–Connes are also established, for example Greenfield–Marcolli–Teh, *Twisted Spectral Triples and Quantum Statistical Mechanical Systems*, P-Adic Numbers, Ultrametric Analysis, and Applications **6** (2014), 81–104, DOI `10.1134/S2070046614020010`.

Those sources define a much broader operator-algebraic landscape than the narrow calculation here. The weighted-partial-isometry mechanism behind `(4)`–`(19)` is standard elementary operator theory once the coefficient sequence is fixed. A targeted search for Bost–Connes semigroup commutators, Möbius diagonals, prime-phase controls, and cross-prime partial-isometry Gram relations did not locate this exact specialization. No novelty inference is drawn from that absence: the theorem is an elementary consequence of the represented semigroup action plus square-free multiplicativity, so it is recorded with **no novelty claim**.

## Boundaries and falsification tests

- **Quadratic Gram layer only.** The exact theorem covers `C_p^*C_q`, the partial-isometry system it generates through those pairwise edges, and closed Gram paths. It does not classify arbitrary words containing an unmatched odd number of orientation-bearing commutators.
- **No global information-theory claim.** Square-free support together with the ambient prime labels can itself reconstruct `(-1)^{\omega(n)}`. The result therefore does not assert that a mathematician given the full support-labelled representation can never recover Möbius. It says the Gram coefficient and its cycle phase supply no new intrinsic cross-prime orientation beyond separable local data and support transport.
- **Matched phase controls are diagnostic, not alternative arithmetic universes.** The family `(1)` tests whether a proposed relation uses a genuinely joint phase mechanism. It is not assumed to satisfy every arithmetic theorem available for Möbius.
- **Local phase sensitivity is not denied.** Equation `(4)` changes when a single `z_p` changes. The obstruction is that this sensitivity factorizes as `a_p\overline{a_q}` and has trivial closed-cycle phase; it is not a relational cancellation law.
- **KMS conclusions require a separate theorem.** No claim is made here about all KMS expectations of arbitrary off-diagonal words, especially in regimes where the number-state Gibbs representation is not normal. A proposed KMS statistic must be computed in its legitimate state/representation.
- **Twisted or mixed observables remain open.** A twist can alter the coefficient law before the adjoint product, and a coefficient-algebra insertion between semigroup commutators can prevent the simple factorization. Such a candidate must be derived separately and tested for target re-encoding.
- **No Mertens estimate follows.** The result is a representation-level obstruction. It neither bounds `M(x)` nor supplies a new RH criterion.

## Consequence for the line

The Bost–Connes residual frontier is narrower. Merely leaving the diagonal algebra and forming the natural pairwise Gram/covariance operators does not produce the missing cross-prime Möbius phase: after exact calculation, the edge phase is separable and every closed Gram cycle has trivial holonomy.

Accordingly, further work should not treat `C_p^*C_q` coherence, its normalized prime-replacement graph, or closed products of those Gram edges as an unexplored phase carrier. A surviving relational mechanism must evade this factorization — for example through an orientation-bearing odd word, a genuinely twisted commutator, a nontrivial coefficient insertion, or another source-forced relation — and must still provide a quantitative transfer to anchored Mertens excursion that is cheaper than reconstructing the target itself.