# WI-034 — MRT almost-all shifts implies the structured `L^2` aggregation used by the one-sided route

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + NEEDS-AUDIT`. This finding closes a specific provenance/audit subproblem left open in WI-033. Matomäki--Radziwiłł--Tao Theorem 1.3(i) is an almost-all-shifts pointwise theorem, not literally the `L^2` variance proposition printed in the Yang--Yang candidate. Nevertheless, in the same long-shift range it implies the required unweighted `L^2` estimate by a good/bad-shift decomposition, and the source's structured multiplicity transfer `nu(h) <= tau(h)` then follows with its advertised arbitrary logarithmic saving. This does **not** certify the full one-sided fourth-moment theorem, change Mathia's current unconditional simple-critical proportion, or repair WI-003's separate higher-moment cell-truncation gap.

## 1. Exact primary theorem and source claim

The primary arithmetic source is

Kaisa Matomäki, Maksym Radziwiłł and Terence Tao, *Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges*, Proc. London Math. Soc. 118 (2019), 284--350, DOI `10.1112/plms.12181`, arXiv:1707.01315v3.

Their Theorem 1.3(i) states the following. Put

\[
\sigma=\frac{8}{33}.
\]

For fixed `A>0`, `0<epsilon<1/2`,

\[
X^{\sigma+\varepsilon}\le H\le X^{1-\varepsilon},
\qquad
0\le h_0\le X^{1-\varepsilon},
\tag{1}
\]

one has

\[
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)
=\mathfrak S(h)X+O_{A,\varepsilon}(X\log^{-A}X)
\tag{2}
\]

for all but

\[
O_{A,\varepsilon}(H\log^{-A}X)
\tag{3}
\]

integers `h` with `|h-h0|<=H`.

The pinned Yang--Yang source

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`

prints, in the one-sided fourth-moment section, a proposition labelled

`[MRT, Thm. 1.3(i)], variance form`

asserting instead

\[
\sum_{|h-h_0|\le H}
\left|
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)-\mathfrak S(h)X
\right|^2
\ll_{A,\varepsilon}HX^2\log^{-A}X.
\tag{4}
\]

Equation (4) is **not the verbatim statement of MRT Theorem 1.3(i)**. The issue is one of provenance rather than truth: (4) is an elementary corollary of (2)--(3), as shown next.

Primary URLs:

- https://arxiv.org/abs/1707.01315
- https://doi.org/10.1112/plms.12181
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex

## 2. Almost-all pointwise control gives the needed unweighted `L^2` estimate

For nonzero `h`, write

\[
D_X(h)=
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)-\mathfrak S(h)X.
\tag{5}
\]

There is a uniform crude bound in the range `|h|<=X`:

\[
|D_X(h)|\ll X\log^2 X.
\tag{6}
\]

Indeed, each von Mangoldt factor is at most `O(log X)` on the relevant support, so the correlation is `O(X log^2 X)`. The classical formula

\[
\mathfrak S(h)=
2\Pi_2\prod_{p\mid h,\ p>2}\frac{p-1}{p-2}
\tag{7}
\]

for even nonzero `h` (and zero for odd `h`) gives the much smaller standard bound `mathfrak S(h) << log log(3|h|)`, so its main term is absorbed by (6). If a bookkeeping convention includes `h=0`, that single shift may be bounded crudely and is negligible because `H` is a fixed positive power of `X`; the Yang structured shifts themselves have `k != 0`.

Now request MRT Theorem 1.3(i) with logarithmic exponent `B`, to be chosen after the desired `L^2` exponent `A`. There are `O(H)` good shifts with

\[
|D_X(h)|\ll X\log^{-B}X
\]

and only `O(H log^{-B}X)` bad shifts. Therefore

\[
\begin{aligned}
\sum_{|h-h_0|\le H}|D_X(h)|^2
&\ll
HX^2\log^{-2B}X
+H\log^{-B}X\,X^2\log^4X\\
&=HX^2\left(\log^{-2B}X+\log^{4-B}X\right).
\end{aligned}
\tag{8}
\]

Taking, for example, `B=A+5` gives

\[
\boxed{
\sum_{|h-h_0|\le H}|D_X(h)|^2
\ll_{A,\varepsilon}HX^2\log^{-A}X.
}
\tag{9}
\]

Thus the Yang proposition is a valid derived `L^2` form in the exact MRT range (1), even though the citation should be read as `MRT Theorem 1.3(i) + good/bad decomposition`, not as a quotation of the theorem statement.

## 3. The structured multiplicity loss is only logarithmic

The next Yang lemma considers structured shifts `h=qk`. If `Q` is any set of moduli and `K_q<=H/q`, the structured square sum can be written

\[
\sum_{q\in Q}\sum_{k\le K_q}|D(qk)|^2
=
\sum_{h\le H}\nu(h)|D(h)|^2,
\tag{10}
\]

where the multiplicity satisfies the exact elementary bound

\[
\nu(h)\le\tau(h).
\tag{11}
\]

Let

\[
V=(\log X)^C.
\]

On the generic set `nu(h)<=V`, (9) with an arbitrarily stronger exponent `A'` gives

\[
\sum_{\nu(h)\le V}\nu(h)|D(h)|^2
\le
V\sum_{h\le H}|D(h)|^2
\ll HX^2\log^{C-A'}X.
\tag{12}
\]

There is therefore no modulus-count loss beyond a selectable power of `log X`.

For the rare set, the source uses its pointwise upper-bound-sieve envelope

\[
|D(h)|\le 9\,\mathfrak S(h)X
\tag{13}
\]

and the standard divisor-square tail. The line suppressed in the manuscript is harmless but worth making explicit: from (7),

\[
\mathfrak S(h)\ll\log\log(3h),
\qquad
\mathfrak S(h)^2\ll\log X
\tag{14}
\]

uniformly for `h<=H<=X`, once `X` is large. Also

\[
\sum_{h\le H,\ \tau(h)>V}\tau(h)
\le
\frac1V\sum_{h\le H}\tau(h)^2
\ll \frac{H(\log H)^3}{V}.
\tag{15}
\]

The last estimate is the classical second moment of the divisor function. If one wants to avoid its sharp logarithmic degree entirely, the identity

\[
\sum_{n\ge1}\frac{\tau(n)^2}{n^s}
=\frac{\zeta(s)^4}{\zeta(2s)}
\qquad(\Re s>1)
\tag{16}
\]

and Rankin's trick already give the weaker `O(H log^4 H)`, which is still enough after increasing `C` by one.

Using (13)--(15),

\[
\begin{aligned}
\sum_{\nu(h)>V}\nu(h)|D(h)|^2
&\ll
X^2\sum_{\tau(h)>V}\tau(h)\mathfrak S(h)^2\\
&\ll
HX^2\frac{\log^4X}{V}.
\end{aligned}
\tag{17}
\]

Therefore the source choices

\[
C=A+4,
\qquad
A'=2A+4
\tag{18}
\]

indeed yield, from (12) and (17),

\[
\boxed{
\sum_{q\in Q}\sum_{k\le K_q}|D(qk)|^2
\ll_A HX^2\log^{-A}X,
}
\tag{19}
\]

uniformly in the set `Q`. With the self-contained Rankin version of (15), replace `C=A+4` by `C=A+5`; the conclusion is unchanged.

The important point is structural: **a divisor-bounded concentration of the structured shifts cannot defeat an arbitrary logarithmic saving from MRT**. No factor comparable to the moduli survives the aggregation.

## 4. What this does and does not close

This finding closes two narrow questions in WI-033's upstream audit budget:

1. the hard-cutoff `L^2` shifted-prime variance used by the candidate really does follow from the published MRT almost-all-shifts theorem in the range `X^(8/33+epsilon)<=H<=X^(1-epsilon)`;
2. once that unweighted `L^2` estimate is available for arbitrary logarithmic exponent, the `h=qk` structured family with multiplicity `nu<=tau` inherits the same arbitrary logarithmic saving.

It does **not** establish the complete transport from the zeta fourth trace to the deterministic singular-series core. In particular, this finding has not independently verified:

- that every smooth/windowed deviation consumed after the Yang smoothing-collar step is reduced to (9) with no extra range or endpoint loss;
- the two-modulus major-arc discharge and its claimed `b`-uniformity;
- the exact dispersion-swaps identity in the normalization ultimately entering `R(1)`;
- the bridge/gluing weight, Abel summation, and minor-arc envelopes at all cells actually retained;
- the final finite zone/remainder ledger.

Those remain outside the established conclusion. WI-030--WI-033 concern the deterministic side after such a transport has been justified; WI-028's scalar consumer may still only be invoked after a rigorous bound on the actual `R(1)` is obtained.

## 5. Relation to WI-003

WI-003 concerns the **different higher-moment cell-truncation mechanism** in the Yang--Yang moment tower: a global `ell_1` is reused as though it were a cell-dependent arithmetic modulus. Nothing here repairs that mismatch.

The present one-sided route was introduced precisely as a logically independent fourth-moment bound. Its relevant arithmetic input is the long-shift averaged Hardy--Littlewood theorem plus the structured-shift/dispersion architecture above. Certifying this MRT-to-`L^2` sublayer therefore strengthens the independent one-sided route without upgrading the separate claimed exact moment tower.

## 6. Prior-art and novelty assessment

MRT Theorem 1.3(i), the singular-series formula and bounds, divisor-function second moments, and the implication `almost all + crude pointwise bound => L^2` are classical/literature consequences. The Yang--Yang source already contains the structured-to-full lemma, the multiplicity bound `nu<=tau`, and the generic/rare split. **No novelty is claimed for that architecture.**

The Mathia contribution is an audit/provenance reconstruction:

- identify that the source's displayed “variance form” is a corollary rather than the literal statement of MRT Theorem 1.3(i);
- derive that corollary with explicit logarithmic budgets;
- restore the suppressed `mathfrak S(h)^2` factor in the rare-shift estimate and verify that the source's `C=A+4` budget can absorb it using the classical `mathfrak S(h)^2 << log X` bound;
- separate this now-closed arithmetic sublayer from the still-open smoothing, two-modulus, gluing, and final-ledger interfaces.

This is an audit closure, not a new theorem about prime correlations and not a priority claim.

## 7. Decisive audit tests

Reject or narrow this finding if any of the following fails.

1. Compare MRT Theorem 1.3(i) directly with (2)--(3), including the exponent `8/33`, the upper range `H<=X^(1-epsilon)`, and the movable center `h0`.
2. Reproduce (8) from the exceptional-set count and the crude pointwise bound without assuming an `L^2` theorem not present in MRT.
3. Verify in the exact Yang structured family that every represented shift satisfies `h=qk<=H` and that its multiplicity is at most `tau(h)`.
4. Restore the factor `mathfrak S(h)^2` in the rare-shift argument and verify (14)--(17); do not silently treat the singular series as uniformly bounded.
5. Keep the smoothing-collar/two-modulus/gluing layer outside the conclusion until its hypotheses have independently been matched to (9).

## 8. Consequence for `weil_inertia`

The one-sided fourth-moment route has one fewer genuinely analytic unknown than WI-033 recorded. The published MRT input is strong enough for the **hard-window variance and structured multiplicity aggregation**; the remaining load is now localized further downstream, at the exact interface between the Yang two-modulus/smoothing/gluing construction and that variance estimate, followed by the final remainder ledger.

This does not yet justify a new numerical bound, so Mathia's current unconditional theorem remains unchanged. But it removes a plausible failure mode of the independent `R(1)` route without borrowing the unresolved higher-moment truncation from WI-003.