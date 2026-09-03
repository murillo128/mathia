# MC-037 — Pintz v2 repairs contour multiplicity bookkeeping but leaves Section 5 incomplete as printed

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `PARTIAL-AUDIT`, `NEEDS-AUDIT`, `NO-NOVELTY-CLAIM`.

## Claim

The 1 September 2026 `v2` revision of János Pintz's recent preprint `arXiv:2608.24878` materially changes the previously unaudited Section 5 input behind `MC-009`–`MC-012`. Relative to `v1`, the revised proof now separates contour pieces associated with zeros a fixed distance from `1` from pieces associated with zeros satisfying `eta<=delta`, and it explicitly inserts Carlson zero-density information to control the total contour length of the latter family.

That revision is a genuine improvement: it addresses the multiplicity/total-length bookkeeping that was not explicit in the `v1` route to the pointwise upper bound for `M(x)`. However, the revised Section 5 still does not justify its final bound as printed. There are two distinct issues.

First, the small-`eta` branch has an exact constant mismatch. From the new equation (5.9),

\[
M(J_{T^*}^{\prime\prime},u)
\ll
x^{1-\eta+\varepsilon\eta}
(T^*)^{4\delta+2\varepsilon-1}.
\tag{1}
\]

To replace the height exponent by the denominator power used in (5.10), namely `1-5 epsilon/2`, one needs

\[
4\delta+2\varepsilon\le \frac52\varepsilon,
\qquad\text{i.e.}\qquad
\boxed{\delta\le\varepsilon/8}.
\tag{2}
\]

The paper instead says only `delta<=epsilon/4`. With that stated choice, (1) gives at best the height power `1-3 epsilon`, not `1-5 epsilon/2`. This part is repairable by taking `delta<=epsilon/8` (or smaller), because `delta` is an auxiliary fixed cutoff.

Second, and more importantly, the large-`eta` branch still contains a missing implication. The revised equation (5.6) states for `eta>delta`

\[
M(J'_{T^*},u)
\ll
x^{1-\eta+\varepsilon\eta}
(T^*)^{\varepsilon+C\eta\log(1/(\varepsilon\eta))}
\log T^*
\ll x^{1-\delta/2}.
\tag{3}
\]

The second inequality does not follow from the first uniformly over the stated height range `T^*<=x^2`. Even discarding the positive `C eta log(1/(epsilon eta))` term, taking `eta` near `delta` and `T^*=x^2` leaves the upper-bound exponent

\[
1-(1-\varepsilon)\delta+2\varepsilon+o(1),
\tag{4}
\]

which is larger than `1-delta/2` whenever, for example, the later stated regime `delta<=epsilon/4` is used. Retaining the omitted positive term only worsens the comparison. Thus the displayed estimates alone do not provide the claimed fixed power saving for the `eta>delta` contour.

This is not a proof that Pintz's Theorems 2.1–2.2 are false. A localized reciprocal-zeta estimate stronger than the displayed (5.2), a density argument extended to the large-`eta` pieces, or another contour decomposition could repair the missing step. But such an input is not supplied in `v2`, so the current source still cannot be promoted from `NEEDS-AUDIT` to independently supported theorem-level evidence.

## 1. What changed from v1 to v2

The current arXiv record identifies `v1` as submitted 25 August 2026 and `v2` as revised 1 September 2026. The relevant Section 5 text changed materially.

In `v1`, equation (5.6) treated the dyadic contour contribution in one expression and then passed directly to the global maximum bound. In `v2`, Section 5 introduces a split:

- `J'_{T^*}` for pieces associated with zeros satisfying `eta>delta`, leading to the revised (5.6);
- `J''_{T^*}` for pieces associated with zeros satisfying `eta<=delta`.

For the second family the paper now invokes Carlson's density theorem and states that the total contour length in a dyadic height range is at most `T^(4 delta+epsilon)`. Combining this with the factor `1/|s|`, the reciprocal-zeta bound, and the contour integrand yields (1). That is exactly the kind of counting factor that must be present when a contour is assembled from many zero-associated vertical and horizontal pieces.

The revised argument therefore narrows the earlier audit surface: the small-`eta` multiplicity issue is no longer merely implicit. What remains is to verify the quantitative exponent bookkeeping and the separate large-`eta` estimate.

## 2. The small-eta exponent has a one-line repair

Equation (1) can be rewritten as

\[
M(J_{T^*}^{\prime\prime},u)
\ll
\frac{x^{1-(1-\varepsilon)\eta}}
{(T^*)^{1-4\delta-2\varepsilon}}.
\tag{5}
\]

The next displayed global bound (5.10) uses

\[
\frac{x}{x^{(1-\varepsilon)\eta}\gamma^{1-5\varepsilon/2}}.
\tag{6}
\]

Since the associated zero has ordinate comparable with `T^*` on the dyadic block, (5) implies the height exponent in (6) precisely when

\[
1-4\delta-2\varepsilon
\ge 1-\frac52\varepsilon,
\]

which is (2). Therefore `delta<=epsilon/8`, not merely `delta<=epsilon/4`, is the direct constant choice supporting the printed exponent.

This repair is compatible with the intended proof architecture. Making `delta` smaller only shrinks the zero family treated by the density estimate and does not conflict with the requirement that it be a fixed positive auxiliary cutoff. If an additional smallness condition is needed to absorb the `C eta log(1/(epsilon eta))` exponent for the small-`eta` family, `delta` can be reduced further as a function of the fixed outer `epsilon`.

The exact coefficient `5/2` is not itself mathematically important for Theorems 2.1–2.2; a reparameterized `1-O(epsilon)` exponent would also suffice. The point is narrower: the literal transition to the displayed (5.10) uses a stronger exponent than the stated `delta<=epsilon/4` choice supplies.

## 3. The large-eta step needs an additional argument

The more serious remaining issue is the last inequality in (3). The first part of (3) is the source's own bound after summing the `eta>delta` contour pieces. To deduce `x^(1-delta/2)` from it using only `T^*<=x^2`, one would need

\[
2\varepsilon
+2C\eta\log\frac1{\varepsilon\eta}
\le
(1-\varepsilon)\eta-\frac\delta2
\tag{7}
\]

uniformly for every relevant `eta>delta`.

Nothing in the displayed hypotheses establishes (7). Near the splitting boundary `eta=delta+o(delta)`, the later choice `delta<=epsilon/4` already makes the first term `2 epsilon` exceed the available `delta/2` margin before the positive `C eta log(...)` term is even considered. Shrinking `delta` does not fix this comparison; it reduces the `x`-saving at the same time.

This isolates the missing mathematical input very precisely. A valid repair must do at least one of the following:

1. replace (5.2) on the far-zero pieces by a stronger localized bound for `1/zeta(s)` whose height exponent is genuinely dominated by the fixed `x^{-eta}` saving;
2. use zero-density/counting information on the `eta>delta` family as well, rather than estimating the entire family by the displayed worst-case height power;
3. reorganize the contour so that the high-height factor is offset before the `x^(1-delta/2)` reduction.

Merely changing the constant relation between `delta` and `epsilon` cannot simultaneously justify the printed large-`eta` inference and the small-`eta` exponent in (5.10) from the displayed estimates.

## 4. Relation to the existing Pintz audit chain

The current `v2` does not make `MC-010`–`MC-012` obsolete. Direct inspection shows that the revision still prints:

- the signed `gamma` denominator in (2.10), despite the positive `|gamma|` definition elsewhere (`MC-010`);
- Theorem 6.1 with upper endpoint `Y e^3` followed by Corollary 6.3 with upper endpoint `Y` and no explicit constant rescaling (`MC-010`);
- the loss of the linear shifted-height factor between the two bounds in (6.23) (`MC-011`);
- `epsilon'=epsilon/9` in (7.7) followed by use of the pointwise cap down to `Y^(1-epsilon/8)` in (7.8) (`MC-012`).

The explicit repairs in `MC-010`–`MC-012` therefore remain relevant to the latest version. The new information in this finding is orthogonal: `v2` has strengthened the previously un-audited Section 5 contour bookkeeping, but its revised pointwise-upper-bound route still contains the small constant slip (2) and the unresolved large-`eta` implication (3).

## 5. Prior art and novelty assessment

The primary source is János Pintz, *Oscillation of partial sums of the Möbius function and zeros of Riemann's zeta function*, arXiv:2608.24878v2, revised 1 September 2026. The version history and both HTML versions are public at:

- https://arxiv.org/abs/2608.24878
- https://arxiv.org/html/2608.24878v1
- https://arxiv.org/html/2608.24878v2

Carlson's density theorem and the Huxley–Hooley–Ramachandra contour framework are classical inputs already cited by Pintz. No novelty is claimed for those methods or for the theorem Pintz states.

The Mathia contribution is a version-aware proof audit: identify what `v2` materially repaired relative to `v1`, verify the exact exponent required by the new density branch, and isolate the remaining inference that is not supplied by the displayed estimates. A targeted search found no public erratum or independent proof discussion resolving this `v2` Section 5 step as of 3 September 2026.

## 6. Boundaries and falsification tests

This finding does not refute Pintz's main theorem. It asserts only that the current printed derivation is incomplete at a specific point.

The large-`eta` objection is falsified if one can derive the second inequality in (3) uniformly from a stated theorem already available under Pintz's hypotheses, with all dependence on `epsilon`, `delta`, `eta`, and `T^*` made explicit. The small-`eta` constant objection is falsified if (5.9) contains an additional saving not displayed in `v2` or if the `1-5 epsilon/2` exponent is not actually used downstream.

Conversely, simply observing that all constants are auxiliary does not answer the large-`eta` objection: the displayed bound has a height-growth term whose exponent competes directly with the fixed `x`-power saving.

## Consequence for the research line

`MC-009` should remain `NEEDS-AUDIT`. The current `v2` is stronger than the version originally audited because it explicitly brings zero-density information into the Section 5 contour-length calculation, but it does not yet supply a complete verified bridge from that contour to the pointwise upper bound used in Section 7.

For the Möbius Cancellation program, this sharpens the external dependency rather than changing the mathematical target. Pintz's mean-absolute statistic remains a potentially valuable RH-complete `L^1` carrier, but any use of it as a theorem-level bridge should either supply the missing large-`eta` contour estimate or wait for a corrected source version.