# MC-462 — Anchor-fibre support ceiling forces a residual-range gate

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The fixed-anchor energy gain isolated in `MC-461` has a sharp coefficient-independent **support-size gate** before the surviving `B_beta` amplitude is even considered.

Keep the prime-conductor setting of `MC-461`, fix one outer pair and one gcd sector, and write

\[
s=d s_0,\qquad r_2=d t,\qquad h_0=d h_1,\qquad g_0=(h_1,t),\qquad t_0=t/g_0.
\tag{1}
\]

Assume `t<p`, so `MC-461` gives the exact anchor-fibre equivalence

\[
U_s=U_{s'}
\quad\Longleftrightarrow\quad
s_0\equiv s'_0\pmod{t_0}.
\tag{2}
\]

Let the residual coefficient block satisfy

\[
\beta_s=0\qquad(s>S).
\tag{3}
\]

Then every represented source anchor contains at most

\[
\boxed{
N_U\le 1+\frac{S}{d t_0}
      =1+\frac{S(h_1,t)}{r_2}
}
\tag{4}
\]

admissible residual divisors before any coefficient cancellation is used.

After all collisions with the reciprocal shift

\[
D_s=\delta s_0^{-1}\pmod p
\tag{5}
\]

are aggregated into a source weight `W(U,D)`, the participation ratio from `MC-461`,

\[
R_{\rm eff}(W)=\frac{\|W\|_1^2}{\|W\|_2^2},
\tag{6}
\]

satisfies the universal support bound

\[
\boxed{
R_{\rm eff}(W)
\le \#\operatorname{supp}W
\le R_U\left(1+\frac{S(h_1,t)}{r_2}\right),
}
\tag{7}
\]

where `R_U` is the number of represented anchors.

But the bare fixed-anchor estimate of `MC-461` beats the pointwise `H||W||_1` bound only if

\[
R_{\rm eff}(W)>R_U\frac pH.
\tag{8}
\]

Therefore the entire bare anchor-slicing route is impossible in this sector whenever

\[
\boxed{
1+\frac{S(h_1,t)}{r_2}\le \frac pH.
}
\tag{9}
\]

Equivalently, away from the endpoint where the additive `1` matters, a **necessary** range condition for any gain from the `MC-461` source-frame moment is

\[
\boxed{
S H\,(h_1,t)\gtrsim p r_2.
}
\tag{10}
\]

In the generic coprime normalized-shift sector `(h_1,t)=1`, this reduces to

\[
\boxed{S H\gtrsim p r_2.}
\tag{11}
\]

Thus the anchor compression found in `MC-461` is not free analytic leverage. It can lower the ambient start count only when the same arithmetic sector also contains enough residual-divisor support **per anchor** to pay the remaining `p/H` shift tariff. Large `(h_1,t)` helps twice: it reduces `t_0` and correspondingly packs more admissible residual divisors into one anchor fibre. When `(h_1,t)=1`, the fibre spacing is exactly `r_2/d` in `s_0`, or `r_2` in `s`, so a short residual block cannot populate the fibre densely enough.

This is a necessary condition only. Satisfying `(9)` in the opposite direction does not prove useful weight spread, does not control cancellations among `beta_s`, and does not handle the surviving aligned amplitude

\[
\overline{B_\beta(C_s+r_1s_0j)}.
\tag{12}
\]

No conductor-power saving, no bound for `M(x)`, and no RH consequence follows.

## 1. Exact fibre cardinality from the anchor congruence

Fix one represented anchor `U`. By `(2)`, all residual divisors contributing to that anchor have

\[
s_0\equiv a\pmod{t_0}
\tag{13}
\]

for one unit residue class `a`. Since `s=d s_0` and `s\le S`,

\[
1\le s_0\le S/d.
\tag{14}
\]

An interval of length `S/d` contains at most `1+S/(d t_0)` integers in one residue class modulo `t_0`. The additional admissibility conditions `(s_0,t)=1`, `(s,p)=1`, or support restrictions inside the block can only remove terms, so `(4)` follows.

Using `r_2=d t` and `t_0=t/(h_1,t)`,

\[
d t_0
=d\frac{t}{(h_1,t)}
=\frac{r_2}{(h_1,t)},
\tag{15}
\]

which gives the second form in `(4)`.

This count does not assume that the reciprocal shifts `D_s` are distinct. If two residual divisors collide in `D`, their coefficients are first aggregated into the same source point `(U,D)`, which only decreases the support cardinality relevant below.

## 2. Participation cannot exceed source support

For any finite complex vector `W`, Cauchy gives

\[
\|W\|_1^2
\le
\#\operatorname{supp}(W)\,\|W\|_2^2.
\tag{16}
\]

Hence

\[
R_{\rm eff}(W)
\le \#\operatorname{supp}(W).
\tag{17}
\]

If the staged family uses `R_U` represented anchors, `(4)` bounds each anchor fibre by the same sector envelope, so

\[
\#\operatorname{supp}(W)
\le
R_U\left(1+\frac{S}{d t_0}\right).
\tag{18}
\]

This proves `(7)` without assumptions on signs, phases, magnitudes, or equidistribution of the residual coefficients.

The estimate is intentionally one-sided. Sparse `beta_s`, destructive aggregation at repeated `D`, or concentration on a few source points can make `R_eff` much smaller than `(7)`; no coefficient hypothesis available here forces near-equality.

## 3. Comparison with the exact `MC-461` shift moment

For one common interval `J` of length `H`, `MC-461` proves

\[
\sum_{D\bmod p}|K_J(U,D)|^2\le pH
\tag{19}
\]

for each fixed anchor and therefore

\[
\left|\sum_{U,D}W(U,D)K_J(U,D)\right|
\le
\|W\|_2\sqrt{R_U pH}.
\tag{20}
\]

The pointwise comparison is

\[
\left|\sum_{U,D}W(U,D)K_J(U,D)\right|
\le H\|W\|_1.
\tag{21}
\]

Squaring the strict inequality `(20)<(21)` gives exactly the `MC-461` gate

\[
R_{\rm eff}(W)>R_U p/H.
\tag{22}
\]

Combining `(7)` and `(22)` proves that no gain is possible when `(9)` holds. Importantly, this is not a failure of character orthogonality: the complete-shift second moment is already optimal at the level used here. The obstruction is simply that the arithmetic source image does not contain enough points inside each anchor slice to exploit that ambient energy.

The normalized-shift gcd now has a precise role. From `(4)`, the maximal number of residual source points in one anchor is proportional to `(h_1,t)`. When that gcd is `1`, anchor compression is strongest only because the anchor classes are spaced by the full modulus `t`; the same spacing makes each fibre sparse. A large gcd compresses the number of anchors by the reciprocal factor and simultaneously increases the maximal occupancy of each anchor. The two effects are the same quotient geometry viewed from opposite sides.

## 4. What this does and does not say about well-factorability

The argument uses only the residual support bound `(3)`. It does **not** assert that a standard well-factorable component is uniformly distributed across its support, nor that its coefficients have comparable size. In particular, standard factorability supplies an auxiliary convolution representation, but the present estimate needs actual participation after the map

\[
s\mapsto(U_s,D_s).
\tag{23}
\]

A proof that invokes factorability only to bound `|beta_s|` from above cannot reverse `(7)` into a useful lower bound for `R_eff`.

This sharply separates two questions that were still mixed in the accepted clue after `MC-461`:

1. **geometric admissibility:** is the residual range large enough that a fixed anchor could possibly contain more than `p/H` effective shifts? This is answered by `(9)`--`(10)`;
2. **coefficient/amplitude dispersion:** in the admissible sectors, do the actual factorable coefficients and the surviving `B_beta` amplitude produce enough effective spread, and can that spread survive the first oscillatory estimate? This remains open.

A sector failing the first test should no longer be sent through a more elaborate weighted completion argument: no choice of coefficients can make the bare `MC-461` participation ratio large enough there.

## 5. Prior-art and novelty boundary

The residue-class count in `(4)`, the support inequality `(16)`, and the comparison of `(20)` with `(21)` are elementary. No novelty is claimed for any of them, for participation-ratio bounds, or for the complete shifted-character moment inherited from `MC-461`.

The current well-factorable/dispersion literature audited in `MC-456` remains the closest positive neighboring framework. Pascadi's triply-well-factorable arguments and Yang's 2026 convolution-type Bombieri--Vinogradov theorem exploit factor blocks that survive into reciprocal/Kloosterman-type oscillation before positive closure. Those works provide no automatic lower bound for the branch-specific participation ratio `(6)` after the map `(23)`; their successful modulus geometry is different from the fixed external character conductor here. Shparlinski-type bilinear reciprocal character sums likewise provide estimates once a sufficiently populated reciprocal family with admissible coefficient structure has been identified; they do not create the missing source points.

A targeted literature check on 22 September 2026 therefore changes no status: the analytic languages are established prior art, while `(9)` is only the elementary necessary range condition obtained by applying that source-size logic to the exact `MC-461` anchor quotient. Absence of an identical formulation in the checked literature is not treated as novelty evidence.

## Boundaries and falsification tests

- **`t<p` is load-bearing for the exact anchor partition.** When `t>=p`, reduction `m_s mod p` can merge distinct `m_s mod t` classes, producing larger `U` fibres than `(2)` alone describes. That regime needs a separate collision count before `(4)` can be used unchanged.
- **The result gates only the bare `MC-461` slicing estimate.** A stronger joint estimate that exploits the full aligned amplitude in `(12)` may use information not summarized by a scalar weight `W(U,D)` and is not ruled out by `(9)`.
- **Support is not participation.** Passing `(9)` in the favourable direction is not sufficient: `R_eff` may still be small because the coefficients are sparse or uneven, or because several residual divisors collide and cancel after aggregation.
- **The additive `1` matters near very short fibres.** The scale form `(10)` is asymptotic shorthand; the exact obstruction is `(9)`.
- **Variable interval lengths remain outside the calculation.** The comparison uses the common-`H` source moment of `MC-461`. Any variable-length reduction must preserve the same fibre count or pay its own maximal/smoothing cost.
- **Large gcd sectors may be rare.** The finding identifies `(h_1,t)` as the only source of fibre compression in this quotient, but it does not sum those sectors or show that the favourable gcds carry enough outer weight.
- **No statement about Möbius cancellation is obtained.** This is a source-budget classification inside one staged auxiliary representation.

## Consequence for the live clue

The accepted staged q-vdC clue can now discard every `t<p` gcd sector satisfying `(9)` before attempting any delicate weighted completion. The live factor-specific branch is narrower: first isolate sectors with

\[
1+\frac{S(h_1,t)}{r_2}>\frac pH,
\tag{24}
\]

then determine whether their actual residual weights have participation comparable to the available support and whether the aligned `B_beta` amplitude preserves a gain.

The next useful calculation should therefore not ask generically whether `U_s` is low-dimensional. It should price the distribution of the favourable gcd sectors and the actual weighted participation inside them. If those sectors are too sparse after the outer `(r,r')` and source-depth sums, the bare anchor-slicing escape closes; if they carry enough mass, the surviving aligned amplitude becomes the first genuinely new analytic object that still needs a structured reciprocal estimate.