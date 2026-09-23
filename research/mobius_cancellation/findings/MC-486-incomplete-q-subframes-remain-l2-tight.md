# MC-486 — Incomplete q-subframes remain coefficient-blind L2-tight

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-CORRELATION+DERIVED-APPLICATION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NON-RH`.

## Claim

`MC-485` proves that the complete inverse-shift family

\[
K_q(m)=\chi(m+hq^{-1})\overline{\chi(m)}
\]

has coefficient-side Gram matrix `pI-J-vv*`, and therefore no coefficient-blind `L^2` gain below the natural `sqrt(p)` operator scale. It left open a narrower possibility: perhaps restricting `q` to the actual incomplete source-prime set lowers that norm even before the moving first-exit sieve mask is used.

It does not. For every subset `Q\subset \mathbf F_p^*` of distinct residue classes, let

\[
A_Q=(K_q(m))_{q\in Q,\ m\in\mathbf F_p^*}
\]

and put

\[
u_q:=\chi(hq^{-1}).
\]

Then the **row-side Gram matrix** is exactly

\[
\boxed{
A_QA_Q^*=pI_Q-\mathbf1_Q\mathbf1_Q^*-u_Qu_Q^*.
}
\tag{1}
\]

Equivalently, for arbitrary complex weights `c_q`,

\[
\boxed{
\sum_{m\in\mathbf F_p^*}
\left|\sum_{q\in Q}c_qK_q(m)\right|^2
=
p\sum_{q\in Q}|c_q|^2
-\left|\sum_{q\in Q}c_q\right|^2
-\left|\sum_{q\in Q}c_q\chi(q)\right|^2.
}
\tag{2}
\]

The unit factor `\overline{\chi(h)}` disappears from the last absolute value. If `k=|Q|` and

\[
S_Q:=\sum_{q\in Q}u_q,
\]

then for `k\ge2` the two possibly non-`p` eigenvalues are

\[
p-k-|S_Q|,
\qquad
p-k+|S_Q|,
\tag{3}
\]

and every vector orthogonal to both `\mathbf1_Q` and `u_Q` has eigenvalue `p`. Hence for every `k\ge3`,

\[
\boxed{\|A_Q\|_{2\to2}=\sqrt p.}
\tag{4}
\]

So passing from the complete family to **any** incomplete set of at least three distinct `q` residues does not reduce the sharp uniform coefficient-blind `L^2` operator norm at all.

More strongly, by Cauchy-Schwarz,

\[
|S_Q|\le k,
\]

and `(3)` gives

\[
(p-2k)\|c\|_2^2
\le
\|A_Q^*c\|_2^2
\le
p\|c\|_2^2.
\tag{5}
\]

Thus when `k=o(p)` the incomplete row family is itself asymptotically `sqrt(p)`-tight in **every** source-weight direction, not merely in its top singular direction. For `k\le p/4`, for example,

\[
\frac p2\|c\|_2^2
\le
\|A_Q^*c\|_2^2
\le
p\|c\|_2^2.
\tag{6}
\]

For the unweighted source average `c_q=1`, `(2)` specializes to

\[
\boxed{
\sum_m\left|\sum_{q\in Q}K_q(m)\right|^2
=pk-k^2-\left|\sum_{q\in Q}\chi(q)\right|^2.
}
\tag{7}
\]

When `k=o(p)`, the right side is `pk(1+o(1))` uniformly in the arithmetic placement of `Q`, because the two subtracted terms are at most `2k^2`. Therefore sparsity of the actual source-prime set, or its mere incompleteness modulo `p`, cannot by itself create a conductor-power `L^2` saving in the frozen-mask architecture.

This closes the incomplete-`q` **coefficient-blind frame** escape left in `MC-485`. It does not control a special arithmetic coefficient vector against a particular incomplete set, and it still does not touch the actual `MC-484` family where the interval and pair-sieve coefficient profile depends on `q`. Any surviving gain must come from that coupled coefficient motion, or from a proved special alignment of the arithmetic coefficient vector with the restricted row space/kernel; it cannot come from a generic reduction of the inverse-shift frame norm caused by using only source primes.

## 1. Exact row Gram calculation

Take `q,r\in Q`. By definition,

\[
(A_QA_Q^*)_{q,r}
=
\sum_{m\in\mathbf F_p^*}
K_q(m)\overline{K_r(m)}.
\tag{8}
\]

Write

\[
\delta_q=hq^{-1},
\qquad
\delta_r=hr^{-1}.
\]

Because `m\ne0`, `|\chi(m)|=1`, so

\[
K_q(m)\overline{K_r(m)}
=
\chi(m+\delta_q)\overline{\chi(m+\delta_r)}.
\tag{9}
\]

If `q=r`, exactly one nonzero `m`, namely `m=-\delta_q`, makes the translated character vanish. Hence

\[
(A_QA_Q^*)_{q,q}=p-2.
\tag{10}
\]

If `q\ne r`, then `\delta_q\ne\delta_r`. The standard complete shifted-character correlation gives

\[
\sum_{m\in\mathbf F_p}
\chi(m+\delta_q)\overline{\chi(m+\delta_r)}=-1.
\tag{11}
\]

Removing the `m=0` term yields

\[
(A_QA_Q^*)_{q,r}
=
-1-\chi(\delta_q)\overline{\chi(\delta_r)}.
\tag{12}
\]

Equations `(10)`--`(12)` are exactly `(1)`.

The correlation `(11)` is the same classical Jacobi-sum/fractional-linear orthogonality already used in `MC-485`; the present step does not introduce a new character-sum theorem. The difference is that the Gram orientation is reversed and then restricted to an arbitrary source subset `Q`.

## 2. Dual frame identity and spectrum

Taking the quadratic form of `(1)` against `c=(c_q)_{q\in Q}` gives

\[
\|A_Q^*c\|_2^2
=
p\|c\|_2^2
-|\langle c,\mathbf1_Q\rangle|^2
-|\langle c,u_Q\rangle|^2.
\tag{13}
\]

Since

\[
\overline{u_q}
=
\overline{\chi(hq^{-1})}
=
\overline{\chi(h)}\chi(q),
\]

`(13)` is `(2)`.

The nonzero eigenvalues of

\[
\mathbf1_Q\mathbf1_Q^*+u_Qu_Q^*
\]

are

\[
k\pm|\langle\mathbf1_Q,u_Q\rangle|
=
k\pm|S_Q|.
\tag{14}
\]

Its orthogonal complement has dimension at least `k-2`. Subtracting from `pI_Q` proves `(3)` and the eigenvalue-`p` subspace. For `k\ge3` that subspace is nonzero, proving `(4)`.

This is stronger than completing an incomplete set to all `q` residues and applying the complete-family upper bound. Completion only gives `\|A_Q\|\le\sqrt p`; the row Gram proves equality for every `k\ge3` and quantifies the whole singular spectrum when `k` is sparse.

## 3. Consequence for incomplete source primes

Suppose the first-exit source primes occupy a set of `k` distinct residue classes modulo the conductor `p`, and suppose the `q`-dependent sieve/interval coefficients have been frozen to one common profile `b_m`. Any estimate based only on a uniform `L^2` bound for the phase matrix `A_Q` still faces the exact norm `sqrt(p)` from `(4)`. There is no hidden operator-norm improvement coming from the fact that `Q` consists of primes, is sparse, or omits most residues.

The unweighted identity `(7)` makes the sparse regime even more explicit. If `k=o(p)`, then

\[
pk-2k^2
\le
\sum_m\left|\sum_{q\in Q}K_q(m)\right|^2
\le
pk-k^2.
\tag{15}
\]

So an incomplete source set with sublinear residue support still carries essentially the full `pk` phase energy. A special character bias of the primes inside `Q` only changes the second low-rank subtraction; it cannot remove a fixed power of `p` while `k=o(p)`.

If different source primes repeat the same residue modulo `p`, then they generate the same frozen-mask phase row. Their coefficient-blind contribution therefore first aggregates by residue class, after which `(1)`--`(2)` apply to the aggregated weights. Repeated prime identities do not create additional phase directions; any usefulness of those identities must enter through coefficients that were discarded by the freezing step.

## 4. What remains live

This result removes only a generic incomplete-subset loophole. It does **not** prove that every particular common coefficient vector `b` gives a large incomplete-source sum. When `Q` is proper, `A_Q` has a large right kernel in coefficient space, and a special arithmetic `b` could lie partly or wholly near that kernel. Such alignment is an arithmetic statement about `b`, not a consequence of source-set incompleteness.

More importantly, the exact first-exit coefficients in `MC-484` are not common:

\[
b_{q,m}
=
\mathbf1_{m\in I_q}
\mathbf1_{(m(m+\delta_q),P(q))=1}
\]

up to the root branches and source weights. Both `I_q` and the pair-sieve mask move with the same `q` as the character phase. The matrices `(1)`--`(2)` cannot absorb that dependence into a fixed vector `b`.

The frontier is therefore sharper:

- **closed:** complete-family coefficient-blind `L^2` gain (`MC-485`);
- **closed:** incomplete-source coefficient-blind `L^2` norm reduction from subset sparsity alone (this finding);
- **live:** special alignment of the actual arithmetic coefficients with an incomplete row space/kernel;
- **live and primary:** a weighted Gram/dispersion estimate that keeps the first-exit pair-sieve mask and shortened source interval inside the `q,m` family.

A successful continuation must prove structure in one of the live bullets. Merely replacing the complete `q` family by actual source primes is no longer a distinct mechanism.

## 5. Prior art and novelty boundary

The shifted-character correlation `(11)` is classical Jacobi-sum orthogonality. Standard references include Bruce C. Berndt, Ronald J. Evans and Kenneth S. Williams, *Gauss and Jacobi Sums*, Wiley, 1998, ISBN `978-0-471-12807-6`; the line also records Cochrane--Pinner (`MC-S55`) for bounded-complexity complete multiplicative-character sums. No novelty is claimed for `(11)`, Jacobi sums, or elementary Gram-matrix linear algebra.

Targeted searches for shifted multiplicative-character correlations, Jacobi sums, character-sequence frames, and incomplete character families found the classical correlation machinery and broader incomplete/sparse character-sum literature, but no reason to present `(1)`--`(7)` as a new finite-field theorem. The Mathia-specific contribution is the exact **frontier audit**: applying the dual Gram identity to the incomplete first-exit source set and showing that the incomplete-prime loophole left by `MC-485` does not lower the coefficient-blind `L^2` scale.

This finding is therefore classified as an exact derived application of classical correlation plus linear algebra, not as a novelty claim.

## Boundaries

- `Q` is a set of distinct nonzero residue classes modulo `p`. Repeated source primes are handled only after aggregating their weights by residue.
- The hypothesis `h\not\equiv0\pmod p` and nonprincipality of `\chi` remain essential.
- `(4)` is a **uniform operator-norm statement**, not a lower bound for every particular arithmetic coefficient vector.
- `(5)` is useful as a lower singular-value estimate only when `p-2k>0`; positivity of the exact Gram matrix remains automatic outside that coarse range.
- No result here controls the `q`-dependent pair-sieve mask, endpoint geometry, source weights, or the final Möbius source frame.
- No conductor-power estimate for the actual first-exit bilinear family, no improved bound for `M(x)`, no zero-free region, and no RH consequence is obtained.