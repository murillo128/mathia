# MC-497 — Quadratic short-overlap bias requires exceptional interval starts

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces incomplete repeated-residue cross-root interference to a weighted sum against one fixed conductor phase. Fix an odd prime conductor `p`, the quadratic character `chi (mod p)`, a nonzero shift `h (mod p)`, and one repeated source residue `a in F_p^*`. In the physical shortened-source coordinate `m`, put

\[
c:=h a^{-1}\pmod p.
\]

The exact relative phase from `MC-495` is

\[
R_c(0)=0,
\qquad
R_c(m)=\chi(m^2-c^2)\quad(m\ne0),
\tag{1}
\]

where the values at `m=\pm c` vanish automatically. Its complete mean is

\[
\mu_c=\frac1p\sum_{m\bmod p}R_c(m)
=-\frac{1+\chi(-1)}p.
\tag{2}
\]

For `1<=H<=p` and `x in F_p`, let

\[
S_{c,x}(H)=\sum_{j=1}^{H}\bigl(R_c(x+j)-\mu_c\bigr),
\tag{3}
\]

with cyclic intervals modulo `p`. Then, uniformly in `c ne 0`,

\[
\boxed{
\sum_{x\bmod p}|S_{c,x}(H)|^2\ll pH,
\qquad
\frac1p\sum_x|S_{c,x}(H)|^2\ll H.
}
\tag{4}
\]

Consequently, for every `eta>0`, if

\[
E_{c,H}(\eta)=\{x\bmod p:|S_{c,x}(H)|\ge \eta H\},
\]

then

\[
\boxed{
\frac{|E_{c,H}(\eta)|}{p}
\ll \frac1{\eta^2H}.
}
\tag{5}
\]

Thus an order-one normalized endpoint bias at a fixed short length can occur only on `O_eta(p/H)` physical conductor starts. This is stronger than the earlier autocorrelation expansion, which bounded the same mean square by `pH+sqrt(p)H^2`; that extra `sqrt(p)H^2` term is not intrinsic. Fourier diagonalization exposes cancellation between the nonzero shifts and removes the artificial `p^{-1/2}` exceptional-density floor.

This remains an **average-over-start** theorem, not a uniform short-character-sum bound. It therefore does not conflict with the lack of a general Burgess-scale theorem for one-variable inhomogeneous polynomial character sums.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Exact centering and the one-point defect

Define

\[
Q_c(m)=\chi(m^2-c^2).
\tag{6}
\]

The classical quadratic identity gives

\[
\sum_{m\bmod p}Q_c(m)=-1.
\tag{7}
\]

Since `Q_c(0)=chi(-1)` while `R_c(0)=0`, one has exactly

\[
F_c(m):=R_c(m)-\mu_c
=Q_c(m)+\frac1p
-\chi(-1)\left(\mathbf 1_{m=0}-\frac1p\right).
\tag{8}
\]

In particular `sum_m F_c(m)=0`.

## 2. Fourier-Weil diagonalization gives the sharp start mean square

Use the unnormalized additive Fourier transform

\[
\widehat F_c(k)=\sum_{m\bmod p}F_c(m)e_p(-km),
\qquad e_p(y)=e^{2\pi i y/p}.
\tag{9}
\]

The zero mode vanishes by centering. For `k ne 0`, equation `(8)` gives

\[
\widehat F_c(k)
=\sum_{m\bmod p}\chi(m^2-c^2)e_p(-km)-\chi(-1).
\tag{10}
\]

The polynomial `m^2-c^2` has two distinct simple roots because `c ne0`, and it is not a square in `F_p[m]`. The classical Weil bound for mixed additive-multiplicative character sums of bounded-degree rational/polynomial phases, as recorded in `MC-S55`, therefore yields

\[
\boxed{
|\widehat F_c(k)|\ll\sqrt p
\qquad(k\ne0),
}
\tag{11}
\]

uniformly in `c` and `k`; the one-point defect contributes only the bounded scalar in `(10)`.

Let

\[
D_H(k)=\sum_{j=1}^{H}e_p(kj).
\tag{12}
\]

Fourier inversion and Parseval give

\[
\sum_x|S_{c,x}(H)|^2
=\frac1p\sum_{k\ne0}|\widehat F_c(k)|^2|D_H(k)|^2.
\tag{13}
\]

Since

\[
\sum_{k\bmod p}|D_H(k)|^2=pH,
\tag{14}
\]

substitution of `(11)` proves `(4)` immediately. Chebyshev then gives `(5)`.

The earlier shifted-correlation proof bounded each nonzero lag separately by `O(sqrt(p))` and then summed absolute values over all lags. Equation `(13)` is the correct spectral organization of the same second moment: it keeps the signed correlation information through the Fourier transform instead of discarding it lag by lag.

## 3. Weighted endpoint consequence

For any finite family of physical source intervals `J_i` of the same length `H`, starts `x_i mod p`, and nonnegative reconstruction weights `lambda_i`, put

\[
M=H\sum_i\lambda_i,
\qquad
B=\sum_i\lambda_i S_{c,x_i}(H).
\tag{15}
\]

If `|B|>=epsilon M`, then a fixed positive fraction of the weighted interval mass must lie on starts in `E_{c,H}(eta)` for a fixed `eta>0` depending only on `epsilon`. Equation `(5)` shows that only `O_epsilon(p/H)` conductor residues are available to carry that mass.

For variable lengths inside one dyadic band, the appropriate uniform weighted statement is the maximal estimate derived in `MC-498`. The strengthened fixed-length input `(4)` removes the old `sqrt(p)` floor from that tariff as well.

## 4. Relation to the long-overlap completion bound

`MC-496` gives a worst-case endpoint-only bound by Fourier completion, ruling out order-one endpoint bias once weighted overlap lengths are much larger than `sqrt(p) log p`. The present result is complementary: for shorter intervals it does not bound every start, but it shows that large bias can occur only on a `O(1/H)` fraction of starts.

The two statements use the same underlying square-root complete Fourier control in different norms. `MC-496` sums the Fourier envelope in `l1` to obtain a worst-case incomplete interval bound; `(13)` uses Parseval in `l2` to obtain a stronger average-over-start statement.

## Prior art and novelty boundary

- Complete mixed additive-multiplicative character bounds are classical Weil/Stepanov theory. `MC-S55` records Cochrane--Pinner, *Using Stepanov's method for exponential sums involving rational functions*, Journal of Number Theory 116 (2006), 270--292, DOI `10.1016/j.jnt.2005.04.001`.
- The Fourier-envelope plus Parseval mechanism is already used elsewhere in this line, notably `MC-448`; no novelty is claimed for that harmonic argument.
- Mean-square exceptional-set extraction by Chebyshev is standard.
- Rena Chu, *Short character sums of inhomogeneous polynomials* (arXiv:`2609.04092`, submitted 3 September 2026), is relevant only to the boundary between average-over-start information and uniform one-variable short-sum bounds. The present result does not claim a new uniform Burgess theorem.
- The durable Mathia result is the specialization to the exact `MC-495` physical cross-root phase and the resulting source-frame obstruction: short endpoint-only bias requires the actual first-exit start measure to concentrate on only `O(p/H)` conductor starts.

## Boundaries and falsification tests

- **Quadratic character only.** The factorization and bounded-degree Fourier transform are used for the quadratic repeated-residue phase. Higher-order characters require their own transform audit.
- **Physical additive coordinate.** Consecutive source intervals are intervals in `m`; conductor scaling is harmless for complete sums but must not be used to replace a physical interval by a unit-step interval in another coordinate.
- **Average over starts, not a maximum.** Individual adversarial starts may still carry large short sums.
- **Endpoint-only implication.** Lower-prime pair-sieve masks, signed or complex pre-aggregation coefficients, and other internal source arithmetic can create non-interval weights and lie outside this theorem.
- **No independence assumption.** The theorem does not model Möbius or the source starts as random; it only prices how much weighted source mass may occupy a sparse exceptional set.
- **No Möbius summatory conclusion.** This is a finite conductor obstruction inside the normalized first-exit architecture.

## Consequence for the research line

The short quadratic endpoint branch is narrower than previously recorded. At fixed length `H`, the exceptional-start density is `O(1/H)`, with no residual `p^{-1/2}` floor. The next source-frame question is therefore purely arithmetic: whether the exact first-exit endpoint map and reconstruction weights can concentrate enough mass on those rare physical start residues. `MC-498` prices that question for variable lengths and quotient fibres using the corrected Fourier-Parseval input.