# MC-494 — Complete repeated-residue blocks tensorize before root interference

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-CRT+JACOBI` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-493` bounds a native complete-period repeated-residue cross-root block by summing the pairwise Jacobi-scale correlations from `MC-492`. That argument leaves a square-root-conductor effective-multiplicity threshold because it treats the `k_+k_-` opposite-root pairs independently. For the exact repeated-residue source frame, this is not sharp: **the entire block tensorizes before the two roots interact.**

Fix an odd prime conductor `p`, a nonprincipal character `chi (mod p)`, a nonzero shift `h (mod p)`, and one nonzero conductor residue `a (mod p)`. Let `Q_+` and `Q_-` be finite families of active first-exit primes, all congruent to `a (mod p)`. Lift every exact completed row to one common joint period `pM`, where `M` is a common auxiliary/sieve period and `(p,M)=1`. Positive row normalizations may be absorbed into the amplitudes below.

On the two roots write

\[
G_q^+(m)=K^+(m)B_q^+(m),
\qquad
G_r^-(m)=K^-(m)B_r^-(m),
\tag{1}
\]

where

\[
K^+(m)=\chi(am+h)\overline{\chi(am)},
\qquad
K^-(m)=\chi(am)\overline{\chi(am-h)}.
\tag{2}
\]

The repeated-residue condition is what removes `q` and `r` from the conductor phases. Each exact completed hard-mask amplitude `B_q^+`, `B_r^-` is nonnegative and depends only on the auxiliary coordinate modulo `M`. Define

\[
A(m)=\sum_{q\in Q_+}B_q^+(m),
\qquad
B(m)=\sum_{r\in Q_-}B_r^-(m),
\tag{3}
\]

and the native common-sign block sums

\[
U=\sum_{q\in Q_+}G_q^+=K^+A,
\qquad
V=\sum_{r\in Q_-}G_r^-=K^-B.
\tag{4}
\]

Thus row multiplicity is already absorbed into two nonnegative auxiliary amplitudes before conductor averaging.

CRT now gives the exact aggregate identities

\[
\|U\|_2^2=(p-2)\|A\|_{2,M}^2,
\qquad
\|V\|_2^2=(p-2)\|B\|_{2,M}^2,
\tag{5}
\]

and

\[
\langle U,V\rangle
=C_p^{+-}\,\langle A,B\rangle_M,
\qquad
C_p^{+-}=\chi(4)J(\chi,\chi)-1,
\tag{6}
\]

with the same classical Jacobi sum as in `MC-492`. Put

\[
X=\|A\|_{2,M}^2,
\qquad
Y=\|B\|_{2,M}^2,
\qquad
Z=\langle A,B\rangle_M.
\tag{7}
\]

Because `A,B>=0`, one has `Z>=0`, and Cauchy plus `2sqrt(XY)<=X+Y` gives

\[
0\le 2Z\le X+Y.
\tag{8}
\]

Therefore

\[
\|U+V\|_2^2
=(p-2)(X+Y)+2\operatorname{Re}(C_p^{+-})Z
\tag{9}
\]

and hence

\[
\boxed{
\|U+V\|_2^2
\ge
\left(1-\frac{|C_p^{+-}|}{p-2}\right)
\left(\|U\|_2^2+\|V\|_2^2\right).
}
\tag{10}
\]

If `chi^2` is nonprincipal, the classical Jacobi estimate gives

\[
|C_p^{+-}|\le \sqrt p+1,
\tag{11}
\]

so

\[
\boxed{
\|U+V\|_2^2
\ge
\left(1-O(p^{-1/2})\right)
\left(\|U\|_2^2+\|V\|_2^2\right),
}
\tag{12}
\]

**uniformly in the number of rows and their effective participation.**

For quadratic `chi`,

\[
C_p^{+-}=-\chi(-1)-1.
\tag{13}
\]

Thus `C_p^{+-}=0` when `p congruent 3 (mod 4)`, giving exact complete-period cross-root orthogonality, while `C_p^{+-}=-2` when `p congruent 1 (mod 4)`, giving

\[
\|U+V\|_2^2
\ge
\frac{p-4}{p-2}
\left(\|U\|_2^2+\|V\|_2^2\right).
\tag{14}
\]

Consequently the square-root multiplicity threshold in `MC-493` is a valid but nonsharp consequence of pairwise summation. **For the native common-sign complete-period repeated-residue block, there is no density threshold at which cross-root accumulation can produce an order-one cancellation.** Arbitrarily many rows still leave the total two-root energy within `1-O(p^{-1/2})` of the sum of the separate root energies.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Why multiplicity disappears before the Jacobi sum

For every `q congruent a (mod p)`, periodicity of `chi` makes the plus-root conductor phase exactly the same function `K^+`; likewise every minus-root row shares `K^-`. The q-dependence of an exact completed first-exit row therefore lives entirely in its auxiliary hard mask and any positive scalar normalization.

A finite family of such auxiliary masks has a common period `M` coprime to `p`. After lifting to `pM`, CRT identifies the conductor coordinate and auxiliary coordinate independently. Summing rows first gives `(4)`; there is no need to estimate the `k_+k_-` pairs separately.

On the conductor factor, both `|K^+|^2` and `|K^-|^2` have total mass `p-2`, proving `(5)`. The mixed conductor factor is exactly

\[
\sum_{u\bmod p}K^+(u)\overline{K^-(u)}=C_p^{+-},
\tag{15}
\]

while the auxiliary factor is `sum_{v mod M} A(v)B(v)=Z`. This proves `(6)` and `(9)` directly.

The important distinction from `MC-493` is structural rather than numerical. Pairwise coherence treats each opposite-root pair as if its auxiliary overlap could align independently. Exact source geometry forbids that freedom: all pairs share one of only two conductor vectors, and all multiplicity is confined to the nonnegative auxiliary amplitudes `A` and `B`.

## 2. The complete-period collective loophole is closed at arbitrary density

`MC-492` showed that same-root repeated-residue cross terms are constructive for the native Buchstab coefficient. `MC-493` then asked whether many opposite-root Jacobi-scale terms could accumulate destructively. Equation `(10)` answers that question for completed exact rows: they cannot.

There is no dependence on `|Q_+|`, `|Q_-|`, the participation numbers from `MC-493`, or a source cutoff such as `Q<=p^(3/2-epsilon)`. The bound holds for every finite completed repeated-residue family for which the common auxiliary period is formed.

The only possible negative contribution is the single scalar `Re(C_p^{+-})` multiplying the nonnegative overlap `Z`. Its size is at most square-root conductor in the nondegenerate character case, whereas each branch carries conductor mass `p-2`. Increasing the number of source rows changes `A`, `B`, and `Z`, but cannot change that conductor ratio.

Thus the native complete-period route is more rigid than a generic low-coherence frame. The relevant completed subspace in the conductor variable has rank at most two, with a fixed `2x2` conductor Gram matrix. The auxiliary sieve geometry only supplies nonnegative amplitudes to those two conductor directions.

## 3. What remains genuinely live

The theorem uses three load-bearing properties: complete conductor averaging, one repeated conductor residue, and the native common-sign/nonnegative amplitude structure. A future mechanism must break at least one of them before positive closure.

A **source-derived q-dependent sign or complex phase** can prevent the collapse to nonnegative `A` and `B`. A **genuinely incomplete signed transform** can prevent the CRT conductor factor from reducing to the complete Jacobi scalar. A more radical factor-specific dispersion operation may also mix the first-exit label into a different arithmetic slot before completion, rather than merely summing completed repeated-residue rows.

What is no longer live is bare complete-period cross-root multiplicity. Reaching `sqrt(p)` rows, `p` rows, or any larger finite multiplicity does not by itself create a favorable native scalar direction.

## 4. Prior art and novelty boundary

The mathematical ingredients are classical. CRT tensorization of functions whose periods are coprime is elementary. Jacobi sums, the relation to Gauss sums, the `sqrt(p)` magnitude in the nondegenerate case, and the quadratic exceptional identity are standard; a monograph reference is Bruce C. Berndt, Ronald J. Evans and Kenneth S. Williams, *Gauss and Jacobi Sums*, Wiley-Interscience, 1998, ISBN 978-0-471-12807-6.

No novelty is claimed for CRT factorization, the Jacobi-sum identities, Cauchy--Schwarz, or the resulting abstract `2x2` Gram estimate. The durable Mathia delta is the **frontier closure inside the exact Buchstab first-exit source frame**: once repeated-residue completed rows are summed in their native common-sign form, the supposedly dangerous `k_+k_-` Jacobi interactions are not independent degrees of freedom at all.

## Boundaries and falsification tests

- **Complete joint periods.** Equations `(5)`--`(10)` use exact completion to a common period `pM`. A sharply truncated or otherwise incomplete signed transform is outside the theorem.
- **One conductor residue class.** The factorization targets the dense repeated-residue branch. Distinct conductor residues have different conductor vectors and are governed by `MC-490`--`MC-491`.
- **Native common-sign amplitudes.** The row amplitudes entering `A` and `B` are nonnegative after absorbing positive normalizations. A q-dependent sign or complex phase before aggregation can invalidate `Z>=0` and the two-amplitude reduction.
- **Exact hard masks retained.** Different first-exit masks may be arbitrarily complicated; they are lifted exactly into the common auxiliary period. No positive envelope replaces them.
- **Finite families.** The statement is for finite source blocks so a common auxiliary period exists. An infinite limiting argument requires its own topology and convergence control.
- **No inference from pairwise independence.** The proof uses the opposite fact: all repeated-residue rows share the same two conductor directions. Generic frame-coherence intuition is not evidence here.
- **No global arithmetic conclusion.** This closes one completed proof architecture only; it is not a Mertens-function estimate.

## Consequence for the accepted clue

The accepted first-exit clue should now remove **collective complete-period cross-root accumulation** from its live-resource list. `MC-493`'s square-root-multiplicity admission threshold is superseded at the frontier by the exact aggregate factorization here: native completed repeated-residue blocks remain stable at arbitrary finite multiplicity.

The surviving target is narrower. A useful continuation must exhibit the first exact source formula that creates q-dependent signed/complex inner coefficients, a genuinely incomplete transform whose conductor variable does not average to the Jacobi scalar, or another factor-specific operation that mixes the first-exit label into the oscillatory kernel before this two-direction tensorization occurs.