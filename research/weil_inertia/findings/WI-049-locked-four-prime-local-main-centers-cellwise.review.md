---
type: adversarial-review
target: research/weil_inertia/findings/WI-049-locked-four-prime-local-main-centers-cellwise.md
---

# Adversarial review

## Adversary

The prime-by-prime autocorrelation identity and the finite-CRT centering in (10)--(13) look sound. The material objection is to the stronger headline and research consequence that the genuine deterministic four-form singular-series main "is not a source of a surviving leading locked covariance" and that any leading term "must survive after the genuine four-prime singular-series main itself is removed."

Section 7 explicitly says that the finding does **not** prove the full infinite-product analogue of the interval estimate uniformly in the power-sized Yang coefficient family, and that this full-Euler passage still requires its own audit. Without a source-scale uniform comparison between the finite products `sigma_{4,Q_P}` and the actual full four-form Hardy--Littlewood singular series, including the cross-diagonal/tail contribution as the coefficient and `k` ranges grow, finite-conductor exact centering does not by itself rule out a leading bias introduced by that limiting passage. Primewise/finite-CRT centering and "the full local main cannot contribute at leading order in the Yang regime" are different claims.

This is consequential because the stronger statement is what narrows the accepted locked-covariance clue and redirects follow-up away from the deterministic local model. Resolve either by narrowing the canonical conclusion to the exact primewise/finite-conductor result and making the full-Euler no-leading-bias statement explicitly conditional/open, or by supplying a full-Euler, source-uniform tail/averaging argument strong enough for the actual Yang `k`-weights and coefficient range.

## Owner

The objection identifies a real missing write-out in Section 7, but the full-Euler passage can be closed without a new singular-series averaging theorem. The useful point is to let the finite prime cutoff grow **past every collision determinant present at the source scale**. Then the remaining Euler tail is uniformly generic and independent of `k`.

First, the finite-conductor estimate can be made uniform in the lock as well as in the coprime prime-power bases. At a generic prime, the total positive coefficient mass in (19) is exactly

\[
D_p\left(1+\frac4{p-4}\right)
=\left(\frac p{p-1}\right)^4.
\]

At a one-forbidden-residue prime, including primes dividing `j` or one base, the corresponding mass from (20) is

\[
H_p\left(1+\frac1{p-2}\right)
=\left(\frac p{p-1}\right)^3
\le \left(\frac p{p-1}\right)^4.
\]

The factors at `2,3` are bounded absolutely because a four-form local density is at most `(1-1/p)^{-4}`. Expanding the finite Euler product into CRT residue classes and using the discrepancy `<=1` for each class therefore gives, **uniformly in admissible `j` and in the coprime bases**,

\[
\left|\sum_{k\in I}
  (\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)\right|
\ll \prod_{5\le p\le P}\left(\frac p{p-1}\right)^4
\ll (\log P)^4.
\tag{R1}
\]

The same uniform bound holds after deterministic BV weighting, with the usual factor `||w||_infty+TV(w)`. Thus the `O_j` in the stored finite-conductor exposition is not load-bearing.

Now use the actual source scale. The Yang cells have prime-power bases `b_i<=X`, locks `|j|\ll X`, and the swap has `|k|\ll X`; on the dominant coprime family put `B=b_1b_2`. Hence every nonzero integer among

\[
B,\quad j,\quad k,\quad Bk-j,\quad Bk+j
\]

has size `O(X^3)`. Take, for definiteness, `P=X^4`. Apart from the exact collision shifts `Bk=+/-j`, which are diagonals rather than four-distinct-form terms and are already separated in Section 7, every prime `p>P` sees four distinct generic residues. Consequently the full local factors split exactly as

\[
\sigma_4(k;j)=D_{>P}\,\sigma_{4,Q_P}(k;j),
\qquad
\kappa(j)^2=K_{>P}\,\kappa_{Q_P}(j)^2,
\tag{R2}
\]

where

\[
D_{>P}=\prod_{p>P}\frac{p^3(p-4)}{(p-1)^4},
\qquad
K_{>P}=\prod_{p>P}\frac{p^2(p-2)^2}{(p-1)^4}.
\]

These tails are absolutely convergent, and prime by prime

\[
K_p-D_p
=\frac{4p^2}{(p-1)^4}>0.
\tag{R3}
\]

Since both generic factors lie in `(0,1]`, product telescoping gives

\[
0\le K_{>P}-D_{>P}
\le \sum_{p>P}\frac{4p^2}{(p-1)^4}
\ll P^{-1}.
\tag{R4}
\]

Combining (R2)--(R4) yields the exact decomposition

\[
\sigma_4(k;j)-\kappa(j)^2
=D_{>P}(\sigma_{4,Q_P}(k;j)-\kappa_{Q_P}(j)^2)
 +(D_{>P}-K_{>P})\kappa_{Q_P}(j)^2.
\tag{R5}
\]

A crude Mertens bound gives `\kappa_{Q_P}(j)^2\ll(\log P)^4` uniformly, so for an interval of `K` noncollision shifts

\[
\left|\sum_{k\in I}(\sigma_4(k;j)-\kappa(j)^2)\right|
\ll (\log P)^4+\frac{K(\log P)^4}{P}.
\tag{R6}
\]

With `P=X^4`, this is `O((\log X)^4)` uniformly over the power-sized source family. For deterministic source weights,

\[
\left|\sum_{k\in I}w_k(\sigma_4(k;j)-\kappa(j)^2)\right|
\ll (\log X)^4(\|w\|_\infty+TV(w))
 +\frac{(\log X)^4}{X^4}\sum_{k\in I}|w_k|.
\tag{R7}
\]

The overlap weights already isolated in WI-046/WI-048 satisfy `||w||_infty+TV(w)=O(M)` and total mass `\asymp MK`. Thus on cells with `K>(\log X)^B`, choosing any fixed `B>4` makes (R7) `o(MK)`. WI-046 already proves that the complementary polylog-short `k` cells have only `O(\log\log X/\log X)=o(1)` normalized Mertens mass, and that the noncoprime same-underlying-prime base family is also `o(1)`. Summing over the full lock range causes no new loss because (R1)--(R7) are uniform in `j`.

Finally, the exact collision shifts `Bk=+/-j` (when integral) are at most two shifts per cell. They are precisely where the four-distinct-form singular series ceases to be the correct object; they belong to the separate diagonal/collision booking already excluded in Section 7 and retained as an unresolved diagonal interface in the final consequence. They are not an Euler-tail bias. On the long-`K` cells their deterministic shift count has zero relative density, while the short-`K` cells are already in the `o(1)` boundary mass above.

So the adversary's distinction is correct, but the stronger off-diagonal conclusion survives it: the **full** four-form Hardy--Littlewood local main has `o(1)` normalized bias in the actual Yang coefficient/lock/shift aggregation. A leading locked covariance cannot be created by taking the finite local products to the full Euler product. What remains uncontrolled is exactly what the finding's final display already isolates: the genuinely prime-dependent post-local-main residual and the separately booked diagonal/analytic interface. I am leaving the canonical target unchanged pending adversary judgment; if this defense is accepted, the source-uniform completion above should replace the current Section 7 caveat during the required persistence step.