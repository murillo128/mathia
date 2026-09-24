# MC-499 — Endpoint-start dispersion has a source-population ceiling

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `ELEMENTARY-CARDINALITY+DERIVED` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-498` reduces the quadratic endpoint-only repeated-residue branch to the effective support of the actual weighted physical-start pushforward. Before computing the detailed first-exit reconstruction weights, there is a sharp elementary admission test that was missing from that criterion: **the repeated-residue source population itself caps the effective support**.

Fix an odd prime conductor `p`, a repeated residue `a mod p`, and a dyadic label range

\[
Q\le q,r\le 2Q,
\qquad q\equiv r\equiv a\pmod p.
\tag{1}
\]

Let

\[
\mathcal Q_a(Q):=\{n\in[Q,2Q]\cap\mathbf Z:n\equiv a\pmod p\}.
\tag{2}
\]

The actual first-exit primes form a subset of this integer set, so

\[
N_Q:=\#\mathcal Q_a(Q)\le 1+\frac Qp.
\tag{3}
\]

For the physical endpoints from `MC-498`,

\[
u_q=\left\lceil\frac Xq\right\rceil,
\qquad
v_r=\left\lceil\frac{X+h}{r}\right\rceil,
\qquad
x_{q,r}=\max(u_q,v_r).
\tag{4}
\]

Give any selected nonempty overlap family arbitrary nonnegative pair weights `lambda_{q,r}` and let the induced start histogram modulo `p` be

\[
w(\xi):=
\sum_{q,r}\lambda_{q,r}
\mathbf 1_{x_{q,r}\equiv\xi\pmod p}.
\tag{5}
\]

Because every maximum in `(4)` is literally one of its two endpoints,

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
\le 2N_Q
\le 2\left(1+\frac Qp\right).
\tag{7}
\]

The effective start support of `MC-498`,

\[
R_{\rm start}
:=\frac{\|w\|_1^2}{\|w\|_2^2},
\tag{8}
\]

satisfies by Cauchy

\[
\boxed{
R_{\rm start}
\le \#\operatorname{supp}(w)
\le 2\left(1+\frac Qp\right).
}
\tag{9}
\]

This bound is independent of the reconstruction coefficients, overlap selector, primality restriction, and quotient-fibre geometry. Those can only reduce the effective support further.

Now write the `MC-498` short-overlap tariff as

\[
T_{p,H}
:=
\frac pH\log^2(2H)+\sqrt p\log(2H).
\tag{10}
\]

Its maximal-second-moment estimate has the form

\[
\frac{|B|}{M}
\ll \sqrt{\frac{T_{p,H}}{R_{\rm start}}}.
\tag{11}
\]

Consequently, this particular start-dispersion mechanism can certify a fixed small normalized bias only if the available repeated-residue label population is itself larger than the threshold. Quantitatively, for any fixed target saving `delta>0`, feasibility of `(11)` requires

\[
2\left(1+\frac Qp\right)
\gg_\delta T_{p,H}.
\tag{12}
\]

Once `T_{p,H}` is large, this forces the scale condition

\[
\boxed{
Q\gg_\delta pT_{p,H}
=
\frac{p^2}{H}\log^2(2H)
+p^{3/2}\log(2H).
}
\tag{13}
\]

In particular, the `sqrt(p) log(2H)` term alone imposes a population floor of order

\[
Q\gg_\delta p^{3/2}\log(2H)
\tag{14}
\]

for the `MC-497`/`MC-498` effective-support certificate to have enough possible physical starts to close a repeated-residue block by dispersion alone.

The same obstruction is visible directly in the winning-endpoint criterion of `MC-498`. For its induced weights `gamma_q` and `delta_r`,

\[
\kappa_+
=\frac{(\sum_q\gamma_q)^2}{\sum_q\gamma_q^2}
\le \#\{q:\gamma_q>0\}
\le N_Q,
\tag{15}
\]

and likewise `kappa_-<=N_Q`. Since the quotient-fibre costs `D_+,D_-` are at least one,

\[
\frac{\kappa_\pm}{D_\pm}\le N_Q\le1+\frac Qp.
\tag{16}
\]

Thus the sufficient threshold `kappa_\pm/D_\pm \gg T_{p,H}` from `MC-498` is **structurally impossible** whenever the repeated-residue label population lies below `T_{p,H}`, regardless of how evenly the actual coefficients are distributed.

This is a method obstruction, not evidence for a true endpoint bias and not a bound for `M(x)`.

## Derivation

The only arithmetic input is the size of one residue class inside a dyadic interval. The interval `[Q,2Q]` has length `Q`, so one congruence class modulo `p` contains at most `1+Q/p` integers. Restricting those integers to primes or to active first-exit labels only lowers the count, proving `(3)`.

Equation `(6)` uses the exact first-exit geometry from `MC-498`: an overlap starts at `max(u_q,v_r)`, so no third start coordinate can be created by pairing. Pair multiplicity may be quadratic in the numbers of `q` and `r` labels, but the set of possible starts remains contained in the union of the two endpoint images. This is precisely where a large pair population fails to buy a large physical-start population.

For any nonnegative histogram supported on `S` residues,

\[
\left(\sum_\xi w(\xi)\right)^2
\le S\sum_\xi w(\xi)^2,
\tag{17}
\]

which gives `R_start<=S` and hence `(9)`. Equations `(12)`--`(14)` are then obtained by substituting the ceiling `(9)` into the `MC-498` estimate `(11)`. Equation `(16)` is the same Cauchy inequality before quotienting, applied separately to the winning-endpoint label weights.

No distribution theorem for primes in progressions, floor quotients, or exceptional character-sum starts is required for this ceiling.

## What changes in the MC-498 decisive test

A failed `kappa/D` threshold does **not** always diagnose concentration of the true reconstruction coefficients. There are now two qualitatively different failure regimes.

If

\[
1+Q/p\lesssim T_{p,H},
\tag{18}
\]

then low effective start support is forced already by source cardinality. Even perfectly flat weights on every available repeated-residue label cannot supply enough start participation for the maximal-second-moment argument. In this regime, describing the failure as “coefficient localization” or an “arithmetic concentration on exceptional starts” would overinterpret the data: the ambient source family is simply too small relative to the exceptional-set energy threshold.

Only after

\[
1+Q/p\gg T_{p,H}
\tag{19}
\]

becomes feasible does the detailed `MC-498` computation of `kappa_\pm/D_\pm` become diagnostic. A failure there can genuinely be attributed to coefficient concentration, quotient folding, imbalance between the winning sides, or another feature of the exact reconstruction.

This split makes the next endpoint audit cheaper: test the population gate `(18)` first, and compute detailed reconstruction participation only on blocks that pass it.

## Prior art and novelty boundary

The inequality `(17)` is the elementary Cauchy bound behind the standard inverse-squared-weight effective-sample-size / participation-ratio quantity. The use of

\[
(\sum w)^2/\sum w^2
\]

as an effective sample size is standard; for example, Martino, Elvira and Louzada discuss the inverse sum of squared normalized importance weights in *Effective Sample Size for Importance Sampling based on discrepancy measures* (2017; arXiv:1602.03572). No novelty is claimed for that inequality or interpretation.

Floor-quotient sets such as `{floor(x/n)}` and their residue-class distribution also have an established literature; for example Yu and Wu, *Distribution of elements of a floor function set in arithmetical progression* (arXiv:2112.14427), study a substantially sharper distribution problem. None of those results is needed here: `(3)` is only the trivial count of source labels in one residue class, and `(6)` uses the exact first-exit maximum map already proved in `MC-498`.

The Mathia-specific contribution of this finding is therefore only the **exact specialization of those elementary support facts to the `MC-498` source-frame certificate** and the resulting method boundary `(12)`--`(14)`. It is recorded because it changes how a future failure of the accepted clue's participation-ratio test must be interpreted, not as a claim of a new general theorem.

## Boundaries and failure modes

- `(9)` is an upper bound on the effective support available to the `MC-497`/`MC-498` second-moment method. It does not lower-bound the actual endpoint bias.
- A block below the population threshold may still have tiny true bias for reasons invisible to this certificate. Stronger incomplete character-sum information, a different norm, or arithmetic cancellation inside the source weights could close it.
- Pooling different source residue classes before the repeated-residue reduction can enlarge the start population, but it also changes the cross-root phase organization. Such pooling must be derived before importing this count across blocks.
- The lower-prime pair-sieve masks retained by `MC-495` are not endpoint-only data and are untouched by this obstruction.
- When `(19)` holds, the population ceiling is no longer decisive; the actual winning-endpoint weights and quotient fibres from `MC-498` remain load-bearing.
- The prime restriction can only make the source-population ceiling smaller than `(9)`, so no prime-distribution irregularity can invalidate the obstruction.

## Consequence

The accepted endpoint clue should be triaged in two stages. First compare each material dyadic repeated-residue block with the cheap source-population gate `1+Q/p` versus `T_{p,H}`. Blocks below threshold cannot be closed by the current start-dispersion certificate and should be classified as **method-limited by population**, not as unexplained coefficient concentration. Only blocks above threshold merit the more expensive exact `kappa_\pm/D_\pm` reconstruction audit.

If every material block falls below the population gate, then the endpoint-only continuation cannot be settled by further refinement of the same `MC-497` exceptional-start second moment: a genuinely stronger character-sum input or a different surviving arithmetic channel is required.