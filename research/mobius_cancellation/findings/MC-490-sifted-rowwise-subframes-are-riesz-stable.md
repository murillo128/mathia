# MC-490 — Sifted rowwise first-exit subframes are Riesz-stable below conductor density

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-CORRELATION+GERSHGORIN` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-489` showed that the first genuinely `q`-dependent coordinate change left by the exact Buchstab first-exit family — rowwise dilation `n=qm` — still carries a `p^{1/2-o(1)}` one-row diagonal after the moving hard pair-sieve mask is retained. That ruled out a coefficient-blind **upper operator-norm** gain, but it deliberately left open a narrower escape: perhaps the actual scalar outer weights could align with a small singular direction of the completed masked row family and cancel the large individual diagonals.

For any sublinear family of first-exit primes occupying distinct residues modulo the conductor, that escape is absent at the level of scalar row weights.

Let `p` be an odd prime, let `chi` be a nonprincipal character modulo `p`, fix `h not\equiv 0 (mod p)`, and for an active first-exit prime `q != p` use the root `q|n` and the row from `MC-489`,

\[
G_q(m)=K_h(qm)A_q(qm),
\qquad
K_h(x)=\chi(x+h)\overline{\chi(x)},
\qquad
A_q(x)=\mathbf 1_{(x(x+h),P(q))=1}.
\tag{1}
\]

Take a finite set `Q` of `k` active first-exit primes whose residues modulo `p` are pairwise distinct, let

\[
q_*:=\max Q,
\qquad
P_*:=P(q_*),
\tag{2}
\]

and regard every row on the common complete period `pP_*`. Write

\[
d_q:=\frac1{P(q)}\#\{b\bmod P(q):A_q(qb)=1\}
\tag{3}
\]

and, for distinct `q,r`, let `d_{q,r}` be the density on the larger sieve period of the simultaneous hard masks appearing in the complete cross term of `MC-489`. Then

\[
\boxed{
\langle G_q,G_q\rangle_{pP_*}
=(p-2)P_*d_q,
}
\tag{4}
\]

while for `q != r`,

\[
\boxed{
\langle G_q,G_r\rangle_{pP_*}
=P_*C_p(q,r)d_{q,r},
\qquad |C_p(q,r)|\le 2.
}
\tag{5}
\]

Because `d_{q,r}` is an intersection density,

\[
0\le d_{q,r}\le \min(d_q,d_r)\le \sqrt{d_qd_r}.
\tag{6}
\]

Normalize each nonempty row by

\[
H_q:=\frac{G_q}{\sqrt{(p-2)P_*d_q}}.
\tag{7}
\]

Its Gram matrix `\Gamma=(\langle H_q,H_r\rangle)_{q,r\in Q}` therefore satisfies

\[
\Gamma_{q,q}=1,
\qquad
|\Gamma_{q,r}|\le \frac{2}{p-2}\quad(q\ne r).
\tag{8}
\]

Geršgorin's theorem gives the exact uniform spectral enclosure

\[
\boxed{
1-\frac{2(k-1)}{p-2}
\le
\lambda(\Gamma)
\le
1+\frac{2(k-1)}{p-2}.
}
\tag{9}
\]

Hence whenever `2(k-1)<p-2`, every scalar coefficient vector `a=(a_q)` obeys

\[
\boxed{
\left(1-\frac{2(k-1)}{p-2}\right)\sum_q|a_q|^2
\le
\left\|\sum_q a_qH_q\right\|_2^2
\le
\left(1+\frac{2(k-1)}{p-2}\right)\sum_q|a_q|^2.
}
\tag{10}
\]

In particular, if `k=o(p)`, the **exact moving-hard-mask rows are asymptotically orthonormal in every scalar row-weight direction**. There is no hidden small singular subspace analogous to the loophole that remained after the one-column lower bound in `MC-489`. For `k<=p/4`, the lower factor in `(10)` is at least `1/2`.

Undoing the normalization yields

\[
\boxed{
\left\|\sum_{q\in Q}c_qG_q\right\|_2^2
\ge
\left(1-\frac{2(k-1)}{p-2}\right)
(p-2)P_*\sum_{q\in Q}|c_q|^2d_q.
}
\tag{11}
\]

For polynomial first-exit ranges `q<=p^A`, `MC-489` gives `d_q\gg_A(\log p)^{-2}` for every nonempty row. Thus a scalar-weighted complete-period combination of `k=o(p)` distinct-residue rows cannot obtain a fixed conductor-power saving by arranging the outer `q` weights into a favorable singular direction. The completed hard masks themselves are too incoherent: their normalized mutual coherence is only `O(1/p)`.

This is strictly stronger than the coefficient-blind operator-norm obstruction in `MC-489` and different from the bare-phase result `MC-486`. `MC-486` proves near-isometry for incomplete subsets after the `q`-dependent masks are frozen to a common coefficient profile; `(9)`--`(11)` retain the **actual nested hard sieve mask of every row after rowwise dilation**.

The result does not close the accepted clue. It rules out only scalar outer-weight alignment inside this complete-period row model. A live continuation must still alter the arithmetic kernel before positive closure, exploit `m`-dependent `q`-specific source coefficients/endpoints, use repeated conductor-residue blocks nontrivially, or prove a signed incomplete-interval/off-diagonal theorem not reducible to the complete-period Hilbert norm.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Common-period diagonal and cross terms

For a single row, `MC-489` proves on its native period `pP(q)` that

\[
\sum_{m\bmod pP(q)}|G_q(m)|^2=(p-2)P(q)d_q.
\tag{12}
\]

Since `P(q)|P_*`, replication to the common period `pP_*` multiplies `(12)` by `P_*/P(q)`, giving `(4)`.

For distinct `q<r`, `MC-489` proves on `pP(r)` that

\[
\sum_{m\bmod pP(r)}G_q(m)\overline{G_r(m)}
=C_p(q,r)P(r)d_{q,r}.
\tag{13}
\]

The same replication gives `(5)`. Pairwise distinct residues modulo `p` put every pair in the small branch of the character correlation,

\[
C_p(q,r)=-1-\chi(hq^{-1})\overline{\chi(hr^{-1})},
\tag{14}
\]

so `|C_p(q,r)|<=2`.

The density inequality `(6)` is purely set-theoretic. On the common sieve period, the simultaneous survivor set is contained in each one-row survivor set. Therefore `d_{q,r}<=d_q` and `d_{q,r}<=d_r`, and the geometric-mean bound follows.

Substituting `(4)`--`(6)` into `(7)` gives `(8)` without any probabilistic independence or heuristic about the sieve masks.

## 2. Geršgorin closes the scalar favorable-subspace loophole

The normalized Gram matrix is Hermitian with unit diagonal. Every row has total off-diagonal absolute mass at most

\[
\frac{2(k-1)}{p-2}.
\tag{15}
\]

Geršgorin's eigenvalue-inclusion theorem therefore puts every eigenvalue in the real interval `(9)`. Taking the quadratic form against `a` gives `(10)`.

The point is not the upper bound: `MC-489` already showed that a one-row test forces the top norm to retain the conductor scale. The new information is the **lower** bound. When `k=o(p)`, no scalar vector of outer row weights can make the completed masked family anomalously small in `L^2`; all singular values of the normalized family are `1+o(1)`.

For unnormalized weights set

\[
a_q=c_q\sqrt{(p-2)P_*d_q}.
\tag{16}
\]

Equation `(10)` immediately becomes `(11)`.

Thus the exact hard sieve masks do not rescue a scalar favorable-direction mechanism. They make different rows *less*, not more, coherent at the complete-period level: the intersection density can only reduce the already `O(1)` off-diagonal character correlation relative to the `p`-scale diagonal.

## 3. What this removes from the live first-exit clue

`MC-489` ended with two coefficient-sensitive possibilities. One was a genuinely arithmetic signed off-diagonal operation before positive closure. The other was the possibility that the actual first-exit coefficient vector happened to lie near a small singular direction of the completed row family.

The present result removes the second possibility **when the coefficient dependence on a row is scalar** and the active residue support is sublinear in `p`. Any such weights — including highly nonuniform or signed `c_q` — are controlled from below by `(11)`.

This is the natural exact hard-mask analogue of the bare-phase near-isometry in `MC-486`, but its proof uses the full first-exit sieve overlap from `MC-489`. The accepted clue should therefore no longer treat generic scalar least-prime weights as sufficient evidence of a favorable subspace in this completed architecture.

What remains potentially load-bearing is more structured than a vector `c_q`:

- an `m`-dependent coefficient `c_q(m)` tied to exact source endpoints or earlier factorization data;
- a transform where `q` enters a different modulus, reciprocal phase, or arithmetic kernel before the Hilbert norm is taken;
- repeated residue classes `q\equiv r (mod p)`, where the character correlation has the large `p-2` branch and must be aggregated with their different sieve cutoffs rather than treated by `(8)`;
- genuinely incomplete source intervals, where complete-period replication and the positive `L^2` closure used here may be too lossy;
- cross-component signed interference retained before the empty-vector base is isolated.

Those mechanisms are outside `(9)`--`(11)` and must be analyzed from their exact arithmetic formulas.

## 4. Prior art and novelty boundary

The eigenvalue step is classical Geršgorin theory. A standard monograph reference is Richard S. Varga, *Geršgorin and His Circles*, Springer Series in Computational Mathematics 36, Springer, 2004, DOI `10.1007/978-3-642-17798-9`. No novelty is claimed for diagonal dominance, Gram-matrix conditioning, mutual-coherence bounds, or the resulting Riesz-sequence interpretation.

The character correlation and exact sieve-overlap factorization are already audited locally in `MC-485`--`MC-489`; no new finite-field or sieve theorem is claimed. A targeted prior-art search for sifted multiplicative-character frames and Gram/coherence formulations found the standard character-sum and frame/diagonal-dominance machinery but no reason to treat the abstract eigenvalue argument as novel.

The durable Mathia delta is the **frontier application**: once the rowwise `q`-dependent dilation is combined with its exact nested first-exit hard mask, the pairwise complete-period correlations are still small enough to make every sublinear distinct-residue row family uniformly well conditioned. This closes a specific favorable-singular-direction escape left explicitly open by `MC-489`.

## Boundaries and falsification tests

- **Scalar row coefficients only.** Equation `(10)` controls combinations `sum_q c_qG_q`. Coefficients varying with the inner coordinate `m` can change the Gram structure and are not covered.
- **Complete-period statement.** The proof uses exact completion to the common period `pP_*`. It does not give a lower singular-value bound for a short source interval.
- **Distinct conductor residues.** If `q\equiv r (mod p)`, then `C_p(q,r)=p-2`; `(8)` fails. Repeated residues must be grouped and priced with their actual different sieve cutoffs and source coefficients.
- **Sublinear-cardinality gain.** The useful lower bound requires `2(k-1)<p-2`; the asymptotic near-isometry statement assumes `k=o(p)`. No claim is made for a dense set of nearly `p` distinct residue classes.
- **One root branch at a time.** The displayed rows use `q|n`. The `q|n+h` branch satisfies the translated analogue. A tagged direct-sum treatment inherits the same estimate, but an analytic step that superposes the two branches before closure can create additional interference and must be checked separately.
- **Nonempty rows.** Rows killed by a local parity obstruction are removed exactly. The normalization `(7)` is used only when `d_q>0`.
- **No lower bound for the original scalar first-exit sum.** A complete-period `L^2` lower frame bound is a proof-architecture obstruction, not a statement that the final one-dimensional Möbius-related sum is large.
- **No circular zeta input.** The proof uses only the exact first-exit identities, classical complete character correlation, sieve-set inclusion, and elementary matrix spectral localization.

## Consequence for the research line

The normalized empty-vector first-exit branch has now lost another generic escape. Common transforms are blocked by the disjoint partition (`MC-488`); rowwise dilation retains the conductor-scale diagonal (`MC-489`); and the present finding shows that, after retaining the exact moving hard masks, a sublinear distinct-residue row family has no scalar small-singular direction either.

The next useful step must therefore introduce **inner-coordinate-dependent arithmetic asymmetry before positive closure**, or leave the complete-period Hilbert-space architecture altogether. Reweighting the completed first-exit rows by a clever scalar function of the least prime `q` is not enough in the regime `(9)`.