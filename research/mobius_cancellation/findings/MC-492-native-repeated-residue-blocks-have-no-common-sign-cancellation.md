# MC-492 — Native repeated-residue blocks have no common-sign cancellation

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-JACOBI-SUM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-491` leaves dense repeated conductor-residue blocks open because pairwise coherence alone no longer controls the smallest singular value once the family size reaches the logarithmic threshold. For the **native Buchstab first-exit coefficient**, however, the most direct dense-block escape is already impossible for a simpler reason that does not use Geršgorin and does not require completion.

Fix an odd prime conductor `p`, a nonprincipal character `chi (mod p)`, and `h not congruent 0 (mod p)`. On the root `q|n`, write `n=qm` and let

\[
K_q^+(m)=\chi(qm+h)\overline{\chi(qm)}.
\tag{1}
\]

Allow any nonnegative row amplitude `B_q^+(m)>=0`; it may include the exact first-exit hard mask, the exact truncated source interval, and any other common-sign real cutoff retained before positive closure. Put

\[
G_q^+(m)=K_q^+(m)B_q^+(m).
\tag{2}
\]

If two first-exit primes satisfy

\[
q\equiv r\pmod p,
\tag{3}
\]

then their character phases are **identical pointwise** in the common `m` coordinate:

\[
K_q^+(m)=K_r^+(m).
\tag{4}
\]

Consequently

\[
\boxed{
\langle G_q^+,G_r^+\rangle
=\sum_m |K_q^+(m)|^2 B_q^+(m)B_r^+(m)\ge0.
}
\tag{5}
\]

This is valid on arbitrary finite or infinite common `m` domains whenever the displayed sums converge; no complete-period factorization is needed. Therefore for any finite repeated-residue block `Q_a={q:q congruent a (mod p)}` and coefficients with a common complex argument, `c_q=e^{i theta}b_q`, `b_q>=0`,

\[
\boxed{
\left\|\sum_{q\in Q_a}c_qG_q^+\right\|_2^2
\ge
\sum_{q\in Q_a}|c_q|^2\|G_q^+\|_2^2.
}
\tag{6}
\]

The same statement holds on the other root. If `q|n+h`, write `n=qm-h` and

\[
K_q^-(m)=\chi(qm)\overline{\chi(qm-h)}.
\tag{7}
\]

Again `q congruent r (mod p)` implies `K_q^-=K_r^-`, so the same-root Gram entries are nonnegative on exact incomplete intervals as well as complete periods.

The canonical Buchstab identity in `MC-484` gives every first-exit prime the same outer coefficient `-1`. Hence a dense repeated-residue block **within either root branch cannot itself be a cancellation mechanism for the native first-exit sum**. Its same-root cross terms are constructive, not destructive. A small singular direction of the completed repeated-residue Gram matrix, even if one exists for some sign-changing scalar vector, is irrelevant to the actual common-sign Buchstab coefficient unless another arithmetic step first creates the required q-dependent signs or phases.

There is one remaining native way for root superposition to alter this conclusion: interference between the two different root branches. On a complete conductor period that interaction is only Jacobi-sum scale, not conductor scale. For `q congruent r (mod p)` define

\[
C_p^{+-}
:=\sum_{m\bmod p}K_q^+(m)\overline{K_r^-(m)}.
\tag{8}
\]

The residue condition makes `(8)` independent of the particular `q,r` in the class. A direct change of variables gives the exact identity

\[
\boxed{
C_p^{+-}=\chi(4)J(\chi,\chi)-1,
}
\tag{9}
\]

where

\[
J(\chi,\chi)=\sum_{v\bmod p}\chi(v)\chi(1-v)
\tag{10}
\]

is the classical Jacobi sum. If `chi^2` is nonprincipal, then `|J(chi,chi)|=sqrt(p)`; if `chi` is quadratic, `J(chi,chi)=-chi(-1)`. Thus

\[
\boxed{
|C_p^{+-}|\le \sqrt p+1,
}
\tag{11}
\]

and in the quadratic case `|C_p^{+-}|<=2` (indeed it is `0` or `2`).

On a complete joint period, CRT separates the conductor variable from the exact sieve masks. If `d_{q,r}^{+-}` denotes the simultaneous normalized sieve density of the two opposite-root rows, then

\[
\langle G_q^+,G_r^-\rangle
=C_p^{+-}P_*d_{q,r}^{+-},
\tag{12}
\]

while each one-root diagonal is `(p-2)P_*d_q^+` or `(p-2)P_*d_r^-`. Since an intersection density is at most the geometric mean of the one-row densities,

\[
\boxed{
\frac{|\langle G_q^+,G_r^-\rangle|}
{\|G_q^+\|_2\|G_r^-\|_2}
\le
\frac{\sqrt p+1}{p-2}
=O(p^{-1/2}).
}
\tag{13}
\]

For quadratic `chi`, the right side improves to `O(p^{-1})`.

Thus the large `p-2` repeated-residue correlation is a **same-root phenomenon only**. Same-root native coefficients have the wrong sign for cancellation, while root-switching has at most square-root conductor correlation pairwise on complete periods. Dense repeated residues therefore do not supply an automatic scalar cancellation resource. A surviving route must either create genuinely sign-changing/q-dependent coefficients before the same-root positive Gram is closed, exploit a collective cross-root effect whose accumulation overcomes the Jacobi-scale pair tariff with all exact source costs restored, or leave this rowwise Hilbert architecture.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Pointwise phase locking proves the common-sign obstruction

For `q congruent r (mod p)`, the two integers `qm` and `rm` are congruent modulo `p` for every `m`. The same is true after adding `h`. Dirichlet-character periodicity therefore gives `(4)` immediately, including the zero values at the two exceptional conductor residues.

Multiplying `(4)` by nonnegative amplitudes proves `(5)`. Expanding the norm of a common-phase coefficient combination gives

\[
\left\|\sum_q c_qG_q^+\right\|_2^2
=
\sum_q |c_q|^2\|G_q^+\|_2^2
+2\sum_{q<r}b_qb_r\langle G_q^+,G_r^+\rangle,
\tag{14}
\]

because `c_q overline(c_r)=b_qb_r>=0`. Every cross term in `(14)` is nonnegative by `(5)`, proving `(6)`.

Nothing in this argument uses periodic completion, Mertens products, or a pairwise-coherence estimate. In particular, the incomplete exact endpoints that remained outside `MC-490`--`MC-491` do not change the sign statement as long as they enter as ordinary nonnegative support/amplitude factors. The obstruction fails only when the inner source coefficient itself carries a q-dependent sign/phase or when the two different root branches are superposed.

For the exact `R=T=1` first-exit identity, `MC-484` has precisely the common coefficient pattern covered by `(6)`: each `T_q` is subtracted once. Therefore an argument that invokes a dense repeated residue class solely because its completed Gram matrix may have a small eigenvalue has not yet connected that eigenvector to the arithmetic coefficient actually present in the source decomposition.

## 2. Opposite-root correlation is an exact Jacobi sum

Let `a` denote the common nonzero residue of `q,r` modulo `p`. Then

\[
K_q^+(m)=\chi(am+h)\overline{\chi(am)},
\qquad
K_r^-(m)=\chi(am)\overline{\chi(am-h)}.
\tag{15}
\]

Hence

\[
K_q^+(m)\overline{K_r^-(m)}
=
\chi(am+h)\chi(am-h)\overline{\chi(am)}^2.
\tag{16}
\]

Set `t=am h^{-1}` in `F_p`. The terms at `t=0,+/-1` are handled automatically by the extension `chi(0)=0`. On `t!=0`, inversion `u=t^{-1}` gives

\[
C_p^{+-}
=
\sum_{u\in\mathbf F_p^*}\chi(1-u^2).
\tag{17}
\]

Adding the missing `u=0` term and then setting `u=1-2v`,

\[
\sum_{u\in\mathbf F_p}\chi(1-u^2)
=
\chi(4)\sum_{v\in\mathbf F_p}\chi(v)\chi(1-v)
=
\chi(4)J(\chi,\chi).
\tag{18}
\]

The added `u=0` term equals one, proving `(9)`.

The classical Gauss/Jacobi relation gives `|J(alpha,beta)|=sqrt(p)` when `alpha`, `beta`, and `alpha beta` are nonprincipal. Taking `alpha=beta=chi` proves `(11)` when `chi^2` is nonprincipal. In the quadratic case the exceptional Jacobi identity `J(chi,chi)=-chi(-1)` gives the stated `O(1)` value instead.

Equation `(12)` is then the same CRT factorization used in `MC-489`: the character factor depends only on `m mod p`, the two exact sieve masks depend only on the coprime sieve modulus, and replication to a common period separates the two counts. The density inequality used in `(13)` is purely set-theoretic.

## 3. What remains of the dense repeated-residue branch

`MC-491` correctly leaves open the spectral question for a large repeated-residue Gram block: logarithmically small pair coherence does not preclude a small eigenvalue at large cardinality. The present result does not claim such eigenvalues are absent. It shows instead that **the native Buchstab vector is not free to choose one**.

For one root branch, the actual coefficient vector lies in the common-sign cone on which the repeated-residue Gram quadratic form is bounded below by its diagonal, regardless of block size. Thus a future small-eigenvalue construction matters only if the exact source algebra supplies a sign-changing projection onto it with reconstruction cost below the desired conductor gain.

The other native possibility is to superpose the two root branches before closure. Pairwise, their complete conductor interaction is at most `sqrt(p)+1`, compared with the `p-2` same-root conductor scale. This does not by itself rule out a very large collective cross-root block: `k^2` Jacobi-scale terms can accumulate when the family is dense. But it identifies the correct next test. One must prove an aggregate signed cross-root estimate or an actual coefficient-generation mechanism; the bare fact `q congruent r (mod p)` no longer supplies a conductor-scale negative pair interaction.

## 4. Prior art and novelty boundary

The phase-locking argument is elementary Hilbert-space algebra applied to periodic Dirichlet characters. No novelty is claimed for positivity of Gram matrices of same-phase nonnegative amplitudes.

Jacobi sums, the identity relating them to Gauss sums, the magnitude `sqrt(p)` in the nondegenerate case, and the quadratic exceptional formula are classical. A standard monograph source is Bruce C. Berndt, Ronald J. Evans and Kenneth S. Williams, *Gauss and Jacobi Sums*, Wiley, 1998. The same square-root character-sum scale is consistent with the more general rational-character Weil bounds already anchored by `MC-S55`.

The durable Mathia delta is the **frontier classification** inside the exact `MC-484` source frame. The dense repeated-residue loophole from `MC-491` cannot be justified merely by the existence of many conductor collisions: within each root, the native coefficients force constructive interference at arbitrary cardinality, while switching roots replaces the `p`-scale collision by a classical Jacobi-sum correlation of size at most `sqrt(p)+1`.

## Boundaries and falsification tests

- **Common-sign coefficient cone.** The exact lower bound `(6)` applies when the row coefficients share one complex argument and the inner amplitudes are nonnegative. A genuinely q-dependent signed/complex source coefficient lies outside the theorem.
- **Same-root positivity is incomplete-interval robust.** No completion is used in `(5)`--`(6)`. Exact interval endpoints do not rescue same-root native cancellation by themselves.
- **Cross-root Jacobi bound uses complete conductor averaging.** Equations `(9)`--`(13)` do not give the same bound on an arbitrary sharply truncated `m` interval; an incomplete signed transform remains live.
- **Dense cross-root accumulation remains open.** Pairwise `O(p^{-1/2})` normalized coherence does not by itself control a block with cardinality of order `sqrt(p)` or larger.
- **Hard masks retained.** The positive amplitudes may include the exact hard masks. The complete-period cross-root density in `(12)` is not replaced by an envelope.
- **One conductor residue at a time.** The result targets the repeated-residue branch left by `MC-491`; distinct-residue rows remain governed by `MC-490` and its successors.
- **No global arithmetic conclusion.** This is a proof-architecture obstruction for the normalized first-exit family, not a Möbius summatory estimate.

## Consequence for the accepted clue

A dense repeated-residue block should no longer be listed as a generic favorable scalar direction. With the actual Buchstab coefficient, every same-root repeated-residue block has constructive cross terms even on incomplete exact intervals. The only residual dense-collision mechanisms are therefore more specific: a derived q-dependent sign/phase in the inner source coefficient, a collective **cross-root** signed effect beyond the Jacobi pair scale, or a genuinely incomplete transform that changes the arithmetic kernel before positive closure.

Any continuation that invokes conductor collisions must now exhibit the first exact formula creating one of those resources and charge its reconstruction cost. Merely increasing the number of primes in one residue class modulo `p` does not evade the first-exit tariff.