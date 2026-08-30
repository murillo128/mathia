# WI-042 — Yang's public band ledger is the forbidden across-family Cauchy route, not the printed shift-only consumer

**Status:** `PRIOR-ART-AUDIT + EXACT-DERIVED + DECISIVE-NEGATIVE + NEEDS-AUDIT`. This finding does **not** refute the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes a narrower but important repair route left open by WI-037--WI-041: the only public executable ledger in the pinned Yang reproduction tree that quantitatively consumes the middle-band cell deviations, `scripts/g1_ledger.py`, applies exactly the **global/across-cell Cauchy--Schwarz** that the paper itself says is never used because its Poisson floor is `50--60x` over budget. The script labels that operation `[global]`, accumulates a cellwise square function `D = sum_cell (Acell-MTcell)^2`, and forms `L_CS=sqrt(W2)sqrt(D)`. Its own `F-A3` "theorem-chain proxy" still depends on the empirically computed `D` and is therefore not an asymptotic theorem replacing the missing shift-only welding consumer.

The exact dispersion swaps in `t2_swaps.py` remain useful and may still permit a different proof: they can regroup unweighted quadratic cell expressions into structured twin-shift families before the dangerous inequality is applied. What is now ruled out is treating `g1_ledger.py` itself, or the standard MRT/BDH input applied after its global cellwise square, as the missing theorem bridge. A valid repair must perform an **exact shift-first regrouping of the actual outer weights** and apply Cauchy--Schwarz only after that regrouping, or prove a genuinely stronger cellwise square-function theorem with a budget below the Poisson floor.

## 1. Exact source conflict

The pinned source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

In `paper.tex`, subsection `Covered zone, middle band, bridge and aggregation`, the authors first state the exact dispersion-swap lemma, the fixed-window bridge, and the structured-to-full aggregation lemma. Immediately after those lemmas the paper says:

> The band consumer applies a single Cauchy--Schwarz in the shift variable only (any Cauchy--Schwarz across the family pays its Poisson floor, measured 50--60x over budget, and is never used).

The same paragraph introduces the welding weight

\[
w_k(n)=\sum_{m\in I(n)}\Lambda(m)\Lambda(m-rk)
\tag{1}
\]

and says that the glue closes by exact factorization of main terms, Abel summation on the major arcs, and MRT envelopes on the minor arcs. WI-037 already showed that the last citation is not, by itself, a theorem for the new weighted coefficient; WI-041 then showed that moving interval endpoints can be absorbed into a maximal MRT norm, leaving the actual outer aggregation as the load-bearing question.

Now compare this printed contract with the public quantitative ledger. The docstring of `scripts/g1_ledger.py` defines cells

\[
c=(b_1,b_2,j,\mathrm{block}),
\]

kernel-weighted cell masses

\[
\widetilde A(c),\qquad \widetilde{MT}(c),
\]

and slow weights `wtilde(c)`, then states literally

\[
\widetilde D
 =\sum_c(\widetilde A(c)-\widetilde{MT}(c))^2
\]

and

\[
\boxed{
\left|\sum_c \widetilde w(c)
 (\widetilde A(c)-\widetilde{MT}(c))\right|
\le
\sqrt{\sum_c\widetilde w(c)^2}
\sqrt{\sum_c(\widetilde A(c)-\widetilde{MT}(c))^2}.
}
\tag{2}
\]

The source comment after (2) is `[global]` / `全局`. This is not Cauchy--Schwarz in a single shift variable after the exact structured regrouping; it is Cauchy--Schwarz over the cell family itself.

Primary source:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/g1_ledger.py

## 2. The executable gate really consumes the global cell norm

The implementation is as explicit as the docstring. For every admissible `(b1,b2)` pair it constructs fine cells indexed by `(j,block)`, computes

```text
dev = Acell - MTc
```

and accumulates

```text
tot['D']  += sum(dev * dev)
tot['W2'] += sum(wt * wt)
```

across **all** modulus pairs. At the end it evaluates

```text
LCS = sqrt(led['W2']) * sqrt(led['D'])
```

against the pre-registered `0.0383` gate. Thus the executable quantity is exactly (2).

The script also tries a coarser granularity by summing the `j` cells first. But it then repeats the same construction over coarse objects `(b1,b2,block)`:

\[
L_{CS}^{\rm coarse}
=\sqrt{\sum_{b_1,b_2,B}w_{b_1,b_2,B}^2}
 \sqrt{\sum_{b_1,b_2,B}D_{b_1,b_2,B}^2}.
\tag{3}
\]

Equation (3) is still an across-family Cauchy--Schwarz. Summing `j` before squaring changes the numerical floor; it does not turn the consumer into the printed shift-only argument.

This distinction is not semantic. The paper explicitly warns that the familywise square norm carries a deterministic Poisson/diagonal floor far above the admissible remainder budget. Therefore neither (2) nor (3) can be silently identified with the paper's stated proof route.

## 3. `F-A3` is a diagnostic proxy, not the missing theorem

The strongest apparently theorem-facing gate in `g1_ledger.py` is `F-A3`. The script defines

\[
D_{\rm thm}
=
\mathrm{diag}
+C_{\rm sel}\,|D-\mathrm{diag}|,
\qquad C_{\rm sel}=4,
\tag{4}
\]

then reports

\[
L_{\rm thm}
=\sqrt{\sum w^2}\sqrt{D_{\rm thm}}.
\tag{5}
\]

But (4) uses the **measured finite-height value `D` itself**. The code line is

```text
tot['Dthm'] += sum(Dgcell)
    + C_SEL * abs(sum(dev * dev) - sum(Dgcell))
```

so `F-A3` does not derive an asymptotic upper bound for the off-diagonal dispersion from MRT; it inserts the observed off-diagonal amount `|D-diag|` and multiplies it by a Selberg-type constant. Its own docstring calls the quantity a "theorem-chain proxy". That is a useful falsification/calibration diagnostic, but it cannot certify that the asymptotic Yang band remainder is `o(1)` or below a prescribed `R`-budget.

Likewise, `F-A2` is explicitly a **floor**

\[
L_{\rm floor}=\sqrt{\sum w^2}\sqrt{\mathrm{diag}},
\tag{6}
\]

not a saving. The public ledger therefore cleanly separates numerical feasibility from proof: its only direct rigorous inequality is the global Cauchy (2), while its sharper consumed value is empirical/proxy-level.

## 4. Why MRT structured `L^2` does not automatically turn (2) into the printed consumer

MRT Theorem 1.3(i), as audited in WI-034, gives the long-shift twin-prime deviation control. After the good/bad-shift conversion and the divisor-multiplicity argument one has schematically

\[
\sum_{q\in\mathcal Q}\sum_{k\le K_q}
|D(qk)|^2
\ll_A H X^2(\log X)^{-A}.
\tag{7}
\]

WI-041 further upgrades the individual shift deviation to a maximal-over-interval norm without changing the power-scale budget.

Equation (7) is a statement after the arithmetic object has been organized by **structured shift**. Equation (2) asks instead for a square sum after organizing by **cells**. There is no abstract implication from one organization to the other. In the simplest finite model, let each shift `h` have two cells with errors

\[
\delta_{h,1}=u_h,
\qquad
\delta_{h,2}=-u_h.
\tag{8}
\]

Then every grouped shift deviation can vanish while

\[
\sum_{h,a}|\delta_{h,a}|^2
=2\sum_h|u_h|^2
\tag{9}
\]

is arbitrarily large. Hence a shift-level `L^2` theorem does not, from information theory alone, control an arbitrary finer cellwise square function.

This toy obstruction must be interpreted carefully in the Yang setting. The exact `t2_swaps.py` identities give **additional algebra**: certain unweighted sums of cell squares can be expanded into linear weighted twin-shift families. So (8)--(9) does *not* prove that the real Yang cell dispersion is uncontrollable. It proves the narrower point needed here: one must actually use those swap identities and the outer weights **before** asserting that MRT (7) controls the consumer. The global Cauchy ledger (2) does not perform that shift-first proof step.

## 5. Public-tree audit: the shift-only consumer is not implemented elsewhere

A recursive inventory of the pinned reproduction commit contains the relevant analytic/helper files

```text
scripts/g1_ledger.py
scripts/t2_swaps.py
pipeline/face_dispersion.py
scripts/m4_band_split.py
```

but no separate `welding`, `band_consumer`, or rounds-38--40 proof artifact. `t2_swaps.py` supplies finite exact identities and the fixed-window bridge. `pipeline/face_dispersion.py` is a finite-height numerical face/calibration. `m4_band_split.py` is a numerical model gate. The paper refers to an archive/memo for some analytic glue steps, but that proof source is not present in the public reproduction tree.

`REPRODUCTION.md` is consistent with this reading: it presents `g1_ledger.py` as a helper/calibration component rather than an end-to-end formal proof of the one-sided arithmetic theorem. The source conflict is therefore not an accusation that the script violates its own stated role. The consequence is evidentiary: **the public package currently contains no executable or written derivation of the shift-only consumer that the theorem statement needs.**

The repository has had no commit after `d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8` as of the 30 Aug 2026 audit, so this gap has not been repaired by a later public revision.

## 6. Prior-art audit: ordinary BDH/Mikawa technology is not a drop-in replacement

A targeted audit checked the nearby variance literature rather than inferring a theorem from the `g1_ledger.py` comment "BDH/Mikawa allows smooth weights".

Classical Barban--Davenport--Halberstam controls mean squares of **first-order prime-counting errors in arithmetic progressions**. The short-interval variants likewise require explicit ranges in interval length and modulus. MRT 2019 is the directly relevant theorem for the binary shifted correlation and is already the stronger input used in (7). None of these statements, as published, is the four-index assertion

\[
\sum_{b_1,b_2,j,B}
|\widetilde A_{b_1,b_2,j,B}
-\widetilde{MT}_{b_1,b_2,j,B}|^2
\le \text{Yang budget}
\tag{10}
\]

with the Yang kernel, moving cell geometry, and power-growing reduced coefficients.

A search for the `Mikawa` reference suggested by the helper comment locates work on primes/almost-primes in short intervals and arithmetic progressions, exponential sums over primes in progressions, and Bombieri--Vinogradov variants, but the pinned Yang paper does not cite a Mikawa theorem at this point and the public tree contains no memo identifying one with hypotheses matching (10). This is not used as a claim that no theorem in the literature could imply (10); it means the current source does not provide such a theorem.

Recent general BDH work also emphasizes that variance theorems for a new sparse/general sequence require independent short-interval and progression-distribution hypotheses rather than following from a pointwise envelope. This is fully consistent with the obstruction already recorded in WI-037.

Relevant primary/secondary anchors:

- K. Matomäki, M. Radziwiłł, T. Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. LMS 118 (2019), 284--350, arXiv:1707.01315.
- classical Barban--Davenport--Halberstam theorem and its short-interval variants; these concern prime-counting errors in arithmetic progressions, not (10).
- A. J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, J. London Math. Soc. (2025), DOI `10.1112/jlms.70293`; relevant only as context on the extra distribution hypotheses needed for general/sparse sequences, not as a theorem consumed here.

No novelty or priority claim is made for any of those results, for Cauchy--Schwarz, or for the elementary cancellation model (8).

## 7. What this resolves from WI-041

WI-041 ended with a precise fork: perhaps the Yang outer normalization consumes the **global** structured-shift budget (7), in which case no `sqrt(r)` loss is needed, or perhaps the proof effectively requires a progression-wise/cellwise budget that MRT does not supply.

The public executable ledger answers that fork for **that ledger path**:

\[
\boxed{
\texttt{g1\_ledger.py}
\text{ consumes a global cell/family square norm, not the shift-only norm.}
}
\tag{11}
\]

Therefore the ledger does not realize the good branch of WI-041. Its global square is precisely the route the paper calls over-budget. This is a decisive negative result for using the public ledger as the missing analytic bridge.

It does **not** answer the broader mathematical fork for a yet-unwritten shift-first derivation. The exact swap identities could still enable

\[
\sum_c w_c\delta_c
\quad\longrightarrow\quad
\sum_h a_h D(h)
+\text{controlled main/boundary terms}
\tag{12}
\]

with a coefficient sequence `a_h` whose norm is compatible with MRT. Equation (12), with all weights and normalization explicit, is now the shortest credible repair target.

## 8. Consequence for the one-sided fourth-moment program

The deterministic part of the one-sided route has become increasingly rigid through WI-028 and WI-030--WI-033, and WI-034/038/041 have shown that several apparent arithmetic nuisances are not fundamental. The remaining arithmetic interface should now be stated as

\[
\boxed{
\text{exact cell swaps}
\to
\textbf{shift-first weighted regrouping}
\to
\text{MRT structured/maximal }L^2
\to
\text{band }o(1)
\to
R(1).
}
\tag{13}
\]

The bold arrow is not present in the public proof package. The already-implemented alternative

\[
\text{cells}
\xrightarrow{\text{global family CS}}
\sqrt{\sum w_c^2}\sqrt{\sum\delta_c^2}
\tag{14}
\]

is explicitly acknowledged by the source as suffering the unaffordable Poisson floor.

Accordingly, further work should **not** spend effort sharpening `F-A1/F-A3` finite-height calibrations unless they are accompanied by a proof of (10). The higher-value task is algebraic: derive (12) from `t2_swaps.py` with the actual kernel/block weights, or prove that no coefficient norm compatible with the source budget emerges. Either result would materially change the status of the `0.6916` candidate.

## 9. Decisive promotion / falsification test

Narrow or retire this finding if a public proof supplies one of the following.

1. **Shift-first repair.** An exact identity reducing the normalized Yang band error to (12), with one shift-indexed coefficient after all `(b1,b2,j,block)` multiplicities are collected, followed by a norm estimate that lets WI-034/WI-041 close the result using only one Cauchy--Schwarz in `h`.
2. **True cellwise theorem.** A primary BDH/Mikawa/MRT-type theorem whose stated hypotheses match the Yang kernel-weighted cell family and prove (10) at the required asymptotic scale, including the moving endpoints and power-sized reduced coefficients.
3. **Equivalent dispersion argument.** A bilinear/large-sieve estimate that bypasses both (12) and (10) while yielding the same normalized `o(1)` band remainder without paying the paper's recorded Poisson floor.

Conversely, if an exact derivation of the shift-first coefficient in (12) has `L^2` or dual norm at least as large as the `F-A2` Poisson floor, then the current one-sided fourth-moment welding architecture would face a stronger genuine barrier rather than merely a missing public write-out.