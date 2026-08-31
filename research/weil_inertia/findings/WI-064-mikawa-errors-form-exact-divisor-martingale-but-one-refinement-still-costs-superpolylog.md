# WI-064 — Mikawa pair errors form an exact divisor martingale, but one common refinement still costs super-polylogarithmically

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate or change Mathia's current unconditional simple-critical proportion. It identifies genuine cross-conductor structure that is absent from the diagonal Hilbert interface of WI-062--WI-063, then closes the most direct way of exploiting it. After extending Mikawa's pair error to all residue classes exactly as in WI-061, the normalized errors over nested odd squarefree moduli are a literal conditional-expectation martingale on the divisor lattice. Equivalently, additive Fourier coefficients of reduced denominator `d` are the same coefficient at every multiple of `d`, and all exact conductors dividing one common refinement modulus are orthogonal Fourier coordinates of one residue-class error vector.

This is real information beyond the diagonal caps used in WI-062. If all retained conductors divide a common modulus `Q`, one can assemble them by one Parseval/Cauchy step with coefficient `sum_{d|Q} B_d`, rather than the sharp norm-only cost `sum_d d B_d`. However, feeding the resulting fine-modulus residue norm into Mikawa's theorem pays an unavoidable extra factor `Q`, because Mikawa controls a residue **maximum**, not the residue-summed fine-modulus variance. WI-059 then implies that any single common refinement capturing `1-o(1)` of the `W`-local Fourier energy has `Q` larger than every fixed power of `log X`. Hence Mikawa's arbitrary but fixed logarithmic saving cannot close a lossless **one-common-refinement** repair.

The surviving positive target is therefore more specific than “find cross-conductor orthogonality”: the orthogonality already exists. What is missing is an arithmetic estimate that exploits it without paying the full common-refinement modulus, for example a weighted residue-averaged pair-AP square function, a blockwise/vector-valued refinement theorem, or an equivalent direct covariance estimate.

## 1. Mikawa's all-residue error has an exactly compatible main

Fix a nonzero even shift

\[
H=2k
\]

and an odd squarefree modulus `q`. Write Mikawa's pair count

\[
\Psi_q(a;H)
:=
\sum_{\substack{0<m,n\le x\\m-n=H\\n\equiv a\pmod q}}
\Lambda(m)\Lambda(n).
\tag{1}
\]

For a residue class admissible for both prime legs, Mikawa subtracts the residue-independent Hardy--Littlewood main

\[
\mathcal H_q(H)
=
\mathfrak S
\prod_{\substack{p\mid qk\\p>2}}
\frac{p-1}{p-2}
\frac{x-|H|}{\varphi(q)}.
\tag{2}
\]

Here `mathfrak S=2 prod_{p>2}(1-1/(p-1)^2)`. This is the primary-source normalization already reconstructed in WI-061 from H. Mikawa, *On prime twins in arithmetic progressions*, *Tsukuba J. Math.* 16:2 (1992), 377--387, DOI `10.21099/tkbjm/1496161970`.

Define the main on **all** residue classes by

\[
M_q(a;H)
:=
1_{(a,q)=1}
1_{(a+H,q)=1}
\mathcal H_q(H),
\tag{3}
\]

and the extended error

\[
\widetilde E_q(a;H)
:=
\Psi_q(a;H)-M_q(a;H).
\tag{4}
\]

This is exactly the extension used in WI-061: on Mikawa-admissible reduced classes it is his error `E`; on a class where one prime leg is non-reduced it is just the raw pair count and is booked separately as the prime-power error.

Let `q|Q`, with `Q/q` odd squarefree and coprime to `q`. Raw pair counts trivially project:

\[
\Psi_q(a;H)
=
\sum_{\substack{b\bmod Q\\b\equiv a\pmod q}}
\Psi_Q(b;H).
\tag{5}
\]

Less trivially, the **Mikawa main has the identical projection law**:

\[
\boxed{
M_q(a;H)
=
\sum_{\substack{b\bmod Q\\b\equiv a\pmod q}}
M_Q(b;H).
}
\tag{6}
\]

It is enough to add one new odd prime `p`. If the parent class is inadmissible modulo `q`, every refinement remains inadmissible at that inherited bad prime, so both sides of (6) vanish. If the parent is admissible, there are two cases.

- If `p|H`, exactly `p-1` refinements are admissible modulo `p`. The prime `p` is already present in the singular product in (2) through `p|k`, so adding `p` to the modulus changes only `phi(q)`: `mathcal H_{qp}/mathcal H_q=1/(p-1)`.
- If `p` does not divide `H`, exactly `p-2` refinements avoid the two forbidden residues `0,-H mod p`. Adding `p` contributes `(p-1)/(p-2)` to the singular product and `p-1` to `phi`, hence `mathcal H_{qp}/mathcal H_q=1/(p-2)`.

Thus the number of admissible children is exactly the reciprocal of the main-term ratio in both cases. Iterating over the new primes proves (6). Subtracting (6) from (5) gives the exact error projection

\[
\boxed{
\widetilde E_q(a;H)
=
\sum_{\substack{b\bmod Q\\b\equiv a\pmod q}}
\widetilde E_Q(b;H).
}
\tag{7}
\]

The pinned prime `2` is deliberately outside this statement; the Yang/Mikawa splice already books parity separately, and deleting one fixed local prime has no effect on the conductor asymptotics below.

## 2. After the natural normalization this is literally conditional expectation

Put

\[
F_q(a;H):=q\,\widetilde E_q(a;H)
\qquad(a\in\mathbb Z/q\mathbb Z)
\tag{8}
\]

and give every finite residue space its uniform probability measure. If `Q=qr`, then (7) is exactly

\[
\begin{aligned}
\mathbb E\!\left(F_Q(\cdot;H)\mid \cdot\bmod q=a\right)
&=\frac1r
  \sum_{\substack{b\bmod Q\\b\equiv a\pmod q}}
  Q\widetilde E_Q(b;H)\\
&=q\widetilde E_q(a;H)\\
&=F_q(a;H).
\end{aligned}
\tag{9}
\]

Hence

\[
\boxed{
F_q=\mathbb E(F_Q\mid \mathcal F_q)
\qquad(q\mid Q),
}
\tag{10}
\]

where `mathcal F_q` is the residue sigma-algebra modulo `q`. On the finite CRT product this is the ordinary commuting conditional-expectation/Hoeffding structure; no probabilistic hypothesis about primes is being asserted.

This exact projective relation is absent from the abstract extremizer used in WI-062. In particular, the actual conductor vectors cannot be treated as completely unrelated if they are represented before residue scalarization.

## 3. Fourier coefficients are consistent across every refinement

Use normalized Fourier transform on `Z/qZ`:

\[
\widehat F_q(c;H)
:=
\frac1q\sum_{a\bmod q}
F_q(a;H)e(-ca/q).
\tag{11}
\]

By (8),

\[
\widehat F_q(c;H)
=
\sum_{a\bmod q}
\widetilde E_q(a;H)e(-ca/q)
=:\widetilde T_{q,c}(H).
\tag{12}
\]

If `q|Q`, lift the frequency `c mod q` to

\[
c_Q:=c\,Q/q\pmod Q.
\tag{13}
\]

Equation (7) gives

\[
\boxed{
\widetilde T_{Q,c_Q}(H)
=
\widetilde T_{q,c}(H).
}
\tag{14}
\]

Thus the additive twist depends only on the reduced rational frequency `c/q`, not on which common multiple is used to represent it. This is the exact cross-conductor consistency that the norm-only interface of WI-062 discards.

For a fixed odd squarefree common modulus `Q`, every Fourier frequency `r mod Q` has a unique reduced denominator

\[
d=\frac{Q}{(r,Q)}\mid Q.
\tag{15}
\]

Consequently Parseval partitions the fine-modulus error energy **exactly by conductor**:

\[
\boxed{
\sum_{d\mid Q}
\sum_{\substack{c\bmod d\\(c,d)=1}}
|\widetilde T_{d,c}(H)|^2
=
Q\sum_{a\bmod Q}|\widetilde E_Q(a;H)|^2.
}
\tag{16}
\]

The `d=1` term is the zero frequency. Equation (16) is simply finite Fourier orthogonality after the identification (14), but at the Yang interface it is a genuine collective conductor identity.

## 4. One common refinement removes the `sum d B_d` Hilbert coefficient

Let `G_{W,h_1}` be the normalized `W`-local pair main of WI-058, and let

\[
B_d(h_1)
=
\sum_{\operatorname{cond}(c/d)=d}
|\widehat G_{W,h_1}(c/d)|^2
\tag{17}
\]

be its exact-conductor Fourier energy. Restrict to any spectral family whose reduced denominators all divide one odd squarefree `Q`, and define its pair-error contraction at shift `H` by

\[
C_Q(h_1,H)
:=
\sum_{d\mid Q}
\sum_{\substack{c\bmod d\\(c,d)=1}}
\widehat G_{W,h_1}(c/d)
\widetilde T_{d,c}(H).
\tag{18}
\]

Using (14), all terms in (18) are distinct Fourier coordinates of the **same** vector `F_Q`. A single Cauchy--Schwarz followed by (16) therefore gives

\[
\boxed{
|C_Q(h_1,H)|^2
\le
\left(\sum_{d\mid Q}B_d(h_1)\right)
Q\sum_{a\bmod Q}|\widetilde E_Q(a;H)|^2.
}
\tag{19}
\]

Compare this with WI-062. The deterministic coefficient in (19) is just the retained local-main `L^2` energy

\[
\sum_{d\mid Q}B_d(h_1)
\le \|G_{W,h_1}\|_2^2
\ll (\log w)^2,
\tag{20}
\]

not the super-polylogarithmic diagonal cost `sum_d d B_d`. So (19) is an explicit example of the kind of extra cross-conductor relation that escapes the **information hypothesis** of WI-062--WI-063.

This is also why those earlier no-go results must not be over-read as saying that useful cross-conductor orthogonality is absent. It is present algebraically; the remaining question is whether available prime-distribution estimates can exploit it at a lossless spectral scale.

## 5. Mikawa's residue maximum makes the one-refinement route pay `Q`

The obstruction appears when (19) is connected back to the arithmetic theorem. On reduced residue classes define, as in WI-061,

\[
M_Q
:=
\max_{(a,Q)=1}
\sum_H |E(x;Q,a,H)|^2
\tag{21}
\]

on the booked injective shift range. Ignoring the already-separated non-reduced prime-power contribution only makes the estimate more optimistic. Summing the reduced part of the fine-modulus norm gives

\[
\begin{aligned}
Q\sum_H\sum_{(a,Q)=1}|E(x;Q,a,H)|^2
&\le Q\varphi(Q)M_Q\\
&\le Q^2M_Q.
\end{aligned}
\tag{22}
\]

Mikawa's proof supplies the modulus-weighted square-function budget reconstructed in WI-061,

\[
\sum_{q\le Q_*}qM_q
\ll_A x^3(\log x)^{-A}
\tag{23}
\]

for every fixed `A>0`, with the corresponding fixed modulus-range loss `B(A)`. For a single refinement modulus `Q`, (22)--(23) therefore leave one additional factor

\[
\boxed{Q.}
\tag{24}
\]

In other words, the exact Fourier martingale removes the bad **conductor-energy sum**, but Mikawa's `max_a` interface turns the common fine residue space back into a cost proportional to its modulus. Nothing in (23) supplies a growing-logarithmic saving uniform enough to absorb an arbitrary super-polylogarithmic `Q`.

A theorem controlling the relevant **residue-summed** fine-modulus variance, or a weighted vector-valued form that can be paired with the coefficients in (18) before the residue maximum, would be genuinely stronger information and is not contained in Mikawa's printed theorem/proof as audited in WI-061.

## 6. Any lossless single common refinement is larger than every fixed log power

Suppose a family of retained Fourier modes has every reduced conductor dividing `Q=Q(X)` and captures asymptotically all normalized `W`-local squared Fourier energy:

\[
\frac{\sum_{d\mid Q}B_d(h_1)}{\sum_dB_d(h_1)}\to1.
\tag{25}
\]

Because `d|Q` implies `d\le Q`, (25) is stronger than capturing the spectrum below the raw cutoff `Q`. Write

\[
Q=w^{K(X)}.
\tag{26}
\]

WI-059 proves that every fixed exponent `K_0` leaves a positive proportion of the exact Fourier energy above `w^{K_0}`. Therefore (25) forces

\[
\boxed{K(X)\to\infty.}
\tag{27}
\]

Indeed, if `K(X)` were bounded along an unbounded subsequence, choose one fixed upper bound `K_0`; then every retained conductor would lie below `w^{K_0}`, contradicting WI-059's fixed-exponent positive tail.

At the source scale

\[
w=(\log X)^C
\tag{28}
\]

with fixed `C>0`, (26)--(27) imply

\[
\frac{\log Q}{\log\log X}
=C K(X)\to\infty,
\tag{29}
\]

hence

\[
\boxed{
\frac{Q}{(\log X)^A}\to\infty
\qquad\text{for every fixed }A>0.
}
\tag{30}
\]

Combining (24) and (30) shows that the route

\[
\boxed{
\text{put a lossless retained spectrum under one common }Q
\to
\text{use exact divisor-martingale Parseval}
\to
\text{apply Mikawa only at }Q
}
\tag{31}
\]

cannot close using Mikawa's arbitrary **fixed** logarithmic saving. This is a different obstruction from WI-062--WI-063: those findings kill diagonal scalarization before cross-conductor relations are used; the present one grants the exact relation and kills only the naive **single-refinement** way of using it.

## 7. What remains genuinely open

The finding leaves several structurally different routes alive.

1. **Blockwise common refinements.** Partition the conductor spectrum into families, each contained in a manageable common modulus, exploit (16) inside every block, and prove a collective estimate across blocks that costs substantially less than the sum of their refinement moduli. A generic Cauchy step must be checked against WI-062--WI-063 rather than assumed harmless.
2. **Residue-averaged/vector-valued pair dispersion.** Replace Mikawa's residue-maximum interface by an estimate for the exact weighted fine-residue square function appearing in (19), or a vector-valued theorem that keeps the rational-frequency coordinates together before scalarization.
3. **Direct covariance.** Estimate the Yang source-normalized contraction (18) without separately materializing either the full common modulus or per-conductor Hilbert norms.

The exact martingale identity gives these routes a concrete target: a successful argument must exploit (7), (14), or (16) while avoiding the `Q` factor in (22). Merely proving better individual-conductor bounds or choosing a more elaborate spectral cutoff remains inside the no-go interfaces of WI-060--WI-063.

## 8. Prior-art and novelty audit

The ingredients underlying the structural identity are classical: aggregation of arithmetic-progression counts under refinement, finite conditional expectation, CRT/Fourier decomposition, Parseval, and exact-period/reduced-denominator partitioning. No novelty is claimed for those operations or for the generic martingale terminology.

The arithmetic normalization is anchored in Mikawa's 1992 prime-twins-in-progressions main term and in the all-residue extension already persisted in WI-061. A bounded targeted public search around Mikawa/Kawada prime-pair progression theorems, Barban--Davenport--Halberstam/large-sieve pair-error estimates, Ramanujan/exact-conductor decompositions, and divisor-lattice martingales did not locate a source stating the specific projective identity (7)--(16) for Mikawa's pair error or using it to assemble the Yang `W`-local conductor spectrum. Classical large-sieve and Ramanujan/Fourier literature is therefore treated as structural prior art, not as evidence that the source-specific consequence is new. Absence from that search is **not** used as a priority claim.

Nearby multiplet-in-progression work, including Koichi Kawada's *The prime k-tuplets in arithmetic progressions* (Tsukuba J. Math. 17 (1993), 43--57), studies distribution of multiplets across progressions but does not supply, from the theorem surface audited here, the residue-summed/vector-valued pair-error estimate needed to remove (24). Henryk Iwaniec's modern large-sieve estimates likewise concern collective character/exponential-sum control but are not silently substituted for a theorem on Mikawa's shifted pair error.

The durable Mathia contribution claimed here is only the exact source-specific deduction and its consequence for the current decision tree: **cross-conductor orthogonality exists, but the one-common-refinement implementation is still asymptotically too expensive under Mikawa's present residue-max square-function interface.**

## 9. Decisive falsification / narrowing gates

Narrow or retire the finding if any of the following occurs.

1. The main-term projection identity (6) fails after reconstructing the exact source parity/collision convention on the Yang booked family. The present theorem explicitly excludes the pinned prime `2`; any further nonmultiplicative source factor would have to be exhibited.
2. WI-059's fixed-exponent positive conductor-energy tail fails on the actual locally admissible `h_1` family, invalidating the deduction (27)--(30).
3. A theorem already available in the literature controls the residue-summed/vector-valued pair-error norm in (19) with fixed-logarithmic loss and the required moving-interval/source normalization. That would preserve (7)--(16) but materially redirect the program from a missing theorem to an existing one.
4. A blockwise refinement argument proves that the `Q` loss in (22) can be averaged away while remaining within currently established Mikawa-type information. That would not falsify the exact martingale identity, but it would narrow the decisive-negative conclusion to the single-refinement architecture explicitly stated here.
