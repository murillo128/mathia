# WI-037 — the covered-zone Gallagher collar is automatic at the MRT scale

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding closes one of the explicit audit gates left open by WI-035 for the Yang--Yang one-sided fourth-moment route. Under the public collar convention and the same covered-zone hypothesis needed to invoke Matomäki--Radziwiłł--Tao, the Diophantine separation hypothesis used in WI-035 is automatic: the apparently dangerous dilation factors cancel against the matched physical lengths of the two prime sums. The same calculation also gives the polylogarithmic phase-variation hypothesis needed for the reduced-denominator Siegel--Walfisz major-arc law.

This does **not** establish the one-sided fourth-moment theorem or change Mathia's current unconditional simple-critical proportion. It applies only on the covered zone where both prime-sum lengths are in the MRT range. The uncovered/low-zone ledger, welding/Abel glue, dispersion normalization and final asymptotic remainder remain separate live gates.

## 1. Source boundary

The pinned source is

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

In `paper.tex`, subsection `Covered zone, middle band, bridge and aggregation`, Yang--Yang write

\[
S_i(\alpha)=\sum_{m\sim M_i}\Lambda(m)e(b_i m\alpha)
\]

and state four archived discharge lemmas: a reduced-denominator major-arc law, simultaneous near-major classification, dilation transfer, and a **smoothing-collar lemma aligning the Gallagher width**. The same subsection invokes Matomäki--Radziwiłł--Tao only on windows

\[
M_i\ge X^{8/33+\varepsilon}
\tag{1}
\]

(up to the source's harmless dyadic rescaling) and calls the resulting region the covered share.

The public reproduction code makes the collar normalization explicit. In `pipeline/common.py`, `arc_quality(gam,P,wid)` declares a major arc when

\[
|q\gamma-a|\le \mathrm{wid},\qquad q\le P,
\tag{2}
\]

while `pipeline/face_arcs.py` sets

\[
\mathrm{wid}_i=\frac{P}{Y_i},
\tag{3}
\]

with `Y_i` the physical span after dilation. Thus the actual rational approximation is

\[
\boxed{
\left|\gamma_i-\frac{a_i}{q_i}\right|
\le \frac{P}{q_iY_i},
\qquad q_i\le P.
}
\tag{4}
\]

For the analytic tail the paper takes `P=(log X)^B`; the finite-height face uses `P=40`. The argument below is uniform for either choice and needs only `P=X^{o(1)}`.

No novelty is claimed for Gallagher smoothing, rational separation, Siegel--Walfisz, or the MRT theorem. The point is to discharge the source-specific parameter compatibility that WI-035 had deliberately left conditional.

## 2. Matched physical scale removes the dilation factors

Write

\[
\gamma_1=b_1\alpha,
\qquad
\gamma_2=b_2\alpha.
\tag{5}
\]

The locked fourth-moment cells compare the two prime sums at the same physical product scale. Let

\[
Y_i=b_iM_i
\tag{6}
\]

be their physical lengths. After the standard dyadic localization, the two locked products are comparable with an absolute constant:

\[
C^{-1}Y_1\le Y_2\le CY_1.
\tag{7}
\]

For the exact locked-center model one has `Y_1=Y_2`; retaining `C` only makes the audit robust to the source's harmless smooth/dyadic collars.

Assume (4). Since

\[
b_2\gamma_1=b_1\gamma_2
\tag{8}
\]

exactly,

\[
\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
\frac{P b_2}{q_1Y_1}
+
\frac{P b_1}{q_2Y_2}.
\tag{9}
\]

Multiply by `q_1q_2` and use `q_i<=P`:

\[
q_1q_2\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
P^2\left(\frac{b_2}{Y_1}+\frac{b_1}{Y_2}\right).
\tag{10}
\]

The matched-scale relation now cancels the apparently dangerous large dilations. From `Y_1=b_1M_1`, `Y_2=b_2M_2` and (7),

\[
\frac{b_2}{Y_1}
=\frac{Y_2}{Y_1}\frac1{M_2}
\le \frac{C}{M_2},
\qquad
\frac{b_1}{Y_2}
=\frac{Y_1}{Y_2}\frac1{M_1}
\le \frac{C}{M_1}.
\tag{11}
\]

Therefore

\[
\boxed{
q_1q_2\left|
\frac{b_2a_1}{q_1}-\frac{b_1a_2}{q_2}
\right|
\le
CP^2\left(\frac1{M_1}+\frac1{M_2}\right).
}
\tag{12}
\]

On the covered zone (1), with `P=(log X)^B`, the right side is

\[
O\!\left((\log X)^{2B}X^{-8/33-\varepsilon}\right)=o(1).
\tag{13}
\]

Hence for all sufficiently large `X` it is strictly below `1`. But if the rational number in (9) is nonzero, after putting it over the denominator `q_1q_2` its absolute value is at least `1/(q_1q_2)`. Thus (12)--(13) force

\[
\boxed{
\frac{b_2a_1}{q_1}=\frac{b_1a_2}{q_2}.
}
\tag{14}
\]

Equation (14) is exactly the separation conclusion that WI-035 previously obtained under the explicit collar hypothesis

\[
b_2\delta_1+b_1\delta_2<\frac1{q_1q_2}.
\]

The public Gallagher-width collar plus the MRT covered-zone lower bound on `M_i` prove that hypothesis automatically. No independent `b`-uniform Diophantine lemma is needed.

## 3. The reduced-denominator major-arc phase condition is automatic too

WI-035's reduced-denominator Siegel--Walfisz step needs, for each prime sum, a polylogarithmic bound on the phase variation

\[
|\eta_i|M_i,
\qquad
\eta_i:=\gamma_i-a_i/q_i.
\]

From (4) and `Y_i=b_iM_i`, one gets directly

\[
\boxed{
|\eta_i|M_i
\le \frac{P}{q_ib_i}
\le P.
}
\tag{15}
\]

Thus for `P=(log X)^B` the partial-summation cost is polylogarithmic, exactly the hypothesis used in WI-035 to derive

\[
S_i(\alpha)
=
\frac{\mu(q_i')}{\varphi(q_i')}V_i(\eta_i)
+O\!\left(M_i e^{-c\sqrt{\log M_i}}\right),
\qquad
q_i'=\frac{q_i}{(q_i,b_i)},
\tag{16}
\]

uniformly after denominator contraction. Again the physical dilation does not create an extra loss; the `b_i` in the collar width cancels against the prime-sum length.

This also explains why the fixed-height face in `pipeline/face_arcs.py` is numerically well behaved even though it tests genuinely dilated spectra: its `wid_i=P/Y_i` convention has already normalized to physical length before any rational classification is made.

## 4. Consequence for the simultaneous-major classification

Once (14) holds, WI-035's exact denominator argument applies without any remaining collar assumption. If `g=(b_1,b_2)` and `d` is the reduced common rational center, then

\[
d\mid b_1q_1,
\qquad
d\mid b_2q_2,
\]

hence

\[
\boxed{
d\le \min(Pb_1,Pb_2,P^2g).
}
\tag{17}
\]

This is the simultaneous-major denominator shape printed in the Yang--Yang paper. Therefore, **on the covered MRT zone**, the chain

\[
\text{Gallagher collar}
\longrightarrow
\text{rational coalescence}
\longrightarrow
\text{denominator contraction}
\longrightarrow
\text{ordinary Siegel--Walfisz major arc}
\]

is now self-contained from the public parameters.

## 5. What this closes and what remains live

WI-035 listed as its first open gate: verify that the source's actual smoothing/Gallagher collars imply the rational-separation condition and the phase-variation bound needed by the major-arc law. Equations (12)--(15) close that gate **for the covered zone**.

The important structural point is that large `b_i` are not themselves an obstruction. A naive estimate can appear to lose a factor `b_1+b_2`; the locked physical-scale identity converts those factors into `1/M_1+1/M_2`, and the same `M_i>=X^{8/33+epsilon}` hypothesis already required by MRT then gives a power saving over every polylogarithmic arc cutoff.

The following remain outside the conclusion:

- **Uncovered / low zone.** If one of the `M_i` falls below the MRT threshold, (13) is no longer supplied by this argument. The paper's statement that covered-zone, band and low-zone deviations enter `o(1)` still needs an asymptotic ledger; finite-height prices are not a substitute.
- **Welding/glue.** Exact main-term factorization, Abel summation against the welding weight, and the use of MRT Proposition 5.4 / Appendix A on minor arcs remain to be audited at the source's normalization.
- **Dispersion swaps and consumer normalization.** The exact conversion from the prime-correlation variance to the `R(1)` remainder must still be checked end to end.
- **Finite deterministic remainder.** WI-030/WI-031 remove the continuum-core and infinite-gamma-tail conceptual gaps, but the finite interval/zone replay still needs fail-closed bounds.
- **Higher-moment tower.** Nothing here repairs WI-003's separate global-`ell_1` truncation defect in the fifth/sixth-moment route.

Thus WI-028's potentially high-leverage one-sided fourth-moment route remains unproved, but one of its apparently source-specific analytic lemmas has disappeared from the genuine proof burden.

## 6. Prior-art / novelty audit

Classical / literature-backed inputs:

- Gallagher/circle-method major-arc smoothing at physical width `1/Y`;
- elementary rational separation: two distinct rationals with denominators `q_1,q_2` differ by at least `1/(q_1q_2)`;
- Siegel--Walfisz and partial summation;
- Matomäki--Radziwiłł--Tao's averaged shifted-prime theorem in the range beginning at exponent `8/33+epsilon`.

Source-backed inputs:

- Yang--Yang's locked dilated sums `S_i(alpha)` and its simultaneous-major denominator target;
- the public reproduction convention `|q gamma-a|<=P/Y` in `common.py::arc_quality` / `face_arcs.py`;
- the covered-zone requirement that both prime-sum lengths reach the MRT range.

Previously established Mathia input:

- WI-034 for the almost-all-shifts to structured-`L^2` aggregation;
- WI-035 for exact denominator contraction, the simultaneous-center lemma conditional on collar separation, and the reduced-denominator Siegel--Walfisz law.

New exact deduction recorded here:

\[
\boxed{
P^2\left(\frac{b_2}{Y_1}+\frac{b_1}{Y_2}\right)
\asymp
P^2\left(\frac1{M_1}+\frac1{M_2}\right)=o(1)
}
\]

on the covered zone. This identifies the advertised smoothing-collar compatibility as a consequence of already-present scale hypotheses rather than a new arithmetic input. A bounded audit of the existing `weil_inertia` findings found no earlier statement of this cancellation. No priority claim is made from absence of a matching formulation.

## 7. Falsification tests

Reject or narrow this finding if any of the following fails.

1. Verify from the public reproduction that the analytic collar uses the same `|q gamma-a|<=P/Y` normalization as `pipeline/common.py::arc_quality`; a materially wider analytic collar would need a new calculation.
2. Verify the locked-cell localization keeps `Y_1/Y_2` between fixed constants independent of `T`; an unbounded mismatch would destroy (11).
3. Verify that every cell called `covered` has both prime-sum lengths in the MRT range (1), not merely one of them.
4. Track the index swap in the public face (`b_2 m` versus `b_1 n`): equations (9)--(14) are symmetric, but mixing the labels without swapping the cross multipliers would be an error.
5. Keep all uncovered/low-zone claims out of this conclusion; the present power saving deliberately comes from the covered-zone lower bound on `M_i`.

## 8. Consequence for `weil_inertia`

The one-sided fourth-moment audit has now removed three successive apparent obstacles without new conjectural arithmetic: WI-034 derives the needed structured `L^2` control from published MRT, WI-035 reduces the two-modulus major arcs to ordinary denominator contraction, and WI-037 shows that the public Gallagher collar automatically meets the separation and phase-variation hypotheses on exactly the same zone where MRT is available.

The next high-value target is no longer the collar geometry. It is the **uncovered/low-zone plus welding/remainder ledger** that promotes the covered-zone prime-correlation estimate into a uniform bound for `R(1)`. WI-028 shows that this ledger need only close at the coarse level `R(1)<0.0380703...` to beat the current theorem, so there remains substantial numerical slack if the missing asymptotic interfaces can be made fail-closed.