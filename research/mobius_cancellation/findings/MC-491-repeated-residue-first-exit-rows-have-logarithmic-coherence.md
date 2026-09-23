# MC-491 — Repeated-residue first-exit rows have only logarithmic pair coherence

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-SIEVE+MERTENS+TOTIENT` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-490` proves Riesz stability for completed first-exit rows whose prime labels occupy distinct residues modulo the conductor `p`, but deliberately leaves the repeated-residue branch open because the underlying character correlation jumps from `O(1)` to `p-2` when

\[
q\equiv r\pmod p.
\]

That large finite-field correlation does **not** make two exact first-exit hard-mask rows nearly parallel in the polynomial source ranges relevant to the current branch. Their different nested pair-sieve masks decorrelate them by a logarithmic factor.

Keep the notation of `MC-489`--`MC-490`. Let `p` be an odd prime, `chi` a nonprincipal character modulo `p`, and `h\not\equiv0\pmod p`. For an active first-exit prime `q\ne p`, on the root `q|n` put

\[
G_q(m)=K_h(qm)A_q(qm),
\qquad
K_h(x)=\chi(x+h)\overline{\chi(x)},
\qquad
A_q(x)=\mathbf 1_{(x(x+h),P(q))=1}.
\tag{1}
\]

Take distinct active primes `q<r` with

\[
q\equiv r\pmod p,
\tag{2}
\]

and assume both rows are nonempty. Put

\[
d_q=\frac1{P(q)}\#\{b\bmod P(q):A_q(qb)=1\},
\qquad
d_r=\frac1{P(r)}\#\{b\bmod P(r):A_r(rb)=1\},
\tag{3}
\]

and let `d_{q,r}` be the simultaneous mask density on `P(r)` from `MC-489`. On the common period `pP(r)`, the repeated-residue branch of the exact character correlation gives

\[
\langle G_q,G_r\rangle=(p-2)P(r)d_{q,r},
\tag{4}
\]

while

\[
\|G_q\|_2^2=(p-2)P(r)d_q,
\qquad
\|G_r\|_2^2=(p-2)P(r)d_r.
\tag{5}
\]

Hence the normalized pair coherence is **exactly**

\[
\boxed{
\rho(q,r):=
\frac{|\langle G_q,G_r\rangle|}{\|G_q\|_2\|G_r\|_2}
=
\frac{d_{q,r}}{\sqrt{d_qd_r}}.
}
\tag{6}
\]

The apparent `p`-scale character degeneracy has disappeared completely from the normalized problem. What remains is a local sieve-overlap ratio.

For every active sieve prime `ell<q`, the two rows forbid

\[
\{0,-hq^{-1}\},
\qquad
\{0,-hr^{-1}\}
\pmod\ell.
\tag{7}
\]

If `ell|h(q-r)`, the displaced roots collapse and the normalized local overlap factor is `1`. Otherwise the union has three distinct residues and the normalized factor is

\[
\frac{1-3/\ell}{1-2/\ell}
=
\frac{\ell-3}{\ell-2}.
\tag{8}
\]

For `q\le ell<r`, only the `r` row is sifted, so the normalized factor is

\[
\sqrt{1-\frac{\nu_\ell(h)}\ell},
\qquad
\nu_\ell(h)=
\begin{cases}
1,&\ell|h,\\
2,&\ell\nmid h.
\end{cases}
\tag{9}
\]

Therefore the exact Euler product is

\[
\boxed{
\rho(q,r)
=
\prod_{\substack{\ell<q\\ \ell\ \mathrm{active}\\ \ell\nmid h(q-r)}}
\frac{\ell-3}{\ell-2}
\prod_{\substack{q\le\ell<r\\ \ell\ \mathrm{active}}}
\sqrt{1-\frac{\nu_\ell(h)}\ell}.
}
\tag{10}
\]

The factors omitted from the first product because `ell|h(q-r)` are exactly the local coincidences that can increase coherence. Even after charging all of them, they cannot restore order-one coherence in polynomial ranges. For a generic active prime,

\[
\frac{\ell-3}{\ell-2}\le 1-\frac1\ell,
\qquad
\sqrt{1-\frac2\ell}\le 1-\frac1\ell.
\tag{11}
\]

Primes dividing `h` are charged as exceptions, as are primes dividing `q-r`; the conductor prime `p` is harmless here because `(2)` forces `p|(q-r)`. The fixed sieve exclusions of the current source frame only change the implied constant. Thus

\[
\boxed{
\rho(q,r)
\ll
\prod_{\ell<r}\left(1-\frac1\ell\right)
\prod_{\ell\mid h(q-r)}\left(1-\frac1\ell\right)^{-1}
\ll
\frac{1}{\log r}\,
\frac{|h(q-r)|}{\varphi(|h(q-r)|)}.
}
\tag{12}
\]

Using the classical bound `N/phi(N) << log log(3N)`,

\[
\boxed{
\rho(q,r)
\ll
\frac{\log\log(3|h(q-r)|)}{\log r}.
}
\tag{13}
\]

If `q,r<=p^A` and `|h|<=p^B` for fixed `A,B`, then `(2)` and `q\ne r` imply `r-q>=p`, hence `r>=p`. Consequently

\[
\boxed{
\rho(q,r)
\ll_{A,B}
\frac{\log\log p}{\log p}
=o(1).
}
\tag{14}
\]

So the repeated-conductor-residue branch is **pairwise decorrelated by the exact pair-sieve masks**, despite having identical completed character phase.

Combining `(14)` with `MC-490` gives a small-family consequence without any residue-distinctness assumption. For a polynomial-range family `Q` of `k` nonempty rows, let `H_q=G_q/\|G_q\|_2`. Distinct-residue pairs have coherence at most `2/(p-2)` by `MC-490`, while repeated-residue pairs satisfy `(14)`. Hence

\[
\max_{q\ne r}|\langle H_q,H_r\rangle|
\ll_{A,B}\frac{\log\log p}{\log p}.
\tag{15}
\]

Geršgorin then yields

\[
1-(k-1)\mu_p
\le \lambda(\Gamma)\le
1+(k-1)\mu_p,
\qquad
\mu_p\ll_{A,B}\frac{\log\log p}{\log p}.
\tag{16}
\]

Therefore any arbitrary-residue family with

\[
k=o\!\left(\frac{\log p}{\log\log p}\right)
\tag{17}
\]

is asymptotically Riesz-stable. Repeated conductor residues cannot rescue a scalar completed-row mechanism at this cardinality.

This does **not** close dense repeated-residue blocks. The pairwise coherence in `(14)` is only logarithmically small, so a block with cardinality comparable to or larger than `log p/log log p` is outside the conclusion of `(16)`. Nor does the theorem control incomplete source intervals or inner-coordinate-dependent coefficients. Those remain the live ways to escape the complete-period scalar-row obstruction.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Exact local overlap formula

For `ell<q`, both one-row densities have the same local factor

\[
L_\ell=1-\frac{\nu_\ell(h)}\ell.
\tag{18}
\]

If `ell|h`, both forbidden pairs collapse to `{0}`, so the intersection density also has local factor `L_ell` and the normalized ratio is `1`. Assume `ell\nmid h`. If `ell|(q-r)`, then

\[
-hq^{-1}\equiv-hr^{-1}\pmod\ell,
\tag{19}
\]

so again the two forbidden sets coincide and the normalized ratio is `1`. Otherwise the three residues in `(7)` are distinct, the intersection density is `1-3/ell`, and division by `sqrt(L_ell^2)=1-2/ell` gives `(8)`.

For `q<=ell<r`, the `q` row carries no `ell`-restriction while the `r` row contributes `L_ell`. After normalization by `sqrt(1\cdot L_ell)`, the factor is `(9)`. Multiplying the CRT-local factors proves `(10)`.

The possible local zero at `ell=3` is real: if the three forbidden residues exhaust `F_3`, the two completed rows have disjoint hard-mask support and `rho(q,r)=0`. The parity prime is likewise retained exactly; the theorem is stated only for nonempty rows.

## 2. Mertens mass beats the collision correction

Outside primes dividing `h(q-r)`, every local factor in `(10)` is bounded by `1-1/ell` using `(11)`. Reintroducing the exceptional primes multiplicatively gives the first bound in `(12)`; extending the exceptional product to all prime divisors of `|h(q-r)|` only enlarges it.

Mertens' product theorem gives

\[
\prod_{\ell<r}\left(1-\frac1\ell\right)\asymp\frac1{\log r}.
\tag{20}
\]

The correction is the familiar totient ratio

\[
\prod_{\ell\mid N}\left(1-\frac1\ell\right)^{-1}
=\frac{N}{\varphi(N)}
\ll \log\log(3N).
\tag{21}
\]

Rosser--Schoenfeld's classical explicit estimates for prime products and Euler's totient function supply authoritative quantitative forms of `(20)`--`(21)`; `MC-S6` already anchors that source in this line.

The key structural point is that the local coincidences can restore only the product of reciprocal Euler factors for the primes dividing `h(q-r)`. Even an adversarially smooth difference `q-r` pays at most the classical `log log` totient inflation, while the ordinary active-prime mass below `r` contributes the full `1/log r` Mertens decay.

## 3. Relation to the repeated-residue loophole in MC-490

The large branch `C_p(q,r)=p-2` in `MC-489` can look dangerous if the character phase is examined in isolation: rows with `q\equiv r (mod p)` are then identical modulo the conductor. Equation `(6)` shows why that diagnosis is incomplete for the exact first-exit object. The row includes a nested pair-sieve mask whose shifted forbidden class depends on `q^{-1}` modulo every smaller active prime, not only modulo `p`.

Thus conductor collision is not simultaneous collision across the sieve moduli. To keep the two masks aligned at a prime `ell<q`, one also needs `ell|(q-r)` (or the fixed shift degeneracy `ell|h`). Asking for alignment at many small primes forces those primes into `h(q-r)`, and `(21)` prices the maximum possible recovery.

This closes the simplest interpretation of the repeated-residue escape: **identical character rows are not identical exact first-exit rows**. It also upgrades the small-family Riesz statement from `MC-490`: residue distinctness is unnecessary at cardinality `(17)`.

What remains is genuinely collective or non-complete. A dense repeated-residue class could in principle accumulate many logarithmically small positive correlations; an incomplete interval can destroy the exact CRT product; and an `m`-dependent coefficient can alter the Gram structure itself. None is reduced to `(16)`.

## 4. Prior art and novelty boundary

Every analytic ingredient is classical. The local products are ordinary CRT/sieve-overlap factors of the same kind that appear in dimension-two sieves and Hardy--Littlewood singular series. Mertens' prime product and the maximal-order control of `N/phi(N)` are classical; no novelty is claimed for them. Geršgorin is the same classical matrix step already used in `MC-490`.

Schlage-Puchta, *Sifted character sums and free quotients of Bianchi groups*, Math. Proc. Cambridge Philos. Soc. 141 (2006), 205--207, DOI `10.1017/S0305004106009261`, is adjacent prior art showing that sifted multiplicative-character sums are established objects. A targeted search also finds the standard singular-series literature in which local shifted-sieve collision factors are organized by prime divisors of the shift. No searched source was used to support a novelty claim for `(10)`--`(17)`.

The durable Mathia delta is the **frontier classification** inside the exact `MC-484` first-exit architecture: the repeated-conductor-residue branch left open by `MC-490` has now been priced with its moving hard masks. Its pair coherence is logarithmically small in polynomial source ranges, and arbitrary residue patterns remain uniformly well conditioned for families below the logarithmic cardinality threshold `(17)`.

## Boundaries and falsification tests

- **Complete periods only.** The exact factorization uses `pP(r)`. It does not imply the same coherence on a short or sharply truncated source interval.
- **Polynomial source range for `(14)`--`(17)`.** Equation `(13)` is the general bound. The stated `log log p/log p` form assumes polynomial bounds for `q,r,h` in the conductor.
- **Canonical active-prime set.** The comparison with the full Mertens product uses the current first-exit sieve with only its fixed exclusions and the conductor prime removed. A future construction omitting a growing prime set must re-price the missing Euler mass.
- **Pairwise, not dense-block, obstruction.** Small pair coherence does not rule out collective behavior once `k log log p/log p` is order one or larger.
- **Scalar completed rows.** As in `MC-490`, inner-coordinate-dependent coefficients or arithmetic kernels can change the Gram matrix and remain outside the theorem.
- **One root branch displayed.** The translated `q|n+h` branch has the analogous local calculation. Superposing root branches before closure can create extra interference and must be analyzed separately.
- **No global arithmetic conclusion.** This is a proof-architecture obstruction within the normalized first-exit source frame, not a bound for the Möbius summatory function.

## Consequence for the accepted clue

The accepted first-exit clue should no longer list an isolated repeated conductor residue as an unpriced source of row alignment. In polynomial ranges, the exact pair-sieve masks reduce every repeated-residue pair to coherence `O(log log p/log p)`, and arbitrary-residue scalar row families of size `o(log p/log log p)` are Riesz-stable.

The surviving repeated-residue question is **collective**: can a genuinely dense block, with exact source coefficients and endpoints retained, exploit its structured local-overlap matrix before positive closure? Alongside that, incomplete signed transforms and inner-coordinate-dependent `q`-specific kernels remain live. Reusing the bare `p-2` character correlation as evidence of a two-row favorable direction is now exhausted.