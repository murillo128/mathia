# MC-493 — Native cross-root blocks need square-root multiplicity

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-HILBERT/COHERENCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-492` leaves one native repeated-residue escape open on complete periods: although every same-root block is constructive for the Buchstab common-sign coefficient, there are `k_+ k_-` opposite-root pairs, each with normalized Jacobi-scale correlation `O(p^{-1/2})`. Pair counting alone therefore suggests that a sufficiently dense two-root block might accumulate destructive interference.

The accumulation has an exact threshold. Fix an odd prime conductor `p`, a nonprincipal character `chi (mod p)`, a nonzero conductor residue `a`, and finite repeated-residue families

\[
Q_+,Q_-\subset\{q\text{ active prime}:q\equiv a\pmod p\}.
\]

Put all exact completed first-exit rows on one common joint period and retain their exact nonnegative sieve amplitudes. Write the two root families as in `MC-492`, and set

\[
U=\sum_{q\in Q_+}G_q^+,
\qquad
V=\sum_{r\in Q_-}G_r^-.
\tag{1}
\]

The common native Buchstab coefficient is `-1`, so the norm relevant to the two-root repeated-residue block is `||U+V||_2`.

Let

\[
a_q=\|G_q^+\|_2,
\qquad
b_r=\|G_r^-\|_2,
\qquad
A=\sum_{q\in Q_+}a_q^2,
\qquad
B=\sum_{r\in Q_-}b_r^2,
\tag{2}
\]

and define the effective participation numbers

\[
\kappa_+=\frac{(\sum_{q\in Q_+}a_q)^2}{A},
\qquad
\kappa_-=\frac{(\sum_{r\in Q_-}b_r)^2}{B},
\tag{3}
\]

with the empty block omitted. Always `1<=kappa_+<=|Q_+|` and `1<=kappa_-<=|Q_-|`.

`MC-492` gives two inputs. First, same-root repeated-residue Gram entries are nonnegative, hence

\[
\|U\|_2^2\ge A,
\qquad
\|V\|_2^2\ge B.
\tag{4}
\]

Second, every opposite-root pair on a complete joint period satisfies

\[
|\langle G_q^+,G_r^-\rangle|
\le \delta_p\,a_qb_r,
\qquad
\delta_p:=\frac{\sqrt p+1}{p-2}.
\tag{5}
\]

Therefore

\[
|\langle U,V\rangle|
\le
\delta_p\Bigl(\sum_q a_q\Bigr)\Bigl(\sum_r b_r\Bigr)
=
\delta_p\sqrt{\kappa_+\kappa_-AB}.
\tag{6}
\]

Combining `(4)`--`(6)` and `2\sqrt{AB}<=A+B` gives the block lower bound

\[
\boxed{
\|U+V\|_2^2
\ge
\Bigl(1-\delta_p\sqrt{\kappa_+\kappa_-}\Bigr)(A+B).
}
\tag{7}
\]

whenever the displayed factor is positive. Thus a native complete-period collective cross-root mechanism cannot even reduce the diagonal baseline by an order-one proportion unless

\[
\boxed{
\sqrt{\kappa_+\kappa_-}\gtrsim \delta_p^{-1}\asymp \sqrt p.
}
\tag{8}
\]

In particular, if `|Q_+|+|Q_-|=o(sqrt(p))`, then

\[
\|U+V\|_2^2\ge (1-o(1))(A+B).
\tag{9}
\]

The dense cross-root loophole from `MC-492` therefore begins only at **square-root conductor multiplicity**, not merely above the logarithmic pair-coherence threshold from `MC-491`.

For quadratic `chi`, `MC-492` gives the sharper pair bound `|C_p^{+-}|<=2`, so one may replace `(5)` by

\[
\delta_p^{(2)}:=\frac{2}{p-2}=O(p^{-1}).
\tag{10}
\]

The corresponding necessary effective multiplicity is then order `p` rather than `sqrt(p)`.

There is also a deterministic source-scale consequence requiring no prime-distribution theorem. Among integers `q<=Q`, one fixed residue class modulo `p` contains at most `Q/p+1` labels. Hence for every fixed `epsilon>0`, if the repeated-residue first-exit range satisfies

\[
Q\le p^{3/2-\varepsilon},
\tag{11}
\]

then each root block has cardinality `O(p^{1/2-epsilon})`, and `(9)` applies uniformly. For quadratic characters the same argument pushes the protected range to `Q<=p^{2-epsilon}`.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Aggregate Jacobi interference cannot beat the diagonal below the threshold

Expand the native two-root norm:

\[
\|U+V\|_2^2
=
\|U\|_2^2+\|V\|_2^2+2\operatorname{Re}\langle U,V\rangle.
\tag{12}
\]

The pointwise phase locking proved in `MC-492` makes every same-root cross term nonnegative, so discarding those terms can only lower the right side. This gives `(4)`.

For the cross term, sum the pairwise complete-period bound from `MC-492` before making any sign assumption:

\[
|\langle U,V\rangle|
\le
\sum_{q,r}|\langle G_q^+,G_r^-\rangle|
\le
\delta_p\sum_{q,r}a_qb_r.
\tag{13}
\]

The double sum factors, and `(3)` turns it exactly into `(6)`. Thus

\[
\|U+V\|_2^2
\ge A+B-2\delta_p\sqrt{\kappa_+\kappa_-AB}.
\tag{14}
\]

Using `2\sqrt{AB}<=A+B` proves `(7)`. No Geršgorin step, equal-row-norm assumption, random-phase hypothesis, or distribution of first-exit primes is used.

The participation numbers are important. Cardinality by itself can overstate the danger when many completed rows have tiny norm: the relevant quantity is the `l1/l2` effective support of the row norms. A collective escape needs square-root-conductor **effective mass on both root branches**, not simply many nominal labels.

## 2. The first dangerous source scale is at least `p^(3/2)`

Let all active repeated-residue labels lie in `q<=Q`. A fixed congruence class `a (mod p)` contains at most

\[
\left\lfloor\frac{Q-a}{p}\right\rfloor+1\le \frac Qp+1
\tag{15}
\]

integers, so the same bound holds for first-exit primes. If `Q<=p^(3/2-epsilon)`, then

\[
|Q_\pm|\ll p^{1/2-\varepsilon}+1,
\tag{16}
\]

and therefore `delta_p sqrt(kappa_+ kappa_-)=O(p^{-epsilon})`. Equation `(7)` becomes

\[
\boxed{
\|U+V\|_2^2\ge (1-O(p^{-\varepsilon}))(A+B).
}
\tag{17}
\]

For quadratic characters, `(10)` gives the analogous protected scale `Q<=p^(2-epsilon)`.

This does not assert that a block at or above those scales actually cancels. It only identifies the earliest scale at which the pairwise Jacobi tariff stops ruling the mechanism out by itself. Any proposed dense escape above that scale must still preserve exact first-exit support, endpoints and reconstruction weights and must prove the required coherent sign of the aggregate cross term.

## 3. Prior art and novelty boundary

The analytic mechanism in `(6)`--`(7)` is classical Hilbert-space/coherence algebra: pairwise coherence is summed and Cauchy--Schwarz converts `l1` row mass into an effective-support factor. Closely related cumulative-coherence/Babel-function and Gram-matrix bounds are standard in frame and sparse-approximation theory; for example Joel A. Tropp, *Greed is good: Algorithmic results for sparse approximation*, IEEE Transactions on Information Theory 50 (2004), 2231--2242, develops cumulative coherence and Gram singular-value bounds. No novelty is claimed for that abstract inequality.

The arithmetic input is entirely `MC-492`: same-root positivity for the native first-exit coefficient and the exact Jacobi-sum cross-root bound. The durable Mathia delta is their **collective threshold inside the exact Buchstab source frame**. The previously open statement “many Jacobi-scale cross-root terms may accumulate” is now quantitatively narrowed: below square-root conductor effective multiplicity they cannot produce an order-one reduction of the diagonal, and a whole repeated-residue source range below `p^(3/2-epsilon)` is automatically protected.

A targeted prior-art search found the generic coherence machinery but no reason to treat `(7)` as a new abstract frame theorem. The source-specific threshold is therefore classified as a derived frontier obstruction, not a novelty claim.

## Boundaries and falsification tests

- **Complete joint periods.** The Jacobi pair bound in `(5)` is inherited from `MC-492` and uses complete conductor averaging plus CRT separation of the exact masks. A sharply incomplete signed transform is outside `(7)`.
- **One conductor residue class.** The theorem isolates the dense repeated-residue loophole. Distinct conductor residues are governed by the stronger completed-row estimates of `MC-490`--`MC-491`.
- **Native common-sign coefficient.** Same-root positivity is used critically. A source-derived q-dependent sign or phase before closure can invalidate `(4)` and remains a genuine escape.
- **Necessary, not sufficient, multiplicity.** Reaching `sqrt(p)` effective participation does not create cancellation; it merely removes this particular lower-bound obstruction.
- **Exact masks retained.** The pairwise estimate comes from the exact completed hard-mask rows of `MC-492`, not a positive envelope substituted for the first-exit cell.
- **Row-norm participation matters.** A nominal block of size at least `sqrt(p)` can still be protected when its effective participation numbers in `(3)` are smaller.
- **No global arithmetic conclusion.** The result prices one proof architecture inside the normalized empty-vector first-exit branch; it is not a bound for the Möbius summatory function.

## Consequence for the accepted clue

The accepted first-exit clue should no longer treat collective complete-period cross-root accumulation as live at arbitrary density. With native coefficients, the completed repeated-residue route has a new admission threshold: it must first produce effective participation of order `sqrt(p)` on both roots (order `p` for quadratic characters), or it cannot even reduce the diagonal by an order-one factor.

Thus the surviving collective branch is pushed to genuinely large source scales, beginning no earlier than `q`-ranges of order `p^(3/2)` in the general character case under the deterministic residue-count bound. Below that range, research should not revisit cross-root accumulation without introducing a source-derived sign/phase law or an incomplete transform that invalidates the complete-period Jacobi estimate.