# WI-185 — the support-one Montgomery form factor has a square-root bow-visibility barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

WI-183--WI-184 identify the Maynard--Pratt bow as a serious source-compatible obstruction and show that functional-equation symmetrization does not remove its reciprocal horizontal signal: a long count-compatible symmetrized bow has a coherent reciprocal alias at `alpha<=1/2` (and, in the count-saturating `c=4 pi` geometry, also at the second reciprocal harmonic `alpha=1`). Those findings leave the extraction of that selected amplitude from the complete Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSTB) square as the apparent next gate.

There is a more basic scale obstruction. The exact Montgomery weight

\[
W(u)=\frac{4}{4-u^2}
\]

makes the self-form of a polynomially long bow only **linear in its number of sites times `log T`**, rather than quadratic in the number of sites. For a mirror-closed bow with `m` ordinate sites, spacing `c/log T` with fixed `c>0`, and all selected real parts in `[1/4,3/4]`, its complete principal BGSTB form satisfies uniformly for `0<=alpha<=1`

\[
\boxed{
0\le \mathcal F_{\rm bow}(T^\alpha)
\ll_c m(\log T)T^{\alpha/2}
\le m(\log T)T^{1/2}.
}
\tag{1}
\]

After the natural Montgomery normalization `\mathcal N_T=(T/(2 pi))\log T`,

\[
\boxed{
\frac{\mathcal F_{\rm bow}(T^\alpha)}{\mathcal N_T}
\ll_c mT^{\alpha/2-1}
\le mT^{-1/2}.
}
\tag{2}
\]

Hence every Maynard--Pratt bow of length

\[
m=T^\varepsilon,\qquad 0<\varepsilon<\frac12,
\]

has **vanishing complete principal support-one form even if it could be extracted with no external cancellation at all**:

\[
\sup_{0\le\alpha\le1}
\frac{\mathcal F_{\rm bow}(T^\alpha)}{\mathcal N_T}
\ll_c T^{\varepsilon-1/2}=o(1).
\tag{3}
\]

Moreover the current corrected BGSTB Montgomery theorem has a bulk uncertainty `O(T sqrt(log T))`. Equation (1) lies below even that theorem-statement resolution uniformly on support one whenever

\[
\boxed{m=o\!\left(\sqrt{T/\log T}\right).}
\tag{4}
\]

Thus the `T^epsilon` bows used by Maynard--Pratt with any fixed `epsilon<1/2` are not merely vulnerable to external cancellation: their **entire selected weighted quadratic form is sub-resolution at the global Montgomery scale**. This closes the route “extract one bow's support-one principal form and compare it to the global form-factor budget” as an RH-facing mechanism for such bows. A successful continuation must change scale or information: obtain a genuinely local/short-height normalization, aggregate enough bow mass, exploit non-principal coupling to the reservoir, or justify stronger Fourier support/new arithmetic information.

## 1. Literature-backed bow and form-factor objects

Maynard and Pratt introduce in Section 8 of *Half-isolated zeros and zero-density estimates* a potential bad configuration consisting of `T^epsilon` zeros with ordinates in an arithmetic progression of step

\[
\frac{c}{\log T},\qquad c>0\text{ absolute},
\tag{5}
\]

while the real parts ramp from `1/2` to `3/4`, remain at `3/4`, and ramp back. They explicitly emphasize that the cluster has only `T^epsilon` points and that their global clustering methods do not appear able to exploit such a short configuration. Their displayed model is schematic on one side of the critical line; as WI-183--WI-184 stress, an actual zeta configuration must also include the same-ordinate functional-equation mirrors. The mirror closure therefore lies in

\[
\boxed{\frac14\le\beta\le\frac34.}
\tag{6}
\]

The recent corrected BGSTB paper `arXiv:2501.14545v3` (last revised 1 Sep 2026) defines on the dyadic zero set `\mathcal Z(T)`

\[
\mathcal F(x,T)
=\sum_{\rho,\rho'\in\mathcal Z(T)}
 x^{\rho-\rho'}W(\rho-\rho'),
\qquad
W(u)=\frac4{4-u^2},
\tag{7}
\]

and proves uniformly for `1<=x<=T`

\[
\mathcal F(x,T)
=\frac{T}{2\pi x^2}
\bigl((\log T)^2+O((\log T)^{3/2})\bigr)
+\frac{T}{2\pi}\log x
+O(T\sqrt{\log T}).
\tag{8}
\]

Their Lemma 1 gives the positive squared-modulus representation of (7), and their equation (3.8) records the corresponding decay of `W` with vertical separation. The estimate below can in fact be proved directly from the explicit rational kernel, with no hidden arithmetic input.

Primary sources checked in this pass:

- James Maynard and Kyle Pratt, **Half-isolated zeros and zero-density estimates**, *International Mathematics Research Notices* (2024), arXiv:2206.11729v2, especially Section 8, equation (22), and the discussion immediately following it: https://arxiv.org/abs/2206.11729.
- S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, **Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros**, arXiv:2501.14545v3, revised 1 Sep 2026, especially (3.1)--(3.8): https://arxiv.org/abs/2501.14545.

No informal summary is used as evidence for (5)--(8).

## 2. Exact decay of the Montgomery weight on a symmetrized bow

Let the `m` selected ordinate sites be

\[
\gamma_j=\gamma_0+\frac{cj}{L},
\qquad 1\le j\le m,
\qquad L:=\log T,
\tag{9}
\]

and select at most the functional-equation mirror pair at each site. Thus there are at most two selected zero labels per ordinate and every selected real part obeys (6).

Write

\[
a:=\beta-\beta',\qquad v:=\gamma-\gamma'.
\]

Then `|a|<=1/2`, and the explicit kernel gives

\[
\begin{aligned}
|W(a+iv)|
&=\frac4{|4-(a+iv)^2|}\\
&\le \frac4{4-a^2+v^2}\\
&\le \frac{16}{15+4v^2}\\
&\le \frac{16}{15}\,\frac4{4+v^2}.
\end{aligned}
\tag{10}
\]

Put

\[
w(v):=\frac4{4+v^2}.
\]

For the ordinate lattice (9), monotonicity of `w` and the elementary integral

\[
\int_0^\infty \frac4{4+u^2}\,du=\pi
\tag{11}
\]

give

\[
\begin{aligned}
\sum_{j,k=1}^m
w\!\left(\frac{c(j-k)}L\right)
&=m+2\sum_{r=1}^{m-1}(m-r)
 w\!\left(\frac{cr}L\right)\\
&\le m\left(1+2\sum_{r=1}^\infty
 w\!\left(\frac{cr}L\right)\right)\\
&\le
\boxed{
m\left(1+\frac{2\pi L}{c}\right).
}
\end{aligned}
\tag{12}
\]

This is the load-bearing scale change. A raw reciprocal-lattice amplitude can be quadratic in `m`, but the BGSTB/Montgomery quadratic form is not an unweighted square of the whole bow. The kernel `W` has physical vertical correlation length `O(1)`, which contains only `O(L)` sites of a bow spaced by `c/L`. Consequently its full principal pair mass is `O(mL)`.

For a genuinely source-compatible long symmetrized bow, WI-184's Riemann--von Mangoldt count further forces `c>=4 pi-o(1)`. Inserting that fact into (12) only improves the constant to

\[
\sum_{j,k}w(\gamma_j-\gamma_k)
\le (1/2+o(1))mL;
\tag{13}
\]

no part of the square-root exponent below depends on this sharpening.

## 3. Uniform support-one visibility bound

Let `\mathcal B_T` denote the selected mirror-closed bow submultiset and define its principal form by restricting both indices in (7):

\[
\mathcal F_{\mathcal B}(x)
:=\sum_{\rho,\rho'\in\mathcal B_T}
 x^{\rho-\rho'}W(\rho-\rho').
\tag{14}
\]

Because `\mathcal B_T` is closed under `rho -> 1-\bar rho`, the same algebra as BGSTB Lemma 1 gives a squared-modulus representation for (14), hence

\[
\mathcal F_{\mathcal B}(x)\ge0.
\tag{15}
\]

For `x=T^alpha`, `0<=alpha<=1`, equation (6) gives

\[
|x^{\rho-\rho'}|
=x^{\beta-\beta'}
\le T^{\alpha/2}.
\tag{16}
\]

There are at most four ordered zero-label pairs above every ordered pair of ordinate sites. Therefore (10), (12), and (16) imply the explicit bound

\[
\boxed{
0\le\mathcal F_{\mathcal B}(T^\alpha)
\le
\frac{64}{15}
T^{\alpha/2}
 m\left(1+\frac{2\pi L}{c}\right).
}
\tag{17}
\]

For fixed `c>0`, this is (1). Under the source-compatible `c>=4 pi-o(1)` specialization it becomes

\[
\mathcal F_{\mathcal B}(T^\alpha)
\le
\left(\frac{32}{15}+o(1)\right)mLT^{\alpha/2}.
\tag{18}
\]

Normalize by

\[
\mathcal N_T=\frac{T}{2\pi}L.
\tag{19}
\]

Equations (17)--(19) give

\[
\boxed{
\sup_{0\le\alpha\le1}
\frac{\mathcal F_{\mathcal B}(T^\alpha)}{\mathcal N_T}
\ll_c\frac{m}{\sqrt T}.
}
\tag{20}
\]

Thus a `T^epsilon` bow with any fixed `epsilon<1/2` occupies an asymptotically invisible principal sector of the globally normalized support-one form factor.

## 4. The current arithmetic theorem cannot resolve such a bow either

At the most favorable support-one endpoint `alpha=1`, the first spike in (8) is negligible and the corrected theorem reads

\[
\mathcal F(T,T)
=\frac{T}{2\pi}L+O(T\sqrt L).
\tag{21}
\]

Equation (18) gives for the **entire** selected bow principal form

\[
\mathcal F_{\mathcal B}(T)
\ll mL\sqrt T.
\tag{22}
\]

Therefore

\[
\frac{\mathcal F_{\mathcal B}(T)}{T\sqrt L}
\ll
\frac{m\sqrt L}{\sqrt T}.
\tag{23}
\]

If `m=o(sqrt(T/L))`, then

\[
\boxed{
\mathcal F_{\mathcal B}(T)=o(T\sqrt L),
}
\tag{24}
\]

so the entire principal form is smaller than the published theorem's bulk error budget. The same conclusion is uniform over `0<=alpha<=1` from the coarse uniform `O(T sqrt L)` term in (8), since (17) is maximized at `alpha=1`; near `alpha=0` the separate spike uncertainty only enlarges the theorem-statement envelope.

The source-level refinements in WI-161--WI-163 improve the arithmetic error away from the endpoint, but they do not change the polynomial visibility exponent: moving into the interior also reduces the maximum horizontal amplification `T^(alpha/2)`. The present finding does not claim that the source proof contains no still-unknown local statistic; it proves that the **global support-one principal-form comparison itself** has vanishing scale on sub-square-root bows.

For Maynard--Pratt's `m=T^epsilon`, any fixed `epsilon<1/2` satisfies (24) by a polynomial margin. In particular, taking `epsilon` small, as their obstruction discussion explicitly permits, makes the mismatch overwhelming rather than marginal.

## 5. Perfect extraction would still not be an RH mechanism at this scale

WI-124 and WI-184 correctly isolate an extraction problem: the selected bow can carry a coherent reciprocal amplitude while the complete BGSTB square permits cancellation by the rest of the zeta zeros. Equation (20) shows that removing this cancellation is **not sufficient** for the actual Maynard--Pratt scale.

Suppose, more strongly than anything currently proved, that one had a perfect positive extraction inequality at some support-one frequency,

\[
\mathcal F(T^\alpha,T)
\ge \mathcal F_{\mathcal B}(T^\alpha).
\tag{25}
\]

The total left side has scale `Theta(TL)` for fixed positive `alpha`, while the right side is at most `O(mL sqrt T)`. For `m=o(sqrt T)` this gives only an `o(TL)` lower contribution and is completely compatible with the known total form-factor budget. Thus (25), even if proved, cannot exclude a single `T^epsilon` bow for `epsilon<1/2` by a global-size contradiction.

The same calculation applies to any bounded-`L^1` support-one portfolio. If `r_T` is supported in `[0,1]` with `||r_T||_1=O(1)`, then

\[
\int_0^1|r_T(\alpha)|
\mathcal F_{\mathcal B}(T^\alpha)\,d\alpha
\ll_c mL\sqrt T.
\tag{26}
\]

So moving profiles, finite positive mixtures, or an exact reciprocal-frequency selection do not change the square-root visibility scale while the principal block is measured through the same Montgomery weight and global normalization.

This is precisely the distinction required by the canonical research mandate: an asymptotic density or an `o(N)` defect is not an RH conclusion. A method that can see positive-density exceptional mass may still be incapable of excluding one sparse mesoscopic bow, let alone an individual off-critical pair.

## 6. General horizontal-width scale law

The calculation is not special to the numeric plateau `3/4`. Suppose a mirror-closed selected cluster has bounded ordinate multiplicity, spacing `gg 1/L`, and lies in

\[
|\beta-1/2|\le\delta,
\qquad 0<\delta<1/2.
\tag{27}
\]

Then `|beta-beta'|<=2delta`, so the same proof gives, for a support limit `0<=alpha<=A`,

\[
\boxed{
\mathcal F_{\mathcal B}(T^\alpha)
\ll mL T^{2\delta\alpha},
\qquad
\frac{\mathcal F_{\mathcal B}(T^\alpha)}{\mathcal N_T}
\ll mT^{2\delta\alpha-1}.
}
\tag{28}
\]

At bandwidth `A`, a principal-block global-size argument therefore has the visibility scale

\[
\boxed{m\asymp T^{1-2\delta A}.}
\tag{29}
\]

For the Maynard--Pratt bow, `delta=1/4` and the established arithmetic support is `A=1`, producing the square-root scale `m\asymp T^{1/2}`. Formally reaching `A=2` would reduce the polynomial threshold for this particular horizontal width to constant order, but support two is exactly outside the presently established unconditional Montgomery interface used by this line. For defects much closer to the critical line (`delta` small), even substantially wider fixed support would still leave a large sparse-defect threshold.

Equation (29) is a scale ledger, not an assertion that support extension alone solves extraction or RH. It identifies why the global pair form and the individual-exception objective naturally separate.

## 7. Stress tests and boundaries

**Montgomery-weight stress test.** The `mL` bound is not an artifact of replacing `W` by one on a long block. That replacement is valid only for physical vertical diameter `o(1)`, as in the `M=o(log T)` finite blocks of WI-120/WI-124. A Maynard--Pratt bow has `m=T^epsilon` sites and physical length `asymp m/L`, which diverges. For separations beyond `O(1)`, `W` decays quadratically; summing that decay is exactly what produces (12). Treating the whole bow as an unweighted coherent `m^2` square would be invalid.

**Multiplicity stress test.** The proof selects at most one functional-equation mirror pair at each bow ordinate. Extra multiplicity or additional zeros at the same ordinates are not silently treated as bow signal; they belong to the excess/multiplicity reservoir separated in WI-184. If multiplicity itself is large, that is an additional invariant and must be charged separately.

**Spacing stress test.** Only a fixed positive lower scale `c/L` is needed for (12). WI-184's stronger `c>=4 pi-o(1)` source-compatibility condition improves constants but is not needed for the exponent. If a proposed obstruction compresses many more sites into an `o(1/L)` spacing, it has left the Maynard--Pratt bow geometry and enters the overcrowding regime where independent number-variance/multiplicity inputs such as WI-121 become relevant.

**Signed-observable stress test.** The finding closes positive principal-form extraction followed by comparison with the global support-one budget. It does not prove that every signed transform of `\mathcal F` is useless. A signed observable that cancels the `Theta(TL)` background would also have to control its arithmetic error and would lose the simple principal-block positivity used in the extraction argument. Such a construction is genuinely different information and remains admissible if proved.

**Aggregate stress test.** Many bows can become visible in aggregate. Summing the within-bow principal bounds for disjoint selected bows with total `M_T` selected sites gives `O(M_T L sqrt T)` at support one. Thus the same theorem-statement resolution is still blind when `M_T=o(sqrt(T/L))`, but this finding does not obstruct arguments that prove a much larger total exceptional population. The RH-facing issue is exactly that the canonical mandate must also exclude zero-density and finite exceptional sets.

## 8. Prior-art audit and evidence boundary

The two analytic inputs are primary-source facts. Maynard--Pratt explicitly introduce `T^epsilon` bows and already state qualitatively that their short length defeats the global clustering gains available to their method. BGSTB supply the unconditional complex-zero form factor, its positive-square representation, its uniform support-one theorem, and the Montgomery weight used above. The `mL` summability calculation (10)--(20), the sub-square-root resolution threshold (23)--(24), and the general width/support ledger (28)--(29) are exact deductions from those inputs.

A targeted search in this pass covered combinations of “bow of zeros”, Maynard--Pratt, Montgomery pair correlation/form factor, short clusters, and the weight `4/(4-u^2)`. No source was located stating the specific principal-form bound (17), the `m~sqrt(T)` support-one visibility threshold, or its implication that perfect extraction of a single `T^epsilon` bow is insufficient. Absence from that search is not evidence of priority and no priority claim is made. The conceptual observation that global methods have poor leverage on short bows is explicitly Maynard--Pratt's; the durable Mathia delta is the exact **BGSTB/Weil-interface scale calculation** and its consequence for the WI-184 extraction program.

The current corrected BGSTB v3 is an unrefereed revision under review as of its 1 Sep 2026 arXiv version; equations (7)--(8) are treated as literature-backed primary-source statements, not as a peer-reviewed new theorem. The kernel algebra (10)--(20) is independently checkable and does not depend on the corrected lower-order terms.

## 9. Research implication

WI-184's lower-half alias remains mathematically real, but the RH-facing task must now be split into two distinct gates:

1. **extraction:** prevent or charge cancellation of a selected bow against the complementary zeta amplitude;
2. **scale:** after extraction, obtain an observable whose normalization makes a `T^epsilon`, `epsilon<1/2`, bow contribute a nonvanishing amount.

The existing global support-one Montgomery form factor fails the second gate even under hypothetical perfect success on the first. Therefore the next high-value search should not invest in a cancellation lemma that returns only the bow's ordinary principal BGSTB self-form. It should seek a **locally normalized short-height form factor/Weil form**, a source theorem that couples the bow to an extensive reservoir which can itself be charged, or genuinely stronger spectral/arithmetic information. A support-extension route is also meaningful, but equation (29) makes explicit how much support is needed as a function of horizontal depth and why near-line individual exceptions remain especially hard.

This is a decisive negative result for one important route, not a no-go theorem for Weil positivity or for all pair/higher-order observables. It leaves the established unconditional simple-critical proportion unchanged.