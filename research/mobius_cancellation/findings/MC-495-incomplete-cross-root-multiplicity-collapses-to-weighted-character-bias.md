# MC-495 — Incomplete cross-root multiplicity collapses to one weighted character bias

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-CHARACTER-ALGEBRA+DERIVED-APPLICATION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-494` closes arbitrary native repeated-residue multiplicity after complete-period CRT factorization. The remaining loophole in the accepted clue is a genuinely incomplete cross-root transform, where the Jacobi average need not be available. Even there, however, **row multiplicity itself is not a new conductor-phase resource**.

Fix an odd prime conductor `p`, a nonprincipal character `chi (mod p)`, a nonzero shift `h (mod p)`, and one repeated source residue `a in F_p^*`. Consider arbitrary finite native first-exit families on the two roots with every source prime satisfying

\[
q\equiv a\pmod p.
\]

Extend every shortened interval/mask by zero to one common integer `m`-domain. As in `MC-492`, write the exact rows as

\[
G_q^+(m)=K_a^+(m)B_q^+(m),
\qquad
G_r^-(m)=K_a^-(m)B_r^-(m),
\tag{1}
\]

where the native Buchstab sign is common, the exact interval-plus-pair-sieve amplitudes satisfy

\[
B_q^+(m),B_r^-(m)\ge0,
\tag{2}
\]

and repeated residue makes the conductor phases independent of the individual source labels:

\[
K_a^+(m)=\chi(am+h)\overline{\chi(am)},
\qquad
K_a^-(m)=\chi(am)\overline{\chi(am-h)}.
\tag{3}
\]

Therefore the **entire incomplete repeated-residue block already aggregates pointwise** before any completion:

\[
U(m):=\sum_qG_q^+(m)=K_a^+(m)A(m),
\qquad
V(m):=\sum_rG_r^-(m)=K_a^-(m)B(m),
\tag{4}
\]

with only two nonnegative source amplitudes

\[
A(m):=\sum_qB_q^+(m),
\qquad
B(m):=\sum_rB_r^-(m).
\tag{5}
\]

No matter how many repeated-residue rows are present, their incomplete native interaction has only the two conductor directions in `(3)`. Its exact norm is

\[
\boxed{
\|U+V\|_2^2
=E_+ + E_- +2\operatorname{Re} C_{A,B},
}
\tag{6}
\]

where

\[
E_+=\sum_m |K_a^+(m)|^2A(m)^2,
\qquad
E_-=\sum_m |K_a^-(m)|^2B(m)^2,
\tag{7}
\]

and the whole possible destructive interference is the **single weighted relative-phase sum**

\[
\boxed{
C_{A,B}
=\sum_m A(m)B(m)R_a(m),
\qquad
R_a(m):=K_a^+(m)\overline{K_a^-(m)}.
}
\tag{8}
\]

Explicitly,

\[
R_a(m)
=\chi(am+h)\chi(am-h)\overline{\chi(am)}^{\,2}.
\tag{9}
\]

Away from the character zeros this is the fixed rational-function character phase

\[
\boxed{
R_a(m)=\chi\!\left(1-\frac{h^2}{a^2m^2}\right).
}
\tag{10}
\]

Thus an incomplete repeated-residue escape cannot come from having many source rows or many opposite-root pairs. Multiplicity can only change the **nonnegative weight**

\[
W(m)=A(m)B(m)
\tag{11}
\]

placed against one fixed conductor phase `R_a`. To obtain an order-one reduction of the separate-root energy `E_++E_-`, the exact source overlap must itself have an order-one **negative weighted bias** against `R_a`; pair counting or row density cannot manufacture it.

Equivalently, if

\[
\|U+V\|_2^2\le (1-\eta)(E_++E_-)
\qquad (0<\eta<1),
\tag{12}
\]

then necessarily

\[
\boxed{
-\operatorname{Re}C_{A,B}
\ge \frac{\eta}{2}(E_++E_-).
}
\tag{13}
\]

Since `|C_{A,B}|<=sqrt(E_+E_-)`, this forces a fixed negative correlation of at least the requested saving scale and sufficient balance between the two root energies. Incompleteness remains a live route, but it is now a precise **weighted character-bias problem**, not a collective-multiplicity problem.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Pointwise aggregation does not use completion

The factorization `(4)` is purely algebraic. If `q\equiv a (mod p)`, then the plus-root phase after `n=qm` is exactly the first expression in `(3)`, regardless of the source prime's size, cutoff, or shortened interval. All q-dependence is confined to the nonnegative exact amplitude `B_q^+`, so

\[
\sum_qG_q^+
=K_a^+\sum_qB_q^+.
\tag{14}
\]

The same argument applies to the minus root. Zero-extension lets the physical shortened intervals differ arbitrarily without changing `(14)`. No complete conductor period, common auxiliary sieve period, CRT factorization, or Jacobi estimate has been used.

This is the incomplete analogue of the aggregation step that `MC-494` exploited before completion. The new consequence is that the aggregation itself survives when completion is forbidden. What is lost without completion is only the ability to replace the cross-root term by a universal Jacobi scalar.

The native common Buchstab coefficient contributes the same overall sign to all first-exit rows and therefore does not alter this conclusion. A genuinely q-dependent signed or complex source coefficient introduced **before** the sum in `(14)` would break the nonnegative aggregation and remains outside the theorem.

## 2. The surviving object is one rational-function character phase

Expanding `(4)` gives `(6)` with

\[
K_a^+(m)\overline{K_a^-(m)}
=\chi(am+h)\overline{\chi(am)}\,
  \overline{\chi(am)}\chi(am-h),
\]

which is `(9)`. For `am\not\equiv0 (mod p)`, multiplicativity and unit modulus give `(10)`.

After the conductor relabeling

\[
t=amh^{-1}\pmod p,
\]

this becomes simply

\[
R(t)=\chi(1-t^{-2}),
\tag{15}
\]

up to the zero residues. Hence changing the repeated residue `a`, the number of source primes, or their multiplicities does not create a family of independent conductor phases; it only changes how the exact source weight samples a fixed phase after a conductor permutation.

For quadratic `chi`, `(9)` simplifies further on nonzero points to

\[
R_a(m)=\chi((am)^2-h^2).
\tag{16}
\]

So even in the most concrete two-root case the unresolved cross term is exactly a nonnegative source-derived weight against one quadratic character sequence. Pointwise destructive interference is certainly possible where `R_a(m)=-1`; the theorem does **not** assert incomplete positivity. It says that any such cancellation must be proved as a correlation of the actual source weight with that sign pattern.

## 3. Conductor projection isolates the only possible incomplete bias

Because `R_a` is `p`-periodic, every finite physical `m`-domain can be compressed exactly to its conductor-residue weight

\[
w(t):=
\sum_{\substack{m\equiv t\ (p)}}A(m)B(m)
\ge0.
\tag{17}
\]

Then

\[
\boxed{
C_{A,B}=\sum_{t\in\mathbf F_p} w(t)R_a(t).
}
\tag{18}
\]

This projection loses no information relevant to cross-root interference. It also cleanly separates the completed and incomplete pieces. Writing

\[
\bar w=\frac1p\sum_t w(t),
\]

one has

\[
C_{A,B}
=
\bar w\sum_tR_a(t)
+
\sum_t(w(t)-\bar w)R_a(t).
\tag{19}
\]

The first term is exactly the complete Jacobi-scale contribution already evaluated in `MC-492`--`MC-494`. Therefore any incomplete effect larger than that completed scale must come from the **centered conductor profile**

\[
w(t)-\bar w.
\tag{20}
\]

In particular, incompleteness is useful only insofar as exact endpoints, lower-prime cutoffs, or other retained source data create a nonuniform conductor projection that correlates negatively with `(15)`. Merely increasing the number of repeated-residue first-exit primes changes `w`; it does not enlarge the conductor phase space.

Equation `(19)` provides a direct falsification target. A proposed incomplete mechanism must estimate the second term with the **actual** `w` induced by the source frame. Replacing `w` by an arbitrary interval, smooth weight, independent random weight, or uniform density changes the question unless the replacement error is quantitatively transferred.

## 4. Necessary correlation for an order-one energy reduction

Equation `(13)` follows immediately from `(6)` and `(12)`. There is also the universal Cauchy bound

\[
|C_{A,B}|\le \sqrt{E_+E_-},
\tag{21}
\]

because pointwise

\[
|R_a(m)|=|K_a^+(m)|\,|K_a^-(m)|.
\]

Consequently the relative reduction of `E_++E_-` is at most

\[
\frac{2\sqrt{E_+E_-}}{E_++E_-}\le1.
\tag{22}
\]

To save a fixed fraction `eta`, `(13)` requires the normalized negative bias

\[
\frac{-\operatorname{Re}C_{A,B}}{\sqrt{E_+E_-}}
\tag{23}
\]

to be at least `eta`, and when the two root energies are strongly unbalanced the stronger balance tariff from `(22)` applies. Thus a successful incomplete argument must prove both substantial root overlap and phase-selective bias; cardinality or effective participation alone is insufficient.

This sharpens `MC-493`: the square-root-multiplicity threshold there came from summing pairwise complete correlations before `MC-494` tensorized the complete block. In the incomplete setting, multiplicity has no analogous threshold at all. After exact aggregation it is absorbed into `A` and `B`; the only remaining question is the weighted bias `(18)`.

## 5. Prior art and novelty boundary

No new character-sum theorem is claimed. The algebra `(4)`--`(10)` uses only the repeated-residue phase locking already established in `MC-492`, and the completed mean term in `(19)` is the same Jacobi-sum object used in `MC-492`--`MC-494`. Complete rational multiplicative-character sums and their Weil-type bounds are classical; `MC-S55` (Cochrane--Pinner) is the line's primary anchor for that machinery.

Classical Burgess theory (`MC-S34`) gives power savings for unweighted interval character sums in suitable ranges, and `MC-S38` records a concrete squarefree-weighted character-sum treatment obtained from additional arithmetic structure. Those results do not supply a bound for `(18)` with the exact first-exit overlap profile `w`: an arbitrary nonnegative weight can concentrate on residues with negative relative phase, while the source-derived weight must be analyzed rather than replaced.

A targeted audit of weighted/incomplete multiplicative-character and rational trace-function sums found the expected theme: power savings require usable structure in the summation set or coefficients (interval, bilinear/factorable, smooth/squarefree, or comparable hypotheses). No theorem was identified that turns mere repeated-residue multiplicity of the present exact first-exit block into cancellation of `(18)`. The durable contribution here is therefore the Mathia-specific **frontier reduction** from an apparently many-row incomplete interaction to one exact weighted relative-phase correlation, not a novelty claim for character sums or finite-field algebra.

## What is closed and what remains live

This finding closes one more interpretation of the accepted clue:

- repeated-residue **same-root** native cancellation is already impossible pointwise (`MC-492`);
- repeated-residue **completed cross-root** multiplicity tensorizes away (`MC-494`);
- repeated-residue **incomplete cross-root multiplicity** also creates no new conductor directions (this finding).

What remains live is narrower but genuine. The exact conductor projection `w(t)` may carry q-dependent endpoint, cutoff, pair-sieve, or source-coefficient information capable of correlating with `R_a(t)`. Proving a fixed conductor-power gain from that structure would be a real incomplete-transform mechanism. Alternatively, a source-derived q-dependent sign/complex phase inserted before `(14)` would prevent aggregation into nonnegative `A,B` and would also escape this obstruction.

A useful next test is therefore not to count more repeated-residue rows. It is to derive the exact structure of `w(t)` in the relevant q-range and ask whether its centered component can have an order-one negative correlation with `chi(1-t^{-2})` after all endpoint and reconstruction tariffs are restored.

## Boundaries and falsification tests

- **One repeated conductor residue.** The theorem concerns a block with `q\equiv a (mod p)`. Distinct conductor residues still supply distinct phase directions and are governed by `MC-490` and related findings.
- **Native common-sign first exit.** The nonnegative amplitudes in `(2)` are essential. A proved q-dependent signed or complex inner coefficient before aggregation is a genuine escape.
- **No completeness assumption.** Intervals, cutoffs and exact masks may be arbitrary and q-dependent; they are absorbed by zero-extension into `A,B`. What is not controlled is the resulting weighted bias `(18)`.
- **Character zeros retained.** Equations `(9)` and `(18)` are valid with the convention `chi(0)=0`; the rational form `(10)` is asserted only away from its poles/zeros.
- **Weighted bias not estimated.** Arbitrary nonnegative `w` can correlate strongly with `R_a`; no Burgess or Weil saving applies without additional source structure.
- **No global arithmetic conclusion.** There is no new bound for `M(x)`, no zero-free region and no RH consequence.

## Consequence for the accepted clue

The clue should no longer describe a genuinely incomplete repeated-residue transform as though multiplicity itself were the resource. Before any completion, all native repeated-residue rows already collapse to two conductor phases. The incomplete escape is exactly the centered source-weight correlation in `(19)`, or a new q-dependent signed/complex coefficient that prevents the collapse.

Thus the next admission gate is: **exhibit and estimate source-derived phase-selective structure in the conductor projection `w`, or derive a pre-aggregation q-specific sign/phase/modulus.** Repeating the same conductor residue more densely, by itself, is closed.