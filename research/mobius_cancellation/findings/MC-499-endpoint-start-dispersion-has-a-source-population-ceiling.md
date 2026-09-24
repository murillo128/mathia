# MC-499 — Endpoint-start dispersion has a source-population ceiling

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `ELEMENTARY-CARDINALITY+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-498` reduces the quadratic endpoint-only repeated-residue branch to the effective support of the actual weighted physical-start pushforward. Before computing detailed first-exit reconstruction weights, the repeated-residue source population itself caps that support.

Fix an odd prime conductor `p`, one repeated residue `a mod p`, and a dyadic label range

\[
Q\le q,r\le2Q,
\qquad q\equiv r\equiv a\pmod p.
\tag{1}
\]

Let

\[
\mathcal Q_a(Q)=\{n\in[Q,2Q]\cap\mathbf Z:n\equiv a\pmod p\}.
\tag{2}
\]

Then

\[
N_Q:=\#\mathcal Q_a(Q)\le1+\frac Qp.
\tag{3}
\]

For the physical first-exit endpoints from `MC-498`,

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil,
\qquad
x_{q,r}=\max(u_q,v_r).
\tag{4}
\]

Give any selected nonempty overlap family arbitrary nonnegative pair weights `lambda_{q,r}` and let

\[
w(\xi)=\sum_{q,r}\lambda_{q,r}
\mathbf1_{x_{q,r}\equiv\xi\pmod p}.
\tag{5}
\]

Because every start in `(4)` is literally one of its two endpoints,

\[
\operatorname{supp}(w)
\subseteq
\{u_q\bmod p:q\in\mathcal Q_a(Q)\}
\cup
\{v_r\bmod p:r\in\mathcal Q_a(Q)\}.
\tag{6}
\]

Therefore

\[
\#\operatorname{supp}(w)
\le2N_Q
\le2\left(1+\frac Qp\right).
\tag{7}
\]

The effective start support

\[
R_{\rm start}=\frac{\|w\|_1^2}{\|w\|_2^2}
\tag{8}
\]

satisfies by Cauchy

\[
\boxed{
R_{\rm start}
\le2\left(1+\frac Qp\right).
}
\tag{9}
\]

After the Fourier-Parseval correction in `MC-497`, the `MC-498` dyadic short-overlap tariff is

\[
\boxed{
T_{p,H}:=\frac pH\log^2(2H).
}
\tag{10}
\]

and its weighted start-dispersion estimate is

\[
\frac{|B|}{M}
\ll\sqrt{\frac{T_{p,H}}{R_{\rm start}}}.
\tag{11}
\]

Consequently, for this certificate to prove any fixed target saving `|B|/M<=delta`, a necessary feasibility condition is

\[
2\left(1+\frac Qp\right)
\gg_\delta T_{p,H}.
\tag{12}
\]

Whenever `T_{p,H}` is larger than a fixed constant, this forces

\[
\boxed{
Q\gg_\delta pT_{p,H}
=
\frac{p^2}{H}\log^2(2H).
}
\tag{13}
\]

The previous version contained an additional `p^{3/2} log(2H)` population floor. That term came entirely from the nonsharp `sqrt(p)H^2` contribution in the original `MC-497` lag-by-lag second moment and is removed by the corrected Fourier-Parseval diagonalization. The source-population obstruction itself remains: pair multiplicity cannot manufacture more physical endpoint starts than the two one-dimensional label families provide.

The same ceiling applies to the winning-endpoint participation ratios of `MC-498`. For induced plus weights `gamma_q` and minus weights `delta_r`,

\[
\kappa_+
=\frac{(\sum_q\gamma_q)^2}{\sum_q\gamma_q^2}
\le \#\{q:\gamma_q>0\}
\le N_Q,
\tag{14}
\]

and similarly `kappa_-<=N_Q`. Since the quotient-fibre costs `D_+,D_-` are at least one,

\[
\frac{\kappa_\pm}{D_\pm}
\le N_Q
\le1+\frac Qp.
\tag{15}
\]

Thus the sufficient `MC-498` threshold `kappa_\pm/D_\pm >> T_{p,H}` is structurally impossible whenever the source population lies below `T_{p,H}`, regardless of how evenly the actual coefficients are distributed.

This is a method obstruction, not evidence for a true endpoint bias and not a bound for `M(x)`.

## Derivation

One residue class modulo `p` contains at most `1+Q/p` integers in an interval of length `Q`, proving `(3)`. Restricting those integers to primes or active first-exit labels only lowers the count.

Equation `(6)` uses the exact first-exit geometry: an overlap starts at `max(u_q,v_r)`, so no third start coordinate is created by pairing. Pair multiplicity may be quadratic in the numbers of labels, but the set of possible starts remains contained in the union of the two endpoint images.

For any nonnegative histogram supported on `S` residues,

\[
\left(\sum_\xi w(\xi)\right)^2
\le S\sum_\xi w(\xi)^2,
\tag{16}
\]

which proves `(9)`. Substitution into `(11)` yields `(12)`--`(13)`.

No distribution theorem for primes in progressions, floor quotients, or exceptional character-sum starts is needed.

## What changes in the MC-498 decisive test

A failed `kappa/D` threshold has two distinct interpretations.

If

\[
1+Q/p\lesssim T_{p,H},
\tag{17}
\]

then low effective start support is forced already by source cardinality. Even perfectly flat weights on every available repeated-residue label cannot supply enough start participation for the maximal-second-moment certificate. Calling such a failure “coefficient localization” would overinterpret it.

Only after

\[
1+Q/p\gg T_{p,H}
\tag{18}
\]

becomes feasible does the detailed `MC-498` computation of `kappa_\pm/D_\pm` become diagnostic of coefficient concentration, quotient folding, side imbalance, or another feature of the exact reconstruction.

The efficient endpoint audit is therefore: source-population gate first, exact participation/fibre calculation second.

## Prior art and novelty boundary

The participation-ratio inequality `(16)` is elementary Cauchy and standard effective-sample-size bookkeeping. Floor-quotient sets and their arithmetic-progression distribution have an established literature, but no such theorem is needed for `(3)` or `(6)`.

No novelty is claimed for those ingredients. The durable Mathia result is their specialization to the exact `MC-498` physical start map and, after the corrected `MC-497`/`MC-498` tariff, the necessary scale `(13)`.

## Boundaries and failure modes

- `(9)` caps only the effective support available to the `MC-497`/`MC-498` second-moment method. It does not lower-bound the true endpoint bias.
- A block below the population threshold may still have tiny true bias for stronger arithmetic reasons invisible to this certificate.
- Pooling different source residue classes changes the cross-root phase organization and is outside this repeated-residue count.
- Lower-prime pair-sieve masks retained by `MC-495` are not endpoint-only data and remain untouched.
- When `(18)` holds, source cardinality is no longer decisive; the actual winning-endpoint weights and quotient fibres remain load-bearing.
- Restricting labels to primes only reduces the source-population ceiling, so prime-distribution irregularity cannot invalidate the obstruction.

## Consequence

The endpoint branch should first compare every material dyadic repeated-residue block with the corrected population threshold

\[
1+Q/p
\quad\text{versus}\quad
\frac pH\log^2(2H).
\]

Blocks below threshold are method-limited by population. Only blocks above it merit the more expensive `MC-498` reconstruction audit. `MC-500` removes the dyadic scale `Q` entirely and shows when no choice of first-exit scale can satisfy even this admission test.