# MC-497 — Quadratic short-overlap bias requires exceptional interval starts

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces incomplete repeated-residue cross-root interference to a weighted sum against the fixed conductor phase

\[
R(t)=\chi(1-t^{-2}),
\]

with the zero/singular conductor classes handled by the original character factors. `MC-496` shows that endpoint-only overlap intervals of length much larger than `p^{1/2}\log p` cannot create order-one bias by the classical completion bound. In the quadratic-character case, the remaining short-overlap branch has a further exact restriction: **large interval bias is possible only at a sparse exceptional set of interval starts.**

Let `p>3` be prime and let `chi` be the quadratic character modulo `p`. Define the exact cross-root phase on `F_p` by

\[
R(0)=0,
\qquad
R(t)=\chi(1-t^{-2})\quad(t\ne0),
\tag{1}
\]

and let

\[
\mu_R=\frac1p\sum_{t\bmod p}R(t)
=-\frac{1+\chi(-1)}p.
\tag{2}
\]

For `1<=H<=p` and `x in F_p`, put

\[
S_x(H)=\sum_{j=1}^{H}\bigl(R(x+j)-\mu_R\bigr),
\tag{3}
\]

where the interval is read cyclically modulo `p`. Then

\[
\boxed{
\frac1p\sum_{x\bmod p}|S_x(H)|^2
\ll H+\frac{H^2}{\sqrt p}.
}
\tag{4}
\]

Consequently, for every `eta>0`, if

\[
E_H(\eta)=\{x\bmod p:|S_x(H)|\ge \eta H\},
\]

then

\[
\boxed{
\frac{|E_H(\eta)|}{p}
\ll \frac1{\eta^2}\left(\frac1H+\frac1{\sqrt p}\right).
}
\tag{5}
\]

Thus as soon as `H -> infinity`, an order-one normalized endpoint bias is confined to a vanishing fraction of conductor starts, even when `H` is far below the worst-case Pólya--Vinogradov scale `sqrt(p) log p` used in `MC-496`.

This does **not** give a uniform short-interval bound. It instead converts the unresolved endpoint-only escape into a source-distribution requirement. For any finite collection of source intervals `J_i` with lengths `H_i`, conductor starts `x_i`, and nonnegative reconstruction weights `c_i`, write

\[
M=\sum_i c_iH_i,
\qquad
B=\sum_i c_i S_{x_i}(H_i).
\tag{6}
\]

If `|B|>=epsilon M`, then with `eta=epsilon/2`, at least an `epsilon/2` fraction of the weighted interval mass must lie on intervals satisfying

\[
|S_{x_i}(H_i)|\ge \frac\epsilon2 H_i.
\tag{7}
\]

Indeed, the complementary intervals contribute at most `(epsilon/2)M`, while every interval is trivially bounded by its length. Therefore a quadratic endpoint-only mechanism below the `MC-496` completion threshold must make the **actual first-exit overlap starts concentrate on the exceptional conductor sets `(5)`**. Merely producing many short overlaps is not enough.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Quadratic specialization exposes a Legendre autocorrelation

For `t ne 0`, quadraticity removes the denominator square:

\[
R(t)=\chi(t^2-1)=\chi(t-1)\chi(t+1).
\tag{8}
\]

Let

\[
Q(t)=\chi(t^2-1)
\tag{9}
\]

for all `t in F_p`. Then `sum_t Q(t)=-1`, while `R` differs from `Q` only at `t=0`, where `Q(0)=chi(-1)` and `R(0)=0`. Thus `R-mu_R` differs from `Q+1/p` by one centered point mass. Its contribution to the interval-start mean square is `O(H)` and does not change the scale in `(4)`.

The representation `(8)` is useful because it turns the rational phase into the lag-two aperiodic correlation of the Legendre character sequence. This is a strictly better representation for the current question than treating `chi(1-t^{-2})` as a generic rational function: interval-start averaging becomes a four-point complete character correlation.

## 2. Complete shifted correlations give the second moment

For `d in F_p`, define

\[
C(d)=\sum_{t\bmod p}Q(t)Q(t+d).
\tag{10}
\]

At `d=0`,

\[
C(0)=p-2.
\tag{11}
\]

For `d ne 0, plusminus 2`, the product

\[
(t^2-1)((t+d)^2-1)
\]

has four distinct roots and is not a square, so the classical Weil bound gives

\[
C(d)=O(\sqrt p).
\tag{12}
\]

For `d=plusminus2`, one root is doubled; removing the square factor leaves a nondegenerate quadratic character sum, so in fact `C(d)=O(1)`. Hence `(12)` holds uniformly for every nonzero `d`.

Centering `Q` changes each complete correlation only by `O(1/p)`. Expanding the square in an interval of length `H` therefore gives

\[
\sum_{x\bmod p}
\left|\sum_{j=1}^{H}(Q(x+j)+1/p)\right|^2
\ll pH+\sqrt p\,H^2.
\tag{13}
\]

Adding the centered one-point defect from `R-Q` proves `(4)`. Chebyshev immediately gives `(5)`.

The bound is intentionally average-over-start rather than uniform. It says that the obstruction below the completion threshold cannot be generic endpoint geometry; it must be arithmetic concentration of the source starts on the exceptional set.

## 3. Weighted endpoint consequence

Take the exact endpoint-only expansion from `MC-496` after grouping one root-pair contribution into its interval intersections. The weights multiplying those interval sums are nonnegative. Centering contributes only `mu_R M=O(M/p)`, so an order-one negative cross-root term requires an order-one centered aggregate `B` as in `(6)`.

Split the intervals into good and bad according to `(7)`. The good contribution has absolute value at most `(epsilon/2)M`. If the total has size at least `epsilon M`, the bad intervals must therefore carry weighted length mass at least `(epsilon/2)M`. Equation `(5)` says that, at any fixed length `H`, the available bad starts occupy only

\[
O_\epsilon\left(p/H+\sqrt p\right)
\tag{14}
\]

residue classes.

This is the new proof obligation. A surviving source mechanism must show that the exact first-exit endpoint map sends a substantial fraction of its reconstruction mass into those rare classes, or else use the lower-prime pair-sieve/internal arithmetic or a genuinely `q`-dependent pre-aggregation sign/phase that lies outside the endpoint-only model.

## 4. Why ordinary Burgess is not a free replacement

There is a tempting but invalid shortcut: apply the classical Burgess bound for `sum chi(n)` to `(8)` and declare the short branch closed at the `p^(1/4+epsilon)` scale. The variable change

\[
u=\frac{t-1}{t+1}
\tag{15}
\]

indeed gives, away from the exceptional points,

\[
\chi(t^2-1)=\chi(u)
\tag{16}
\]

for quadratic `chi`, because the remaining factor is a square. But an additive interval in `t` becomes a fractional-linear image in `u`, not an additive interval. The ordinary one-dimensional Burgess theorem therefore does not transfer by this coordinate change.

The literature boundary is consistent with that distinction. Mauduit and Sárközy's classical Legendre-sequence work (*Acta Arithmetica* 82 (1997), 365--377, DOI `10.4064/aa-82-4-365-377`) and subsequent pseudorandom-sequence literature give the familiar `O(sqrt(p) log p)` worst-case aperiodic-correlation scale. Rena Chu's recent *Short character sums of inhomogeneous polynomials* (arXiv:`2609.04092`, submitted 3 September 2026) explicitly notes that nontrivial short bounds for one-variable inhomogeneous polynomial character sums remain open in general, giving `X^2+1` as an example. That statement does **not** prove that the special reducible polynomial `X^2-1` is itself an open case, and the present finding makes no such claim. A targeted audit did not identify a theorem that supplies a Burgess-scale worst-case bound for this exact shifted Legendre autocorrelation.

So `(4)`--`(5)` should not be read as a substitute for a missing uniform theorem. Their value is different: they prove that the only short endpoint intervals capable of mattering are exceptional starts, and they quantify how sparse those starts are.

## Prior art and novelty boundary

- Complete quadratic and quartic character-sum bounds used in `(10)`--`(13)` are classical Weil theory; no novelty is claimed.
- Mean-square expansion over interval starts and Chebyshev are classical harmonic/probabilistic bookkeeping.
- Aperiodic Legendre autocorrelation and higher correlation measures are established pseudorandom-sequence topics; the classical worst-case `sqrt(p) log p` scale predates this line.
- Chu's 2026 result is cited only as a boundary on importing a generic inhomogeneous-polynomial Burgess theorem. It is not evidence that this special polynomial has no stronger theorem.
- The durable Mathia delta is the specialization of those classical ingredients to the exact `MC-495` cross-root phase and the resulting **source-frame admission condition**: below the `MC-496` completion threshold, endpoint-only cancellation requires weighted concentration of actual first-exit interval starts on the exceptional sets `(5)`.

## Boundaries and falsification tests

- **Quadratic character only.** The identity `(8)` and the especially clean autocorrelation calculation use `chi^2=1`. Higher-order characters need their own shifted-rational correlation audit.
- **Average over conductor starts, not a maximum.** A single adversarial start may still have a large short sum. This finding cannot close the short-overlap branch without source information on where its starts land.
- **Endpoint-only model.** Internal pair-sieve variation inside the overlap interval, or a source-derived `q`-dependent sign/phase before aggregation, is intentionally outside the theorem.
- **Cyclic conductor intervals.** Integer intervals of length at most `p` descend to this model after reduction modulo `p`; endpoint defects at the singular classes change only `O(1)` terms.
- **No independence assumption.** Equation `(5)` is deterministic. Conversely, treating first-exit starts as random without proving a source-distribution statement would add an unsupported hypothesis.
- **Worst-case Burgess remains unimported.** Any future use of a sub-square-root uniform estimate must cite a theorem whose hypotheses cover the exact shifted-product/rational phase, not merely ordinary `sum chi(n)`.

## Consequence for the research line

The endpoint-only loophole from `MC-496` is now split cleanly. Long overlaps are uniformly harmless by completion; short overlaps can be dangerous only if the exact source endpoint map concentrates reconstruction mass on a sparse exceptional set of conductor starts. The next meaningful endpoint calculation is therefore **not another generic character-sum estimate**: it is the distribution, with the true first-exit weights retained, of the start residues of the overlap intervals relative to the exceptional sets in `(5)`.

If that source map is sufficiently dispersed, the endpoint-only branch closes even below the Pólya--Vinogradov threshold. If it is not, the concentration pattern itself becomes a concrete arithmetic object to explain. In parallel, the lower-prime pair-sieve profile and genuinely `q`-dependent pre-aggregation asymmetry remain independent live channels.